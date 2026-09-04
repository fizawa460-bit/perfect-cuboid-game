#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers through the exact audited V23 projection.

The real V24 state promotes hostile-audited 35EX-24, records the mandatory 24B
breadth audit, and advances current to 35EX-25. Historical base/10--24
mathematics must remain replayable without weakening their original checks.
This adapter first validates the real V24 successor authority, then restores
all V24-mutated routing/authority fields to the exact V23 values audited at
35EX-24 head 529c550c742e75025cdcc1a6b9666582f26697a1.
"""
from __future__ import annotations

import copy
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
V24 = "STAGE35_EX_PESCH_E1_STATE_V24_POST_35EX25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER"
V23 = "STAGE35_EX_PESCH_E1_STATE_V23_POST_35EX24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION"
ALLOWED = {"base", *{str(i) for i in range(10, 25)}}

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit("usage: verify_stage35_ex_v24_legacy_replay.py {base|10|...|24}")

target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real["schema"] == V24
assert real["stage"] == "35-EX"
assert real["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert real["base_main_sha"] == "0981f00bcafd8870508030c1b3733b28d5f36c05"
parent = real["parent_authority"]
assert parent["unit"] == "35EX-24"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["hostile_audit_review"] == 5112867152
assert parent["audited_head_sha"] == "529c550c742e75025cdcc1a6b9666582f26697a1"
assert parent["merged_main_sha"] == "81569110952b348692e688c5e1d7148dca10b163"
assert parent["audited_theorem_credit"] is False
assert real["completed_units"]["35EX-24"]["status"] == "AUDITED_EXACT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_NO_CREDIT"
assert real["completed_units"]["35EX-24B"]["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert real["completed_units"]["35EX-25"]["status"] == "PROVISIONAL_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
assert real["current"]["unit"] == "35EX-25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_OR_KUMMER_INTERSECTION"
assert real["current"]["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
assert real["claims"]["stage35_closed"] is False
assert real["claims"]["E1_proved"] is False

projected = copy.deepcopy(real)
projected["schema"] = V23
projected["base_main_sha"] = "8c59c81bcf0bcd442705cfb7a3db297253b34679"
projected["parent_authority"] = {
    "unit": "35EX-23",
    "status": "AUDITED_EXACT_GENUS5_CHARACTER_QUOTIENT_FIVE_ELLIPTIC_UNIFORMITY_BLOCKER_NO_CREDIT",
    "hostile_audit_verdict": "PASS",
    "hostile_audit_review": 5111910947,
    "audited_head_sha": "77ff0a6cf51679bd64525a0be843fcd1eed77d8e",
    "merged_main_sha": "c20ee71d91af850103fd7406f9b1072448a11fcf",
    "audited_theorem_credit": False,
}

u23b = copy.deepcopy(projected["completed_units"]["35EX-23B"])
u23b["status"] = "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
for key in ("hostile_audit_verdict", "hostile_audit_review", "audited_head_sha", "merged_main_sha"):
    u23b.pop(key, None)
projected["completed_units"]["35EX-23B"] = u23b

u24 = copy.deepcopy(projected["completed_units"]["35EX-24"])
u24["status"] = "PROVISIONAL_EXACT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_NO_CREDIT"
for key in ("hostile_audit_verdict", "hostile_audit_review", "audited_head_sha", "merged_main_sha"):
    u24.pop(key, None)
projected["completed_units"]["35EX-24"] = u24
projected["completed_units"].pop("35EX-24B", None)
projected["completed_units"].pop("35EX-25", None)

projected["resolved_investigations"]["CURRENT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION"] = {
    "status": "PROVISIONAL_PASS_NEW_GATE_PENDING_HOSTILE_AUDIT",
    "reason": "the five quotient factors are not five unrelated moving shapes: exact pair-quartic adapters and kernel-2 isogenies give two fixed minus-one twist pairs plus Eminus over K and multiplicities 2,2,1 over K(i); the three representatives remain nonisotrivial",
    "reopen_condition": "hostile audit may revoke this provisional stronger gate; after PASS run the required fresh breadth audit before selecting an arithmetic successor",
}
projected["resolved_investigations"].pop("CURRENT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER", None)
projected.pop("candidate_ledger_after_35ex24_breadth_audit", None)
projected["current"] = {
    "unit": "35EX-24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_OR_INDEPENDENT_CHANNEL_BLOCKER",
    "status": "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT",
    "candidate": "E1-FIVE-ELLIPTIC-ISOGENY-TWIST-COMPRESSION",
    "result": "PASS_NEW_GATE_TWO_FIXED_MINUS1_TWIST_PAIRS_PLUS_EMINUS_PENDING_HOSTILE_AUDIT",
    "next_if_audited_pass": "FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION",
    "working_set": [
        "stages/stage35-ex/35ex-23/post-five-elliptic-breadth-audit.json",
        "stages/stage35-ex/35ex-24/five-elliptic-isogeny-twist-compression.md",
        "stages/stage35-ex/35ex-24/isogeny-twist-certificate.json",
        "stages/stage35-ex/verify_stage35_ex_24.py",
        "docs/arsenal/cards/formal/S31-W01.md",
        "docs/arsenal/cards/formal/S34-W03.md",
        "stages/stage35-ex/MAIN-STATE.json",
    ],
}
projected["arsenal"] = {
    "S34_W01": "FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT",
    "S34_W03": "EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED_CURRENT_DIRECT_LOCAL_ROUTE_FROZEN_INTERSECTION_NOT_CLOSED",
    "S31_W01": "GENUS_ONE_CHARACTER_QUOTIENT_FIBERWISE_ROUTING_ONLY_NO_UNIFORM_SURFACE_CLOSURE",
    "S34_W02": "LOCKED_NO_GLOBAL_FINITE_REDUCTION",
    "S33_PW07": "PROVISIONAL_ROUTING_ONLY_REQUIRES_EXISTING_BRAUER_REPRESENTATIVE_COMMON_COCYCLE_AND_TORSOR_NOT_A_CLASS_CONSTRUCTOR",
    "matching_global_reciprocity_Hilbert_Jacobi_card_found": False,
    "matching_formal_gaussian_coordinate_gcd_split_card_found": False,
    "matching_formal_nonisotrivial_surface_closure_card_found": False,
    "matching_formal_global_surface_classification_card_found": False,
    "matching_formal_global_surface_or_brauer_closure_card_found": False,
    "matching_formal_isogeny_twist_compression_card_found": False,
    "matching_formal_uniform_elliptic_surface_specialization_card_found": False,
    "S34_W03_simultaneous_kummer_router_after_dictionary": True,
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
    if target == "base":
        runpy.run_path(str(ROOT / "stages/stage35-ex/verify_stage35_ex.py"), run_name="__main__")
    elif target in {"20", "21", "22", "23"}:
        old_argv = sys.argv[:]
        try:
            sys.argv = ["verify_stage35_ex_v23_legacy_replay.py", target]
            runpy.run_path(
                str(ROOT / "stages/stage35-ex/verify_stage35_ex_v23_legacy_replay.py"),
                run_name="__main__",
            )
        finally:
            sys.argv = old_argv
    else:
        runpy.run_path(
            str(ROOT / f"stages/stage35-ex/verify_stage35_ex_{target}.py"),
            run_name="__main__",
        )
finally:
    Path.read_text = original_read_text

print(f"PASS V24_SUCCESSOR_PROJECTION_REPLAY_35EX_{target}")
