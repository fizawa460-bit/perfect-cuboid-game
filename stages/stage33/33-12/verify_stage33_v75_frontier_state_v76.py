#!/usr/bin/env python3
"""Verify Stage33 V76 live startup/state/roadmap alignment at the V75 frontier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
ROADMAP = STAGE / "ROADMAP-33-12-V71-J1-TORSOR.md"
V75 = HERE / "e3-b1-c22-j1-generic-quotient-discriminator-rejection-v75.json"

STATE_SHA = "4398106ccb793a69b728318aa6894c105c3803bc218a160d082faec823ceea37"
V75_BLOB = "6d316b60c933b446004297d9d32d0a7ef6c1c357"
V75_SHA = "22b166d44d516a5e0cb57bf582a21144d40b0035489a29036f86dc0944ce1192"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert obj.get("canonical_sha256") == expected == csha(obj), path
    return obj

state = locked(STATE, STATE_SHA)
assert git_blob_sha(V75) == V75_BLOB
v75 = locked(V75, V75_SHA)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V24_V75_J1_GLOBAL_INTEGRAL_KERNEL_INTERFACE_ACTIVE"
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["frontier_authority"] == "V75_J1_GENERIC_QUOTIENT_DISCRIMINATOR_REJECTION"
assert state["branch_exact_frontier_authority"].endswith("e3-b1-c22-j1-generic-quotient-discriminator-rejection-v75.json")
assert state["current"]["active_missing_interface"] == "J1_SPECIFIC_COMPACTIFIED_SURFACE_INTEGRAL_KERNEL_OR_PRIMITIVE_PULLBACK_IDENTIFICATION"
assert state["current"]["next_exact_leaf"] == "D2_2_MATERIALIZE_J1_SPECIFIC_GLOBAL_COMPONENT_GLUE_OR_EQUIVALENT_INTEGRAL_KERNEL_FINGERPRINT"
assert state["current_exact_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert state["current_exact_frontier"]["J1_marked_kc_remaining_ambiguity_bits"] == 1
assert state["current_exact_frontier"]["j1_translation_torsor_materialized"] is True
assert state["current_exact_frontier"]["j1_generic_quotient_d_independent"] is True
assert state["current_exact_frontier"]["j1_generic_quotient_discriminator_sufficient"] is False
assert state["current_exact_frontier"]["j1_j2_r4_lattice_transplant_rejected"] is True
assert state["current_exact_frontier"]["j1_twisted_kernel_minimum_norm_materialized"] is False
assert state["locked_facts"]["v75"]["sha256"] == V75_SHA
assert state["resolved_investigations"]["j1_generic_translation_quotient_discriminator"] == "REJECTED_EXACT_D_INDEPENDENT_V75_DO_NOT_REOPEN_WITHOUT_SURFACE_LEVEL_DATUM"
assert state["anti_loop_policy"]["do_not_transplant_j2_r4_lattice_from_d_independent_generic_quotient_to_j1"] is True
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

assert v75["generic_quotient_replay"]["d_survives_in_quotient_equation"] is False
assert v75["nonportable_j2_lattice_step"]["j2_exact_result"]["minimum_norm"] == 8
assert v75["nonportable_j2_lattice_step"]["v65_exact_j1_gate"]["allowed_minimum_norms"] == [4, 12]
assert v75["exact_missing_interface"]["generic_function_field_quotient_alone_sufficient"] is False
assert v75["next_kernel_contract"]["minimum_norm_materialized"] is False
assert v75["next_kernel_contract"]["marked_kc_coordinate_selected"] is False

start = START.read_text(encoding="utf-8")
roadmap = ROADMAP.read_text(encoding="utf-8")
assert "Current exact frontier: V75" in start
assert "D2.2 remains CURRENT after V75" in start
assert "J1_SPECIFIC_COMPACTIFIED_SURFACE_INTEGRAL_KERNEL_OR_PRIMITIVE_PULLBACK_IDENTIFICATION" in start
assert "Do not reuse the retained J2 minimum norm `8`" in start
assert "S33-PW07" in start and "S33-PW04" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V75_WITH_V68_V69_TRANSPORT_REDUCTION" in roadmap
assert "CURRENT_LEAF=D2_2_MATERIALIZE_J1_SPECIFIC_GLOBAL_INTEGRAL_KERNEL" in roadmap
assert "D2.2a — generic quotient discriminator — REJECTED V75" in roadmap
assert "D2.2b — J1-specific global integral kernel — CURRENT" in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V76_STAGE33_V75_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v75_canonical_sha256": V75_SHA,
    "remaining_transport_bits": 1,
    "current_leaf": state["current"]["active_missing_interface"],
    "advance_allowed": True,
    "merge_allowed": False
}, sort_keys=True))
