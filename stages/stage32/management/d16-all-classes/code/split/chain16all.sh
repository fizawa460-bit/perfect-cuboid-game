#!/bin/bash
# 32R-91 chain: wait for the d16 all-rep enumeration, mu prefilter, then GLPK h0 judge on the survivors
B=/mnt/c/Users/fizaw/claudework/stage32_research
while ! grep -q ENUM-DONE $B/split/full16all.log 2>/dev/null; do sleep 30; done
python3 $B/stoll/mu1820/mupre.py 16 /root/s16all /root/s16allmu > $B/split/mupre16all.log 2>&1
bash $B/stoll/fasth0/judge_glpk.sh /root/s16allmu /root/j16all 2 > $B/split/judge16all.log 2>&1
echo CHAIN16-DONE >> $B/split/judge16all.log
