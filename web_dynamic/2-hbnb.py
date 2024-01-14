#!/usr/bin/python3
"""starts a flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
import uuid


app = Flask(__name__)


@app.route("/2-hbnb", strict_slashes=False)
def hbnb():
    """Renders the 2-hbnb.html template."""
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    states = storage.all(State)
    return render_template("2-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


@app.teardown_appcontext
def teardown(exc):
    """Closes the storage."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
