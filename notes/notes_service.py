from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route('/notes', methods=['POST'])
def create_note():
    note = request.json
    notes.append(note)
    return jsonify(note), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200

@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = next((n for n in notes if n['id'] == id), None)
    if note:
        return jsonify(note), 200
    return jsonify({"error": "Note not found"}), 404

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    note = next((n for n in notes if n['id'] == id), None)
    if note:
        data = request.json
        note.update(data)
        return jsonify(note), 200
    return jsonify({"error": "Note not found"}), 404

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    global notes
    notes = [n for n in notes if n['id'] != id]
    return '', 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)
