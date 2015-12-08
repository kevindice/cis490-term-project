#!/usr/bin/env python2.7
import sys
import json
import unicodedata
from string import punctuation
from string import maketrans
import re

def clean(input):
    v1 = unicodedata.normalize('NFC', input)

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

    v2 = v1.translate(remap)

    v3 = re.sub("\s\s+", " ", v2)

    v4 = v3.upper().strip()

    return v4


for line in sys.stdin:
    post = json.loads(line)
    print clean(post['body'])

