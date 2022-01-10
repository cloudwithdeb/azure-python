#Import Libries
from azure.appconfiguration import AzureAppConfigurationClient
from azure.identity import DefaultAzureCredential
from fastapi import FastAPI
import os

#Get Environment variables
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
ENVIRONMENT_VARIABLE = os.getenv("ENVIRONMENT_VARIABLE")

#Initialize fastapi
app = FastAPI()

#Add route
@app.get("/")
async def home():
    return {
        "message": CONNECTION_STRING,
        "others": ENVIRONMENT_VARIABLE
    }