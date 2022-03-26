import pika, os
import json
from deletecomment import deleteComment
from plagiarismC import checkPlagiarism
from getfile import getfile,sendresult
from decouple import config

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = config('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='cisgraderoom.plagiarism.result',passive=False,durable=True,auto_delete=False)

def callback(ch, method, properties, body):
  print(" [x] Received "+ str(body, 'UTF-8'))
  obj = str(body, 'UTF-8')
  json_object = json.loads(obj)
  problem_id = json_object["problem_id"]
  jobs_id = json_object["jobs_id"]
  result = checkPlagiarism(deleteComment(getfile(problem_id)),problem_id)
  res = sendresult(result,int(jobs_id))
  if res == True:
    channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='cisgraderoom.plagiarism.result',on_message_callback=callback,auto_ack=False)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
