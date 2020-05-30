import hashlib
import json
from time import time
from uuid import uuid4



#We will create a blockchain class whose constructor creates an initial empty list
#(to store our blockchain) and another to store transactions.
class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #Create a genesis block
        self.new_block(previous_hash=1, proof = 100)

    def new_block(self, proof, previous_hash=None):
        #Create a new block

        block = {
            'index':len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        #reset the transactions
        self.current_transactions = []

        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        #creates  a new transaction to go into the next mined block

        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """ Creates a SHA-256 hash of a block
            We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]


    def proof_of_work(self, last_proof):
        """
        Simple Proof of work algorithm:
        - find p' such that hash(pp') contains leading 4 zeros, where p in previous p'
        - p is the previous proof and p' is the new proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof


    def valid_proof(last_proof, proof):
        # Validated does hash(last_proof, proof) contains leading 4 zeros

        guess = f'{last_proof}{proof}'.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"
