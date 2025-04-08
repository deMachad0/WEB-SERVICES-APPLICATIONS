import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)

mycursor = mydb.cursor()
sql="insert into student (name, age) values (%s, %s)"
values = ("Mary", 21)
mycursor.execute(sql, values)

# commit if create, update or delete
mydb.commit()
mycursor.close()
mydb.close()