# Labs

Hands-on labs on a Seeed XIAO ESP32-S3, from first contact to secure boot.

| Lab | Topic | Key result |
|---|---|---|
| [Lab 01](lab01-esp32-first-contact/) | Chip identification + eFuse security review | Board fully open: full 8 MB firmware dumped in 50 s over USB |
| [Lab 02](lab02-first-firmware/) | First firmware with ESP-IDF + boot chain | ROM → bootloader → app, no signature check; SHA-256 detects corruption only |
| Lab 03 | Secure boot (planned) | Signed firmware accepted, unsigned rejected |
