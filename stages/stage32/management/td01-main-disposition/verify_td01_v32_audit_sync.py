#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RECEIPT = HERE / "TD01-V32-HOSTILE-AUDIT-PASS-SYNC.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"

PREDECESSOR_HEAD = "f5558f0d1b23c6dd48519207e1dc872ae66127d7"
PREDECESSOR_STATE_BLOB = "a7f58ca7cccee3f0e3ae538288d3298cf5571bb6"
PREDECESSOR_STATE_CANON = "0da2f2bc76d0a27b12277bbcf3f823293465f7e937afb80e75940db7f8aed31e"
AUDIT_REVIEW_ID = 5216133884
CURRENT_MAIN = "c6284abbb29930255892d56f800da0ea1e34734b"
RECEIPT_CANON = "0f504c054e951763580c7aadf293c38600c3cf201e4c8c6055006ee80f4a69bb"
BOUND = 3453268626299532038131
HPADJ11_BOUND = 3360778813767800658369

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
    ap.add_argument("--audited-v31-root")
    args = ap.parse_args()

    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    req(receipt["schema"] == "STAGE32_MAIN_TD01_V32_HOSTILE_AUDIT_PASS_SYNC_V1", "receipt schema")
    req(receipt.get("canonical_sha256_without_this_field") == RECEIPT_CANON, "receipt stored canonical")
    req(canon(receipt) == RECEIPT_CANON, "receipt canonical")
    req(receipt["predecessor_v31"]["exact_head"] == PREDECESSOR_HEAD, "predecessor head")
    req(receipt["predecessor_v31"]["main_state_blob_sha1"] == PREDECESSOR_STATE_BLOB, "predecessor state blob")
    req(receipt["predecessor_v31"]["main_state_canonical_sha256"] == PREDECESSOR_STATE_CANON, "predecessor state canonical")
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
    hp = receipt["next_audited_candidate"]
    req(hp["audited_exact_head"] == "1c694f6650125a8fb0121925beff7f800b5d6283", "HPADJ11 audited head")
    req(hp["hostile_audit_review_id"] == 5216065509, "HPADJ11 audit review")
    req(hp["candidate_upper_bound"] == HPADJ11_BOUND, "HPADJ11 bound")
    req(hp["main_consumption_performed"] is False and hp["additional_v32_credit"] == 0, "V32 consumed HPADJ11")
    req(hp["additive_stacking_authorized"] is False, "same-character stacking")
    req(receipt["claim_sync"]["claim_core_mutated"] is False, "claim core mutated")
    req(receipt["claim_sync"]["full178_status"] == "ACTIVE_INCOMPLETE", "FULL178 status")
    req(all(receipt["firewalls"][k] is False for k in (
        "full178_complete","effectivity_credit","receiver_credit","theorem_credit",
        "endpoint_credit","stage32_closed","perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim","merge_authorized"
    )), "credit firewall")

    if args.audited_v31_root:
        root = Path(args.audited_v31_root)
        p = root / "stages/stage32/MAIN-STATE.json"
        req(p.is_file(), "missing audited V31 state")
        req(blob(p) == PREDECESSOR_STATE_BLOB, "audited V31 state blob drift")
        old = json.loads(p.read_text(encoding="utf-8"))
        req(old.get("canonical_sha256_without_this_field") == PREDECESSOR_STATE_CANON, "audited V31 stored canonical")
        req(canon(old) == PREDECESSOR_STATE_CANON, "audited V31 canonical")
        req(old["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "audited V31 stop gate")
        req(old["current_exact_frontier"]["authoritative_remaining_terminals"] == BOUND, "audited V31 bound")

    current = json.loads(STATE.read_text(encoding="utf-8"))
    req(current["schema"] == "STAGE32_MAIN_COMPACT_STATE_V32_TD01_AUDIT_SYNCED_HPADJ11_QUEUED", "current state schema")
    req(current["current"]["mainbatch_stop_gate"] == "NONE", "current stop gate")
    req(current["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "current audit firewall")
    req(current["current_exact_frontier"]["authoritative_remaining_terminals"] == BOUND, "current bound")
    req(current["authority_sync"]["v31_td01_replacement_hostile_audit_review_id"] == AUDIT_REVIEW_ID, "current audit review")
    req(current["current_exact_frontier"]["hpadj11_refined_upper_bound_candidate"] == HPADJ11_BOUND, "current HPADJ11 queue")
    req(current["current_exact_frontier"]["hpadj11_main_consumption_performed"] is False, "current HPADJ11 credit")

    print("PASS: Stage32 MAIN V32 TD01 hostile-audit PASS synchronization")
    print("PASS: additional_pruning=0 stop_gate=NONE HPADJ11=audited_queued FULL178=ACTIVE_INCOMPLETE merge_authorized=false")

if __name__ == "__main__":
    main()
