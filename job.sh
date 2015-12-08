#!/bin/bash
#$ -t 1:15
sh /homes/kmdice/cis490-term-project/ping.sh `sed -n "${SGE_TASK_ID}p" /homes/kmdice/cis490-term-project/filelist.txt`
