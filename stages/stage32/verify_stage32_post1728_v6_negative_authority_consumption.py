#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
REMAP = HERE / "post1728-v6-negative-authority-consumption-and-frontier-remap.json"
REG = HERE / "proof" / "CLAIM-REGISTRY.json"

EXPECTED_STATE_CANONICAL = "6fab5e3ba32b5d673353949dfaef466699d469cd89a4d44fcd5bfbfed992a993"
EXPECTED_REMAP_CANONICAL = "be5fd93e5c8efa0087c10e0773eb0076c28af80a529b1c11b81d80c6c412fffc"
EXPECTED_V6_CORE = "c7927cd86c321de2956b3843dff4882ddeb29fb3489715d4dd7d1d60eff58cc6"
EXPECTED_ADAPTER_CORE = "4e0ec501c299fe0a41699eb6cc377ef977ebed27172f0e6f10a25039d835fe06"
EXPECTED_REVIEW = 5147810198


def csha(obj: dict) -> str:
    body = dict(obj); body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def by_id(reg: dict, cid: str) -> dict:
    return next(x for x in reg["claims"] if x["claim_id"] == cid)


def main() -> None:
    state = json.loads(STATE.read_text())
    remap = json.loads(REMAP.read_text())
    reg = json.loads(REG.read_text())
    assert state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V2_POST1728_V6_NEGATIVE_AUTHORITY_CONSUMED"
    assert state["canonical_sha256_without_this_field"] == EXPECTED_STATE_CANONICAL
    assert csha(state) == EXPECTED_STATE_CANONICAL
    assert remap["canonical_sha256_without_this_field"] == EXPECTED_REMAP_CANONICAL
    assert csha(remap) == EXPECTED_REMAP_CANONICAL

    v6 = by_id(reg, "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2")
    ad = by_id(reg, "S32.ADAPTER.EX1_V6_CARRIER_TO_MAIN_V6_CARRIER.V1")
    ex1 = by_id(reg, "S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V2")
    assert v6["authority_status"] == "AUDITED" and v6["claim_core_sha256"] == EXPECTED_V6_CORE
    assert v6["audit_receipt"]["review_id"] == EXPECTED_REVIEW
    assert ad["authority_status"] == "AUDITED" and ad["claim_core_sha256"] == EXPECTED_ADAPTER_CORE
    assert ad["audit_receipt"]["review_id"] == EXPECTED_REVIEW
    assert ex1["authority_status"] == "AUDITED" and ex1["audit_receipt"]["review_id"] == 5147627146

    f = state["current_exact_frontier"]
    assert f["v6_integral_irreducible_genus1_population_empty_audited"] is True
    for key in ["v6_actual_member_branch_active","v6_surface_node_multibranch_branch_active","v6_smooth_ambient_locus_curve_singularity_branch_active","v6_same_member_q602_identity_active","absolute_delta0inf_marking_active_for_selected_route","q602_excluded","full178_numerical_census_complete"]:
        assert f[key] is False
    assert f["q602_survivors_audited"] == [73,97,235]
    # The post-1728 artifact is an immutable historical remap checkpoint: it
    # correctly had O210/Q602 false. MAIN may subsequently advance O210 only
    # through a separately audited claim-sync, which is now recorded in state.
    assert remap["credit"]["O210_excluded"] is False
    assert remap["credit"]["Q602_excluded"] is False
    assert remap["credit"]["Stage32_closed"] is False
    assert f["o210_excluded"] is True
    assert f["o210_exclusion_claim_id"] == "S32.O210.EXCLUSION.V3"
    assert state["firewalls"]["O210_excluded"] is True
    assert state["firewalls"]["Q602_excluded"] is False
    assert state["firewalls"]["O212_plus_advance_allowed"] is False
    print("PASS_STAGE32_POST1728_V6_NEGATIVE_AUTHORITY_CONSUMPTION")
    print(EXPECTED_REMAP_CANONICAL)


if __name__ == "__main__":
    main()
