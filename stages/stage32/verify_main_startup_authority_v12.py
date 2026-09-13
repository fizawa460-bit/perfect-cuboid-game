#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V12_CUT191_AUDITED_CONSUMED"
EXPECTED_STATE_BLOB = "484139b653256d34c351aa10fe815c1642cc7cd8"
EXPECTED_STATE_CANONICAL = "4c143ad944a3506f0c39acdd5cc697276576aa5d0c7293c433d10834f9f462f3"
EXPECTED_REPOSITORY_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"

PRE_N356_REMAIN = 66462870551188628549910
POST_N356_REMAIN = 65396964990500233636214
CUT191_REJECT = 113
POST_CUT191_REMAIN = 65396964990500233636101
REMAIN_STRATA = 17128

N356_REVIEW = 5176607630
N356_HEAD = "0cd222d4824e65ea122bc90ac0d48686ddae38f2"
CUT_EXTERNAL_REVIEW = 5177635336
CUT_EXTERNAL_HEAD = "c1bba42b8b61040ce567037cf864fcfb3e6a1746"
CUT_EXTERNAL_CI = 34588749601
CUT_MAIN_REVIEW = 5177949195
CUT_MAIN_HEAD = "890469a848ad8cfb72877eb92d42c615eaa1d70f"
CUT_MAIN_CI = 34591098499

EXPECTED = {
    "full178_manifest": ("stages/stage32/residual-32-01-production/full178-manifest.json", "0a46b34e278688240656b4977e9cb7f589e90e06", "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"),
    "n356_receipt": ("stages/stage32/32-01-178/nodes/N356/HOSTILE-AUDIT-PASS.json", "b6dd078c258c51b88c7fccb791893af6dc7a81f1", "b710cb0fdaf9f5308655e3c5491ec4017e5f19a6a82f3fd5477a8e2396881505"),
    "n356_result": ("stages/stage32/32-01-178/nodes/N356/RESULT.json", "677b1ae2bab910db0805d20ee489d922522919ed", "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31"),
    "n356_management": ("stages/stage32/management/post-n356-hostile-pass-n357-checkpoint-20260911.json", "715aa701208b576b78503dabf294a7b5c71c971e", "ef33829623f399fd5de2d46ce529c6a4b8eb8f14ba490057b65246f6f4919933"),
    "cut_checkpoint": ("stages/stage32/full178-cut/CUT191-first-block-closure-checkpoint.json", "a90042ec931cb487ae6be852524db5a4537862f4", "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd"),
    "cut_handoff": ("stages/stage32/full178-cut/CUT191-AUDIT-HANDOFF.json", "016c92ea002bf8e5a04836933b6bb1729fa9aa7d", "a779e5aa5b8e01c373f356302b8da371fe349f7e1c08f5840b499c02b22645ba"),
    "cut_external_pass": ("stages/stage32/full178-cut/CUT191-HOSTILE-AUDIT-PASS.json", "57ab3aa10ea40300f80622d57c8738edc2fa4bff", "5667fbf15a2472dcb8fb972b32639c2fc6a69d0b6bffe5ccc6d032685c43f629"),
    "cut_management": ("stages/stage32/management/post-cut191-hostile-pass-consumption-20260911.json", "8bea39e443d7996a8958c95005206d6ff349fa52", "f1c59f708190f99ef87422eabc443a5c9df981438a5e647c93dc5052fc5fe6a2"),
    "cut_main_pass": ("stages/stage32/management/CUT191-MAIN-CONSUMPTION-HOSTILE-AUDIT-PASS.json", "6116d5d1561af6010d8f44132a89ed8233c2eeb8", "7cd75b05608fc06014bd785b29034a63cf823946d90193308339a87e20f6a488"),
    "cut_candidate_verifier": ("stages/stage32/verify_cut191_main_consumption.py", "1a39218fe11dd241f1aec986740ea639d6959238", None),
}


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json(rel: str) -> dict:
    obj = json.loads((ROOT / rel).read_text())
    if not isinstance(obj, dict):
        raise AssertionError(rel)
    return obj


def assert_locked(rel: str, blob: str, canon: str | None) -> dict | None:
    path = ROOT / rel
    actual = git_blob_sha(path)
    assert actual == blob, f"{rel}: blob {actual}!={blob}"
    if canon is None:
        return None
    obj = load_json(rel)
    assert obj.get("canonical_sha256_without_this_field") == canon, rel
    assert canonical(obj) == canon, rel
    return obj


