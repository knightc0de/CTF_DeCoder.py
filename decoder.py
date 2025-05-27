#!/usr/bin/env python3
"""
CTF Decoder Tool
Author: @knightc0de
Supported Encodings: Base64, Base32, Hex, ROT13, Binary to ASCII

Usage:
    python3 decoder.py --b64 aGVsbG8=
    python3 decoder.py --hex 68656c6c6f
    python3 decoder.py --r13 uryyb
    python3 decoder.py --Binary "01101000 01100101 01101100 01101100 01101111"
"""

import base64
import codecs
import sys
import argparse

class CTF_Decoder:
    def __init__(self, encoded=None):
        self.encoded_str = encoded

    def set_encoded(self, encoded_str):
        #Set  encoded string to be decoded
        self.encoded_str = encoded_str

    def base64_decoder(self):
        #Decode a Base64 encoded string
        try:
            decoded = base64.b64decode(self.encoded_str).decode("utf-8")
            print("Base64 Decoded:", decoded)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)

    def base32_decoder(self):
        #Decode a Base32 encoded string
        try:
            decoded = base64.b32decode(self.encoded_str).decode("utf-8")
            print("Base32 Decoded:", decoded)
        except Exception as error:
            sys.stderr.write(f"Error: {error}\n")
            sys.exit(1)

    def hex_decoder(self):
        #Decode a hex string to ASCII
        try:
            decoded = bytes.fromhex(self.encoded_str).decode("utf-8")
            print("Hex Decoded:", decoded)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)

    def rot13_decoder(self):
        #Decode a ROT13 encoded string
        try:
            decoded = codecs.decode(self.encoded_str, "rot_13")
            print("ROT13 Decoded:", decoded)
        except Exception as e:
            sys.stderr.write(f"[ERROR] {e}\n")
            sys.exit(1)

    def binary_decoder(self):
        #Decode a binary string (8-bit per char) to ASCII
        try:
            clean_bin = self.encoded_str.replace(" ", "")
            if len(clean_bin) % 8 != 0:
                sys.stderr.write("ValueError: Binary string length must be a multiple of 8\n")
                sys.exit(1)
            decoded = ''.join([chr(int(clean_bin[i:i+8], 2)) for i in range(0, len(clean_bin), 8)])
            print("Binary Decoded:", decoded)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)

# --- CLI ---
parser = argparse.ArgumentParser(
    description='CTF Decoder',
    usage='%(prog)s --b64/--b32/--r13/--hex/--Binary value',
    epilog='Example: %(prog)s --b64 aGVsbG8='
)

# Define CLI arguments
parser.add_argument('--b64', help= '--b64 encoded input', dest='b64', metavar='base64', nargs='+')
parser.add_argument('--b32', help='--b32 encoded input', dest='b32', metavar='base32', nargs='+')
parser.add_argument('--hex', help='--hex "encoded input"', dest='hex_value', metavar='hex', nargs='+')
parser.add_argument('--r13', help='--r13 encoded input', dest='r13', metavar='rot13', nargs='+')
parser.add_argument('--Binary', help='--Binary "encoded input"', dest='Binary', metavar='binary', nargs='+')
parser.add_argument('-V', help="Print version", action="version", version="%(prog)s 1.0")

args = parser.parse_args()

# Show help if no  arguments are given
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)


decode = CTF_Decoder()

# Handle decoder type based on arguments
if args.b64:
    for value in args.b64:
        decode.set_encoded(value)
        decode.base64_decoder()

if args.b32:
    for value in args.b32:
        decode.set_encoded(value)
        decode.base32_decoder()

if args.hex_value:
    for value in args.hex_value:
        decode.set_encoded(value)
        decode.hex_decoder()

if args.r13:
    for value in args.r13:
        decode.set_encoded(value)
        decode.rot13_decoder()

if args.Binary:
    for value in args.Binary:
        decode.set_encoded(value)
        decode.binary_decoder()
