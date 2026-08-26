#!/usr/bin/env python3
"""Exact one-P-orbit shard of the pure-geometric k=1 support census."""
import hashlib,json,os
from collections import Counter
from pathlib import Path
from nonelementary_k1_geometric_support_orbit_common import *
HERE=Path(__file__).resolve().parent
idx=int(os.environ.get('P_ORBIT_INDEX','0'))
if not 0<=idx<len(P_ORBITS):raise SystemExit('invalid P orbit index')
p,p_orbit,stab=P_ORBITS[idx]
Ws=enumerate_W_for_P(p)
unseen=set(Ws);records=[];hist=Counter();fixed_P_total=0
while unseen:
    seed=min(unseen);orb={canon(transport(v,g) for v in seed) for g in stab}
    if not orb<=Ws:raise SystemExit('fixed-P W universe not stabilizer-stable')
    unseen.difference_update(orb);rep=min(orb);wsz=len(orb);pair_size=len(p_orbit)*wsz
    pair_stab=sum(1 for g in SYM if transport(p,g)==p and canon(transport(v,g) for v in rep)==rep)
    if pair_size*pair_stab!=288:raise SystemExit('pair orbit-stabilizer regression')
    hist[wsz]+=1;fixed_P_total+=wsz
    records.append({'P_basis_bits':[p],'W_basis_bits':list(rep),'P_orbit_size':len(p_orbit),'P_stabilizer_order':len(stab),'W_orbit_size_under_P_stabilizer':wsz,'pair_orbit_size':pair_size,'lift_section_fibre_size':64})
records.sort(key=lambda r:r['W_basis_bits'])
if fixed_P_total!=len(Ws):raise SystemExit('fixed-P orbit coverage regression')
cert={'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_ORBIT_SHARD_V1','source_2Q_support_sha256':twoq['canonical_sha256'],'arithmetic_generators_used':[],'firewall':'NO_ARITHMETIC_CC_CT_USED__SOURCE_COORDINATE_SYMMETRY_ONLY','p_orbit_index':idx,'P_basis_bits':[p],'P_orbit_size':len(p_orbit),'P_stabilizer_order':len(stab),'P_orbit_members':list(p_orbit),'fixed_P_support_skeleton_count':len(Ws),'fixed_P_W_orbit_count':len(records),'fixed_P_W_orbit_size_histogram':{str(k):v for k,v in sorted(hist.items())},'full_pair_skeletons_covered':sum(r['pair_orbit_size'] for r in records),'representative_lift_sections_for_next_exact_leaf':64*len(records),'weighted_structural_H_covered':64*sum(r['pair_orbit_size'] for r in records),'orbit_representatives':records,'all_fixed_P_support_skeletons_partitioned_exactly':True,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-K1-PURE-GEOMETRIC-FIXED-FILTRATION-ON-SOURCE-ORBIT-REPRESENTATIVES','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();out=HERE/f'nonelementary-k1-geometric-support-orbit-shard-{idx}.json';out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'p_orbit_index':idx,'p_orbit_size':len(p_orbit),'fixed_P_skeletons':len(Ws),'W_orbits':len(records),'full_pair_skeletons':cert['full_pair_skeletons_covered'],'representative_sections_next':cert['representative_lift_sections_for_next_exact_leaf'],'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
