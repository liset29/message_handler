import json
from kafka import KafkaConsumer, TopicPartition, KafkaProducer
from modify_message import modify_order
import config as con

consumer = KafkaConsumer(bootstrap_servers=con.bootstrap_servers, group_id=con.group_id)
topic_partition = TopicPartition(topic=con.topic, partition=1)
consumer.assign([topic_partition])
producer = KafkaProducer(bootstrap_servers=con.bootstrap_servers)


def send_message(value):
    producer.send(con.topic, key=con.key0.encode('utf-8'), value=json.dumps(value).encode('utf-8'))
    print(value)
    producer.flush()


for message in consumer:
    print(message)
    body = message.value
    unicode_string = body.decode('utf-8')
    json_data = json.loads(unicode_string)
    order = modify_order(json_data)
    send_message(order)

