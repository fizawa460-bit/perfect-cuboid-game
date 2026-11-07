cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/x14; rm -f /root/x14/*
s=$(date +%s)
seq 0 11 | xargs -P 8 -I{} bash -c 'SPLIT_EXACT=ex14.txt /root/splitenum9x < r14_in_{}.txt > /root/x14/out_{}.txt 2> /root/x14/err_{}.txt'
echo "time $(( $(date +%s) - s )) s"
cat /root/x14/out_*.txt | sort > /root/x14/all.sorted; cat r14_out_*.txt | sed 's/ *$//' | sort > /root/x14/old.sorted; sed -i 's/ *$//' /root/x14/all.sorted
wc -l /root/x14/all.sorted /root/x14/old.sorted; comm -3 /root/x14/all.sorted /root/x14/old.sorted | wc -l
grep -h EXACT /root/x14/err_*.txt | head -3; cat /root/x14/err_0.txt
