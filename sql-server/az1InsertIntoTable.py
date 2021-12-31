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
USERID = 8
USERNAME = 'Bismark Bimpong'
AGE = 81

#Insert dataset into table
sqlquery = f"INSERT INTO users(user_id, username, age) VALUES(?, ?, ?)"

#Add dataset to table
resp = cursor.execute(sqlquery, (USERID, USERNAME, AGE,))
print(resp)
conn.commit()
conn.close()