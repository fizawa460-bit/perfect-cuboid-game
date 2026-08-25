#!/usr/bin/env python3
"""Aggregate 16 exact simultaneous finite-q + V4 conjugacy shards."""
import hashlib,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
Q256_LOCK='3c68ac5ff99e8e4dd9f57733f1fd64b0637e8a7d7f69454e3bf391b9b8127506'
FULLQ_LOCK='9555ccb575e96ab46f400a353184d4a25ccafc882e8bd3250cc6c811c12fa19e'
root=HERE/'simultaneous-v4-shards'
files=sorted(root.glob('elementary-index512-q256-simultaneous-v4-shard-*.json'))
if len(files)!=16:raise SystemExit(f'simultaneous V4 shard count regression {len(files)}')
allr=[];shas=[];surv=0;cc=Counter();ct=Counter();h0=False
for f in files:
    x=json.loads(f.read_text())
    if x['schema']!='STAGE33_07_ELEMENTARY_INDEX512_Q256_SIMULTANEOUS_V4_SHARD_V1':raise SystemExit('shard schema regression')
    if x['q256_sha256']!=Q256_LOCK or x['full_q_census_sha256']!=FULLQ_LOCK:raise SystemExit('shard source-lock mismatch')
    if x['candidate_count']!=16:raise SystemExit('shard candidate-count regression')
    shas.append(x['canonical_sha256']);surv+=int(x['simultaneous_q_v4_survivor_count']);allr.extend(x['results'])
    cc.update({int(k):int(v) for k,v in x['cc_induced_class_count_census'].items()})
    ct.update({int(k):int(v) for k,v in x['ct_induced_class_count_census'].items()})
    h0=h0 or bool(x.get('h0_rejection_regressed'))
inds=[int(r['index']) for r in allr]
if sorted(inds)!=list(range(256)) or len(set(inds))!=256:raise SystemExit('simultaneous V4 index coverage regression')
if not h0:raise SystemExit('H0 rejection regression was not executed')
if sum(bool(r['simultaneous_q_v4_conjugacy']) for r in allr)!=surv:raise SystemExit('survivor total mismatch')
for r in allr:
    ok=bool(r['simultaneous_q_v4_conjugacy'])
    if ok and (not r['witness_sha256'] or not r['matching_cc_class_indices'] or not r['matching_ct_class_indices']):raise SystemExit('SAT record witness/class regression')
    if not ok and r['witness_sha256'] is not None:raise SystemExit('UNSAT record carries witness')
allr.sort(key=lambda r:int(r['index']))
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_SIMULTANEOUS_V4_CENSUS_V1',
 'q256_sha256':Q256_LOCK,'full_q_census_sha256':FULLQ_LOCK,
 'shard_certificate_sha256':shas,
 'candidate_count_before':256,
 'simultaneous_finite_q_cc_ct_conjugacy_survivor_count':surv,
 'simultaneous_finite_q_cc_ct_conjugacy_rejected_count':256-surv,
 'cc_induced_class_count_census':{str(k):v for k,v in sorted(cc.items())},
 'ct_induced_class_count_census':{str(k):v for k,v in sorted(ct.items())},
 'h0_known_rejection_regressed':True,
 'results':allr,
 'all_elementary_order512_glue_rejected':surv==0,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':('L33-07-ELEMENTARY-GLUE-BRANCH-REJECTED-CONTINUE-8-NONELEMENTARY-TYPES' if surv==0 else f'L33-07-CLASSIFY-{surv}-SIMULTANEOUS-V4-ELEMENTARY-EMBEDDINGS-AGAINST-INTEGRAL-ENDPOINT-GLUE'),
 'new_residual_kernel':('R33-BR2A-INDEX512-NONELEMENTARY-8-ABSTRACT-TYPES-AFTER-ELEMENTARY-REJECTION' if surv==0 else f'R33-BR2A-INDEX512-ELEMENTARY-{surv}-SIMULTANEOUS-V4-PLUS-NONELEMENTARY-8-TYPES'),
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q256-simultaneous-v4-census.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':256,'survivors':surv,'rejected':256-surv,'all_elementary_rejected':surv==0,'cc_class_census':cert['cc_induced_class_count_census'],'ct_class_census':cert['ct_induced_class_count_census'],'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
