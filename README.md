# Rainbow Phone Number Attack Demo

A simple script to demonstrate a rainbow-table-style attack on phone-number hashes, inspired by the 2024 KakaoPay data breach in South Korea. In that incident, user passwords were hashed with SHA-256 **without** a salt, making them vulnerable to dictionary or rainbow-table attacks. This code lets you experiment with the same principle against phone-number-based hashes.

## Usage

```bash
python rainbowPhoneNumber.py
