# Import Flask and necessary utilities:
# - Flask: The main Flask class to create the app
# - request: To access incoming request data (like form data or JSON)
# - jsonify: To convert Python dictionaries to JSON responses
from flask import Flask, request, jsonify

# Create the Flask application instance
app = Flask(__name__)

# Route for the homepage (root URL '/')
@app.route('/')
def index():
    return "Hi there"  # Simple text response for the homepage

# Route to handle query parameters (e.g., /inquery?name=Andre)
@app.route('/inquery')
def inquery():
    # Get the 'name' parameter from the URL query string
    # Example: /inquery?name=Andre → request.args = {'name': 'Andre'}
    name = request.args["name"]  # This will raise an error if 'name' is missing
    
    # Return all query parameters as a dictionary (automatically converted to JSON)
    return request.args

# Route to handle POST requests with JSON data
@app.route("/inbody", methods=["POST"])
def inbody():
    # Get JSON data from the request body
    # Example: POST {"name": "Andre", "age": 21} to /inbody
    name = request.json["name"]  # Access 'name' from JSON
    age = request.json["age"]    # Access 'age' from JSON
    
    # Optional: Uncomment to see the full JSON in your terminal
    # print(request.json)
    
    # Return a formatted string response
    return f"You are {name} and your age is {age}"

# Route to return user data as JSON
@app.route('/user')
def get_user():
    # Create a Python dictionary with user data
    user = {
        "name": "Andre",
        "age": 21
    }
    
    # Convert the dictionary to a proper JSON response
    return jsonify(user)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables auto-reload and error pages