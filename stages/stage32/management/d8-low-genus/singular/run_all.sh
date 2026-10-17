#!/bin/bash
# D8-LOW-GENUS: rerun every Singular computation (Singular 4.4.1). Run from this directory.
set -e
for n in swap id; do Singular -q primes_$n.sing 2>&1 | grep -v redefining > primes_$n.log; done
Singular -q fstar.sing 2>&1 | grep -v redefining | grep -v '^//' > fstar.log
