#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
setsid bash -c "xargs -P 4 -I{} bash one.sh {} < lgjobs.txt; echo LG-DONE > lg.done" > /dev/null 2>&1 &
sleep 2; echo started
