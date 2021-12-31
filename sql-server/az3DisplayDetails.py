#Import Libries
import pyodbc

#Define connection strings
driver = "{ODBC Driver 17 for SQL Server}"
server = "cloudhams.database.windows.net"
username = "debrah"
password = "owusuBRIGHT1997"
database = "schooldb"

#Setup connection
conn = pyodbc.connect(
    "DRIVER="+driver
    +";SERVER="+server
    +";DATABASE="+database
    +";UID="+username
    +";PWD="+password
)

#Define cursor connection
cursor = conn.cursor()

#Get values to insert into table
USERID = 7
USERNAME = 'Eva Pokuah Mansah'
AGE = 100

#Query to retrieve dataset
sqlquery = """
            SELECT * FROM users
            WHERE user_id = ?
            """

#Add dataset to table
resp = cursor.execute(sqlquery, (USERID,))

data = []

#Loop through to get datasets
for row in resp:
    data.append({
        "user-id": row.user_id,
        "username": row.username,
        "age": row.age
    })

print(data)
print(f"The length of responds is: {len(data)}")
conn.commit()
conn.close()