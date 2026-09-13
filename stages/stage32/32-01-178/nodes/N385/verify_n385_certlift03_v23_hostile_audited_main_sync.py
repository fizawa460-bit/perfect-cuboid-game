#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

EXPECTED_N384_BLOB = "66ed1e4a6a36aa3784213459b344208f2502d318"
EXPECTED_N384_CANONICAL = "ce2523230b4e13bb3be270265881e73c5a50bd1f4815e8e6a6380472978b1a6e"
EXPECTED_N385_CANONICAL = "0af1a4deaa1924f6785e2adb259b03bdd64ed6a78e09efd1d16bfde2d6fa5a2f"

EXPECTED_AUDIT_PASS_BLOB = "442f84b392254383736f1b695da7a9b2954c053d"
EXPECTED_AUDIT_PASS_CANONICAL = "ceec3c102ad194c05e1429e7af293716a21993fb2dcfd531525c30c371bc2821"
EXPECTED_ADAPTER_BLOB = "327aa601acad47bc1e486cccbbac3d3dee7c2681"
EXPECTED_ADAPTER_CANONICAL = "597fe83b10c7a23f1da9748423ea3f70a78d448991a253777b64cab554c7ffaf"
EXPECTED_CANDIDATE_RECEIPT_BLOB = "291bb8b125566bb72c1caae0537dff2625219ffb"
EXPECTED_CANDIDATE_RECEIPT_CANONICAL = "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858"
EXPECTED_PRODUCER_AUDIT_REVIEW = 5188860951
EXPECTED_PRODUCER_REVIEWED_HEAD = "289437a4a97a814c2388133cbde0c794d9502e4b"
EXPECTED_PRODUCER_AUDIT_PASS_HEAD = "51c56b5c3ee15177c2975b966ab546d0b548c4af"

EXPECTED_V22_HEAD = "f8039b4ce479a4b91f2f0547e7049f629e9be5f5"
EXPECTED_V22_REVIEW = 5188224290
EXPECTED_V22_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"
EXPECTED_V22_CANONICAL = "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"
EXPECTED_V22_TERMINALS = 47589703313957134804198

EXPECTED_V23_HEAD = "fba76454a49132f752dc93deb20214970b314d89"
EXPECTED_V23_REVIEW = 5189031846
EXPECTED_V23_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
EXPECTED_V23_CANONICAL = "460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
EXPECTED_V23_VERIFIER_BLOB = "0a14c08be80e86b7393a92b42903f08db1fe4275"
EXPECTED_V23_TERMINALS = 47589703313957134649501

