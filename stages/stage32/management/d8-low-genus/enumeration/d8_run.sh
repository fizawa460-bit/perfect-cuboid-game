#!/bin/bash
n1=$1; e=$2
cd /c/Users/fizaw/claudework/stage32_research/scripts
PYTHONUTF8=1 python 32R-21_classes_driver.py "/c/Users/fizaw/Documents/Codex/病棟物語/perfect-cuboid-game" 8 $n1 $e --enum "wsl.exe -d Ubuntu -u root -- /root/fp_enum" > d8/n${n1}_e${e}.json 2> d8/n${n1}_e${e}.err
echo "done $n1 $e"
