import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://stylhohb:JO7Bl-v82OGGuK7EJS85NEJ3yNk4iBLp@cougar.rmq.cloudamqp.com/stylhohb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
message = '{"problem_id": "1", "jobs_id": "2"}'
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(" [x] Sent 'problem_id = 2'")
connection.close()