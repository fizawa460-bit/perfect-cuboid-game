#!/bin/bash
for p in $(ls /proc | grep -E '^[0-9]+$'); do c=$(tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null); case "$c" in *xargs*one.sh*|*Singular*r_c1_*) [ "$p" != "$$" ] && kill $p;; esac; done
sleep 1; ps -eo args | grep -c '[S]ingular -q r_c1'
