#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """route the homepage"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
