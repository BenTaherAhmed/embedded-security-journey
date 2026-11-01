# Lab 01 — ESP32-S3 first contact

## Goal
Identify the chip and read its security configuration (eFuses). Read-only, nothing changed.

## Hardware & tools
Seeed XIAO ESP32-S3 · esptool / espefuse v5.6.0 · Git Bash on Windows

## Commands
```
esptool -p COM4 chip-id
esptool -p COM4 flash-id
espefuse -p COM4 summary
```

## Results
- Chip: ESP32-S3 (QFN56) rev v0.2, dual core 240 MHz, Wi-Fi + BLE 5
- Memory: 8 MB flash (quad SPI), 8 MB PSRAM
- USB mode: native USB-Serial/JTAG
- Built-in CAN controller (TWAI) available

## Security state (see efuse-summary.txt)
| Protection | State | Meaning for an attacker |
|---|---|---|
| Secure boot | Off | Any firmware boots, including malicious firmware |
| Flash encryption | Off | Firmware and secrets can be dumped in clear |
| USB download mode | Open | Anyone with USB access can read/write flash |
| JTAG debug | Open | A debugger can halt the CPU and read memory |
| Key slots | Empty (6 free) | No keys provisioned yet |

## Bonus: firmware dump (attacker view)
```
esptool -p COM4 read-flash 0 0x800000 dump.bin
```
- The full 8 MB flash was copied in about 50 seconds, with only a USB cable.
- Readable text inside the dump (versions, messages, URLs) helps an attacker
  understand and reverse-engineer the firmware.
- The dump is not published (factory firmware, ignored by .gitignore).

## What I learned
- The ESP32-S3 has strong security hardware (secure boot, flash encryption,
  6 key slots, crypto accelerators), but a new chip ships with all of it OFF.
  Turning it on is the manufacturer's job; forgetting it is a common real-world mistake.
- eFuses are one-time switches: once burned, they can never be reset.
  Reading them (espefuse summary) is safe; burning them is permanent.
- Physical USB access + open download mode = full access to the firmware.
- Two protections would have stopped my dump: flash encryption (unreadable data)
  and disabling download mode (no read-flash at all). Secure boot would block
  the next step: flashing malicious firmware.
- The CPU is Xtensa LX7 (not ARM), so reverse engineering needs Xtensa support.
- The chip has a CAN controller (TWAI): useful for automotive labs later.
- Masking device identifiers (MAC, unique ID) before publishing is a security habit.

## Next
Lab 02: build and flash my own firmware with ESP-IDF.
