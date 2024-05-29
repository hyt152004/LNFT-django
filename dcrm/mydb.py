import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

sql_passwd = os.getenv('SQL_PASSWORD')

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = sql_passwd,
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE lnft")


print("All Done!")
