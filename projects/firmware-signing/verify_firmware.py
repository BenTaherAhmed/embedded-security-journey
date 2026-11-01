# verify_firmware.py - device side: verify with the PUBLIC key only
import hashlib, sys
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

firmware_file = sys.argv[1] if len(sys.argv) > 1 else "firmware.bin"
firmware = open(firmware_file, "rb").read()
signature = open(firmware_file + ".sig", "rb").read()
public_key = serialization.load_pem_public_key(open("public_key.pem", "rb").read())

print("Firmware SHA-256:", hashlib.sha256(firmware).hexdigest())
try:
    public_key.verify(signature, firmware, ec.ECDSA(hashes.SHA256()))
    print("VALID: firmware is genuine -> boot")
except InvalidSignature:
    print("REJECTED: firmware modified or not signed by the manufacturer -> do not boot")
    sys.exit(1)
