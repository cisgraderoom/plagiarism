# consume.py
import pika, os
from checkPlagiarism.deletecomment import deleteComment
from checkPlagiarism.plagiarismC import checkPlagiarism

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://stylhohb:JO7Bl-v82OGGuK7EJS85NEJ3yNk4iBLp@cougar.rmq.cloudamqp.com/stylhohb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))
  deleteComment()
  checkPlagiarism()


channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
