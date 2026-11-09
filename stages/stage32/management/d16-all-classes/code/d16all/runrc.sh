#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
setsid bash -c "xargs -P 2 -I{} bash ../one_h1.sh {} < rcjobs.txt; echo RC-DONE > rc.done" > /dev/null 2>&1 &
sleep 2; pgrep -fa 'rc_t' | head -2
