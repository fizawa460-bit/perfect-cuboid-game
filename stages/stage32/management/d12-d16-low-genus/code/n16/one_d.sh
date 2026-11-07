#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
[ -s d_$1.out ] && exit 0
s=$(date +%s)
timeout 259200 stdbuf -oL -eL Singular -q d_$1.sing < /dev/null 2>&1 | grep --line-buffered -v redefining > d_$1.out
echo "time $(( $(date +%s) - s ))" >> d_$1.out
