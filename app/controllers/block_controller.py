from flask import request, jsonify
from app import app
from app.models import Block

@app.route('/blocks/<int:height>', methods=['GET'])
def get_block_by_height(height):
    """
    Fetches a block by its height from the blockchain.

    Args:
        height (int): The block height.

    Returns:
        dict: A dictionary containing block data.
    """
    block = Block.query.get(height)
    if block:
        return jsonify({'block': block.to_dict()})
    return jsonify({'error': 'Block not found'}), 404
