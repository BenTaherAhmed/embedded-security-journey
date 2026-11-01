# Firmware signing — how secure boot works, in 3 Python scripts

## Goal
Simulate what a manufacturer and a device do in secure boot:
the manufacturer signs the firmware with a PRIVATE key, the device checks it with the PUBLIC key only.

## Scripts
| Script | Side | What it does |
|---|---|---|
| `keygen.py` | Manufacturer | Creates an ECDSA P-256 key pair: `private_key.pem` (secret) + `public_key.pem` |
| `sign_firmware.py` | Manufacturer | Hashes the firmware (SHA-256) and signs it → `firmware.bin.sig` |
| `verify_firmware.py` | Device | Verifies the signature with the public key → VALID (boot) or REJECTED |

## How to run
```
pip install cryptography
echo "unlock door" > firmware.bin
python keygen.py
python sign_firmware.py
python verify_firmware.py
```

## Experiments and results
| Test | Result | Why |
|---|---|---|
| Original firmware | <VALID / REJECTED> | |
| Firmware modified after signing | <...> | |
| Attacker signs modified firmware with their own key | <...> | |

## What I learned
- Why the device stores only the public key: ...
- What happens if the private key leaks: ...
- Link with Lab 03 (ESP32 secure boot): ...

## Security note
`private_key.pem` is never committed (see `.gitignore`). In real life it lives in an HSM, not on a laptop.
