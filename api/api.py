# api.py
from flask_restful import Api, Resource
from block import BlockService
from transaction import TransactionService

api = Api()

class BlockAPI(Resource):
    def get(self, height):
        block_service = BlockService()
        block = block_service.get_block_by_height(height)
        if block:
            return {"block": block.to_dict()}
        return {"error": "Block not found"}, 404

class TransactionAPI(Resource):
    def get(self, transaction_id):
        transaction_service = TransactionService()
        transaction = transaction_service.get_transaction_by_id(transaction_id)
        if transaction:
            return {"transaction": transaction.to_dict()}
        return {"error": "Transaction not found"}, 404

api.add_resource(BlockAPI, "/api/block/<int:height>")
api.add_resource(TransactionAPI, "/api/transaction/<int:transaction_id>")
