import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)

mycursor = mydb.cursor()

mycursor.execute("create DATABASE wsaa")

# commit if create, update or delete
mycursor.close()
mydb.close()