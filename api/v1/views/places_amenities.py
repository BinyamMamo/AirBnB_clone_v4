#!/usr/bin/python3
"""
Retrieve default API actions for Place and Amenity view objects link.
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from os import getenv


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def places_amenities(place_id):
    """
     Get a list of amenities associated with a Place
    """
    place = storage.get("Place", place_id)
    if not place:
        abort(404)

    place_amenities = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = [amenity.to_dict() for amenity in place.amenities]
    else:
        place_amenities = [storage.get("Amenity", id).to_dict()
                           for id in place.amenity_ids]
    return jsonify(place_amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_places_amenities(place_id, amenity_id):
    """
     Delete an amenity from a place
    """
    place = storage.get("Place", place_id)
    if not place:
        abort(404)

    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        if amenity not in place.amenities:
            abort(404)
    else:
        if amenity_id not in place.amenity_ids:
            abort(404)
        index = place.amenity_ids.index(amenity_id)
        place.amenity_ids.pop(index)

    amenity.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'],
                 strict_slashes=False)
def link_amenity_place(place_id, amenity_id):
    """
     Link an amenity to a place
    """
    place = storage.get("Place", place_id)
    if not place:
        abort(404)

    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        if amenity in place.amenities:
            return amenity.to_dict(), 200
        place.amenities.append(amenity)
    else:
        if amenity_id in place.amenity_ids:
            return amenity.to_dict(), 200
        place.amenity_ids.append(amenity_id)

    storage.save()
    return amenity.to_dict(), 201
