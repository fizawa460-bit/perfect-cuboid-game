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
EX2_03 = Path(__file__).with_name("EX2-03") / "zero-intersection-restriction-adapter-gap.json"
EX2_03_VERIFY = Path(__file__).with_name("verify_ex2_03_restriction_gap.py")
CLAIM_SYNC = ROOT / "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

state = json.loads(STATE.read_text())
roadmap = ROADMAP.read_text()
start = START.read_text()
audit = AUDIT.read_text()
ex2_00 = json.loads(EX2_00.read_text())
ex2_01 = json.loads(EX2_01.read_text())
ex2_02 = json.loads(EX2_02.read_text())
ex2_03 = json.loads(EX2_03.read_text())
registry = json.loads(REGISTRY.read_text())
lanes = json.loads(LANES.read_text())


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


assert state["schema"] == "STAGE32EX2_MAIN_COMPACT_STATE_V6_EX2_03_RESTRICTION_GAP_SYMMETRY_ORBIT_ACTIVE"
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
assert state["completion_contract"]["blocked_route_is_stage_exhaustion"] is False

assert state["authority"]["EX2_00_source_contract"] == "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
assert state["authority"]["EX2_01_claim_id"] == "S32.EX2.SECTION_SOURCE_INVENTORY.V1"
assert state["authority"]["EX2_02_fixed_component_scan"] == "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"
assert state["authority"]["EX2_02_artifact_blob_sha1"] == blob(EX2_02) == "b07fd12a40acbfc478cdab472157cb4a34efe39c"
assert state["authority"]["EX2_02_artifact_canonical_sha256"] == ex2_02["canonical_sha256_without_this_field"]
assert state["authority"]["EX2_02_candidate_claim_id"] == "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"
assert state["authority"]["EX2_02_claim_status"] == "PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED"
assert state["authority"]["EX2_03_restriction_gap"] == "stages/stage32-ex2/EX2-03/zero-intersection-restriction-adapter-gap.json"
assert state["authority"]["EX2_03_artifact_blob_sha1"] == blob(EX2_03) == "222b4a17a75b397831fe6b641e9459d042aeec60"
assert state["authority"]["EX2_03_artifact_canonical_sha256"] == ex2_03["canonical_sha256_without_this_field"] == "22b90a9facb7c2de7d69f8cfdfc36a90bbfb02680463b8a59066d16572b392f4"
assert state["authority"]["EX2_03_verifier_blob_sha1"] == blob(EX2_03_VERIFY) == "2fa32967b98a17fef8eb2885ac0e2c5053477bec"
assert state["authority"]["EX2_03_claim_status"] == "TYPED_BLOCKER_NO_MATHEMATICAL_CLAIM_NO_CLAIM_DAG_ENTRY"

