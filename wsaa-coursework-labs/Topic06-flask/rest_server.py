from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Mom"

@app.route('/books', methods=['GET'])
def getall():
    return "get all"

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by ID"

@app.route('/books', methods=['POST'])
def create_user():
    # read json from the body
    jsonstring = request.json
    return f" Creating book {jsonstring}"

@app.route('/books/<int:id>', methods=['PUT'])
def update_user(id):
    jsonstring = request.json
    return f"Updating book {id} {jsonstring}"

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"Delete an ID {id}"


if __name__ == "__main__":
    app.run(debug=True)