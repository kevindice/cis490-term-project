cat /homes/kmdice/extracted-reddit-posts/*.gz | gunzip \
| head -n 10000 | python /homes/kmdice/cis490-term-project/6-reduce/reduce.py
