# File: flask_app.py

# Q7: Create a web server using Flask & Python

from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello! Flask server is running."

# About route
@app.route("/about")
def about():
    return "This is the about page."

# Run server
if __name__ == "__main__":
    app.run(debug=True)