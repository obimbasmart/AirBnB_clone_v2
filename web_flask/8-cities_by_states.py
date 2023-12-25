#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_city_list():
    """show list of states and cities"""
    states = sorted([state for _, state in storage.all(
        State).items()], key=lambda state: state.name)
    [state.cities.sort(key=lambda city: city.name) for state in states]
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db_connection(error=None):
    """close database connections"""
    storage.reload()
    storage.close()


if __name__ == "__main__":
    app.run()
