#!/usr/bin/env python3
"""Verify V91C1C A2_02 strict-transform prime refinement and prime-level cc/ct transport."""
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
S11=HERE.parent/"33-11"; S07=HERE.parent/"33-07"
CERT=HERE/"e3-v91c1c-a2-02-strict-transform-prime-refinement.json"
V91C1B=HERE/"e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json"
GALOIS=S07/"galois-known-class-permutations.json"
SMALL=S11/"materialize_stage33_11_smallest_direct_exceptional_valuations.py"
REMAIN=S11/"materialize_stage33_11_remaining_representative_direct_exceptional_valuations.py"
CARRIERS=S11/"materialize_stage33_11_all_generator_strict_transform_carriers.py"
GENERATED=[S11/"stage33-11-smallest-direct-exceptional-valuations.json",S11/"stage33-11-remaining-representative-direct-exceptional-valuations.json",S11/"stage33-11-all-generator-strict-transform-carriers.json"]
CERT_SHA="ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6"
V91C1B_SHA="4398be760e937e1aba279af5fd099b029dc9998675503b5df7130e714ee81387"
GALOIS_SHA="e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"
BLOB_LOCKS={GALOIS:"f277939b7f258928f484d2b970d4dfb2ec6133a8",SMALL:"14541416d8d5f891d36d677be0872878026b1795",REMAIN:"85342c41f79a3b12782c718672a715e506dfd77b",CARRIERS:"ad8704b8c5c5c4b248d1fa553a7a44a05b39e21d"}
SOURCE="A2_02"; COORDS=["a1","a2","a3","b1","b2","b3","c"]
COMPONENTS=["EXC_003","EXC_004","EXC_011","EXC_012","SIDE_002","SIDE_004","SIDE_006","SIDE_008"]
NEXT="V91C1D_MATERIALIZE_A2_02_PURITY_OFFBOUNDARY_CORRECTION_AND_PRIME_LEVEL_CECH_CARTIER_TRANSITION_DATA"

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def blob(raw): return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load(p,h):
 x=json.loads(p.read_text()); b=dict(x); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return x
def sg(e): return "p" if e==1 else "m"
def c1a1(e1,e2,e3): return f"C1_A1_{sg(e1)}{sg(e2)}{sg(e3)}"
def c1a3(e1,e2,e3): return f"C1_A3_{sg(e1)}{sg(e2)}{sg(e3)}"
def c2b2(e1,e2): return f"C2_B2_{sg(e1)}{sg(e2)}"
def gf2rank(mat):
 rows=[sum((int(x)&1)<<j for j,x in enumerate(r)) for r in mat]; rank=0
 while rows:
  p=max(rows)
  if p==0: break
  k=p.bit_length()-1; rank+=1; rows=[r^p if ((r>>k)&1) else r for r in rows if r!=p]
 return rank
def scrank(polys,t):
 facs=[]; supports=[]
 for p in polys:
  _,fl=sp.factor_list(sp.Poly(p,t),extension=[sp.I,sp.sqrt(2)]); row=[]
  for f,e in fl:
   key=sp.srepr(sp.Poly(f,t,extension=[sp.I,sp.sqrt(2)]).monic().as_expr())
   if key not in facs: facs.append(key)
   row.append((key,e&1))
  supports.append(row)
 mat=[[0]*len(facs) for _ in polys]
 for i,row in enumerate(supports):
  for key,e in row: mat[i][facs.index(key)]^=e
 return gf2rank(mat)

