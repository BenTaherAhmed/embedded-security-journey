\# Lab 01 — ESP32-S3 first contact



\## Goal

Identify the chip and read its security configuration (eFuses). Read-only, nothing changed.



\## Hardware \& tools

Seeed XIAO ESP32-S3 · esptool / espefuse v5.6.0 · Git Bash on Windows



\## Commands

esptool -p COM4 chip-id

esptool -p COM4 flash-id

espefuse -p COM4 summary



\## Results

\- Chip: ESP32-S3 (QFN56) rev v0.2, dual core 240 MHz, Wi-Fi + BLE 5

\- Memory: 8 MB flash (quad SPI), 8 MB PSRAM

\- USB mode: native USB-Serial/JTAG

\- Built-in CAN controller (TWAI) available



\## Security state

| Protection | State | Meaning for an attacker |

|---|---|---|

| Secure boot | Off | Any firmware boots, including malicious firmware |

| Flash encryption | Off | Firmware and secrets can be dumped in clear |

| USB download mode | Open | Anyone with USB access can read/write flash |

| JTAG debug | Open | A debugger can halt the CPU and read memory |

| Key slots | Empty (6 free) | No keys provisioned yet |



\## What I learned

\- ...



\## Next

Lab 02: build and flash my own firmware with ESP-IDF.

