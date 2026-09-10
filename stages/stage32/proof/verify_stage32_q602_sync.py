#!/usr/bin/env python3
"""Verify retained Q602 V3 authority while current MAIN routes through FULL178."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
STATE_CANON = "8f44f0473be26d183e3b9710e074f1b6d727ca825b543da8af3d31047284ca88"
CHECKPOINT_CANON = "6730cc294f6a2f5800a1ba6697639e5c25c4f6ce43361acffc9e130025858a0e"
OBJECT_ID = "S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1"
EMPTY_ID = "S32.ADAPTER.O210_EMPTY_TO_Q602_REALIZATION_EMPTY.V1"
Q_ID = "S32.Q602.EXCLUSION.V3"
AUDIT_OBJECT = {"status":"PASS", "pr":1730, "review_id":5149322780, "exact_head":"1689ed2bdfa149b5e462ce0182e7a7e7c31ee62c"}
AUDIT_REPAIR = {"status":"PASS", "pr":1730, "review_id":5149462285, "exact_head":"6487de765b0d35e05d81018aeaff902af9b7d21a"}
AUDIT_POST_SYNC = {"status":"PASS", "pr":1730, "review_id":5149990935, "exact_head":"9b605ed7f44415198a0e261dc46971e5ecd3c80b"}
MERGE_COMMIT = "733176600f99e91993d08c16aa98f09c08a1e726"
EXPECTED = {
    OBJECT_ID: ("ed1ea5441a3b0bb876a3a8b93f272e2a16d693f1b44f0f050c13af1625c1e028", AUDIT_OBJECT),
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

    # Current mutable routing state is now FULL178-final-chain V3.  The Q602
    # claim itself remains immutable/audited provenance and must not be
    # presented as a live attack target or current survivor population.
    s = load("stages/stage32/MAIN-STATE.json")
    body = dict(s)
    assert body.pop("canonical_sha256_without_this_field") == STATE_CANON
    assert basev.csha(body) == STATE_CANON
    assert s["schema"] == "STAGE32_MAIN_COMPACT_STATE_V3_FULL178_FINAL_CHAIN_POST_EX5_MERGE"

    a = s["authority_sync"]
    target = s["current_target"]
    prov = s["historical_formal_provenance"]
    f = s["current_exact_frontier"]
    fw = s["firewalls"]

    assert a["historical_narrow_chain_post_sync_review_id"] == AUDIT_POST_SYNC["review_id"]
    assert a["historical_narrow_chain_post_sync_exact_head"] == AUDIT_POST_SYNC["exact_head"]
    assert a["historical_narrow_chain_merge_commit"] == MERGE_COMMIT
    assert prov["audited_q602_claim"] == Q_ID
    assert prov["audited_o210_claim"] == "S32.O210.EXCLUSION.V3"
    assert prov["audited_v6_claim"] == "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"
    assert prov["formal_q602_residues"] == [73,97,235]
    assert prov["formal_q602_residues_are_current_survivors"] is False
    assert by_id["S32.Q602.SURVIVORS_73_97_235.V1"]["scope"]["surviving_residues"] == [73,97,235]

    assert target["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert target["primary_incomplete_id"] == "32-01"
    assert target["V6_is_current_attack_target"] is False
    assert target["O210_is_current_attack_target"] is False
    assert target["Q602_is_current_attack_target"] is False
    assert f["full178_numerical_census_complete"] is False
    assert f["primary_incomplete_remains_32_01"] is True
    assert f["ex5_auto_promoted_to_n150"] is False
    assert f["ex5_population_wide_full178_result_complete"] is False

    assert fw["historical_V6_excluded_at_audited_scope"] is True
    assert fw["historical_O210_excluded_at_audited_scope"] is True
    assert fw["historical_Q602_excluded_at_audited_scope"] is True
    assert fw["historical_q602_residues_treated_as_current_survivors"] is False
    assert fw["ex5_merge_auto_promotes_n150"] is False
    assert fw["ex5_merge_auto_promotes_full178"] is False
    for key in [
        "n240_repair_self_promoted_to_audited", "n104_completeness_release_granted",
        "heavy_compute_authorized_by_startup_state", "receiver_credit", "route_credit",
        "theorem_credit", "endpoint_credit", "stage32_closed",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
    ]:
        assert fw[key] is False, key

    assert by_id["S32.FULL178.NUMERICAL_CENSUS.V1"]["authority_status"] == "DECLARED_GOAL"
    assert by_id["S32.GOAL.STAGE32_CLOSURE.V1"]["authority_status"] == "DECLARED_GOAL"
    for cid in ["S32.O210.EXCLUSION.V3", Q_ID]:
        assert all(link["role"] != "ATTACKS" for link in by_id[cid]["lane_links"])

    checkpoint = load("stages/stage32/management/post-ex5-merge-final-chain-sync-20260910.json")
    cp = dict(checkpoint)
    assert cp.pop("canonical_sha256_without_this_field") == CHECKPOINT_CANON
    assert basev.csha(cp) == CHECKPOINT_CANON
    assert checkpoint["authority"]["v6_o210_q602_current_attack_targets"] is False
    assert checkpoint["authority"]["formal_q602_residues"] == [73,97,235]
    assert checkpoint["ex5"]["auto_promoted_to_n150"] is False
    assert checkpoint["full178"]["complete"] is False
    assert checkpoint["claim_sync"]["ex_to_main_promotion_performed"] is False
    assert checkpoint["firewalls"]["heavy_compute_authorized"] is False
    assert checkpoint["firewalls"]["merge_authorized"] is False

    text = (ROOT / "stages/stage32/STAGE32-PROOF-PATH.md").read_text()
    for token in [
        "POST-#1730 Q602-V3-CONSUMED / POST-SYNC-AUDITED / FINAL-CHAIN FRONTIER",
        Q_ID,
        "Q602_excluded=true",
        "O210_excluded=true",
        "FULL178_AND_FINAL_MILESTONE_CHAIN",
        "5149990935",
        "32-02-L   rigorous effectivity certification",
        "32-03-L   multibranch-at-node carrier ledger",
    ]:
        assert token in text, token


def main():
    spec = importlib.util.spec_from_file_location("stage32_live_frontier", HERE / "verify_stage32_active_frontier.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main()


if __name__ == "__main__":
    raise SystemExit(main())