cert=load(CERT,CERT_SHA); v91c1b=load(V91C1B,V91C1B_SHA); galois=load(GALOIS,GALOIS_SHA)
for p,h in BLOB_LOCKS.items(): assert blob(p.read_bytes())==h,p
assert cert["entry_authority"]=={"audited_authority":"V91C1A","v91c1b_candidate_canonical_sha256":V91C1B_SHA,"v91c1b_hostile_audit_pass_claimed":False}
assert v91c1b["next_exact_leaf"].startswith("V91C1C_REFINE_A2_02_") and v91c1b["credit_firewall"]["merge_allowed"] is False
src=cert["source_locks"]
assert src["stoll_repository"]=="MichaelStollBayreuth/Verification" and src["stoll_commit"]=="51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
assert src["stoll_path"]=="Cuboids/cuboids.magma" and src["stoll_blob_sha1"]=="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
assert src["stoll_geometry_prefix_sha256"]=="c0456ca5e024b8d200e5516d62292d701da77b0142f8225c282ea978bad1e58c"
assert galois["source"]["git_blob_sha1"]==src["stoll_blob_sha1"] and galois["source"]["commit"]==src["stoll_commit"] and galois["source"]["geometry_prefix_sha256"]==src["stoll_geometry_prefix_sha256"]
assert galois["known_curve_count"]==92 and galois["known_class_count"]==140
F=cert["source_locked_prime_families"]
assert F["C1_A1"]=="Curve(S,[a1,a2+e1*b3,a3+e2*b2,b1+e3*c]), e1,e2,e3 in {+1,-1}; conics"
assert F["C1_A3"]=="Curve(S,[a3,a1+e1*b2,a2+e2*b1,b3+e3*c]), e1,e2,e3 in {+1,-1}; conics"
assert F["C2_B2"]=="Curve(S,[b2,i*a3+e1*a1,a2+e2*c]), e1,e2 in {+1,-1}; genus-1 degree-4 curves"
sm=cert["surface_model"]; assert sm["field"]=="L=Q(i,sqrt(2))" and sm["coordinates"]==COORDS and sm["hyperplane_section_degree"]==16
a1,a2,a3,b1,b2,b3,c=sp.symbols("a1 a2 a3 b1 b2 b3 c")
Q1=a1**2+a2**2-b3**2; Q2=a2**2+a3**2-b1**2; Q3=a1**2+a3**2-b2**2; Q4=a1**2+a2**2+a3**2-c**2
assert sm["equations"]==["a1^2+a2^2-b3^2","a2^2+a3^2-b1^2","a1^2+a3^2-b2^2","a1^2+a2^2+a3^2-c^2"]
assert sp.expand((a2+b3)*(a2-b3)+a1**2-Q1)==0
assert sp.expand((a3+b2)*(a3-b2)+a1**2-Q3)==0
assert sp.expand((b3-c)*(b3+c)+a3**2-(Q4-Q1))==0
x,y,z=sp.symbols("x y z"); conic=z**2-x**2-y**2; assert sp.factor(conic,extension=[sp.I,sp.sqrt(2)])==conic
t=sp.symbols("t"); assert scrank([1+t**2,1-t**2],t)==2
for key,polys in (("H_B2_PLUS_B3_MINUS_C",[t,t+2,2*t+1,t**2+4*t+1]),("H_B2_MINUS_B3_PLUS_C",[t,t-2,2*t-1,t**2-4*t+1])):
 assert scrank(polys,t)==4
 _,qfac=sp.factor_list(sp.Poly(polys[-1],t),extension=[sp.I,sp.sqrt(2)]); assert len(qfac)==1 and qfac[0][0].degree()==2 and qfac[0][1]==1
 assert cert["prime_refinement"][key]["valuation_parity_rank"]==4 and cert["prime_refinement"][key]["no_b3_zero_component"] is True
for csub in (b2,-b2):
 assert sp.expand((Q4-Q3).subs({b3:0,c:csub}))==a2**2
 assert sp.expand(Q1.subs({b3:0,a2:0}))==a1**2
 assert sp.expand(Q3.subs({a1:0}))==a3**2-b2**2
 assert sp.expand(Q2.subs({a2:0}))==a3**2-b1**2
