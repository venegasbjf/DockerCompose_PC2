from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.json
    return jsonify({"message": "User signed up", "user": data}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({"message": "User logged in", "user": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
