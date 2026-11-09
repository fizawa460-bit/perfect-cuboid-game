#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all/fix0
setsid bash -c "xargs -P 9 -I{} bash one.sh {} < jobs.txt; echo FIX-DONE > fix.done" > /dev/null 2>&1 &
sleep 2; echo started
