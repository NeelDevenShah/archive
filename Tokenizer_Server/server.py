import flask
from flask import request, jsonify
from sentence_transformers import SentenceTransformer
import json

app = flask.Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

@app.route("/checking", methods=["GET"])
def checking():
    return "Working!!"

@app.route("/preprocess", methods=["POST"])
def preprocess_text():
    data = request.get_json()
    texts = []
    for key, value in data.items():
        texts.append(f"{key}: {value}")
    embeddings = model.encode(texts)
    print("Processed an request successfully")
    return jsonify({"embeddings": embeddings.tolist()})

def convert_json_to_text(data):
    texts = []
    for item in data:
        text = item.get("text")
        texts.append(text)
    return texts

if __name__ == "__main__":
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    app.run(host="0.0.0.0", port=5000)  # Change port if needed
