import pyodbc

cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 13 for SQL Server};"
    "Server=uspp01-24860414\eaudit;"
    "Database=Practice;"
    "Trusted_connection=yes;"
)

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM dbo.Employee')

for row in cursor:
    print(row)