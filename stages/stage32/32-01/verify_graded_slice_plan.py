#!/usr/bin/env python3
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
p = json.loads((ROOT / 'graded-slice-manifest.json').read_text())
assert p['schema'] == 'STAGE32_GRADED_SLICE_MANIFEST_V1'
assert p['row_count'] == 183
rows = p['rows']
assert sum(1 for r in rows if r['genus']==0) == 88
assert sum(1 for r in rows if r['genus']==1) == 95
assert max(r['degree'] for r in rows if r['genus']==0) == 176
assert max(r['degree'] for r in rows if r['genus']==1) == 192

def stable_id(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()[:20]

count=0
global_ids=set()
for r in rows:
    d=r['degree']; total=19*d
    assert r['positive_identity_total']==total
    assert r['exceptional_coordinate_cap']==total//5
    assert r['nonexceptional_coordinate_cap']==total
    assert len(r['strata']) == total//5 + 1
    for s in r['strata']:
        e=s['exceptional_mass']; nm=total-5*e
        assert e >= 0 and s['nonexceptional_mass']==nm and nm >= 0
        key={'g':r['genus'],'d':d,'exceptional_mass':e,'nonexceptional_mass':nm}
        assert s['id']==stable_id(key)
        assert s['id'] not in global_ids
        global_ids.add(s['id'])
    count += len(r['strata'])
assert count == p['stratum_count']
stored=p['manifest_sha256']
q=dict(p); q.pop('manifest_sha256')
recomputed=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert stored==recomputed
assert p['complete_census_claim'] is False
print(json.dumps({'verified':True,'row_count':183,'stratum_count':count,'global_unique_ids':len(global_ids),'manifest_sha256':recomputed},sort_keys=True))
