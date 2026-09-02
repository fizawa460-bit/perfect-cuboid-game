#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / "34-02"
STATE = ROOT / "MAIN-STATE.json"
PROMO = UNIT / "d2-stageA2-pr1486-q8039-hostile-audit-promotion-certificate.json"
Q84 = UNIT / "d2-stageA2-q8413-two-quotient-rankzero-preaudit-certificate.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


state = load(STATE)
promo = load(PROMO)
q84 = load(Q84)

assert state["schema"] == "STAGE34_EXT_C_MAIN_STATE_V20_D2_STAGEA2_4_BRANCHES_AFTER_PR1486_Q8039_HOSTILE_AUDIT"
assert state["audited_foundation"]["pr1486_q8039_review_id"] == 5086426527
assert state["audited_foundation"]["pr1486_q8039_audited_head"] == "53d0a34fc45594edb2a698cf40914125344e7fd0"
assert state["promotion_gates"]["stage34_02c_q8039_hostile_audit_passed"] is True
assert state["promotion_gates"]["D2_stageA2_q8039_four_branch_closure_complete"] is True
assert state["locked_evidence"]["D2_stageA2_remaining_d1"] == 4
assert state["locked_evidence"]["D2_stageA2_remaining_sign_orbits"] == 2
assert state["locked_evidence"]["D2_stageA2_remaining_d1_by_q"] == {
    "20/99": 0, "24/7": 0, "48/55": 0, "60/11": 0, "80/39": 0, "84/13": 4
}
assert state["locked_evidence"]["D2_stageA2_remaining_representatives"] == [
    "40dc8f63e92a8a3a65e8", "7a7ef1a67e794fe1651f"
]
assert state["locked_evidence"]["D2_stageA2_remaining_sign_partners"] == [
    "8a374a057daf5f92a87e", "98b42307b3aa398f1e0c"
]
assert state["locked_evidence"]["D2_stageA2_q8039_promotion_certificate"]["blob_sha"] == git_blob_sha(PROMO)

assert promo["status"] == "PASS_HOSTILE_AUDIT_PROMOTED_Q8039_FOUR_BRANCHES_8_TO_4"
assert promo["hostile_audit"]["review_id"] == 5086426527
assert promo["promotion"]["closed_branches"] == 4
assert promo["promotion"]["closed_sign_orbits"] == 2
assert promo["authoritative_after"]["remaining_branches"] == 4
assert promo["authoritative_after"]["remaining_sign_orbits"] == 2
assert promo["firewalls"]["q84_13_four_branches_closed"] is False
assert promo["firewalls"]["D2_all_factor_branches_closed"] is False

assert q84["status"] == "PASS_EXACT_Q8413_QUOTIENT_RANKZERO_PREAUDIT_NO_BRANCH_CLOSURE"
assert q84["model38"]["mordell_weil_rank"] == 0
assert q84["model165"]["mordell_weil_rank"] == 0
assert q84["firewalls"]["rational_X_classified"] is False
assert q84["firewalls"]["parent_pullback_classified"] is False
assert q84["firewalls"]["branch_40dc_closed"] is False
assert q84["firewalls"]["branch_7a7_closed"] is False
assert state["promotion_gates"]["D2_stageA2_q8413_parent_pullback_complete"] is False
assert state["promotion_gates"]["D2_all_factor_branches_closed"] is False
assert state["promotion_gates"]["R29_EXT_CHANG_C_closed"] is False
assert state["firewalls"]["q8413_quotient_rankzero_implies_branch_closure"] is False
assert state["firewalls"]["remaining_4_closed"] is False

print("PASS PR1486 q80/39 hostile-audit promotion: authority=4 branches / 2 sign orbits, q84/13 remains OPEN.")
