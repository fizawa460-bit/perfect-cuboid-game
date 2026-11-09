#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
xargs -P ${1:-2} -I{} bash one.sh {} < sxjobs.txt
echo SX-DONE
