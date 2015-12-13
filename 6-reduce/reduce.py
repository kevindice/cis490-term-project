#!/usr/bin/env python2.7

import sys
import string
import operator
from blist import sorteddict
import json

all = sorteddict()
buffersize = 2 ** 22
window2 = [None] * 2
window3 = [None] * 3


def addToDict(weeknumber, ngram):
    if(ngram not in all):
        all[ngram] = sorteddict()
    if(weeknumber not in all[ngram]):
        all[ngram][weeknumber] = 1
    else:
        all[ngram][weeknumber] = 1 + all[ngram][weeknumber]


for line in sys.stdin:
    index = 0
    weeknumber, body = line.split('\t')
    wn = int(weeknumber)
    msg = body.strip().split(' ')

    print("Line:  " + line)

    for word in msg:
        window2[index % 2] = word
        window3[index % 3] = word
        if(index >= 1):
            ngram = ' '.join(window2[(index + 1) % 2:] + window2[:(index + 1) % 2])
            addToDict(wn, ngram)
        if(index >= 2):
            ngram = ''.join(window3[(index + 1) % 3] + window3[(index + 1) % 3])
            addToDict(wn, ngram)
        addToDict(wn, word)



with open('/homes/kmdice/tempDeleteThis.json', 'w', buffersize) as fout:
    json.dump(all, fout)

#with open(output, 'w', buffersize) as fout:
#    for line in fin:
#        index = 0
#        post = json.loads(line)
#        body = clean(post['body']).split()
#        weeknumber = dateToWeekNumber(post['created_utc'])
#
#        for word in body:
#            window[index % k] = word
#            if(index >= k - 1):
#                ngram = ' '.join(window[(index + 1) % k:] + window[:(index + 1) % k])
#
#                if(weeknumber not in all):
#                    all[weeknumber] = dict()
#                if(ngram not in all[weeknumber]):
#                    all[weeknumber][ngram] = 0
#
#                all[weeknumber][ngram] = all[weeknumber][ngram] + 1
#
#            index = index + 1
#
#    for weeknum, weekdict in all.iteritems():
#        for ngram, count in sorted(weekdict.iteritems(), key=operator.itemgetter(1), reverse=True):
#            fout.write(weeknum + '\t' + ngram + '\t' + str(count) + '\n')
