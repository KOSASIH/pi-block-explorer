from app.models import Block

class BlockService:
    def get_block(self, height):
        return Block.query.get(height)

    def get_blocks(self, start, end):
        return Block.query.filter(Block.height >= start, Block.height <= end).all()

    def create_block(self, height, hash, timestamp):
        block = Block(height=height, hash=hash, timestamp=timestamp)
        db.session.add(block)
        db.session.commit()
        return block
