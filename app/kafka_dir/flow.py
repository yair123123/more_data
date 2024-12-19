import os
from typing import List, Callable
import toolz as t
from dotenv import load_dotenv
from app.kafka_dir.producers import publisher

load_dotenv(verbose=True)

def produce_chunks(data: List, produce: Callable, chunks_size: int = 10):
    [produce(item) for item in list(t.partition_all(chunks_size, data))]

def send_data(df_data):
    print(df_data.columns)
    print({k:v for k,v in enumerate(df_data.columns)})
    list_of_rows = df_data.values.tolist()
    produce_chunks(list_of_rows,publisher(os.environ.get("TOPIC_PROCESS2"),"process_data"))
