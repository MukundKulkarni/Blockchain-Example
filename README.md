# Blockchain-Example

A blockchain is an immutable, sequential chain of records called Blocks. They can contain transactions, files or any data you like, really. But the important thing is that they’re chained together using hashes.
<br>
# Blocks

Each Block has an index, a timestamp (in Unix time), a list of transactions, a proof, and the hash of the previous Block.<br>
Here's an Example of a block

```python
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```
# Understanding Proof of Work

The Proof of Work algorithm (PoW) is how new blocks are created or mined from the blockchain.
The goal of PoW is to discover a number which solves a problem. The number must be difficult to
find but easy to verify—computationally speaking—by anyone on the network.<br>

In Bitcoin the Proof of Work algorithm used is called __HASHCASH__.<br>
It’s the algorithm that miners race to solve in order to create a new block. In general,
the difficulty is determined by the number of characters searched for in a string.
 The miners are then rewarded for their solution by receiving a coin—in a transaction.<br>

 The network is able to easily verify their solution.
