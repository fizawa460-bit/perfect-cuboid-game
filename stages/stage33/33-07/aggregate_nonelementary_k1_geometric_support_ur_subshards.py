#!/usr/bin/env python3
"""Merge balanced (U,R)-orbit subshards into one standard k=1 P shard."""
import hashlib,json,os
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
pidx=int(os.environ.get('P_ORBIT_INDEX','5'))
scount=int(os.environ.get('UR_SHARD_COUNT','32'))
D=HERE/'k1-geometric-support-ur-subshards'
files=sorted(D.glob(f'nonelementary-k1-geometric-support-ur-subshard-p{pidx}-s*.json'))
if len(files)!=scount:raise SystemExit(f'expected {scount} P{pidx} support subshards, got {len(files)}')
seen=set();group_seen=set();locks={};records=[];partition_sha=None;source_sha=None
p=None;p_members=None;p_size=None;p_stab=None;group_total=None;pair_candidate_total=None
fixed_total=pair_total=rep_sections=weighted=selected_pairs=0
for f in files:
    d=json.loads(f.read_text());u=dict(d);s=u.pop('canonical_sha256',None);h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if s!=h:raise SystemExit(f'subshard hash regression {f.name}')
    if d.get('schema')!='STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_UR_SUBSHARD_V1' or d.get('arithmetic_generators_used')!=[]:raise SystemExit('support subshard schema/firewall regression')
    if int(d['p_orbit_index'])!=pidx or int(d['ur_shard_count'])!=scount:raise SystemExit('support subshard coordinate regression')
    si=int(d['ur_shard_index'])
    if not 0<=si<scount or si in seen:raise SystemExit('duplicate support subshard index')
    seen.add(si);locks[str(si)]=s
    partition_sha=partition_sha or d['UR_partition_sha256'];source_sha=source_sha or d['source_2Q_support_sha256']
    if partition_sha!=d['UR_partition_sha256'] or source_sha!=d['source_2Q_support_sha256']:raise SystemExit('support subshard source/partition moved')
    p0=int(d['P_basis_bits'][0]);members=tuple(map(int,d['P_orbit_members']));ps=int(d['P_orbit_size']);st=int(d['P_stabilizer_order'])
    if p is None:p,p_members,p_size,p_stab=p0,members,ps,st
    if (p0,members,ps,st)!=(p,p_members,p_size,p_stab):raise SystemExit('P metadata inconsistent across support subshards')
    group_total=group_total if group_total is not None else int(d['total_UR_orbit_group_count']);pair_candidate_total=pair_candidate_total if pair_candidate_total is not None else int(d['total_candidate_UR_pair_count'])
    if group_total!=int(d['total_UR_orbit_group_count']) or pair_candidate_total!=int(d['total_candidate_UR_pair_count']):raise SystemExit('candidate (U,R) universe moved')
    for gi in map(int,d['selected_UR_orbit_group_indices']):
        if gi in group_seen:raise SystemExit('candidate (U,R) orbit assigned twice')
        group_seen.add(gi)
    selected_pairs+=int(d['selected_candidate_UR_pair_count']);fixed_total+=int(d['fixed_P_support_skeleton_count']);pair_total+=int(d['full_pair_skeletons_covered']);rep_sections+=int(d['representative_lift_sections_for_next_exact_leaf']);weighted+=int(d['weighted_structural_H_covered'])
    if not d.get('all_selected_UR_orbits_exhausted_exactly'):raise SystemExit('support subshard exactness regression')
    records.extend(d['orbit_representatives'])
if seen!=set(range(scount)) or group_seen!=set(range(int(group_total))):raise SystemExit('balanced support group coverage regression')
if selected_pairs!=pair_candidate_total:raise SystemExit('candidate (U,R) pair coverage regression')
keys=[tuple(map(int,r['W_basis_bits'])) for r in records]
if len(keys)!=len(set(keys)):raise SystemExit('duplicate W orbit representative across balanced support subshards')
hist=Counter(int(r['W_orbit_size_under_P_stabilizer']) for r in records)
if sum(int(r['W_orbit_size_under_P_stabilizer']) for r in records)!=fixed_total:raise SystemExit('fixed-P W orbit-size sum regression')
if pair_total!=int(p_size)*fixed_total:raise SystemExit('full pair skeleton count regression')
if rep_sections!=64*len(records) or weighted!=64*pair_total:raise SystemExit('support lift/weight regression')
if int(p_size)*int(p_stab)!=288:raise SystemExit('P orbit-stabilizer regression')
records.sort(key=lambda r:r['W_basis_bits'])
cert={'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_ORBIT_SHARD_V1','source_2Q_support_sha256':source_sha,'source_balanced_subshard_sha256':locks,'balanced_UR_partition_sha256':partition_sha,'balanced_UR_subshard_count':scount,'arithmetic_generators_used':[],'firewall':'NO_ARITHMETIC_CC_CT_USED__SOURCE_COORDINATE_SYMMETRY_ONLY','p_orbit_index':pidx,'P_basis_bits':[p],'P_orbit_size':p_size,'P_stabilizer_order':p_stab,'P_orbit_members':list(p_members),'fixed_P_support_skeleton_count':fixed_total,'fixed_P_W_orbit_count':len(records),'fixed_P_W_orbit_size_histogram':{str(k):v for k,v in sorted(hist.items())},'full_pair_skeletons_covered':pair_total,'representative_lift_sections_for_next_exact_leaf':rep_sections,'weighted_structural_H_covered':weighted,'orbit_representatives':records,'all_fixed_P_support_skeletons_partitioned_exactly':True,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-K1-PURE-GEOMETRIC-FIXED-FILTRATION-ON-SOURCE-ORBIT-REPRESENTATIVES','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();out=HERE/f'nonelementary-k1-geometric-support-orbit-shard-{pidx}.json';out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'p_orbit_index':pidx,'subshards':scount,'candidate_pairs':pair_candidate_total,'fixed_P_skeletons':fixed_total,'W_orbits':len(records),'full_pair_skeletons':pair_total,'representative_sections_next':rep_sections,'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
