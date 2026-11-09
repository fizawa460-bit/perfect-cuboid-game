#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
rm -f *.tmp
xargs -P 2 -I{} bash one.sh {} < jobs.txt
echo DONE
