
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "INSERT INTO customers(name,address) VALUES (%s, %s)"
val = ("John", "HIghway 21")

mycursor.execute(sql,val)

conn.commit()                                               #required command

print(mycursor.rowcount, "Record(s) Inserted")

