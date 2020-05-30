import hashlib
import json

from time import time
from uuid import uuid4
from flask import Flask
from flask import jsonify
from textwrap import dedent
from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    #"We will mine a new block."

    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof, )

    #Award a coin for mining

    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    #Add the new block to chain

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message' :"New block Forged",
        'index':block['index'],
        'transactions' :block['transactions'],
        'proof' :block['proof'],
        'previous_hash': block['previous_hash'],

    }

    return jsonify(response), 200



@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    # "We will add a new transaction."
    values = request.get_json()

    # Check if the required fields are in the posted data
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required):
        return "Missing Values", 400

    #Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}

    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5000)
