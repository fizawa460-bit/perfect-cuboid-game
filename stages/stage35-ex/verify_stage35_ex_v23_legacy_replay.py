#!/usr/bin/env python3
"""Run a historical Stage35-EX verifier against the V22 authority projection.

The V23 state changes only the active parent/current route after 35EX-23 audit.
Historical completed_units, freezes, ledgers and artifacts remain the real V23
payload.  This adapter projects only schema/base/parent/current back to the
last state understood by the legacy 20/21/22 verifiers, then runs their full
original code unchanged.  It first verifies the real V23 successor authority.
"""
from __future__ import annotations

import copy
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
V23 = "STAGE35_EX_PESCH_E1_STATE_V23_POST_35EX24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION"
V22 = "STAGE35_EX_PESCH_E1_STATE_V22_POST_35EX23_GENUS5_CHARACTER_QUOTIENT_UNIFORMITY_BLOCKER"
ALLOWED = {"20", "21", "22"}

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit("usage: verify_stage35_ex_v23_legacy_replay.py {20|21|22}")

target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real["schema"] == V23
assert real["stage"] == "35-EX"
assert real["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert real["base_main_sha"] in {
    "c20ee71d91af850103fd7406f9b1072448a11fcf",
    "5ed32fa53bdecb735f461d7c27e85851d9ad8c21",
}
parent = real["parent_authority"]
assert parent["unit"] == "35EX-23"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["hostile_audit_review"] == 5111910947
assert parent["audited_head_sha"] == "77ff0a6cf51679bd64525a0be843fcd1eed77d8e"
assert parent["merged_main_sha"] == "c20ee71d91af850103fd7406f9b1072448a11fcf"
assert parent["audited_theorem_credit"] is False
assert real["completed_units"]["35EX-23"]["status"] == "AUDITED_EXACT_GENUS5_CHARACTER_QUOTIENT_FIVE_ELLIPTIC_UNIFORMITY_BLOCKER_NO_CREDIT"
assert real["current"]["unit"] == "35EX-24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_OR_INDEPENDENT_CHANNEL_BLOCKER"
assert real["current"]["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
assert real["claims"]["stage35_closed"] is False
assert real["claims"]["E1_proved"] is False

# Project only the successor-routing fields.  All historical mathematics and
# artifacts remain the values from the real V23 state.
projected = copy.deepcopy(real)
projected["schema"] = V22
projected["base_main_sha"] = "7a5d01b438c68c228ad73955f906f3128780d6ef"
projected["parent_authority"] = {
    "unit": "35EX-22",
    "status": "AUDITED_EXACT_OBVIOUS_BRAUER_SYMBOL_LAYER_BLOCKER_NO_CREDIT",
    "hostile_audit_verdict": "PASS",
    "hostile_audit_review": 5111539148,
    "audited_head_sha": "f4276680239bb2b84687f8ba8ac8964de0613552",
    "merged_main_sha": "2e07dde92fdf270fff1233635a7cb4cea1427080",
    "audited_theorem_credit": False,
}
projected["current"] = {
    "unit": "35EX-23_GENUS5_MULTIQUADRATIC_CHARACTER_QUOTIENT_DESCENT_OR_UNIFORMITY_BLOCKER",
    "status": "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT",
    "candidate": "E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT",
    "result": "FROZEN_AT_NONISOTRIVIAL_FIVE_ELLIPTIC_COMPATIBILITY_LAYER_PENDING_HOSTILE_AUDIT",
    "next_if_audited_pass": "FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION",
    "working_set": [
        "stages/stage35-ex/35ex-23/genus5-character-quotient-uniformity-blocker.md",
        "stages/stage35-ex/35ex-23/character-quotient-certificate.json",
        "stages/stage35-ex/verify_stage35_ex_23.py",
        "stages/stage35-ex/MAIN-STATE.json",
    ],
}

original_read_text = Path.read_text
state_resolved = STATE.resolve()

def projected_read_text(self: Path, *args, **kwargs):
    if self.resolve() == state_resolved:
        return json.dumps(projected)
    return original_read_text(self, *args, **kwargs)

Path.read_text = projected_read_text
try:
    runpy.run_path(str(ROOT / f"stages/stage35-ex/verify_stage35_ex_{target}.py"), run_name="__main__")
finally:
    Path.read_text = original_read_text

print(f"PASS V23_SUCCESSOR_PROJECTION_REPLAY_35EX_{target}")
