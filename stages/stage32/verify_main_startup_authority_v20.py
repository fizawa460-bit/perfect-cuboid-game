#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
SNAPSHOT = HERE / "management/MAIN-STATE-V19-N358-PRE-REAUDIT.json"
RECEIPT = HERE / "management/post-n358-v19-hostile-reaudit-pass-n372-reaudit-selection-20260913.json"

STATE_BLOB = "c9b5f71c49904ee0afbb929346e27d1f89c60f83"
STATE_CANON = "8d705f54fa7d90f8344917e7fc1f3709da5a598a5ce3b546eae1d826e1b2df6d"
V19_STATE_BLOB = "acad022fe90b4d72edeac5f9d7ba08930decdff2"
V19_STATE_CANON = "2f0ed49bd3640f4f7158176bc435344d46785928e20c4ce67173305eb3974771"
RECEIPT_BLOB = "de96a11ff5cbbbefd15f242a4a18324d1cbb9907"
RECEIPT_CANON = "70bbf092d62cc696ab51b80cbd2fb8615ef1e55fa532145c3bbd832a74dafb58"
V19_HEAD = "56c52a64dc402126431a6de6d023007052f4112c"
V19_REVIEW = 5186730520
N372_HEAD = "9fb78a0e0c7b52baca84058dea69b8b083e33774"
N372_CI = 34700502007
AUTH_STRATA = 17128
AUTH_TERMS = 47589703313957134886123

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path}")
    req(canonical(obj) == can, f"canonical drift {path}")
    return obj

def main() -> None:
    state = locked(STATE, STATE_BLOB, STATE_CANON)
    old = locked(SNAPSHOT, V19_STATE_BLOB, V19_STATE_CANON)
    receipt = locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)

    oldf = old["current_exact_frontier"]
    req(oldf["authoritative_remaining_strata"] == AUTH_STRATA, "V19 strata drift")
    req(oldf["authoritative_remaining_terminals"] == AUTH_TERMS, "V19 terminal authority drift")
    req(oldf["n358_main_pruning_credit"] is True, "V19 N358 credit missing")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == AUTH_STRATA, "V20 strata drift")
    req(f["authoritative_remaining_terminals"] == AUTH_TERMS, "V20 terminal authority drift")
    req(f["n358_main_pruning_credit"] is True, "V20 N358 credit lost")
    req(f["n358_synchronized_head_hostile_audited"] is True, "V20 N358 audit sync missing")
    req(f["cut193_main_pruning_credit"] is False, "CUT193 gained credit")
    req(f["cut197_main_pruning_credit"] is False, "CUT197 gained credit")
    req(f["n372_candidate_exact_head"] == N372_HEAD, "N372 head drift")
    req(f["n372_candidate_exact_head_ci_run"] == N372_CI, "N372 CI drift")
    req(f["n372_candidate_hostile_audited"] is False, "N372 self-awarded hostile audit")
    req(f["n372_current_v15_witness_candidate_only"] is True, "N372 witness-only marker lost")
    req(f["n372_main_pruning_credit"] is False, "N372 MAIN credit opened")
    req(f["n372_full178_credit"] is False, "N372 FULL178 credit opened")
    req(f["n372_effectivity_final_credit"] is False, "N372 effectivity credit opened")
    req(f["full178_numerical_census_complete"] is False, "FULL178 incorrectly closed")
    req(f["stage32_closed"] is False, "Stage32 incorrectly closed")

    auth = state["authority_sync"]
    req(auth["n358_post_sync_reaudit_exact_head"] == V19_HEAD, "V19 audit head drift")
    req(auth["n358_post_sync_reaudit_review_id"] == V19_REVIEW, "V19 audit review drift")
    req(auth["n358_post_sync_reaudit_status"] == "PASS", "V19 hostile re-audit not PASS")
    req(auth["n358_synchronized_head_hostile_audited"] is True, "N358 synchronized audit false")
    req(auth["n372_candidate_hostile_audit_status"] == "PENDING_REAUDIT", "N372 audit gate drift")
    req(auth["n372_main_pruning_credit_consumed"] is False, "N372 consumption self-awarded")

    pr = receipt["prior_main_boundary"]
    req(pr["exact_head"] == V19_HEAD and pr["hostile_reaudit_review_id"] == V19_REVIEW, "receipt V19 audit identity drift")
    req(pr["hostile_reaudit_status"] == "PASS", "receipt V19 audit status drift")
    req(pr["authoritative_remaining_strata"] == AUTH_STRATA, "receipt V19 strata drift")
    req(pr["authoritative_remaining_terminals"] == AUTH_TERMS, "receipt V19 terminals drift")
    ra = receipt["authority"]
    req(ra["before_remaining_terminals"] == AUTH_TERMS, "receipt pre-authority drift")
    req(ra["incremental_rejected_terminals"] == 0, "V20 synchronization changed authority")
    req(ra["after_remaining_terminals"] == AUTH_TERMS, "receipt post-authority drift")

    n372 = receipt["n372_candidate"]
    req(n372["repaired_exact_head"] == N372_HEAD, "receipt N372 head drift")
    req(n372["repaired_exact_head_ci_run"] == N372_CI and n372["repaired_exact_head_ci_status"] == "SUCCESS", "receipt N372 CI drift")
    req(n372["hostile_audit_status"] == "PENDING_REAUDIT", "receipt N372 audit status drift")
    req(n372["prior_failed_audit_review_id"] == 5186762166, "receipt prior N372 FAIL review drift")

    fw = state["firewalls"]
    for key in ("receiver_credit","theorem_credit","endpoint_credit","route_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(fw[key] is False, f"firewall opened: {key}")

    print(json.dumps({
        "verdict":"PASS_STAGE32_MAIN_V20_N358_REAUDIT_SYNC_N372_ZERO_CREDIT_SELECTION",
        "v19_hostile_reaudit_review_id":V19_REVIEW,
        "authority_unchanged":True,
        "authoritative_remaining_strata":AUTH_STRATA,
        "authoritative_remaining_terminals":AUTH_TERMS,
        "n372_candidate_exact_head":N372_HEAD,
        "n372_hostile_audit_status":"PENDING_REAUDIT",
        "n372_main_pruning_credit":False,
        "full178_complete":False,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
