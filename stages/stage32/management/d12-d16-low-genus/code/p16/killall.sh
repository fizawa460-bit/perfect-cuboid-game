#!/bin/bash
for p in $(ps -eo pid,args | awk '/xargs/ && !/awk/ {print $1}'); do kill $p; done
sleep 1
for p in $(ps -eo pid,args | awk '/Singular -q/ && !/awk/ {print $1}'); do kill $p; done
sleep 2; ps -eo args | grep -c "[S]ingular -q"
