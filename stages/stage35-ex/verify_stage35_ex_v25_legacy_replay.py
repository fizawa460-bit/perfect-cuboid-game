#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers through the exact audited V24 projection.

The real V25 state promotes user-confirmed hostile-PASS 35EX-25, records the
mandatory 25B fresh breadth audit, and advances current to 35EX-26. Historical
base/10--25 mathematics remains replayed against the exact V24 state that was
certified at final 35EX-25 head 7a2d70e04dcd679881630267cb2e1810f209e44c.
"""
from __future__ import annotations

import copy
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
V25 = "STAGE35_EX_PESCH_E1_STATE_V25_POST_35EX26_BASE_INVOLUTION_RECEIVER_DESCENT"
V24 = "STAGE35_EX_PESCH_E1_STATE_V24_POST_35EX25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER"
ALLOWED = {"base", *{str(i) for i in range(10, 26)}}
CURRENT_MAIN = "4ec2b9af886f9ac9be13c3324788c26625c9e5d9"
AUDITED_V24_BASE = "0e7d0b282ec8b15c888a1efe4de43a114f4d5911"

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit("usage: verify_stage35_ex_v25_legacy_replay.py {base|10|...|25}")

target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real["schema"] == V25
assert real["stage"] == "35-EX"
assert real["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert real["base_main_sha"] == CURRENT_MAIN

parent = real["parent_authority"]
assert parent["unit"] == "35EX-25"
assert parent["status"] == "AUDITED_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["pass_source"] == "USER_CONFIRMED_AFTER_FRESHNESS_ONLY_REPAIR"
assert parent["audited_head_sha"] == "7a2d70e04dcd679881630267cb2e1810f209e44c"
assert parent["merged_main_sha"] == "3cadfd55d91f1e3267f31f9d7384b62d38678cc3"
assert parent["audited_theorem_credit"] is False

assert real["completed_units"]["35EX-25"]["status"] == "AUDITED_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
assert real["completed_units"]["35EX-25B"]["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert real["completed_units"]["35EX-26"]["status"] == "PROVISIONAL_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT"
assert real["current"]["unit"] == "35EX-26_BASE_INVOLUTION_RECEIVER_DESCENT_OR_NO_REDUCTION_BLOCKER"
assert real["current"]["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
assert real["claims"]["stage35_closed"] is False
assert real["claims"]["E1_proved"] is False

projected = copy.deepcopy(real)
projected["schema"] = V24
projected["base_main_sha"] = AUDITED_V24_BASE
projected["parent_authority"] = {
    "unit": "35EX-24",
    "status": "AUDITED_EXACT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_NO_CREDIT",
    "hostile_audit_verdict": "PASS",
    "hostile_audit_review": 5112867152,
    "audited_head_sha": "529c550c742e75025cdcc1a6b9666582f26697a1",
    "merged_main_sha": "81569110952b348692e688c5e1d7148dca10b163",
    "audited_theorem_credit": False,
}

u24b = copy.deepcopy(projected["completed_units"]["35EX-24B"])
u24b["status"] = "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
for key in ("hostile_audit_verdict", "pass_source", "audited_head_sha", "merged_main_sha"):
    u24b.pop(key, None)
projected["completed_units"]["35EX-24B"] = u24b

u25 = copy.deepcopy(projected["completed_units"]["35EX-25"])
u25["status"] = "PROVISIONAL_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
for key in ("hostile_audit_verdict", "pass_source", "audited_head_sha", "merged_main_sha"):
    u25.pop(key, None)
projected["completed_units"]["35EX-25"] = u25
projected["completed_units"].pop("35EX-25B", None)
projected["completed_units"].pop("35EX-26", None)

projected["resolved_investigations"]["CURRENT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER"] = {
    "status": "PROVISIONAL_PASS_NEW_GATE_PENDING_HOSTILE_AUDIT",
    "reason": "the exact C lift is equivalent to one Eplus point with X, X+1, X+a, X+1+a simultaneously square; pair-isogeny lift conditions and Eminus reconstruct automatically",
    "reopen_condition": "hostile audit may revoke this provisional stronger gate; after PASS run the required fresh breadth audit before selecting an arithmetic successor",
}
projected["resolved_investigations"].pop("CURRENT_BASE_INVOLUTION_RECEIVER_DESCENT", None)
projected.pop("candidate_ledger_after_35ex25_breadth_audit", None)
projected["current"] = {
    "unit": "35EX-25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_OR_KUMMER_INTERSECTION",
    "status": "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT",
    "candidate": "E1-SIMULTANEOUS-ELLIPTIC-KUMMER-LIFT-COMPATIBILITY",
    "result": "PASS_NEW_GATE_SINGLE_MOVING_EPLUS_FOUR_SQUARE_RECEIVER_PENDING_HOSTILE_AUDIT",
    "next_if_audited_pass": "FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION",
    "working_set": [
        "stages/stage35-ex/35ex-24/post-isogeny-compression-breadth-audit.json",
        "stages/stage35-ex/35ex-25/single-elliptic-full-square-receiver.md",
        "stages/stage35-ex/35ex-25/single-elliptic-full-square-certificate.json",
        "stages/stage35-ex/verify_stage35_ex_25.py",
        "docs/arsenal/cards/formal/S34-W03.md",
        "stages/stage35-ex/MAIN-STATE.json",
    ],
}
projected["arsenal"] = {
    "S34_W01": "FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT",
    "S34_W03": "EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_ROUTER_MATCH_INTERSECTION_NOT_CLOSED",
    "S31_W01": "GENUS_ONE_CHARACTER_QUOTIENT_FIBERWISE_ROUTING_ONLY_NO_UNIFORM_SURFACE_CLOSURE",
    "S34_W02": "LOCKED_NO_GLOBAL_FINITE_REDUCTION_OR_UNIFORM_FULL_MW",
    "S33_PW07": "PROVISIONAL_ROUTING_ONLY_REQUIRES_EXISTING_BRAUER_REPRESENTATIVE_COMMON_COCYCLE_AND_TORSOR_NOT_A_CLASS_CONSTRUCTOR",
    "matching_global_reciprocity_Hilbert_Jacobi_card_found": False,
    "matching_formal_gaussian_coordinate_gcd_split_card_found": False,
    "matching_formal_nonisotrivial_surface_closure_card_found": False,
    "matching_formal_global_surface_classification_card_found": False,
    "matching_formal_global_surface_or_brauer_closure_card_found": False,
    "matching_formal_isogeny_twist_compression_card_found": False,
    "matching_formal_uniform_elliptic_surface_specialization_card_found": False,
    "matching_formal_uniform_moving_family_kummer_closure_card_found": False,
    "S34_W03_simultaneous_kummer_router_after_dictionary": True,
    "S34_W03_single_elliptic_receiver_router_after_dictionary": True,
    "stage34_concrete_coefficients_branches_and_local_primes_transfer": False,
}

original_read_text = Path.read_text
state_resolved = STATE.resolve()

def projected_read_text(self: Path, *args, **kwargs):
    if self.resolve() == state_resolved:
        return json.dumps(projected)
    return original_read_text(self, *args, **kwargs)

Path.read_text = projected_read_text
try:
    if target == "25":
        runpy.run_path(str(ROOT / "stages/stage35-ex/verify_stage35_ex_25.py"), run_name="__main__")
    else:
        old_argv = sys.argv[:]
        try:
            sys.argv = ["verify_stage35_ex_v24_legacy_replay.py", target]
            runpy.run_path(
                str(ROOT / "stages/stage35-ex/verify_stage35_ex_v24_legacy_replay.py"),
                run_name="__main__",
            )
        finally:
            sys.argv = old_argv
finally:
    Path.read_text = original_read_text

print(f"PASS V25_SUCCESSOR_PROJECTION_REPLAY_35EX_{target}")
