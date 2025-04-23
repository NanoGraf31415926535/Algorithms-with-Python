import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_aes(plaintext, key):
    """Encrypts plaintext using AES with CBC mode and PKCS#7 padding."""
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    iv = os.urandom(16)  # Initialization vector; should be unique for each encryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv + ciphertext  # Prepend IV to the ciphertext

def decrypt_aes(ciphertext_with_iv, key):
    """Decrypts ciphertext encrypted with AES in CBC mode and removes PKCS#7 padding."""
    iv = ciphertext_with_iv[:16]
    ciphertext = ciphertext_with_iv[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext

# Example Usage for AES
if __name__ == "__main__":
    key = os.urandom(32)  # 256-bit key
    plaintext = b"This is a secret message encrypted with AES."
    ciphertext_with_iv = encrypt_aes(plaintext, key)
    decrypted_plaintext = decrypt_aes(ciphertext_with_iv, key)

    print("Original Plaintext:", plaintext.decode())
    print("Ciphertext (with IV):", ciphertext_with_iv.hex())
    print("Decrypted Plaintext:", decrypted_plaintext.decode())
    assert plaintext == decrypted_plaintext