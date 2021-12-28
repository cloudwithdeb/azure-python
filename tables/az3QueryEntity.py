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

#Declare an empty variable to store data in.
data = []

#Define your queries
"""
Note:
    1. Equal to => eq
    2. Less than => lt
    3. Greater than => gt
    4. Less than or equal to => le
    5. Greater than or equal to => ge
    6. Not equal to => ne
    7. Not => not
    8. And => and
    9. Or => or
"""

#Get fullname and age
FULL_NAME="Owusu Bright Debrah"
AGE=900

#Create query to get users data
my_filter = f"age eq {AGE} and fullname eq '{FULL_NAME}'"
table_client = table_service_client.get_table_client(table_name=TABLE_NAME)
responds = table_client.query_entities(my_filter)

#Loop through to get data
for entity in responds:
    data.append({
        "age": entity["age"],
        "fullname": entity["fullname"]
    })

print(data)