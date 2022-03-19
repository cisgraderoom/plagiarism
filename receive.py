# consume.py
import pika, os
from deletecomment import deleteComment
# from plagiarismC import checkPlagiarism
from getfile import deletefile,getfile

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://stylhohb:JO7Bl-v82OGGuK7EJS85NEJ3yNk4iBLp@cougar.rmq.cloudamqp.com/stylhohb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received problem_id :" + str(body))
  getfile(body)
  deleteComment()
  # checkPlagiarism()
  # deletefile()


channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
