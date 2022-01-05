#Import Libries
from azure.appconfiguration import AzureAppConfigurationClient
from azure.identity import DefaultAzureCredential
from fastapi import FastAPI
import pymongo
import os

#Get Environment variables
USERNAMES = os.getenv("USERNAMES")
PASSWORD = os.getenv("PASSWORD")
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
    key="db:name:v1",
    label="version1"
)

print(responds.value)

#Initialize fastapi
app = FastAPI()
#Add route
@app.get("/")
async def home():
    return {
        "message": "Welcome to home page",
        "password": PASSWORD,
        "username": USERNAMES
    }