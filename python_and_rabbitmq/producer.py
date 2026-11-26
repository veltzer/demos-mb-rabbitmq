#!/usr/bin/env python

import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

body = sys.argv[1]

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=body.encode(),
)
print(f"sent [{body}]")
channel.close()
