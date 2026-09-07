#!/usr/bin/env python3
"""Promote the exact noncredit V91C1X_R2 construction contract into MAIN routing.

This is a routing/contract promotion only.  It grants no H2 fixedness,
mask20 exclusion, marked Brauer image, dim-5 subspace, theorem, receiver,
endpoint, or merge credit.
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
R2 = HERE / "e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"

OLD_STATE_SHA = "9c436458001fafc4c036aeeb99e610abbdc2d0554f34bf7fde9ba4c144d84191"
R1_SHA = "b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb"
R2_SHA = "912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1"
R2_CANDIDATE = "V91C1X_R2_LITERAL_MU2_OR_UNIMODULAR_CECH_GLUE_CONSTRUCTION_CONTRACT"
NEXT = "V91C1X_R3_CONSTRUCT_OR_LOCATE_THE_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT_THEN_SOLVE_THE_KUMMER_1_COCHAIN_EQUATIONS"
MISSING = "SOURCE_BOUND_COVER_INDEXED_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_GLUE_WITH_SWAP23_COMMON_REFINEMENT_AND_KUMMER_SQUARE_ROOT_1_COCHAIN"


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
    r2 = load(R2, R2_SHA)
    assert r1["semantic_bridge"]["next_exact_leaf"].startswith("V91C1X_R2_")
    assert r2["next_exact_leaf"] == NEXT
    assert r2["next_missing_object"] == MISSING
    assert r2["current_materialization_status"]["accepted_source_representative_materialized"] is False
    assert r2["current_materialization_status"]["triple_overlap_identity_verified"] is False
    assert r2["credit_firewall"]["swap23_h2_seed_fixedness"] is False

    s["schema"] = "STAGE33_MAIN_COMPACT_STATE_V50_V91C1X_R2_CHAIN_CONSTRUCTION_CONTRACT_R3_COVER_INDEXED_REPRESENTATIVE"
    s["authority_sync"]["branch_candidate_frontier"] = R2_CANDIDATE
    s["authority_sync"]["status"] = "V91C1V_HOSTILE_REAUDITED_MERGED_V91C1W_RETAINED_X_R1_NEGATIVE_X_R2_CHAIN_CONSTRUCTION_CONTRACT"
    s["branch_exact_frontier_candidate"] = "stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"

    previous = s["candidate_audit_gate"]
    assert previous["candidate"] == "V91C1X_R1_CHAIN_LEVEL_ACTION_DIFFERENCE_PREFLIGHT_BLOCKED"
    assert previous["candidate_certificate_sha256"] == R1_SHA
    s["prior_x_r1_candidate_gate"] = previous
    s["candidate_audit_gate"] = {
        "candidate": R2_CANDIDATE,
        "candidate_certificate": "stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json",
        "candidate_certificate_sha256": R2_SHA,
        "pr": 1678,
        "status": "EXACT_NONCREDIT_CONSTRUCTION_CONTRACT_CONTINUATION_ALLOWED",
        "audit_pass_credit": False,
        "merge_allowed": False,
        "parent_r1_candidate": "V91C1X_R1_CHAIN_LEVEL_ACTION_DIFFERENCE_PREFLIGHT_BLOCKED",
        "parent_r1_sha256": R1_SHA,
        "retained_v91c1w_sha256": "e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7",
        "hostile_audit_blocker_review": 5127167940
    }

    s["continuation_provenance"]["x_r2_chain_construction_contract"] = {
        "pr": 1678,
        "certificate_sha256": R2_SHA,
        "accepted_source_representative_materialized": False,
        "cover_action_or_common_refinement_materialized": False,
        "line_bundle_gm_1_cocycle_materialized": False,
        "square_root_1_cochain_materialized": False,
        "triple_overlap_identity_verified": False,
        "next_missing_object": MISSING
    }

    s["current"] = {
        "active_missing_interface": MISSING,
        "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
        "next_exact_leaf": NEXT,
        "substep": "E3_V91C1X_R3_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT",
        "unit": "33-12"
    }

    f = s["current_exact_frontier"]
    f["a2_02_chain_level_kummer_action_difference_construction_contract_materialized"] = True
    f["a2_02_accepted_source_representative_materialized"] = False
    f["a2_02_cover_action_or_common_refinement_materialized"] = False
    f["a2_02_line_bundle_gm_1_cocycle_ell_ij_materialized"] = False
    f["a2_02_square_root_1_cochain_r_ij_materialized"] = False
    f["a2_02_triple_overlap_action_difference_identity_verified"] = False
    f["a2_02_literal_mu2_2_cocycle_materialized"] = False
    f["a2_02_equivalent_unimodular_cech_glue_materialized"] = False
    f["a2_02_actual_swap23_gm_1_cochain_comparison_materialized"] = False
    f["a2_02_semantic_action_difference_chain_witness_materialized"] = False
    f["a2_02_semantic_action_difference_verified_automorphisms"] = []
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
        "docs/arsenal/cards/provisional/S33-PW08.md",
        "stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json",
        "stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json",
        "stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json",
        "stages/stage33/33-12/e3-v91c1d-a2-02-purity-cech-cartier-assembly.json",
        "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
        "stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json"
    ]

    s["locked_facts"]["v91c1x_r2_chain_construction_contract"] = {"sha256": R2_SHA}
    s["resolved_investigations"]["e3_v91c1x_r2_literal_mu2_or_unimodular_glue_contract"] = (
        "EXACT_NONCREDIT_ACCEPTANCE_CONTRACT_FIXED_SOURCE_REPRESENTATIVE_COMMON_REFINEMENT_GM_COCYCLE_SQUARE_ROOT_AND_TRIPLE_OVERLAP_IDENTITY_STILL_UNMATERIALIZED"
    )
    s["execution_gate"] = {
        "advance_allowed": True,
        "advance_scope": "V91C1X_R3_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT_ONLY_NO_H2_FIXEDNESS_MASK20_OR_DIM5_CREDIT",
        "next_expected_command": "STAGE33_MAIN_BATCH_V91C1X_R3_COVER_INDEXED_A2_02_H2_REPRESENTATIVE",
        "stop_semantics": "CONTINUE_ONLY_ON_SOURCE_BOUND_COVER_INDEXED_REPRESENTATIVE_COMMON_REFINEMENT_OR_EXACT_CONSTRUCTION_BLOCKER"
    }
    s["work_checkpoint"] = {
        "authority": "V91C1V_HOSTILE_REAUDITED_MERGED",
        "status": "V91C1X_R2_CHAIN_CONSTRUCTION_CONTRACT_R3_COVER_INDEXED_REPRESENTATIVE_OPEN"
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
        "marker": "V112_MATERIALIZE_V91C1X_R2_CHAIN_CONSTRUCTION_CONTRACT_ROUTING",
        "state_sha256": s["canonical_sha256"],
        "candidate_sha256": R2_SHA,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
