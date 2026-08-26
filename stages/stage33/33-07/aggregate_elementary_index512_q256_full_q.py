#!/usr/bin/env python3
"""Aggregate 8 exact q256 full finite-q isometry shards."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
SURV=json.loads((HERE/'elementary-index512-q256-survivors.json').read_text())
root=HERE/'full-q-shards'
files=sorted(root.glob('elementary-index512-q256-full-q-shard-*.json'))
if len(files)!=8:raise SystemExit(f'full-q shard file count regression {len(files)}')
allr=[];shas=[];distinct=set();iso=0
for f in files:
    x=json.loads(f.read_text());shas.append(x['canonical_sha256'])
    if x['schema']!='STAGE33_07_ELEMENTARY_INDEX512_Q256_FULL_Q_SHARD_V1':raise SystemExit('shard schema regression')
    if x['q256_survivor_sha256']!=SURV['canonical_sha256']:raise SystemExit('shard q256 source lock mismatch')
    if x['candidate_count']!=32:raise SystemExit('shard size regression')
    allr.extend(x['results']);iso+=x['full_q_isometric_count'];distinct.update(r['b8_sha256'] for r in x['results'])
inds=[int(r['index']) for r in allr]
if sorted(inds)!=list(range(256)) or len(set(inds))!=256:raise SystemExit('q256 shard coverage regression')
if any((r['full_q_isometric'] and not r['witness_sha256']) or ((not r['full_q_isometric']) and r['witness_sha256'] is not None) for r in allr):raise SystemExit('witness presence regression')
allr.sort(key=lambda r:int(r['index']))
cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_FULL_Q_CENSUS_V1','q256_survivor_sha256':SURV['canonical_sha256'],'shard_certificate_sha256':shas,'candidate_count_before':256,'distinct_B8_matrix_count':len(distinct),'full_finite_q_isometric_count':iso,'full_finite_q_rejected_count':256-iso,'results':allr,'all_elementary_order512_glue_rejected_by_full_q':iso==0,'actual_index512_glue_identified':False,'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,'next_exact_leaf':('L33-07-ELEMENTARY-BRANCH-REJECTED-CONTINUE-8-NONELEMENTARY-TYPES' if iso==0 else f'L33-07-DECIDE-SIMULTANEOUS-ENDPOINT-V4-CONJUGACY-FOR-{iso}-FULL-Q-ELEMENTARY-H'),'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q256-full-q-census.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':256,'distinct_B8':len(distinct),'full_q_isometric':iso,'full_q_rejected':256-iso,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
