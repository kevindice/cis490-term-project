#!/usr/bin/env python2.7

import sys
import json
import unicodedata
import re
import string
import operator

if(len(sys.argv) != 4):
    print "You must specify two arguments: The filename and the n-gram size."
    print "Number of arguments specified:  " + str(len(sys.argv))
    print sys.argv
    sys.exit(1)

k = int(sys.argv[1])
input = sys.argv[2]
output = sys.argv[3]


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
window = [None] * k
with open(input, 'r', buffersize) as fin, open(output, 'w', buffersize) as fout:
    for line in fin:
        index = 0
        post = json.loads(line)
        body = clean(post['body']).split()
        weeknumber = dateToWeekNumber(post['created_utc'])

        for word in body:
            window[index % k] = word
            if(index >= k - 1):
                ngram = ' '.join(window[(index + 1) % k:] + window[:(index + 1) % k])

                if(weeknumber not in all):
                    all[weeknumber] = dict()
                if(ngram not in all[weeknumber]):
                    all[weeknumber][ngram] = 0

                all[weeknumber][ngram] = all[weeknumber][ngram] + 1

            index = index + 1

    for weeknum, weekdict in all.iteritems():
        for ngram, count in sorted(weekdict.iteritems(), key=operator.itemgetter(1), reverse=True):
            fout.write(weeknum + '\t' + ngram + '\t' + str(count) + '\n')
