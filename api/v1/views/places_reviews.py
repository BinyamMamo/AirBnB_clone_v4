#!/usr/bin/python3
"""
 Create a view to review objects that can handle default API actions
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.place import Place
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def reviews(place_id):
    """
     Get reviews for a place.
    """
    place = storage.get("Place", place_id)
    if not place:
        abort(404)
    return jsonify([review.to_dict() for review in place.reviews])


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def r_review_id(review_id):
    """
     Get a review by id
    """
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_review(review_id):
    """
     Delete a review. This will delete the review with the given id
    """
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """
     Create a reviews for a place
    """
    place = storage.get("Place", place_id)
    if not place:
        abort(404)
    new_review = request.get_json()
    if not new_review:
        abort(400, "Not a JSON")
    if "user_id" not in new_review:
        abort(400, "Missing user_id")
    user_id = new_review['user_id']
    if not storage.get("User", user_id):
        abort(404)
    if "text" not in new_review:
        abort(400, "Missing text")
    review = Review(**new_review)
    setattr(review, 'place_id', place_id)
    storage.new(review)
    storage.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_review(review_id):
    """
     Update a review. This will update the fields that are in the request body.
    """
    review = storage.get("Review", review_id)
    if not review:
        abort(404)

    body_request = request.get_json()
    if not body_request:
        abort(400, "Not a JSON")

    for k, v in body_request.items():
        if k not in ['id', 'user_id', 'place_id',
                     'created_at', 'updated_at']:
            setattr(review, k, v)

    storage.save()
    return make_response(jsonify(review.to_dict()), 200)
