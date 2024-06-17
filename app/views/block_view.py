from flask import render_template
from app import app
from app.models import Block

@app.route('/blocks/<int:height>')
def block_view(height):
    block = Block.query.get(height)
    return render_template('block.html', block=block)
