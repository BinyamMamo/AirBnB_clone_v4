from flask import Blueprint
from api.v1.views import *
app_views = Blueprint("app_views", __name__)
