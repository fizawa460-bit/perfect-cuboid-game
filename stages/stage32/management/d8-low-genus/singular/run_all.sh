#!/bin/bash
# D8-LOW-GENUS: rerun every Singular computation (Singular 4.x). Run from this directory: bash run_all.sh
# Fails (non-zero exit) if Singular is missing, exits non-zero, prints any error/warning marker, or if an expected
# output line is absent. Error detection: Singular prefixes every interpreter error line with "?" (e.g. "   ? ...",
# "? error occurred in ..."), and warnings with "// **". Every line starting (after blanks) with "?" is an error;
# every "// **" line other than the library "redefining" notices is treated as an error too. Beyond these markers,
# correctness rests on the explicit content checks below (counts of primes, absolute factors, genus).
set -euo pipefail
command -v Singular >/dev/null || { echo "Singular not found" >&2; exit 1; }
run() {  # run <script> <log> ; keep stderr, drop only library-redefinition notices
  local out
  out=$(Singular -q "$1" 2>&1) || { echo "$out" >&2; echo "Singular failed on $1" >&2; exit 1; }
  if printf '%s\n' "$out" | grep -Eq '^[[:space:]]*\?|error occurred|halt'; then
    echo "$out" >&2; echo "Singular reported an error in $1" >&2; exit 1
  fi
  if printf '%s\n' "$out" | grep '^// \*\*' | grep -vq 'redefining'; then
    echo "$out" >&2; echo "Singular reported a warning in $1" >&2; exit 1
  fi
  printf '%s\n' "$out" | grep -v 'redefining' | grep -v '^//' | sed 's/[[:space:]]*$//' > "$2"
}
run primes_swap.sing primes_swap.log
run primes_id.sing primes_id.log
run fstar.sing fstar.log
grep -q '^== swap: .*minimal primes: 3$' primes_swap.log
grep -q '^== id: .*minimal primes: 17$' primes_id.log
grep -q 'number of absolute factors: 1' fstar.log
grep -q 'geometric genus (normal.lib): 3' fstar.log
for n in swap id; do test -s primes_$n.txt; done
echo "run_all.sh: OK"
