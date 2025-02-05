
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"      #specificall 'Mountain'

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "Record(s) Deleted")

