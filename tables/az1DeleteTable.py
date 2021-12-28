#Import Libries
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient

#Initialize DefaultAzureCredentials
default_credentials = DefaultAzureCredential()

#Set variables
TABLE_NAME="students"
ACCOUNT_NAME="storageaccountazurea855"

table_service_client = TableServiceClient(
    endpoint=f"https://{ACCOUNT_NAME}.table.core.windows.net",
    credential=default_credentials
)

#Delete table from storage account
table_client = table_service_client.get_table_client(table_name=TABLE_NAME)
responds = table_client.delete_table()

#Display responds
print(responds)
