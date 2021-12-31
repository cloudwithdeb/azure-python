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

#Query to delete user
sqlquery = f"""
            DELETE FROM users
            WHERE user_id = ?
            """

#Delete user
resp = cursor.execute(sqlquery, (USERID,))
print(resp)
conn.commit()
conn.close()