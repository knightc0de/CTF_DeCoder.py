# CTF_DeCoder.py

**CTF_DeCoder.py** is a simple Python command-line tool designed for cybersecurity enthusiasts and CTF (Capture The Flag) players. It supports decoding of common encoded formats such as:

- Base64
- Base32
- Hexadecimal
- ROT13
- Binary (ASCII)
- ⚙ Command-line interface (CLI) for flexibility
-  Easily extendable with new encodings

> Decode CTF strings easily and quickly right from your terminal.

---


---

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/knightc0de/CTF_DeCoder.py.git
   cd CTF_DeCoder.py
   python3 decoder.py [options]

## Usage 
 - python3 decoder.py --b64 aGVsbG8=
 - python3 decoder.py --hex 68656c6c6f
 - python3 decoder.py --r13 uryyb
 - python3 decoder.py --Binary "01101000 01100101 01101100 01101100 01101111"
 - python3 decoder.py --b32 NBSWY3DP

## Options
**Option	Description	Example**
---
- --b64	Decode Base64 string	--b64 aGVsbG8=
- --b32	Decode Base32 string	--b32 NBSWY3DP
- --hex	Decode Hexadecimal string	--hex 68656c6c6f
- --r13	Decode ROT13-encoded string	--r13 uryyb
- --Binary	Decode Binary to ASCII	--Binary "01101000 ..."
- -V	Show version	-V
---
> All options support multiple values: e.g., --b64 aGVs bG8=

 **Example Output**
```bash
$ python3 decoder.py --b64 aGVsbG8=
Base64 Decoded: hello

$ python3 decoder.py --hex 68656c6c6f
Hex Decoded: hello

$ python3 decoder.py --Binary "01101000 01100101 01101100 01101100 01101111"
Binary Decoded: hello
``` 
# Author 
Created by @knightc0de

