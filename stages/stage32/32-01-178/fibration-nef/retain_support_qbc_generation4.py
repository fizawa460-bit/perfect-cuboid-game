"""One-shot completion retention; does not arm or launch any successor."""
import hashlib
import json
import shutil
from pathlib import Path
from decimal import Decimal
from verify_local_support_qbc_receipt import validate

HERE = Path(__file__).resolve().parent
SOURCE = Path('C:/CodexWorktrees/hpadj22-source-locked')
DURABLE = Path('C:/CodexWorktrees/stage32-support-wave-g4-20260923')

def main():
    key = json.loads((HERE/'SUPPORT-QBC-LOCAL-WAVE-RUNKEY.json').read_text())
    assert key['generation'] == 4 and key['armed'] is False
    mp = HERE/key['carry_manifest']
    assert hashlib.sha256(mp.read_bytes()).hexdigest() == key['carry_manifest_sha256']
    prior = json.loads(mp.read_text())
    items = list(prior['receipts'])
    assert len(items) == 336
    for i in items:
        assert validate(HERE/i['path'], SOURCE) == i['verified']
    status = json.loads((DURABLE/'status.json').read_text())
    assert status['status'] == 'COMPLETE' and status['remaining_units'] == 0
    assert not status['failed'] and not status['running'] and status['stop_reason'] is None
    paths = sorted(DURABLE.glob('row*-b*.json'))
    results = [validate(p, SOURCE) for p in paths]
    assert len(results) == len(status['completed']) == 48
    assert all(v in status['completed'] for v in results)
    assert sum(int(v['saving']) for v in results) == int(status['exact_disjoint_reduction'])
    coords = [(i['verified']['row_index'],i['verified']['b']) for i in items]+[(v['row_index'],v['b']) for v in results]
    assert len(coords) == len(set(coords)) == 384
    assert set(coords) == {(r,b) for r in key['authorized_rows'] for b in key['authorized_b']}
    out = HERE/'local-support-qbc/generation4'
    manifest_path = HERE/'local-support-qbc/GENERATION4-COMPLETE.json'
    assert not manifest_path.exists()
    out.mkdir(exist_ok=False)
    for p,v in zip(paths,results):
        dest = out/p.name
        shutil.copyfile(p,dest)
        assert dest.read_bytes() == p.read_bytes()
        items.append({'path':dest.relative_to(HERE).as_posix(),'verified':v})
    total = sum(int(i['verified']['saving']) for i in items)
    manifest = {'schema':'STAGE32_178_SUPPORT_QBC_CARRY_UNION_V1',
        'discovered_artifact_count':384,'validated_carried_unit_count':384,'receipts':items,
        'union_saving':str(total),'generation4_saving':status['exact_disjoint_reduction'],
        'generation4_elapsed_seconds':status['elapsed_seconds'],
        'baseline_upper_bound':'138652739800650593494',
        'fixed_baseline_percent':str(Decimal(total)*100/Decimal(138652739800650593494)),
        'source_worker_unchanged':key['worker_blob_sha1'],
        'credit':0,'hostile_audit_required':True,'incremental_vs_grf04_unknown':True,
        'successor_armed':False}
    manifest['canonical_sha256_without_this_field'] = hashlib.sha256(json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    with manifest_path.open('x',encoding='utf8',newline='\n') as f:
        json.dump(manifest,f,sort_keys=True,indent=2)
        f.write('\n')
    print(json.dumps({k:v for k,v in manifest.items() if k!='receipts'}))

if __name__ == '__main__':
    main()
