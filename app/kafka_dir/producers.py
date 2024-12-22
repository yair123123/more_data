import json
import os
import toolz as t
from kafka import KafkaProducer



@t.curry
def publisher(topic,key,value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    chunk_json = value.to_dict(orient="records")
    producer.send(os.environ[topic], chunk_json)
    print(f"Sent Chunk to Kafka: {chunk_json}")