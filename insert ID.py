
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "INSERT INTO customers(name,address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")

mycursor.execute(sql,val)

conn.commit()

print("Record(s) Inserted, ID:", mycursor.lastrowid)

