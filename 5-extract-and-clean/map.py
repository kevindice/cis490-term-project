#!/usr/bin/env python2.7

import sys
import json
import unicodedata
import re
import string

if(len(sys.argv) != 2):
    print "You must specify the filename."
    print "Number of arguments specified:  " + str(len(sys.argv))
    print sys.argv
    sys.exit(1)

input = sys.argv[1]

def clean(input):
    v1 = unicodedata.normalize('NFC', input)

    v2 = filter(lambda x: x in string.printable, v1)

    remap = {
        ord('\t'): u' ',
        ord('\f'): u' ',
        ord('\r'): None,
        ord('\n'): u' ',
        ord('!'): None,
        ord('!'): None,
        ord('"'): None,
        ord('#'): None,
        ord('$'): None,
        ord('%'): None,
        ord('&'): None,
        ord('\\'): None,
        ord('\''): None,
        ord('('): None,
        ord(')'): None,
        ord('*'): None,
        ord('+'): None,
        ord(','): None,
        ord('-'): None,
        ord('.'): None,
        ord('/'): None,
        ord(':'): None,
        ord(';'): None,
        ord('<'): None,
        ord('='): None,
        ord('>'): None,
        ord('?'): None,
        ord('@'): None,
        ord('['): None,
        ord('\\'): None,
        ord('\\'): None,
        ord(']'): None,
        ord('^'): None,
        ord('_'): None,
        ord('`'): None,
        ord('{'): None,
        ord('|'): None,
        ord('}'): None,
        ord('~'): None
    }

    v3 = v2.translate(remap)

    v4 = re.sub("\s\s+", " ", v3)

    v5 = v4.upper().strip()

    return v5


def dateToWeekNumber(unixTime):
    return str(int(unixTime)/604800)



all = dict()
buffersize = 2 ** 22
with open(input, 'r', buffersize) as fin:
    for line in fin:
        index = 0
        post = json.loads(line)
        body = clean(post['body'])
        weeknum = dateToWeekNumber(post['created_utc'])
        print(weeknum + '\t' + body)
