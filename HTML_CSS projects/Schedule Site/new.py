import mysql.connector

db = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="site123",
    database="testdatabase"
    )

mycursor = db.cursor()

