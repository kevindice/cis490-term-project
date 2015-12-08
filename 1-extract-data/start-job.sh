./update-file-list.sh
qsub -l mem=3G,h_rt=4:00:00 -q killable.q,batch.q -t 1-`cat filelist.txt | wc -l`:1 job.sh
