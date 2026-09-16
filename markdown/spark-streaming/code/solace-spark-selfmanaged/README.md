# solace-spark-selfmanaged

Self-managed Spark entry point for the Solace connector, referenced from Appendix A of the
[Streaming between Solace and Databricks](https://codelabs.solace.dev/codelabs/spark-streaming/index.html) codelab.

Reads from a Solace queue and republishes to a Solace topic, with `sparkRuntimePlatform` set to `OTHER`
so the connector skips the Databricks Unity Catalog checkpoint path.

## Build

```bash
mvn clean package
```

## Configure

All configuration comes from environment variables:

| Variable | Required | Description |
|---|---|---|
| `SOLACE_HOST` | Yes | SMF host, e.g. `tcps://<host>:55443` |
| `SOLACE_VPN` | Yes | Message VPN |
| `SOLACE_USERNAME` | Yes | Client username |
| `SOLACE_PASSWORD` | Yes | Client password |
| `SOLACE_SOURCE_QUEUE` | Yes | Source queue name |
| `SOLACE_LVQ_NAME` | Yes | Last Value Queue name |
| `SOLACE_LVQ_TOPIC` | Yes | Last Value Queue topic |
| `SOLACE_RESULT_TOPIC` | Yes | Topic to publish results to |
| `CHECKPOINT_ROOT` | Yes | Shared filesystem path (S3, HDFS, NFS) for the checkpoint |
| `SOLACE_PARTITIONS` | No (default `0`) | Consumers per worker; `0` tracks the current worker count |
| `SOLACE_BATCH_SIZE` | No (default `100`) | Read/write batch size |

## Run

```bash
export SOLACE_HOST=tcps://<host>:55443
export SOLACE_VPN=default
export SOLACE_USERNAME=<username>
export SOLACE_PASSWORD=<password>
export SOLACE_SOURCE_QUEUE=spark/orders/source
export SOLACE_LVQ_NAME=spark/orders/lvq
export SOLACE_LVQ_TOPIC=spark/orders/lvq/offsets
export SOLACE_RESULT_TOPIC=solace/spark/stream/processing/result
export CHECKPOINT_ROOT=s3a://my-bucket/spark-checkpoints

spark-submit \
  --packages com.solacecoe.connectors:pubsubplus-connector-spark:3.1.7 \
  --conf spark.executor.instances=3 \
  --class com.solace.codelab.spark.SolaceSparkJob \
  target/solace-spark-selfmanaged.jar
```

For an air-gapped environment, replace `--packages` with `--jars /path/to/pubsubplus-connector-spark-3.1.7.jar`.
