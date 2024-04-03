from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generating RSA key pair
key = RSA.generate(2048)

public_key = key.publickey()
private_key = key

with open("plaintext.txt", "rb") as file:
    plaintext = file.read()

# Encryption
cipher_rsa = PKCS1_OAEP.new(public_key)
ciphertext = cipher_rsa.encrypt(plaintext)

# Saving keys
with open("public_key.pem", "wb") as file:
    file.write(public_key.export_key(format='PEM'))

with open("private_key.pem", "wb") as file:
    file.write(private_key.export_key(format='PEM'))

with open("ciphertext.txt", "wb") as file:
    file.write(ciphertext)

print("Public and private keys saved to 'public_key.pem' and 'private_key.pem' files.")
print("Ciphertext saved to 'ciphertext.txt' file.")
