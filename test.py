import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123")

if conn.is_connected():
    print("Connection established successfully")

