# Cryptographic Utilities for EMV

This module provides cryptographic utilities for DES and RSA operations used in EMV (Europay, MasterCard, and Visa) standards.

## DES Encryption and Decryption

```python
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class DESUtils:
    @staticmethod
    def encrypt(key: bytes, plaintext: bytes) -> bytes:
        cipher = DES.new(key, DES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext, DES.block_size))
        return cipher.iv + ct_bytes

    @staticmethod
    def decrypt(key: bytes, ciphertext: bytes) -> bytes:
        iv = ciphertext[:DES.block_size]
        ct = ciphertext[DES.block_size:]
        cipher = DES.new(key, DES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), DES.block_size)
```

## RSA Encryption and Decryption

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSAUtils:
    @staticmethod
    def encrypt(public_key: RSA.RsaKey, plaintext: bytes) -> bytes:
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(plaintext)

    @staticmethod
    def decrypt(private_key: RSA.RsaKey, ciphertext: bytes) -> bytes:
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(ciphertext)
```

## Usage

To use these utilities, import the respective classes and call the methods with the required parameters.
