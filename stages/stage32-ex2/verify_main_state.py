#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = Path(__file__).with_name("MAIN-STATE.json")
ROADMAP = Path(__file__).with_name("stage32-ex2.md")
START = Path(__file__).with_name("MAIN-START-HERE.md")
AUDIT = Path(__file__).with_name("AUDIT-CONTRACT.md")

state = json.loads(STATE.read_text())
roadmap = ROADMAP.read_text()
start = START.read_text()
audit = AUDIT.read_text()

assert state["stage"] == "32EX2"
assert state["execution"]["main_command"] == "stage32ex2-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex2-audit"
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

assert state["current"]["leaf"] == "EX2-00_SOURCE_LOCK_AND_EXACT_TARGET_CONTRACT"
assert state["frontier"]["EX2_00_source_lock_complete"] is False
assert state["frontier"]["explicit_V6_member_materialized"] is False
assert state["frontier"]["explicit_V6_genus1_member_verified"] is False
assert state["frontier"]["population_wide_no_genus1_member_proved"] is False
assert state["frontier"]["full_target_closure"] is False

fw = state["firewalls"]
for key in [
    "rr_effectivity_promoted_to_explicit_member",
    "h0_lower_bound_promoted_to_section_basis",
    "known140_decomposition_promoted_to_fixed_part",
    "known140_decomposition_promoted_to_complete_linear_system",
    "picard_class_promoted_to_unique_member",
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

working_set = state["current_leaf_working_set"]
assert "stages/stage32-ex2/verify_main_state.py" in working_set
assert len(working_set) == len(set(working_set))
for rel in working_set:
    assert (ROOT / rel).exists(), rel

print("Stage32EX2 MAIN bootstrap state: PASS")
