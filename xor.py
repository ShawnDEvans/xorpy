#!/usr/bin/python
import sys 

def xorcrypt(data, key):
    result = ''
    pad = key*(len(data)/len(key)) + key[:(len(data)%len(key))]
    for i in range(len(data)):
        result += chr (ord(data[i]) ^ ord(pad[i]))        
    return result

title = 'Xorpy v1.0'
author = 'Coded by: Shawn Evans'
email = 'Email: Shawn.Evans@knowledgeCG.com'
   
def usage():
    print '*'*40
    print '* %s%s*' % (title, ' '*int(37-len(title)))
    print '*'*40
    print '* %s%s*' % (author, ' '*int(37-len(author)))
    print '* %s%s*' % (email, ' '*int(37-len(email)))
    print '*'*40
    print ''
    print 'Usage: python %s %s %s' % (sys.argv[0], '"key"', 'encrypted.txt')
    print '$ cat decryptMe.txt | python %s %s' % (sys.argv[0], '"key"')
    print '$ cat encryptMe.txt | python %s %s' % (sys.argv[0], '"$eCreTkey"')

if __name__ == '__main__':

    try:
        if not sys.stdin.isatty():
            inFile = sys.stdin
        else:
            inFile = sys.argv[2]
    except:
        usage()
        sys.exit()
   
    key = sys.argv[1]

    data = inFile.read()
    print xorcrypt(data, key)

