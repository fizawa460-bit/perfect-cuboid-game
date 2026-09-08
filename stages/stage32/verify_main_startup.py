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
EXPECTED_CANONICAL = "165362e691949cb0079a7cb581ac7209d1b6231dfc5ffce82428ed4c7bae7f5b"
EXPECTED_ROUTE = "BUILD_AND_HOSTILE_AUDIT_V6_EMPTY_TO_O210_AND_Q602_POPULATION_PRESERVING_ADAPTERS_IN_PARALLEL_WITH_FULL178_CENSUS"
EXPECTED_WORKING_SET = [
    "stages/stage32/post1728-v6-negative-authority-consumption-and-frontier-remap.json",
    "stages/stage32/verify_stage32_post1728_v6_negative_authority_consumption.py",
    "stages/stage32-ex1/ex1-07-current-main-v6-carrier-promotion-adapter.json",
    "stages/stage32-ex1/verify_ex1_07_current_main_v6_carrier_promotion_adapter.py",
]


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    state = json.loads(STATE.read_text())
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert csha(state) == EXPECTED_CANONICAL
    assert state["fixed_target"] == {"row_id":"g1-d186","degree":186,"e":266,"genus":1,"O":210,"qprime":4,"Q":602,"surviving_residues_decimal":[73,97,235]}
    a = state["authority_sync"]
    assert a["latest_audited_stage32_pr"] == 1728
    assert a["latest_hostile_audit_review_id"] == 5147810198
    assert a["audited_main_v6_negative_claim"] == "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"
    f = state["current_exact_frontier"]
    assert f["v6_integral_irreducible_genus1_population_empty_audited"] is True
    assert f["q602_survivors_audited"] == [73,97,235]
    assert f["q602_excluded"] is False and f["o210_excluded"] is False
    assert f["full178_numerical_census_complete"] is False
    for key in ["v6_actual_member_branch_active","v6_surface_node_multibranch_branch_active","v6_smooth_ambient_locus_curve_singularity_branch_active","v6_same_member_q602_identity_active","absolute_delta0inf_marking_active_for_selected_route"]:
        assert f[key] is False
    assert state["current"]["next_exact_route"] == EXPECTED_ROUTE
    assert state["current_leaf_working_set"] == EXPECTED_WORKING_SET
    for rel in EXPECTED_WORKING_SET:
        assert (ROOT / rel).is_file(), rel
    fw = state["firewalls"]
    assert fw["V6_genus1_carrier_excluded"] is True
    for key in ["Q602_excluded","O210_excluded","O212_plus_advance_allowed","controller_promotion_granted","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
        assert fw[key] is False
    cleanup = state["cleanup_gate"]
    assert cleanup == {
        "stage32_root_cleanup_started": True,
        "root_cleanup_phase": "PHASE_B_LOOSE_LEGACY_ROOT_RELOCATION_PENDING_HOSTILE_AUDIT",
        "archive_manifest": "stages/stage32/archive/legacy-root/manifest.json",
        "proof_or_source_locked_assets_may_be_deleted_without_reference_audit": False,
        "next_cleanup_phase": "AFTER_PHASE_B_HOSTILE_AUDIT_REVIEW_REFERENCED_ROOT_AUTHORITY_FILES",
    }
    startup = START.read_text()
    for fragment in ["Ordinary `Stage32-main-batch` reads, in this order:","only the paths listed in `MAIN-STATE.json.current_leaf_working_set`","Do not merge without explicit user authorization."]:
        assert fragment in startup
    print("PASS Stage32 MAIN startup authority POST1728")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("v6_integral_irreducible_genus1_population_empty_audited=true")
    print("remaining=O210_adapter,Q602_adapter,FULL178,final_synthesis")


if __name__ == "__main__":
    main()
