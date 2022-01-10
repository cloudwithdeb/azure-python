
"""Note: 
Azure storage account Queue requires
connection string to send and retrieve
messages."""

#Import Libries
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy, BinaryBase64DecodePolicy
import os
import base64
import json

#Set and define que name
QUEUE_NAME = "cloudhams"

#Set and define storage account connection string
STORAGE_ACCOUNT_CONNECTION_STR = "DefaultEndpointsProtocol=https;AccountName=storageaccountazurea855;AccountKey=l5NNTgIj8aDfrb10Hw23kzcJfppBkwdJbAd0pvNACFssyjlFDf9T4cifmPgRYG90QVPQSkepZx4hDP+rtW3NYg==;EndpointSuffix=core.windows.net"

#Initialize variables
QUEUE_URL = f"https://{QUEUE_NAME}.queue.core.windows.net/"

#Initialize queue client
queue = QueueClient.from_connection_string(
    queue_name = QUEUE_NAME,
    conn_str=STORAGE_ACCOUNT_CONNECTION_STR
)

message = {
    "username": "Owusu Bright Debrah",
    "age": 988,
    "amount": 89.10,
    "email": "cloudguru@gmail.com"
}

queue.message_encode_policy = BinaryBase64EncodePolicy()
message_bytes = base64.b64encode(bytes(f"b{message}", "utf-8"))

#Send message
respond = queue.send_message(
    queue.message_encode_policy.encode(content=message_bytes)
)

#Display responds
print(respond)