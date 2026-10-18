#!/bin/bash
# D8-LOW-GENUS: rerun every Singular computation (Singular 4.x). Run from this directory: bash run_all.sh
# Fails (non-zero exit) if Singular is missing, exits non-zero, prints any error/warning marker, or if an expected
# output line is absent. Error detection: Singular prefixes every interpreter error line with "?" (e.g. "   ? ...",
# "? error occurred in ..."), and warnings with "// **". Every line starting (after blanks) with "?" is an error;
# every "// **" line (after blanks) other than the library "redefining" notices is treated as an error too.
# The complete output is written to a file first and then scanned (no early-exit pipe, so a long output cannot
# hide an error via SIGPIPE). Beyond these markers, correctness rests on the explicit content checks below.
set -euo pipefail
command -v Singular >/dev/null || { echo "Singular not found" >&2; exit 1; }
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
run() {  # run <script> <log>
  if ! Singular -q "$1" > "$TMP" 2>&1; then cat "$TMP" >&2; echo "Singular failed on $1" >&2; exit 1; fi
  local nerr nwarn
  nerr=$(grep -Ec '^[[:space:]]*\?|error occurred|halt' "$TMP" || true)
  nwarn=$(grep -E '^[[:space:]]*// \*\*' "$TMP" | grep -vc 'redefining' || true)
  if [ "$nerr" != "0" ]; then cat "$TMP" >&2; echo "Singular reported an error in $1" >&2; exit 1; fi
  if [ "$nwarn" != "0" ]; then cat "$TMP" >&2; echo "Singular reported a warning in $1" >&2; exit 1; fi
  grep -v 'redefining' "$TMP" | grep -v '^[[:space:]]*//' | sed 's/[[:space:]]*$//' > "$2" || true
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
