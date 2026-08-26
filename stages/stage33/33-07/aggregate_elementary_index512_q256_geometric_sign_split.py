#!/usr/bin/env python3
"""Aggregate the exact q256 finite-q + seven-geometric-sign shards."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE/'q256-geometric-sign-shards'
files=sorted(ROOT.glob('elementary-index512-q256-geometric-sign-shard-*.json'))
if len(files)!=32:raise SystemExit(f'expected 32 geometric-sign shards, got {len(files)}')
rows=[];source_q=None;source_fullq=None;endpoint=None;shards=set()
for p in files:
    x=json.loads(p.read_text())
    if x['schema']!='STAGE33_07_ELEMENTARY_INDEX512_Q256_GEOMETRIC_SIGN_SPLIT_SHARD_V1':raise SystemExit('shard schema moved')
    if x['arithmetic_cc_ct_used'] is not False or x['geometric_coordinate_signs_used']!=7:raise SystemExit('geometric-only firewall moved')
    if x['shard_count']!=32 or x['candidate_count']!=8:raise SystemExit('shard partition moved')
    shards.add(int(x['shard_index']))
    source_q=source_q or x['source_q256_sha256'];source_fullq=source_fullq or x['source_full_q_sha256'];endpoint=endpoint or x['endpoint_coordinate_sign_sha256']
    if (source_q,source_fullq,endpoint)!=(x['source_q256_sha256'],x['source_full_q_sha256'],x['endpoint_coordinate_sign_sha256']):raise SystemExit('cross-shard source lock mismatch')
    if x['actual_index512_glue_identified'] or x['INDEX512_GLUE_ACTUAL_GEOMETRY_PROVED']:raise SystemExit('shard overclaim regression')
    rows.extend(x['results'])
if shards!=set(range(32)):raise SystemExit('missing shard index')
rows=sorted(rows,key=lambda z:int(z['index']))
if [int(r['index']) for r in rows]!=list(range(256)):raise SystemExit('q256 coverage regression')
surv=[int(r['index']) for r in rows if r['simultaneous_q_7geometric_sign_conjugacy']]
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_GEOMETRIC_SIGN_SPLIT_CENSUS_V1',
 'source_q256_sha256':source_q,'source_full_q_sha256':source_fullq,'endpoint_coordinate_sign_sha256':endpoint,
 'candidate_count_before':256,'arithmetic_cc_ct_used':False,'geometric_coordinate_signs_used':7,
 'simultaneous_q_7geometric_sign_survivor_count':len(surv),'rejected_count':256-len(surv),'survivor_indices':surv,
 'all_256_decided_exactly':True,
 'interpretation':'elementary branch only; actual geometry may still be non-elementary, so this census does not identify T(S)/L0',
 'actual_index512_glue_identified':False,'INDEX512_GLUE_ACTUAL_GEOMETRY_PROVED':False,
 'next_exact_leaf':'L33-07-COMBINE-ELEMENTARY-Q7SIGN-CENSUS-WITH-PURE-GEOMETRIC-NONELEMENTARY-SIGN-Q-FILTERS',
 'new_residual_kernel':'R33-BR2A-ELEMENTARY-Q7SIGN-EXACT-CENSUS-PLUS-NONELEMENTARY-PURE-GEOMETRIC-BRANCH',
 'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,'unit_status':'RUNNING_REPAIR',
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
out=HERE/'elementary-index512-q256-geometric-sign-split-census.json';out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':256,'survivors':len(surv),'survivor_indices':surv,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
