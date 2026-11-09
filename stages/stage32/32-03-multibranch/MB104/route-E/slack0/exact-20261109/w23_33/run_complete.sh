#!/bin/sh
set -eu
# Run from the parent directory of exact_w.
python exact_w/degree3_enumeration.py > exact_w/degree3_log.txt
python exact_w/modular_search.py 874009
python exact_w/validate_lifting.py
python - <<'PY'
import json
D=json.load(open('exact_w/split_data.json'));f=open('exact_w/split_data.txt','w');print(D['p'],len(D['maps']),file=f)
for b in D['B']:print(*b,file=f)
for m in D['maps']:
 print(m['n'],file=f)
 for k in ['P','Q','pts','labs']:print(*m[k],file=f)
PY
g++ -O3 -std=c++17 exact_w/match.cpp -o exact_w/match
exact_w/match < exact_w/split_data.txt > exact_w/match_result.txt 2> exact_w/match_progress.txt
python - <<'PY'
from pathlib import Path
s=Path('exact_w/match_result.txt').read_text()
assert 'PAIR 2 3 TOTAL 230688 UNCLASSIFIED 0' in s
assert 'PAIR 3 3 TOTAL 3287808 UNCLASSIFIED 0' in s
assert 'HIT 0 8400' in s and 'HIT 4 496' in s
print(s)
print('PASS finite-field exhaustive certificate; characteristic-zero consequence uses PROOF.md')
PY
