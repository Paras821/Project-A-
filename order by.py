
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

