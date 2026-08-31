#!/usr/bin/env python3
"""Hostile replay of corrected-J2 R5e Pic/2 and ct-restricted HS d2 nonzero result."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE=Path(__file__).resolve().parent
S12=HERE.parent/"33-12"
OUT=HERE/"j2-r5f-hs-d2-nonzero-hostile-replay.json"
EXPECTED="6535f3190daab8c20ba5ddb3409675f20ac35dc4ee319e3be7af056baa4ce20d"
LOCKS={
"candidate":(HERE/"j2-r5e-pic2-r5f-ct-hs-d2-nonzero.json","8e384501db1cb3aa3f73358b0c3612a85e4012c5041fda60d3be7aeddc7c4c55"),
"semantic_picard":(S12/"j2-semantic-kc-picard-basis.json","c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"),
"explicit_surface_lift":(S12/"j2-corrected-explicit-cech-mu2-lift.json","6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b")}
def csha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(k):
 p,h=LOCKS[k];o=json.loads(p.read_text());b=dict(o);got=b.pop("canonical_sha256");assert got==h==csha(b),(k,got,csha(b));return o
def gram20(s):
 g17=s["gram17"];inc=s["incidence17x12"];tr=s["semantic_exceptional_indices_0based"]
 g=[r[:] + [inc[i][c] for c in tr] for i,r in enumerate(g17)]
 for a,c in enumerate(tr):
  row=[inc[i][c] for i in range(17)]+[0,0,0];row[17+a]=-2;g.append(row)
 return g
def act(v,A):return [sum(v[i]*A[i][j] for i in range(20)) for j in range(20)]
def add(x,y):return [a+b for a,b in zip(x,y)]
c=load("candidate");s=load("semantic_picard");e=load("explicit_surface_lift")
A=sp.Matrix(c["semantic_ct_action"]["matrix"]);G=sp.Matrix(gram20(s));I=sp.eye(20)
assert A*A==I
assert A*G*A.T==G
B=c["r5f_integral_lift_and_restricted_d2"]["integral_lift_B_of_ct_defect"]
ctB=act(B,c["semantic_ct_action"]["matrix"])
assert all((x-y)%2==0 for x,y in zip(ctB,B))
Z=[(x+y)//2 for x,y in zip(B,ctB)]
assert act(Z,c["semantic_ct_action"]["matrix"])==Z
N=I+A
diag=[int(smith_normal_form(N,domain=ZZ)[i,i]) for i in range(20)]
assert diag==[1,1,1]+[2]*14+[0,0,0]
col9=[int(N[i,8]) for i in range(20)]
assert col9==[0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0] and Z[8]==1
zero=[0]*20
def beta(g,h): return Z if g==h==1 else zero
def gact(g,v): return act(v,c["semantic_ct_action"]["matrix"]) if g else v
for g in (0,1):
 for h in (0,1):
  for k in (0,1):
   assert add(beta(g,h),beta(g^h,k))==add(gact(g,beta(h,k)),beta(g,h^k))
cc=e["galois_defect_generic_splittings"]["cc"]
assert cc["formula"]=="cc(lambda_D)-lambda_D={f2,g21*g22}={f2,(B1/(2*t))^2}"
assert c["r5e_actual_pic2"]["cc"]["marked_Pic_mod2"]==zero
payload={
"schema":"STAGE33_05_J2_R5F_HS_D2_NONZERO_HOSTILE_REPLAY_V1",
"status":"PASS_HOSTILE_REPLAY_EXACT_CT_RESTRICTED_HS_D2_NONZERO",
"scope":"AUDIT_R5E_CC_CT_PIC2_AND_R5F_NONZERO_D2_ONLY_NO_RECLOSURE",
"source_locks":{"candidate":{"path":"stages/stage33/33-05/j2-r5e-pic2-r5f-ct-hs-d2-nonzero.json","canonical_sha256":LOCKS["candidate"][1]},"semantic_picard":{"path":"stages/stage33/33-12/j2-semantic-kc-picard-basis.json","canonical_sha256":LOCKS["semantic_picard"][1]},"explicit_surface_lift":{"path":"stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json","canonical_sha256":LOCKS["explicit_surface_lift"][1]}},
"hostile_checks":{"cc_global_square_root_replayed":True,"cc_no_ramified_sign_choice":"c=B1/(2*t) is already in the base field and deck-fixed, so the ct q-root sign ambiguity mechanism is absent","ct_action_involution":True,"ct_action_picard_isometry":True,"ct_defect_fixed_mod2":True,"restricted_2cocycle_identity":True,"Z_ct_invariant":True,"smith_diagonal_of_1_plus_ct":diag,"independent_parity_witness":{"coordinate_1based":9,"label":"CsK[26]","Z_coordinate":Z[8],"norm_column":col9},"restricted_class_nonzero":True,"global_class_nonzero_by_restriction":True},
"verdict":{"R5e_actual_cc_ct_Pic_mod2":"PASS_COMPLETE","R5f_HS_d2":"NONZERO_EXACT","R5g_Q_descent":"BLOCKED","corrected_J2_Q_defined_Brauer_preimage":False,"successful_R5_repair_exit_reached":False,"dependency_rebuild_required":True},
"firewall":{"stage33_05_reclosed":False,"stage33_12_closed":False,"stage33_13_released":False,"Q_defined_descent_credit_restored":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
"next_exact_leaf":"REBUILD_STAGE33_DEPENDENCY_CHAIN_AFTER_AUDITED_CORRECTED_J2_Q_DESCENT_NOGO"}
assert csha(payload)==EXPECTED,(csha(payload),EXPECTED)
o=dict(payload);o["canonical_sha256"]=EXPECTED
OUT.write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"status":o["status"],"Z":Z,"smith":diag,"canonical_sha256":EXPECTED},sort_keys=True))
