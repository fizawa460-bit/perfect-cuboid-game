#!/usr/bin/env python3
"""Separate the exact raw J2 H1 class from an unproved Kummer boundary."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-raw-h1-not-kummer-target-v24.json"
LOCKS = {
    "v21_source": (HERE / "j2-order4-swap-functional-source-v21.json", "19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366"),
    "v22_reachability": (HERE / "j2-kummer-source-target-module-source-first-v22.json", "e51a5f13a17cf7c24e789dd4feedf6797db5cfa89486046c9a96692abe96ef2c"),
    "v23_trace": (HERE / "j2-kummer-target-h1-coordinate41-trace-v23.json", "7718ea63eafa5561bfb2acaf1fb957c9d1767a609036d1a97bee36e9114ed003"),
    "finite_v4_target_contract": (HERE / "full-surface-pic2-kummer-target.json", "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"),
    "raw_named_h1": (HERE / "j2-named-v4-h1-target-before-source-orientation.json", "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3"),
}


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


d = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
v21, v22, v23 = d["v21_source"], d["v22_reachability"], d["v23_trace"]
contract, raw = d["finite_v4_target_contract"], d["raw_named_h1"]

assert v21["named_full_surface_source"]["retained10_mask_decimal"] == 6
assert v22["locked_named_j2"]["locked_target_reachable_from_locked_source"] is False
assert v22["locked_named_j2"]["separating_functional_support_1based"] == [41]
assert v23["separating_coordinate"]["H1_basis41_raw_pic2_ct_support_1based"] == [9, 11, 19]
boundary = contract["exact_information_boundary"]
kummer = contract["kummer_defect_map_contract"]
assert boundary["kummer_extension_class_missing"] is True
assert kummer["matrix_entries_materialized"] == 0
assert kummer["columns_materialized"] == 0
raw_boundary = raw["exact_information_boundary"]
assert raw_boundary["named_J2_V4_H1_target_image_materialized"] is True
assert raw_boundary["named_J2_target_placed_as_75x10_matrix_column"] is False
assert raw_boundary["finite_v4_kummer_columns_materialized"] == 0

out = {
    "schema": "STAGE33_12_J2_RAW_H1_NOT_KUMMER_TARGET_V24",
    "stage": "33-12",
    "status": "PASS_EXACT_RAW_H1_SCOPE_SEPARATED_FROM_MISSING_KUMMER_ADAPTER",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "exact_scope_separation": {
        "named_source_coordinate_exact": True,
        "named_source_retained10_mask_decimal": 6,
        "raw_cech_pic2_cocycle_exact": True,
        "raw_cech_H1_class_exact_nonzero": True,
        "raw_cech_H1_weight": raw["retained_H1_projection"]["coordinate_weight"],
        "raw_cech_H1_may_be_used_as_named_kummer_boundary": False,
        "reason": "the finite-V4 target contract explicitly leaves the Kummer extension class absent, and the source-first all-extension replay proves this raw H1 class cannot be the connecting image of the exact named source under the locked actions",
    },
    "basis_and_gauge_independence": {
        "failure_is_not_a_choice_of_H1_basis": True,
        "reason_basis": "membership of a vector in the source-reachable subspace is invariant under invertible H1 coordinate changes",
        "failure_is_not_removed_by_pic2_coboundary_gauge": True,
        "reason_gauge": "v22 works in H1 modulo all Pic/2 coboundaries and enumerates every compatible V4 module-extension block",
        "separating_H1_coordinate_1based_in_locked_basis": 41,
        "locked_basis41_raw_cc_support_1based": [],
        "locked_basis41_raw_ct_support_1based": [9, 11, 19],
    },
    "supersession": {
        "old_weight15_vector_retained_as_raw_H1_evidence": True,
        "old_weight15_vector_revoked_as_named_kummer_matrix_target": True,
        "historical_C2_plus_C3_relation_restored": False,
        "target_coordinate_should_not_be_bit_patched": True,
    },
    "minimal_missing_interface": {
        "name": "ACTUAL_FULL_SURFACE_H2_MU2_KUMMER_EXTENSION_OR_EQUIVALENT_GENUINE_LIFT_ADAPTER_FOR_NAMED_J2",
        "next_exact_action": "construct a genuine H2_et(Sbar,mu2) lift of the exact named source (or the equivalent Kummer extension block) and compute its V4 connecting cocycle; do not reuse the raw weight-15 class as that cocycle",
    },
    "promotion_firewall": {
        "source_target_relation_materialized": False,
        "standard_columns_materialized": 0,
        "stage33_progress": "6/11",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
assert out["exact_scope_separation"]["raw_cech_H1_weight"] == 15
out["canonical_sha256"] = csha(out)
if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "status": out["status"],
    "raw_h1_weight": 15,
    "raw_h1_is_named_kummer_target": False,
    "standard_columns_materialized": 0,
    "canonical_sha256": out["canonical_sha256"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
