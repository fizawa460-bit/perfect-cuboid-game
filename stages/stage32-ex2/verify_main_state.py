#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = Path(__file__).with_name("MAIN-STATE.json")
ROADMAP = Path(__file__).with_name("stage32-ex2.md")
START = Path(__file__).with_name("MAIN-START-HERE.md")
AUDIT = Path(__file__).with_name("AUDIT-CONTRACT.md")
EX2_00 = Path(__file__).with_name("EX2-00") / "v6-source-lock-target-contract.json"
EX2_01 = Path(__file__).with_name("EX2-01") / "section-source-inventory.json"
EX2_02 = Path(__file__).with_name("EX2-02") / "exact-fixed-component-extraction.json"
EX2_02_VERIFY = Path(__file__).with_name("verify_ex2_02_fixed_components.py")
CLAIM_SYNC = ROOT / "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"

state = json.loads(STATE.read_text())
roadmap = ROADMAP.read_text()
start = START.read_text()
audit = AUDIT.read_text()
ex2_00 = json.loads(EX2_00.read_text())
ex2_01 = json.loads(EX2_01.read_text())
ex2_02 = json.loads(EX2_02.read_text())
registry = json.loads(REGISTRY.read_text())


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


assert state["schema"] == "STAGE32EX2_MAIN_COMPACT_STATE_V4_EX2_02_FIXED_COMPONENT_SCAN_COMPLETE_PENDING_CLAIM_SYNC"
assert state["stage"] == "32EX2"
assert state["execution"]["main_command"] == "stage32ex2-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex2-audit"
assert state["bootstrap"]["active_work_pr"] == 1709
assert state["bootstrap"]["work_branch"] == "stage32ex2-ex2-00-source-lock-continuation"
assert state["bootstrap"]["merge_authorized"] is False

allowed = state["completion_contract"]["allowed_terminal_outcomes"]
assert allowed == [
    "GENUINE_V6_GENUS1_MEMBER_ESTABLISHED",
    "NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM",
]
assert state["completion_contract"]["terminal_outcome"] is None
assert state["completion_contract"]["finite_search_miss_is_terminal_success"] is False
assert state["completion_contract"]["source_gap_diagnosis_is_terminal_success"] is False
assert state["completion_contract"]["bounded_negative_intersection_scan_is_terminal_success"] is False
assert state["completion_contract"]["blocked_route_is_stage_exhaustion"] is False

assert state["authority"]["EX2_00_source_contract"] == "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
assert state["authority"]["EX2_01_claim_id"] == "S32.EX2.SECTION_SOURCE_INVENTORY.V1"
assert state["authority"]["EX2_02_fixed_component_scan"] == "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"
assert state["authority"]["EX2_02_artifact_blob_sha1"] == blob(EX2_02) == "b07fd12a40acbfc478cdab472157cb4a34efe39c"
assert state["authority"]["EX2_02_artifact_canonical_sha256"] == ex2_02["canonical_sha256_without_this_field"]
assert state["authority"]["EX2_02_candidate_claim_id"] == "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"
assert state["authority"]["EX2_02_claim_status"] == "RETAINED_RESULT_CLAIM_DAG_SYNC_PENDING"

