import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "INSERT INTO products(id,name) VALUES (%s, %s)"
val = [
    ('154', 'Chocolate Heaven'),
    ('155', 'Tasty Lemons'),
    ('156', 'Vanilla Dreams')
    ]
mycursor.executemany(sql,val)

conn.commit()

print(mycursor.rowcount, "Record(s) Inserted")

