#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
setsid bash -c "xargs -P 3 -I{} bash one.sh {} < cgjobs.txt; echo CG-DONE > cg.done" > /dev/null 2>&1 &
sleep 2; pgrep -fa 'cg_sx' | grep -c Singular
