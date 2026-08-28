#!/usr/bin/env python3
"""Materialize direct exceptional-divisor valuations for the A2_26 boundary functions.

This is a finite local leaf.  For every ambient linear factor already exposed by
A2_26, evaluate it at every frozen ordinary-double-point blow-up center.  A
linear form has exceptional valuation one on the blow-up iff it vanishes at the
center; otherwise the valuation is zero.  The calculation is exact over Q(i).

This does not classify strict-transform height-one primes away from the
exceptional locus.  That residual purity question remains explicit audit debt.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
PREIMAGE = HERE / "stage33-11-a2-26-explicit-gersten-difference-preimage.json"
NODES = S07 / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "stage33-11-a2-26-direct-exceptional-valuations.json"

SOURCE = "A2_26"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    if "canonical_sha256" in obj:
        body = dict(obj)
        claimed = body.pop("canonical_sha256")
        if csha(body) != claimed:
            raise SystemExit(f"canonical hash mismatch for {path.name}")
    return obj


def qi(z):
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def qadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def qmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qinv(x):
    d = x[0] * x[0] + x[1] * x[1]
    if d == 0:
        raise SystemExit("cannot invert zero Gaussian rational")
    return x[0] / d, -x[1] / d


def qconj(x):
    return x[0], -x[1]


def qenc(x):
    return [x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator]


def normalize_projective(raw):
    vals = [qi(z) for z in raw]
    pivot = next((x for x in vals if x != (0, 0)), None)
    if pivot is None:
        raise SystemExit("zero projective vector")
    inv = qinv(pivot)
    return tuple(tuple(qenc(qmul(x, inv))) for x in vals)


def conj_signature(sig):
    vals = [qconj((Fraction(z[0], z[1]), Fraction(z[2], z[3]))) for z in sig]
    return normalize_projective([qenc(x) for x in vals])


def dot(form, point):
    acc = (Fraction(0), Fraction(0))
    for a, b in zip(form, point):
        acc = qadd(acc, qmul(a, b))
    return acc


pre = load_checked(PREIMAGE)
nodes = load_checked(NODES)
if pre.get("source_direction") != SOURCE:
    raise SystemExit("explicit-preimage source moved")
if pre.get("repair_frontier", {}).get("ambient_function_package_difference_before_purity_correction_is_zero") is not True:
    raise SystemExit("ambient function package difference is no longer exact zero")

models = nodes.get("exceptional_models", [])
if len(models) != 48:
    raise SystemExit(f"expected 48 frozen exceptional models, got {len(models)}")

node_sig_to_id = {}
node_point = {}
for row in models:
    eid = row["exceptional_id"]
    raw = row["node_point_ambient_P6_L_basis"]
    sig = normalize_projective(raw)
    if sig in node_sig_to_id:
        raise SystemExit("duplicate projective node signature")
    node_sig_to_id[sig] = eid
    node_point[eid] = [qi(z) for z in raw]

cc_node = {}
for sig, eid in node_sig_to_id.items():
    image = node_sig_to_id.get(conj_signature(sig))
    if image is None:
        raise SystemExit(f"cc node image missing for {eid}")
    cc_node[eid] = image
ct_node = {eid: eid for eid in node_point}

inventory = pre.get("offboundary_hyperplane_factor_inventory", [])
if not inventory:
    raise SystemExit("A2_26 ambient factor inventory missing")
forms = {
    row["linear_form_sha256"]: [qi(z) for z in row["normalized_linear_form_Qi"]]
    for row in inventory
}
orbit_rows = {r["linear_form_sha256"]: r for r in pre["offboundary_hyperplane_factor_galois_orbits"]}

valuation_vectors = {}
for h, form in forms.items():
    values = {}
    for eid, p in node_point.items():
        values[eid] = 1 if dot(form, p) == (0, 0) else 0
    valuation_vectors[h] = values

equivariance_checks = []
for h, vals in valuation_vectors.items():
    orbit = orbit_rows[h]
    for generator, node_map in (("cc", cc_node), ("ct", ct_node)):
        gh = orbit.get(f"{generator}_image_linear_form_sha256_in_A2_26_inventory")
        if gh is None:
            raise SystemExit(f"{generator} image of factor {h} missing from A2_26 inventory")
        gvals = valuation_vectors[gh]
        ok = all(vals[eid] == gvals[node_map[eid]] for eid in vals)
        if not ok:
            raise SystemExit(f"{generator} exceptional valuation equivariance failed for {h}")
        equivariance_checks.append({
            "generator": generator,
            "linear_form_sha256": h,
            "image_linear_form_sha256": gh,
            "all_48_exceptional_valuations_match_under_node_action": True,
        })

component_exceptional_valuations = {}
for cid, atoms in pre["ambient_rational_function_atoms"].items():
    totals = {eid: 0 for eid in node_point}
    for atom in atoms:
        h = atom["linear_form_sha256"]
        exp = int(atom["divisor_exponent"])
        for eid, v in valuation_vectors[h].items():
            totals[eid] += exp * v
    component_exceptional_valuations[cid] = totals

component_checks = []
action = pre["generator_component_action"]
for generator, node_map in (("cc", cc_node), ("ct", ct_node)):
    for cid, vals in component_exceptional_valuations.items():
        target = action[generator][cid]
        tvals = component_exceptional_valuations[target]
        ok = all(vals[eid] == tvals[node_map[eid]] for eid in vals)
        if not ok:
            raise SystemExit(f"{generator} component exceptional valuation mismatch {cid}->{target}")
        component_checks.append({
            "generator": generator,
            "source_component": cid,
            "target_component": target,
            "exceptional_divisor_valuation_vector_matches": True,
        })

nonzero_factor_entries = sum(sum(v.values()) for v in valuation_vectors.values())
nonzero_component_entries = sum(
    sum(1 for x in vals.values() if x != 0)
    for vals in component_exceptional_valuations.values()
)

cert = {
    "schema": "STAGE33_11_A2_26_DIRECT_EXCEPTIONAL_VALUATIONS_V1",
    "stage": "33-11",
    "branch": "33-11c_A2_26_DIRECT_BLOWUP_EXCEPTIONAL_VALUATIONS",
    "source_direction": SOURCE,
    "source_locks": {
        "explicit_gersten_preimage_sha256": pre["canonical_sha256"],
        "exceptional_coordinate_source_sha256": nodes.get("canonical_sha256"),
    },
    "method": {
        "local_model": "blow-up of each frozen ordinary double point",
        "linear_form_exceptional_valuation_rule": "v_E(l)=1 iff l(node)=0, else 0",
        "coefficient_field": "Q(i)",
        "arithmetic": "exact Fraction pairs",
        "node_count": 48,
        "ambient_factor_count": len(forms),
    },
    "node_galois_action": {
        "cc": cc_node,
        "ct": ct_node,
    },
    "factor_exceptional_valuation_vectors": valuation_vectors,
    "component_exceptional_valuation_vectors": component_exceptional_valuations,
    "equivariance_checks": {
        "factor_level": equivariance_checks,
        "component_level": component_checks,
    },
    "summary": {
        "nonzero_factor_exceptional_valuation_entries": nonzero_factor_entries,
        "nonzero_component_exceptional_valuation_entries": nonzero_component_entries,
        "all_factor_vectors_cc_ct_equivariant": True,
        "all_component_vectors_cc_ct_equivariant": True,
        "exceptional_locus_galois_difference_before_purity_correction": "ZERO_EXACT",
    },
    "main_working_bridge": {
        "five_bit_vector_under_q_defined_v4_fixed_purity_pin": [0, 0, 0, 0, 0],
        "five_bit_vector_status": "MAIN_WORKING_PENDING_OFFBOUNDARY_PURITY_AUDIT",
        "explicit_gersten_difference_preimage_working_value": "ZERO",
    },
    "audit_debt": {
        "required": True,
        "unresolved": "strict-transform/off-boundary height-one prime decomposition and legitimacy of a Q-defined/V4-fixed purity correction",
        "this_leaf_does_not_claim": [
            "global Gersten purity correction classified",
            "A2_26 exact connecting column closed",
            "Stage33-11 exact closure",
        ],
    },
    "firewalls": {
        "stage33_11_closed_exact": False,
        "stage33_12_released": False,
        "stage33_08_released": False,
        "stage33_07_closed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "source": SOURCE,
    "node_count": 48,
    "ambient_factor_count": len(forms),
    "exceptional_locus_difference": "ZERO_EXACT",
    "five_bit_main_working": [0, 0, 0, 0, 0],
    "audit_debt": True,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
