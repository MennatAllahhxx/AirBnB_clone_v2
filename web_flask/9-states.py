#!/usr/bin/python3
"""9-states module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """a fun to display states"""
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """a fun to display state by id"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def close_storage(exception):
    """a fun to close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
