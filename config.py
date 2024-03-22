import os
from dotenv import load_dotenv

load_dotenv()

unprocessed_queue=os.getenv('UNPROCESSED_QUEUE')
processed_queue=os.getenv('PROCESSED_QUEUE')
host=os.getenv('HOST')
