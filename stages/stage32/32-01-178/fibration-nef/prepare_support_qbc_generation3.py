#!/usr/bin/env python3
"""One-shot verified generation-2 carry and bounded adjacent-b selector."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
from verify_local_support_qbc_receipt import validate, source_context

HERE = Path(__file__).resolve().parent


def dump(path, obj):
    with path.open('w', encoding='utf8', newline='\n') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--durable', type=Path, required=True)
    ap.add_argument('--source-root', type=Path, required=True)
    args = ap.parse_args()
    status = json.loads((args.durable/'status.json').read_text())
    assert status['status'] == 'COMPLETE' and status['stop_reason'] is None
    assert not status['running'] and not status['failed'] and status['remaining_units'] == 0
    kp = HERE/'SUPPORT-QBC-LOCAL-WAVE-RUNKEY.json'
    key = json.loads(kp.read_text())
    assert key['generation'] == 2 and key['armed'] is False
    prior_path = HERE/key['carry_manifest']
    assert hashlib.sha256(prior_path.read_bytes()).hexdigest() == key['carry_manifest_sha256']
    prior = json.loads(prior_path.read_text())
    items = prior['receipts']
    for item in items:
        assert validate(HERE/item['path'], args.source_root) == item['verified']
    assert len(items) == 131
    sources = sorted(args.durable.glob('row*-b*.json'))
    assert len(sources) == len(status['completed']) == 157
    results = [validate(p, args.source_root) for p in sources]
    assert all(v in status['completed'] for v in results)
    saving = sum(int(v['saving']) for v in results)
    assert saving == int(status['exact_disjoint_reduction'])
    outdir = HERE/'local-support-qbc/generation2'
    outdir.mkdir(exist_ok=False)
    for p,v in zip(sources, results):
        dest = outdir/p.name
        shutil.copyfile(p,dest)
        assert p.read_bytes() == dest.read_bytes()
        items.append({'path': dest.relative_to(HERE).as_posix(), 'verified': v})
    coordinates = sorted((i['verified']['row_index'],i['verified']['b']) for i in items)
    assert len(coordinates) == len(set(coordinates)) == 288
    old_universe = {(r,b) for r in key['authorized_rows'] for b in key['authorized_b']}
    assert set(coordinates) == old_universe, 'previous domain not complete'
    rows, _, _ = source_context(str(args.source_root))
    assert all(int(rows[r][2])//2 >= 75 for r in key['authorized_rows'])
    next_b = list(range(72,76))
    planned = sorted((r,b) for r in key['authorized_rows'] for b in next_b)
    assert len(planned) == 48 and not set(planned)&set(coordinates)
    neighbors = [v for v in results if v['b'] == 71]
    assert len(neighbors) == 12
    neighbor_saving = sum(int(v['saving']) for v in neighbors)
    neighbor_wall = sum(v['wall_seconds'] for v in neighbors)
    maxrss = max(json.loads(p.read_text())['timing']['peak_rss_bytes'] for p in sources)
    manifest = {
        'schema':'STAGE32_178_SUPPORT_QBC_CARRY_UNION_V1',
        'discovered_artifact_count':len(sources)+prior['discovered_artifact_count'],
        'validated_carried_unit_count':len(items), 'receipts':items,
        'generation2_saving':str(saving), 'generation2_elapsed_seconds':status['elapsed_seconds'],
        'union_saving':str(sum(int(i['verified']['saving']) for i in items)),
        'baseline_upper_bound':'138652739800650593494', 'new_planned_units':planned,
        'source_worker_unchanged':key['worker_blob_sha1'], 'max_generation2_peak_rss_bytes':maxrss,
        'selector':{'observed_b71_saving':str(neighbor_saving),'observed_b71_sum_worker_wall':neighbor_wall,
                    'observed_b71_reduction_per_worker_hour':neighbor_saving*3600/neighbor_wall,
                    'next_b':next_b,'heuristic_only':True,'confidence':'medium-low',
                    'expected_wave_saving':str(neighbor_saving*4*85//100),
                    'expected_wave_wall_hours_at_four_workers':neighbor_wall/3600*1.1,
                    'reason':'bounded nearby b; existing necessary condition unchanged; b71 measured ROI exceeds row65 benchmark'},
        'credit':0,'hostile_audit_required':True,'incremental_vs_grf04_unknown':True,
    }
    mp = HERE/'local-support-qbc/GENERATION2-CARRY.json'
    assert not mp.exists()
    dump(mp,manifest)
    key['carry_manifest'] = mp.relative_to(HERE).as_posix()
    key['carry_manifest_sha256'] = hashlib.sha256(mp.read_bytes()).hexdigest()
    key['excluded_completed_units'] = coordinates
    key['authorized_b'] = next_b+key['authorized_b']
    key['expected_authorized_units'] = len(planned)
    key['max_elapsed_hours'] = 6
    dump(kp,key)
    print(json.dumps({k:manifest[k] for k in ('validated_carried_unit_count','generation2_saving','generation2_elapsed_seconds','union_saving','max_generation2_peak_rss_bytes','selector')},sort_keys=True))


if __name__ == '__main__':
    main()
