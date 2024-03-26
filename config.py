import os
from dotenv import load_dotenv

load_dotenv()

unprocessed_queue=os.getenv('UNPROCESSED_QUEUE')
processed_queue=os.getenv('PROCESSED_QUEUE')
host=os.getenv('HOST')
topic=os.getenv('TOPIC')
bootstrap_servers=os.getenv('bootstrap_servers')
group_id=os.getenv('group_id')
key0=os.getenv('key0')
key1=os.getenv('key1')
