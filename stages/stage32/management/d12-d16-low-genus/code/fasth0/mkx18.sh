#!/bin/bash
# 32R-71: d18 x lines in the same order as j18_glpk.txt (cat18.sh order)
cd /root/s18sym
for f in $(ls out_*.txt); do cat $f; done > /root/x18_ord.txt
wc -l < /root/x18_ord.txt
