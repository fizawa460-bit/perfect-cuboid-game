#!/bin/bash
# D10-LOW-GENUS: rebuild certified_enum from the committed source with the recorded flags and compare the binary
# sha256 with PROVENANCE.json (= producer_info.binary_sha256 of every record). Exit 0 iff byte-identical;
# exit 2 if the local compiler differs from the recorded one (comparison inconclusive); exit 1 on mismatch.
set -euo pipefail
cd "$(dirname "$0")"
want=$(python3 -c 'import json;print(json.load(open("PROVENANCE.json"))["binary_sha256"])')
flags=$(python3 -c 'import json;print(json.load(open("PROVENANCE.json"))["cflags"])')
comp_want=$(python3 -c 'import json;print(json.load(open("PROVENANCE.json"))["compiler"])')
comp=$(gcc --version | head -1)
out=$(mktemp); trap 'rm -f "$out"' EXIT
gcc $flags -o "$out" certified_enum.c -lm
got=$(sha256sum "$out" | cut -d' ' -f1)
echo "compiler: $comp"; echo "rebuilt:  $got"; echo "recorded: $want"
if [ "$got" = "$want" ]; then echo "reproduce_binary.sh: OK (byte-identical)"; exit 0; fi
if [ "$comp" != "$comp_want" ]; then echo "compiler differs from the recorded one ($comp_want); inconclusive" >&2; exit 2; fi
echo "reproduce_binary.sh: MISMATCH" >&2; exit 1
