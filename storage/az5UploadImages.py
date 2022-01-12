#Import Libries
import os
import json
import uuid
import base64
import logging
import tempfile
from PIL import Image
from io import BytesIO
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient, ContentSettings

def main(image) -> func.HttpResponse:
    
    #Get image name to be uploaded
    imagename = f'{str(uuid.uuid1())}'

    #Get storage account and container name
    STORAGE_ACCOUNT_NAME = "storageaccountazurea855"
    containername = "users-container"

    #Set image extension
    image_extension = ".jpeg"

    #Initialize azure credentials
    def_credentials = DefaultAzureCredential()

     #Get a temporary image path
    tempFilePath = tempfile.gettempdir()

    #Combine image with extension
    filename = f'{imagename}{image_extension}'

    #Combine image with temporary path
    imagePath = f'{tempFilePath}/{filename}'

    #Set application content type
    content_settings = ContentSettings(content_type="image/jpeg")
    userid = str(uuid.uuid4())

    #Initialize Blob connection
    blob_con = BlobClient(
        credential = def_credentials,
        account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net.",
        container_name=containername+"/Owusu Bright Debrah/"+userid,
        blob_name=filename
    )

    #Get incoming image from client
    userimage = bytes(image, encoding="utf-8")

    #Decode Incoming Image
    decoded_image = base64.b64decode(userimage)

    Image.open(BytesIO(decoded_image)).convert('RGB').save(imagePath)

    #Upload image to azure
    with open(imagePath, "rb") as data:
        blob_con.upload_blob(data, content_settings=content_settings)

    #Define and return responds to clients
    responds = {"message": "Image saved successfully thanks"}
    return responds
