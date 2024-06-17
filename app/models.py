from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    hash = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.Integer, db.ForeignKey('block.id'))
    block = db.relationship('Block', backref=db.backref('transactions', lazy=True))
    tx_hash = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
