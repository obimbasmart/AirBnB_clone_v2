#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """route the homepage"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """route the hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    """route hbnb C"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hbnb_python(text="is_cool"):
    """route hbnb python"""
    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run()
