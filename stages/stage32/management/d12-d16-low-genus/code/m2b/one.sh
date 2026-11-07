#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/m2b
[ -e $1.out ] || { s=$(date +%s); timeout 1800 Singular -q $1.sing < /dev/null 2>&1 | grep -v redefining > $1.out; echo "time $(( $(date +%s) - s ))" >> $1.out; }
