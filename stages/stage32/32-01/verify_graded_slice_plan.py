#!/usr/bin/env python3
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
p = json.loads((ROOT / 'graded-slice-manifest.json').read_text())
assert p['schema'] == 'STAGE32_GRADED_SLICE_MANIFEST_V1'
assert p['row_count'] == 183
rows = p['rows']
assert sum(1 for r in rows if r['genus']==0) == 88
assert sum(1 for r in rows if r['genus']==1) == 95
assert max(r['degree'] for r in rows if r['genus']==0) == 176
assert max(r['degree'] for r in rows if r['genus']==1) == 192
count = 0
for r in rows:
    d=r['degree']; total=19*d
    assert r['positive_identity_total']==total
    assert r['exceptional_coordinate_cap']==total//5
    assert r['nonexceptional_coordinate_cap']==total
    assert len(r['strata']) == total//5 + 1
    ids=set()
    for s in r['strata']:
        assert s['exceptional_mass'] >= 0
        assert s['nonexceptional_mass'] == total - 5*s['exceptional_mass']
        assert s['nonexceptional_mass'] >= 0
        assert s['id'] not in ids
        ids.add(s['id'])
    count += len(r['strata'])
assert count == p['stratum_count']
assert p['complete_census_claim'] is False
print(json.dumps({'verified':True,'row_count':183,'stratum_count':count,'manifest_sha256':p['manifest_sha256']},sort_keys=True))
