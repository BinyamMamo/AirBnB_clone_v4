#!/usr/bin/python3
"""
sets up a Flask application for an API
registers blueprints for the API routes
defines a teardown function to close the app session,
and an error handler for 404 errors.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    """Closes the app session
    """
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """returns a JSON response with an error message and a status code of 404.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    HBNB_API_HOST = getenv("HBNB_API_HOST")
    HBNB_API_PORT = getenv("HBNB_API_PORT")
    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else HBNB_API_PORT
    print(host)
    app.run(host=host, port=port, threaded=True)
