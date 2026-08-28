#!/usr/bin/env python3
"""Materialize direct exceptional valuations for all five smallest raw-order2 directions.

This MAIN leaf generalizes the A2_26 local calculation to A2_02, A2_03,
A2_24, A2_25, and A2_26. It reconstructs each retained ambient boundary
function from the Stage33-07 side/exceptional lifts, evaluates every ambient
linear factor at all 48 frozen blow-up centers over Q(i), and checks cc/ct
equivariance. Strict-transform/off-boundary purity remains audit debt.
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
NODES = S07 / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "stage33-11-smallest-direct-exceptional-valuations.json"
SMALLEST = ["A2_02", "A2_03", "A2_24", "A2_25", "A2_26"]
LOCKS = {
    SIDE.name: "2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d",
    EXC.name: "a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    if claimed != LOCKS[path.name] or csha(body) != LOCKS[path.name]:
        raise SystemExit(f"source lock moved for {path.name}: {claimed}")
    return obj


def load_checked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    if "canonical_sha256" in obj:
        body = dict(obj); claimed = body.pop("canonical_sha256")
        if csha(body) != claimed:
            raise SystemExit(f"canonical hash mismatch for {path.name}")
    return obj


def qi(z): return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))
def qadd(x,y): return x[0]+y[0], x[1]+y[1]
def qmul(x,y): return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]
def qconj(x): return x[0], -x[1]
def qenc(x): return [x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator]


def qinv(x):
    d=x[0]*x[0]+x[1]*x[1]
    if d==0: raise SystemExit("cannot invert zero Gaussian rational")
    return x[0]/d,-x[1]/d


def normalize(raw):
    vals=[qi(z) for z in raw]
    pivot=next((x for x in vals if x!=(0,0)),None)
    if pivot is None: raise SystemExit("zero projective vector/form")
    inv=qinv(pivot)
    return tuple(tuple(qenc(qmul(x,inv))) for x in vals)


def act_sig(sig,generator):
    vals=[(Fraction(z[0],z[1]),Fraction(z[2],z[3])) for z in sig]
    if generator=="cc": vals=[qconj(x) for x in vals]
    elif generator!="ct": raise SystemExit(f"unknown generator {generator}")
    return normalize([qenc(x) for x in vals])


def dot(form,point):
    out=(Fraction(0),Fraction(0))
    for a,b in zip(form,point): out=qadd(out,qmul(a,b))
    return out


def atom(raw, exponent, label):
    sig=normalize(raw); sj=[list(z) for z in sig]
    return {"linear_form_sha256":csha(sj),"normalized_linear_form_Qi":sj,"divisor_exponent":int(exponent),"source_label":label}


def package_side(row):
    out=[]
    for j,f in enumerate(row["numerator_factors"]):
        out.append(atom(f["ambient_linear_factor_coefficients_L_basis"],int(f.get("exponent",1)),f"numerator_factors[{j}]/{f['edge_id']}"))
    out.append(atom(row["D_coefficients_L_basis"],-int(row["denominator"]["exponent"]),"D"))
    return out


def package_exc(row):
    out=[]
    for j,f in enumerate(row["numerator_factors"]):
        out.append(atom(f["ambient_tangent_linear_factor_coefficients_L_basis"],int(f.get("exponent",1)),f"numerator_factors[{j}]/{f['edge_id']}"))
    out.append(atom(row["ambient_projection_R0_R1_coefficients_L_basis"][1],-int(row["denominator"]["exponent"]),"R1"))
    return out


def multiset(atoms,generator=None):
    counts={}
    for a in atoms:
        sig=tuple(tuple(z) for z in a["normalized_linear_form_Qi"])
        if generator is not None: sig=act_sig(sig,generator)
        key=(sig,int(a["divisor_exponent"])); counts[key]=counts.get(key,0)+1
    return counts


side=load_locked(SIDE); exc=load_locked(EXC); nodes=load_checked(NODES)
models=nodes.get("exceptional_models",[])
if len(models)!=48: raise SystemExit(f"expected 48 exceptional models, got {len(models)}")
node_sig_to_id={}; node_points={}
for row in models:
    eid=row["exceptional_id"]; raw=row["node_point_ambient_P6_L_basis"]; sig=normalize(raw)
    if sig in node_sig_to_id: raise SystemExit("duplicate exceptional node signature")
    node_sig_to_id[sig]=eid; node_points[eid]=[qi(z) for z in raw]
cc_node={}
for sig,eid in node_sig_to_id.items():
    image=node_sig_to_id.get(act_sig(sig,"cc"))
    if image is None: raise SystemExit(f"cc node image missing for {eid}")
    cc_node[eid]=image
ct_node={eid:eid for eid in node_points}
side_src={r["source_basis_name"]:r for r in side["source_ambient_side_lifts"]}
exc_src={r["source_basis_name"]:r for r in exc["source_ambient_exceptional_lifts"]}
records=[]
for source in SMALLEST:
    if source not in side_src or source not in exc_src: raise SystemExit(f"missing ambient lift source {source}")
    sr,er=side_src[source],exc_src[source]
    if int(sr["raw_order"])!=2 or int(er["raw_order"])!=2: raise SystemExit(f"{source} is no longer raw-order2")
    packages={}
    for row in sr["side_ambient_function_lifts"]: packages[row["component_id"]]=package_side(row)
    for row in er["exceptional_ambient_tangent_function_lifts"]: packages[row["component_id"]]=package_exc(row)
    if not packages: raise SystemExit(f"{source} has empty ambient package")
    forms={}
    sig_to_hash={}
    for atoms in packages.values():
        for a in atoms:
            h=a["linear_form_sha256"]; forms[h]=[qi(z) for z in a["normalized_linear_form_Qi"]]
            sig_to_hash[tuple(tuple(z) for z in a["normalized_linear_form_Qi"])]=h
    factor_vectors={h:{eid:1 if dot(form,p)==(0,0) else 0 for eid,p in node_points.items()} for h,form in forms.items()}
    factor_checks=[]
    for h,vals in factor_vectors.items():
        sig=next(sig for sig,hh in sig_to_hash.items() if hh==h)
        for generator,node_map in (("cc",cc_node),("ct",ct_node)):
            gh=sig_to_hash.get(act_sig(sig,generator))
            if gh is None: raise SystemExit(f"{source}: {generator} image of factor {h} missing")
            gvals=factor_vectors[gh]
            if not all(vals[eid]==gvals[node_map[eid]] for eid in vals): raise SystemExit(f"{source}: factor valuation equivariance failed")
            factor_checks.append({"generator":generator,"linear_form_sha256":h,"image_linear_form_sha256":gh,"all_48_exceptional_valuations_match":True})
    component_vectors={}; component_multisets={}
    for cid,atoms in packages.items():
        totals={eid:0 for eid in node_points}
        for a in atoms:
            h=a["linear_form_sha256"]; exp=int(a["divisor_exponent"])
            for eid,v in factor_vectors[h].items(): totals[eid]+=exp*v
        component_vectors[cid]=totals; component_multisets[cid]=multiset(atoms)
    actions={"cc":{},"ct":{}}; component_checks=[]; cids=sorted(packages)
    for generator,node_map in (("cc",cc_node),("ct",ct_node)):
        for cid in cids:
            acted=multiset(packages[cid],generator)
            candidates=[t for t in cids if component_multisets[t]==acted]
            good=[]; vals=component_vectors[cid]
            for target in candidates:
                tv=component_vectors[target]
                if all(vals[eid]==tv[node_map[eid]] for eid in vals): good.append(target)
            if not good: raise SystemExit(f"{source}: {generator} component image failed for {cid}")
            actions[generator][cid]=good
            component_checks.append({"generator":generator,"source_component":cid,"matching_target_components":good,"valuation_vector_match":True})
    records.append({
        "source_direction":source,"component_count":len(packages),"ambient_factor_count":len(forms),"component_ids":sorted(packages),
        "component_galois_target_candidates":actions,"factor_exceptional_valuation_vectors":factor_vectors,
        "component_exceptional_valuation_vectors":component_vectors,
        "equivariance_checks":{"factor_level":factor_checks,"component_level":component_checks},
        "summary":{"all_48_blowup_centers_evaluated_exact":True,"all_factor_vectors_cc_ct_equivariant":True,"all_component_packages_have_cc_ct_valuation_compatible_targets":True,"exceptional_locus_galois_difference_before_purity_correction":"ZERO_EXACT"},
        "main_working_bridge":{"connecting_value_under_q_defined_v4_fixed_remaining_purity_pin":"ZERO","status":"MAIN_WORKING_PENDING_STRICT_TRANSFORM_PURITY_AUDIT"},
    })
cert={
    "schema":"STAGE33_11_SMALLEST_DIRECT_EXCEPTIONAL_VALUATIONS_V1","stage":"33-11","branch":"33-11c_SMALLEST_DIRECT_BLOWUP_EXCEPTIONAL_VALUATIONS","directions":SMALLEST,
    "source_locks":{"mixed_order_side_ambient_function_lifts_sha256":LOCKS[SIDE.name],"mixed_order_exceptional_ambient_tangent_function_lifts_sha256":LOCKS[EXC.name],"exceptional_coordinate_source_sha256":nodes.get("canonical_sha256")},
    "records":records,
    "exact_local_consequence":{"directions_with_exact_exceptional_valuations":len(records),"coverage":"5/5","all_five_exceptional_locus_differences":"ZERO_EXACT","strict_transform_purity_not_promoted":True},
    "audit_debt":{"required":True,"remaining":"strict-transform/off-boundary height-one decomposition and legitimacy of the pinned Q-defined/V4-fixed global purity correction for each direction"},
    "firewalls":{"stage33_11_closed_exact":False,"stage33_12_released":False,"stage33_08_released":False,"stage33_07_closed":False,"theorem_credit":False,"endpoint_credit":False},
}
cert["canonical_sha256"]=csha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"success":True,"directions":SMALLEST,"exact_exceptional_local_coverage":"5/5","exceptional_locus_difference":"ZERO_EXACT_ALL_FIVE","audit_debt":True,"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
