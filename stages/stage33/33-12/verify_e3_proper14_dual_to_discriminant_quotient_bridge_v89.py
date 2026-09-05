#!/usr/bin/env python3
"""Exact replay for Stage33 V89 proper14-dual -> discriminant quotient bridge."""
import hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent; S=H.parent
CERT=H/"e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"
EC="26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639"
locks={
 S/"33-07"/"picard-discriminant-compact.json":("a6c2174968d068fa1076e683fe80c8ea4393fcf1","4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"),
 S/"33-07"/"proper-brauer2-from-discriminant.json":("c8f12e5f2b0ac9c07f1866406cea331d7f41f278","c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"),
 H/"e3-proper14-boundary-basis-definitions-v45.json":("5f3a0ac3091ff6204d927a0dee24e1207f965d5e","a1dafa0be79c80d7275cd2629278bf6a56d6e592f90738316e71ca2689f9feb5"),
 H/"e3-direct-cech-seed-contract-v88.json":("8e94550bd1a14a68b053100fa3787c83b563aee1","1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7"),
}
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def canon(o):
 x=dict(o); h=x.pop("canonical_sha256")
 assert h==hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
 return h
def load(p):
 o=json.loads(p.read_text()); b,c=locks[p]; assert blob(p)==b and canon(o)==c; return o
def rank(a):
 a=[r[:] for r in a]; r=0
 for c in range(len(a[0])):
  q=next((i for i in range(r,len(a)) if a[i][c]),None)
  if q is None: continue
  a[r],a[q]=a[q],a[r]
  for i in range(len(a)):
   if i!=r and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[r])]
  r+=1
 return r
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b)))&1 for j in range(len(b[0]))] for i in range(len(a))]
def rm(v,m): return [sum(v[i]*m[i][j] for i in range(len(v)))&1 for j in range(len(m[0]))]
def tr(a): return [list(r) for r in zip(*a)]
def r2(M,mods):
 sc=[m//2 for m in mods]; out=[]
 for i in range(14):
  row=[]
  for j in range(14):
   n=sc[i]*M[i][j]; assert n%sc[j]==0; row.append((n//sc[j])&1)
  out.append(row)
 return out

disc=load(S/"33-07"/"picard-discriminant-compact.json")
br=load(S/"33-07"/"proper-brauer2-from-discriminant.json")
v45=load(H/"e3-proper14-boundary-basis-definitions-v45.json")
v88=load(H/"e3-direct-cech-seed-contract-v88.json")
assert blob(S/"33-07"/"certify_proper_brauer2_from_discriminant.py")=="23fe426ab0a43b7cacc6923c92cd93367906e2fd"
c=json.loads(CERT.read_text()); assert canon(c)==EC
assert c["schema"]=="stage33.e3.proper14_dual_to_discriminant_quotient_bridge.v89"

mods=disc["discriminant_moduli"]; assert mods==[2]*4+[4]*6+[8]*4
B8=disc["discriminant_bilinear_numerator_over_8_reduced"]
P=[]
for i in range(14):
 row=[]
 for j in range(14):
  n=B8[i][j]*(mods[j]//2); assert n%4==0; row.append((n//4)&1)
 P.append(row)
assert rank(P)==14==c["dual_pairing_bridge"]["rank_f2"]

Acc=r2(disc["cc_action_mixed_moduli"],mods); Act=r2(disc["ct_action_mixed_moduli"],mods)
assert Acc==br["A_T_two_torsion_cc_action_f2"] and Act==br["A_T_two_torsion_ct_action_f2"]
Bcc,Bct=tr(Acc),tr(Act)
assert Bcc==br["proper_Br2_cc_action_f2"] and Bct==br["proper_Br2_ct_action_f2"]
Qcc=[[x&1 for x in r] for r in disc["cc_action_mixed_moduli"]]
Qct=[[x&1 for x in r] for r in disc["ct_action_mixed_moduli"]]
assert mm(Qcc,P)==mm(P,Bcc) and mm(Qct,P)==mm(P,Bct)

target=[0,0,1,0,1,0,0,0,0,0,0,0,0,0]
w=[1,0,0,0,0,0,0,1,0,1,0,0,0,0]
assert v45["e3_context"]["proper14_mask_decimal"]==20
assert v45["non_identification_lock"]["positional_identification_allowed"] is False
assert v88["bounded_negative_findings"]["proper14_axis_labels_3_and_5_supply_literal_geometry"] is False
assert c["e3_transport"]["proper14_coordinate_f2"]==target and rm(w,P)==target
assert c["e3_transport"]["retained_at_mod2_quotient_coordinate_f2"]==w
assert c["e3_transport"]["retained_at_mod2_quotient_support_one_based"]==[1,8,10]
assert c["e3_transport"]["solution_unique"] is True

e=c["exact_consequence"]; assert e["dual_coordinate_to_discriminant_quotient_bridge_materialized"] is True
for k in ("literal_picard_divisor_materialized","literal_kummer_function_materialized","literal_cech_seed_materialized","complete_residue_audit_materialized","genuine_full_surface_h2_mu2_lift_for_e3"): assert e[k] is False
f=c["credit_firewall"]; assert f["stage33_progress"]=="6/11"
for k in ("stage33_12_closed_exact","stage33_13_released","receiver_credit","theorem_credit","endpoint_credit","merge_allowed"): assert f[k] is False
assert c["next_exact_leaf"]=="V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"
print("V89_E3_PROPER14_DUAL_TO_DISCRIMINANT_QUOTIENT_BRIDGE=PASS_EXACT")
print("RETAINED_AT_MOD2_SUPPORT_ONE_BASED=1,8,10")
print("CERTIFICATE_SHA256="+EC)
