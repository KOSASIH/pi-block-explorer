# block_routes.py
from flask import Blueprint
from api import BlockAPI

block_blueprint = Blueprint("block", __name__)

block_blueprint.add_url_rule("/block/<int:height>", view_func=BlockAPI.as_view("block_api"))