assert ex2_00["exit"]["EX2_00_source_lock_complete"] is True
assert ex2_01["exit"]["EX2_01_complete"] is True
assert ex2_01["exit"]["next_leaf"] == "EX2-02_EXACT_FIXED_COMPONENT_EXTRACTION"
assert ex2_02["exit"]["EX2_02_complete"] is True
assert ex2_02["exact_scan"]["pairing_count"] == 140
assert ex2_02["exact_scan"]["negative_pairing_count"] == 0
assert ex2_02["exact_scan"]["zero_pairing_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]
assert ex2_02["fixed_component_extraction"]["new_forced_fixed_components_certified_by_this_gate"] == 0
assert ex2_02["fixed_component_extraction"]["full_fixed_part_proved_zero"] is False

assert state["current"]["status"] == "EX2_02_BOUNDED_NEGATIVE_INTERSECTION_SCAN_COMPLETE_PENDING_CLAIM_DAG_SYNC"
assert state["current"]["leaf"] == "EX2-02_RETAINED_CONSOLIDATION_CLAIM_DAG_RECONCILIATION"
assert state["current"]["next_route_on_success"] == "EX2-03_BASE_LOCUS_AND_MOVING_SYSTEM_STRUCTURE"

frontier = state["frontier"]
assert frontier["EX2_00_source_lock_complete"] is True
assert frontier["EX2_01_section_source_inventory_complete"] is True
assert frontier["EX2_02_exact_negative_intersection_scan_complete"] is True
assert frontier["EX2_02_known140_pairing_count"] == 140
assert frontier["EX2_02_negative_pairing_count"] == 0
assert frontier["EX2_02_new_forced_fixed_components_certified"] == 0
assert frontier["EX2_02_residual_after_certified_subtractions"] == "V6"
assert frontier["fixed_part_fully_classified"] is False
assert frontier["known140_fixed_part_proved_empty"] is False
assert frontier["moving_system_structure_classified"] is False
assert frontier["explicit_V6_member_materialized"] is False
assert frontier["explicit_V6_genus1_member_verified"] is False
assert frontier["population_wide_no_genus1_member_proved"] is False
assert frontier["full_target_closure"] is False

sync = state["claim_sync"]
assert sync["triggered_for_EX2_02"] is True
assert sync["trigger"] == "RETAINED_CONSOLIDATION"
assert sync["contract"] == "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
assert sync["status"] == "PENDING_CURRENT_MAIN_RECONCILIATION"
assert sync["candidate_claim_id"] == "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"
assert sync["shared_claim_files_written_from_stale_branch"] is False
assert sync["checkpoint_claim_dag_complete"] is False
assert sync["current_main_reconciliation_required"] is True
assert sync["stage32_main_authority_changed"] is False
assert sync["promotion_attempted"] is False
assert CLAIM_SYNC.exists()

claim_ids = {c["claim_id"] for c in registry["claims"]}
assert "S32.EX2.SECTION_SOURCE_INVENTORY.V1" in claim_ids
assert "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1" not in claim_ids

credit = state["credit"]
assert credit["bounded_negative_intersection_gate_closed"] is True
assert credit["fixed_part_fully_classified"] is False
assert credit["genuine_v6_genus1_member_established"] is False
assert credit["no_integral_irreducible_v6_genus1_member_in_linear_system"] is False
assert credit["full_target_closure"] is False
assert credit["stage32_main_credit"] is False

fw = state["firewalls"]
for key in [
    "rr_effectivity_promoted_to_explicit_member",
    "h0_lower_bound_promoted_to_section_basis",
    "known140_decomposition_promoted_to_fixed_part",
    "known140_decomposition_promoted_to_complete_linear_system",
    "one_dimensional_section_line_promoted_to_complete_H0",
    "abstract_projective_section_promoted_to_coordinate_section",
    "bounded_no_negative_hit_promoted_to_fixed_part_empty",
    "positive_pairing_promoted_to_nonfixed_curve",
    "zero_pairing_promoted_to_fixed_curve",
    "picard_class_promoted_to_unique_member",
    "geometric_picard_class_promoted_to_Q_defined_member",
    "candidate_polynomial_promoted_without_class_adapter",
    "finite_search_miss_promoted_to_population_wide_exclusion",
    "reducible_member_promoted_to_positive_terminal",
    "blocked_route_treated_as_stage_exhaustion",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "stage32_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False, key

for token in [
    "GENUINE_V6_GENUS1_MEMBER_ESTABLISHED",
    "NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM",
    "FULL_TARGET_CLOSURE",
    "EX2-02",
    "EX2-03",
]:
    assert token in roadmap, token

assert "stage32ex2-mainbatch" in start
assert "stage32ex2-audit" in start
assert "stage32ex2-audit" in audit
assert "Do not merge without explicit user authorization" in start
assert EX2_02_VERIFY.exists()

working_set = state["current_leaf_working_set"]
required = {
    "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json",
    "stages/stage32-ex2/verify_ex2_02_fixed_components.py",
    "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md",
    "stages/stage32/STAGE32-PROOF-PATH.md",
    "stages/stage32/proof/LANE-ADAPTERS.json",
    "stages/stage32/proof/CLAIM-REGISTRY.json",
    "stages/stage32/proof/ACTIVE-FRONTIER.json",
}
assert required.issubset(set(working_set))
assert len(working_set) == len(set(working_set))
for rel in working_set:
    assert (ROOT / rel).exists(), rel

print(
    "Stage32EX2 MAIN state: PASS at retained EX2-02 bounded no-hit scan; fixed part remains unclassified and claim-DAG reconciliation is the mandatory next gate before EX2-03."
)
