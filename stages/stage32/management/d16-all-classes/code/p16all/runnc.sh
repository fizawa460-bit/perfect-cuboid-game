#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all/nc
setsid bash -c "xargs -P 3 -I{} bash one.sh {} < jobs.txt; echo NC-DONE > nc.done" > /dev/null 2>&1 &
sleep 2; echo started
