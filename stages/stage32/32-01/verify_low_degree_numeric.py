#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent


def kept_from_stdout(s: str) -> int:
    m = re.search(r'kept=(\d+)', s or '')
    if not m:
        raise SystemExit(f'missing kept= field in transcript: {s!r}')
    return int(m.group(1))

# Degree-2 genus-0 regression.
d2 = (ROOT / 'numeric-magma-slice-d2-g0.txt').read_text()
m = re.search(r'STAGE32_NUMERIC_SLICE d=2 g=0 raw=(\d+) kept=(\d+)', d2)
if not m:
    raise SystemExit('missing d2/g0 regression transcript')
d2_raw, d2_kept = map(int, m.groups())
if d2_kept != 0 or 'STAGE32_NUMERIC_SLICE_END' not in d2:
    raise SystemExit('d2/g0 regression is not cleanly closed')

# Degree-4 genus-1: all exceptional-mass strata already completed in the
# first-level checkpoint.
d4 = json.loads((ROOT / 'numeric-magma-strata-d4-g1.json').read_text())
if not d4.get('all_completed') or len(d4.get('results', [])) != 16:
    raise SystemExit('d4/g1 strata checkpoint incomplete')
d4_raw = 0
for r in d4['results']:
    if not r.get('ok'):
        raise SystemExit(f'd4/g1 failed stratum e={r.get("e")}')
    d4_raw += int(re.search(r'raw=(\d+)', r.get('stdout', '')).group(1))
    if kept_from_stdout(r.get('stdout', '')) != 0:
        raise SystemExit(f'd4/g1 survivor in e={r.get("e")}')

# Degree-6 genus-1: use the original successful strata and exact adaptive
# curve-group refinements for the seven calculator-timeout strata.
d6 = json.loads((ROOT / 'numeric-magma-strata-d6-g1.json').read_text())
original = {int(r['e']): r for r in d6['results']}
timeout_e = {0, 2, 4, 6, 8, 10, 12}
covered = set()
d6_raw = 0
for e in range(23):
    if e in timeout_e:
        p = ROOT / f'numeric-magma-curvegroup-adaptive-d6-g1-e{e}.json'
        if not p.exists():
            raise SystemExit(f'missing adaptive d6/g1/e{e} checkpoint')
        a = json.loads(p.read_text())
        if not a.get('all_completed') or a.get('completed_row_count') != a.get('expected_row_count'):
            raise SystemExit(f'adaptive d6/g1/e{e} incomplete')
        if a.get('kept_total') != 0:
            raise SystemExit(f'd6/g1/e{e} has survivors')
        d6_raw += int(a.get('raw_total', 0)); covered.add(e)
    else:
        r = original.get(e)
        if not r or not r.get('ok'):
            raise SystemExit(f'original d6/g1/e{e} checkpoint missing or failed')
        if kept_from_stdout(r.get('stdout', '')) != 0:
            raise SystemExit(f'd6/g1/e{e} has survivors')
        mr = re.search(r'raw=(\d+)', r.get('stdout', ''))
        if not mr:
            raise SystemExit(f'missing raw count d6/g1/e{e}')
        d6_raw += int(mr.group(1)); covered.add(e)
if covered != set(range(23)):
    raise SystemExit('d6/g1 coverage mismatch')

payload = {
    'schema': 'STAGE32_LOW_DEGREE_NUMERIC_CHECKPOINT_V1',
    'scope': 'REGRESSION_AND_PRODUCTION_PREFIX_ONLY',
    'd2_g0': {'complete': True, 'raw': d2_raw, 'kept': d2_kept},
    'd4_g1': {'complete': True, 'strata': 16, 'raw': d4_raw, 'kept': 0},
    'd6_g1': {'complete': True, 'strata': 23, 'raw': d6_raw, 'kept': 0,
              'adaptive_exceptional_masses': sorted(timeout_e)},
    'full_d176_d192_numerical_orbit_census': False,
    'receiver_credit': False,
}
(ROOT / 'numeric-low-degree-summary.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')
print(json.dumps(payload, sort_keys=True))
