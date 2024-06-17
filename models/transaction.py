# transaction.py
from app import db
from models import Transaction

class TransactionService:
    def get_transactions_by_block(self, block_id):
        return Transaction.query.filter_by(block_id=block_id).all()

    def get_transaction_by_id(self, transaction_id):
        return Transaction.query.get(transaction_id)
