#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
setsid bash -c "xargs -P 9 -I{} bash ../one_h1.sh {} < runq.txt; echo Q-DONE > q.done" > /dev/null 2>&1 &
sleep 3; echo "running: $(ps -C Singular -o stat= | grep -vc '^T')"