def main() -> None:
    assert git_blob_sha(STATE) == EXPECTED_STATE_BLOB
    state = json.loads(STATE.read_text())
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"
    assert state["canonical_sha256_without_this_field"] == EXPECTED_STATE_CANONICAL
    assert canonical(state) == EXPECTED_STATE_CANONICAL

    for rel, blob, canon in EXPECTED.values():
        assert_locked(rel, blob, canon)

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_REPOSITORY_MAIN
    assert auth["n356_hostile_audit_status"] == "PASS"
    assert auth["n356_hostile_audit_review_id"] == N356_REVIEW
    assert auth["n356_hostile_audit_exact_head"] == N356_HEAD
    assert auth["n356_audit_credit_consumed"] is True
    assert auth["cut191_external_hostile_audit_status"] == "PASS"
    assert auth["cut191_external_hostile_audit_review_id"] == CUT_EXTERNAL_REVIEW
    assert auth["cut191_external_hostile_audit_exact_head"] == CUT_EXTERNAL_HEAD
    assert auth["cut191_external_exact_head_ci_run"] == CUT_EXTERNAL_CI
    assert auth["cut191_main_consumption_hostile_audit_status"] == "PASS"
    assert auth["cut191_main_consumption_hostile_audit_review_id"] == CUT_MAIN_REVIEW
    assert auth["cut191_main_consumption_audited_exact_head"] == CUT_MAIN_HEAD
    assert auth["cut191_main_consumption_exact_head_ci_run"] == CUT_MAIN_CI
    assert auth["cut191_main_pruning_credit_consumed"] is True
    assert auth["cut191_incremental_rejected_terminals"] == CUT191_REJECT
    assert auth["cut191_remaining_strata"] == REMAIN_STRATA
    assert auth["cut191_remaining_terminals"] == POST_CUT191_REMAIN
    assert auth["cut191_post_sync_reaudit_required"] is True
    assert auth["cut191_post_sync_reaudit_status"] == "PENDING"
    assert auth["cut191_synchronized_head_hostile_audited"] is False

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == POST_CUT191_REMAIN
    assert frontier["n356_main_pruning_credit"] is True
    assert frontier["cut191_main_pruning_credit"] is True
    assert frontier["cut191_incremental_rejected_terminals"] == CUT191_REJECT
    assert frontier["cut191_status"] == "AUDITED_FIRST_BLOCK_PICARD64_UNSAT_CONSUMED"
    assert frontier["cut191_post_sync_reaudit_required"] is True
    assert frontier["cut191_synchronized_head_hostile_audited"] is False
    assert frontier["n357_main_pruning_credit"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False

    assert PRE_N356_REMAIN - 1065905560688394913696 == POST_N356_REMAIN
    assert POST_N356_REMAIN - CUT191_REJECT == POST_CUT191_REMAIN

    n356_receipt = load_json(EXPECTED["n356_receipt"][0])
    assert n356_receipt["status"] == "PASS"
    assert n356_receipt["review_id"] == N356_REVIEW
    assert n356_receipt["audited_exact_head"] == N356_HEAD

    cut = load_json(EXPECTED["cut_checkpoint"][0])
    assert cut["target"]["row_id"] == "g1-d008"
    assert cut["target"]["d"] == 8 and cut["target"]["e"] == 8
    assert cut["population_preimage"]["first_block_rank_range"] == [0, 112]
    assert cut["population_preimage"]["rank_unrank_replay_count"] == CUT191_REJECT
    assert cut["population_preimage"]["n355_group_sums_on_first_block"] == [0, 1, 1]
    assert cut["coverage_certificate"]["covered_parent_count"] == 7336
    assert cut["coverage_certificate"]["sat_parent_count"] == 0
    assert cut["coverage_certificate"]["unknown_parent_count"] == 0
    # Historical CUT checkpoint must still show no self-promotion.
    assert cut["credit"]["stage32_main_pruning_credit"] is False

    ext = load_json(EXPECTED["cut_external_pass"][0])
    assert ext["status"] == "PASS"
    assert ext["review_id"] == CUT_EXTERNAL_REVIEW
    assert ext["audited_exact_head"] == CUT_EXTERNAL_HEAD
    assert ext["exact_head_workflow_run"] == CUT_EXTERNAL_CI

    mgmt = load_json(EXPECTED["cut_management"][0])
    assert mgmt["n356_overlap_replay"]["lhs_b_minus_c"] == 0
    assert mgmt["n356_overlap_replay"]["rhs_3d_minus_e"] == 16
    assert mgmt["n356_overlap_replay"]["n356_preserves_all_113_cut191_terminals"] is True
    assert mgmt["n356_overlap_replay"]["double_charge"] is False
    assert mgmt["authority"]["authoritative_remaining_terminals"] == POST_CUT191_REMAIN
    assert mgmt["authority"]["cut191_incremental_rejected_terminals"] == CUT191_REJECT

    sync_pass = load_json(EXPECTED["cut_main_pass"][0])
    assert sync_pass["status"] == "PASS"
    assert sync_pass["review_id"] == CUT_MAIN_REVIEW
    assert sync_pass["audited_exact_head"] == CUT_MAIN_HEAD
    assert sync_pass["exact_head_workflow_run"] == CUT_MAIN_CI
    tr = sync_pass["audited_transition"]
    assert tr["pre_cut_remaining_terminals"] == POST_N356_REMAIN
    assert tr["incremental_rejected_terminals"] == CUT191_REJECT
    assert tr["post_cut_remaining_terminals"] == POST_CUT191_REMAIN
    assert tr["n356_overlap_zero"] is True
    assert sync_pass["credit_ceiling"]["synchronization_authorized"] is True
    assert sync_pass["credit_ceiling"]["replacement_head_reaudit_required"] is True
    assert sync_pass["credit_ceiling"]["merge_authorized"] is False

    cut_lock = state["source_locks"]["cut191"]
    assert cut_lock["external_audit_review_id"] == CUT_EXTERNAL_REVIEW
    assert cut_lock["external_audited_exact_head"] == CUT_EXTERNAL_HEAD
    assert cut_lock["main_consumption_audit_review_id"] == CUT_MAIN_REVIEW
    assert cut_lock["main_consumption_audited_exact_head"] == CUT_MAIN_HEAD
    assert cut_lock["main_consumption_audit_receipt_blob_sha1"] == EXPECTED["cut_main_pass"][1]
    assert cut_lock["main_consumption_candidate_verifier_blob_sha1"] == EXPECTED["cut_candidate_verifier"][1]

    current = state["current"]
    assert current["next_exact_route"] == "N357_ALL178_TRANSPORT_SUPPORT_CAPACITY_CENSUS_THEN_EXTERNAL_AUDIT"
    assert current["stop_semantics"] == "N357_OWNED_BY_STAGE32_01_178_MAINBATCH_MAIN_MUST_NOT_DUPLICATE"

    fw = state["firewalls"]
    for key in [
        "historical_q602_residues_treated_as_current_survivors",
        "n356_self_promoted_to_audited",
        "n356_credit_exceeds_external_audit",
        "cut191_self_promoted_to_audited",
        "cut191_credit_exceeds_external_or_main_consumption_audit",
        "n350_producer_registered_without_audit",
        "production_complete_released_without_audited_leaf_contract",
        "n104_completeness_release_granted",
        "heavy_compute_authorized_by_startup_state",
        "receiver_credit",
        "route_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        assert fw[key] is False, key

    prov = state["historical_formal_provenance"]
    assert prov["formal_q602_residues"] == [73, 97, 235]
    assert prov["formal_q602_residues_are_current_survivors"] is False

    for rel in state["current_leaf_working_set"]:
        assert (ROOT / rel).is_file(), rel

    startup = START.read_text()
    for fragment in [
        "Ordinary `stage32mainbatch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        assert fragment in startup

    print("PASS Stage32 MAIN startup authority V12 CUT191_AUDITED_CONSUMED")
    print(f"authoritative_remaining={REMAIN_STRATA}_strata/{POST_CUT191_REMAIN}_terminals")
    print("cut191_incremental_reject=113 n356_overlap=zero")
    print("post_sync_reaudit_required=true synchronized_head_hostile_audited=false")
    print("full178_complete=false n357_main_credit=false merge_authorized=false")


if __name__ == "__main__":
    main()
