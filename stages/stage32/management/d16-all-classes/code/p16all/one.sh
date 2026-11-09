#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/p16all
[ -e $1.out ] || [ -e $1.tmp ] || { s=$(date +%s); timeout 14400 Singular -q $1.sing < /dev/null 2>&1 | grep -v redefining > $1.tmp; echo "time $(( $(date +%s) - s ))" >> $1.tmp; mv $1.tmp $1.out; }
