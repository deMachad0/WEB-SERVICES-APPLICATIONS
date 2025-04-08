# Import the StudentDAO class from the zstudentDAO module
from zstudentDAO import studentDAO

# Create a new student dictionary with a name and age
student = {
    "name": "mark",  # Student's name
    "age": 31        # Student's age
}

# Create the student in the database using the create method
student = studentDAO.create(student)  # This will insert the student into the database
studentid = student["id"]  # Store the ID of the newly created student

# Find the student by their ID using the findById method
result = studentDAO.findById(studentid)  # Fetch the student record by ID
print("Test create and find by id")  # Print a message indicating the test
print(result)  # Print the result of the find operation (student details)

# Update the student's information with new values
newstudentvalues = {"name": "Fred", "age": 18}  # New name and age for the student
student = studentDAO.update(studentid, newstudentvalues)  # Update the student's data
result = studentDAO.findById(studentid)  # Fetch the updated student record by ID
print("test update")  # Print a message indicating the update test
print(result)  # Print the updated student details

# Fetch and print all students from the database using the getAll method
print("test get all")  # Print a message indicating the test for getting all students
allStudents = studentDAO.getAll()  # Fetch all students from the database
for student in allStudents:  # Loop through the list of all students
    print(student)  # Print each student record

# Delete the student from the database by their ID
studentDAO.delete(studentid)  # Remove the student from the database by ID

