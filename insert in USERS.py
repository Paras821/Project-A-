
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "INSERT INTO users(id,name,fav) VALUES (%s, %s, %s)"
val = [
    ('1', 'John', '154'),
    ('2', 'Peter', '154'),
    ('3', 'Amy', '155'),
    ('4', 'Hannah', ''),
    ('5', 'Michael', '')
    ]

mycursor.executemany(sql,val)

conn.commit()

print(mycursor.rowcount, "Record(s) Inserted")

