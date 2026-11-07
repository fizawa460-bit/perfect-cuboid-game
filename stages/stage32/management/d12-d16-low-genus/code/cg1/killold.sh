#!/bin/bash
ps -eo pid,etimes,args | awk '/Singular -q c1_/ && $2 > 600 && !/timeout/ && !/awk/ {print $1}' | xargs -r kill
ps -eo etimes,args | grep 'Singular -q c1_' | grep -v grep | grep -v timeout
