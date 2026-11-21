#!/bin/bash
# rerun profiles whose mono_dir run ended short of the Hurwitz number (LOOPS=0; seeds_8_<tag>.pkl used if present).
# at most 2 reruns per profile; at most 5 mono_dir processes at once.
cd /home/user/deg8/gen
while true; do
  for p in $(cat profiles.txt); do
    t=$(echo $p | tr -d ,); f=log_$t.txt; [ -f $f ] || continue
    line=$(grep "^done:" $f | tail -1); [ -z "$line" ] && continue
    echo "$line" | grep -oE "weighted [0-9.]+/[0-9.]+" | awk -F'[ /]' '{exit !($2 - $3 < 1e-6 && $3 - $2 < 1e-6)}' && continue
    pgrep -f "mono_dir_nb.py 8 $p " > /dev/null && continue
    # the last done line must be newer than the last requeue of this profile
    nd=$(grep -c "^done:" $f); last=$(grep -c "^requeue $p " requeue.log 2>/dev/null)
    [ $last -ge 2 ] && continue
    [ $(grep "^requeue $p " requeue.log 2>/dev/null | tail -1 | awk '{print $3}') = "$nd" ] 2>/dev/null && continue
    [ $(pgrep -f "mono_dir_nb.py 8" | wc -l) -ge 5 ] && continue
    echo "requeue $p $nd $(date +%T)" >> requeue.log
    LOOPS=0 nohup ./run1.sh $p > /dev/null 2>&1 &
  done
  sleep 300
done
