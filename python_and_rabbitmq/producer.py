#!/usr/bin/python3

import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

body = sys.argv[1]

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=body,
)
print(f"sent [{body}]")
channel.close()
