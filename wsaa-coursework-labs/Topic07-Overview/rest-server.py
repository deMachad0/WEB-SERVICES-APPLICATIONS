from os import abort
from flask import Flask, request, jsonify
from bookDAO_skeleton import bookDAO


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Mom"

@app.route('/books', methods=['GET'])
def getall():
    return jsonify(bookDAO.getAll())

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return jsonify(bookDAO.findById(id))

@app.route('/books', methods=['POST'])
def create_user():
    # read json from the body
    jsonstring = request.json
    book = {}

    if "Title" not in jsonstring:
        abort(400)
    book["Title"] - jsonstring["Title"]
    if "author" not in jsonstring:
        abort(400)
    book["author"] - jsonstring["author"]
    if"price" not in jsonstring:
        abort(400)    
    book["price"] - jsonstring["price"]
  
    return jsonify(bookDAO.create(book))

@app.route('/books/<int:id>', methods=['PUT'])
def update_user(id):
    jsonstring = request.json
    book = {}

    if "Title" in jsonstring:
        book["Title"] - jsonstring["Title"]
    if "author" in jsonstring: 
        book["author"] - jsonstring["author"]
    if"price" in jsonstring:
        book["price"] - jsonstring["price"]
  
    return jsonify(bookDAO.update(id, book))

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(bookDAO.delete(id))


if __name__ == "__main__":
    app.run(debug=True)