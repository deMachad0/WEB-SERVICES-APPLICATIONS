# Import the mysql.connector module to work with MySQL databases
import mysql.connector

# Define the StudentDAO class for interacting with the database
class StudentDAO:
    # Class variables for MySQL connection details
    host = ""
    user = ""
    password = ""
    database = ""
    
    connection = ""
    cursor = ""

    # Constructor to initialize connection details
    def __init__(self):
        self.host = "localhost"  # Set the host (usually localhost for local development)
        self.user = "root"  # Set the username for the MySQL database
        self.password = "root"  # Set the password for the MySQL database
        self.database = "wsaa"  # Set the database name

    # Method to get a cursor to execute SQL queries
    def getCursor(self):
        # Establish a connection to the MySQL database
        self.connection = mysql.connector.connect (
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()  # Create a cursor object for querying
        return self.cursor
    
    # Method to close the database connection and cursor
    def closeAll(self):
        self.connection.close()  # Close the database connection
        self.cursor.close()  # Close the cursor

    # Method to get all students from the 'student' table
    def getAll(self):
        cursor = self.getCursor()  # Get a cursor to execute the query
        sql = "select * from student"  # SQL query to select all students
        cursor.execute(sql)  # Execute the query

        result = cursor.fetchall()  # Fetch all the results of the query
        student_list = []  # Initialize an empty list to store student records
        for row in result:  # Loop through each row in the result
            student_list.append(self.convert_to_dict(row))  # Convert each row to a dictionary
        self.closeAll()  # Close the connection and cursor
        return student_list  # Return the list of students
    
    # Method to find a student by their ID
    def findById(self, id):
        cursor = self.getCursor()  # Get a cursor to execute the query
        sql = "select * from student where id = %s"  # SQL query to find a student by ID
        values = (id,)  # Tuple with the ID as a parameter
        cursor.execute(sql, values)  # Execute the query with the ID parameter

        result = cursor.fetchone()  # Fetch the first result (only one student)
        self.closeAll()  # Close the connection and cursor
        return self.convert_to_dict(result)  # Convert the result to a dictionary and return it
    
    # Method to create a new student in the database
    def create(self, student):
        cursor = self.getCursor()  # Get a cursor to execute the query
        sql = "insert into student (name, age) values (%s, %s)"  # SQL query to insert a new student
        values = (student.get("name"), student.get("age"))  # Values to insert (name and age)
        cursor.execute(sql, values)  # Execute the insert query

        self.connection.commit()  # Commit the transaction to save the changes
        newid = cursor.lastrowid  # Get the ID of the newly inserted student
        student["id"] = newid  # Add the ID to the student dictionary
        self.closeAll()  # Close the connection and cursor
        return student  # Return the student with the new ID
    
    # Method to update a student's information
    def update(self, studentid, student):
        cursor = self.getCursor()  # Get a cursor to execute the query
        sql = "update student set name = %s, age = %s where id = %s"  # SQL query to update a student
        values = (student.get("name"), student.get("age"), studentid)  # Values to update (name, age, and ID)
        cursor.execute(sql, values)  # Execute the update query

        self.connection.commit()  # Commit the transaction to save the changes
        self.closeAll()  # Close the connection and cursor
        return student  # Return the updated student
    
    # Method to delete a student by their ID
    def delete(self, id):
        cursor = self.getCursor()  # Get a cursor to execute the query
        sql = "delete from student where id = %s"  # SQL query to delete a student by ID
        values = (id,)  # Tuple with the ID as a parameter
        cursor.execute(sql, values)  # Execute the delete query

        self.connection.commit()  # Commit the transaction to save the changes
        self.closeAll()  # Close the connection and cursor
        return True  # Return True to indicate that the student was deleted
    
    # Method to convert a row from the database into a dictionary
    def convert_to_dict(self, resultLine):
        student_keys = ["id", "name", "age"]  # Keys for the student dictionary
        current_key = 0  # Initialize the index for the keys
        student = {}  # Initialize an empty dictionary to store student data
        for attrib in resultLine:  # Loop through each attribute (column) in the row
            student[student_keys[current_key]] = attrib  # Assign each attribute to the dictionary
            current_key = current_key + 1  # Move to the next key in the list
        return student  # Return the student dictionary

# Create an instance of the StudentDAO class
studentDAO = StudentDAO()
