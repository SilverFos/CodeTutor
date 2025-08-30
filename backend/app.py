from flask import Flask, jsonify
import json
import os
from datetime import datetime

STARTED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
app = Flask(__name__)

@app.route("/exercise")
def get_exercise():
    filepath = "exercises/exintro.json"
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/exercise/python", strict_slashes = False)
def list_python_topics():
    print(f"{STARTED_AT}RUNNING UPDATED get_python_topic")
    folder = os.path.join("exercises", "python")
    try:
        topics = []
        for filename in os.listdir(folder):
            if filename.endswith(".json"):
                topics.append(os.path.splitext(filename)[0])  # strip .json
        return jsonify({
            "status": "success",
            "topics": sorted(topics)
        })
    except FileNotFoundError:
        return jsonify({
            "status": "error",
            "message": "Python exercises folder not found"
        }), 500

@app.route("/exercise/python/<value>")
def get_python_topic(value):
    print(f"{STARTED_AT}RUNNING UPDATED get_python_topic")

    filepath = os.path.join("exercises", "python", f"{value}.json")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data=json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": f"Topic {value} not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
