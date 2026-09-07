#!/usr/bin/env python3
"""V91C1X_R1 fail-closed preflight for the swap23 Kummer action-difference bridge.

This diagnostic deliberately separates three layers:

1. the literal A2_02 boundary-function package transport under swap23;
2. the retained Cartier/Picard-2 action-difference class from V91C1W;
3. the missing chain-level mu_2 2-cocycle (or equivalent unimodular Cech glue)
   needed to identify g(seed)-seed with the Kummer boundary of that Cartier
   class.

Package closure, scalar-one transport, and Pic/2 zero are not promoted to H^2
fixedness.  A positive semantic bridge requires an actual source-bound
chain-level comparison on the same literal A2_02 representative.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
W = HERE / "e3-v91c1w-a2-02-all8-picard64-reduction.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
R = HERE / "diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py"
OUT = HERE / "e3-v91c1x-r1-chain-level-action-difference-preflight.json"

D_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
W_SHA = "e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7"
TARGET_SHA = "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"
ENTRY_MAIN = "652cbd51cd6b546f2a178597f7f2d3474c92b1c6"
REPAIR_MERGE = "d620871bcadc0fe92af8e44e541fcb4c20197349"
FAIL_HEAD = "3d96e40705995e6355c9570c2fe9e6eeddad8353"
FAIL_REVIEW = 5127167940


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    d = load(D, D_SHA)
    w = load(W, W_SHA)
    target = load(TARGET, TARGET_SHA)
    rns = runpy.run_path(str(R))
    r = rns["result"]

    assert r["success"] is True
    assert r["marker"] == "V91C1R_SWAP23_LITERAL_BOUNDARY_FUNCTION_PACKAGE_TRANSPORT_DIAGNOSTIC"
    assert r["q_word"] == ["swap12", "swap13", "swap12"]
    assert r["composed_coordinate_permutation"] == [0, 2, 1, 3, 5, 4, 6]
    assert d["a2_02_literal_seed"]["source_direction"] == "A2_02"
    assert d["a2_02_literal_seed"]["raw_order"] == 2
    assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
    assert d["exact_consequence"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False
    assert w["exact_result"]["complete_swap23_difference_zero_mod2"] is True
    assert w["exact_result"]["complete_swap23_difference_mod2_support_one_based"] == []
    assert w["exact_consequence"]["a2_02_swap23_seed_fixed_mod_pic2_promoted"] is False
    assert target["exact_information_boundary"]["kummer_extension_class_missing"] is True

    package_level_literal_closure = bool(
        r["every_acted_package_has_unique_original_a2_02_divisor_candidate"]
        and r["all_candidate_function_scalar_ratios_one"]
        and r["literal_package_action_is_permutation_of_same_eight"]
    )

    cert = {
        "schema": "stage33.e3.v91c1x_r1.chain_level_action_difference_preflight.v1",
        "stage": "33-12",
        "role": "EXACT_NONCREDIT_SWAP23_CHAIN_LEVEL_KUMMER_ACTION_DIFFERENCE_PREFLIGHT",
        "entry_boundary": {
            "branch_base_main": ENTRY_MAIN,
            "hostile_audit_repair_merge": REPAIR_MERGE,
            "failed_candidate_head": FAIL_HEAD,
            "failed_hostile_audit_review": FAIL_REVIEW,
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "a2_02_cech_cartier_assembly_sha256": D_SHA,
            "v91c1w_complete_swap23_pic2_zero_sha256": W_SHA,
            "full_surface_pic2_kummer_target_sha256": TARGET_SHA,
            "swap23_literal_package_transport": "stages/stage33/33-12/diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py",
        },
        "swap23_package_level": {
            "every_acted_package_has_original_a2_02_divisor_candidate": bool(r["every_acted_package_has_original_a2_02_divisor_candidate"]),
            "every_acted_package_has_unique_original_a2_02_divisor_candidate": bool(r["every_acted_package_has_unique_original_a2_02_divisor_candidate"]),
            "all_candidate_function_scalar_ratios_one": bool(r["all_candidate_function_scalar_ratios_one"]),
            "literal_package_action_is_identity": bool(r["literal_package_action_is_identity"]),
            "literal_package_action_is_permutation_of_same_eight": bool(r["literal_package_action_is_permutation_of_same_eight"]),
            "package_level_literal_closure": package_level_literal_closure,
        },
        "retained_pic2_layer": {
            "complete_swap23_difference_zero_in_retained_picard_mod2": True,
            "complete_swap23_difference_mod2_support_one_based": [],
        },
        "chain_level_h2_interface": {
            "d_cech_cartier_seed_assembly_materialized": True,
            "d_genuine_full_surface_h2_mu2_lift_for_e3": False,
            "full_surface_kummer_extension_class_missing": True,
            "locked_interface_exposes_literal_mu2_2_cocycle": False,
            "locked_interface_exposes_equivalent_unimodular_cech_glue": False,
            "actual_swap23_gm_1_cochain_comparison_materialized": False,
            "chain_level_identity_g_seed_minus_seed_equals_delta_Lg_verifiable": False,
        },
        "semantic_bridge": {
            "swap23_h2_seed_fixedness_credit": False,
            "mask20_exclusion_credit": False,
            "status": "BLOCKED_MISSING_LITERAL_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_DATUM",
            "next_missing_object": "SOURCE_BOUND_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_DATUM_WITH_SWAP23_ACTION_AND_GM_1_COCHAIN_COMPARISON",
            "next_exact_leaf": "V91C1X_R2_MATERIALIZE_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_THEN_COMPARE_SWAP23_ACTION_DIFFERENCE",
        },
        "anti_inference": {
            "package_level_closure_promoted_to_h2_fixedness": False,
            "pic2_zero_promoted_to_h2_fixedness": False,
            "kummer_exactness_or_functoriality_used_as_chain_witness": False,
            "brauer_image_fixedness_used_to_prove_bridge": False,
            "j2_global_square_cochain_relabelled_as_a2_02_source": False,
            "repository_wide_absence_claim": False,
        },
        "credit_firewall": {
            "swap23_h2_seed_fixedness": False,
            "mask20_exclusion": False,
            "sign_b1_h2_seed_fixedness": False,
            "sign_a2_h2_seed_fixedness": False,
            "source_bound_dim5_credit": False,
            "marked_brauer_image_computed": False,
            "e3_genuine_full_surface_h2_mu2_lift_materialized": False,
            "e3_kummer_column_materialized": False,
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R1_CHAIN_LEVEL_ACTION_DIFFERENCE_PREFLIGHT_BLOCKED",
        "certificate_sha256": cert["canonical_sha256"],
        "package_level_literal_closure": package_level_literal_closure,
        "unique_a2_02_candidate_each": bool(r["every_acted_package_has_unique_original_a2_02_divisor_candidate"]),
        "all_candidate_function_scalar_ratios_one": bool(r["all_candidate_function_scalar_ratios_one"]),
        "same_eight_permutation": bool(r["literal_package_action_is_permutation_of_same_eight"]),
        "chain_level_identity_verifiable": False,
        "next_exact_leaf": cert["semantic_bridge"]["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
