#!/bin/bash
# 32R-91: d = 16 enumeration WITHOUT the unibranch prune (all reps, symmetry-reduced as full16sym.sh)
cd /mnt/c/Users/fizaw/claudework/stage32_research/split
mkdir -p /root/s16all; rm -f /root/s16all/*
s=$(date +%s)
seq 0 479 | xargs -P ${1:-2} -I{} bash -c 'SPLIT_SYMFILE=symz.txt nice -n 5 /root/splitenum9 < r16_in_{}.txt > /root/s16all/out_{}.txt 2> /root/s16all/err_{}.txt'
echo "total $(( $(date +%s) - s )) s"
cat /root/s16all/out_*.txt | wc -l
echo ENUM-DONE
