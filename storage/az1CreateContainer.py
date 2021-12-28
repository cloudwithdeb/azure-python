#Import Libries
from azure.identity import DefaultAzureCredential
from azure.storage.blob import ContainerClient

#Initialize DefaultAzureCredential
def_credentials = DefaultAzureCredential()

#Set storage account name
STORAGE_ACCOUNT_NAME = "storageaccountazurea855"

#Initialize ContainerClient
container_client = ContainerClient(
    account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net.",
    credential=def_credentials,
    container_name="users-container"
)

#Create new container
responds = container_client.create_container()

#Display responds
print(responds)