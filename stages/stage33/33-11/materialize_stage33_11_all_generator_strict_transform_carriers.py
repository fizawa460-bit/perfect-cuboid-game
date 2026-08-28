#!/usr/bin/env python3
"""Materialize finite strict-transform carrier data for all 14 MAIN generators.

For every ambient rational-function factor used by the five smallest directions
and the nine remaining cyclic-block representatives, normalize the ambient
linear form over Q(i).  Its hyperplane defines a strict-transform *carrier* on
the blown-up surface.  We record the signed divisor coefficient of every carrier
in every component and verify exact cc/ct transport by normalized-factor
multisets.

This deliberately stops one step before claiming that every hyperplane-section
carrier is a single height-one prime on the surface.  Any reducible carrier must
be refined into its prime components.  That finite carrier-refinement question
is the only strict-transform purity audit debt left by this leaf.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
SIDE = S07 / "mixed-order-side-ambient-function-lifts.json"
EXC = S07 / "mixed-order-exceptional-ambient-tangent-function-lifts.json"
LOCAL5 = HERE / "stage33-11-smallest-direct-exceptional-valuations.json"
LOCAL9 = HERE / "stage33-11-remaining-representative-direct-exceptional-valuations.json"
OUT = HERE / "stage33-11-all-generator-strict-transform-carriers.json"
GENERATORS = ["A2_02","A2_03","A2_24","A2_25","A2_26",
              "A2_04","A2_01","A2_07","A2_05","A2_10","A2_08","A2_09","A2_16","A2_15"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    if "canonical_sha256" in obj:
        body = dict(obj); claimed = body.pop("canonical_sha256")
        if csha(body) != claimed:
            raise SystemExit(f"canonical hash mismatch for {path.name}")
    return obj


def qi(z):
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def qmul(x,y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def qinv(x):
    d=x[0]*x[0]+x[1]*x[1]
    if d==0: raise SystemExit("zero projective vector")
    return x[0]/d,-x[1]/d


def qconj(x): return x[0],-x[1]
def qenc(x): return [x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator]


def normalize(raw):
    vals=[qi(z) for z in raw]
    pivot=next((x for x in vals if x!=(0,0)),None)
    if pivot is None: raise SystemExit("zero linear form")
    inv=qinv(pivot)
    return tuple(tuple(qenc(qmul(x,inv))) for x in vals)


def act(sig,g):
    vals=[(Fraction(z[0],z[1]),Fraction(z[2],z[3])) for z in sig]
    if g=="cc": vals=[qconj(x) for x in vals]
    elif g!="ct": raise SystemExit(g)
    return normalize([qenc(x) for x in vals])


def atom(raw, exponent, label):
    sig=normalize(raw)
    return {"carrier_id":csha([list(z) for z in sig]),"signature":sig,
            "exponent":int(exponent),"source_label":label}


def side_atoms(row):
    out=[]
    for j,f in enumerate(row["numerator_factors"]):
        out.append(atom(f["ambient_linear_factor_coefficients_L_basis"],int(f.get("exponent",1)),f"num[{j}]/{f['edge_id']}"))
    out.append(atom(row["D_coefficients_L_basis"],-int(row["denominator"]["exponent"]),"D"))
    return out


def exc_atoms(row):
    out=[]
    for j,f in enumerate(row["numerator_factors"]):
        out.append(atom(f["ambient_tangent_linear_factor_coefficients_L_basis"],int(f.get("exponent",1)),f"num[{j}]/{f['edge_id']}"))
    out.append(atom(row["ambient_projection_R0_R1_coefficients_L_basis"][1],-int(row["denominator"]["exponent"]),"R1"))
    return out


def vector(atoms):
    v={}
    for a in atoms:
        h=a["carrier_id"]; v[h]=v.get(h,0)+a["exponent"]
    return {h:e for h,e in sorted(v.items()) if e}


def acted_vector(atoms,g,sig_to_id):
    v={}
    for a in atoms:
        h=sig_to_id.get(act(a["signature"],g))
        if h is None: raise SystemExit("Galois image carrier missing from finite inventory")
        v[h]=v.get(h,0)+a["exponent"]
    return {h:e for h,e in sorted(v.items()) if e}


side=load_checked(SIDE); exc=load_checked(EXC)
local5=load_checked(LOCAL5); local9=load_checked(LOCAL9)
if local5.get("exact_local_consequence",{}).get("coverage")!="5/5": raise SystemExit("5-local evidence moved")
if local9.get("exact_local_consequence",{}).get("coverage")!="9/9": raise SystemExit("9-local evidence moved")
side_src={r["source_basis_name"]:r for r in side["source_ambient_side_lifts"]}
exc_src={r["source_basis_name"]:r for r in exc["source_ambient_exceptional_lifts"]}

records=[]; global_carriers={}
for source in GENERATORS:
    if source not in side_src or source not in exc_src: raise SystemExit(f"missing source {source}")
    packages={}
    for row in side_src[source]["side_ambient_function_lifts"]: packages[row["component_id"]]=side_atoms(row)
    for row in exc_src[source]["exceptional_ambient_tangent_function_lifts"]: packages[row["component_id"]]=exc_atoms(row)
    sig_to_id={}
    for atoms in packages.values():
        for a in atoms:
            sig_to_id[a["signature"]]=a["carrier_id"]
            global_carriers[a["carrier_id"]]=[list(z) for z in a["signature"]]
    # Require the finite carrier inventory itself to be closed under cc/ct.
    for sig in list(sig_to_id):
        for g in ("cc","ct"):
            image=act(sig,g)
            if image not in sig_to_id:
                raise SystemExit(f"{source}: {g} image carrier absent")
    base_vectors={cid:vector(atoms) for cid,atoms in packages.items()}
    transport={"cc":{},"ct":{}}
    checks=[]
    for g in ("cc","ct"):
        for cid,atoms in packages.items():
            av=acted_vector(atoms,g,sig_to_id)
            matches=sorted(t for t,v in base_vectors.items() if v==av)
            if not matches: raise SystemExit(f"{source}: {g} strict carrier vector has no component target for {cid}")
            transport[g][cid]=matches
            checks.append({"generator":g,"source_component":cid,"matching_target_components":matches,
                           "signed_strict_transform_carrier_vector_matches_exactly":True})
    records.append({
        "source_direction":source,
        "component_count":len(packages),
        "distinct_carrier_count":len(sig_to_id),
        "component_signed_carrier_vectors":base_vectors,
        "component_galois_target_candidates":transport,
        "checks":checks,
        "exact_consequence":{
            "ambient_strict_transform_carrier_inventory_closed_under_cc_ct":True,
            "all_component_signed_carrier_vectors_cc_ct_transport_exact":True,
            "strict_transform_difference_zero_at_carrier_level":"ZERO_EXACT_CARRIER_LEVEL",
        },
    })

cert={
    "schema":"STAGE33_11_ALL_GENERATOR_STRICT_TRANSFORM_CARRIERS_V1",
    "stage":"33-11",
    "branch":"33-11c_ALL_GENERATOR_FINITE_STRICT_TRANSFORM_CARRIERS",
    "generators":GENERATORS,
    "source_locks":{
        "smallest_local_exceptional_valuation_sha256":local5["canonical_sha256"],
        "remaining_representative_local_exceptional_valuation_sha256":local9["canonical_sha256"],
        "side_ambient_lifts_sha256":side.get("canonical_sha256"),
        "exceptional_ambient_lifts_sha256":exc.get("canonical_sha256"),
    },
    "global_carrier_inventory":global_carriers,
    "records":records,
    "summary":{
        "working_generator_coverage":"14/14",
        "distinct_global_normalized_linear_carriers":len(global_carriers),
        "all_14_strict_transform_differences_zero_at_carrier_level":True,
        "all_14_exceptional_locus_differences_already_zero_exact":True,
        "remaining_purity_problem_is_finite_carrier_prime_refinement":True,
    },
    "audit_debt":{
        "required":True,
        "narrowed_to":"for each distinct normalized hyperplane-section carrier, factor/refine its strict transform into actual height-one primes on the surface and verify Galois transport of any nontrivial splitting",
        "no_longer_open":"ambient linear-factor carrier enumeration, signed carrier multiplicities, cc/ct carrier transport, exceptional-divisor valuations",
        "main_working_pin":"treat each finite carrier refinement as Q-defined/V4-compatible pending audit",
    },
    "firewalls":{
        "stage33_11_exact_connecting_columns":0,
        "stage33_11_closed_exact":False,
        "stage33_12_released":False,
        "stage33_08_released":False,
        "stage33_07_closed":False,
        "theorem_credit":False,
        "endpoint_credit":False,
    },
}
cert["canonical_sha256"]=csha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"success":True,"generator_coverage":"14/14","distinct_carriers":len(global_carriers),"strict_transform_difference":"ZERO_EXACT_CARRIER_LEVEL_ALL_14","remaining_audit_debt":"FINITE_CARRIER_PRIME_REFINEMENT","exact_exit_progress":"0/26","certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
