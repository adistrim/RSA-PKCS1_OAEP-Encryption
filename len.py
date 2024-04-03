from Crypto.PublicKey import RSA

with open("private_key.pem", "rb") as file:
    private_key = RSA.import_key(file.read())

with open("public_key.pem", "rb") as file:
    public_key = RSA.import_key(file.read())

print("Private key:", len(private_key.export_key()))
print("Public key:", len(public_key.export_key()))
