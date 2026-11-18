n=$1
python3 reps.py $n | while read a b c d e f w o; do
  prof=$(echo "$a$b$c$d$e$f" | tr -d '() ' ); 
  echo "python3 run_covers.py $n $prof 7 $w 2000 2000000 > log_${n}_$(echo $prof|tr -d ,).txt 2>&1"
done
