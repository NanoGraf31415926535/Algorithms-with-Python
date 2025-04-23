from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend  # Import default_backend

def generate_rsa_key_pair(key_size=2048):
    """Generates an RSA private and public key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_rsa(plaintext, public_key):
    """Encrypts plaintext using RSA public key."""
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_rsa(ciphertext, private_key):
    """Decrypts ciphertext using RSA private key."""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# Example Usage for RSA
if __name__ == "__main__":
    private_key, public_key = generate_rsa_key_pair()
    rsa_plaintext = b"This is a secret message encrypted with RSA."
    rsa_ciphertext = encrypt_rsa(rsa_plaintext, public_key)
    rsa_decrypted_plaintext = decrypt_rsa(rsa_ciphertext, private_key)

    print("\nOriginal RSA Plaintext:", rsa_plaintext.decode())
    print("RSA Ciphertext:", rsa_ciphertext.hex())
    print("Decrypted RSA Plaintext:", rsa_decrypted_plaintext.decode())
    assert rsa_plaintext == rsa_decrypted_plaintext