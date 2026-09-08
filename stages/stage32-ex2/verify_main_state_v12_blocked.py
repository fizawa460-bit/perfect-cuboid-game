#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CURRENT_MAIN = "70265586b3f97be21c7621af73f443311f1f3fa3"
AUDIT_HEAD = "0a39b08b767681f1a475dbe12d87e29315af041d"
AUDIT_REVIEW = 5142431810
LEAVES = [
    "verify_ex2_00_source_lock.py",
    "verify_ex2_01_section_sources_v2.py",
    "verify_ex2_02_fixed_components.py",
    "verify_ex2_03_restriction_gap.py",
    "verify_ex2_03b_v6_stabilizer_orbit.py",
    "verify_ex2_03c_omission_witnesses.py",
    "verify_ex2_03d_five_conic_restriction.py",
    "verify_ex2_03e_adjoint_nef_blocker.py",
    "verify_ex2_03f_corrected_adjoint_known140.py",
    "verify_ex2_04a_two_divisor_section_pencil.py",
    "verify_ex2_04b_third_section_valuation_separation.py",
    "verify_ex2_04b_claim_sync_blocker.py",
]


def verify_state() -> None:
    S = json.loads((HERE / "MAIN-STATE.json").read_text())
    R = json.loads((ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json").read_text())

    assert S["schema"] == "STAGE32EX2_MAIN_COMPACT_STATE_V12_EX2_04B_RETAINED_CLAIM_SYNC_BLOCKED"
    assert S["stage"] == "32EX2"
    assert S["bootstrap"]["active_work_pr"] == 1709
    assert S["bootstrap"]["merge_authorized"] is False
    assert S["audit"]["status"] == "NOT_READY_EX2_04B_RETAINED_CLAIM_SYNC_BLOCKED_BY_INHERITED_MAIN_DAG_DRIFT"
    assert S["audit"]["previous_intermediate_pass"] == {
        "credit_ceiling": "NECESSARY_CONDITION_ONLY",
        "exact_head": AUDIT_HEAD,
        "review_id": AUDIT_REVIEW,
        "status": "PASS",
        "through": "EX2-03F",
    }

    assert S["freshness"]["current_main_observed_sha"] == CURRENT_MAIN
    assert S["freshness"]["last_reconciled_current_main_sha"] == CURRENT_MAIN
    assert S["freshness"]["unreconciled_main_commit_count"] == 0
    assert S["freshness"]["stage32ex2_source_drift_in_intervening_main_commit"] is False
    assert S["freshness"]["claim_dag_integrity_on_current_main"] == "FAIL_SOURCE_LOCKS_PREEXISTING_EX2_OVERLAY"
    assert S["freshness"]["claim_dag_integrity_main_baseline_mismatch_count"] == 4

    A = S["authority"]
    assert A["EX2_03D_candidate_claim_id"] == "S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"
    assert A["EX2_03D_artifact_blob_sha1"] == "32e19797812f35ad15fc5cad7559be76140480ef"
    assert A["EX2_03F_artifact_blob_sha1"] == "f5e8c5dbf7d01bf9e71cde7c13924de0d66e3007"
    assert A["EX2_04A_artifact_blob_sha1"] == "3122bccb0afe2c72ac13b24e385aaaaa1dd67956"
    assert A["EX2_04A_artifact_canonical_sha256"] == "ba5a134d3438453ece33ad05ea5ab556db5108c894864ff3c067269b38d46b34"
    assert A["EX2_04A_verifier_blob_sha1"] == "2b31f8f8bc8d00555bb880d280ed33119bec095d"
    assert A["EX2_04A_candidate_claim_id"] == "S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"
    assert A["EX2_04A_claim_status"] == "PROVISIONAL_CORE_SOURCE_LOCK_STALE_AFTER_VERIFIER_SCHEMA_REPAIR_REQUIRES_VERSIONING"
    assert A["EX2_04B_artifact_blob_sha1"] == "5e9cf16ece57162db995cb1b7014a9d583453202"
    assert A["EX2_04B_artifact_canonical_sha256"] == "9d50dc72c467edce946427f1b74786464e1c6401ca86dab6af87bea792d23c70"
    assert A["EX2_04B_candidate_claim_id"] == "S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
    assert A["EX2_04B_claim_status"] == "RETAINED_SCRATCH_PENDING_CLAIM_SYNC_BLOCKED_BY_INHERITED_MAIN_DAG_DRIFT"
    assert A["EX2_04B_claim_sync_blocker"] == "stages/stage32-ex2/EX2-04/ex2-04b-claim-sync-blocker.json"

    F = S["frontier"]
    assert F["EX2_03_zero_curve_nonfixedness_classified_count"] == 2
    assert F["EX2_03C_certified_nonfixed_zero_labels_1based"] == [17, 98]
    assert F["EX2_03C_unresolved_zero_labels_1based"] == [21, 24, 25, 30, 31]
    assert F["EX2_03D_remaining_five_are_pairwise_disjoint_rational_conics"] is True
    assert F["EX2_03D_remaining_five_fixedness_classified"] is False
    assert F["EX2_03F_corrected_adjoint_known140_negative_labels_1based"] == [17, 26, 28]
    assert F["EX2_04A_certified_two_dimensional_section_subspace"] is True
    assert F["EX2_04A_projective_pencil_dimension"] == 1
    assert F["EX2_04B_third_section_line_outside_previous_pencil"] is True
    assert F["EX2_04B_valuation_separator_curve_label_1based"] == 25
    assert F["EX2_04B_previous_pencil_order_lower_bound"] == 6
    assert F["EX2_04B_third_divisor_order"] == 4
    assert F["EX2_04B_linear_independence_certified"] is True
    assert F["certified_section_subspace_dimension"] == 3
    assert F["complete_section_space_basis_obtained"] is False
    assert F["EX2_04_finite_dimensional_section_reconstruction_active"] is False
    assert F["EX2_04C_blocked_until_claim_sync"] is True

    CS = S["claim_sync"]
    assert CS["candidate_claim_id"] == "S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
    assert CS["checkpoint_claim_dag_complete"] is False
    assert CS["claim_dag_integrity_verifier_passed"] is False
    assert CS["current_main_reconciliation_required"] is True
    assert CS["reconciled_current_main_sha"] == CURRENT_MAIN
    assert CS["status"] == "BLOCKED_INHERITED_CURRENT_MAIN_CLAIM_DAG_SOURCE_LOCK_DRIFT"
    assert CS["inherited_current_main_mismatch_count"] == 4
    assert CS["promotion_attempted"] is False
    assert CS["stage32_main_authority_changed"] is False

    assert S["current"]["leaf"] == "EX2-04B_CLAIM_SYNC_BLOCKER_CHECKPOINT"
    assert S["current"]["subroute"] == "WAIT_FOR_CURRENT_MAIN_STAGE32_CLAIM_DAG_INTEGRITY_REPAIR"
    assert S["current"]["stop_semantics"] == "MANAGEMENT_GATE_ONLY_NOT_EX2_MATHEMATICAL_FAILURE_OR_STAGE_EXHAUSTION"
    assert S["completion_contract"]["terminal_outcome"] is None
    assert S["credit"]["genuine_v6_genus1_member_established"] is False
    assert S["credit"]["no_integral_irreducible_v6_genus1_member_in_linear_system"] is False
    assert S["credit"]["full_target_closure"] is False
    assert S["credit"]["stage32_main_credit"] is False

    for k in [
        "trivial_conic_restriction_promoted_to_nonfixedness",
        "trivial_conic_restriction_promoted_to_fixedness",
        "rr_chi_drop_promoted_to_h0_drop",
        "remaining_five_known140_unsat_promoted_to_fixedness",
        "corrected_adjoint_known140_scan_promoted_to_global_nef",
        "h1_vanishing_inferred_from_blocked_nef_route",
        "nef_route_blocker_promoted_to_fixedness",
        "two_dimensional_section_subspace_promoted_to_complete_H0",
        "common_pencil_divisor_promoted_to_complete_fixed_part",
        "h0_lower_bound_promoted_to_explicit_third_section",
        "known140_endpoint_pencil_promoted_to_outside_known140_member",
        "three_dimensional_section_subspace_promoted_to_complete_H0",
        "ex2_04b_scratch_result_promoted_before_claim_sync",
        "inherited_main_claim_dag_drift_repaired_by_cross_lane_audit_credit_carry_forward",
        "claim_sync_blocker_bypassed",
        "stage32_main_credit",
        "Q602_excluded",
        "O210_excluded",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ]:
        assert S["firewalls"][k] is False, k

    claims = {c["claim_id"]: c for c in R["claims"]}
    for cid in [
        "S32.EX2.SECTION_SOURCE_INVENTORY.V2",
        "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1",
        "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1",
        "S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1",
    ]:
        c = claims[cid]
        assert c["authority_status"] == "AUDITED", cid
        assert c["audit_receipt"] == {
            "exact_head": AUDIT_HEAD,
            "pr": 1709,
            "review_id": AUDIT_REVIEW,
            "status": "PASS",
        }, cid

    c04a = claims["S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"]
    assert c04a["authority_status"] == "PROVISIONAL"
    assert c04a["audit_receipt"] is None
    assert "S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1" not in claims
    print("PASS Stage32EX2 V12 state assertions")


def run_leaves() -> None:
    for rel in LEAVES:
        print("RUN retained leaf=" + rel, flush=True)
        subprocess.check_call([sys.executable, "-B", str(HERE / rel)], cwd=ROOT)
    print("PASS Stage32EX2 retained EX2 leaf replay")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--state-only", action="store_true")
    p.add_argument("--leaves-only", action="store_true")
    args = p.parse_args()
    if args.state_only and args.leaves_only:
        raise SystemExit("choose at most one mode")
    if not args.leaves_only:
        verify_state()
    if not args.state_only:
        run_leaves()
    if not args.state_only and not args.leaves_only:
        print("PASS Stage32EX2 MAIN state V12 blocked checkpoint")
        print("current_leaf=EX2-04B claim-sync blocker checkpoint")
        print("current_main=" + CURRENT_MAIN + " baseline_claim_dag_source_lock_mismatches=4")
        print("EX2-04B certified_subspace_dimension=3 authority=scratch_pending_claim_sync")
        print("advance_to_EX2-04C=false merge_authorized=false stage32_main_credit=false")


if __name__ == "__main__":
    main()
