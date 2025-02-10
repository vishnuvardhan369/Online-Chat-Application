from flask import Flask, request, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
chat_history = []
UPLOAD_DIR = "uploads"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "index.html")

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(chat_history)

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    data["timestamp"] = get_timestamp()
    chat_history.append(data)
    return jsonify({"status": "Success"})

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"status": "No file part"}), 400
    file = request.files["file"]
    username = request.form.get("username", "Anonymous")
    if file.filename == "":
        return jsonify({"status": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(file_path)
    file_url = f"/files/{file.filename}"
    message = f"<a href='{file_url}' download='{file.filename}'>📁 {file.filename} (Click to Download)</a>"
    chat_history.append({
        "username": username,
        "message": message,
        "timestamp": get_timestamp()
    })
    return jsonify({"status": "Success", "file_url": file_url})

@app.route("/files/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
