#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
setsid nohup bash chain.sh > chain.log 2>&1 &
sleep 3; pgrep -fa p16all/chain
