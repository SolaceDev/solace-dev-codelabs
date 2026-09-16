# Code assets: Streaming between Solace and Databricks

Runnable companions to the [Streaming between Solace and Databricks](https://codelabs.solace.dev/codelabs/spark-streaming/index.html) codelab.

| Asset | Use it for |
|---|---|
| [`solace-databricks.py`](solace-databricks.py) | The primary asset. Steps 5-9 as a Databricks source-format notebook, import it directly into a Databricks workspace. Configuration is driven by widgets, not inline edits. |
| [`solace-spark-selfmanaged/`](solace-spark-selfmanaged/) | A Maven project with a `spark-submit` entry point for Appendix A, configured entirely through environment variables. See its README for the full `spark-submit` command. |
| [`publisher/publish_orders.py`](publisher/publish_orders.py) | Publishes sample order events to your source topic, so you have data flowing without standing up a second producer. |
| [`docker-compose.yml`](docker-compose.yml) | A Solace software broker plus a single-node Spark 3.5.2 container, for following along without a Databricks workspace. |

## Quick start with docker-compose

```bash
docker compose up -d
# Broker Manager: http://localhost:8080  (admin / admin)
# SMF: tcp://localhost:55555 (plaintext) or tcps://localhost:55443 (TLS)
```

Provision the source queue and Last Value Queue described in Step 3 of the codelab, then publish sample data:

```bash
pip install -r publisher/requirements.txt
python publisher/publish_orders.py \
  --host tcp://localhost:55555 --vpn default \
  --username admin --password admin \
  --topic solace/spark/stream/orders
```
