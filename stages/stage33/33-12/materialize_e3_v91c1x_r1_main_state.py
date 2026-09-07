#!/usr/bin/env python3
"""Promote the exact noncredit V91C1X_R1 negative preflight into MAIN routing.

This changes only the live blocker/working frontier.  It does not promote any
H^2 fixedness, Brauer coordinate, dim-5 subspace, theorem, receiver, endpoint,
or merge credit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
STATE = S33 / "MAIN-STATE.json"
R1 = HERE / "e3-v91c1x-r1-chain-level-action-difference-preflight.json"

OLD_STATE_SHA = "6991e41d18c9e06f4d2d4bedffc8f6ac4fbfd209e93012d7f5a7989d5e599241"
R1_SHA = "b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb"
R1_CANDIDATE = "V91C1X_R1_CHAIN_LEVEL_ACTION_DIFFERENCE_PREFLIGHT_BLOCKED"
NEXT = "V91C1X_R2_MATERIALIZE_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_THEN_COMPARE_SWAP23_ACTION_DIFFERENCE"
MISSING = "SOURCE_BOUND_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_DATUM_WITH_SWAP23_ACTION_AND_GM_1_COCHAIN_COMPARISON"


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

    s = load(STATE, OLD_STATE_SHA)
    r1 = load(R1, R1_SHA)
    assert r1["semantic_bridge"]["status"] == "BLOCKED_MISSING_LITERAL_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_DATUM"
    assert r1["semantic_bridge"]["next_exact_leaf"] == NEXT
    assert r1["semantic_bridge"]["next_missing_object"] == MISSING
    assert r1["swap23_package_level"]["package_level_literal_closure"] is False
    assert r1["swap23_package_level"]["every_acted_package_has_original_a2_02_divisor_candidate"] is False
    assert r1["swap23_package_level"]["all_candidate_function_scalar_ratios_one"] is False
    assert r1["chain_level_h2_interface"]["chain_level_identity_g_seed_minus_seed_equals_delta_Lg_verifiable"] is False

    s["schema"] = "STAGE33_MAIN_COMPACT_STATE_V49_V91C1X_R1_CHAIN_LEVEL_PREFLIGHT_BLOCKED_R2_LITERAL_MU2_GLUE"
    s["authority_sync"]["branch_candidate_frontier"] = R1_CANDIDATE
    s["authority_sync"]["status"] = "V91C1V_HOSTILE_REAUDITED_MERGED_V91C1W_RETAINED_V91C1X_R1_EXACT_NEGATIVE_CHAIN_PREFLIGHT"
    s["branch_exact_frontier_candidate"] = "stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json"

    prior = s["candidate_audit_gate"]
    assert prior["pr"] == 1671 and prior["hostile_audit_review"] == 5127167940
    s["prior_failed_candidate_gate"] = prior
    s["candidate_audit_gate"] = {
        "candidate": R1_CANDIDATE,
        "candidate_certificate": "stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json",
        "candidate_certificate_sha256": R1_SHA,
        "pr": 1678,
        "status": "EXACT_NONCREDIT_NEGATIVE_PREFLIGHT_CONTINUATION_ALLOWED",
        "audit_pass_credit": False,
        "merge_allowed": False,
        "parent_retained_candidate": "V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO",
        "parent_retained_candidate_sha256": "e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7",
        "hostile_audit_blocker_review": 5127167940,
        "runtime_materialization_workflow_run": 34073099933,
        "runtime_materialization_trigger_head": "4399e388ba5bb4cae7110f8c744ef797fa361499",
        "runtime_materialized_commit": "2907d655cf37efe04fcae64d665d48184ee286bf",
    }

    s["continuation_provenance"]["x_r1_chain_preflight"] = {
        "pr": 1678,
        "certificate_sha256": R1_SHA,
        "package_level_literal_closure": False,
        "same_a2_02_package_candidate_for_every_component": False,
        "all_candidate_function_scalar_ratios_one": False,
        "chain_level_identity_verifiable": False,
        "next_missing_object": MISSING,
    }

    s["current"] = {
        "active_missing_interface": MISSING,
        "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
        "next_exact_leaf": NEXT,
        "substep": "E3_V91C1X_R2_LITERAL_MU2_COCYCLE_OR_UNIMODULAR_CECH_GLUE",
        "unit": "33-12",
    }

    f = s["current_exact_frontier"]
    f["a2_02_swap23_package_level_literal_closure"] = False
    f["a2_02_swap23_every_component_has_original_package_candidate"] = False
    f["a2_02_swap23_all_candidate_function_scalar_ratios_one"] = False
    f["a2_02_literal_mu2_2_cocycle_materialized"] = False
    f["a2_02_equivalent_unimodular_cech_glue_materialized"] = False
    f["a2_02_actual_swap23_gm_1_cochain_comparison_materialized"] = False
    f["a2_02_semantic_action_difference_chain_witness_materialized"] = False
    f["a2_02_semantic_action_difference_verified_automorphisms"] = []
    f["a2_02_semantic_action_difference_blocked_automorphisms"] = ["swap23", "sign_b1", "sign_a2"]
    f["a2_02_swap23_seed_fixed_mod_pic2"] = False
    f["a2_02_marked_brauer_image_excluded_from_mask20"] = False
    f["a2_02_source_bound_stabilizer_fixed_subspace_materialized"] = False
    f["a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2"] = None
    f["a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality"] = None
    f["a2_02_minimal_source_bound_discriminator_positions_one_based"] = []

    s["current_leaf_working_set"] = [
        "docs/research-os/policies/repository-asset-discovery.md",
        "docs/arsenal/index.json",
        "docs/arsenal/cards/provisional/S33-PW04.md",
        "docs/arsenal/cards/provisional/S33-PW07.md",
        "stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json",
        "stages/stage33/33-12/e3-v91c1d-a2-02-purity-cech-cartier-assembly.json",
        "stages/stage33/33-12/full-surface-pic2-kummer-target.json",
        "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
        "stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json"
    ]

    s["locked_facts"]["v91c1x_r1_negative_preflight"] = {"sha256": R1_SHA}
    s["resolved_investigations"]["e3_v91c1x_r1_chain_level_action_difference_preflight"] = (
        "EXACT_NONCREDIT_PACKAGE_LAYER_NOT_CLOSED_AND_LITERAL_MU2_2_COCYCLE_OR_EQUIVALENT_GLUE_MISSING_SEMANTIC_BRIDGE_BLOCKED"
    )
    s["execution_gate"] = {
        "advance_allowed": True,
        "advance_scope": "V91C1X_R2_LITERAL_MU2_2_COCYCLE_OR_EQUIVALENT_CECH_GLUE_ONLY_NO_H2_FIXEDNESS_MASK20_OR_DIM5_CREDIT",
        "next_expected_command": "STAGE33_MAIN_BATCH_V91C1X_R2_LITERAL_MU2_COCYCLE_GLUE",
        "stop_semantics": "CONTINUE_ONLY_ON_SOURCE_BOUND_LITERAL_H2_REPRESENTATIVE_OR_EQUIVALENT_GLUE_CONSTRUCTION"
    }
    s["work_checkpoint"] = {
        "authority": "V91C1V_HOSTILE_REAUDITED_MERGED",
        "status": "V91C1X_R1_EXACT_NEGATIVE_CHAIN_PREFLIGHT_R2_LITERAL_MU2_GLUE_OPEN"
    }
    s["stage33_progress"] = "6/11"
    for key in ["stage33_12_closed_exact", "stage33_13_released", "receiver_credit", "theorem_credit", "endpoint_credit"]:
        assert s["firewalls"][key] is False
    assert s["firewalls"]["merge_allowed"] is False

    s.pop("canonical_sha256")
    s["canonical_sha256"] = csha(s)
    if args.write:
        STATE.write_text(json.dumps(s, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": "V111_MATERIALIZE_V91C1X_R1_NEGATIVE_PREFLIGHT_ROUTING",
        "state_sha256": s["canonical_sha256"],
        "candidate_sha256": R1_SHA,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
