#!/usr/bin/python3
"""7-states_list module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """a fun to display states list"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """a fun to close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
