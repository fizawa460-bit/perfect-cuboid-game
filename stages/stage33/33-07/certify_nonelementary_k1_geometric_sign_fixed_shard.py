#!/usr/bin/env python3
"""Exact subshard of the k=1 endpoint-group-type plus seven-sign census."""
import hashlib,json,os
from collections import Counter
from pathlib import Path
from nonelementary_k1_geometric_sign_fixed_common import *
from nonelementary_k1_endpoint_group_type import TARGET_POWER_LOG2,classify_endpoint_group_type
HERE=Path(__file__).resolve().parent
pidx=int(os.environ.get('P_ORBIT_INDEX','0'));sidx=int(os.environ.get('RECORD_SHARD_INDEX','0'));scount=int(os.environ.get('RECORD_SHARD_COUNT','16'))
if not 0<=pidx<15 or not 0<=sidx<scount:raise SystemExit('invalid shard coordinates')
ENDPOINT_RUN=32934384807;ENDPOINT_LOCK='9f9dec186d3401d75f4aad4e7e4b819529362880091f0070548cb2bf3b13fbf3'
def rehash(doc):
 d=dict(doc);stored=d.pop('canonical_sha256',None);got=hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest();return stored,got
support_path=HERE/f'nonelementary-k1-geometric-support-orbit-shard-{pidx}.json';support=json.loads(support_path.read_text());stored,got=rehash(support)
if stored!=got or support.get('schema')!='STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_ORBIT_SHARD_V1':raise SystemExit('support shard hash/schema regression')
if support.get('p_orbit_index')!=pidx or support.get('arithmetic_generators_used')!=[] or not support.get('all_fixed_P_support_skeletons_partitioned_exactly'):raise SystemExit('support shard provenance/exactness regression')
if support.get('weighted_structural_H_covered')!=64*support.get('full_pair_skeletons_covered'):raise SystemExit('support weighted-H regression')
reps=support['orbit_representatives']
if len(reps)!=support['fixed_P_W_orbit_count']:raise SystemExit('support representative count regression')
endpoint=json.loads((HERE/'endpoint-coordinate-sign-discriminant-actions-split.json').read_text());es,eg=rehash(endpoint)
if es!=eg or es!=ENDPOINT_LOCK or endpoint.get('discriminant_moduli')!=TARGET_MODS:raise SystemExit('endpoint sign source regression')
if not endpoint.get('all_actions_well_defined_involutions_and_q_isometries') or not endpoint.get('seven_sign_involutions_commute') or not endpoint.get('seven_sign_product_identity'):raise SystemExit('endpoint sign action regression')
actions=endpoint.get('sign_actions_mixed_moduli',[])
if len(actions)!=7:raise SystemExit('endpoint sign count regression')
target=[(fixed_log2_from_action(A,TARGET_MODS,2),fixed_log2_from_action(A,TARGET_MODS,4)) for A in actions]
if target!=[(12,14)]*7 or TARGET_POWER_LOG2!={2:14,4:24,8:28}:raise SystemExit('endpoint target regression')
owned=[(i,r) for i,r in enumerate(reps) if i%scount==sidx];reject=Counter();survivors=[];owned_pair=0;stable_records=0;unstable_records=0;group_match=0
checks=[]
for piece in range(7):checks.extend(((piece,4,14),(piece,2,12)))
checks=[(0,4,14),(0,2,12)]+[x for x in checks if x[0]!=0]
for ridx,record in owned:
 if len(record.get('P_basis_bits',[]))!=1 or len(record.get('W_basis_bits',[]))!=8 or int(record.get('lift_section_fibre_size',0))!=64:raise SystemExit('owned record k1 shape regression')
 mult=int(record['pair_orbit_size']);owned_pair+=mult
 if mult<=0:raise SystemExit('owned pair orbit size regression')
 if not all_sections_stable_under_signs(record):unstable_records+=1;reject['H_STABILITY']+=64;continue
 stable_records+=1
 for solution in range(64):
  H=reconstruct_H(record,solution);verify_isotropic_H(H);group_ok,group_reason,_=classify_endpoint_group_type(H)
  if not group_ok:reject[group_reason]+=1;continue
  group_match+=1;status=None
  for piece,power,want in checks:
   gotlog=fixed_Qpower_log2_direct(H,piece,power)
   if gotlog!=want:status=f'S{piece}_Q{power}';reject[status]+=1;break
  if status is None:survivors.append({'record_index':ridx,'solution':solution,'pair_orbit_size':mult})
checked=64*len(owned);weighted_checked=64*owned_pair;surv=len(survivors);weighted_surv=sum(int(x['pair_orbit_size']) for x in survivors)
if sum(reject.values())+surv!=checked or group_match<surv:raise SystemExit('owned section accounting regression')
cert={'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_SUBSHARD_V1','source_support_sha256':stored,'source_endpoint_workflow_run_id':ENDPOINT_RUN,'source_endpoint_sha256':ENDPOINT_LOCK,'p_orbit_index':pidx,'record_shard_index':sidx,'record_shard_count':scount,'source_fixed_P_W_orbit_count':len(reps),'source_full_pair_skeletons_covered':int(support['full_pair_skeletons_covered']),'source_weighted_structural_H_covered':int(support['weighted_structural_H_covered']),'owned_record_count':len(owned),'owned_pair_skeleton_count':owned_pair,'owned_stable_record_count':stable_records,'owned_unstable_record_count':unstable_records,'representative_lift_sections_checked':checked,'weighted_H_checked':weighted_checked,'endpoint_finite_group_type_matches_before_signs':group_match,'rejection_counts':dict(sorted(reject.items())),'representative_section_survivors':surv,'weighted_H_survivors':weighted_surv,'survivors':survivors,'target_quotient_power_torsion_log2':{str(k):v for k,v in sorted(TARGET_POWER_LOG2.items())},'target_fixed_Q2_log2':[x[0] for x in target],'target_fixed_Q4_log2':[x[1] for x in target],'arithmetic_generators_used':[],'geometric_coordinate_sign_family_enforced':7,'endpoint_finite_group_type_filter_enforced':True,'all_survivors_have_endpoint_finite_group_type':True,'all_owned_lift_sections_decided_exactly_once':True,'all_survivors_pass_Q2_Q4_fixed_filtration_for_all_seven_signs':True,'fast_or_heuristic_traversal_used':False,'full_finite_q_isometry_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-AGGREGATE-K1-PURE-GEOMETRIC-FIXED-FILTRATION','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();out=HERE/f'nonelementary-k1-geometric-sign-fixed-p{pidx}-s{sidx}.json';out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'p_orbit':pidx,'subshard':sidx,'owned_records':len(owned),'checked':checked,'group_type_matches':group_match,'survivors':surv,'weighted_survivors':weighted_surv,'rejections':dict(sorted(reject.items())),'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
