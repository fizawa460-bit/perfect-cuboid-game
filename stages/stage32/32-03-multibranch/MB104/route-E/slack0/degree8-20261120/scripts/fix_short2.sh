#!/bin/bash
cd /home/user/deg8/gen
for p in 1,2,2,3,2,4 1,2,2,3,4,2 1,2,1,3,3,4 1,3,1,4,3,2 1,2,1,4,4,2; do
  while pgrep -f "mono_dir_nb.py 8 $p " > /dev/null; do sleep 30; done
  t=$(echo $p | tr -d ,)
  grep "^done:" log_$t.txt | tail -1 | grep -oE "weighted [0-9.]+/[0-9.]+" | awk -F'[ /]' '{exit !($2 - $3 < 1e-6 && $3 - $2 < 1e-6)}' && continue
  echo "fix $p $(date +%T)" >> requeue.log; LOOPS=0 ./run1.sh $p
done
