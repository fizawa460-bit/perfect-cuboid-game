#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = Path(__file__).with_name("MAIN-STATE.json")
ROADMAP = Path(__file__).with_name("stage32-ex2.md")
START = Path(__file__).with_name("MAIN-START-HERE.md")
AUDIT = Path(__file__).with_name("AUDIT-CONTRACT.md")
EX2_00 = Path(__file__).with_name("EX2-00") / "v6-source-lock-target-contract.json"
EX2_00_VERIFY = Path(__file__).with_name("verify_ex2_00_source_lock.py")

state = json.loads(STATE.read_text())
roadmap = ROADMAP.read_text()
start = START.read_text()
audit = AUDIT.read_text()
ex2_00 = json.loads(EX2_00.read_text())

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
assert state["authority"]["EX2_00_source_contract_status"] == "PROVISIONAL_RETAINED_LEAF_NOT_HOSTILE_AUDITED"
assert ex2_00["exit"]["EX2_00_source_lock_complete"] is True
assert ex2_00["exit"]["claim_dag_sync_triggered"] is False

assert state["current"]["leaf"] == "EX2-01_LINE_BUNDLE_REALIZATION_AND_SECTION_SOURCE_INVENTORY"
assert state["frontier"]["EX2_00_source_lock_complete"] is True
assert state["parallel_lanes"]["currently_unlocked"] is True
assert state["fixed_target"]["context_values_EX2_00_source_locked"] is True
assert state["fixed_target"]["picard_context"] == "GEOMETRIC_PICARD_GROUP_OVER_QBAR_CONTEXT"
assert state["fixed_target"]["V6_class_Q_descent_asserted"] is False
assert state["fixed_target"]["arithmetic_member_field_not_asserted"] is True

assert state["frontier"]["explicit_V6_member_materialized"] is False
assert state["frontier"]["explicit_V6_genus1_member_verified"] is False
assert state["frontier"]["population_wide_no_genus1_member_proved"] is False
assert state["frontier"]["full_target_closure"] is False
assert state["credit"]["level"] == "SOURCE_LOCK_ONLY_NO_MEMBER_CREDIT"

fw = state["firewalls"]
for key in [
    "rr_effectivity_promoted_to_explicit_member",
    "h0_lower_bound_promoted_to_section_basis",
    "known140_decomposition_promoted_to_fixed_part",
    "known140_decomposition_promoted_to_complete_linear_system",
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
    "h^0>=294",
    "finite",
]:
    assert token in roadmap, token

assert "stage32ex2-mainbatch" in start
assert "stage32ex2-audit" in start
assert "stage32ex2-audit" in audit
assert "Do not merge without explicit user authorization" in start
assert EX2_00_VERIFY.exists()

working_set = state["current_leaf_working_set"]
assert "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json" in working_set
assert "stages/stage32-ex2/verify_ex2_00_source_lock.py" in working_set
assert len(working_set) == len(set(working_set))
for rel in working_set:
    assert (ROOT / rel).exists(), rel

print("Stage32EX2 MAIN state: PASS at EX2-01 after exact EX2-00 source lock; no member or downstream credit")
