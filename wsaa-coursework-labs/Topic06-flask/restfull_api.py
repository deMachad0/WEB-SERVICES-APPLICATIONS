from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "API server..."

@app.route('/ppsn/<int:id>', methods=['GET'])
def findbyId(id):
    return f"Finding by {id}"

@app.route('/ppsn', methods=['POST'])
def create():
    return f"Creating...{id}"

@app.route('/ppsn/<int:id>', methods=['PUT'])
def update(id):
    return f"Updating ...{id}"

@app.route('/ppsn/<int:id>', methods=['DELETE'])
def delete(id):
    return f"Deleting {id}"

if __name__ == "__main__":
    app.run(debug=True)