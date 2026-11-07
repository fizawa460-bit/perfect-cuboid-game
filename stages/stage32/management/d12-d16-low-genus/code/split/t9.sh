cd /mnt/c/Users/fizaw/claudework/stage32_research/split
gcc -O3 -march=native -o /root/splitenum9 splitenum9.c -lm 2>&1 | grep -i error
for sh in 7 250 401; do
  s=$(date +%s%N); SPLIT_UB=1 SPLIT_SYMFILE=symz.txt /root/splitenum9 < r16_in_$sh.txt > /root/s9_$sh.txt 2> /root/s9_$sh.err; e=$(date +%s%N)
  echo "shard $sh $(( (e-s)/1000000 )) ms $(tail -1 /root/s9_$sh.err)"
done
