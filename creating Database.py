
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123")

mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

