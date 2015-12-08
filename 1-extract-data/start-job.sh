./update-file-list.sh
qsub -l mem=512M,h_rt=1:00:00 -q killable.q,batch.q -t 1-`cat filelist.txt | wc -l`:1 job.sh
