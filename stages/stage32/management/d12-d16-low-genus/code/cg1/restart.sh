#!/bin/bash
for p in $(pgrep -x Singular); do
  a=$(tr '\0' ' ' < /proc/$p/cmdline)
  case "$a" in *" c1_"*|*" c14"*) kill $p;; esac
done
sleep 2
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/cg1
nohup xargs -P 4 -n 1 ./one.sh < jobs.txt > /dev/null 2>&1 &
echo started
