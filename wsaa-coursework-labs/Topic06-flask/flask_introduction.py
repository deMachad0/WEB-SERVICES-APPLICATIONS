# Very simple flask server

# !flask/bin/python

# Importing the Flask framework to create a web application
from flask import Flask

# Create a Flask application instance
# __name__ is a special Python variable that gets as value the string "__main__" 
# when the script is executed directly
app = Flask(__name__)

# Define the route for the root URL ('/')
# This decorator tells Flask what URL should trigger our function
@app.route('/')
def index():
    # This function returns the response for the root URL
    # In this case, it simply returns a "Hello, World!" text
    return "Hello, World!"

# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask development server
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server when code changes
    app.run(debug=True)