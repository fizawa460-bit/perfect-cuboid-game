#!/bin/bash
p=$1; F=/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fastmono-20261119
cd /home/user/deg8/gen
t=$(echo $p|tr -d ,); [ -z "$SEEDFILE" ] && [ -f seeds_8_$t.pkl ] && SEEDFILE=seeds_8_$t.pkl
python3 /home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/degree8-20261120/mono_dir_nb.py 8 $p --rules $F/aut_rules_7_222222.pkl --loops ${LOOPS:-1} ${SEEDFILE:+--seedfile $SEEDFILE} >> log_$(echo $p|tr -d ,).txt 2>&1
echo "$p exit $? $(date +%T)" >> done.txt
