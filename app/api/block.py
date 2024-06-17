from flask import Blueprint, request, jsonify
from app.services.block import BlockService

block_api = Blueprint('block_api', __name__)

@block_api.route('/blocks/<int:height>')
def get_block(height):
    block = BlockService().get_block(height)
    if block:
        return jsonify({'block': block.to_dict()})
    return jsonify({'error': 'Block not found'}), 404

@block_api.route('/blocks', methods=['GET'])
def get_blocks():
    start = request.args.get('start', type=int)
    end = request.args.get('end', type=int)
    blocks = BlockService().get_blocks(start, end)
    return jsonify({'blocks': [block.to_dict() for block in blocks]})
