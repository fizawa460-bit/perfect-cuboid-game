#!/bin/bash
for j in $(cat /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16/rt2jobs.txt); do pkill -f "Singular -q $j.sing"; done
sleep 2; ps -eo args | grep -c "[S]ingular -q"
