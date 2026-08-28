#!/usr/bin/env python3
"""Reduce the finite carrier-refinement problem by exact geometric symmetry.

The Testa--Stoll model is preserved by the two actual coordinate swaps certified
in Stage33-09:
  swap12: a1<->a2, b1<->b2;
  swap13: a1<->a3, b1<->b3;
and by complex conjugation.  Starting from the 30 carriers actually used by the
14 MAIN working generators, close their normalized Q(i)-linear signatures under
these actions and partition them into exact geometric orbits.  Only one prime
refinement per orbit representative is needed; transport to the rest is by the
certified surface automorphisms.

This is a MAIN reduction only.  It does not assert irreducibility or promote an
exact Stage33-11 connecting column.
"""
from __future__ import annotations
import hashlib,json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
CARR=HERE/"stage33-11-all-generator-strict-transform-carriers.json"
SCOUT=HERE/"stage33-11-carrier-prime-refinement-scout.json"
OUT=HERE/"stage33-11-carrier-geometric-orbit-reduction.json"
PERMS={"swap12":[1,0,2,4,3,5,6],"swap13":[2,1,0,5,4,3,6]}

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p):
    x=json.loads(p.read_text()); b=dict(x); h=b.pop("canonical_sha256")
    if csha(b)!=h: raise SystemExit(f"hash mismatch {p.name}")
    return x

def qi(z): return Fraction(z[0],z[1]),Fraction(z[2],z[3])
def mul(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    return x[0]/d,-x[1]/d
def enc(x): return (x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator)
def norm(sig):
    vals=[qi(z) for z in sig]; p=next(x for x in vals if x!=(0,0)); u=inv(p)
    return tuple(enc(mul(x,u)) for x in vals)
def cc(sig): return norm([(z[0],z[1],-z[2],z[3]) for z in sig])
def swap(sig,perm): return norm([sig[j] for j in perm])
def sid(sig): return csha([list(z) for z in sig])

car=load(CARR); scout=load(SCOUT)
if car["summary"]["distinct_global_normalized_linear_carriers"]!=30: raise SystemExit("carrier count moved")
if scout["summary"]["carrier_count"]!=30: raise SystemExit("scout carrier count moved")
original={h:tuple(tuple(z) for z in s) for h,s in car["global_carrier_inventory"].items()}
orig_by_sig={s:h for h,s in original.items()}
unresolved=set(scout["summary"]["unresolved_carrier_ids"])
forced=set(scout["summary"]["forced_refinement_carrier_ids"])

def orbit(seed):
    seen={seed}; stack=[seed]
    while stack:
        s=stack.pop()
        for t in (cc(s),swap(s,PERMS["swap12"]),swap(s,PERMS["swap13"])):
            if t not in seen: seen.add(t); stack.append(t)
    return seen

remaining=set(original.values()); rows=[]
while remaining:
    seed=min(remaining); orb=orbit(seed); orig=sorted(orig_by_sig[s] for s in orb if s in orig_by_sig)
    remaining.difference_update(orb)
    rep=min(orb,key=sid)
    rows.append({
      "orbit_id":csha(sorted(sid(s) for s in orb)),
      "closure_size":len(orb),
      "representative_signature":[list(z) for z in rep],
      "representative_signature_sha256":sid(rep),
      "original_carrier_ids":orig,
      "original_carrier_count":len(orig),
      "forced_original_carrier_ids":[h for h in orig if h in forced],
      "unresolved_original_carrier_ids":[h for h in orig if h in unresolved],
      "requires_prime_refinement":any(h in unresolved for h in orig),
    })
rows.sort(key=lambda r:r["orbit_id"])
unresolved_orbits=[r for r in rows if r["requires_prime_refinement"]]
cert={
 "schema":"STAGE33_11_CARRIER_GEOMETRIC_ORBIT_REDUCTION_V1","stage":"33-11",
 "source_locks":{"carrier_sha256":car["canonical_sha256"],"prime_refinement_scout_sha256":scout["canonical_sha256"],"stage33_09_actual_swaps":"swap12=[1,0,2,4,3,5,6]; swap13=[2,1,0,5,4,3,6]"},
 "action_generators":{"cc":"complex conjugation on Q(i) coefficients",**PERMS},
 "orbits":rows,
 "summary":{"original_carrier_count":30,"geometric_orbit_count":len(rows),"unresolved_original_carrier_count":len(unresolved),"unresolved_geometric_orbit_count":len(unresolved_orbits),"prime_refinement_representatives":[r["representative_signature_sha256"] for r in unresolved_orbits],"all_30_original_carriers_partitioned_exactly":sum(r["original_carrier_count"] for r in rows)==30},
 "main_working_consequence":{"factorization_work_reduced_to_one_representative_per_unresolved_geometric_orbit":True,"transport_generators_are_certified_surface_automorphisms":True,"exact_connecting_columns_promoted":0},
 "firewalls":{"stage33_11_closed_exact":False,"stage33_12_released":False,"stage33_08_released":False,"stage33_07_closed":False,"theorem_credit":False,"endpoint_credit":False}
}
if not cert["summary"]["all_30_original_carriers_partitioned_exactly"]: raise SystemExit("orbit partition incomplete")
cert["canonical_sha256"]=csha(cert); OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,**cert["summary"],"exact_exit_progress":"0/26"},indent=2,sort_keys=True))
