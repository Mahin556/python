
import mysql.connector

# conn=mysql.connector.connect(host="192.168.29.173", username="mahin", password="Mahin@123")
conn=mysql.connector.connect(host="192.168.29.173", username="mahin", password="Mahin@123", database="demo")

print(conn)
my_cursor=conn.cursor()

# query="CREATE DATABASE demo"
# query="SHOW DATABASES"
# query="CREATE TABLE students(id INT PRIMARY KEY, name VARCHAR(50))"
# query="SHOW TABLES;"

# query="INSERT INTO students(id, name) VALUES (%s, %s);"
# values=(1,"mahin")

# query="SELECT * FROM students"

query="INSERT INTO students(id, name) VALUES (%s, %s);"
values=[
    (2, "raza"),
    (3, "john"),
    (4, "shv"),
    (5, "mon"),
    (6, "frz")
]

# my_cursor.execute(query,values)
# my_cursor.execute(query)
my_cursor.executemany(query,values)

# for table in my_cursor:
#     print(table)

# for table in my_cursor:
#     print(table)

# for database in my_cursor:
#     print(database)

# print(my_cursor.fetchall())

conn.commit()
conn.close()