assert ex2_00["exit"]["EX2_00_source_lock_complete"] is True
assert ex2_01["exit"]["EX2_01_complete"] is True
assert ex2_02["exit"]["EX2_02_complete"] is True
assert ex2_02["exact_scan"]["zero_pairing_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]
assert ex2_03["exit"]["EX2_03_restriction_preflight_complete"] is True
assert ex2_03["exit"]["result"] == "EXACT_SCOPED_ADAPTER_GAP_NO_BASE_LOCUS_CREDIT"
assert ex2_03["exit"]["claim_dag_sync_triggered"] is False
assert ex2_03["exact_gap"]["pairwise_intersection_matrix_alone_would_not_prove_fixedness"] is True
assert ex2_03["distinct_lane_route"]["next_leaf"] == "EX2-03B_SYMMETRY_DIVISOR_ORBIT_PREFLIGHT"
assert ex2_03["distinct_lane_route"]["requires_line_bundle_linearization_for_divisor_level_member"] is False
assert ex2_03["distinct_lane_route"]["symmetry_eigenspace_or_H0_representation_claimed"] is False

assert state["current"]["status"] == "EX2_03_RESTRICTION_PREFLIGHT_BLOCKED_ROUTED_TO_SYMMETRY_ORBIT"
assert state["current"]["leaf"] == "EX2-03B_SYMMETRY_DIVISOR_ORBIT_PREFLIGHT"
assert state["current"]["subroute"] == "V6_STABILIZER_AND_KNOWN_DIVISOR_ORBIT_PREFLIGHT"
assert state["current"]["stop_semantics"] == "LEAF_GATE_ONLY_NOT_STAGE_EXHAUSTION"

frontier = state["frontier"]
assert frontier["EX2_00_source_lock_complete"] is True
assert frontier["EX2_01_section_source_inventory_complete"] is True
assert frontier["EX2_02_exact_negative_intersection_scan_complete"] is True
assert frontier["EX2_02_claim_dag_sync_complete"] is True
assert frontier["EX2_02_zero_pairing_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]
assert frontier["EX2_03_restriction_preflight_complete"] is True
assert frontier["EX2_03_restriction_or_base_locus_adapter_obtained"] is False
assert frontier["EX2_03_zero_curve_fixedness_classified_count"] == 0
assert frontier["EX2_03_zero_curve_nonfixedness_classified_count"] == 0
assert frontier["EX2_03_symmetry_divisor_orbit_preflight_active"] is True
assert frontier["fixed_part_fully_classified"] is False
assert frontier["moving_system_structure_classified"] is False
assert frontier["explicit_V6_member_materialized"] is False
assert frontier["explicit_V6_genus1_member_verified"] is False
assert frontier["population_wide_no_genus1_member_proved"] is False
assert frontier["full_target_closure"] is False

fresh = state["freshness"]
assert fresh["last_reconciled_current_main_sha"] == "d5545b32e6b3088bca53318998d434f2745b03e9"
assert fresh["ancestry_sync_commit"] == "a6cb7d6c0b18dd11710ad58bb4f3457f75026c8a"
assert fresh["stage32ex2_source_drift_in_intervening_main_commit"] is False
assert fresh["promotion_requires_recheck_current_main"] is True

sync = state["claim_sync"]
assert sync["triggered_for_EX2_02"] is True
assert sync["triggered_for_EX2_03"] is False
assert sync["trigger"] == "RETAINED_CONSOLIDATION"
assert sync["contract"] == "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
assert sync["status"] == "COMPLETE_CURRENT_MAIN_RECONCILED_REQUIRED_DAG_VERIFIERS_PASS"
assert sync["candidate_claim_id"] == "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"
assert sync["checkpoint_claim_dag_complete"] is True
assert sync["claim_dag_integrity_verifier_passed"] is True
assert sync["active_frontier_verifier_passed"] is True
assert sync["current_main_reconciliation_required"] is False
assert sync["reconciled_current_main_sha"] == "d5545b32e6b3088bca53318998d434f2745b03e9"
assert sync["mathematical_frontier_semantics_changed"] is False
assert sync["shared_claim_files_written_from_stale_branch"] is False
assert sync["stage32_main_authority_changed"] is False
assert sync["promotion_attempted"] is False
assert CLAIM_SYNC.exists()

claims = {c["claim_id"]: c for c in registry["claims"]}
assert "S32.EX2.SECTION_SOURCE_INVENTORY.V1" in claims
fixed_claim = claims["S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"]
assert fixed_claim["authority_status"] == "PROVISIONAL"
assert fixed_claim["requires"] == ["S32.EX2.LANE_CONTRACT.V3"]
assert fixed_claim["replay_verifier"] == "stages/stage32-ex2/verify_ex2_02_fixed_components.py"
locks = {x["path"]: x for x in fixed_claim["source_locks"]}
assert locks["stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"]["blob_sha1"] == blob(EX2_02)
assert locks["stages/stage32-ex2/verify_ex2_02_fixed_components.py"]["blob_sha1"] == blob(EX2_02_VERIFY)
assert claims["S32.EX1.CANDIDATE_THROUGH_05H.V3"]["authority_status"] == "AUDITED"
assert claims["S32.EX1.CANDIDATE_THROUGH_05H.V3"]["audit_receipt"]["review_id"] == 5136931113
assert not any(c["claim_id"].startswith("S32.EX2.RESTRICTION") for c in registry["claims"])

lane_map = {x["lane"]: x for x in lanes["lanes"]}
assert "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1" in lane_map["EX2"]["claim_refs"]
assert "S32.EX2.SECTION_SOURCE_INVENTORY.V1" in lane_map["EX2"]["claim_refs"]
assert lane_map["EX1"]["claim_refs"][1] == "S32.EX1.CANDIDATE_THROUGH_05H.V3"

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
    "restriction_gap_promoted_to_base_locus_classification",
    "symmetry_class_action_promoted_to_H0_linearization",
    "unverified_automorphism_promoted_to_divisor_member",
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
    "EX2-03",
]:
    assert token in roadmap, token
assert "SYMMETRY-LANE" in roadmap
assert "stage32ex2-mainbatch" in start
assert "stage32ex2-audit" in start
assert "stage32ex2-audit" in audit
assert "Do not merge without explicit user authorization" in start
assert EX2_02_VERIFY.exists()
assert EX2_03_VERIFY.exists()

working_set = state["current_leaf_working_set"]
required = {
    "stages/stage32-ex2/EX2-03/zero-intersection-restriction-adapter-gap.json",
    "stages/stage32-ex2/verify_ex2_03_restriction_gap.py",
    "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json",
    "stages/stage32-ex2/verify_ex2_02_fixed_components.py",
    "stages/stage32-ex2/EX2-01/section-source-inventory.json",
    "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json",
    "stages/stage32-ex2/stage32-ex2.md",
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
    "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json",
}
assert required == set(working_set)
assert len(working_set) == len(set(working_set))
for rel in working_set:
    assert (ROOT / rel).exists(), rel

print(
    "Stage32EX2 MAIN state: PASS; EX2-03 records an exact no-credit restriction/base-locus adapter gap, preserves the prior EX2-02 provisional claim ceiling and current-main reconciliation, and routes the next nonterminal unit to divisor-level symmetry-orbit preflight."
)
