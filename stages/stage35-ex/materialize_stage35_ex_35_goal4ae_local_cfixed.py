#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIAG = ROOT / 'stages/stage35-ex/diagnose_stage35_ex_35_goal4ae_local_cfixed.py'
ns = runpy.run_path(str(DIAG))
sets = ns['sets']
actions = ns['actions']
row_times_matrix = ns['row_times_matrix']


def orbit_partition(S):
    unseen = set(S)
    out = []
    while unseen:
        seed = min(unseen)
        orb = {seed}
        queue = [list(seed)]
        stable = True
        while queue:
            v = queue.pop()
            for A in actions:
                w = tuple(row_times_matrix(v, A))
                if w not in S:
                    stable = False
                    break
                if w not in orb:
                    orb.add(w)
                    queue.append(list(w))
            if not stable:
                break
        if not stable:
            return None
        unseen -= orb
        out.append(sorted(orb))
    return sorted(out, key=lambda o: (len(o), o[0]))


matches = []
for name, S in sets.items():
    parts = orbit_partition(S)
    if parts is None:
        continue
    sizes = sorted(len(o) for o in parts)
    if sizes == [8, 48]:
        small = next(o for o in parts if len(o) == 8)
        matches.append({
            'candidate_set': name,
            'orbit_sizes': sizes,
            'c5_candidate_rows_indlist64': [list(r) for r in small],
        })

out = {
    'schema': 'STAGE35_EX_GOAL4AE_LOCAL_CFIXED_MATERIALIZATION_DIAGNOSTIC_V1',
    'expected_8_plus_48_reproduced': bool(matches),
    'matching_filter_count': len(matches),
    'matches': matches,
    'semantic_alignment_to_goal4ac_residual_pair_labels_completed': False,
    'target_span_with_C5_pairs_computed': False,
    'remote_cas_used': False,
    'theorem_credit': False,
    'endpoint_credit': False,
}
print('GOAL4AE_LOCAL_MATERIALIZATION_JSON=' + json.dumps(out, sort_keys=True, separators=(',', ':')))
