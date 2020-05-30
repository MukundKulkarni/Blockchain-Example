import hashlib
import json

from time import time
from uuid import uuid4
from flask import Flask
from textwrap import dedent
from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We will mine a new block."

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We will add a new transaction."

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jasonify(response), 200

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
