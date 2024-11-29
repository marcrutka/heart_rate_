import json
import time
import logging
import socket
import numpy as np
from datetime import datetime
from confluent_kafka import Producer

# Configuration
SERVER = 'localhost:9092'
KAFKA_TOPIC = 'heartrate'
LAG = 2

# Simulation parameters
HEART_RATE_PARAMS = {
    "main": {"mean": 72, "std_dev": 1.5, "size": 9000},
    "occasional": {"mean": 100, "std_dev": 2, "size": 1000}
}
MIN_VALUE, MAX_VALUE = 60, 120

# Creating Kafka producer
def create_producer(server):
    try:
        return Producer({
            "bootstrap.servers": server,
            "client.id": socket.gethostname(),
            "enable.idempotence": True,
            "batch.size": 64000,
            "linger.ms": 10,
            "acks": "all",
            "retries": 5,
            "delivery.timeout.ms": 1000
        })
    except Exception as e:
        logging.exception("Unable to create Kafka producer")
        return None

# Generating heart rate data
def generate_heart_rate(params, min_value, max_value):
    rates = []
    for key in params:
        p = params[key]
        rates.append(np.random.normal(p["mean"], p["std_dev"], p["size"]))
    combined_rates = np.concatenate(rates)
    return int(np.clip(np.random.choice(combined_rates), min_value, max_value))

# Main loop
def main():
    producer = create_producer(SERVER)
    if not producer:
        return
    
    print("Already working")

    while True:
        heart_rate = generate_heart_rate(HEART_RATE_PARAMS, MIN_VALUE, MAX_VALUE)
        data = json.dumps({
            "time": datetime.utcnow().isoformat(),
            "heart_rate": heart_rate
        }).encode("utf-8")

        try:
            producer.produce(topic=KAFKA_TOPIC, value=data)
            producer.flush()
        #    print(f"Sent: {data}")  # Logs
        except Exception as e:
            logging.error("Error sending data to Kafka", exc_info=True)

        time.sleep(LAG)

if __name__ == "__main__":
    main()

