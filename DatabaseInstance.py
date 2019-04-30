import cx_Oracle

from Database.DatabaseConfig import DB_ID
from Database.DatabaseConfig import DB_URL
from Database.DatabaseConfig import DB_NID

#DB connect
con=cx_Oracle.connect(DB_ID+'/'+DB_URL+'/'+DB_NID)
db=con.cursor()

