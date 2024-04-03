from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP # Padding, Cryptographic Message Syntax Version 1 - Optimal Asymmetric Encryption Padding

# private key
with open("private_key.pem", "rb") as file:
    private_key = RSA.import_key(file.read())

with open("ciphertext.txt", "rb") as file:
    ciphertext = file.read()

# Decryption
cipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = cipher_rsa.decrypt(ciphertext)

print("Decrypted plaintext:", plaintext.decode())


'''
PKCS1_OAEP features:

Optimal Asymmetric Encryption Padding (OAEP): 
OAEP is a padding scheme used in RSA encryption to add randomness to the plaintext before encryption. This randomness helps prevent certain cryptographic attacks, such as chosen ciphertext attacks.

Padding Scheme: 
PKCS1_OAEP padding scheme pads the input message before encryption. It adds a random value to the plaintext, ensuring that the same plaintext encrypted multiple times results in different ciphertexts. This adds probabilistic encryption, which is desirable for security.

Hash Function: 
PKCS1_OAEP typically uses a hash function, such as SHA-1 or SHA-256, to hash the plaintext and the padding before encryption. This provides integrity protection, ensuring that any modification to the ciphertext or padding can be detected during decryption.

Security: 
PKCS1_OAEP is designed to provide a high level of security when used correctly. It prevents certain attacks, such as padding oracle attacks, by ensuring that decryption errors are not exposed to attackers.

In Python's Crypto library, PKCS1_OAEP is implemented as a cipher module (Crypto.Cipher.PKCS1_OAEP). It provides encryption and decryption functions compatible with RSA public and private keys. When using PKCS1_OAEP for encryption, you need the public key; for decryption, you need the private key.

'''