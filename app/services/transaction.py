from app.models import Transaction

class TransactionService:
    def get_transaction(self, tx_hash):
        return Transaction.query.get(tx_hash)

    def get_transactions(self, block_id):
        return Transaction.query.filter(Transaction.block_id == block_id).all()

    def create_transaction(self, block_id, tx_hash, timestamp):
        transaction = Transaction(block_id=block_id, tx_hash=tx_hash, timestamp=timestamp)
        db.session.add(transaction)
        db.session.commit()
        return transaction
