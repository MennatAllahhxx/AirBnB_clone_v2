#!/usr/bin/python3
"""10-hbnb_filters module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """a fun to display hbnb filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def close_storage(exception):
    """a fun to close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
