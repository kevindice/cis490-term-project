# For this script, send as an argument the size n of the n-grams desired

echo $#

if [ "$#" -ne 1 ]; then
  echo "USAGE: Specify exactly one argument for the n in n-gram." >&2
  exit 1
fi

./update-file-list.sh
qsub -l mem=1G,h_rt=1:00:00 -q killable.q,batch.q -t 1-`cat filelist.txt | wc -l`:1 job.sh $1
