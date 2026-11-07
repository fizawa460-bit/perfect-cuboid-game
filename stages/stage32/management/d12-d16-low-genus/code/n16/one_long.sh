#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
[ -e $1.out ] || { s=$(date +%s); timeout 259200 stdbuf -oL -eL Singular -q $1.sing < /dev/null 2>&1 | grep --line-buffered -v redefining > $1.out; echo "time $(( $(date +%s) - s ))" >> $1.out; }
