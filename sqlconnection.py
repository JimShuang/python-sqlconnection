import pyodbc

cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 13 for SQL Server};"
    "Server=Servername;"
    "Database=Databasename;"
    "Trusted_connection=yes;"
)
#Please make sure there is no space in between =, otherwise the connection will not work!
#Please replace the Driver, Server and Database to your own ones


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM tablename')

for row in cursor:
    print(row)
