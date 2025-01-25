from time import sleep
import random
# import json
# from kafka import KafkaProducer

# KAFKA_TOPIC = 'sensor-data'
# KAFKA_BROKER = 'localhost:9092'

# producer = KafkaProducer(
#     bootstrap_servers=KAFKA_BROKER,
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

def generate_weight_sensor_data():
    return {
        'sensor_type': 'weight',
        'value': round(random.uniform(0.5, 50.0), 2), 
        'unit': 'kg'
    }

def generate_lidar_sensor_data():
    return {
        'sensor_type': 'lidar',
        'distance': round(random.uniform(0.1, 10.0), 2), 
        'unit': 'm'
    }

def generate_peripheral_analytics_data():
    return {
        'sensor_type': 'peripheral_analytics',
        'activity': random.choice(['idle', 'active', 'error']),
        'timestamp': random.randint(1609459200, 1672444800) 
    }

def send_sensor_data():
    while True:
        weight_data = generate_weight_sensor_data()
        lidar_data = generate_lidar_sensor_data()
        peripheral_data = generate_peripheral_analytics_data()

        # producer.send(KAFKA_TOPIC, weight_data)
        # producer.send(KAFKA_TOPIC, lidar_data)
        # producer.send(KAFKA_TOPIC, peripheral_data)

        print(f"Sent data: {weight_data}")
        print(f"Sent data: {lidar_data}")
        print(f"Sent data: {peripheral_data}")

        sleep(5) 

if __name__ == "__main__":
    send_sensor_data()
