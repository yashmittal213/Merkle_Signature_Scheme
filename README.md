# Merkle Tree and Lamport signature Python implementation

## Merkle tree
In cryptography and computer science, a hash tree or Merkle tree is a tree in which every non-leaf node is labelled with the hash of the labels or values (in case of leaves) of its child nodes. Hash trees allow efficient and secure verification of the contents of large data structures.

## Lamport One-Time Signature Scheme
The Lamport One-Time Signature Scheme is a signature scheme in which the public key can only be used to sign a single message. The security of the LOTSS is based on cryptographic hash functions. Any secure hash function can be used, which makes this signature scheme very adjustable.

## Requirements
- Python 3
- [bitstring](https://pypi.python.org/pypi/bitstring/3.1.5)
It needs to assured that both of these requirements are installed in the system.
To install bitstring 'pip' command has been used as mentioned in its site.

## How to Run
- First run main_server_side.py file
- After that run main_client_side.py file and provide a message in input.
- Finally we get the result of the verification on the server side terminal.