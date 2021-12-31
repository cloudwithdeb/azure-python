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
PARTITION_KEY="86168496-67bb-11ec-b1e3-7d7be3720ec6"
ROW_KEY="4eb45764-c787-44a4-86e5-f4715cb9fc7d"

"""
Before you can update an entity, you first have to get the entity you
wont to update thats all its related datasets, then update a specific
entity.
"""
#Get entity by partition and row key
table_client = table_service_client.get_table_client(table_name=TABLE_NAME)
get_entity = table_client.get_entity(
    partition_key=PARTITION_KEY,
    row_key=ROW_KEY
)

"""
After getting the entity set, then perform the update.
"""
#Set new age
get_entity["friends"] = "Mirabel"

#Update an entity
get_entity_responds = table_client.upsert_entity(get_entity)

#Display responds
print(get_entity)
print("===========================================================")
print(get_entity_responds)

"""
Note:
    When you wont to add new column to
    your table, you just have to perform
    an upset statement, and add the name
    of the new COLUMN to your entity set.
"""