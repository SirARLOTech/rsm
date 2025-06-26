from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# TEMP: Store logs in memory
logs = []

@app.route('/rsm', methods=['POST'])
def rsm_handler():
    data = request.json
    action = data.get("action")
    username = data.get("username")
    reason = data.get("reason")
    warn_id = data.get("warn_id")
    new_name = data.get("new_name")

    print(f"Received RSM command: {data}")
    logs.append(data)

    # Your Roblox game polls this (or use MessagingService + HTTPService)
    # You can store this in a file, database, or just return it when asked

    return jsonify({"status": "received"}), 200

@app.route('/rsm-commands', methods=['GET'])
def get_commands():
    return jsonify(logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
