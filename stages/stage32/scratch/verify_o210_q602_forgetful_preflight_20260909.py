#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "o210-q602-forgetful-preflight-20260909.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"

EXPECTED_CANONICAL = "52bc9c8ba3fe2e81dbe2e29992cd4e44cdac6ce886a401eb4ea7ecbea42269a5"


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    art = json.loads(ART.read_text())
    assert art["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert csha(art) == EXPECTED_CANONICAL
    assert art["status"] == "SCRATCH_PREFLIGHT_NO_AUTHORITY_NO_CLAIM_SYNC"

    frontier = json.loads(FRONTIER.read_text())
    claims = {c["claim_id"]: c for c in frontier["claims"]}
    q = claims["S32.Q602.EXCLUSION.V1"]
    s = claims["S32.Q602.SURVIVORS_73_97_235.V1"]

    expected_q = art["current_q602_goal"]
    assert q["claim_core_sha256"] == expected_q["claim_core_sha256"]
    assert q["scope_key"] == expected_q["scope_key"]
    assert q["scope"]["row_id"] == expected_q["row_id"] == "g1-d186"
    assert q["scope"]["O"] == expected_q["O"] == 210
    assert q["scope"]["Q"] == expected_q["Q"] == 602
    assert q["scope"]["input_survivors"] == expected_q["input_survivors"] == [73, 97, 235]
    assert q["authority_status"] == "DECLARED_GOAL"
    assert q["frontier_status"] == "OPEN_GOAL"

    assert s["claim_core_sha256"] == art["audited_survivor_input"]["claim_core_sha256"]
    assert s["authority_status"] == "AUDITED"
    assert s["scope"]["surviving_residues"] == [73, 97, 235]

    o = art["audited_o210_handoff"]
    assert o["source_pr"] == 1714
    assert o["claim_id"] == "S32.O210.EXCLUSION.V3"
    assert o["claim_core_sha256"] == "7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824"
    assert o["audit_receipt"] == {
        "status": "PASS",
        "review_id": 5147304889,
        "exact_head": "040dfb6c7e1dc40573866bb10f62e93419121711",
    }
    assert o["main_routing_credit_consumed"] is False

    m = art["typed_forgetful_map"]
    assert m["total_on_domain"] is True
    assert "Q602" in m["domain"] and "O210" in m["codomain"]

    lc = art["logical_consequence"]
    assert lc["o210_population_empty_implies_q602_admissible_population_empty"] is True
    assert lc["survivor_arithmetic_receipt_revoked"] is False
    assert lc["historical_survivors_remain_valid_conditional_arithmetic_data"] is True
    assert lc["candidate_new_adapter_claim_id"] == "S32.ADAPTER.O210_EMPTY_TO_Q602_ADMISSIBLE_EMPTY.V1"
    assert lc["candidate_new_q602_claim_id"] == "S32.Q602.EXCLUSION.V2"

    state = json.loads(MAIN.read_text())
    assert state["firewalls"]["O210_excluded"] is False
    assert state["firewalls"]["Q602_excluded"] is False
    assert state["current"]["stacked_candidate_audit_status"] == "POST1728_ACTIVE_FRONTIER_REMAP_AUDIT_REQUIRED"

    gate = art["promotion_gate"]
    assert gate["pr1730_hostile_reaudit_pass_required_before_main_authority_mutation"] is True
    assert gate["o210_v3_must_be_consumed_into_current_main_routing_first"] is True
    assert gate["q602_adapter_requires_separate_hostile_audit"] is True
    assert gate["scratch_grants_o210_credit"] is False
    assert gate["scratch_grants_q602_credit"] is False
    assert gate["scratch_changes_active_frontier"] is False

    assert all(v is False for v in art["firewalls"].values())
    print("PASS_STAGE32_SCRATCH_O210_TO_Q602_FORGETFUL_PREFLIGHT")
    print(EXPECTED_CANONICAL)


if __name__ == "__main__":
    main()
