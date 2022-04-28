
import pickle
from socket_client_server import Client
from lamport import LamportSignature
from merkle_tree import MerkleTree


def main():
    N = 32  # Limited number of messages

    # Generate 'N' private/public key pairs (Xi, Yi) from the Lamport signature scheme
    key_pairs = [LamportSignature() for _ in range(N)]  # Private key of the Merkle signature scheme

    # The leaves of the tree are the hashed values of the public keys Y0, ..., YN
    mk = MerkleTree(n_leaves=N)
    for i in range(N):
        mk.add_node(key_pairs[i].get_key('public', concatenate=True), (0, i), hashed=False)

    # Build Merkle tree
    mk.generate_tree()
    pub = mk.get_root()  # Public key of the Merkle signature scheme

    # Merkle signature generation using a chosen pair of keys (Xi, Yi) from the Lamport signature scheme
    # sig = concatenate(sig_prime, Yi, auth(0), ..., auth(n-1))
    pair = 3
    sig = []
    M = input()
    sig_prime = key_pairs[pair].sign(M)
    sig.append(sig_prime)
    sig.append(key_pairs[pair].get_key('public', concatenate=True))
    sig.append(mk.get_authentification_path_hashes(pair))
    # Send to receiver the public key 'pub' (tree root), the message 'M' and the Merkle signature 'sig'.
    client = Client()

    msg = (32, pair, pub, M, sig)
    client.send(pickle.dumps(msg))
    client.close()


if __name__ == "__main__":
    main()
