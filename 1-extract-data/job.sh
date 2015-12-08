#!/bin/bash
/homes/kmdice/cis490-term-project/1-extract-data/extract.sh `sed -n "${SGE_TASK_ID}p" 
/homes/kmdice/cis490-term-project/1-extract-data/filelist.txt`
