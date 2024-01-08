#!/usr/bin/python3
"""
sets up a Flask application for an API
registers blueprints for the API routes
defines a teardown function to close the app session,
and an error handler for 404 errors.
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views.index import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")

@app.teardown_appcontext()
def close_session(exception):
    """Closes the app session
    """
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """returns a JSON response with an error message and a status code of 404.
    """
    return jsonify({'error': 'Not found'}), 404



if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST"), port=getenv("HBNB_API_PORT"), threaded=True)
