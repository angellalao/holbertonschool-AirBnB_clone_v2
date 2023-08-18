#!/usr/bin/python3
"""script that starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """returns list of state objects present in db storage"""
    states = storage.all(State)
    print(states)
    print({type(states)})
    for v in states.values():
        print(v)
        print({type(v)})
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def app_teardown(exception):
    """removes current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
