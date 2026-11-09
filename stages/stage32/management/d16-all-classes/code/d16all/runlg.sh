#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
setsid bash -c "xargs -P 9 -I{} bash ../one_h1.sh {} < lgjobs.txt; echo LG-DONE > lg.done" > /dev/null 2>&1 &
sleep 2; echo started
