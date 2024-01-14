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


@app.route("/states", strict_slashes=False)
def list_states():
    """
     function - List all states in the database.

     Return: A view to display the states
    """
    states = []
    for key, value in storage.all(State).items():
        states.append(value)
    states.sort(key=lambda state: state.name)
    print(states)
    return render_template("9-states.html", states=states, route="states_list")


@app.route("/states/<id>", strict_slashes=False)
def show_state(id):
    """
     function - Shows the state with the given id
     @id: id of the state to show

     Return: HTML to display the state
    """
    states = storage.all(State)
    key = "State." + id
    if key in states:
        return render_template("9-states.html",
                               state=states[key],
                               route="state")
    return render_template("9-states.html", route="abort")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
