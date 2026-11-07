cd /mnt/c/Users/fizaw/claudework/stage32_research/split
for sh in 100 250 401; do
 for b in splitenum7 splitenum8; do
  s=$(date +%s%N); SPLIT_UB=1 /root/$b < r16_in_$sh.txt > /root/c_$b.txt 2> /root/c_$b.err; e=$(date +%s%N)
  echo "shard $sh $b $(( (e-s)/1000000 )) ms $(tail -1 /root/c_$b.err | cut -d' ' -f8-) md5 $(sort /root/c_$b.txt | md5sum | cut -c1-12)"
 done
done
