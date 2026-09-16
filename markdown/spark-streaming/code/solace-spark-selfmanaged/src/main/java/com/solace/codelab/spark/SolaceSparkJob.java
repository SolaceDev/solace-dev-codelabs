package com.solace.codelab.spark;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;

import java.util.concurrent.TimeoutException;

import static org.apache.spark.sql.functions.col;

/**
 * Self-managed Spark entry point for the Solace connector.
 * Configuration comes from environment variables so the same jar runs unchanged
 * across environments; see README.md for the full list and a sample spark-submit command.
 */
public class SolaceSparkJob {

    private static String env(String name, String defaultValue) {
        String value = System.getenv(name);
        return (value == null || value.isEmpty()) ? defaultValue : value;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isEmpty()) {
            throw new IllegalStateException("Required environment variable not set: " + name);
        }
        return value;
    }

    public static void main(String[] args) throws StreamingQueryException, TimeoutException {
        String host = requireEnv("SOLACE_HOST");
        String vpn = requireEnv("SOLACE_VPN");
        String username = requireEnv("SOLACE_USERNAME");
        String password = requireEnv("SOLACE_PASSWORD");
        String sourceQueue = requireEnv("SOLACE_SOURCE_QUEUE");
        String lvqName = requireEnv("SOLACE_LVQ_NAME");
        String lvqTopic = requireEnv("SOLACE_LVQ_TOPIC");
        String resultTopic = requireEnv("SOLACE_RESULT_TOPIC");
        String checkpointRoot = requireEnv("CHECKPOINT_ROOT");
        int partitions = Integer.parseInt(env("SOLACE_PARTITIONS", "0"));
        int batchSize = Integer.parseInt(env("SOLACE_BATCH_SIZE", "100"));

        SparkSession spark = SparkSession.builder()
                .appName("solace-spark-selfmanaged")
                .getOrCreate();

        Dataset<Row> source = spark.readStream()
                .format("solace")
                .option("sparkRuntimePlatform", "OTHER")
                .option("host", host)
                .option("vpn", vpn)
                .option("username", username)
                .option("password", password)
                .option("queue", sourceQueue)
                .option("lvq.name", lvqName)
                .option("lvq.topic", lvqTopic)
                .option("connectRetries", 2)
                .option("reconnectRetries", 3)
                .option("batchSize", batchSize)
                .option("partitions", partitions)
                .option("includeHeaders", true)
                .load();

        Dataset<Row> result = source.select(
                col("Id"),
                col("Topic"),
                col("Payload"),
                col("TimeStamp"));

        StreamingQuery query = result.writeStream()
                .format("solace")
                .option("sparkRuntimePlatform", "OTHER")
                .option("host", host)
                .option("vpn", vpn)
                .option("username", username)
                .option("password", password)
                .option("topic", resultTopic)
                .option("batchSize", batchSize)
                .option("publishAckTimeout", 5000)
                .option("publishAckTimeoutFailOnError", true)
                .outputMode("append")
                .option("checkpointLocation", checkpointRoot + "/solace-spark-selfmanaged")
                .start();

        query.awaitTermination();
    }
}
