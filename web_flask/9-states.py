#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """show list of states (and cities) id is found"""
    states = sorted([state for _, state in storage.all(
        State).items()], key=lambda state: state.name)
    if id is None:
        return render_template("9-states.html", states=states,
                               state_by_id=None)

    state_by_id = [state for state in states if state.id == id]
    if state_by_id:
        [state.cities.sort(key=lambda city: city.name)
         for state in state_by_id]
        state_by_id = state_by_id[0]
    return render_template("9-states.html", states=states,
                           state_by_id=state_by_id)


@app.teardown_appcontext
def close_db_connection(error=None):
    """close database connections"""
    storage.reload()
    storage.close()


if __name__ == "__main__":
    app.run()
