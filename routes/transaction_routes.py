# transaction_routes.py
from flask import Blueprint
from api import TransactionAPI

transaction_blueprint = Blueprint("transaction", __name__)

transaction_blueprint.add_url_rule("/transaction/<int:transaction_id>", view_func=TransactionAPI.as_view("transaction_api"))
