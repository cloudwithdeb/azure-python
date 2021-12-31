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
NEW_USERNAME = 'Justice Owusu Boateng'
NEW_AGE = 200

#Query to update user
sqlquery = f"""
            UPDATE users SET username = ?,
            age = ? WHERE user_id = ?
            """

#Add dataset to table
resp = cursor.execute(sqlquery, (NEW_USERNAME, NEW_AGE, USERID,))
print(resp)
conn.commit()
conn.close()