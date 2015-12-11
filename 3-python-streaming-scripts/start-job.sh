# For this script, send as an argument the size n of the n-grams desired

./update-file-list.sh
qsub -l mem=32G,h_rt=10:00:00 -q killable.q,batch.q -t 1-`cat filelist.txt | wc -l`:1 job.sh $1
