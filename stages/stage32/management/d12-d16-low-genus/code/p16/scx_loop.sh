#!/bin/bash
cd /c/Users/fizaw/claudework/stage32_research/stoll/p16
while true; do
  python tally_sx.py > /dev/null; python mk_scx.py > /dev/null
  MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -u root -- bash -c "cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16 && xargs -P 1 -n 1 ./one.sh < scxjobs.txt"
  p=$(python -c "import json,os; print(sum(1 for n in open('sxjobs_new.txt').read().split() if not os.path.exists(n+'.out') or 'time' not in open(n+'.out',errors='replace').read()))")
  [ -z "$p" ] && p=0
  if [ "$p" -eq 0 ]; then python tally_sx.py > /dev/null; python mk_scx.py > /dev/null; MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -u root -- bash -c "cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16 && xargs -P 4 -n 1 ./one.sh < scxjobs.txt"; echo finished; break; fi
  sleep 300
done
