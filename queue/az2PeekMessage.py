
"""Note: 
Azure storage account Queue requires
connection string to send and retrieve
messages."""

#Import Libries
from azure.storage.queue import QueueClient
import os

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

#Peek to view message
responds = queue.peek_messages(max_messages=3)

#Displat peeked messages
for res in responds:
    print(res.content)