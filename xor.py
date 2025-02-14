#!/usr/bin/env python3
import sys
import argparse
import string
import random

def xorcrypt(data, key):
    try:
        result = bytearray()
        pad = key*round(len(data)/len(key)) + key[:round(len(data)%len(key))]
        pad.encode('ascii')
        for i in range(len(data)-1):
            result.append(data[i] ^ ord(pad[i]))
        return bytes(result)
    except Exception as e:
        print(e)

title = 'Xorpy v1.1'
author = 'Coded by: Shawn Evans'
email = 'Email: ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Xorpy v1.2', description='Stupid simple XOR encryption utility', epilog='Duct taped together by Shawn Evans - sevans@nopsec.com')
    parser.add_argument('-o', '--output', help='Output file name, random otherwise.', dest='output_file')
    parser.add_argument('-k', '--key', help='Secret key, ex "P@ssH0le"', required=True)
    parser.add_argument('input_file', nargs='?')

    args = parser.parse_args()

    try:
        if not sys.stdin.isatty():
            inFile = sys.stdin.buffer
        else:
            inFile = open(args.input_file)
        key = sys.argv[1]
    except Exception as e:
        print(e)
        parser.print_help()
        sys.exit()

    data = inFile.read()
    enc_data = xorcrypt(data, key)
    output_file = ''
    if not args.output_file:
        rando = ''.join(random.choice(string.ascii_letters) for i in range(10))
        output_file = f'{rando}.txt'
    else:
        output_file = args.output_file
    output = open(f'{output_file}', 'wb')
    output.write(enc_data)
    output.close()

