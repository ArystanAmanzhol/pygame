import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='example1')

channel.basic_publish(exchange='', routing_key='example1', body='Example1')

print("Sent 'Example1'")
channel.close()
