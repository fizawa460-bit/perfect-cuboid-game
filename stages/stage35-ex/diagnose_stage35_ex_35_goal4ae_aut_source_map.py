#!/usr/bin/env python3
"""Bounded metadata-only diagnostic for the retained Stage32 Aut(S) generators.

This intentionally does not print the retained permutations or opaque payloads.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIC_DIR = ROOT / 'stages/stage33/33-07'
sys.path.insert(0, str(PIC_DIR))
from stage32_picard_marking_retained import load as load_marking

marking = load_marking()
aut = marking['aut_action']
perms = aut.get('permutations_1based', [])

meta = {}
for k, v in aut.items():
    if k == 'permutations_1based':
        continue
    if isinstance(v, (str, int, float, bool)) or v is None:
        meta[k] = v
    elif isinstance(v, list):
        # Only print short scalar lists. Never expand nested/opaque payloads.
        if len(v) <= 32 and all(isinstance(x, (str, int, float, bool)) or x is None for x in v):
            meta[k] = v
        else:
            meta[k] = {'type': 'list', 'length': len(v)}
    elif isinstance(v, dict):
        meta[k] = {'type': 'dict', 'keys': sorted(map(str, v.keys()))[:32], 'key_count': len(v)}
    else:
        meta[k] = {'type': type(v).__name__}

cycles = []
for idx, p in enumerate(perms, 1):
    seen = set(); lens = []
    for x in range(1, len(p)+1):
        if x in seen:
            continue
        y=x; n=0
        while y not in seen:
            seen.add(y); n += 1; y = p[y-1]
        lens.append(n)
    cycles.append({
        'index_1based': idx,
        'fixed_points_on_known140': sum(1 for i,x in enumerate(p,1) if i==x),
        'cycle_lengths': sorted(lens),
    })

out = {
    'schema': 'STAGE35_EX_GOAL4AE_AUT_SOURCE_MAP_DIAGNOSTIC_V1',
    'aut_metadata': meta,
    'generator_count': len(perms),
    'generator_cycle_summaries': cycles,
    'opaque_permutations_printed': False,
}
print('GOAL4AE_AUT_SOURCE_MAP_JSON=' + json.dumps(out, sort_keys=True, separators=(',', ':')))
