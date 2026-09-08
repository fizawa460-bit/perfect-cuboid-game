#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-pass-promotion-adapter-preflight-20260909.json"
FRONT = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"

EXPECTED_CANONICAL = "3a462d9f7462f898dd89ff3865a5873bc1bd867abea6191f6803673049e41e0b"
EXPECTED_AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
EXPECTED_REVIEW = 5147627146
EXPECTED_EX1_CORE = "84e7a4b6990d7c687eebe341fbea296fad1da2cae4785cb87580a0d84572437a"


def canonical(x: dict) -> str:
    y = dict(x)
    y.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(y, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def claim(front: dict, cid: str) -> dict:
    return next(c for c in front["claims"] if c["claim_id"] == cid)


def main() -> None:
    a = json.loads(ART.read_text())
    assert a["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert canonical(a) == EXPECTED_CANONICAL
    assert a["audit_input"]["exact_head"] == EXPECTED_AUDITED_HEAD
    assert a["audit_input"]["review_id"] == EXPECTED_REVIEW
    assert a["audit_input"]["claim_core_sha256"] == EXPECTED_EX1_CORE
    assert a["audit_input"]["verdict"] == "PASS"

    front = json.loads(FRONT.read_text())
    v6 = claim(front, "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1")
    o210 = claim(front, "S32.O210.EXCLUSION.V1")
    surv = claim(front, "S32.Q602.SURVIVORS_73_97_235.V1")
    q602 = claim(front, "S32.Q602.EXCLUSION.V1")
    same = claim(front, "S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V2")

    assert v6["scope_key"] == "S32.MAIN.V6_CARRIER"
    assert v6["scope"]["picard_class"] == "V6"
    assert v6["scope"]["target"] == "population_wide_nonexistence"
    assert v6["authority_status"] == "DECLARED_GOAL"

    assert o210["scope_key"] == "S32.O210.COVER"
    assert o210["scope"]["picard_class"] == "V6"
    assert o210["scope"]["O"] == 210
    assert "population-preserving argument" in o210["statement"]

    assert surv["scope"]["surviving_residues"] == [73, 97, 235]
    assert surv["authority_status"] == "AUDITED"
    assert q602["scope_key"] == "S32.Q602.ARITHMETIC"
    assert q602["scope"]["input_survivors"] == [73, 97, 235]
    assert "equally exact population-preserving obstruction" in q602["statement"]

    assert same["scope_key"] == "S32.MAIN.V6_CARRIER"
    assert same["frontier_status"] == "BLOCKED_OPEN_GOAL"

    ids = [x["candidate_claim_id"] for x in a["candidate_adapters"]]
    assert ids == [
        "S32.ADAPTER.EX1_V6_TERMINAL_TO_MAIN_V6_NO_MEMBER.V1",
        "S32.ADAPTER.MAIN_V6_EMPTY_TO_O210_EMPTY.V1",
        "S32.ADAPTER.MAIN_V6_EMPTY_TO_Q602_EMPTY.V1",
    ]
    assert all(x["promotion_granted_now"] is False for x in a["candidate_adapters"])
    assert all(x["status_needed_for_consumption"] == "AUDITED" for x in a["candidate_adapters"])

    gate = a["authority_gate"]
    assert gate["hostile_pass_known"] is True
    assert gate["claim_sync_triggered"] is True
    assert gate["ex1_consumable_audited_authority_before_sync"] is False
    assert gate["concrete_promotion_adapters_registered"] is False
    assert a["firewalls"]["MAIN_credit_changed"] is False
    assert a["firewalls"]["Q602_excluded"] is False
    assert a["firewalls"]["O210_excluded"] is False

    print("PASS_STAGE32_MAIN_EX1_PASS_PROMOTION_ADAPTER_PREFLIGHT")
    print(EXPECTED_CANONICAL)


if __name__ == "__main__":
    main()
