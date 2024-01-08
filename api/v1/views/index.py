#!/usr/bin/python3
"""
defines two routes for a Flask application.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "ok"})
