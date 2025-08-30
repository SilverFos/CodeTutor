# Flask Project Notes — CodeTutor

## 1. HTTP (Surface Level)
- A protocol — the "language" browser and server use.
- My project: Flask handles all HTTP translation automatically.
- Flask makes http request into python understandable form, which then returns a response to flask again converting it to browser understandable form.

## 2. Web Framework
- A kit of tools for building web apps faster.
- Flask in particular makes a seperate server and has built in pipelines for easy setup
- My project: Flask matches URLs (`@app.route`) to Python functions.

## 3. Flask Basics
- `Flask(__name__)` → creates the app.
- `@app.route("/path")` → connects a URL written in brackets to a function defined right below..
- `jsonify()` → turns Python data into proper JSON + sets headers.
- `if __name__ == "__main__": app.run(debug=True)` → Restarts app whenever changes occur.

## 4. My Routes
- *Eg:*`/exercise/python/introduction`: reads `exercises/python/intro.json` and sends back message + next topics.

## 5. Common Gotchas
- Folder/file name typos break paths.
- Ports matter — default 5000 for Flask.

## 6. Flask Dynamic Routes & File Loading
- Dynamic Route Basics
    A dynamic route in Flask uses <variable> in the URL to capture part of the path as a Python variable.
    Example:
    ```
       @app.route("/exercise/python/<topic>") 
       def get_python_topic(topic):
    ```
    Visiting /exercise/python/loops sets topic = "loops"

## 7. Building File Paths Cross‑Platform
- Use os.path.join() to build file paths that work on Windows, Linux, and Mac.
- Example: 
  ``filepath = os.path.join("exercises", "python", f"{topic}.json")``
- On Windows → exercises\python\loops.json
- On Linux/Mac → exercises/python/loops.json

## 8. f‑Strings (Formatted String Literals)
- Syntax: f"some text {variable} more text"
- The f tells Python to evaluate anything inside {} and insert its value.
- Example:
```
topic = "loops"
f"{topic}.json"  # → "loops.json"
```