#Import Libries
from azure.servicebus import ServiceBusClient, ServiceBusMessage

#Initialize connection strings and key name
conn_str = "Endpoint=sb://azservicebusdemodebrah.servicebus.windows.net/;SharedAccessKeyName=send;SharedAccessKey=5awtaWfNPNA3FUMEUv9tjZm/+TIN5vcfZz0tWimgKt8=;EntityPath=mystorekeeper-warehouse"
queue_name = "mystorekeeper-warehouse"

#Define message variable
message = '{"username": "Owusu Bright Debrah", "age": 78, "amount": 97.10, "balance": 10.20}'
m1 = {"username": "Owusu Bright Debrah", "age": 78, "amount": 97.10, "balance": 10.20}

#Start ServiceBusClient connection
with ServiceBusClient.from_connection_string(conn_str) as client:
    with client.get_queue_sender(queue_name) as sender:
        
        # Sending a single message
        send_message = ServiceBusMessage(message)
        send_message.content_type = "application/json"
        # send_message.time_to_live = 30
        send_message.application_properties(m1)
        sender.send_messages(send_message)