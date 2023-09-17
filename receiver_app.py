
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
received_data = []

@app.route('/api', methods=['POST'])
def receive_data():
    data = request.json
    received_data.append(data)
    return jsonify({"status": "success", "message": "Data received successfully"}), 200

@app.route('/')
def display_data():
    return "<br>".join([str(item) for item in received_data])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
