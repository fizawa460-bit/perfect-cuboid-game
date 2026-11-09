#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
xargs -P 2 -I{} bash one.sh m_{} < ${1:-mobjobs.txt}
echo DONE
