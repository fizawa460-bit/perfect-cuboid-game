#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / "34-02"
STATE = ROOT / "MAIN-STATE.json"
PROMO = UNIT / "d2-stageA2-pr1486-q8039-hostile-audit-promotion-certificate.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


state = load(STATE)
promo = load(PROMO)

# Historical integrity only. Do not freeze the later Stage34 schema/residual state.
assert state["schema"].startswith("STAGE34_EXT_C_MAIN_STATE_")
assert state["audited_foundation"]["pr1486_q8039_review_id"] == 5086426527
assert state["audited_foundation"]["pr1486_q8039_audited_head"] == "53d0a34fc45594edb2a698cf40914125344e7fd0"
assert state["promotion_gates"]["stage34_02c_q8039_hostile_audit_passed"] is True
assert state["promotion_gates"]["D2_stageA2_q8039_four_branch_closure_complete"] is True
assert state["locked_evidence"]["D2_stageA2_q8039_promotion_certificate"]["blob_sha"] == git_blob_sha(PROMO)
assert state["locked_evidence"]["D2_stageA2_q8039_closed_branch_ids"] == [
    "169f94dd000a9c5c053f",
    "b870eb75fe3db7bf6a04",
    "99448685b81e29427c3f",
    "d4f551f1038c705e3a16",
]

assert promo["status"] == "PASS_HOSTILE_AUDIT_PROMOTED_Q8039_FOUR_BRANCHES_8_TO_4"
assert promo["hostile_audit"]["review_id"] == 5086426527
assert promo["promotion"]["closed_branches"] == 4
assert promo["promotion"]["closed_sign_orbits"] == 2
assert promo["authoritative_before"]["remaining_branches"] == 8
assert promo["authoritative_after"]["remaining_branches"] == 4
assert promo["authoritative_after"]["remaining_sign_orbits"] == 2
assert promo["firewalls"]["q84_13_four_branches_closed"] is False
assert promo["firewalls"]["D2_all_factor_branches_closed"] is False

print("PASS historical PR1486 q80/39 hostile-audit promotion integrity; later Stage34 state may advance independently.")
