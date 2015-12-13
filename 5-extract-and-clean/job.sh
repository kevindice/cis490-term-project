#!/bin/bash
echo "started"

SRC=`sed -n "${SGE_TASK_ID}p" \
/homes/kmdice/cis490-term-project/5-extract-and-clean/filelist.txt`

DEST=`printf "%02d" ${SGE_TASK_ID}`

/homes/kmdice/cis490-term-project/5-extract-and-clean/map.py \
$SRC | gzip > "/homes/kmdice/extracted-reddit-posts/posts-$DEST.gz"

echo "finished"
