#!/usr/bin/env python3
"""Aggregate all 15 pure-geometric k=1 P-orbit support shards."""
import hashlib,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
D=HERE/'k1-geometric-support-orbit-shards';files=sorted(D.glob('nonelementary-k1-geometric-support-orbit-shard-*.json'))
if len(files)!=15:raise SystemExit(f'expected 15 shards, got {len(files)}')
seen=set();records=[];p_members=set();pair_total=rep_sections=weighted=0;p_sizes=Counter();w_orbits=0;locks={}
for f in files:
 d=json.loads(f.read_text());u=dict(d);s=u.pop('canonical_sha256',None);h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if s!=h:raise SystemExit(f'shard hash regression {f.name}')
 if d.get('schema')!='STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_ORBIT_SHARD_V1' or d.get('arithmetic_generators_used')!=[]:raise SystemExit('shard firewall/schema regression')
 i=int(d['p_orbit_index'])
 if i in seen:raise SystemExit('duplicate P orbit shard')
 seen.add(i);locks[str(i)]=s;p_members.update(map(int,d['P_orbit_members']));p_sizes[int(d['P_orbit_size'])]+=1
 pair_total+=int(d['full_pair_skeletons_covered']);rep_sections+=int(d['representative_lift_sections_for_next_exact_leaf']);weighted+=int(d['weighted_structural_H_covered']);w_orbits+=int(d['fixed_P_W_orbit_count']);records.extend(d['orbit_representatives'])
if seen!=set(range(15)) or len(p_members)!=63:raise SystemExit('P orbit coverage regression')
if pair_total!=20487593:raise SystemExit(f'k1 support skeleton total regression {pair_total}')
if weighted!=1311205952 or weighted!=pair_total*64:raise SystemExit(f'k1 weighted H regression {weighted}')
if rep_sections!=w_orbits*64:raise SystemExit('representative section reconstruction regression')
cert={'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_ORBITS_V1','source_shard_sha256':locks,'arithmetic_generators_used':[],'firewall':'NO_ARITHMETIC_CC_CT_USED_IN_SHARDS_OR_AGGREGATE','source_integral_coordinate_symmetry_order':288,'eligible_rank_one_E7_P_count':63,'exact_P_orbit_count':15,'P_orbit_size_histogram':{str(k):v for k,v in sorted(p_sizes.items())},'support_skeleton_count':pair_total,'exact_support_skeleton_orbit_count':w_orbits,'representative_lift_sections_for_next_exact_leaf':rep_sections,'lift_section_fibre_size_per_skeleton_orbit_representative':64,'weighted_structural_H_count':weighted,'orbit_representatives':records,'coverage_partition':'15 full-source P orbits; within each representative P, W quotiented by its exact stabilizer; pair orbit size=P orbit size times stabilizer-W orbit size','full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-K1-PURE-GEOMETRIC-FIXED-FILTRATION-ON-SOURCE-ORBIT-REPRESENTATIVES','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();(HERE/'nonelementary-k1-geometric-support-orbits.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'P_orbits':15,'support_skeletons':pair_total,'support_orbits':w_orbits,'representative_sections_next':rep_sections,'weighted_H':weighted,'sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
