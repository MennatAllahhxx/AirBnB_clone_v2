#!/usr/bin/python3
"""8-cities_by_states module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """a fun to display states and cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_storage(exceptiom):
    """a fun to close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
