#!/usr/bin/python3
"""script that starts a flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns message to be displayed in users browser"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns message to be displayed in users browser"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """returns message to be displayed in users browser"""
    formatted_text = text.replace("_", " ")
    return "C %s" % formatted_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
