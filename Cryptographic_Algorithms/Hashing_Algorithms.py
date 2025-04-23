import hashlib

def hash_sha256(data):
    """Computes the SHA-256 hash of the input data."""
    m = hashlib.sha256()
    m.update(data)
    return m.hexdigest()

def hash_md5(data):
    """Computes the MD5 hash of the input data."""
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

# Example Usage for Hashing
if __name__ == "__main__":
    message = b"This data needs to be hashed."
    sha256_digest = hash_sha256(message)
    md5_digest = hash_md5(message)

    print("\nOriginal Message:", message.decode())
    print("SHA-256 Hash:", sha256_digest)
    print("MD5 Hash:", md5_digest)

    modified_message = b"This data needs to be hashed!"
    sha256_digest_modified = hash_sha256(modified_message)
    md5_digest_modified = hash_md5(modified_message)

    print("Modified Message:", modified_message.decode())
    print("SHA-256 Hash (modified):", sha256_digest_modified)
    print("MD5 Hash (modified):", md5_digest_modified)