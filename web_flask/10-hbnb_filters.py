#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def show_filters():
    """display hbnb filters"""
    states = sorted([state for _, state in storage.all(
        State).items()], key=lambda state: state.name)
    [state.cities.sort(key=lambda city: city.name) for state in states]

    amenities = sorted([amenity for _, amenity in storage.all(
        Amenity).items()], key=lambda am: am.name)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_db_connection(error=None):
    """close database connections"""
    storage.reload()
    storage.close()


if __name__ == "__main__":
    app.run()
