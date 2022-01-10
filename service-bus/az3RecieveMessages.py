"""
Recieve message from service bus queue and delete it.
"""

#Import Libries
from azure.servicebus import ServiceBusClient
import os
import json

#Initialize connection strings and key name
conn_str = "Endpoint=sb://azservicebusdemodebrah.servicebus.windows.net/;SharedAccessKeyName=Listen;SharedAccessKey=8OLR0jJCGEcfK/znxmM8IEM/TZTwNqaLLBUdjF4QXg0=;EntityPath=mystorekeeper-warehouse"
queue_name = "mystorekeeper-warehouse"

with ServiceBusClient.from_connection_string(conn_str) as client:
    with client.get_queue_receiver(queue_name) as receiver:
        received_message_array = receiver.receive_messages(max_wait_time=10)  # try to receive a single message within 10 seconds
        if received_message_array:
            print(str(received_message_array[0]))