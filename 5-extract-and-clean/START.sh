#!/bin/bash

./update-file-list.sh
qsub \
   -l mem=2G,h_rt=12:00:00 \
   -q killable.q,batch.q \
   -t 1:`cat filelist.txt | wc -l` \
   -pe single 2 \
   job.sh
