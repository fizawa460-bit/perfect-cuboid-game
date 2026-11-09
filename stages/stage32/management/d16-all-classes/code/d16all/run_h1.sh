#!/bin/bash
# d16 all reps, new classes, h0=1 fast genus (2 workers alongside the d18 nets), resumable
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
rm -f *.tmp
xargs -P 2 -I{} bash ../one_h1.sh {} < jobs.txt
echo DONE >> ../run_h1.log
