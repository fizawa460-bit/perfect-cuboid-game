"""Exact finite-presentation certificate, NOT a character of the true class group."""
import json, runpy
from pathlib import Path
O = Path(__file__).resolve().parent
d = runpy.run_path(str(O/'analyse_pair.py'))
ix, labels, basis = d['ix'], d['labels'], d['piv']
v, _ = d['reduce'](1 << ix[(827,0)], basis)
assert v
t = v.bit_length()-1
assert t not in basis
lam = 1 << t
for k in sorted(basis):
    row = basis[k][0]
    assert row.bit_length()-1 == k
    if (row & lam).bit_count() & 1:
        lam ^= 1 << k
assert all((d['vec'](r)&lam).bit_count()%2 == 0 for r in d['rows'])
value=lambda p,j: (lam >> ix[p,j]) & 1
assert value(827,0)==1
assert value(667801,3)^value(15849133,0)==1
result = dict(scope='finite row393 plus one new relation presentation ONLY; not an actual unramified character',
    checked_row_count=len(d['rows']), column_count=len(labels), rank=len(basis),
    free_coordinate=labels[t], nonzero_dual_labels=[x for i,x in enumerate(labels) if lam>>i&1],
    distinguished_values=[[p,j,value(p,j)] for p,j in [(827,0),(667801,3),(15849133,0)]],
    all_rows_annihilated=True, p827_value=1,
    criterion='Any collection of additional parity rows proving P827=0 must contain a row on which this functional, extended by zero to new columns, is nonzero. This is necessary, not sufficient.')
(O/'dual_obstruction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='nonzero_dual_labels'},indent=2))
print('nonzero_dual_labels',len(result['nonzero_dual_labels']))
