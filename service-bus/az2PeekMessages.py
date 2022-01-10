"""
Peek message from service bus queue and
delete it after it has been successfully
been proccessed.
"""

#Import Libries
from azure.servicebus import ServiceBusClient
import os
import json

#Initialize connection strings and key name
conn_str = "Endpoint=sb://azservicebusdemodebrah.servicebus.windows.net/;SharedAccessKeyName=Listen;SharedAccessKey=8OLR0jJCGEcfK/znxmM8IEM/TZTwNqaLLBUdjF4QXg0=;EntityPath=mystorekeeper-warehouse"
queue_name = "mystorekeeper-warehouse"

servicebus_client = ServiceBusClient.from_connection_string(conn_str=conn_str, logging_enable=True)
with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=queue_name, max_wait_time=5)
    with receiver:
        for msg in receiver:
            print(str(msg))
            receiver.complete_message(msg)

