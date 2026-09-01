#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
FILES={
 'receipt':(HERE/'qpic-bridge-local-recertification-receipt.json','c6e9466c509699b1ef2c037ad248915673d391f00115032782970667f44e7dd0'),
 'bridge':(S33/'33-07'/'marked-picard-basis-bridge-certified.json','039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92'),
 'smith':(HERE/'j2-semantic-u1-full-surface-smith-source.json','ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec'),
 'proper':(S33/'33-07'/'proper-brauer2-from-discriminant.json','c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'),
 'gap':(HERE/'j2-marked-order4-lift-label-gap.json','4ca10da7ea214258dd57d1e42c2dc7ea7b66ae29c8cfd5b75ecd6a3eb0fd0101'),
 'geo':(HERE/'j2-marked-order4-geometric-sign-indistinguishability.json','6bb409ffff10e3a4e9d05b9a08f0a5c867c660fa71fd7c414b5535ced0242403'),
 'out':(HERE/'j2-actual-swap-mixed-discriminant-descent.json','93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3'),
}

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ahash(x): return hashlib.sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
def load(name):
 p,h=FILES[name]; x=json.loads(p.read_text()); b=dict(x); got=b.pop('canonical_sha256'); assert got==h==csha(b),(name,got,csha(b)); return x

def tr(A): return [list(r) for r in zip(*A)]
def mm(A,B):
 bt=tr(B); return [[sum(int(x)*int(y) for x,y in zip(r,c)) for c in bt] for r in A]
def mod(A,m): return [[int(x)%m for x in r] for r in A]
def vm(v,A): return [sum(int(x)*int(y) for x,y in zip(v,c))%2 for c in tr(A)]
def rank2(A):
 A=[[(int(x)&1) for x in r] for r in A]; m=len(A); n=len(A[0]); q=0
 for c in range(n):
  p=next((i for i in range(q,m) if A[i][c]),None)
  if p is None: continue
  A[q],A[p]=A[p],A[q]
  for i in range(m):
   if i!=q and A[i][c]: A[i]=[x^y for x,y in zip(A[i],A[q])]
  q+=1
 return q

receipt=load('receipt'); bridge=load('bridge'); smith=load('smith'); proper=load('proper'); gap=load('gap'); geo=load('geo'); out=load('out')
assert receipt['status']=='PASS_EXACT_LOCAL_REVERIFY'
assert receipt['certified_bridge']['canonical_sha256']==FILES['bridge'][1]
sc=smith['retained_common_smith_source']; mods=sc['discriminant_moduli']; assert mods==[2]*4+[4]*6+[8]*4
R=sc['vin_nontrivial_rows_mod8_14x64']; C=sc['v_nontrivial_columns_mod8_64x14']; assert len(R)==14 and len(C)==64
sw=bridge['actual_coordinate_swaps_in_historical_magma_picard_basis']

def descend(G):
 M=mod(mm(mm(R,tr(G)),C),8); scales=[m//2 for m in mods]; A=[]; bad=0
 for a in range(14):
  row=[]
  for b in range(14):
   num=scales[a]*M[a][b]
   if num%scales[b]: bad+=1
   row.append((num//scales[b])&1)
  A.append(row)
 return M,A,bad
M12,A12,b12=descend(sw['swap12_action_64x64']); M13,A13,b13=descend(sw['swap13_action_64x64'])
I=[[int(i==j) for j in range(14)] for i in range(14)]
assert b12+b13==0 and rank2(A12)==rank2(A13)==14
assert mod(mm(A12,A12),2)==I and mod(mm(A13,A13),2)==I
assert mod(mm(mm(A12,A13),A12),2)==mod(mm(mm(A13,A12),A13),2)
u1=smith['exact_normalization']['full_surface_A_T_2_coordinates_f2']
assert vm(u1,A12)==u1 and vm(u1,A13)==u1
P12=tr(A12); P13=tr(A13)
assert proper['proper_Br2_cc_action_f2']==tr(proper['A_T_two_torsion_cc_action_f2'])
assert proper['proper_Br2_ct_action_f2']==tr(proper['A_T_two_torsion_ct_action_f2'])
assert ahash(M12)==out['mixed_discriminant_basis']['swap12_mixed_nontrivial_mod8_sha256']
assert ahash(M13)==out['mixed_discriminant_basis']['swap13_mixed_nontrivial_mod8_sha256']
assert ahash(A12)==out['induced_A_T_2_actions_f2']['swap12_sha256']
assert ahash(A13)==out['induced_A_T_2_actions_f2']['swap13_sha256']
assert ahash(P12)==out['proper_Br2_dual_actions_f2']['swap12_sha256']
assert ahash(P13)==out['proper_Br2_dual_actions_f2']['swap13_sha256']
cands={x['retained10_mask_decimal']:x['proper14_f2'] for x in gap['exact_enumeration']['joint_v4_fixed_functionals']}
def image_mask(v,P):
 w=vm(v,P)
 return next((m for m,x in cands.items() if x==w),None)
images={str(m):{'swap12':image_mask(v,P12),'swap13':image_mask(v,P13)} for m,v in cands.items()}
assert images==out['residual_order4_affine_candidate_S3_action']['candidate_images_by_retained10_mask']
fixed=[m for m,v in cands.items() if image_mask(v,P12)==m and image_mask(v,P13)==m]
assert fixed==[6]
assert out['residual_order4_affine_candidate_S3_action']['unique_joint_fixed_proper14_mask_decimal']==25
assert out['exact_consequence']['historical_mask6_reused_as_named_J2_source'] is False
assert out['exact_consequence']['named_J2_order4_lift_S3_invariance_proved'] is False
assert out['exact_consequence']['finite_v4_kummer_standard_columns_materialized']==0
assert out['promotion_firewall']['stage33_progress']=='6/11' and not out['promotion_firewall']['theorem_credit'] and not out['promotion_firewall']['receiver_credit'] and not out['promotion_firewall']['endpoint_credit']
print(json.dumps({'success':True,'certificate_sha256':FILES['out'][1],'unique_joint_fixed_retained10_mask_decimal':6,'named_J2_source_selected':False,'next':out['next_exact_leaf']},sort_keys=True))
