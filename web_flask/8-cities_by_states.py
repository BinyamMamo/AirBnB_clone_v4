#!/usr/bin/python3
""" starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def closeSession(exception):
    """
     function - Closes the sqlalchemy session. It is called
                 when the user closes the session.
     @exception: The exception that caused the closing of the session
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """
     function - List all states in the database.

     Return: A view to display the states
    """
    states = []
    for key, value in storage.all(State).items():
        states.append(value)
    states.sort(key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
