#!/bin/bash
# D8-LOW-GENUS: rebuild certified_enum from the committed source with the exact flags used for
# certified_results.jsonl, and compare its sha256 with the one recorded in PROVENANCE.json.
# (gcc 15.2.0, Ubuntu x86-64; a different compiler version may legitimately give a different binary hash.)
set -euo pipefail
cd "$(dirname "$0")"
gcc -O2 -std=c11 -Wall -ffp-contract=off -fno-fast-math -o /tmp/certified_enum_repro certified_enum.c -lm
gcc --version | head -1
sha256sum certified_enum.c /tmp/certified_enum_repro
