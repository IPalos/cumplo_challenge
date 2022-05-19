import os
import mysql.connector

db = mysql.connector.connect(
  host=os.environ.get("DB_HOSTNAME","localhost:3306"),
  user=os.environ.get("DB_USERNAME","admin"),
  password=os.environ.get("DB_PASSWORD","password"),
	database=os.environ.get("DB_DATABASE","mydb")
)

cursor = db.cursor()
cursor.execute("CREATE TABLE users(name VARCHAR(255), email VARCHAR(255);")

def insert_db(cursor,table,vals):
	return cursor.execute(f"INSERT INTO {table} VALUES ({vals[0]} , {vals[1]})")