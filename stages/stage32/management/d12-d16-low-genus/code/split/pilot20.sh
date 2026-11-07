cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/pilot20
for sh in 0 24 48 72 96 120 144 168 192 216; do
  ( s=$(date +%s); SPLIT_UB=1 /root/splitenum < r20_in_$sh.txt > /root/pilot20/out_$sh.txt 2> /root/pilot20/err_$sh.txt; echo "shard $sh time $(( $(date +%s) - s )) $(tail -1 /root/pilot20/err_$sh.txt)" >> pilot20.log ) &
done
wait; echo pilot-done >> pilot20.log
