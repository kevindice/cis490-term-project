#!/bin/bash
echo "started"
/homes/kmdice/cis490-term-project/3-python-streaming-scripts/ngram-count.sh $1 \
`sed -n "${SGE_TASK_ID}p" /homes/kmdice/cis490-term-project/3-python-streaming-scripts/filelist.txt`

echo "finished"
