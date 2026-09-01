#!/usr/bin/env python3
"""Materialize a compact certificate from the all-extension reachability audit."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIT = HERE / "audit_v4_kummer_extension_space_after_j2_anchor.py"
OUT = HERE / "j2-kummer-source-target-module-compatibility-audit.json"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def recompute() -> dict:
    proc = subprocess.run(
        [sys.executable, str(AUDIT)],
        cwd=HERE,
        check=True,
        capture_output=True,
        text=True,
    )
    raw = json.loads(proc.stdout.strip().splitlines()[-1])
    assert raw["success"] is True
    assert raw["schema"] == "STAGE33_12_V4_KUMMER_EXTENSION_REACHABILITY_AUDIT_V2"
    assert raw["extension_solution_space"] == {
        "variables_phi_cc_phi_ct": 1792,
        "equations": 2688,
        "rank_f2": 781,
        "nullity_f2": 1011,
        "zero_extension_present": True,
    }
    j2 = raw["locked_named_j2"]
    assert j2["proper14_f2"] == [1,0,0,1,1,0,0,0,0,0,0,0,0,0]
    assert j2["retained10_support_1based"] == [2,3]
    assert j2["target_75D_weight"] == 15
    assert j2["reachable_H1_subspace_dimension_f2"] == 13
    assert j2["locked_target_reachable_from_locked_source"] is False

    reach = raw["target_reachability_over_all_nonzero_retained_sources"]
    compatible = [int(x) for x in reach["compatible_source_masks_decimal"]]
    incompatible = sorted(set(range(1, 1 << 10)) - set(compatible))
    assert len(compatible) == 1000
    assert len(incompatible) == 23
    assert 6 in incompatible
    assert reach["locked_j2_source_mask_decimal"] == 6
    assert reach["locked_j2_source_is_compatible"] is False

    def support(mask: int) -> list[int]:
        return [i + 1 for i in range(10) if (mask >> i) & 1]

    cert = {
        "schema": "STAGE33_12_J2_KUMMER_SOURCE_TARGET_MODULE_COMPATIBILITY_AUDIT_V1",
        "stage": "33-12",
        "status": "FAIL_EXACT_LOCKED_J2_SOURCE_TARGET_MODULE_COMPATIBILITY",
        "source_locks": raw["source_locks"],
        "all_v4_module_extensions_audit": {
            "scope": raw["scope"],
            "variables_phi_cc_phi_ct": 1792,
            "equations": 2688,
            "rank_f2": 781,
            "nullity_f2": 1011,
            "zero_extension_present": True,
        },
        "locked_named_j2": {
            "proper_Br2_14D_coordinate_f2": j2["proper14_f2"],
            "retained_10D_support_1based": [2,3],
            "retained_10D_mask_decimal": 6,
            "locked_75D_target_weight": 15,
            "reachable_H1_subspace_dimension_f2": 13,
            "locked_75D_target_reachable_from_locked_source": False,
        },
        "diagnostic": {
            "nonzero_retained_sources_total": 1023,
            "sources_for_which_locked_target_is_reachable": 1000,
            "sources_for_which_locked_target_is_not_reachable": 23,
            "incompatible_source_masks_decimal": incompatible,
            "incompatible_source_supports_1based": [support(mask) for mask in incompatible],
            "meaning": "the locked target is not globally impossible; the incompatibility is specific to a 23-element source subset containing the currently locked J2 source",
        },
        "consequence": {
            "old_relation_certificate": "stages/stage33/33-12/j2-named-kummer-source-target-relation.json",
            "old_relation_equation": "C2 + C3 = h_J2",
            "old_relation_may_be_used_as_kummer_matrix_relation": False,
            "named_source_target_relation_rank_credit_after_this_audit": 0,
            "standard_columns_materialized_after_this_audit": 0,
            "repair_target": "identify the exact coordinate/semantic adapter that makes the independently exact J2 proper-Br2 source and independently exact raw/75D J2 target live in one Kummer V4-module extension",
        },
        "promotion_firewall": {
            "J2_source_certificate_revoked": False,
            "J2_target_certificate_revoked": False,
            "only_source_target_binding_revoked": True,
            "Q_defined_descent_credit_added": False,
            "actual_geometric_extension_identified": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = recompute()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "status": cert["status"],
        "incompatible_source_count": cert["diagnostic"]["sources_for_which_locked_target_is_not_reachable"],
        "J2_relation_rank_after_audit": cert["consequence"]["named_source_target_relation_rank_credit_after_this_audit"],
        "canonical_sha256": cert["canonical_sha256"],
        "wrote": args.write,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
