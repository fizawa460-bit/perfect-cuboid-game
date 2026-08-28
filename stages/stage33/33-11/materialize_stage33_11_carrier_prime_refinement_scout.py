#!/usr/bin/env python3
"""Exact finite scout for strict-transform carrier prime refinement.

Consumes the 30 normalized ambient hyperplane carriers already materialized for
all 14 MAIN generators.  It does not claim a full height-one prime
factorization.  Instead it (1) quotients the finite inventory by complex
conjugation, and (2) recognizes the carrier types whose scheme-theoretic
refinement follows immediately from the four frozen Testa--Stoll quadrics.

The remaining carriers are an explicit finite list for the next MAIN leaf.
No Stage33-11 exact connecting column is promoted here.
"""
from __future__ import annotations

import hashlib, json
from fractions import Fraction
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
SRC=HERE/"stage33-11-all-generator-strict-transform-carriers.json"
OUT=HERE/"stage33-11-carrier-prime-refinement-scout.json"
COORDS=["a1","a2","a3","b1","b2","b3","c"]

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load_checked(p):
    x=json.loads(p.read_text()); body=dict(x); claimed=body.pop("canonical_sha256")
    if csha(body)!=claimed: raise SystemExit("carrier certificate hash mismatch")
    return x

def qi(z): return Fraction(z[0],z[1]),Fraction(z[2],z[3])
def mul(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    if not d: raise SystemExit("zero pivot")
    return x[0]/d,-x[1]/d
def enc(x): return [x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator]
def norm(vals):
    q=[qi(z) for z in vals]; p=next(x for x in q if x!=(0,0)); u=inv(p)
    return tuple(tuple(enc(mul(x,u))) for x in q)
def conj(sig):
    vals=[]
    for z in sig: vals.append([z[0],z[1],-z[2],z[3]])
    return norm(vals)
def linear(**kw):
    vals=[]
    for k in COORDS:
        q=kw.get(k,0)
        vals.append([int(q),1,0,1])
    return norm(vals)

src=load_checked(SRC)
if src["summary"]["working_generator_coverage"]!="14/14": raise SystemExit("coverage moved")
carriers=src["global_carrier_inventory"]
if len(carriers)!=30: raise SystemExit(f"expected 30 carriers, got {len(carriers)}")
sig_to_id={tuple(tuple(z) for z in sig):h for h,sig in carriers.items()}

# Frozen surface identities.  These are polynomial identities, not heuristic
# factorization statements.
a1,a2,a3,b1,b2,b3,c=sp.symbols("a1 a2 a3 b1 b2 b3 c")
Q1=a1**2+a2**2-b3**2
Q2=a2**2+a3**2-b1**2
Q3=a1**2+a3**2-b2**2
Q4=a1**2+a2**2+a3**2-c**2
identities={
 "c2-b1_2=a1_2":sp.expand((c**2-b1**2)-a1**2 - (Q2-Q4)),
 "c2-b2_2=a2_2":sp.expand((c**2-b2**2)-a2**2 - (Q3-Q4)),
 "c2-b3_2=a3_2":sp.expand((c**2-b3**2)-a3**2 - (Q1-Q4)),
 "b1_2=a2_2+a3_2":sp.expand(b1**2-a2**2-a3**2+Q2),
 "b2_2=a1_2+a3_2":sp.expand(b2**2-a1**2-a3**2+Q3),
 "b3_2=a1_2+a2_2":sp.expand(b3**2-a1**2-a2**2+Q1),
}
if any(v!=0 for v in identities.values()): raise SystemExit("surface identity regression")

special={
 linear(b1=1):{"type":"AXIS_B1_ZERO","forced_equation":"a2^2+a3^2=0","reduced_linear_branches_over_Qi":["a2+i*a3","a2-i*a3"]},
 linear(b2=1):{"type":"AXIS_B2_ZERO","forced_equation":"a1^2+a3^2=0","reduced_linear_branches_over_Qi":["a1+i*a3","a1-i*a3"]},
 linear(b3=1):{"type":"AXIS_B3_ZERO","forced_equation":"a1^2+a2^2=0","reduced_linear_branches_over_Qi":["a1+i*a2","a1-i*a2"]},
 linear(c=1,b1=-1):{"type":"DIFF_C_MINUS_B1","forced_equation":"a1^2=0","scheme_multiplicity_signal":2,"reduced_support":"a1=0"},
 linear(c=1,b2=-1):{"type":"DIFF_C_MINUS_B2","forced_equation":"a2^2=0","scheme_multiplicity_signal":2,"reduced_support":"a2=0"},
 linear(c=1,b3=-1):{"type":"DIFF_C_MINUS_B3","forced_equation":"a3^2=0","scheme_multiplicity_signal":2,"reduced_support":"a3=0"},
}

records=[]; recognized=[]; unresolved=[]
for h,sraw in sorted(carriers.items()):
    sig=tuple(tuple(z) for z in sraw)
    cc=conj(sig); ccid=sig_to_id.get(cc)
    if ccid is None: raise SystemExit(f"cc image missing for {h}")
    row={"carrier_id":h,"cc_carrier_id":ccid,"support":[COORDS[i] for i,z in enumerate(sig) if tuple(z)!=(0,1,0,1)]}
    if sig in special:
        row["refinement_scout"]={"status":"FORCED_BY_FROZEN_QUADRICS",**special[sig]}; recognized.append(h)
    else:
        row["refinement_scout"]={"status":"EXPLICIT_FINITE_PRIME_REFINEMENT_STILL_REQUIRED"}; unresolved.append(h)
    records.append(row)

# Exact cc orbit partition of the finite carrier set.
unseen=set(carriers); orbits=[]
while unseen:
    h=min(unseen); sig=tuple(tuple(z) for z in carriers[h]); mate=sig_to_id[conj(sig)]
    orb=sorted({h,mate}); orbits.append(orb); unseen.difference_update(orb)

cert={
 "schema":"STAGE33_11_CARRIER_PRIME_REFINEMENT_SCOUT_V1",
 "stage":"33-11","branch":"33-11c_FINITE_CARRIER_PRIME_REFINEMENT_SCOUT",
 "source_locks":{"strict_transform_carrier_sha256":src["canonical_sha256"],"testa_stoll_surface_model":"a1^2+a2^2=b3^2; a2^2+a3^2=b1^2; a1^2+a3^2=b2^2; a1^2+a2^2+a3^2=c^2"},
 "exact_surface_identity_checks":{k:True for k in identities},
 "carrier_cc_orbits":orbits,"records":records,
 "summary":{"carrier_count":30,"cc_orbit_count":len(orbits),"forced_refinement_carrier_count":len(recognized),"forced_refinement_carrier_ids":recognized,"unresolved_carrier_count":len(unresolved),"unresolved_carrier_ids":unresolved,"all_unresolved_carriers_explicitly_enumerated":True},
 "main_working_consequence":{"prime_refinement_debt_is_now_explicit_finite_list":True,"forced_axis_and_c_minus_b_refinements_separated":True,"remaining_work":"factor/refine only the unresolved carrier list on the surface; then verify prime-level cc transport","exact_connecting_columns_promoted":0},
 "firewalls":{"stage33_11_closed_exact":False,"stage33_12_released":False,"stage33_08_released":False,"stage33_07_closed":False,"theorem_credit":False,"endpoint_credit":False}
}
cert["canonical_sha256"]=csha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,**cert["summary"],"exact_exit_progress":"0/26"},indent=2,sort_keys=True))
