# keygen.py - create the manufacturer's key pair (ECDSA P-256)
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

private_key = ec.generate_private_key(ec.SECP256R1())

with open("private_key.pem", "wb") as f:   # SECRET: stays with the manufacturer
    f.write(private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()))

with open("public_key.pem", "wb") as f:    # PUBLIC: goes into the device
    f.write(private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo))

print("Created private_key.pem (keep secret!) and public_key.pem")
