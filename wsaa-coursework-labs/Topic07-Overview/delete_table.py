import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)

cursor = mydb.cursor()
sql="delete from student where id = %s"
values = (2,)

cursor.execute(sql, values)

mydb.commit()
print("delete done")