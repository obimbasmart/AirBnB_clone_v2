#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
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


@app.route("/number/<int:number>", strict_slashes=False)
def show_integer(number):
    """show number"""
    return f"{escape(number)} is a number"


@app.route("/number_template/<int:number>", strict_slashes=False)
def show_template_int(number):
    """show number"""
    return render_template("5-number.html", number=number)


@app.route("/number_odd_or_even/<int:number>", strict_slashes=False)
def show_template_odd_even(number):
    """show number"""
    return render_template("6-number_odd_or_even.html", number=number)


if __name__ == "__main__":
    app.run()
