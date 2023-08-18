#!/usr/bin/python3
"""script that starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """returns list of state objects present in db storage"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@app.teardown_appcontext
def app_teardown(exception):
    """removes current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
