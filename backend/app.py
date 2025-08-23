from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/exercise")
def get_exercise():
    with open("exercises/python/ForLoop.json") as f:
        data = json.load(f)
    return jsonify(data[0])

@app.route("/exercise/")
def get_exercise():
    with open("exercises/python/ForLoop.json") as f:
        data = json.load(f)
    return jsonify(data[0])

@app.route("/exercise/introduction")
def exercise_intro():
    with open("exercises/intro.json") as f:
        data = json.load(f)
    return jsonify(data[0])

@app.route("/exercise/introduction/")
def exercise_intro():
    with open("exercises/intro.json") as f:
        data = json.load(f)
    return jsonify(data[0])

if __name__ == "__main__":
    app.run(debug=True)
