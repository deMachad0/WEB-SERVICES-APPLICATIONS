# Import Flask and necessary utilities (url_for for generating URLs, redirect for redirecting users)
from flask import Flask, url_for, redirect

# Initialize the Flask app:
# - __name__ tells Flask where to find files (like templates)
# - static_url_path="" makes static files available at the root URL (/)
# - static_folder='staticpages' sets the folder for static files (HTML/CSS/JS)
app = Flask(__name__, static_url_path="", static_folder='staticpages')

# Define route for the homepage (root URL '/')
@app.route('/')
def index():
    return "<h1>Hi there Mom </h1>"  # Returns an HTML heading as the homepage

# Define route to GET all users (accessible via /users)
@app.route('/users', methods=['GET'])
def get_users():
    return "Getting all users"  # Returns a plain text response

# Define route to GET a specific user by username (e.g., /users/John)
@app.route('/users/<username>', methods=['GET'])
def get_users_byname(username):
    return f"Hello {username}"  # Returns a personalized greeting

# Define route to GET a user by ID (e.g., /users/123)
# <int:id> ensures the ID is an integer (otherwise 404)
@app.route('/users/<int:id>', methods=['GET'])
def get_users_byId(id):
    return f"Your ID is {id}"  # Returns the user's ID

# Define route to POST (create) a new user
# Note: POST requests can't be tested directly in browsers (use Postman/curl)
@app.route('/users', methods=['POST'])
def create_user():
    return "Creating an user"  # Placeholder for user creation logic

# Define route to PUT (update) a user
# Note: PUT requests can't be tested directly in browsers
@app.route('/users', methods=['PUT'])
def update_user():
    return "Updating user"  # Placeholder for user update logic

# Define a route that redirects (/invalid → homepage)
@app.route('/invalid', methods=['GET'])
def testing_redirect():
    # url_for('index') generates the URL for the index() function (/)
    # redirect() sends the user to that URL
    return redirect(url_for('index'))


# Define route to calculate the square of a number (e.g., /square/5 → 25)
@app.route('/square/<int:id>', methods=['GET'])
def get_square_of(id):
    return f"The square of {id} is {id*2}"  # Returns the calculated square

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables auto-reload and error messages