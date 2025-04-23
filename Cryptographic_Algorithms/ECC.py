from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

def generate_ec_key_pair():
    """Generates an ECDH private and public key pair using NIST P-256 curve."""
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def derive_ec_shared_secret(private_key, public_key, salt):
    """Derives a shared secret using ECDH with a given salt."""
    shared_secret = private_key.exchange(ec.ECDH(), public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        info=b'handshake data',
        backend=default_backend()
    ).derive(shared_secret)
    return derived_key

# Example Usage for ECC (Key Exchange - not direct encryption like RSA)
if __name__ == "__main__":
    # Alice's key pair
    alice_private_key, alice_public_key = generate_ec_key_pair()

    # Bob's key pair
    bob_private_key, bob_public_key = generate_ec_key_pair()

    # Agree on a common salt
    common_salt = os.urandom(16)

    # Alice derives shared secret with Bob's public key using the common salt
    alice_shared_secret = derive_ec_shared_secret(alice_private_key, bob_public_key, common_salt)

    # Bob derives shared secret with Alice's public key using the same common salt
    bob_shared_secret = derive_ec_shared_secret(bob_private_key, alice_public_key, common_salt)

    print("\nAlice's Shared Secret:", alice_shared_secret.hex())
    print("Bob's Shared Secret:", bob_shared_secret.hex())
    assert alice_shared_secret == bob_shared_secret