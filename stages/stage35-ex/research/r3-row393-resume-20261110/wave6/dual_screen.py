"""Screen new rows against the previous finite dual, extended by zero on new columns.

This is a necessary-condition diagnostic, not an actual class-group character
or a claim that an individual row removes the obstruction.
"""
import hashlib
import json
from pathlib import Path

if not __debug__:
    raise RuntimeError('Python -O is unsupported')
out = Path(__file__).resolve().parent
old = out.parent / 'wave5'
dual_bytes = (old / 'dual_wave5.json').read_bytes()
dual = json.loads(dual_bytes)
assert dual['all_rows_annihilated'] and dual['p827_value'] == 1
support = {tuple(label) for label in dual['nonzero_labels']}
factors = {int(p): value for p, value in json.loads((old / 'factorizations_wave5.json').read_text()).items()}
labels = {(2, 0), (2, 1)} | {(p, j) for p, v in factors.items() for j in range(len(v[0]))}
assert support <= labels and (827, 0) in support and len(labels) == 69432
rows = json.loads((out / 'new_relations_wave6.json').read_text())
hits = []
old_only = []
for i, row in enumerate(rows):
    parity = {(p, j) for p, j, e in row['valuations'] if e % 2}
    value = len(parity & support) % 2
    if value:
        hits.append(i)
    if parity <= labels:
        old_only.append((i, value))
result = {
    'old_dual_sha256': hashlib.sha256(dual_bytes).hexdigest(),
    'extension': 'zero on prime-ideal columns absent from the wave5 presentation',
    'new_rows': len(rows),
    'prior_dual_one_count': len(hits),
    'prior_dual_one_indices': hits,
    'old_columns_only_count': len(old_only),
    'old_columns_only_dual_one_indices': [i for i, value in old_only if value],
    'scope': 'finite presentation diagnostic only; a hit alone neither proves P827 zero nor excludes a new dual extension',
}
(out / 'dual_screen.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if not k.endswith('_indices')}))
