#Import libries
from azure.servicebus import ServiceBusClient,ServiceBusSubQueue
import json

#Define variables for connection strings and queue name
conn_str = "Endpoint=sb://azservicebusdemodebrah.servicebus.windows.net/;SharedAccessKeyName=Listen;SharedAccessKey=8OLR0jJCGEcfK/znxmM8IEM/TZTwNqaLLBUdjF4QXg0=;EntityPath=mystorekeeper-warehouse"
queue_name = "mystorekeeper-warehouse"

#Initialize service bus client
client = ServiceBusClient.from_connection_string(conn_str)

#Initialize queue reciever client
dlq_receiver = client.get_queue_receiver(queue_name=queue_name, sub_queue=ServiceBusSubQueue.DEAD_LETTER)
with dlq_receiver:
    received_msgs = dlq_receiver.receive_messages(max_message_count=10, max_wait_time=5)
    for msg in received_msgs:
        print(str(msg))

        #If you wont to delete the message after recieving the messages, uncomment the code bellow
        dlq_receiver.complete_message(msg)