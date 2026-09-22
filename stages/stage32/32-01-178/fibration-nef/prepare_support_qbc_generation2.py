#!/usr/bin/env python3
"""One-shot generation-1 retention and cold generation-2 preparation. No compute."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
from verify_local_support_qbc_receipt import validate

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
    assert status['status'] == 'STOPPED' and status['stop_reason'] == 'ONE_PERCENT_EXACT_CANDIDATE_REACHED'
    assert not status['running'] and not status['failed']
    kp = HERE/'SUPPORT-QBC-LOCAL-WAVE-RUNKEY.json'
    key = json.loads(kp.read_text())
    assert key['generation'] == 1 and key['armed'] is False
    sources = sorted(args.durable.glob('row*-b*.json'))
    assert len(sources) == len(status['completed']) == 130
    outdir = HERE/'local-support-qbc/generation1'
    outdir.mkdir(exist_ok=False)
    items = []
    raw = []
    for p in sources:
        v = validate(p, args.source_root)
        assert v in status['completed']
        dest = outdir/p.name
        shutil.copyfile(p, dest)
        assert p.read_bytes() == dest.read_bytes()
        items.append({'path': dest.relative_to(HERE).as_posix(), 'verified': v})
        raw.append(json.loads(p.read_text()))
    saving = sum(int(i['verified']['saving']) for i in items)
    assert saving == int(status['exact_disjoint_reduction'])
    first = HERE/'local-support-qbc/row022-b047.json'
    items.append({'path': first.relative_to(HERE).as_posix(), 'verified': validate(first, args.source_root)})
    coordinates = sorted((i['verified']['row_index'], i['verified']['b']) for i in items)
    assert len(coordinates) == len(set(coordinates)) == 131
    universe = {(r,b) for r in key['authorized_rows'] for b in key['authorized_b']}
    remaining = universe-set(coordinates)
    assert len(remaining) == 157 and set(coordinates) <= universe
    bands = []
    for b in sorted({i['verified']['b'] for i in items}):
        group = [i['verified'] for i in items if i['verified']['b'] == b]
        bands.append({'b': b, 'count': len(group), 'saving': str(sum(int(v['saving']) for v in group)), 'sum_worker_wall_seconds': sum(v['wall_seconds'] for v in group)})
    manifest = {
        'schema': 'STAGE32_178_SUPPORT_QBC_CARRY_UNION_V1',
        'discovered_artifact_count': len(sources)+1, 'validated_carried_unit_count': len(items),
        'generation1_saving': str(saving), 'generation1_elapsed_seconds': status['elapsed_seconds'],
        'union_saving': str(sum(int(i['verified']['saving']) for i in items)),
        'baseline_upper_bound': '138652739800650593494', 'remaining_authorized_units': sorted(remaining),
        'receipts': items, 'band_measurements': bands,
        'source_worker_unchanged': key['worker_blob_sha1'],
        'max_worker_peak_rss_bytes': max(r['timing']['peak_rss_bytes'] for r in raw),
        'max_receipt_bytes': max(p.stat().st_size for p in sources),
        'credit': 0, 'hostile_audit_required': True, 'incremental_vs_grf04_unknown': True,
    }
    mp = HERE/'local-support-qbc/GENERATION1-CARRY.json'
    assert not mp.exists()
    dump(mp, manifest)
    key['excluded_completed_units'] = coordinates
    key['expected_authorized_units'] = len(remaining)
    key['stop_new_dispatch_at_exact_reduction'] = None
    key['carry_manifest'] = mp.relative_to(HERE).as_posix()
    key['carry_manifest_sha256'] = hashlib.sha256(mp.read_bytes()).hexdigest()
    # b47 benchmark is stronger per worker-hour than the late b70 region.
    key['authorized_b'] = list(range(47,35,-1))+list(range(60,72))
    key['continuation_authority'] = 'User explicitly authorized useful local computation beyond 1%; normal-wave continuation only; no retries through failure.'
    dump(kp, key)
    print(json.dumps({k: manifest[k] for k in ('validated_carried_unit_count','generation1_saving','generation1_elapsed_seconds','union_saving','max_worker_peak_rss_bytes','max_receipt_bytes','band_measurements')}, sort_keys=True))


if __name__ == '__main__':
    main()
