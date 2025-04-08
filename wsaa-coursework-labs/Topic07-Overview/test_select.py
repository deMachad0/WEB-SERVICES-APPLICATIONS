import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)
cursor = mydb.cursor()
sql = "select * from student where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)

cursor.close()
mydb.close()