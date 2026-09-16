#!/usr/bin/env python3
"""
Publishes sample order events to a Solace topic, for the
Streaming between Solace and Databricks codelab
(https://codelabs.solace.dev/codelabs/spark-streaming/index.html).

Usage:
    python publish_orders.py --host tcps://<host>:55443 --vpn default \
        --username <user> --password <password> \
        --topic solace/spark/stream/orders --count 20 --interval 1.0
"""

import argparse
import json
import random
import time
import uuid

from solace.messaging.messaging_service import MessagingService
from solace.messaging.resources.topic import Topic
from solace.messaging.config.transport_security_strategy import TLS

ITEMS = ["widget", "gadget", "gizmo", "doohickey", "thingamajig"]


def build_order():
    return {
        "orderId": str(uuid.uuid4()),
        "customerId": f"cust-{random.randint(1000, 9999)}",
        "item": random.choice(ITEMS),
        "amount": round(random.uniform(5.0, 500.0), 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True, help="SMF host, e.g. tcps://<host>:55443")
    parser.add_argument("--vpn", required=True, help="Message VPN")
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--topic", default="solace/spark/stream/orders")
    parser.add_argument("--count", type=int, default=20, help="Number of messages to publish, 0 for unlimited")
    parser.add_argument("--interval", type=float, default=1.0, help="Seconds between messages")
    args = parser.parse_args()

    broker_props = {
        "solace.messaging.transport.host": args.host,
        "solace.messaging.service.vpn-name": args.vpn,
        "solace.messaging.authentication.scheme.basic.username": args.username,
        "solace.messaging.authentication.scheme.basic.password": args.password,
    }

    messaging_service = (MessagingService.builder()
                          .from_properties(broker_props)
                          .with_transport_security_strategy(TLS.create())
                          .build())
    messaging_service.connect()

    publisher = messaging_service.create_direct_message_publisher_builder().build()
    publisher.start()

    topic = Topic.of(args.topic)

    published = 0
    try:
        while args.count == 0 or published < args.count:
            order = build_order()
            payload = json.dumps(order).encode("utf-8")
            message = messaging_service.message_builder().build(payload)
            publisher.publish(message, topic)
            published += 1
            print(f"Published to {args.topic}: {order}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        pass
    finally:
        publisher.terminate()
        messaging_service.disconnect()
        print(f"Done. Published {published} message(s).")


if __name__ == "__main__":
    main()
