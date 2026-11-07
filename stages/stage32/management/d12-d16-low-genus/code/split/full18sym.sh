cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/s18sym; rm -f /root/s18sym/*
s=$(date +%s)
seq 0 479 | xargs -P 10 -I{} bash -c 'SPLIT_UB=1 SPLIT_SYMFILE=symz.txt /root/splitenum9 < r18_in_{}.txt > /root/s18sym/out_{}.txt 2> /root/s18sym/err_{}.txt'
echo "total $(( $(date +%s) - s )) s"
cat /root/s18sym/out_*.txt > /root/s18sym/all.txt; wc -l < /root/s18sym/all.txt
grep -L "reps" /root/s18sym/err_*.txt | head
cp /root/s18sym/all.txt s18sym_all.txt
