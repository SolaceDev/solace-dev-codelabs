# Databricks notebook source
# MAGIC %md
# MAGIC # Solace and Databricks Structured Streaming
# MAGIC
# MAGIC Companion notebook for the [Streaming between Solace and Databricks](https://codelabs.solace.dev/codelabs/spark-streaming/index.html) codelab.
# MAGIC Covers Steps 5 through 9: read from Solace, checkpoint to a Unity Catalog Volume, publish back to Solace,
# MAGIC move credentials into Databricks secrets, and tune for throughput.
# MAGIC
# MAGIC Fill in the widgets below rather than editing values inline.

# COMMAND ----------

dbutils.widgets.text("host", "tcps://<host>:55443", "Solace SMF host")
dbutils.widgets.text("vpn", "default", "Message VPN")
dbutils.widgets.text("source_queue", "spark/orders/source", "Source queue")
dbutils.widgets.text("lvq_name", "spark/orders/lvq", "Last Value Queue name")
dbutils.widgets.text("lvq_topic", "spark/orders/lvq/offsets", "Last Value Queue topic")
dbutils.widgets.text("result_topic", "solace/spark/stream/processing/result", "Publish-back topic")
dbutils.widgets.text("secret_scope", "solace-dev-credentials", "Databricks secret scope")
dbutils.widgets.text("checkpoint_root", "/Volumes/main/default/checkpoints/spark-streaming", "UC Volume checkpoint root")

host = dbutils.widgets.get("host")
vpn = dbutils.widgets.get("vpn")
source_queue = dbutils.widgets.get("source_queue")
lvq_name = dbutils.widgets.get("lvq_name")
lvq_topic = dbutils.widgets.get("lvq_topic")
result_topic = dbutils.widgets.get("result_topic")
secret_scope = dbutils.widgets.get("secret_scope")
checkpoint_root = dbutils.widgets.get("checkpoint_root")

username = dbutils.secrets.get(scope=secret_scope, key="username")
password = dbutils.secrets.get(scope=secret_scope, key="password")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Read from Solace into a DataFrame

# COMMAND ----------

df = (spark.readStream
      .format("solace")
      .option("host", host)
      .option("vpn", vpn)
      .option("username", username)
      .option("password", password)
      .option("queue", source_queue)
      .option("lvq.name", lvq_name)
      .option("lvq.topic", lvq_topic)
      .option("connectRetries", 2)
      .option("reconnectRetries", 2)
      .option("batchSize", 100)
      .option("partitions", 1)
      .option("includeHeaders", True)
      .load())

display(df)

# COMMAND ----------

from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

order_schema = StructType([
    StructField("orderId", StringType()),
    StructField("customerId", StringType()),
    StructField("item", StringType()),
    StructField("amount", DoubleType()),
])

parsed = df.select(
    col("Id"),
    col("Topic"),
    col("TimeStamp"),
    from_json(col("Payload").cast("string"), order_schema).alias("order"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Checkpoint to a Unity Catalog Volume
# MAGIC
# MAGIC The `databricks*` options below are required only when `checkpointLocation` points at a UC Volume
# MAGIC (a path containing `Volumes`). They are **secret names inside the scope**, not literal values.

# COMMAND ----------

bronze_checkpoint = f"{checkpoint_root}/orders_bronze"

bronze_query = (parsed.writeStream
      .format("delta")
      .option("checkpointLocation", bronze_checkpoint)
      .option("sparkRuntimePlatform", "DATABRICKS")
      .option("databricksSecretScope", secret_scope)
      .option("databricksHost", "databricks-host")
      .option("databricksClientId", "databricks-client-id")
      .option("databricksClientSecret", "databricks-client-secret")
      .option("databricksClientSecretRefreshInterval", 1440)
      .toTable("orders_bronze"))

# COMMAND ----------

# MAGIC %md
# MAGIC **Exercise:** publish a few messages, confirm they land in `orders_bronze`, then run the cell below to stop the
# MAGIC stream, and re-run the cell above to restart it. Publish a few more messages and confirm no gap or duplicates.

# COMMAND ----------

# bronze_query.stop()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 7: Publish back to Solace

# COMMAND ----------

from pyspark.sql.functions import lit

result_df = parsed.select(
    col("Id"),
    lit(result_topic).alias("Topic"),
    col("order").cast("string").cast("binary").alias("Payload"),
    col("TimeStamp"))

publish_checkpoint = f"{checkpoint_root}/orders_published"

publish_query = (result_df.writeStream
         .format("solace")
         .option("host", host)
         .option("vpn", vpn)
         .option("username", username)
         .option("password", password)
         .option("topic", result_topic)
         .option("batchSize", 100)
         .option("publishAckTimeout", 5000)
         .option("publishAckTimeoutFailOnError", True)
         .outputMode("append")
         .option("checkpointLocation", publish_checkpoint)
         .start())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 9: Scale and operate
# MAGIC
# MAGIC A few settings worth trying against your own broker and cluster:
# MAGIC
# MAGIC - `partitions=0` on the read stream to track worker count automatically on an autoscaling cluster.
# MAGIC - Raise `batchSize` and, on the source queue, Maximum Delivered Unacknowledged Messages to twice that value.
# MAGIC - Add `replayStrategy` / `replayStartTime` options to reprocess from a point in time instead of republishing.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Cleanup

# COMMAND ----------

# bronze_query.stop()
# publish_query.stop()
