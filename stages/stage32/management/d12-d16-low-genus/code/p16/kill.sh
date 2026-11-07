#!/bin/bash
for p in $(ps -eo pid,args | awk '/xargs -P 11/ && !/awk/ {print $1}'); do kill $p; done
sleep 1
for p in $(ps -eo pid,args | awk '/Singular -q c_/ && !/awk/ {print $1}'); do kill $p; done
sleep 2; ps -eo args | grep -c "[S]ingular -q c_"
