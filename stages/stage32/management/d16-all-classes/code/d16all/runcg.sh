#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
setsid bash -c "xargs -P 3 -I{} bash ../one_h1.sh {} < cgjobs.txt; echo CG-DONE > cg.done" > /dev/null 2>&1 &
sleep 2; pgrep -fa 'cg_' | grep -c Singular
