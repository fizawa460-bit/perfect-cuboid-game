#!/usr/bin/env python3
"""Network-free hostile replay of the corrected-J2 actual cc overlap."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-cc-actual-cech-global-square-overlap.json"
AUDIT = HERE / "first-exact-kummer-column-support-reduction-audit.json"
CONTROLLER = HERE.parent / "controller.json"
EXPECTED = "82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd"
AUDIT_SHA = "c636334f719780c461817c37ae772f013292e8d2830548066b4fa402d6dde064"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


def add(left, right):
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = answer.get(monomial, 0) + coefficient
        if answer[monomial] == 0:
            del answer[monomial]
    return answer


def scale(coefficient, polynomial):
    return {monomial: coefficient * value for monomial, value in polynomial.items()}


def multiply(left, right):
    answer = {}
    for (lt, ls), lc in left.items():
        for (rt, rs), rc in right.items():
            monomial = (lt + rt, ls + rs)
            answer[monomial] = answer.get(monomial, 0) + lc * rc
    return {monomial: coefficient for monomial, coefficient in answer.items() if coefficient}


cert = locked(CERT, EXPECTED)
audit = locked(AUDIT, AUDIT_SHA)
controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
assert cert["schema"] == "STAGE33_12_J2_CC_ACTUAL_CECH_GLOBAL_SQUARE_OVERLAP_V1"
assert cert["source_locks"] == {
    "corrected_explicit_cech_mu2_lift_sha256": "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
    "corrected_branch_surface_mu2_adapter_sha256": "edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875",
    "ct_six_fullPic64_pullbacks_sha256": "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d",
}

# Independently replay g21*g22=(A2^2+A3^2)/(4t^2).
a = {(0, 0): 1, (0, 2): -1}
b = {(-1, 1): 1, (1, 1): -1}
assert multiply(add(a, scale(-1j, b)), add(a, scale(1j, b))) == add(
    multiply(a, a), multiply(b, b)
)

# Independently replay diag(c,1) Y diag(c^-1,1)=J entry by entry.
def cpow_product(left, right):
    if left is None or right is None:
        return None
    return left + right


def matrix_product(left, right):
    answer = []
    for row in range(2):
        output_row = []
        for column in range(2):
            terms = [cpow_product(left[row][k], right[k][column]) for k in range(2)]
            nonzero = [term for term in terms if term is not None]
            assert len(nonzero) <= 1
            output_row.append(nonzero[0] if nonzero else None)
        answer.append(tuple(output_row))
    return tuple(answer)


Y = ((None, 1), (1, None))
G = ((1, None), (None, 0))
Ginv = ((-1, None), (None, 0))
J = ((None, 2), (0, None))
assert matrix_product(matrix_product(G, Y), Ginv) == J
assert cert["actual_rank2_cech_overlap"]["determinant"] == "det(G)=c"
assembly = cert["cartier_divisor_assembly"]
assert assembly["all_resolution_exceptionals_covered"]
assert assembly["determinant_divisor"] == "sum_D ord_D(c)*D=div(c)"
assert assembly["determinant_divisor_principal"]
assert assembly["picard_class_integral"] == "[div(c)]=0 in Pic(Kc_bar)"
assert cert["actual_cc_defect"]["marked_semantic_PicK_mod2_coordinates"] == [0] * 20
assert cert["actual_cc_defect"]["full_surface_Pic64_INDLIST_mod2_coordinates"] == [0] * 64
assert cert["actual_cc_defect"]["full_surface_Pic64_historical_Magma_mod2_coordinates"] == [0] * 64
assert cert["actual_cc_defect"]["zero_proved_not_guessed"]
assert cert["fixed_corrected_lift"]["old_ell_Q_used"] is False
assert cert["fixed_corrected_lift"]["historical_kummer_glue_used"] is False
assert not any(cert["promotion_firewall"].values())

assert audit["exact_progress"]["cc_actual_cech_overlap_canonical_sha256"] == EXPECTED
assert audit["cc_actual_cech_result"]["actual_marked_Pic2_cc_defect_zero"]
assert audit["next_exact_leaf"] == controller["current"]["next_exact_leaf"]
assert controller["current"]["active_missing_interface"] == "NAMED_CV_d2_TO_SEMANTIC_DISCRIMINANT_ORIENTATION"
state = controller["stage33_12"]
assert state["j2_support_reduction_audit_sha256"] == AUDIT_SHA
assert state["corrected_J2_cc_actual_cech_certificate_sha256"] == EXPECTED
assert state["corrected_J2_cc_defect_integral_Pic_class_zero"]
assert state["corrected_J2_named_semantic_discriminant_orientation_materialized"] is False
assert state["finite_v4_kummer_columns_materialized"] == 0
assert state["first_exact_kummer_column_materialized"] is False
assert controller["release_gates"]["stage33_12_closed_exact"] is False
assert controller["release_gates"]["stage33_07_reclosed"] is False
assert controller["release_gates"]["stage33_08_released"] is False
assert controller["theorem_credit"] is False
assert controller["receiver_credit"] is False
assert controller["endpoint_credit"] is False

print(json.dumps({
    "success": True,
    "certificate_sha256": EXPECTED,
    "actual_cc_integral_pic_class_zero": True,
    "remaining_interface": cert["remaining_interface"],
    "first_exact_75D_kummer_column_materialized": False,
}, sort_keys=True))