TARGET_BLOCKS = 1677
OVERLAP_BLOCKS = 308
INCREMENTAL_BLOCKS = 1369
INCREMENTAL_TERMINALS = 154697


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def check_blob(path: Path, expected: str, label: str) -> None:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == expected, f"{label} blob drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", required=True)
    ap.add_argument("--main-v23-root", required=True)
    args = ap.parse_args()

    cert = Path(args.certlift_root)
    main_v23 = Path(args.main_v23_root)

    n384_path = HERE.parent / "N384" / "STATE.json"
    n385_path = HERE / "STATE.json"

    check_blob(n384_path, EXPECTED_N384_BLOB, "N384 state")
    n384 = load(n384_path)
    req(canonical(n384) == EXPECTED_N384_CANONICAL, "N384 canonical drift")
    req(
        n384["status"]
        == "CERTLIFT03_V22_ADAPTER_RECEIPT_RETAINED_READY_FOR_HOSTILE_AUDIT_NO_CREDIT",
        "N384 status drift",
    )
    req(n384["promotion_boundary"]["hostile_audit_pass"] is False, "N384 wait semantics drift")

    audit_path = (
        cert
        / "stages/stage32/cert-lift/"
        "CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json"
    )
    check_blob(audit_path, EXPECTED_AUDIT_PASS_BLOB, "CERTLIFT-03 V22 audit PASS receipt")
    audit = load(audit_path)
    req(audit["status"] == "HOSTILE_AUDIT_PASS", "producer audit status drift")
    req(audit["pr"] == 1803, "producer audit PR drift")
    req(audit["review_id"] == EXPECTED_PRODUCER_AUDIT_REVIEW, "producer review drift")
    req(audit["reviewed_pr_head"] == EXPECTED_PRODUCER_REVIEWED_HEAD, "producer reviewed head drift")
    req(audit["adapter_blob_sha1"] == EXPECTED_ADAPTER_BLOB, "adapter blob drift")
    req(audit["adapter_canonical_sha256"] == EXPECTED_ADAPTER_CANONICAL, "adapter canonical drift")
    req(audit["frozen_receipt_blob_sha1"] == EXPECTED_CANDIDATE_RECEIPT_BLOB, "candidate receipt blob drift")
    req(
        audit["frozen_receipt_canonical_sha256"] == EXPECTED_CANDIDATE_RECEIPT_CANONICAL,
        "candidate receipt canonical drift",
    )
    req(
        audit["canonical_sha256_without_this_field"] == EXPECTED_AUDIT_PASS_CANONICAL,
        "audit stored canonical drift",
    )
    req(canonical(audit) == EXPECTED_AUDIT_PASS_CANONICAL, "audit canonical drift")

    av22 = audit["v22_authority"]
    req(av22["exact_head"] == EXPECTED_V22_HEAD, "producer V22 head drift")
    req(av22["hostile_audit_review_id"] == EXPECTED_V22_REVIEW, "producer V22 review drift")
    req(av22["main_state_blob_sha1"] == EXPECTED_V22_BLOB, "producer V22 blob drift")
    req(
        av22["main_state_canonical_sha256"] == EXPECTED_V22_CANONICAL,
        "producer V22 canonical drift",
    )
    req(av22["remaining_terminals"] == EXPECTED_V22_TERMINALS, "producer V22 terminal drift")

    recomp = audit["recomposition"]
    req(recomp["symbolic_target_blocks"] == TARGET_BLOCKS, "target block drift")
    req(recomp["prior_overlap_union_blocks"] == OVERLAP_BLOCKS, "overlap drift")
    req(recomp["double_charge"] is False, "producer double-charge drift")
    req(recomp["incremental_blocks"] == INCREMENTAL_BLOCKS, "incremental block drift")
    req(recomp["incremental_terminals"] == INCREMENTAL_TERMINALS, "incremental terminal drift")
    req(
        recomp["candidate_authority_after_if_synchronized"] == EXPECTED_V23_TERMINALS,
        "producer candidate authority drift",
    )
    req(audit["exact_head_ci"]["conclusion"] == "SUCCESS", "producer audit CI drift")
    for key, value in audit["credit_firewall"].items():
        req(value is False, f"producer audit firewall unexpectedly grants {key}")

    v23_state_path = main_v23 / "stages/stage32/MAIN-STATE.json"
    v23_verifier_path = main_v23 / "stages/stage32/verify_main_startup_authority_v23.py"
    check_blob(v23_state_path, EXPECTED_V23_BLOB, "V23 MAIN state")
    check_blob(v23_verifier_path, EXPECTED_V23_VERIFIER_BLOB, "V23 startup verifier")
    v23 = load(v23_state_path)
    req(v23["schema"] == "STAGE32_MAIN_COMPACT_STATE_V23_CERTLIFT03_CONSUMED", "V23 schema drift")
    req(
        v23["canonical_sha256_without_this_field"] == EXPECTED_V23_CANONICAL,
        "V23 stored canonical drift",
    )
    req(canonical(v23) == EXPECTED_V23_CANONICAL, "V23 canonical drift")

    frontier = v23["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == 17128, "V23 strata drift")
    req(frontier["authoritative_remaining_terminals"] == EXPECTED_V23_TERMINALS, "V23 terminal drift")
    req(frontier["certlift03_target_blocks"] == TARGET_BLOCKS, "V23 target block drift")
    req(frontier["certlift03_prior_overlap_blocks"] == OVERLAP_BLOCKS, "V23 overlap drift")
    req(frontier["certlift03_incremental_blocks"] == INCREMENTAL_BLOCKS, "V23 incremental block drift")
    req(
        frontier["certlift03_incremental_rejected_terminals"] == INCREMENTAL_TERMINALS,
        "V23 incremental terminal drift",
    )
    req(frontier["certlift03_double_charge"] is False, "V23 double-charge drift")
    req(frontier["certlift03_main_pruning_credit"] is True, "V23 CERTLIFT credit missing")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    req(frontier["stage32_closed"] is False, "Stage32 unexpectedly closed")
    req(frontier["n372_survives_certlift03"] is True, "N372 no longer survives")
    req(frontier["n372_main_pruning_credit"] is False, "N372 pruning credit drift")
    req(frontier["n372_full178_credit"] is False, "N372 FULL178 credit drift")
    req(frontier["n372_effectivity_final_credit"] is False, "N372 effectivity credit drift")

    v23_cert = v23["source_locks"]["certlift03_v22_adapter"]
    req(v23_cert["adapter_blob_sha1"] == EXPECTED_ADAPTER_BLOB, "V23 adapter blob drift")
    req(v23_cert["adapter_canonical_sha256"] == EXPECTED_ADAPTER_CANONICAL, "V23 adapter canonical drift")
    req(
        v23_cert["candidate_receipt_blob_sha1"] == EXPECTED_CANDIDATE_RECEIPT_BLOB,
        "V23 candidate receipt blob drift",
    )
    req(
        v23_cert["candidate_receipt_canonical_sha256"] == EXPECTED_CANDIDATE_RECEIPT_CANONICAL,
        "V23 candidate receipt canonical drift",
    )
    req(
        v23_cert["hostile_audit_pass_receipt_blob_sha1"] == EXPECTED_AUDIT_PASS_BLOB,
        "V23 audit receipt blob drift",
    )
    req(
        v23_cert["hostile_audit_pass_receipt_canonical_sha256"] == EXPECTED_AUDIT_PASS_CANONICAL,
        "V23 audit receipt canonical drift",
    )
    req(
        v23_cert["hostile_audit_pass_receipt_head"] == EXPECTED_PRODUCER_AUDIT_PASS_HEAD,
        "V23 audit receipt head drift",
    )
    req(v23_cert["hostile_audit_review_id"] == EXPECTED_PRODUCER_AUDIT_REVIEW, "V23 producer review drift")
    req(
        v23_cert["reviewed_pr_head"] == EXPECTED_PRODUCER_REVIEWED_HEAD,
        "V23 producer reviewed head drift",
    )

    pred = v23["source_locks"]["predecessor_v22"]
    req(pred["exact_head"] == EXPECTED_V22_HEAD, "V23 predecessor V22 head drift")
    req(pred["hostile_audit_review_id"] == EXPECTED_V22_REVIEW, "V23 predecessor V22 review drift")
    req(pred["main_state_blob_sha1"] == EXPECTED_V22_BLOB, "V23 predecessor V22 blob drift")
    req(
        pred["main_state_canonical_sha256"] == EXPECTED_V22_CANONICAL,
        "V23 predecessor V22 canonical drift",
    )
    req(
        EXPECTED_V22_TERMINALS - INCREMENTAL_TERMINALS == EXPECTED_V23_TERMINALS,
        "V22 -> V23 terminal arithmetic failure",
    )
    req(TARGET_BLOCKS - OVERLAP_BLOCKS == INCREMENTAL_BLOCKS, "block arithmetic failure")

    # This exact V23 JSON was authored before its external hostile re-audit.
    # Its internal gate therefore remains fail-closed; N385 source-locks the later
    # PASS review instead of mutating or rewriting the audited V23 bytes.
    req(
        v23["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "V23 pre-review firewall drift",
    )
    req(v23["firewalls"]["full178_complete"] is False, "V23 FULL178 firewall drift")
    req(v23["firewalls"]["stage32_closed"] is False, "V23 Stage32 firewall drift")
    req(v23["firewalls"]["merge_authorized"] is False, "V23 merge firewall drift")

    n385 = load(n385_path)
    req(canonical(n385) == EXPECTED_N385_CANONICAL, "N385 canonical drift")
    req(
        n385["canonical_sha256_without_this_field"] == EXPECTED_N385_CANONICAL,
        "N385 stored canonical drift",
    )
    req(
        n385["status"]
        == "CERTLIFT03_V23_HOSTILE_AUDITED_MAIN_AUTHORITY_SYNC_NO_NEW_LOCAL_CREDIT",
        "N385 status drift",
    )
    req(n385["main_v23_authority"]["exact_head"] == EXPECTED_V23_HEAD, "N385 V23 head drift")
    req(n385["main_v23_authority"]["hostile_audit_review_id"] == EXPECTED_V23_REVIEW, "N385 V23 review drift")
    req(n385["main_v23_authority"]["hostile_audit_status"] == "PASS", "N385 V23 audit status drift")
    req(n385["main_v23_authority"]["state_blob_sha1"] == EXPECTED_V23_BLOB, "N385 V23 blob drift")
    req(
        n385["main_v23_authority"]["state_canonical_sha256"] == EXPECTED_V23_CANONICAL,
        "N385 V23 canonical drift",
    )
    req(
        n385["authority_sync"]["latest_hostile_audited_main_authority_visible_to_178"] is True,
        "N385 authority visibility drift",
    )
    req(n385["authority_sync"]["v22_wait_gate_resolved"] is True, "N385 old wait gate not resolved")
    req(
        n385["authority_sync"]["n385_recomputes_or_reconsumes_certlift03"] is False,
        "N385 must not duplicate V23 consumption",
    )
    req(
        n385["certlift03_consumption"]["main_v23_already_owns_pruning_credit"] is True,
        "N385 ownership drift",
    )
    req(n385["certlift03_consumption"]["n385_additional_pruning_blocks"] == 0, "N385 block credit drift")
    req(n385["certlift03_consumption"]["n385_additional_pruning_terminals"] == 0, "N385 terminal credit drift")
    req(n385["certlift03_consumption"]["duplicate_receiver_credit_forbidden"] is True, "N385 duplicate-credit firewall drift")
    req(n385["n101_contract"]["remains_stopped"] is True, "N101 unexpectedly reopened")
    for key, value in n385["credit"].items():
        req(value is False, f"N385 unexpectedly grants {key}")
    req(n385["anti_loop"]["heavy_compute_authorized"] is False, "N385 heavy compute drift")
    req(
        n385["next_gate"]
        == "V23_HOSTILE_AUDITED_MAIN_AUTHORITY_ACTIVE_FOR_178_THEN_FULL178_OR_N377_STRONG_SIGNATURE_ACTION",
        "N385 next gate drift",
    )

    print(
        json.dumps(
            {
                "verdict": "PASS_N385_CERTLIFT03_V23_HOSTILE_AUDITED_MAIN_AUTHORITY_SYNC",
                "producer_audit_review": EXPECTED_PRODUCER_AUDIT_REVIEW,
                "main_v23_audit_review": EXPECTED_V23_REVIEW,
                "main_v23_exact_head": EXPECTED_V23_HEAD,
                "target_blocks": TARGET_BLOCKS,
                "prior_overlap_blocks": OVERLAP_BLOCKS,
                "incremental_blocks": INCREMENTAL_BLOCKS,
                "incremental_terminals": INCREMENTAL_TERMINALS,
                "authoritative_remaining_terminals": EXPECTED_V23_TERMINALS,
                "n385_additional_pruning_terminals": 0,
                "n101_reopened": False,
                "full178_complete": False,
                "stage32_closed": False,
                "merge_authorized": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
