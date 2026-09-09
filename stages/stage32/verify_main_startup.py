#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V2_POST1728_V6_NEGATIVE_AUTHORITY_CONSUMED"
EXPECTED_CANONICAL = "1a7295b3452d4cc7bc4406ee1bcfb655cd28a5d8e75f690fdc8bd93e6d85c6e2"
EXPECTED_ROUTE = "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS"
EXPECTED_WORKING_SET = [
    "stages/stage32/full178-dominance-recheck-after-v6-o210-q602-route-20260909.json",
    "stages/stage32/management/mainbatch-final-chain-reentry-20260909.json",
]
POST_SYNC_AUDIT = {
    "review_id": 5149990935,
    "exact_head": "9b605ed7f44415198a0e261dc46971e5ecd3c80b",
}


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    state = json.loads(STATE.read_text())
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert csha(state) == EXPECTED_CANONICAL
    assert state["fixed_target"] == {
        "row_id":"g1-d186", "degree":186, "e":266, "genus":1,
        "O":210, "qprime":4, "Q":602,
        "surviving_residues_decimal":[73,97,235],
    }

    a = state["authority_sync"]
    assert a["latest_audited_stage32_pr"] == 1730
    assert a["latest_hostile_audit_review_id"] == POST_SYNC_AUDIT["review_id"]
    assert a["latest_audited_exact_head"] == POST_SYNC_AUDIT["exact_head"]
    assert a["latest_stage32_merge_commit"] == "733176600f99e91993d08c16aa98f09c08a1e726"
    assert a["audited_main_v6_negative_claim"] == "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"
    assert a["audited_main_o210_claim"] == "S32.O210.EXCLUSION.V3"
    assert a["audited_main_o210_claim_review_id"] == 5147304889
    assert a["audited_main_q602_claim"] == "S32.Q602.EXCLUSION.V3"
    assert a["q602_post_sync_hostile_audit_status"] == "PASS"
    assert a["q602_post_sync_hostile_audit_review_id"] == POST_SYNC_AUDIT["review_id"]
    assert a["q602_post_sync_hostile_audit_exact_head"] == POST_SYNC_AUDIT["exact_head"]

    f = state["current_exact_frontier"]
    assert f["v6_integral_irreducible_genus1_population_empty_audited"] is True
    assert f["q602_survivors_audited"] == [73,97,235]
    assert f["q602_excluded"] is True and f["o210_excluded"] is True
    assert f["o210_exclusion_claim_id"] == "S32.O210.EXCLUSION.V3"
    assert f["q602_exclusion_claim_id"] == "S32.Q602.EXCLUSION.V3"
    assert f["full178_numerical_census_complete"] is False
    for key in [
        "v6_actual_member_branch_active",
        "v6_surface_node_multibranch_branch_active",
        "v6_smooth_ambient_locus_curve_singularity_branch_active",
        "v6_same_member_q602_identity_active",
        "absolute_delta0inf_marking_active_for_selected_route",
    ]:
        assert f[key] is False

    assert state["current"]["active_missing_interface"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert state["current"]["next_exact_route"] == EXPECTED_ROUTE
    assert state["current_leaf_working_set"] == EXPECTED_WORKING_SET
    for rel in EXPECTED_WORKING_SET:
        assert (ROOT / rel).is_file(), rel

    checkpoint = json.loads((ROOT / EXPECTED_WORKING_SET[1]).read_text())
    cp_body = dict(checkpoint)
    cp_digest = cp_body.pop("canonical_sha256_without_this_field")
    assert csha(checkpoint) == cp_digest
    assert checkpoint["status"] == "RETAINED_ROUTING_CHECKPOINT_NO_NEW_MATHEMATICAL_CREDIT"
    assert checkpoint["final_chain"]["32-01"]["status"] == "ACTIVE_PRIMARY"
    assert checkpoint["final_chain"]["32-02"]["status"] == "FINAL_EXECUTION_WAITS_FOR_COMPLETE_32_01_SURVIVOR_LEDGER"
    assert checkpoint["final_chain"]["32-03"]["status"] == "INDEPENDENT_PARALLEL_WORK_AVAILABLE"

    org = state["organizational_integration"]
    assert org["former_ex1_ex4_user_facing_view"] == "stages/stage32/integrated-ex/README.md"
    assert all(v is False for v in org["ordinary_separate_lane_startup"].values())
    assert org["EX5_remains_separate_active_lane"] is True
    assert org["integration_changes_mathematical_credit"] is False

    fw = state["firewalls"]
    assert fw["V6_genus1_carrier_excluded"] is True
    assert fw["O210_excluded"] is True and fw["Q602_excluded"] is True
    for key in [
        "O212_plus_advance_allowed", "controller_promotion_granted",
        "heavy_compute_authorized_by_startup_state", "receiver_credit", "route_credit",
        "theorem_credit", "endpoint_credit", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ]:
        assert fw[key] is False, key

    cleanup = state["cleanup_gate"]
    assert cleanup["proof_or_source_locked_assets_may_be_deleted_without_reference_audit"] is False
    assert cleanup["root_cleanup_phase"] == "PHASE_C_USER_FACING_EX1_EX4_INTEGRATION_AND_LOOSE_ROOT_RELOCATION"
    assert cleanup["integrated_ex_view"] == "stages/stage32/integrated-ex/README.md"
    assert cleanup["legacy_numbered_directories_physically_relocated"] is False

    startup = START.read_text()
    for fragment in [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        assert fragment in startup

    print("PASS Stage32 MAIN startup authority POST1730_Q602_AUDIT_COMPLETE_PHASE_C")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("v6_o210_q602_audited_and_consumed=true")
    print("integrated_ex1_ex4=true")
    print("ex5_remains_separate_active=true")
    print("remaining=FULL178,effectivity,multibranch,final_synthesis")


if __name__ == "__main__":
    main()
