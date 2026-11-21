#!/bin/bash
# like builder2.sh; when build5 finds covers without any refined cover in their symmetry orbit (exit 3),
# rebuild those at 80 digits with mono_dir REGEN and run build5 again (once).
B=/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/degree8-20261120
FM=/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fastmono-20261119
cd /home/user/deg8/gen
while true; do
  did=0
  for p in $(grep " exit 0 " done.txt | awk '{print $1}' | tr -d , | sort -u); do
    [ -f L5_8_$p.pkl ] && continue
    [ -f full_8_$p.pkl ] || continue
    grep "^done:" log_$p.txt | tail -1 | grep -oE "weighted [0-9.]+/[0-9.]+" | awk -F'[ /]' '{exit !($2 - $3 < 1e-6 && $3 - $2 < 1e-6)}' || continue
    pc=$(echo $p | sed 's/./&,/g; s/,$//')
    pgrep -f "mono_dir_nb.py 8 $pc " > /dev/null && continue
    mkdir lock_$p 2>/dev/null || continue
    echo "build $p $(date +%T)" >> builder.log
    DPS=60 python3 $B/build5.py 8 $p . 1 >> b5log_$p.txt 2>&1; ex=$?
    if [ $ex = 3 ]; then
      echo "build $p orphans $(cat orphans_8_$p.txt) -> 80-digit regen $(date +%T)" >> builder.log
      REGEN=$(cat orphans_8_$p.txt) REGEN_OUT=regen_8_$p.pkl python3 $B/mono_dir_nb.py 8 $pc --rules $FM/aut_rules_7_222222.pkl --ckpt ckpt_dir_8_$p.pkl >> b5log_$p.txt 2>&1
      DPS=60 python3 $B/build5.py 8 $p . 1 >> b5log_$p.txt 2>&1; ex=$?
    fi
    echo "build $p exit $ex $(date +%T)" >> builder.log
    python3 $B/distinct5.py L5_8_$p.pkl >> builder.log 2>&1
    did=1
  done
  n=$(ls L5_8_*.pkl 2>/dev/null | wc -l); [ $n -ge 75 ] && break
  [ $did = 0 ] && sleep 120
done
