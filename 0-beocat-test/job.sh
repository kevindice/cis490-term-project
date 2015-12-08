#!/bin/bash
/homes/kmdice/cis490-term-project/0-beocat-test/ping.sh `sed -n "${SGE_TASK_ID}p" /homes/kmdice/cis490-term-project/0-beocat-test/filelist.txt`
