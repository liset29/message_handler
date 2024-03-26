import json
import pika, sys, os
import config as con
from modify_message import modify_order


connection = pika.BlockingConnection(pika.ConnectionParameters(host=con.host))
channel = connection.channel()




def main():
    def callback(ch, method, properties, body):
        unicode_string = body.decode('utf-8')
        json_data = json.loads(unicode_string)
        refactor_data = modify_order(json_data)
        json_data = json.dumps(refactor_data)
        send_to_queue(json_data)

    channel.queue_declare(queue=con.unprocessed_queue)
    channel.basic_consume(queue=con.unprocessed_queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def send_to_queue(data):
    channel.basic_publish(exchange='', routing_key=con.processed_queue, body=f'{data}')


if __name__ == '__main__':
    try:
        print('start')
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
