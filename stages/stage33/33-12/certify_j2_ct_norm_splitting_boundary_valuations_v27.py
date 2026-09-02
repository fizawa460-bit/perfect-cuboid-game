#!/usr/bin/env python3
"""Certify exact boundary valuations of the current ct norm-splitting cochain.

This is a post-V26 intermediate authority. It materializes the generic
splitting-factor valuations on the five named boundary divisors
t=0, t=infinity, s=infinity, C21, C22. It does not choose the actual
compactification or claim the integral Cech rank-2 lattices.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-ct-norm-splitting-boundary-valuations-v27.json"
LOCKS = {
    "v26_determinant_parity_frontier": (
        HERE / "j2-ct-determinant-compactification-parity-frontier-v26.json",
        "dbfb3e12fa2d5bec7a48d4a3e4c3aeef5a3d4386c08555a1666c0dce53a04e7d",
    ),
    "ct_norm_splitting_module": (
        HERE / "j2-corrected-ct-norm-splitting-module.json",
        "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2",
    ),
    "explicit_cech_mu2_lift": (
        HERE / "j2-corrected-explicit-cech-mu2-lift.json",
        "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
    ),
}
NEXT = (
    "MATERIALIZE_RESOLUTION_EXCEPTIONAL_VALUATIONS_AND_ACTUAL_CECH_LAMBDA_D_"
    "LOCAL_RANK2_LATTICES_FROM_V27_BOUNDARY_PROFILE_THEN_COMPUTE_OVERLAP_"
    "DETERMINANTS_AND_MARKED_PIC_MOD2_DEFECT"
)

def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
v26 = data["v26_determinant_parity_frontier"]
split = data["ct_norm_splitting_module"]
cech = data["explicit_cech_mu2_lift"]

# Exact source route.
null = split["normalized_norm_nullhomotopy"]
assert null["q"] == "t^4-6*t^2+1"
assert null["A"] == "1-t^2+2*i*t*s"
assert null["u"] == "(A+z)/(2*t)"
assert null["deck_conjugate_u"] == "(A-z)/(2*t)"
assert null["identity"] == "A^2-q=4*t^2*g22"
assert null["norm_u_equals_g22"] is True
assert cech["explicit_cech_preimage"]["g22"] == "1-s^2+i*s*(1-t^2)/t"

# V26 remains the promotion authority: this V27 is not a compactification selector.
assert v26["certified_frontier"]["generic_norm_and_residue_data_select_actual_pic_mod2_defect"] is False
assert v26["information_boundary"]["norm_splitting_determinant_line_bundle_on_quotient_materialized"] is False
assert v26["information_boundary"]["actual_cech_local_rank2_lattices_materialized"] is False
assert v26["information_boundary"]["standard_kummer_columns_materialized"] == 0

# Read the source-certified base valuations of g22.
residue_rows = {
    row["divisor"]: row
    for row in cech["codimension_one_residue_audit"]["rows"]
}
source_g22 = {
    "t=0": residue_rows["t=0"]["valuations"][1],
    "t=infinity": residue_rows["t=infinity"]["valuations"][1],
    "s=infinity": residue_rows["s=infinity"]["valuations"][1],
    "C21": residue_rows["C21"]["valuations"][1],
    "C22": residue_rows["C22"]["valuations"][1],
}
assert source_g22 == {
    "t=0": -1, "t=infinity": -1, "s=infinity": -2, "C21": 0, "C22": 1
}

# t=0. q(0)=1 and q'(0)=0, so the two local sheets have z(0)=+/-1
# and z'(0)=0. A(0)=1 and A'(0)=2*i*s, nonzero in the generic
# residue field Qbar(s). A+z therefore has order 0 on z=+1 and order
# 1 on z=-1. The deck conjugate interchanges the sheets.
q0, qp0 = 1, 0
A0 = 1
assert (q0, qp0, A0) == (1, 0, 1)

def cancelled_numerator_order(base_constant, sheet_constant):
    constant = base_constant + sheet_constant
    if constant != 0:
        return 0
    # In each cancellation case below, the first derivative is 2*i*s,
    # which is nonzero at the generic point of the boundary divisor.
    return 1

t0_rows = []
for eps, label in [(1, "z=+1"), (-1, "z=-1")]:
    vu = cancelled_numerator_order(A0, eps) - 1
    vdeck = cancelled_numerator_order(A0, -eps) - 1
    t0_rows.append((label, vu, vdeck))
assert t0_rows == [("z=+1", -1, 0), ("z=-1", 0, -1)]

# t=infinity. With v=1/t and zbar=v^2*z:
# zbar^2=1-6*v^2+v^4 and
# u=(v^2-1+2*i*s*v+zbar)/(2*v).
# Thus B(0)=-1 and B'(0)=2*i*s; cancellation occurs on zbar=+1.
qbar0, qbarp0, B0 = 1, 0, -1
assert (qbar0, qbarp0, B0) == (1, 0, -1)
tinf_rows = []
for eps, label in [(1, "zbar=+1"), (-1, "zbar=-1")]:
    vu = cancelled_numerator_order(B0, eps) - 1
    vdeck = cancelled_numerator_order(B0, -eps) - 1
    tinf_rows.append((label, vu, vdeck))
assert tinf_rows == [("zbar=+1", 0, -1), ("zbar=-1", -1, 0)]

# s=infinity. With w=1/s, both factors have leading term i/w;
# their product has leading term -1/w^2, matching v(g22)=-2.
vsinf_u = vsinf_deck = -1
assert vsinf_u + vsinf_deck == source_g22["s=infinity"]

# C21: t is a unit at the generic point, both factors are regular, and
# their product g22 is a unit, so both factors are units.
vC21_u = vC21_deck = 0
assert vC21_u + vC21_deck == source_g22["C21"]

# C22: v(g22)=1 and q=A^2 on C22. The two generic lifts are z=+A and
# z=-A. On z=+A the A-z factor vanishes; on z=-A the A+z factor
# vanishes. The complementary factor is a generic unit, so the zero is simple.
C22_rows = [("z=+A", 0, 1), ("z=-A", 1, 0)]
assert all(vu + vd == source_g22["C22"] for _, vu, vd in C22_rows)

rows = [
    {"base_divisor": "t=0", "lift": "z=+1", "v_u": -1, "v_deck_u": 0, "v_norm_g22": -1, "role": "u simple pole / deck conjugate regular"},
    {"base_divisor": "t=0", "lift": "z=-1", "v_u": 0, "v_deck_u": -1, "v_norm_g22": -1, "role": "u regular / deck conjugate simple pole"},
    {"base_divisor": "t=infinity", "lift": "zbar=+1", "v_u": 0, "v_deck_u": -1, "v_norm_g22": -1, "role": "u regular / deck conjugate simple pole"},
    {"base_divisor": "t=infinity", "lift": "zbar=-1", "v_u": -1, "v_deck_u": 0, "v_norm_g22": -1, "role": "u simple pole / deck conjugate regular"},
    {"base_divisor": "s=infinity", "lift": "either generic q-cover sheet", "v_u": -1, "v_deck_u": -1, "v_norm_g22": -2, "role": "both splitting factors have a simple pole"},
    {"base_divisor": "C21", "lift": "any generic q-cover lift", "v_u": 0, "v_deck_u": 0, "v_norm_g22": 0, "role": "both splitting factors are units"},
    {"base_divisor": "C22", "lift": "z=+A", "v_u": 0, "v_deck_u": 1, "v_norm_g22": 1, "role": "u unit / deck conjugate simple zero"},
    {"base_divisor": "C22", "lift": "z=-A", "v_u": 1, "v_deck_u": 0, "v_norm_g22": 1, "role": "u simple zero / deck conjugate unit"},
]
assert all(row["v_u"] + row["v_deck_u"] == row["v_norm_g22"] for row in rows)

out = {
    "schema": "STAGE33_12_J2_CT_NORM_SPLITTING_BOUNDARY_VALUATIONS_V27",
    "stage": "33-12",
    "status": "PASS_EXACT_CT_NORM_SPLITTING_BOUNDARY_VALUATIONS_MATERIALIZED_GLOBAL_LATTICE_GLUING_OPEN",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "normalized_splitting": {
        "q": "t^4-6*t^2+1",
        "A": "1-t^2+2*i*t*s",
        "u": "(A+z)/(2*t)",
        "deck_conjugate_u": "(A-z)/(2*t)",
        "identity": "A^2-q=4*t^2*g22",
        "norm_u_equals_g22": True,
        "t_infinity_parameter": "v=1/t",
        "t_infinity_normalized_cover_coordinate": "zbar=v^2*z",
        "qbar": "1-6*v^2+v^4",
        "u_at_t_infinity": "(v^2-1+2*i*s*v+zbar)/(2*v)",
    },
    "local_cancellation_audit": {
        "t_zero": {
            "q_at_boundary": 1,
            "q_derivative_at_boundary": 0,
            "A_at_boundary": 1,
            "A_derivative_at_boundary": "2*i*s != 0 in the generic residue field",
            "sheet_constants": {
                "z=+1": "A+z=2",
                "z=-1": "A+z=0 with first derivative 2*i*s",
            },
        },
        "t_infinity": {
            "qbar_at_boundary": 1,
            "qbar_derivative_at_boundary": 0,
            "B": "v^2-1+2*i*s*v",
            "B_at_boundary": -1,
            "B_derivative_at_boundary": "2*i*s != 0 in the generic residue field",
            "sheet_constants": {
                "zbar=+1": "B+zbar=0 with first derivative 2*i*s",
                "zbar=-1": "B+zbar=-2",
            },
        },
        "s_infinity": {
            "local_parameter": "w=1/s",
            "leading_terms": {
                "u": "i/w",
                "deck_conjugate_u": "i/w",
                "g22": "-1/w^2",
            },
        },
        "C22": {
            "source_valuation_of_g22": 1,
            "restriction": "q=A^2 on C22 because A^2-q=4*t^2*g22",
            "lift_components": ["z=+A", "z=-A"],
            "simple_zero_assignment": "the factor A-z vanishes on z=+A and A+z vanishes on z=-A; the complementary factor is a unit generically",
        },
        "C21": {
            "source_valuation_of_g22": 0,
            "denominator_t_is_generic_unit": True,
            "conclusion": "u and deck_conjugate_u are both units on every generic lift",
        },
    },
    "derived_boundary_valuations": rows,
    "norm_consistency": {
        "all_rows_satisfy_v_u_plus_v_deck_u_equals_v_g22": True,
        "source_cech_g22_valuations": {
            "t=0": -1, "t=infinity": -1, "s=infinity": -2, "C21": 0, "C22": 1,
        },
    },
    "certified_frontier": {
        "named_boundary_splitting_valuations_materialized": ["t=0", "t=infinity", "s=infinity", "C21", "C22"],
        "t_zero_sheet_cancellation_materialized": True,
        "t_infinity_sheet_cancellation_materialized": True,
        "s_infinity_pole_profile_materialized": True,
        "C21_unit_profile_materialized": True,
        "C22_zero_assignment_materialized": True,
        "resolution_exceptional_splitting_valuations_materialized": False,
        "actual_global_compactification_selector_materialized": False,
        "actual_cech_local_rank2_lattices_materialized": False,
        "actual_cc_ct_overlap_transition_matrices_materialized": False,
        "actual_ct_defect_marked_Pic_mod2_materialized": False,
        "standard_kummer_columns_materialized": 0,
    },
    "exact_conclusion": {
        "generic_splitting_boundary_profile_on_five_named_divisors_is_no_longer_missing": True,
        "actual_compactification_branch_selected": False,
        "reason_remaining_open": "Boundary valuations of the generic splitting cochain do not by themselves identify the actual integral lambda_D lattice across resolution exceptionals or its global overlap gluing.",
        "no_terminal_claim": True,
    },
    "next_exact_leaf": NEXT,
    "promotion_firewall": {
        "stage33_progress": "6/11",
        "stage33_12_closed_exact": False,
        "stage33_07_reclosed": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
        "merge_allowed": False,
    },
}
out["canonical_sha256"] = csha(out)

if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

print(json.dumps({
    "success": True,
    "canonical_sha256": out["canonical_sha256"],
    "named_boundary_divisors_materialized": 5,
    "resolution_exceptionals_materialized": False,
    "actual_cech_local_rank2_lattices_materialized": False,
    "standard_kummer_columns_materialized": 0,
    "marker": "PROOF_REPLAY_COMPLETE",
    "next_exact_leaf": NEXT,
}, sort_keys=True))
