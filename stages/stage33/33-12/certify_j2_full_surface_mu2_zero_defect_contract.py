#!/usr/bin/env python3
"""Current corrected-J2 surface-mu2 / HS-d2 boundary contract.

The corrected symbol lift and its generic cc/ct splittings are exact.  The
ct norm splitting module is now explicit, including the even determinant of
its standard auxiliary q-cover compactification and an exact witness that
generic splitting data do not select the actual compactification parity.
Actual local Cech lattices, Pic/2 defect, integral Pic lifts, and HS d2 remain
open.  No retired arithmetic representative or Kummer glue is consumed.
"""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
PRE = S33 / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json"
FAIL = S33 / "33-05" / "j2-post-r5-hs-descent-datum.json"
EXPLICIT = HERE / "j2-corrected-explicit-cech-mu2-lift.json"
SPLIT = HERE / "j2-corrected-ct-norm-splitting-module.json"
OUT = HERE / "j2-full-surface-mu2-zero-defect-contract.json"

EXPECTED_PRE = "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106"
EXPECTED_FAIL = "a7c08372b9ef012a1446bd3bf4f40541d77d372dadc73e3780f6ce2529fcc6d8"
EXPECTED_EXPLICIT = "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"
EXPECTED_SPLIT = "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical source lock moved: {path}")
    return obj


pre = load_canonical(PRE, EXPECTED_PRE)
fail = load_canonical(FAIL, EXPECTED_FAIL)
explicit = load_canonical(EXPLICIT, EXPECTED_EXPLICIT)
split = load_canonical(SPLIT, EXPECTED_SPLIT)
assert pre["audit_boundary"]["HS_d2_2cocycle_materialized"] is False
assert fail["audit_failure"]["HS_d2_2cocycle_materialized"] is False
assert explicit["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"]
assert split["standard_auxiliary_q_cover_compactification"]["determinant_mod2"] == "0"
assert split["exact_nonuniqueness_witness"]["pullback_difference_nonzero_mod2"]

next_leaf = split["next_exact_leaf"]
certificate = {
    "schema": "STAGE33_12_J2_FULL_SURFACE_MU2_ZERO_DEFECT_CONTRACT_V5_CT_NORM_SPLITTING_MODULE_AMBIGUITY",
    "status": "OPEN_EXPLICIT_SURFACE_MU2_LIFT_AND_CT_SPLITTING_MODULE_MATERIALIZED_ACTUAL_CECH_LATTICE_PIC_MOD2_AND_HS_D2_UNPROVEN",
    "source_locks": {
        "corrected_pre_kummer_certificate": "stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json",
        "corrected_pre_kummer_canonical_sha256": EXPECTED_PRE,
        "post_r5_fail_certificate": "stages/stage33/33-05/j2-post-r5-hs-descent-datum.json",
        "post_r5_fail_canonical_sha256": EXPECTED_FAIL,
        "explicit_cech_mu2_lift_certificate": "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
        "explicit_cech_mu2_lift_canonical_sha256": EXPECTED_EXPLICIT,
        "ct_norm_splitting_module_certificate": "stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json",
        "ct_norm_splitting_module_canonical_sha256": EXPECTED_SPLIT,
    },
    "exact_input": {
        "class": "corrected geometric J2=(f2,1)",
        "named_geometric_representative_certified": True,
        "marked_brauer_coordinate": [1, 0],
        "normalization_half_divisor": "D=P_r2-P_r4",
        "normalization_half_divisor_descent_cochain_materialized": True,
        "full_split_pair_representative_witnesses_materialized": True,
    },
    "kummer_exact_sequence": {
        "sequence": "Pic(Kc_bar)/2 -> H^2_et(Kc_bar,mu_2) -> Br(Kc_bar)[2] -> 0",
        "explicit_Cech_preimage_e_D_materialized": True,
        "full_surface_mu2_lift_for_corrected_J2_materialized": True,
        "normalization_to_surface_Kummer_adapter_materialized": True,
        "generic_galois_defect_splittings_materialized": True,
        "ct_norm_generic_rank2_splitting_matrices_materialized": True,
        "ct_norm_standard_auxiliary_q_cover_determinant_mod2_zero": True,
        "ct_norm_compactification_parity_ambiguity_materialized": True,
        "actual_lambda_D_local_rank2_lattices_materialized": False,
        "pic_mod2_integral_coordinates_materialized": False,
        "reason": "The standard auxiliary q-cover module has even determinant, but an elementary transform preserves the generic splitting data and changes parity by a nonzero marked Kc fiber. The actual local Cech lattices and overlap transitions must be materialized before assigning the defect.",
    },
    "defect_state": {
        "pic_mod2_defect_1cocycle_materialized": False,
        "integral_Pic_lift_materialized": False,
        "HS_d2_2cocycle_materialized": False,
        "HS_d2_zero_proved": False,
        "finite_V4_zero_credit": False,
        "absolute_zero_credit": False,
    },
    "retired_historical_credit": {
        "old_Q_defined_ell_J2_may_be_used": False,
        "historical_delta_Kum_V4_EXACT_ZERO_revoked": True,
        "historical_named_kummer_glue_producer_tombstoned": True,
    },
    "next_exact_leaf": next_leaf,
    "promotion_firewall": {
        "Q_defined_descent_credit_restored": False,
        "arithmetic_hs_d2_computed": False,
        "stage33_05_reclosed": False,
        "stage33_12_closed": False,
        "stage33_13_released": False,
        "stage33_progress": "5/11",
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
certificate["canonical_sha256"] = csha(certificate)
OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "status": certificate["status"],
    "surface_mu2_lift_materialized": True,
    "actual_pic_mod2_defect_materialized": False,
    "canonical_sha256": certificate["canonical_sha256"],
    "next_exact_leaf": next_leaf,
}, indent=2, sort_keys=True))
