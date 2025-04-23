# Cryptographic Algorithms

These algorithms are fundamental for ensuring secure communication and protecting data confidentiality and integrity. We'll explore the categories you've listed and touch upon the principles behind some of the prominent algorithms.

**The Core Goal: Security**

Cryptographic algorithms aim to achieve several security objectives:

* **Confidentiality:** Ensuring that only authorized parties can read the data.
* **Integrity:** Guaranteeing that data has not been tampered with during transmission or storage.
* **Authentication:** Verifying the identity of the communicating parties.
* **Non-repudiation:** Preventing a sender from denying that they sent a message.

Let's look at the categories you've mentioned:

**1. Symmetric-key Cryptography: One Key to Rule Them All**

In symmetric-key cryptography, the same secret key is used for both encryption (transforming plaintext into ciphertext) and decryption (transforming ciphertext back into plaintext). This makes it efficient but requires a secure way to share the secret key between communicating parties.

* **AES (Advanced Encryption Standard):** This is the current gold standard for symmetric encryption. It's a block cipher, meaning it encrypts data in fixed-size blocks (typically 128 bits). AES is highly secure and widely adopted due to its strong resistance against known attacks. It supports key sizes of 128, 192, and 256 bits, with larger key sizes offering greater security.

    * **Principle:** AES operates through a series of substitution and permutation steps (including S-boxes, ShiftRows, MixColumns) repeated for a certain number of rounds, which depends on the key size. These operations are designed to thoroughly mix and scramble the data.

* **DES (Data Encryption Standard):** An older symmetric block cipher that was once the dominant standard. However, its relatively small key size of 56 bits makes it vulnerable to brute-force attacks. While still found in some legacy systems, it has largely been superseded by AES. There's also Triple DES (3DES), which applies the DES algorithm three times to increase the key size, offering more security but at the cost of performance.

    * **Principle:** Similar to AES, DES uses rounds of substitution and permutation. However, it has a more complex Feistel structure.

**2. Asymmetric-key Cryptography: Different Keys for Different Tasks**

Asymmetric-key cryptography (also known as public-key cryptography) uses a pair of keys: a public key, which can be freely distributed, and a private key, which must be kept secret by its owner.

* **Encryption:** If Alice wants to send a secure message to Bob, she encrypts it using Bob's public key. Only Bob can decrypt the message using his private key.
* **Digital Signatures:** If Alice wants to sign a document, she uses her private key to create a digital signature. Anyone can verify the signature using Alice's public key, confirming the authenticity and integrity of the document.

* **RSA (Rivest–Shamir–Adleman):** One of the earliest and most widely used public-key cryptosystems. Its security relies on the mathematical difficulty of factoring large composite numbers into their prime factors.

    * **Principle:** RSA involves generating a public key consisting of a modulus (the product of two large prime numbers) and a public exponent. The private key consists of the same modulus and a private exponent, which is related to the prime factors. Encryption and decryption involve modular exponentiation using these keys.

* **Elliptic Curve Cryptography (ECC):** A more modern public-key cryptography approach that offers comparable security to RSA but with smaller key sizes. This makes it particularly attractive for resource-constrained environments like mobile devices. Its security is based on the difficulty of solving the elliptic curve discrete logarithm problem.

    * **Principle:** ECC relies on the properties of elliptic curves defined over finite fields. Public and private keys are points on these curves, and cryptographic operations involve scalar multiplication of these points.

**3. Hashing Algorithms: One-Way Functions for Integrity**

Hashing algorithms (also known as cryptographic hash functions) are one-way functions that take an input (of any size) and produce a fixed-size output called a hash or message digest. These functions have several important properties:

* **Deterministic:** The same input always produces the same hash output.
* **Preimage resistance:** It should be computationally infeasible to find the original input given only the hash output.
* **Second preimage resistance:** Given an input and its hash, it should be computationally infeasible to find a different input that produces the same hash.
* **Collision resistance:** It should be computationally infeasible to find two different inputs that produce the same hash output.

Hashing algorithms are primarily used for verifying data integrity. If the hash of a file changes, it indicates that the file has been modified. They are also used in digital signatures and password storage (by hashing passwords instead of storing them in plaintext).

* **SHA-256 (Secure Hash Algorithm 256-bit):** A widely used and secure hashing algorithm that produces a 256-bit hash value. It's part of the SHA-2 family of algorithms and is considered robust against known attacks.

    * **Principle:** SHA-256 involves a series of bitwise operations, modular additions, and compression functions applied to the input data in blocks.

* **MD5 (Message Digest Algorithm 5):** An older hashing algorithm that produces a 128-bit hash value. While it was once widely used, MD5 is now considered cryptographically weak due to the discovery of practical collision attacks. This means it's relatively easy to find two different inputs that produce the same MD5 hash, making it unsuitable for applications where collision resistance is critical (like digital signatures).

    * **Principle:** MD5 also involves a series of bitwise operations and modular additions, but its design is less complex than SHA-256, which contributes to its vulnerability.