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
- Commands I ran and what each one does:
- What happened when I changed one byte of the file:
- Hash vs MAC vs signature, in my own words:

## 4. Firmware signing project (weekend)
- What I built: `sign_firmware.py`, `verify_firmware.py`
- Why the device stores only the public key:
- What happens if the private key leaks:

## 5. Questions I still have
-

## 6. Next week
-
