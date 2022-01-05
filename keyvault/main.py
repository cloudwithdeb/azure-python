#Import Libries
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

#Initialize variables
BASE_URL = "https://testkeyvalut0010.vault.azure.net/"
SECRET_NAME = "dbpassword"

#Initialize identity
default_credential = DefaultAzureCredential()

#Initialize azure keyvault
keyvault = SecretClient(
    credential=default_credential,
    vault_url=BASE_URL
)

#Get secret values
responds = keyvault.get_secret(SECRET_NAME)

#Display responds
print(responds.name)
print(responds.value)