#!/usr/bin/env python3
"""Aggregate the exact k=1 seven-geometric-sign fixed-filtration census."""
import hashlib,json,os
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
SHARDS=HERE/'k1-geometric-sign-fixed-shards'
P_COUNT=15
S_COUNT=int(os.environ.get('RECORD_SHARD_COUNT','16'))
EXPECTED_PAIR=20487593
EXPECTED_WEIGHTED=1311205952
ENDPOINT_LOCK='9f9dec186d3401d75f4aad4e7e4b819529362880091f0070548cb2bf3b13fbf3'

def rehash(doc):
    d=dict(doc);stored=d.pop('canonical_sha256',None)
    got=hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return stored,got

seen=set();source_by_p={};reject=Counter();survivors=[]
total_records=total_pairs=checked=weighted_checked=surv=weighted_surv=0
stable_records=unstable_records=0
for p in range(P_COUNT):
    p_records=p_pairs=p_checked=p_weighted=0
    for s in range(S_COUNT):
        path=SHARDS/f'nonelementary-k1-geometric-sign-fixed-p{p}-s{s}.json'
        if not path.exists():raise SystemExit(f'missing exact subshard p{p} s{s}')
        x=json.loads(path.read_text());stored,got=rehash(x)
        if stored!=got:raise SystemExit(f'subshard hash regression p{p} s{s}')
        if x.get('schema')!='STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_SUBSHARD_V1':raise SystemExit('subshard schema regression')
        key=(int(x['p_orbit_index']),int(x['record_shard_index']))
        if key!=(p,s) or key in seen:raise SystemExit(f'subshard coordinate regression {key}')
        seen.add(key)
        if int(x['record_shard_count'])!=S_COUNT:raise SystemExit('subshard count regression')
        if x.get('source_endpoint_sha256')!=ENDPOINT_LOCK or x.get('arithmetic_generators_used')!=[]:raise SystemExit('subshard provenance regression')
        if int(x.get('geometric_coordinate_sign_family_enforced',0))!=7:raise SystemExit('seven-sign firewall regression')
        if not x.get('all_owned_lift_sections_decided_exactly_once') or x.get('fast_or_heuristic_traversal_used'):raise SystemExit('subshard exactness regression')
        meta=(x['source_support_sha256'],int(x['source_support_workflow_run_id']),int(x['source_fixed_P_W_orbit_count']),int(x['source_full_pair_skeletons_covered']),int(x['source_weighted_structural_H_covered']))
        if p in source_by_p and source_by_p[p]!=meta:raise SystemExit(f'source metadata moved within P orbit {p}')
        source_by_p[p]=meta
        n=int(x['owned_record_count']);pairs=int(x['owned_pair_skeleton_count']);c=int(x['representative_lift_sections_checked']);wc=int(x['weighted_H_checked'])
        if c!=64*n or wc!=64*pairs:raise SystemExit('owned coverage arithmetic regression')
        r=int(x['representative_section_survivors']);wr=int(x['weighted_H_survivors'])
        if sum(map(int,x['rejection_counts'].values()))+r!=c:raise SystemExit('subshard rejection accounting regression')
        p_records+=n;p_pairs+=pairs;p_checked+=c;p_weighted+=wc
        total_records+=n;total_pairs+=pairs;checked+=c;weighted_checked+=wc;surv+=r;weighted_surv+=wr
        stable_records+=int(x['owned_stable_record_count']);unstable_records+=int(x['owned_unstable_record_count'])
        reject.update({k:int(v) for k,v in x['rejection_counts'].items()})
        for z in x.get('survivors',[]):survivors.append({'p_orbit_index':p,**z})
    _,_,src_records,src_pairs,src_weighted=source_by_p[p]
    if p_records!=src_records or p_pairs!=src_pairs:raise SystemExit(f'P-orbit exact coverage regression {p}')
    if p_checked!=64*src_records or p_weighted!=src_weighted or src_weighted!=64*src_pairs:raise SystemExit(f'P-orbit weighted coverage regression {p}')

if seen!={(p,s) for p in range(P_COUNT) for s in range(S_COUNT)}:raise SystemExit('global subshard coverage regression')
if total_pairs!=EXPECTED_PAIR or weighted_checked!=EXPECTED_WEIGHTED or weighted_checked!=64*total_pairs:raise SystemExit('global predecessor coverage regression')
if total_records!=stable_records+unstable_records or checked!=64*total_records:raise SystemExit('global representative coverage regression')
if sum(reject.values())+surv!=checked:raise SystemExit('global rejection accounting regression')
if weighted_surv!=sum(int(z['pair_orbit_size']) for z in survivors) or len(survivors)!=surv:raise SystemExit('survivor payload accounting regression')

rejected=(surv==0)
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_CENSUS_V1',
 'source_support_workflow_runs':[32965326642,32968214956],'source_endpoint_workflow_run_id':32934384807,'source_endpoint_sha256':ENDPOINT_LOCK,
 'p_orbit_count':P_COUNT,'record_subshards_per_p_orbit':S_COUNT,'exact_support_skeleton_orbit_count':total_records,
 'support_skeleton_count':total_pairs,'representative_lift_sections_checked':checked,'weighted_H_checked':weighted_checked,
 'stable_support_orbit_count':stable_records,'unstable_support_orbit_count':unstable_records,
 'rejection_counts':dict(sorted(reject.items())),'representative_section_survivors':surv,'weighted_H_survivors':weighted_surv,'survivors':survivors,
 'arithmetic_generators_used':[],'geometric_coordinate_sign_family_enforced':7,
 'all_support_orbits_and_all_64_lifts_checked_exactly_once':True,'full_geometric_sign_Q2_Q4_fixed_filtration_census_certified':True,
 'k1_nonelementary_type_rejected':rejected,'full_finite_q_isometry_certified':False,'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,
 'next_exact_leaf':('L33-07-INTEGRATE-ACCEPTED-NONELEMENTARY-K1-K2-K3-REJECTIONS-WITH-INDEX512-GLUE-BRANCH' if rejected else 'L33-07-K1-FULL-FINITE-Q-PLUS-SEVEN-GEOMETRIC-SIGNS-ON-FIXED-FILTRATION-SURVIVORS'),
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k1-geometric-sign-fixed-census.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'support_orbits':total_records,'sections_checked':checked,'survivors':surv,'weighted_survivors':weighted_surv,'k1_rejected':rejected,'rejections':dict(sorted(reject.items())),'sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
