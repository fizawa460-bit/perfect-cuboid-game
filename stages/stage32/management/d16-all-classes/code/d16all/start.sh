#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all
setsid nohup bash run_h1.sh > /dev/null 2>&1 &
sleep 3; pgrep -fa one_h1 | head -3
