#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
setsid bash -c "xargs -P 7 -I{} bash ../one_h1.sh {} < rrjobs.txt; echo RR-DONE > rr.done" > /dev/null 2>&1 &
sleep 2; echo started
