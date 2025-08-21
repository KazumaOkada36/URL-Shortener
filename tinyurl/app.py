import flask
from flask import Flask, request, jsonify, redirect
import db
import config

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({'ok':True}), 200

@app.post("/api/links")
def create():
    data = request.get_json(silent = True)
    original_url = data["url"]
    new_code = db.insert_url(original_url)
    return jsonify({'Success': new_code}), 201




@app.get("/<code>")
def find(code):
    resp = db.fetch_by_code(code)
    if resp == None:
        return jsonify({"error": "Invalid"}), 404
    else:
        return redirect(resp)


if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5052, debug = True)
    print(app.url_map)

