# Week 1 — Security foundations

**Dates:** 2026-10-26 → 2026-11-01
**Time spent:** _ h

## 1. Key concepts (Day 2)
Write each one in 1–2 sentences, plus one example from a car or an industrial device.

| Term | My definition | Example |
|---|---|---|
| Asset |Something valuable that we need to protect |The battery pack and the BMS that protects it during charging |
| Threat |Someone or something that could cause harm | A hacker who takes control of a public charger and wants to damage the cars plugged into it|
| Vulnerability | A weakness that lets the threat succeed | The car trusts the charger’s messages without checking them (older DIN 70121 charging has no encryption) |
| Risk | 	How likely an attack is × how bad the result would be | Public chargers are exposed on the internet (likely) and an overcharged battery can catch fire (severe), so the risk is high |
| Attack surface | All the places where an attacker can reach the system | The charging cable, the charger’s internet connection, the car’s 4G and Bluetooth, the mobile app |
| Confidentiality | Only authorized people can see the information | The Plug & Charge certificate key inside the car must never be readable, or someone could charge on your account |
| Integrity | Information can’t be changed without permission | The charging limits sent by the BMS (max voltage and current) must not be modified on the way |
| Availability | The system keeps working when you need it | An attacker must not be able to stop all charging. Researchers showed this is possible with radio interference (the “Brokenwire” attack) |

## 2. Thinking like an attacker (Day 2)
Device I chose: public EV charging station (DC fast charger)

1. A hacked charger reads the car's ID and Plug & Charge certificate,
   then reuses them to charge on the victim's account. (Confidentiality)
2. An attacker inserts a device in the charging cable and modifies the
   messages, e.g. the current limits sent by the BMS. (Integrity)
3. An attacker nearby listens to the charging communication by radio,
   or jams it to stop charging (Brokenwire). (Confidentiality, Availability)
4. An attacker uses the car's 4G connection while it is parked and charging
   to attack the telematics unit remotely. (All three, remote and scalable)
5. An attacker hacks the operator's backend and uses OCPP to stop all
   chargers or push fake firmware to them, which then attacks the cars.
   (Availability, Integrity: highest scale, can even affect the grid)

Lesson: "hack the charger → open the doors" is an attack chain; the gateway
between ECUs forces the attacker to find a second vulnerability.

## 3. Crypto with openssl (Day 3)
Commands I ran (Git Bash):
| Command | What it does |
|---|---|
| `openssl dgst -sha256 file.bin` | Computes the SHA-256 hash (fingerprint) of the file |
| `openssl dgst -sha256 -hmac mysecret file.bin` | Computes a MAC: hash mixed with a secret key |
| `openssl enc -aes-256-cbc -pbkdf2 -in file.bin -out file.enc` | Encrypts the file with AES-256 (key derived from a password) |
| `openssl enc -d -aes-256-cbc -pbkdf2 -in file.enc -out back.bin` | Decrypts it back |

What happened when I changed one letter ("unlock door" → "Unlock door"):
the hash changed completely, not just one character. Changing only the HMAC
key changed the MAC but not the hash: the MAC depends on the secret, the hash does not.

Hash vs MAC vs signature, in my own words:
| | Key | Who can create it | Proves | Example |
|---|---|---|---|---|
| Hash | None | Anyone | Data not changed (accidents) | Integrity hash at the end of ESP-IDF firmware |
| MAC | One shared secret | Anyone with the key | Not changed + made by a key holder | SecOC on CAN messages |
| Signature | Private + public pair | Only the private-key owner | Not changed + made by THIS sender | Secure boot, firmware updates |

## 4. Firmware signing project (weekend)
Code: `projects/firmware-signing/` (keygen, sign, verify — ECDSA P-256 + SHA-256)

| Test | Result |
|---|---|
| Original firmware, manufacturer signature | VALID |
| Firmware modified after signing | REJECTED |
| Attacker signs modified firmware with their own key | REJECTED |

- Why the device stores only the public key: the public key can only CHECK
  signatures, not create them. Even if an attacker extracts it from the chip,
  they cannot sign fake firmware.
- What happens if the private key leaks: the attacker can sign any firmware and
  every device will accept it. All devices are compromised until the key is
  revoked and replaced. That is why private keys live in an HSM, never in a repo.
- What must be protected in the device: the public key must not be REPLACEABLE
  (stored in ROM/eFuses), otherwise the attacker swaps it for their own.

## 5. Questions I still have
- How does the ESP32-S3 store the secure boot key in eFuses, and can it be revoked?
- What happens on a real car if the OEM signing key leaks?
- Can fault injection (glitching) skip the signature check?

## 6. Week 1 summary and next week
Done: security basics (TryHackMe), EV-charger threat analysis, crypto with openssl,
Lab 01 (eFuse review + firmware dump), Lab 02 (first firmware + boot chain),
firmware signing project.

Week 2:
- Lab 03 preparation: ESP32-S3 Secure Boot v2 — read the docs, generate the
  signing key with espsecure, plan every step BEFORE burning any eFuse
- Serious Cryptography: chapters 2–3 (randomness, cryptographic security)
- TryHackMe: Network Fundamentals (Pre Security path)


