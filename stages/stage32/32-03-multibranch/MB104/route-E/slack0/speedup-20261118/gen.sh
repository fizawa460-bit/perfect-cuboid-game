# usage: sh gen.sh n  -> runs mono.py for every profile representative into data<n>/
n=$1; cd data$n
python3 ../../numeric-upto5-20261118/reps.py $n 2>/dev/null | while read a b c d e f w o; do
  prof=$(echo "$a$b$c$d$e$f" | tr -d '() ')
  python3 ../mono.py $n $prof 100 1 > log_mono_${n}_$(echo $prof|tr -d ,).txt 2>&1
  tail -1 log_mono_${n}_$(echo $prof|tr -d ,).txt
done
