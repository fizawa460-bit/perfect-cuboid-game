#!/usr/bin/env python3
"""Exhaust one shard of all k=2 Q2-affine sections by geometric-sign fixed filtration."""
import hashlib,json,os
from collections import Counter
from pathlib import Path
from nonelementary_k2_geometric_sign_fixed_common import *
HERE=Path(__file__).resolve().parent
MAN=HERE/'nonelementary-k2-geometric-sign-fixed-manifest.json'
MLOCK=os.environ.get('MANIFEST_SHA256','')
shard=int(os.environ.get('SHARD_INDEX','0'));nshard=int(os.environ.get('SHARD_COUNT','64'))
if nshard<=0 or not(0<=shard<nshard):raise SystemExit('invalid shard')
d=json.loads(MAN.read_text());u=dict(d);s=u.pop('canonical_sha256',None);h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
if s!=h or (MLOCK and s!=MLOCK):raise SystemExit('manifest hash regression')
if d.get('schema')!='STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_SIGN_FIXED_MANIFEST_V1' or d.get('arithmetic_generators_used')!=[]:raise SystemExit('manifest firewall/schema regression')
if d.get('endpoint_fixed_Q2_log2_by_sign')!=[12]*7 or d.get('endpoint_fixed_Q4_log2_by_sign')!=[14]*7:raise SystemExit('endpoint filtration regression')
checked=weighted_checked=surv=weighted_surv=0;rej=Counter();first=[];per=[]
for r in d['records']:
 rr=tuple(map(int,r['Q2_survivor_affine_rref_augmented']));free=free_variables(rr);dim=int(r['Q2_survivor_affine_dimension']);total=1<<dim
 if len(free)!=dim or total!=int(r['representative_section_count']):raise SystemExit('family affine count regression')
 order=[int(r['preferred_first_sign_index'])]+[i for i in range(7) if i!=int(r['preferred_first_sign_index'])]
 local_checked=local_surv=0;local_rej=Counter()
 for fm in range(shard,total,nshard):
  sol=solution_from_free(rr,free,fm);Hrows=reconstruct_H(r,sol);verify_isotropic_H(Hrows);local_checked+=1;checked+=1
  reason=None
  for si in order:
   if fixed_Qpower_log2_direct(Hrows,si,2)!=12:reason='Q2';break
   if fixed_Qpower_log2_direct(Hrows,si,4)!=14:reason='Q4';break
  if reason is None:
   local_surv+=1;surv+=1
   if len(first)<12:first.append({'orbit_index':int(r['orbit_index']),'free_mask':int(fm)})
  else:
   rej[reason]+=1;local_rej[reason]+=1
 osz=int(r['orbit_size']);weighted_checked+=osz*local_checked;weighted_surv+=osz*local_surv
 per.append({'orbit_index':int(r['orbit_index']),'assignments_checked':local_checked,'survivors':local_surv,'rejection_layers':dict(sorted(local_rej.items()))})
expected=sum((int(r['representative_section_count'])+nshard-1-shard)//nshard for r in d['records'])
if checked!=expected:raise SystemExit(f'shard coverage regression {checked} {expected}')
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_SIGN_FIXED_SHARD_V1','manifest_sha256':s,
 'arithmetic_generators_used':[],'geometric_coordinate_signs_used':7,
 'fixed_filtration_test':'for every affine H and every sign require log2|Fix(Q[2])|=12 and log2|Fix(Q[4])|=14, exact necessary invariants of simultaneous endpoint sign conjugacy',
 'shard_index':shard,'shard_count':nshard,'coverage_rule':'free_mask mod shard_count == shard_index independently in every one of 867 affine families',
 'representative_sections_checked':checked,'weighted_H_checked':weighted_checked,
 'representative_section_survivors':surv,'weighted_H_survivors':weighted_surv,'rejection_layers':dict(sorted(rej.items())),'first_survivors':first,'records':per,
 'all_owned_sections_checked_exactly_once':True,'fast_or_heuristic_traversal_used':False,
 'full_affine_fixed_filtration_census_certified':False,'k2_nonelementary_type_rejected':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();out=HERE/f'nonelementary-k2-geometric-sign-fixed-shard-{shard}.json';out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'shard':shard,'checked':checked,'survivors':surv,'rejections':dict(rej),'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
