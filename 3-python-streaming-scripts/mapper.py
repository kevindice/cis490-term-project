#!/usr/bin/env python2.7

import sys
import json
import unicodedata
import re
import string

if(len(sys.argv) < 3):
    k = 3
elif(sys.argv[1] == '-k'):
    k = int(sys.argv[2])
else:
    k = 3


def clean(input):
    v1 = unicodedata.normalize('NFC', input)

    v2 = filter(lambda x: x in string.printable, v1)

    remap = {
        ord('\t') : u' ',
        ord('\f') : u' ',
        ord('\r') : None,
        ord('\n') : u' ',
        ord('!'): None,
        ord('!') : None,
        ord('"') : None,
        ord('#') : None,
        ord('$') : None,
        ord('%') : None,
        ord('&') : None,
        ord('\\') : None,
        ord('\'') : None,
        ord('(') : None,
        ord(')') : None,
        ord('*') : None,
        ord('+') : None,
        ord(',') : None,
        ord('-') : None,
        ord('.') : None,
        ord('/') : None,
        ord(':') : None,
        ord(';') : None,
        ord('<') : None,
        ord('=') : None,
        ord('>') : None,
        ord('?') : None,
        ord('@') : None,
        ord('[') : None,
        ord('\\') : None,
        ord('\\') : None,
        ord(']') : None,
        ord('^') : None,
        ord('_') : None,
        ord('`') : None,
        ord('{') : None,
        ord('|') : None,
        ord('}') : None,
        ord('~') : None
    }

    v3 = v2.translate(remap)

    v4 = re.sub("\s\s+", " ", v3)

    v5 = v4.upper().strip()

    return v5

def dateToWeekNumber(unixTime):
    return str(int(unixTime)/604800)


for line in sys.stdin:

    window = [None] * k
    index = 0

    post = json.loads(line)
    body = clean(post['body']).split()

    for word in body:
        window[index % k] = word
        if(index >= k - 1):
            ngram = ' '.join(window[(index + 1) % k:] + window[:(index + 1) % k])
            print(dateToWeekNumber(post['created_utc']) + '\t' + ngram)
        index += 1
