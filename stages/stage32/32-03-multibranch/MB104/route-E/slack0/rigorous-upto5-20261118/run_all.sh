#!/bin/sh
# Full rigorous run for the open slack-(0,0) bidegrees with max(a,b) <= 5 (about 7 minutes on one core).
# Needs python-flint 0.9 (arb), numpy. Run from this folder.
set -e
mkdir -p logs
for n in 3 4 5; do python3 certify.py $n inputs/data$n | tee logs/certify_$n.log; done
for ab in "3 4" "4 4" "4 5" "5 5"; do set -- $ab; python3 search_rig.py $1 $2 | tee logs/search_$1_$2.log; done
for ab in "4 4" "5 5"; do set -- $ab; python3 prove.py $1 $2 | tee logs/prove_$1_$2.log; python3 selftest.py $1 $2 | tee logs/selftest_$1_$2.log; done
