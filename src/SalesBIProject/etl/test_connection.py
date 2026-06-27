import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=SalesDataWarehouse;'
    'Trusted_Connection=yes;'
)

print("Connected to SQL Server!")

conn.close()