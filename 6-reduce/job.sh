#!/bin/bash
cat /homes/kmdice/extracted-reddit-posts/*.gz | gunzip \
| python \
/homes/kmdice/cis490-term-project/6-reduce/reduce.py \
| /homes/kmdice/usr/local/bin/lz4 -9 > /homes/kmdice/testLZ4.lz4
