sed -n '0~100p' $2 | python2 /homes/kmdice/cis490-term-project/3-python-streaming-scripts/mapper.py -k $1 | python2 \
/homes/kmdice/cis490-term-project/3-python-streaming-scripts/reducer.py > \
/homes/kmdice/reddit-weeks/$1-`basename $2`
