#Import Libries
from azure.appconfiguration import AzureAppConfigurationClient
from azure.identity import DefaultAzureCredential
import os

BASE_URL = "https://testconfigsone.azconfig.io"

#Initialize identity
default_credential = DefaultAzureCredential()

#Initialize AzureAppConfigurationClient
appconfig = AzureAppConfigurationClient(
    credential=default_credential,
    base_url=BASE_URL
)

#Get configuration secrets
responds = appconfig.get_configuration_setting(
    key="userskey"
)

print(responds)
print("==========================\n\n")
print(responds._value)
