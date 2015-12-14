#!/usr/bin/env python2.7

import sys
import string
import operator
import json

all = dict()
buffersize = 2 ** 22
lineNumber = 0
totalNgrams = 0
totalCulled = 0

def addToDict(weeknumber, ngram):
    global totalNgrams
    totalNgrams += 1
    if(ngram not in all):
        all[ngram] = dict()
    if(weeknumber not in all[ngram]):
        all[ngram][weeknumber] = 1
    else:
        all[ngram][weeknumber] = 1 + all[ngram][weeknumber]


def cull(limit):
    global totalCulled
    for key in list(all.keys()):
        total = 0
        for week, n in all[key].items():
            total += n
        if(total < limit):
            del all[key]
            totalCulled += total


for line in sys.stdin:
    if(lineNumber % 1000000 == 0):
        cull(2)
    if(lineNumber % 5000000 == 0):
        cull(5)
    window2 = [None] * 2
    window3 = [None] * 3
    index = 0
    weeknumber, body = line.split('\t')
    wn = int(weeknumber)
    msg = body.strip().split(' ')

    for word in msg:
        window2[index % 2] = word
        window3[index % 3] = word
        if(index >= 1):
            ngram = ' '.join(window2[(index + 1) % 2:] + window2[:(index + 1) % 2])
            addToDict(wn, ngram)
        if(index >= 2):
            ngram = ' '.join(window3[(index + 1) % 3:] + window3[:(index + 1) % 3])
            addToDict(wn, ngram)
        addToDict(wn, word)
        index += 1
    lineNumber += 1
cull(int(totalNgrams * 0.000001))


# Take a histogram of the data
freqHistogram = dict()
for key, counts in all.items():
    total = 0
    for week, n in counts.items():
        total += int(n)
    if total in freqHistogram:
        freqHistogram[total] += 1
    else:
        freqHistogram[total] = 1


with open('/homes/kmdice/histogram', 'w') as f:
    remaining = len(all)
    total = len(all)
    f.write("Total n-grams:\t" + str(totalNgrams) + '\n')
    f.write("Total culled:\t" + str(totalCulled) + '\n')
    f.write("\n\nFrequency\tNum @ freq\tReverse Percentile\n" + '-' * 80 + '\n')
    i = 1
    membersLeft = len(freqHistogram)

    while membersLeft != 0:
        if(i in freqHistogram):
            membersLeft -= 1
            f.write(str(i) + '\t\t' + str(freqHistogram[i]) + '\t\t' + str(100 * remaining / total) + '\n')
            remaining -= int(freqHistogram[i])
        i += 1

print(json.dumps(all, sort_keys=True, indent=4))
