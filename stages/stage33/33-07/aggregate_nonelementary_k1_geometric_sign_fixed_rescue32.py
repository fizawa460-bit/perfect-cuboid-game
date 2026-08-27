#!/usr/bin/env python3
"""Aggregate the exact 15x32 rescue census without weakening the Stage33 firewall."""
import hashlib,json
from collections import Counter,defaultdict
from pathlib import Path
HERE=Path(__file__).resolve().parent
D=HERE/'k1-geometric-sign-fixed-rescue32-subshards'
files=sorted(D.glob('nonelementary-k1-geometric-sign-fixed-p*-s*.json'))
if len(files)!=480: raise SystemExit(f'expected 480 rescue32 subshards, got {len(files)}')
seen=set(); rej=Counter(); checked=weighted=surv=wsurv=group_match=0; support_locks={}; endpoint_lock=None
perp=defaultdict(lambda:{'subshards':0,'owned_records':0,'owned_pairs':0,'checked':0,'weighted':0,'survivors':0,'weighted_survivors':0})
for f in files:
 d=json.loads(f.read_text()); u=dict(d); s=u.pop('canonical_sha256',None); h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if s!=h or d.get('schema')!='STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_SUBSHARD_V1' or d.get('arithmetic_generators_used')!=[]: raise SystemExit(f'subshard hash/schema/firewall regression {f.name}')
 p=int(d['p_orbit_index']); q=int(d['record_shard_index']); n=int(d['record_shard_count'])
 if n!=32 or not(0<=p<15 and 0<=q<32) or (p,q) in seen: raise SystemExit('rescue32 identity regression')
 seen.add((p,q)); support_locks.setdefault(str(p),d['source_support_sha256'])
 if support_locks[str(p)]!=d['source_support_sha256']: raise SystemExit('support lock inconsistent within P orbit')
 endpoint_lock=endpoint_lock or d['source_endpoint_sha256']
 if endpoint_lock!=d['source_endpoint_sha256'] or d.get('target_fixed_Q2_log2')!=[12]*7 or d.get('target_fixed_Q4_log2')!=[14]*7: raise SystemExit('endpoint filtration regression')
 if d.get('target_quotient_power_torsion_log2')!={'2':14,'4':24,'8':28} or not d.get('endpoint_finite_group_type_filter_enforced') or not d.get('all_survivors_have_endpoint_finite_group_type'): raise SystemExit('endpoint finite-group-type regression')
 if not d.get('all_owned_lift_sections_decided_exactly_once') or d.get('fast_or_heuristic_traversal_used'): raise SystemExit('rescue32 exactness regression')
 checked+=int(d['representative_lift_sections_checked']); weighted+=int(d['weighted_H_checked']); surv+=int(d['representative_section_survivors']); wsurv+=int(d['weighted_H_survivors']); group_match+=int(d['endpoint_finite_group_type_matches_before_signs']); rej.update({k:int(v) for k,v in d['rejection_counts'].items()})
 z=perp[p]; z['subshards']+=1; z['owned_records']+=int(d['owned_record_count']); z['owned_pairs']+=int(d['owned_pair_skeleton_count']); z['checked']+=int(d['representative_lift_sections_checked']); z['weighted']+=int(d['weighted_H_checked']); z['survivors']+=int(d['representative_section_survivors']); z['weighted_survivors']+=int(d['weighted_H_survivors']); z.setdefault('source_records',int(d['source_fixed_P_W_orbit_count'])); z.setdefault('source_pairs',int(d['source_full_pair_skeletons_covered'])); z.setdefault('source_weighted',int(d['source_weighted_structural_H_covered']))
 if (z['source_records'],z['source_pairs'],z['source_weighted'])!=(int(d['source_fixed_P_W_orbit_count']),int(d['source_full_pair_skeletons_covered']),int(d['source_weighted_structural_H_covered'])): raise SystemExit('source P metadata inconsistent')
if seen!={(p,q) for p in range(15) for q in range(32)}: raise SystemExit('rescue32 coverage regression')
support_orbits=pair_total=source_weighted_total=0
for p in range(15):
 z=perp[p]
 if z['subshards']!=32 or z['owned_records']!=z['source_records'] or z['owned_pairs']!=z['source_pairs']: raise SystemExit(f'P{p} record/pair partition regression {z}')
 if z['checked']!=64*z['source_records'] or z['weighted']!=z['source_weighted'] or z['source_weighted']!=64*z['source_pairs']: raise SystemExit(f'P{p} section/weight regression')
 support_orbits+=z['source_records']; pair_total+=z['source_pairs']; source_weighted_total+=z['source_weighted']
if pair_total!=20487593 or source_weighted_total!=1311205952: raise SystemExit(f'global predecessor coverage regression {(pair_total,source_weighted_total)}')
if checked!=64*support_orbits or weighted!=source_weighted_total or sum(rej.values())+surv!=checked or group_match<surv: raise SystemExit('global exact accounting regression')
zero=(surv==0 and wsurv==0); group_rejections=sum(v for k,v in rej.items() if k.startswith('GROUP_TYPE_')); sign_only_zero=zero and group_rejections==0
cert={'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_CENSUS_V1','rescue_partition_count':32,'source_support_shard_sha256':support_locks,'source_endpoint_sha256':endpoint_lock,'arithmetic_generators_used':[],'geometric_coordinate_sign_family_enforced':7,'eligible_rank_one_E7_P_count':63,'exact_P_orbit_count':15,'support_skeleton_count':pair_total,'exact_support_skeleton_orbit_count':support_orbits,'representative_lift_sections_checked':checked,'weighted_H_checked':weighted,'endpoint_finite_group_type_matches_before_signs':group_match,'target_quotient_power_torsion_log2':{'2':14,'4':24,'8':28},'endpoint_finite_group_type_filter_certified':True,'rejection_counts':dict(sorted(rej.items())),'finite_group_type_rejection_count':group_rejections,'representative_section_survivors':surv,'weighted_H_survivors':wsurv,'all_15x32_rescue_subshards_present_exactly_once':True,'all_support_orbit_representative_lifts_checked_exactly_once':True,'all_1311205952_weighted_structural_H_covered_exactly':weighted==1311205952,'full_affine_fixed_filtration_census_certified':True,'all_survivors_have_endpoint_finite_group_type':True,'k1_nonelementary_type_rejected_by_geometric_sign_fixed_filtration_alone':sign_only_zero,'k1_nonelementary_type_rejected_by_endpoint_group_type_or_geometric_sign_fixed_filtration':zero,'k1_nonelementary_type_rejected':zero,'full_finite_q_isometry_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':('L33-07-INTEGRATE-K1-K2-K3-GEOMETRIC-REJECTIONS-WITH-INDEX512-GLUE-BRIDGE' if zero else 'L33-07-FULL-FINITE-Q-PLUS-SEVEN-SIGN-CONJUGACY-ON-K1-SURVIVORS'),'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest(); (HERE/'nonelementary-k1-geometric-sign-fixed-rescue32-census.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'partition_count':32,'representative_sections_checked':checked,'weighted_H_checked':weighted,'survivors':surv,'weighted_survivors':wsurv,'k1_rejected':zero,'sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
