import flask
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({'ok':True}), 200

@app.post("/api/links")
def create():
    data = request.get_json()
    original_url = data["URL"]
    db.insert_URL(original_url)
    return 




@app.get("/<code>")
def find(code):
    data = request.get_json()
    original_url = data["URL"]
    return original_url


