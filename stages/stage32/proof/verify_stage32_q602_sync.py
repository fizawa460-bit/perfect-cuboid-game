#!/usr/bin/env python3
"""Verify live Q602 V3 authority consumption and completed post-sync management audit."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
STATE_CANON = "1a7295b3452d4cc7bc4406ee1bcfb655cd28a5d8e75f690fdc8bd93e6d85c6e2"
OBJECT_ID = "S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1"
EMPTY_ID = "S32.ADAPTER.O210_EMPTY_TO_Q602_REALIZATION_EMPTY.V1"
Q_ID = "S32.Q602.EXCLUSION.V3"
AUDIT_OBJECT = {"status":"PASS", "pr":1730, "review_id":5149322780, "exact_head":"1689ed2bdfa149b5e462ce0182e7a7e7c31ee62c"}
AUDIT_REPAIR = {"status":"PASS", "pr":1730, "review_id":5149462285, "exact_head":"6487de765b0d35e05d81018aeaff902af9b7d21a"}
AUDIT_POST_SYNC = {"status":"PASS", "pr":1730, "review_id":5149990935, "exact_head":"9b605ed7f44415198a0e261dc46971e5ecd3c80b"}
MERGE_COMMIT = "733176600f99e91993d08c16aa98f09c08a1e726"
EXPECTED = {
    OBJECT_ID: ("ed1ea5441a3b0bb876a3b93f272e2a16d693f1b44f0f050c13af1625c1e028", AUDIT_OBJECT),
    EMPTY_ID: ("4dd78ed5a1917d7c953fee95bb52f1d1429e239ca90d3bf8dae26461e0611de8", AUDIT_REPAIR),
    Q_ID: ("c85a76ac1ed07deec1d65269451452d33b63c3a5221134ee687e282951823067", AUDIT_REPAIR),
}


def load(rel):
    return json.loads((ROOT / rel).read_text())


def validate(basev, by_id):
    old = load("stages/stage32/scratch/q602-o210-versioned-claim-bundle-20260909.json")
    repair = load("stages/stage32/q602-claim-dag-variance-repair-preflight-20260909.json")
    for bundle, digest in [
        (old, "9ce14c2d619685ab9c22a83ccd36cc1b085bf1579132df7b0c0b2b4b1122ba07"),
        (repair, "1ed236ef01fbe739282c10a259dd7b000975cd7a32e475e7a9c8c10bb76c9b38"),
    ]:
        body = dict(bundle)
        assert body.pop("canonical_sha256_without_this_field") == digest
        assert basev.csha(body) == digest
        assert all(v is False for v in bundle["authority_firewalls"].values())

    retained = {c["claim_id"]: c for c in [old["adapter_claim"]] + repair["new_claims"]}
    for cid, (digest, receipt) in EXPECTED.items():
        claim = by_id[cid]
        assert claim["authority_status"] == "AUDITED", cid
        assert claim["audit_receipt"] == receipt, cid
        assert claim["claim_core_sha256"] == digest, cid
        assert basev.claim_core_sha(claim) == digest, cid
        assert basev.claim_core_sha(retained[cid]) == digest, cid
        for key in basev.CORE_KEYS:
            assert claim.get(key) == retained[cid].get(key), (cid, key)

    assert "S32.Q602.EXCLUSION.V1" not in by_id
    assert "S32.Q602.EXCLUSION.V2" not in by_id
    assert by_id[Q_ID]["frontier_status"] == "AUDITED_TRUE"
    assert by_id[Q_ID]["blockers"] == []
    assert by_id[OBJECT_ID]["bridges"]["from_scope_key"] == "S32.Q602.ADMISSIBLE_CONFIGURATION"
    assert by_id[OBJECT_ID]["bridges"]["to_scope_key"] == "S32.O210.COVER"
    assert by_id[EMPTY_ID]["bridges"]["from_scope_key"] == "S32.O210.COVER"
    assert by_id[EMPTY_ID]["bridges"]["to_scope_key"] == "S32.Q602.ARITHMETIC"

    v6 = by_id["S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"]
    assert v6["authority_status"] == "AUDITED"
    assert basev.claim_core_sha(v6) == "c7927cd86c321de2956b3843dff4882ddeb29fb3489715d4dd7d1d60eff58cc6"
    assert v6["audit_receipt"]["review_id"] == 5147810198

    s = load("stages/stage32/MAIN-STATE.json")
    body = dict(s)
    assert body.pop("canonical_sha256_without_this_field") == STATE_CANON
    assert basev.csha(body) == STATE_CANON
    a, f, fw = s["authority_sync"], s["current_exact_frontier"], s["firewalls"]

    assert a["latest_hostile_audit_review_id"] == AUDIT_POST_SYNC["review_id"]
    assert a["latest_audited_exact_head"] == AUDIT_POST_SYNC["exact_head"]
    assert a["latest_stage32_merge_commit"] == MERGE_COMMIT
    assert a["audited_main_q602_claim_core_sha256"] == EXPECTED[Q_ID][0]
    assert a["q602_post_sync_hostile_audit_status"] == "PASS"
    assert a["q602_post_sync_hostile_audit_review_id"] == AUDIT_POST_SYNC["review_id"]
    assert a["q602_post_sync_hostile_audit_exact_head"] == AUDIT_POST_SYNC["exact_head"]

    assert f["q602_excluded"] is True and fw["Q602_excluded"] is True
    assert f["q602_exclusion_claim_id"] == Q_ID
    assert f["q602_exclusion_scope"] == "NO_GEOMETRICALLY_ADMISSIBLE_FIXED_TARGET_CONFIGURATION"
    assert f["o210_excluded"] is True and fw["O210_excluded"] is True
    assert f["v6_integral_irreducible_genus1_population_empty_audited"] is True
    assert f["q602_survivors_audited"] == s["fixed_target"]["surviving_residues_decimal"] == [73,97,235]
    assert by_id["S32.Q602.SURVIVORS_73_97_235.V1"]["scope"]["surviving_residues"] == [73,97,235]
    assert f["full178_numerical_census_complete"] is False
    assert s["current"]["active_missing_interface"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert s["current"]["next_exact_route"] == "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS"

    for key in [
        "O212_plus_advance_allowed", "controller_promotion_granted",
        "heavy_compute_authorized_by_startup_state", "receiver_credit", "route_credit",
        "theorem_credit", "endpoint_credit", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ]:
        assert fw[key] is False, key

    assert by_id["S32.FULL178.NUMERICAL_CENSUS.V1"]["authority_status"] == "DECLARED_GOAL"
    assert by_id["S32.GOAL.STAGE32_CLOSURE.V1"]["authority_status"] == "DECLARED_GOAL"
    for cid in ["S32.O210.EXCLUSION.V3", Q_ID]:
        assert all(link["role"] != "ATTACKS" for link in by_id[cid]["lane_links"])

    checkpoint = load("stages/stage32/management/mainbatch-final-chain-reentry-20260909.json")
    cp = dict(checkpoint)
    digest = cp.pop("canonical_sha256_without_this_field")
    assert basev.csha(cp) == digest
    assert checkpoint["authority_consumed"]["q602_post_sync_management_audit"] == AUDIT_POST_SYNC
    assert checkpoint["final_chain"]["32-01"]["full178_complete"] is False
    assert checkpoint["final_chain"]["32-03"]["depends_on_full178"] is False
    assert checkpoint["mainbatch_policy"]["heavy_compute_authorized"] is False
    assert checkpoint["mainbatch_policy"]["merge_authorized"] is False

    text = (ROOT / "stages/stage32/STAGE32-PROOF-PATH.md").read_text()
    required = [
        "POST-#1730 Q602-V3-CONSUMED / POST-SYNC-AUDITED / FINAL-CHAIN FRONTIER",
        Q_ID,
        "Q602_excluded=true",
        "O210_excluded=true",
        "FULL178_AND_FINAL_MILESTONE_CHAIN",
        "5149990935",
        "post-sync management transition itself received independent hostile-audit PASS",
        "32-02-L   rigorous effectivity certification",
        "32-03-L   multibranch-at-node carrier ledger",
    ]
    for token in required:
        assert token in text, token
    for token in [
        "Q602_excluded=false",
        "Q602_FORGETFUL_O210_POPULATION_ADAPTER_PLUS_FULL178",
        "post-sync hostile re-audit remains PENDING",
        "HOSTILE_REAUDIT_Q602_V3_MAIN_SYNC_THEN_FULL178_AND_FINAL_SYNTHESIS",
    ]:
        assert token not in text, token


def main():
    spec = importlib.util.spec_from_file_location("stage32_live_frontier", HERE / "verify_stage32_active_frontier.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main()


if __name__ == "__main__":
    raise SystemExit(main())
