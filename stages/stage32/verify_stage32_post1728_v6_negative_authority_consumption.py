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

EXPECTED_STATE_CANONICAL = "131982c58dbd265712493230ac943175e5d536b9d6bea5199ee54e547e4191aa"
EXPECTED_REMAP_CANONICAL = "be5fd93e5c8efa0087c10e0773eb0076c28af80a529b1c11b81d80c6c412fffc"
EXPECTED_V6_CORE = "c7927cd86c321de2956b3843dff4882ddeb29fb3489715d4dd7d1d60eff58cc6"
EXPECTED_ADAPTER_CORE = "4e0ec501c299fe0a41699eb6cc377ef977ebed27172f0e6f10a25039d835fe06"
EXPECTED_REVIEW = 5147810198


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
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
    assert v6["authority_status"] == "AUDITED"
    assert v6["claim_core_sha256"] == EXPECTED_V6_CORE
    assert v6["audit_receipt"]["review_id"] == EXPECTED_REVIEW
    assert ad["authority_status"] == "AUDITED"
    assert ad["claim_core_sha256"] == EXPECTED_ADAPTER_CORE
    assert ad["audit_receipt"]["review_id"] == EXPECTED_REVIEW
    assert ex1["authority_status"] == "AUDITED"
    assert ex1["audit_receipt"]["review_id"] == 5147627146

    f = state["current_exact_frontier"]
    assert f["v6_integral_irreducible_genus1_population_empty_audited"] is True
    for key in [
        "v6_actual_member_branch_active",
        "v6_surface_node_multibranch_branch_active",
        "v6_smooth_ambient_locus_curve_singularity_branch_active",
        "v6_same_member_q602_identity_active",
        "absolute_delta0inf_marking_active_for_selected_route",
        "q602_excluded",
        "o210_excluded",
        "full178_numerical_census_complete",
    ]:
        assert f[key] is False
    assert f["q602_survivors_audited"] == [73, 97, 235]

    credit = remap["credit"]
    assert credit["V6_integral_irreducible_genus1_population_empty"] is True
    assert credit["O210_excluded"] is False
    assert credit["Q602_excluded"] is False
    assert credit["Stage32_closed"] is False
    assert remap["firewalls"]["o210_requires_explicit_typed_adapter_and_audit"] is True
    assert remap["firewalls"]["q602_requires_explicit_typed_adapter_and_audit"] is True

    assert state["current"]["next_exact_route"] == remap["remap"]["next_exact_route"]
    print("PASS_STAGE32_POST1728_V6_NEGATIVE_AUTHORITY_CONSUMPTION")
    print(EXPECTED_REMAP_CANONICAL)


if __name__ == "__main__":
    main()
