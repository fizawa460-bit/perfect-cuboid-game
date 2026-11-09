#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
setsid nohup bash run_sx.sh 2 > run_sx.log 2>&1 &
sleep 2; pgrep -fa 'sx_' | head -2
