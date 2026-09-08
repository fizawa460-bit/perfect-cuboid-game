#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-to-main-v6-scope-adapter-20260909.json"
EX1_STATE = ROOT / "stages/stage32-ex1/MAIN-STATE.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"

EXPECTED_CANONICAL = "2aef25c9ed086435933d5e05aaa7dab1467bb4f39af2d81033026e2f29229fe5"
EXPECTED_EX1_CORE = "84e7a4b6990d7c687eebe341fbea296fad1da2cae4785cb87580a0d84572437a"
EXPECTED_AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
EXPECTED_REVIEW = 5147627146


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def by_id(payload: dict, claim_id: str) -> dict:
    return next(c for c in payload["claims"] if c["claim_id"] == claim_id)


def main() -> None:
    art = json.loads(ART.read_text())
    ex1 = json.loads(EX1_STATE.read_text())
    main_state = json.loads(MAIN_STATE.read_text())
    registry = json.loads(REGISTRY.read_text())
    frontier = json.loads(FRONTIER.read_text())

    assert art["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert canonical(art) == EXPECTED_CANONICAL
    assert art["base"]["audited_ex1_head"] == EXPECTED_AUDITED_HEAD
    assert art["base"]["review_id"] == EXPECTED_REVIEW
    assert art["source_claim"]["claim_core_sha256"] == EXPECTED_EX1_CORE

    lane = by_id(registry, "S32.EX1.LANE_CONTRACT.V2")
    terminal = by_id(registry, "S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V2")
    generic_adapter = by_id(registry, "S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V2")
    main_goal = by_id(frontier, "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1")

    assert lane["scope_key"] == "S32.EX1.V6_CARRIER"
    assert "V6 integral irreducible geometric genus 1 carrier decision" in lane["scope"]["target"]
    assert terminal["claim_core_sha256"] == EXPECTED_EX1_CORE
    assert terminal["scope_key"] == "S32.EX1.V6_CARRIER"
    assert terminal["scope"]["h4_Q_state_count"] == 29
    assert terminal["scope"]["q602_residues"] == [73, 97, 235]
    assert generic_adapter["kind"] == "adapter_contract"

    ft = ex1["fixed_target"]
    assert ft["picard_class"] == "V6"
    assert ft["curve_integral"] is True
    assert ft["curve_irreducible"] is True
    assert ft["target_geometric_genus"] == 1
    assert ft["D2"] == 758
    assert ft["K_dot_D"] == 186
    assert ft["geometric_analysis_field"] == "C"

    assert main_goal["scope_key"] == "S32.MAIN.V6_CARRIER"
    assert main_goal["scope"]["row_id"] == "g1-d186"
    assert main_goal["scope"]["picard_class"] == "V6"
    assert main_goal["scope"]["integral"] is True
    assert main_goal["scope"]["irreducible"] is True
    assert main_goal["scope"]["geometric_genus"] == 1
    assert main_goal["scope"]["target"] == "population_wide_nonexistence"

    current = main_state["current_exact_frontier"]
    assert current["v6_self_intersection"] == 758
    assert current["v6_canonical_intersection"] == 186

    assert art["identity_checks"]["same_picard_class"] is True
    assert art["identity_checks"]["same_integrality_predicate"] is True
    assert art["identity_checks"]["same_irreducibility_predicate"] is True
    assert art["identity_checks"]["same_geometric_genus"] == 1
    assert art["identity_checks"]["result"] == "EXACT_CURRENT_TARGET_SCOPE_EQUIVALENCE_CANDIDATE"

    assert art["authority_transition"]["ex1_v2_registry_sync_completed_on_this_scratch_leaf"] is False
    assert art["candidate_adapter"]["promotion_granted"] is False
    assert art["firewalls"]["MAIN_credit_changed"] is False
    assert art["firewalls"]["O210_excluded"] is False
    assert art["firewalls"]["Q602_excluded"] is False
    assert art["firewalls"]["Stage32_closed"] is False

    print("PASS_STAGE32_MAIN_EX1_TO_MAIN_V6_SCOPE_ADAPTER_PREFLIGHT")
    print(EXPECTED_CANONICAL)


if __name__ == "__main__":
    main()
