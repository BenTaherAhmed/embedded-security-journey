# sign_firmware.py - manufacturer side: sign the firmware with the PRIVATE key
import hashlib, sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

firmware_file = sys.argv[1] if len(sys.argv) > 1 else "firmware.bin"
firmware = open(firmware_file, "rb").read()
print("Firmware SHA-256:", hashlib.sha256(firmware).hexdigest())

private_key = serialization.load_pem_private_key(open("private_key.pem", "rb").read(), password=None)
signature = private_key.sign(firmware, ec.ECDSA(hashes.SHA256()))  # hashes, then signs the hash

open(firmware_file + ".sig", "wb").write(signature)
print(f"Signature written to {firmware_file}.sig ({len(signature)} bytes)")
