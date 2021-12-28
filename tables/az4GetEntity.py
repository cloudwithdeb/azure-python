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


#Get users record based on partition and row key
#Note: This will throw an error when partition_key or row_key is not valid
table_client = table_service_client.get_table_client(table_name=TABLE_NAME)
responds = table_client.get_entity(
    partition_key="86168496-67bb-11ec-b1e3-7d7be3720ec6",
    row_key="4eb45764-c787-44a4-86e5-f4715cb9fc7d"
)
print(responds)

