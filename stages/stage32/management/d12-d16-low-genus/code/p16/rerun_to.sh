#!/bin/bash
# wait for the main sx run, then rerun 7200 s timeouts with the 36000 s limit
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16
while pgrep -f "xargs -P 10 -n 1 ./one.sh" > /dev/null; do sleep 120; done
L=$(grep -l "^time 7[12][0-9][0-9]$" sx_*.out | sed 's/\.out$//')
echo "rerun: $L"
for j in $L; do mkdir -p old_timeout; mv $j.out old_timeout/; done
printf "%s\n" $L | xargs -P 10 -n 1 ./one_long.sh
echo rerun-done
