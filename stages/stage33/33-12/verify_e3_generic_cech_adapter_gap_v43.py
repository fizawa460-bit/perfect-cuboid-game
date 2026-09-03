#!/usr/bin/env python3
"""V43: lock the reviewed interface gap between exact e3 proper14 source and a Cech/H2(mu2) lift.

This verifier does not prove nonexistence. It checks only the exact reviewed authority:
V41 fixes e3 at proper14 mask 20, V42 blocks J2 relabelling, the boundary-function
certificate has not materialized a global Gersten Brauer representative, and the
existing explicit Cech symbol remains J2-specific.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOUNDARY = HERE / "boundary-function-generator-source-lock.json"
SCALAR = HERE / "boundary-function-scalar-descent-certificate.json"
V41 = HERE / "e3-independent-proper14-source-v41.json"
V42 = HERE / "e3-v25-transfer-obstruction-v42.json"
J2_CECH = HERE / "j2-corrected-explicit-cech-mu2-lift.json"
OUT = HERE / "e3-generic-cech-adapter-gap-v43.json"

LOCKS = {
    BOUNDARY: "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
    V41: "04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6",
    V42: "b51985a55899c693513959074fa08171b7537d1793fb1372b9dc54facf8f675e",
    J2_CECH: "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
    OUT: "fee50c021723c17984d81514a301b64d981079d9d344fa7a2fce9125c47d7eed",
}


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


boundary = locked(BOUNDARY)
scalar = locked(SCALAR)
v41 = locked(V41)
v42 = locked(V42)
j2 = locked(J2_CECH)
out = locked(OUT)

assert boundary["schema"] == "STAGE33_12_BOUNDARY_FUNCTION_GENERATOR_SOURCE_LOCK_V1"
assert v41["e3_source"]["retained10_standard_mask_decimal"] == 4
assert v41["e3_source"]["proper14_mask_decimal"] == 20
assert v41["e3_source"]["proper14_coordinate_f2"] == [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert v41["construction_boundary"]["genuine_full_surface_h2_mu2_lift_materialized"] is False

assert v42["exact_comparison"]["e3_proper14_mask_decimal"] == 20
assert v42["exact_comparison"]["v25_j2_proper14_mask_decimal"] == 25
assert v42["construction_result"]["v25_adapter_relabelled_as_e3"] is False

assert scalar["exact_conclusion"]["all_14_generator_boundary_function_packages_recovered_with_occurrence_scalars"] is True
assert scalar["exact_conclusion"]["boundary_function_constant_correction_zero_on_all_14_generators"] is True
assert scalar["exact_conclusion"]["other_global_gersten_or_hs_coupling_ruled_out"] is False
assert scalar["promotion_firewall"]["global_gersten_brauer_representatives_materialized"] == 0
assert scalar["next_exact_leaf"] == "USE_THE_FINITE_QI_SCALAR_TABLE_IN_A_GLOBAL_GERSTEN_2COCHAIN_OR_PROVE_IT_LANDS_IN_THE_CONSTANT_COKERNEL_ADAPTER"

assert j2["explicit_cech_preimage"]["class"] == "e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)"
assert j2["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
assert j2["surface_mu2_lift"]["brauer_image"] == "corrected nonzero J2=(f2,1)"

assert out["exact_e3_target"]["retained10_standard_mask_decimal"] == 4
assert out["exact_e3_target"]["proper14_mask_decimal"] == 20
assert out["exact_e3_target"]["proper14_support_one_based"] == [3, 5]
assert out["adapter_gap"]["exact_reusable_proper14_to_cech_or_surface_h2_mu2_adapter_materialized"] is False
assert out["adapter_gap"]["boundary_function_data_promoted_to_e3_cech_without_bridge"] is False
assert out["adapter_gap"]["j2_specific_symbol_relabelled_as_e3"] is False
assert out["adapter_gap"]["global_nonexistence_claimed"] is False
assert out["promotion_firewall"]["stage33_12_closed_exact"] is False
assert out["promotion_firewall"]["merge_allowed"] is False

print(json.dumps({
    "success": True,
    "e3": {"retained10_mask": 4, "proper14_mask": 20, "support": [3, 5]},
    "global_gersten_brauer_representatives_materialized": 0,
    "generic_e3_cech_adapter_materialized": False,
    "global_nonexistence_claimed": False,
    "next_exact_leaf": out["next_exact_leaf"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
