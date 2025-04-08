import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)
cursor = mydb.cursor()
sql = "update student set name = %s, age = %s where id = %s"
values = ("Joe",33, 1)

cursor.execute(sql, values)

mydb.commit()
print("Update done!")

cursor.close()
mydb.close()