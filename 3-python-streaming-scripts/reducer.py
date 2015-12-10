#!/usr/bin/env python

from operator import itemgetter
import sys

all = dict()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if line in all:
        all[line] = all[line] + 1
    else:
        all[line] = 1

for kmer in sorted(all, key=all.get, reverse=True):
    print kmer + "\t" + str(all[kmer])

