#!/usr/bin/env python3
"""Validate a complete single-b receipt; this does not rerun exact counting."""
import argparse
import hashlib
import json
from pathlib import Path


def validate(p):
    obj = json.loads(Path(p).read_text())
    body = dict(obj)
    sha = body.pop('canonical_sha256_without_this_field')
    assert hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode()).hexdigest() == sha
    assert obj['schema'] == 'STAGE32_178_LOCAL_SUPPORT_QBC_SINGLE_B_V1'
    t = obj['target']
    assert (t['row_id'], t['g'], t['d'], t['row_index']) == ('g1-d192', 1, 192, 22)
    lo, hi = t['b_interval']
    assert lo == hi and not 48 <= lo <= 59
    r = obj['result']
    cur, par, ref = (int(r[k]) for k in ('current_row_band_survivors', 'parent_qbc_refined_survivors', 'support_qbc_refined_survivors'))
    assert 0 <= ref <= par <= cur
    saving = cur - ref
    assert saving == int(r['support_qbc_exact_reduction'])
    assert cur-par == int(r['parent_qbc_exact_reduction'])
    assert par-ref == int(r['additional_reduction_vs_parent_qbc'])
    seen = set()
    cell_sum = 0
    for cell in obj['strict_cells']:
        key = (cell['b'], cell['c'])
        assert key[0] == lo and 0 <= key[1] <= 96 and key not in seen
        seen.add(key)
        c, p, v = (int(cell[k]) for k in ('current', 'parent_qbc_refined', 'support_qbc_refined'))
        assert 0 <= v <= p <= c and c-v == int(cell['reduction']) > 0
        assert p-v == int(cell['additional_reduction_vs_parent'])
        cell_sum += c-v
    assert cell_sum == saving and len(seen) == r['strict_bc_cells']
    visited = obj['visited_cells']
    assert len({(x['b'], x['c']) for x in visited}) == len(visited)
    assert all(x['b'] == lo and 0 <= x['c'] <= 96 for x in visited)
    assert sum(int(x['current']) for x in visited) == cur
    assert sum(int(x['parent_refined']) for x in visited) == par
    assert sum(int(x['refined']) for x in visited) == ref
    assert int(r['current_global_upper_bound']) == 138652739800650593494
    assert int(r['candidate_global_upper_bound_if_promoted']) == 138652739800650593494-saving
    assert int(r['one_percent_threshold']) == 1386527398006505935
    assert r['one_percent_reached_by_this_single_row_band'] == (100*saving >= 138652739800650593494)
    for k in ('main_credit_changed', 'theorem_credit_changed', 'endpoint_credit_changed', 'merge', 'full178_complete'):
        assert obj['firewalls'][k] is False
    assert obj['firewalls']['hostile_audit_required_before_promotion'] is True
    here = Path(__file__).resolve().parent
    raw = (here/'run_hpadj22_zero_center_support_qbc_local_b.py').read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == obj['source_locks']['local_worker_blob_sha1']
    return {'status': 'PASS', 'b': lo, 'current': str(cur), 'refined': str(ref), 'saving': str(saving), 'canonical': sha}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('receipts', nargs='+')
    a = ap.parse_args()
    results = [validate(p) for p in a.receipts]
    assert len({x['b'] for x in results}) == len(results), 'duplicate b receipts'
    print(json.dumps({'receipts': results, 'exact_saving': str(sum(int(x['saving']) for x in results)), 'credit': 0}, sort_keys=True))
