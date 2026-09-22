#!/usr/bin/env python3
"""Validate a complete single-b receipt; this does not rerun exact counting."""
import argparse
import hashlib
import json
import subprocess
import importlib.util
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=None)
def committed(repo, revision, rel):
    return subprocess.check_output(['git', '-C', str(repo), 'show', revision+':'+rel])


@lru_cache(maxsize=1)
def source_context(source_root):
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('receipt_worker', here/'run_hpadj22_support_qbc_local_row_b.py')
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    direct = worker.load(here.parents[3]/'stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py', 'receipt_direct')
    old = direct.load_old(Path(source_root))
    ctx = old.source_context()
    return ctx[8], old.PLANNED, old.row_source_locks(ctx[0], ctx[1], ctx[2], ctx[6])


def validate(p, source_root=None):
    obj = json.loads(Path(p).read_text())
    body = dict(obj)
    sha = body.pop('canonical_sha256_without_this_field')
    assert hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode()).hexdigest() == sha
    assert obj['schema'] in ('STAGE32_178_LOCAL_SUPPORT_QBC_SINGLE_B_V1', 'STAGE32_178_LOCAL_SUPPORT_QBC_ROW_B_V1')
    general = obj['schema'].endswith('ROW_B_V1')
    t = obj['target']
    if not general:
        assert (t['row_id'], t['g'], t['d'], t['row_index']) == ('g1-d192', 1, 192, 22)
    assert t['g'] in (0, 1) and t['d'] % 2 == 0 and 0 <= t['row_index'] < 178
    assert t['row_id'] == f"g{t['g']}-d{t['d']:03d}"
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
        assert p-v == int(cell['additional_reduction_vs_parent_qbc'])
        cell_sum += c-v
    assert cell_sum == saving and len(seen) == r['strict_bc_cells']
    visited = obj['visited_cells']
    assert len({(x['b'], x['c']) for x in visited}) == len(visited)
    assert all(x['b'] == lo and 0 <= x['c'] <= 96 for x in visited)
    assert sum(int(x['current']) for x in visited) == cur
    assert sum(int(x['parent_refined']) for x in visited) == par
    assert sum(int(x['refined']) for x in visited) == ref
    assert all(0 <= int(x['refined']) <= int(x['parent_refined']) <= int(x['current']) for x in visited)
    if general:
        assert {x['c'] for x in visited} == set(range(t['d']//2+1)), 'incomplete c traversal'
    by_c = {x['c']: x for x in visited}
    for x in obj['strict_cells']:
        v = by_c[x['c']]
        assert tuple(int(x[k]) for k in ('current', 'parent_qbc_refined', 'support_qbc_refined')) == tuple(int(v[k]) for k in ('current', 'parent_refined', 'refined'))
    assert {x['c'] for x in obj['strict_cells']} == {x['c'] for x in visited if int(x['current']) > int(x['refined'])}
    assert int(r['current_global_upper_bound']) == 138652739800650593494
    assert int(r['candidate_global_upper_bound_if_promoted']) == 138652739800650593494-saving
    assert int(r['one_percent_threshold']) == 1386527398006505935
    assert r['one_percent_reached_by_this_single_row_band'] == (100*saving >= 138652739800650593494)
    for k in ('main_credit_changed', 'theorem_credit_changed', 'endpoint_credit_changed', 'merge', 'full178_complete'):
        assert obj['firewalls'][k] is False
    assert obj['firewalls']['hostile_audit_required_before_promotion'] is True
    here = Path(__file__).resolve().parent
    repo = here.parents[3]
    worker = 'run_hpadj22_support_qbc_local_row_b.py' if general else 'run_hpadj22_zero_center_support_qbc_local_b.py'
    raw = (here/worker).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == obj['source_locks']['local_worker_blob_sha1']
    locks = obj['source_locks']
    head, before = locks['execution_head'], locks['authorization_before']
    rel = (here/worker).relative_to(repo).as_posix()
    assert committed(repo, head, rel) == raw, 'worker differs from execution commit'
    keyname = 'SUPPORT-QBC-LOCAL-WAVE-RUNKEY.json' if general else 'SUPPORT-QBC-LOCAL-RUNKEY.json'
    kr = (here/keyname).relative_to(repo).as_posix()
    key = json.loads(committed(repo, head, kr))
    prior = json.loads(committed(repo, before, kr))
    subprocess.run(['git','-C',str(repo),'merge-base','--is-ancestor',before,head], check=True)
    assert key['armed'] is True and key['generation'] > prior['generation']
    assert key['worker_blob_sha1'] == locks['local_worker_blob_sha1'] and lo in key['authorized_b']
    if general:
        assert t['row_index'] in key['authorized_rows'] and [t['row_index'], lo] not in key['excluded_completed_units']
    dependencies = {
        'fast_qbc_parent_blob_sha1': here/'verify_hpadj22_zero_center_qbc_tinterval_g1d192_band4_fast.py',
        'mathematical_qbc_parent_blob_sha1': here/'verify_hpadj22_zero_center_qbc_tinterval_g1d192_band4.py',
        'direct_count_blob_sha1': repo/'stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py',
        'zero_center_picard_blob_sha1': here/'verify_fibration_nef_lowmass_parity_separable_picard_min.py',
    }
    for k, path in dependencies.items():
        data = path.read_bytes()
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == locks[k], k
    assert locks['hpadj22_source_head'] == '4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2'
    if general:
        assert source_root is not None, 'generalized receipt requires source manifest verification'
        rows, bands, expected_locks = source_context(str(source_root))
        rid, rg, rd = rows[t['row_index']]
        assert (rid, int(rg), int(rd)) == (t['row_id'], t['g'], t['d'])
        assert locks['hpadj22_row_source_locks'] == expected_locks
        assert list(bands[t['band_position']]) == t['containing_band_interval']
        assert bands[t['band_position']][0] <= lo <= bands[t['band_position']][1]
    assert obj['semantics']['main_consumption_performed'] is False
    return {'status': 'PASS', 'row_index': t['row_index'], 'row_id': t['row_id'], 'b': lo, 'current': str(cur), 'refined': str(ref), 'saving': str(saving), 'canonical': sha, 'wall_seconds': obj['timing']['wall_seconds'], 'cpu_seconds': obj['timing']['cpu_seconds']}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('receipts', nargs='+')
    ap.add_argument('--source-root')
    a = ap.parse_args()
    results = [validate(p, a.source_root) for p in a.receipts]
    assert len({(x['row_index'], x['b']) for x in results}) == len(results), 'duplicate row,b receipts'
    print(json.dumps({'receipts': results, 'exact_saving': str(sum(int(x['saving']) for x in results)), 'credit': 0}, sort_keys=True))
