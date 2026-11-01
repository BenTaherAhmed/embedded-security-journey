# Lab 02 — First firmware with ESP-IDF and the boot chain

## Goal
Build and flash my own firmware, then understand the boot chain
and the integrity hash, before enabling secure boot.

## Tools
ESP-IDF v6.1 (EIM installer) · esptool v5.6.0 · Seeed XIAO ESP32-S3

## Commands
```
idf.py set-target esp32s3
idf.py build
idf.py -p COM4 flash monitor
esptool image-info build/hello_world.bin
```

## What I changed
`main/hello_world_main.c`: message changed to "Hello from Ahmed - Lab 02!"
The chip accepted and ran my modified firmware without any check.

## Boot chain (see boot-log.txt)
| Order | Stage | Location | Proof in my log |
|---|---|---|---|
| 1 | ROM bootloader | Inside the chip (read-only, from 2021) | `ESP-ROM:esp32s3-20210327` · `boot:0x8 (SPI_FAST_FLASH_BOOT)` |
| 2 | 2nd-stage bootloader | Flash 0x0 | `I (24) boot: ESP-IDF v6.1 2nd stage bootloader` |
| 3 | Application | Flash 0x10000 | `I (130) boot: Loaded app from partition at offset 0x10000` |

The ROM copies the bootloader into RAM (`load:` lines) and jumps to it
(`entry 0x403c8904`). The bootloader then loads the app (`esp_image: segment 0–5`).
Today, no stage verifies the signature of the next one.

## Partition table (from the boot log)
| Partition | Offset | Size | Contents | Security note |
|---|---|---|---|---|
| nvs | 0x9000 | 24 KB | Settings storage | Wi-Fi passwords stored here, not encrypted |
| phy_init | 0xF000 | 4 KB | Radio calibration | — |
| factory | 0x10000 | 1 MB | My application | Single app slot: no OTA update, no fallback |

## Integrity hash (see image-info.txt)
```
Checksum: 0xfd (valid)
Validation hash: 2e35ace4c639a02a29f079fcbd995d02ae9be716061ae2ef37d1a49ba0b589c0 (valid)
Secure version: 0
```

ESP-IDF appends a SHA-256 hash to the firmware, checked at every boot.
It only detects corruption: anyone who modifies the firmware can recompute
the hash (the build did it for me). Proving WHO made the firmware needs a
signature, which is what secure boot adds.

## Other observations
- Flash size mismatch (fixed): the project used the 2 MB default, but the board has 8 MB.
  Fixed with `idf.py menuconfig` → Serial flasher config → Flash size → 8 MB.
  The boot log now shows `SPI Flash Size : 8MB` and the warning is gone.
- CPU runs at 160 MHz (default), not the 240 MHz maximum.
- `App version: 13af371` is my Git commit ID: every build is traceable.
- `app_main()` starts on CPU0 (core 0) in ESP-IDF.
- Lines starting with `---` are added by the monitor on my PC, not printed by the chip.

## What I learned
- The boot chain has 3 stages (ROM → bootloader → app), and today each stage
  trusts the next one blindly. Secure boot will make each stage verify a signature.
- The ROM bootloader can never be updated: a bug in it stays forever.
- A SHA-256 hash in the firmware detects corruption, not attacks.
- The boot log leaks useful information to an attacker (ESP-IDF version, build dates,
  memory map, partition layout). Real products reduce or disable it.
- Secrets in the nvs partition are stored in clear: with the Lab 01 dump,
  an attacker could read the Wi-Fi password. NVS and flash encryption fix this.
- Reading a log carefully reveals configuration mistakes (flash size mismatch).

## Next
Lab 03: secure boot — sign the firmware and see an unsigned one rejected.
