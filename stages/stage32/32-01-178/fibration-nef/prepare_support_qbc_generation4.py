#!/usr/bin/env python3
"""One-shot: validate and retain generation 3, prepare a COLD generation 4 domain."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
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
    assert key['generation'] == 3 and key['armed'] is False
    prior_path = HERE/key['carry_manifest']
    assert hashlib.sha256(prior_path.read_bytes()).hexdigest() == key['carry_manifest_sha256']
    prior = json.loads(prior_path.read_text())
    items = prior['receipts']
    assert len(items) == 288
    for item in items:
        assert validate(HERE/item['path'], args.source_root) == item['verified']
    sources = sorted(args.durable.glob('row*-b*.json'))
    assert len(sources) == len(status['completed']) == 48
    results = [validate(p, args.source_root) for p in sources]
    assert all(v in status['completed'] for v in results)
    saving = sum(int(v['saving']) for v in results)
    assert saving == int(status['exact_disjoint_reduction'])
    coordinates = sorted([(i['verified']['row_index'],i['verified']['b']) for i in items]
                         + [(v['row_index'],v['b']) for v in results])
    assert len(coordinates) == len(set(coordinates)) == 336
    assert set(coordinates) == {(r,b) for r in key['authorized_rows'] for b in key['authorized_b']}
    rows, _, _ = source_context(str(args.source_root))
    assert all(int(rows[r][2])//2 >= 79 for r in key['authorized_rows'])
    next_b = list(range(76,80))
    planned = sorted((r,b) for r in key['authorized_rows'] for b in next_b)
    assert len(planned) == 48 and not set(planned)&set(coordinates)
    neighbors = [v for v in results if v['b'] == 75]
    assert len(neighbors) == 12
    ns = sum(int(v['saving']) for v in neighbors)
    nw = sum(v['wall_seconds'] for v in neighbors)
    assert ns*3600/nw > 1e16, 'marginal ROI no longer supports this extension'
    outdir = HERE/'local-support-qbc/generation3'
    mp = HERE/'local-support-qbc/GENERATION3-CARRY.json'
    assert not mp.exists()
    outdir.mkdir(exist_ok=False)
    for p,v in zip(sources,results):
        dest = outdir/p.name
        shutil.copyfile(p,dest)
        assert p.read_bytes() == dest.read_bytes()
        items.append({'path':dest.relative_to(HERE).as_posix(),'verified':v})
    manifest = {
        'schema':'STAGE32_178_SUPPORT_QBC_CARRY_UNION_V1',
        'discovered_artifact_count':len(sources)+prior['discovered_artifact_count'],
        'validated_carried_unit_count':len(items),'receipts':items,
        'generation3_saving':str(saving),'generation3_elapsed_seconds':status['elapsed_seconds'],
        'union_saving':str(sum(int(i['verified']['saving']) for i in items)),
        'baseline_upper_bound':'138652739800650593494','new_planned_units':planned,
        'source_worker_unchanged':key['worker_blob_sha1'],
        'max_generation3_peak_rss_bytes':max(json.loads(p.read_text())['timing']['peak_rss_bytes'] for p in sources),
        'selector':{'observed_b75_saving':str(ns),'observed_b75_sum_worker_wall':nw,
                    'observed_b75_reduction_per_worker_hour':ns*3600/nw,
                    'next_b':next_b,'heuristic_only':True,'confidence':'medium-low',
                    'expected_wave_saving':str(ns*4*80//100),
                    'expected_wave_wall_hours_at_four_workers':nw/3600*1.15,
                    'reason':'b75 ROI remains useful despite declining mass; bounded four-b test, unchanged predicate'},
        'credit':0,'hostile_audit_required':True,'incremental_vs_grf04_unknown':True,
    }
    dump(mp,manifest)
    key['carry_manifest'] = mp.relative_to(HERE).as_posix()
    key['carry_manifest_sha256'] = hashlib.sha256(mp.read_bytes()).hexdigest()
    key['excluded_completed_units'] = coordinates
    key['authorized_b'] = next_b+key['authorized_b']
    key['expected_authorized_units'] = len(planned)
    key['max_elapsed_hours'] = 6
    dump(kp,key)
    print(json.dumps({k:manifest[k] for k in ('validated_carried_unit_count','generation3_saving','generation3_elapsed_seconds','union_saving','selector')},sort_keys=True))

if __name__ == '__main__':
    main()
