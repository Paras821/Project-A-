
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE users (id VARCHAR(255), name VARCHAR(255), fav VARCHAR(255))")

