cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/s16sym; rm -f /root/s16sym/*
s=$(date +%s)
seq 0 479 | xargs -P 6 -I{} bash -c 'SPLIT_UB=1 SPLIT_SYMFILE=symz.txt /root/splitenum9 < r16_in_{}.txt > /root/s16sym/out_{}.txt 2> /root/s16sym/err_{}.txt'
echo "total $(( $(date +%s) - s )) s"
cat /root/s16sym/out_*.txt > /root/s16sym/all.txt; wc -l < /root/s16sym/all.txt
grep -L "reps" /root/s16sym/err_*.txt | head
cp /root/s16sym/all.txt s16sym_all.txt
