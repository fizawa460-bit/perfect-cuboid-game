#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all/t7
setsid bash -c "xargs -P 5 -I{} bash one.sh {} < jobs.txt; echo T7-DONE > t7.done" > /dev/null 2>&1 &
sleep 2; echo started
