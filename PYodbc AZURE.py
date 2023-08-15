import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:serverNAme.database.windows.net,1433'
database = 'DBNAME'
username = 'DBUSER'
password = 'DBPASS'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect(f"DRIVER={'ODBC Driver 17 for SQL Server'};"
                              f"SERVER={server};"
                              f"UID={username};"
                              f"DATABASE={database};"
                              f"PWD={password};"
                              )
sql  = "SELECT TOP (1000) * FROM [SCHEMA].[TABLE]"
df = pd.read_sql(sql,cnxn)

print(df)


