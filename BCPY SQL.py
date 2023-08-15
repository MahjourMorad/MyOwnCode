import pandas as pd
import pyodbc
import time
import bcpy
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
from sqlalchemy import create_engine



startTime = time.time()
sql_config = {
    'server': 'tcp:127.0.0.1,1433',
    'database': 'dbName',
    'username': 'db_USER',
    'password': 'DB_PAss'
}
parse_dates = ['dates']
parse_dates=parse_dates
df = pd.read_csv("output.csv")
bdf = bcpy.DataFrame(df)

sql_table =  bcpy.SqlTable(sql_config,schema_name='schema' ,table='table',batch_size=100)
bdf.to_sql(sql_table)



