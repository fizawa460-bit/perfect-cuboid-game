cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/s20sym; rm -f /root/s20sym/*
s=$(date +%s)
seq 0 239 | xargs -P 9 -I{} bash -c 'SPLIT_UB=1 SPLIT_SYMFILE=symz.txt /root/splitenum9 < r20_in_{}.txt > /root/s20sym/out_{}.txt 2> /root/s20sym/err_{}.txt'
echo "total $(( $(date +%s) - s )) s"
cat /root/s20sym/out_*.txt > /root/s20sym/all.txt; wc -l < /root/s20sym/all.txt
grep -L "reps" /root/s20sym/err_*.txt | head
