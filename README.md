# Merkle Tree and Lamport signature Python implementation

## Merkle tree
In cryptography and computer science, a hash tree or Merkle tree is a tree in which every non-leaf node is labelled with the hash of the labels or values (in case of leaves) of its child nodes. Hash trees allow efficient and secure verification of the contents of large data structures. Hash trees are a generalization of hash lists and hash chains.

## Lamport One-Time Signature Scheme
The Lamport One-Time Signature Scheme (LOTSS) is a signature scheme in which the public key can only be used to sign a single message. The security of the LOTSS is based on cryptographic hash functions. Any secure hash function can be used, which makes this signature scheme very adjustable. If a hash function becomes insecure it can easily be exchanged by another secure hash function. In the following first the key generation, then the signing algorithm and finally the verification algorithm are described.

## Requirements
- Python 3
- [bitstring](https://pypi.python.org/pypi/bitstring/3.1.5)

## How to Run
- First run main_server_side.py file
- After that run main_client_side.py file and provide a message in input