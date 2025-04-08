import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)

mycursor = mydb.cursor()
sql="create table student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)"
mycursor.execute(sql)

# commit if create, update or delete
mydb.commit()
mycursor.close()
mydb.close()