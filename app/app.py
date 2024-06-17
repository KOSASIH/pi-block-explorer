from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.pi-network.io/block')
    block = response.json()
    return f"Latest Pi Block: {block['height']}"

if __name__ == '__main__':
    app.run(debug=True)
