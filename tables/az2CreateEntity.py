#Import Libries
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient
import uuid

#Initialize DefaultAzureCredentials
default_credentials = DefaultAzureCredential()

#Set variables
PARTITION_KEY=str(uuid.uuid1())
ROW_KEY=str(uuid.uuid4())
TABLE_NAME="users"
ACCOUNT_NAME="storageaccountazurea855"

#Define Entity Set
user_entity = {
    "PartitionKey": PARTITION_KEY,
    "RowKey": ROW_KEY,
    "fullname": "Justice Owusu Boateng",
    "age": 500,
    "email": "justice@gmail.com",
    "amount": 67.12,
    "location": "Kumasi Odocore",
    "phone": "0271008923"
}

#Initialize table service client
table_service_client = TableServiceClient(
    endpoint=f"https://{ACCOUNT_NAME}.table.core.windows.net",
    credential=default_credentials
)

table_client = table_service_client.get_table_client(table_name=TABLE_NAME)

#Create a new entity. (Make sure the table has already been created)
table_client.create_entity(user_entity)