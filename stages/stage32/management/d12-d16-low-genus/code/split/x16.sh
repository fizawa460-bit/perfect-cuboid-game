cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/x12; rm -f /root/x12/*
seq 0 11 | xargs -P 8 -I{} bash -c 'SPLIT_EXACT=ex12.txt /root/splitenum9x < r12_in_{}.txt > /root/x12/out_{}.txt 2> /root/x12/err_{}.txt'
cat /root/x12/out_*.txt | sed 's/ *$//' | sort > /root/x12/all.sorted; cat r12_out_*.txt | sed 's/ *$//' | sort > /root/x12/old.sorted
echo "d12 exact $(wc -l < /root/x12/all.sorted) old $(wc -l < /root/x12/old.sorted) diff $(comm -3 /root/x12/all.sorted /root/x12/old.sorted | wc -l)"
mkdir -p /root/x16; rm -f /root/x16/*
s=$(date +%s)
seq 0 479 | xargs -P 8 -I{} bash -c 'SPLIT_UB=1 SPLIT_SYMFILE=symz.txt SPLIT_EXACT=ex16.txt /root/splitenum9x < r16_in_{}.txt > /root/x16/out_{}.txt 2> /root/x16/err_{}.txt'
echo "d16 time $(( $(date +%s) - s )) s"
cat /root/x16/out_*.txt | sed 's/ *$//' | sort > /root/x16/all.sorted; sed 's/ *$//' /root/s16sym/all.txt | sort > /root/x16/old.sorted
echo "d16 exact $(wc -l < /root/x16/all.sorted) old $(wc -l < /root/x16/old.sorted) diff $(comm -3 /root/x16/all.sorted /root/x16/old.sorted | wc -l)"
echo "errors: $(grep -L 'reps' /root/x16/err_*.txt | wc -l) shards without final line"
