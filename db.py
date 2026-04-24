import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vishal@12",
    database="library"
)

cursor = conn.cursor()
cursor.execute("select name from users")
b=cursor.fetchall()
for i in b:
    print(i)

