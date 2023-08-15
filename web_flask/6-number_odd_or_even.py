#!/usr/bin/python3
"""script that starts a flask web application """
from flask import Flask
from markupsafe import escape
from flask import render_template
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
    return f"C {escape(formatted_text)}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """returns message to be displayed in users browser"""
    formatted_text = text.replace("_", " ")
    return f"Python {escape(formatted_text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """returns message to be displayed in users browser"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """returns html with int variable from url to be displayed in browser"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """returns html with int variable from url to be diaplyed in browser"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
