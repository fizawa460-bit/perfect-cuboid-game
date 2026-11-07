cd /mnt/c/Users/fizaw/claudework/stage32_research/split
for b in splitenum3 splitenum4; do
 s=$(date +%s%N); SPLIT_UB=1 /root/$b < r16_in_7.txt > /root/cmp_$b.txt 2> /root/cmp_$b.err; e=$(date +%s%N)
 echo "$b $(( (e-s)/1000000 )) ms $(tail -1 /root/cmp_$b.err) md5 $(sort /root/cmp_$b.txt | md5sum | cut -c1-12)"
done