R=cert["prime_refinement"]; all3=[(e1,e2,e3) for e1 in (1,-1) for e2 in (1,-1) for e3 in (1,-1)]; all2=[(e1,e2) for e1 in (1,-1) for e2 in (1,-1)]
assert R["H_A1"]["prime_labels"]==[c1a1(*e) for e in all3]
assert R["H_A2_PLUS_B3"]["prime_labels"]==[c1a1(1,e2,e3) for e2,e3 in all2]
assert R["H_A3_PLUS_B2"]["prime_labels"]==[c1a1(e1,1,e3) for e1,e3 in all2]
assert R["H_B3_MINUS_C"]["prime_labels"]==[c1a3(e1,e2,-1) for e1,e2 in all2]
assert R["H_B2"]["prime_labels"]==[c2b2(*e) for e in all2]
for row in R.values(): assert row["prime_count"]==len(row["prime_labels"]) and row["prime_count"]*row["prime_degree"]*row["scheme_multiplicity_each"]==16 and row["weighted_degree_total"]==16
ccp=list(map(int,galois["cc_permutation_1based"])); ctp=list(map(int,galois["ct_permutation_1based"]))
assert {j:ccp[j-1] for j in (37,38,39,40)}=={37:39,38:40,39:37,40:38}
assert {j:ctp[j-1] for j in (37,38,39,40)}=={37:37,38:38,39:39,40:40}
pre={p:p.exists() for p in GENERATED}
try:
 runpy.run_path(str(SMALL),run_name="__main__"); runpy.run_path(str(REMAIN),run_name="__main__"); ns=runpy.run_path(str(CARRIERS),run_name="__main__"); carriers=ns["cert"]; normalize=ns["normalize"]
 recs=[r for r in carriers["records"] if r["source_direction"]==SOURCE]; assert len(recs)==1; rec=recs[0]; assert rec["component_count"]==8 and rec["distinct_carrier_count"]==7
 def raw(**kw): return [[int(kw.get(k,0)),1,0,1] for k in COORDS]
 forms={"H_A1":raw(a1=1),"H_A2_PLUS_B3":raw(a2=1,b3=1),"H_A3_PLUS_B2":raw(a3=1,b2=1),"H_B3_MINUS_C":raw(b3=1,c=-1),"H_B2":raw(b2=1),"H_B2_PLUS_B3_MINUS_C":raw(b2=1,b3=1,c=-1),"H_B2_MINUS_B3_PLUS_C":raw(b2=1,b3=-1,c=1)}
 global_by_sig={tuple(tuple(z) for z in sig):hid for hid,sig in carriers["global_carrier_inventory"].items()}; ids={}
 for key,coeffs in forms.items(): sig=normalize(coeffs); assert sig in global_by_sig,key; ids[key]=global_by_sig[sig]
 assert set(ids.values())=={h for v in rec["component_signed_carrier_vectors"].values() for h in v}
 ev={"EXC_003":{"H_A1":1,"H_A2_PLUS_B3":-1},"EXC_004":{"H_A1":1,"H_A2_PLUS_B3":-1},"EXC_011":{"H_A1":1,"H_A3_PLUS_B2":-1},"EXC_012":{"H_A1":1,"H_A3_PLUS_B2":-1},"SIDE_002":{"H_B2_PLUS_B3_MINUS_C":1,"H_B3_MINUS_C":-1},"SIDE_004":{"H_B2_MINUS_B3_PLUS_C":1,"H_B3_MINUS_C":-1},"SIDE_006":{"H_B2":1,"H_B2_PLUS_B3_MINUS_C":1,"H_B3_MINUS_C":-2},"SIDE_008":{"H_B2":1,"H_B2_MINUS_B3_PLUS_C":1,"H_B3_MINUS_C":-2}}
 assert set(rec["component_signed_carrier_vectors"])==set(COMPONENTS)
 for cid,v in ev.items(): assert rec["component_signed_carrier_vectors"][cid]==dict(sorted({ids[k]:e for k,e in v.items()}.items()))
 key_by_id={h:k for k,h in ids.items()}; pv={}
 for cid,cv in rec["component_signed_carrier_vectors"].items():
  z={}
  for hid,coeff in cv.items():
   rr=R[key_by_id[hid]]; m=int(rr["scheme_multiplicity_each"])
   for p in rr["prime_labels"]: z[p]=z.get(p,0)+int(coeff)*m
  pv[cid]={p:e for p,e in sorted(z.items()) if e}
 maps=cert["prime_galois_transport"]
 for g,pmap in (("cc",maps["cc_prime_map"]),("ct",maps["ct_prime_map"])):
  for cid,v in pv.items():
   z={}
   for p,e in v.items(): q=pmap[p]; z[q]=z.get(q,0)+e
   z={p:e for p,e in sorted(z.items()) if e}; matches=sorted(tgt for tgt,w in pv.items() if w==z)
   assert matches==sorted(rec["component_galois_target_candidates"][g][cid])
 exact=cert["exact_consequence"]
 for k in ("all_7_carriers_prime_refined","all_prime_components_irducible_over_L" if False else "all_prime_components_irreducible_over_L","scheme_multiplicities_exact","prime_level_cc_ct_transport_complete","resolved_exceptional_valuation_attachment_inherited_exact_from_v91c1b","resolved_full_surface_height_one_attachment_for_a2_02_complete"): assert exact[k] is True
 for k in ("purity_offboundary_correction_materialized","full_surface_cech_transition_glue_materialized","cartier_transition_binding_materialized","exact_marked_brauer_image_equal_mask20_materialized","genuine_full_surface_h2_mu2_lift_for_e3"): assert exact[k] is False
 assert exact["a2_02_distinct_strict_transform_carrier_count"]==7 and cert["next_exact_leaf"]==NEXT
 assert cert["credit_firewall"]["hostile_audit_pass_for_v91c1b_or_v91c1c"] is False and cert["credit_firewall"]["stage33_progress"]=="6/11" and cert["credit_firewall"]["merge_allowed"] is False
 print(json.dumps({"success":True,"marker":"V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT_EXACT","certificate_sha256":CERT_SHA,"carrier_count":7,"prime_level_cc_ct_transport_complete":True,"resolved_full_surface_height_one_attachment_for_a2_02_complete":True,"purity_cech_cartier_still_open":True,"stage33_progress":"6/11","next_exact_leaf":NEXT},sort_keys=True))
finally:
 for p,existed in pre.items():
  if not existed and p.exists(): p.unlink()
