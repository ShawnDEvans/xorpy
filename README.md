This utility takes input from a text file or standard input, and will XOR encrypt it using a user defined key. Due to the nature of bit flipping, the same function that encrypts will also decrypt, assuming you provide the correct key. Use this as a standalone app, or copy/paste it into your own project. It's simple, but works well enough.

****************************************
* Xorpy v1.1                           *
****************************************
* Coded by: Shawn Evans                *
* Email: ShawnDEvans@gmail.com  *
****************************************

Usage: python xorpy.py "key" encrypted.txt
$ cat decryptMe.txt | python xorpy.py "key"
$ cat encryptMe.txt | python xorpy.py "$eCreTkey"
