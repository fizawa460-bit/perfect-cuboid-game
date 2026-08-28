#!/usr/bin/env python3
"""Certify the visible A2_26 ambient boundary package is V4-invariant.

This deliberately does not promote the boundary package to a global Gersten
lift.  It isolates the remaining five-bit input: any cc/ct defect must come
from the off-boundary purity correction used to turn the package into a global
lift, not from its four explicit boundary rational functions.
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
FIRST = S07 / "order2-first-residue-function-liftability.json"
OUT = HERE / "stage33-11-a2-26-ambient-boundary-galois.json"

LOCKS = {
    SIDE.name: "2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d",
    EXC.name: "a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397",
    FIRST.name: "85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    if claimed != LOCKS[path.name] or csha(body) != LOCKS[path.name]:
        raise SystemExit(f"source lock moved: {path.name}")
    return obj


def qi(z):
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def conj_vec(raw):
    return [(a, -b) for a, b in map(qi, raw)]


def vec(raw):
    return list(map(qi, raw))


def projective(v):
    pivot = next((x for x in v if x != (0, 0)), None)
    if pivot is None:
        raise SystemExit("zero linear form")
    a, b = pivot; den = a*a + b*b
    inv = (a/den, -b/den)
    return tuple((x*inv[0]-y*inv[1], x*inv[1]+y*inv[0]) for x, y in v)


side, exc, first = map(load, (SIDE, EXC, FIRST))
srow = next(r for r in side["source_ambient_side_lifts"] if r["source_basis_name"] == "A2_26")
erow = next(r for r in exc["source_ambient_exceptional_lifts"] if r["source_basis_name"] == "A2_26")
frow = next(r for r in first["source_basis"] if r["source_basis_name"] == "A2_26")
if frow["raw_order2_first_residue_function_liftable"] is not True:
    raise SystemExit("A2_26 raw-order2 liftability moved")
if [r["component_id"] for r in srow["side_ambient_function_lifts"]] != ["SIDE_021", "SIDE_022"]:
    raise SystemExit("A2_26 side support moved")
if [r["component_id"] for r in erow["exceptional_ambient_tangent_function_lifts"]] != ["EXC_046", "EXC_047"]:
    raise SystemExit("A2_26 exceptional support moved")

# Each side product has the conjugate pair (-i,+i), hence is fixed projectively.
side_checks = []
for row in srow["side_ambient_function_lifts"]:
    forms = [projective(vec(f["ambient_linear_factor_coefficients_L_basis"])) for f in row["numerator_factors"]]
    cforms = [projective(conj_vec(f["ambient_linear_factor_coefficients_L_basis"])) for f in row["numerator_factors"]]
    if sorted(forms) != sorted(cforms) or any(b for _, b in map(qi, row["D_coefficients_L_basis"])):
        raise SystemExit(f"{row['component_id']}: cc invariance failed")
    side_checks.append(row["component_id"])

# cc exchanges EXC_046 and EXC_047; numerator and denominator forms match
# projectively after conjugation.  sqrt(2)-conjugation fixes every Q(i) entry.
e46, e47 = erow["exceptional_ambient_tangent_function_lifts"]
for key in ("numerator_factors",):
    a = sorted(projective(conj_vec(f["ambient_tangent_linear_factor_coefficients_L_basis"])) for f in e46[key])
    b = sorted(projective(vec(f["ambient_tangent_linear_factor_coefficients_L_basis"])) for f in e47[key])
    if a != b:
        raise SystemExit("EXC_046/047 conjugate numerator match failed")
for idx in (0, 1):
    if projective(conj_vec(e46["ambient_projection_R0_R1_coefficients_L_basis"][idx])) != projective(vec(e47["ambient_projection_R0_R1_coefficients_L_basis"][idx])):
        raise SystemExit("EXC_046/047 conjugate projection match failed")

cert = {
    "schema": "STAGE33_11_A2_26_AMBIENT_BOUNDARY_GALOIS_V1",
    "stage": "33-11",
    "branch": "33-11c_A2_26_EXPLICIT_CC_CT_GERSTEN_DIFFERENCE_BITS",
    "source_locks": {k: v for k, v in LOCKS.items()},
    "source_direction": "A2_26",
    "support": ["SIDE_021", "SIDE_022", "EXC_046", "EXC_047"],
    "exact_checks": {
        "side_021_and_022_numerator_factor_multisets_cc_fixed": True,
        "side_denominators_defined_over_Q": True,
        "cc_exchanges_exceptional_046_047_packages_projectively": True,
        "ct_fixes_all_Qi_coefficients": True,
        "explicit_ambient_boundary_package_v4_fixed": True,
    },
    "exact_consequence": {
        "visible_boundary_package_contributes_nonzero_cc_ct_difference_bits": False,
        "remaining_five_bits_are_entirely_offboundary_purity_correction_data": True,
        "global_gersten_lift_selected": False,
        "a2_26_connecting_column_materialized": False,
        "connecting_columns_materialized": 0,
        "next_exact_task": "A2_26_SELECT_OR_CLASSIFY_V4_ACTION_ON_OFFBOUNDARY_PURITY_CORRECTION",
    },
    "firewalls": {
        "boundary_function_package_is_global_gersten_lift": False,
        "stage33_11_closed": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"success": True, "certificate_sha256": cert["canonical_sha256"], "connecting_columns": "0/26", "next": cert["exact_consequence"]["next_exact_task"]}, indent=2, sort_keys=True))
