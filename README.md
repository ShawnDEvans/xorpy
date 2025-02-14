#Xorpy

This utility takes input from a text file or standard input, and will XOR encrypt it using a user defined key. Due to the nature of bit flipping, the same function that encrypts will also decrypt, assuming you provide the correct key. Use this as a standalone app, or copy/paste it into your own project. It's simple, but works well enough.

```
usage: Xorpy v1.2 [-h] [-o OUTPUT_FILE] -k KEY [input_file]

Stupid simple XOR encryption utility

positional arguments:
  input_file

options:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        Output file name, random otherwise.
  -k KEY, --key KEY     Secret key, ex "P@ssH0le"

Duct taped together by Shawn Evans - sevans@nopsec.com

```
