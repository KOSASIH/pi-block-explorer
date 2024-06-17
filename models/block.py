# block.py
from app import db
from models import Block

class BlockService:
    def get_block_by_height(self, height):
        return Block.query.filter_by(height=height).first()

    def get_latest_block(self):
        return Block.query.order_by(Block.timestamp.desc()).first()
