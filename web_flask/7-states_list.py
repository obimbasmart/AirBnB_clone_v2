#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """show list of states"""
    states = sorted([state for _, state in storage.all(
        State).items()], key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db_connection(error=None):
    """close database connections"""
    storage.reload()
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
