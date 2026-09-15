#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RECEIPT = HERE / "HPADJ08-V30-HOSTILE-AUDIT-PASS-SYNC.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"

PREDECESSOR_HEAD = "cfc23c7c633fa4192c281c8ba6a356ec071fc305"
PREDECESSOR_STATE_BLOB = "bd663e70864d7279063fa4eea9745fdfa479346d"
PREDECESSOR_STATE_CANON = "3cbaa6e0b6b54cd379ba8770cc8e45c56c8444c13814f325fb9737222e306ecc"
AUDIT_REVIEW_ID = 5209163478
CURRENT_MAIN = "c6284abbb29930255892d56f800da0ea1e34734b"
RECEIPT_CANON = "c57e3614ef0111ba35490f48ea707cd7c47d34865e6b85fa336462794867a773"
BOUND = 6703403803993210101494

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-v29-root")
    args = ap.parse_args()

    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    req(receipt["schema"] == "STAGE32_MAIN_HPADJ08_V30_HOSTILE_AUDIT_PASS_SYNC_V1", "receipt schema")
    req(receipt.get("canonical_sha256_without_this_field") == RECEIPT_CANON, "receipt stored canonical")
    req(canon(receipt) == RECEIPT_CANON, "receipt canonical")
    req(receipt["predecessor_v29"]["exact_head"] == PREDECESSOR_HEAD, "predecessor head")
    req(receipt["predecessor_v29"]["main_state_blob_sha1"] == PREDECESSOR_STATE_BLOB, "predecessor state blob")
    req(receipt["predecessor_v29"]["main_state_canonical_sha256"] == PREDECESSOR_STATE_CANON, "predecessor state canonical")
    audit = receipt["hostile_audit"]
    req(audit["audited_exact_head"] == PREDECESSOR_HEAD, "audited head")
    req(audit["review_id"] == AUDIT_REVIEW_ID and audit["status"] == "PASS", "audit PASS identity")
    req(audit["merge_ready_freshness"] == "CLEAR", "audit freshness")
    req(audit["current_repository_main_at_audit"] == CURRENT_MAIN, "audit current main")
    promoted = receipt["promoted_authority"]
    req(promoted["remaining_strata"] == 17128, "strata changed")
    req(promoted["remaining_terminals_upper_bound"] == BOUND, "bound changed")
    req(promoted["additional_pruning_added_by_sync"] == 0, "sync added pruning")
    req(promoted["replacement_head_hostile_reaudit_required"] is False, "audit freeze not released")
    req(receipt["claim_sync"]["claim_core_mutated"] is False, "claim core mutated")
    req(receipt["claim_sync"]["full178_status"] == "ACTIVE_INCOMPLETE", "FULL178 status")
    req(all(receipt["firewalls"][k] is False for k in (
        "full178_complete","effectivity_credit","receiver_credit","theorem_credit",
        "endpoint_credit","stage32_closed","perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim","merge_authorized"
    )), "credit firewall")

    if args.audited_v29_root:
        root = Path(args.audited_v29_root)
        p = root / "stages/stage32/MAIN-STATE.json"
        req(p.is_file(), "missing audited V29 state")
        req(blob(p) == PREDECESSOR_STATE_BLOB, "audited V29 state blob drift")
        old = json.loads(p.read_text(encoding="utf-8"))
        req(old.get("canonical_sha256_without_this_field") == PREDECESSOR_STATE_CANON, "audited V29 stored canonical")
        req(canon(old) == PREDECESSOR_STATE_CANON, "audited V29 canonical")
        req(old["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "audited V29 stop gate")
        req(old["current_exact_frontier"]["authoritative_remaining_terminals"] == BOUND, "audited V29 bound")

    current = json.loads(STATE.read_text(encoding="utf-8"))
    req(current["schema"] == "STAGE32_MAIN_COMPACT_STATE_V30_HPADJ08_AUDIT_SYNCED", "current state schema")
    req(current["current"]["mainbatch_stop_gate"] == "NONE", "current stop gate")
    req(current["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "current audit firewall")
    req(current["current_exact_frontier"]["authoritative_remaining_terminals"] == BOUND, "current bound")
    req(current["authority_sync"]["v29_hpadj08_replacement_hostile_audit_review_id"] == AUDIT_REVIEW_ID, "current audit review")

    print("PASS: Stage32 MAIN V30 HPADJ08 hostile-audit PASS synchronization")
    print("PASS: additional_pruning=0 stop_gate=NONE FULL178=ACTIVE_INCOMPLETE merge_authorized=false")

if __name__ == "__main__":
    main()
