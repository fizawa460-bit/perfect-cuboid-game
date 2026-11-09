#!/bin/bash
# after the d16all h0=1 run: redo its missing jobs once, then the d16all pencil critical and Moebius jobs (2 workers)
B=/mnt/c/Users/fizaw/claudework/stage32_research/stoll
while ! grep -q DONE $B/d16all/run_h1.log 2>/dev/null; do sleep 60; done
bash $B/d16all/run_h1.sh > /dev/null 2>&1
bash $B/p16all/run_c.sh > $B/p16all/run_c.log 2>&1
bash $B/p16all/run_m.sh > $B/p16all/run_m.log 2>&1
echo CHAIN-DONE >> $B/p16all/run_m.log
