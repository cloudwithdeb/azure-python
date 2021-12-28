#Import Libries
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient

#Initialize DefaultAzureCredentials
default_credentials = DefaultAzureCredential()

#Set variables
TABLE_NAME="users"
ACCOUNT_NAME="storageaccountazurea855"

table_service_client = TableServiceClient(
    endpoint=f"https://{ACCOUNT_NAME}.table.core.windows.net",
    credential=default_credentials
)

#GET partition and row key values
PARTITION_KEY="a4c53784-67bb-11ec-b1e3-7d7be3720ec6"
ROW_KEY="57f37030-1db3-407d-82e2-0488adb9732d"

#Delete entity with the above partition key
table_client = table_service_client.get_table_client(table_name=TABLE_NAME)
responds = table_client.delete_entity(partition_key=PARTITION_KEY, row_key=ROW_KEY)

#Display responds
print(responds)
