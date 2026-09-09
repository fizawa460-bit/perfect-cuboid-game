#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
ACTIVE = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
PREFLIGHT = ROOT / "stages/stage32/post1730-o210-v3-main-consumption-preflight.json"
PROOF_PATH = ROOT / "stages/stage32/STAGE32-PROOF-PATH.md"

STATE_CANON = "6fab5e3ba32b5d673353949dfaef466699d469cd89a4d44fcd5bfbfed992a993"
PREFLIGHT_CANON = "b28e95fbeaad0844122fb8fb62722db94cc50ea8cc3130f033a2835d6bd3acd7"
EX3_CORE = "78399b9797723b4134198b2f4b2dc3ed3024897b7ad128d1f0621e1e85cf8102"
ADAPTER_CORE = "55505658e272ec7d60372f2d67cb93c9c007d782145f18d5ef9d2c1146582c88"
O210_CORE = "7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824"


def csha(obj: dict) -> str:
    x = dict(obj); x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    state = json.loads(STATE.read_text())
    active = json.loads(ACTIVE.read_text())
    pre = json.loads(PREFLIGHT.read_text())
    proof_path = PROOF_PATH.read_text(encoding="utf-8")
    assert state["canonical_sha256_without_this_field"] == STATE_CANON and csha(state) == STATE_CANON
    assert pre["canonical_sha256_without_this_field"] == PREFLIGHT_CANON and csha(pre) == PREFLIGHT_CANON

    supporting = {c["claim_id"]: c for c in active["supporting_claims"]}
    claims = {c["claim_id"]: c for c in active["claims"]}
    assert set(supporting) == {
        "S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1",
        "S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3",
    }
    assert "S32.O210.EXCLUSION.V1" not in claims
    ex3 = supporting["S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1"]
    ad = supporting["S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3"]
    o210 = claims["S32.O210.EXCLUSION.V3"]
    assert ex3["claim_core_sha256"] == EX3_CORE and ex3["authority_status"] == "AUDITED"
    assert ex3["audit_receipt"] == {"status":"PASS","pr":1714,"review_id":5141988194,"exact_head":"8da8d4cd932c5c9b82dfd0c304638e866c656069"}
    assert ad["claim_core_sha256"] == ADAPTER_CORE and ad["authority_status"] == "AUDITED"
    assert ad["audit_receipt"] == {"status":"PASS","pr":1714,"review_id":5143014619,"exact_head":"280595ed892ae2ef70e049a3f722ea024452e206"}
    assert o210["claim_core_sha256"] == O210_CORE and o210["authority_status"] == "AUDITED"
    assert o210["audit_receipt"] == {"status":"PASS","pr":1714,"review_id":5147304889,"exact_head":"040dfb6c7e1dc40573866bb10f62e93419121711"}
    assert o210["frontier_status"] == "AUDITED_TRUE" and o210["blockers"] == []
    assert o210["requires"] == [
        "S32.MAIN.CURRENT_TARGET_CONTEXT.V1",
        "S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1",
        "S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3",
    ]

    f = state["current_exact_frontier"]
    assert f["o210_excluded"] is True
    assert f["o210_exclusion_claim_id"] == "S32.O210.EXCLUSION.V3"
    assert f["o210_exclusion_audit_review_id"] == 5147304889
    assert f["q602_excluded"] is False
    assert f["q602_survivors_audited"] == [73,97,235]
    assert f["full178_numerical_census_complete"] is False
    fw = state["firewalls"]
    assert fw["O210_excluded"] is True
    assert fw["Q602_excluded"] is False
    assert fw["O212_plus_advance_allowed"] is False
    assert fw["endpoint_credit"] is False
    assert fw["perfect_cuboid_existence_claim"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False
    a = state["authority_sync"]
    assert a["latest_hostile_audit_review_id"] == 5148641910
    assert a["latest_audited_exact_head"] == "2ad52c41d166d39d7458b6ab228432ba50ed93ce"
    assert a["audited_main_o210_claim_core_sha256"] == O210_CORE

    # Management-layer synchronization is load-bearing after ACTIVE_FRONTIER_REMAP.
    # Fail closed if human-readable proof-path routing regresses to the old O210-open state.
    required_proof_path_tokens = [
        "POST-#1730 O210-V3-CONSUMED FRONTIER",
        "S32.O210.EXCLUSION.V3                       [AUDITED_TRUE]",
        "O210_excluded=true",
        "Q602_excluded=false",
        "Q602_FORGETFUL_O210_POPULATION_ADAPTER_PLUS_FULL178",
        "S32.Q602.EXCLUSION.V1                        [DECLARED_GOAL / OPEN]",
        "O212_plus_advance_allowed=false",
    ]
    for token in required_proof_path_tokens:
        assert token in proof_path, token
    forbidden_proof_path_tokens = [
        "S32.O210.EXCLUSION.V1                       [DECLARED_GOAL / OPEN]",
        "For O210, MAIN must retain and hostile-audit an adapter",
        "This is not an EX3 monodromy proof.",
        "O210_excluded=false",
    ]
    for token in forbidden_proof_path_tokens:
        assert token not in proof_path, token

    print("PASS_STAGE32_POST1730_O210_V3_MAIN_CLAIM_SYNC")
    print("proof_path_post1730_sync=true")
    print(json.dumps({"O210_excluded":True,"Q602_excluded":False,"survivors":[73,97,235],"FULL178_complete":False,"O212_plus":False}, sort_keys=True))


if __name__ == "__main__":
    main()
