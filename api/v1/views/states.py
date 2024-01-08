#!/usr/bin/python3
""" View for State objects that handles default API actions """
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states():
    """
     function - Return all states in JSON format

     Return: JSON representation of all
    """
    d_states = storage.all(State)
    return jsonify([obj.to_dict() for obj in d_states.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def r_state_id(state_id):
    """
     function - Get information about a state
     @state_id: id of the state to get

     Return: jsonified state information if
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    """
     function - Delete a State object.
     @state_id: The id of the State to delete.

     Return: 200 if successful 404 if
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """
     function - Creates a State object in the database

     Return: JSON with the new
    """
    new_state = request.get_json()
    if not new_state:
        abort(400, "Not a JSON")
    if "name" not in new_state:
        abort(400, "Missing name")
    state = State(**new_state)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """
     function - Update a state. This will update the
                properties of an existing state.
     @state_id: The id of the state to update.

     Return: 200 if updated 404 if state doesn't
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    body_request = request.get_json()
    if not body_request:
        abort(400, "Not a JSON")

    for k, v in body_request.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(state, k, v)

    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
