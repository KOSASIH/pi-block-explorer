from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app.controllers import block_controller, transaction_controller
from app.views import block_view, transaction_view
