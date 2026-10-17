#!/bin/bash
n1=$1; e=$2; v=$3
cd /c/Users/fizaw/claudework/stage32_research/scripts
PYTHONUTF8=1 python 32R-21_classes_driver.py "/c/Users/fizaw/Documents/Codex/病棟物語/perfect-cuboid-game" 8 $n1 $e -8 --fix 49=$v --limit 30000000000 --enum "wsl.exe -d Ubuntu -u root -- /root/fp_enum" > d8s/g1_n${n1}_e${e}_x${v}.json 2> d8s/g1_n${n1}_e${e}_x${v}.err
echo "done $n1 $e $v"
