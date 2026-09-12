#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = STAGE.parents[1]
STATE = STAGE / "MAIN-STATE.json"
RECEIPT = STAGE / "management/post-n358-v19-hostile-reaudit-pass-n372-reaudit-selection-20260913.json"

STATE_BLOB = "0886dc0c0a8b8960ca9b5cf8285801d4948de874"
STATE_CANON = "5b087c68f0d81893c65c8210cca112e57d881bcb0713c6ed81ff46d300584cd2"
RECEIPT_BLOB = "52f503f3ae09f89fd866eac4004397a55862ac10"
RECEIPT_CANON = "29283316f04a1b8d9a3c6ec5673df3325725325a7b57bd3843b576c58158ae04"
AUTH_STRATA = 17128
AUTH_TERMS = 47589703313957134886123
N358_INCREMENT = 9274971107798843958
N372_HEAD = "9fb78a0e0c7b52baca84058dea69b8b083e33774"
N372_CI = 34700502007
N372_REVIEW = 5187357950
V19_REVIEW = 5186730520

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path) == blob, f"blob drift {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"canonical drift {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    state = locked(STATE, STATE_BLOB, STATE_CANON)
    receipt = locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == AUTH_STRATA, "strata drift")
    req(f["authoritative_remaining_terminals"] == AUTH_TERMS, "terminal authority drift")
    req(f["n358_incremental_rejected_terminals"] == N358_INCREMENT, "N358 increment drift")
    req(f["n358_main_pruning_credit"] is True, "N358 credit lost")
    req(f["n358_synchronized_head_hostile_audited"] is True, "N358 hostile re-audit sync missing")
    req(f["cut193_main_pruning_credit"] is False, "CUT193 gained credit")
    req(f["cut197_main_pruning_credit"] is False, "CUT197 gained credit")
    req(f["n372_candidate_exact_head"] == N372_HEAD, "N372 selected head drift")
    req(f["n372_candidate_exact_head_ci_run"] == N372_CI, "N372 selected CI drift")
    req(f["n372_candidate_hostile_audited"] is True, "N372 PASS not synchronized")
    req(f["n372_candidate_hostile_audit_review_id"] == N372_REVIEW, "N372 review drift")
    req(f["n372_current_authority_rebased"] is False, "N372 current-authority rebase self-awarded")
    req(f["n372_current_v15_witness_candidate_only"] is True, "N372 witness-only marker lost")
    req(f["n372_main_pruning_credit"] is False, "N372 MAIN credit opened")
    req(f["n372_full178_credit"] is False, "N372 FULL178 credit opened")
    req(f["n372_effectivity_final_credit"] is False, "N372 effectivity credit opened")
    req(f["full178_numerical_census_complete"] is False, "FULL178 incorrectly closed")
    req(f["stage32_closed"] is False, "Stage32 incorrectly closed")
    auth = state["authority_sync"]
    req(auth["n358_post_sync_reaudit_review_id"] == V19_REVIEW, "V19 audit review drift")
    req(auth["n358_post_sync_reaudit_status"] == "PASS", "V19 audit PASS missing")
    req(auth["n372_candidate_hostile_audit_status"] == "PASS_CURRENT_V15_WITNESS_ONLY", "N372 audit route drift")
    req(auth["n372_candidate_hostile_audit_review_id"] == N372_REVIEW, "N372 audit review metadata drift")
    req(auth["n372_current_authority_rebased"] is False, "N372 rebase flag drift")
    req(auth["n372_main_pruning_credit_consumed"] is False, "N372 consumption self-awarded")
    req(auth["cut197_main_pruning_credit_consumed"] is False, "CUT197 consumption drift")
    rr = receipt["n372_candidate"]
    req(rr["repaired_exact_head"] == N372_HEAD, "receipt N372 exact head drift")
    req(rr["repaired_exact_head_ci_run"] == N372_CI and rr["repaired_exact_head_ci_status"] == "SUCCESS", "receipt N372 CI drift")
    req(rr["hostile_audit_review_id"] == N372_REVIEW, "receipt N372 review drift")
    req(rr["hostile_audit_status"] == "PASS_CURRENT_V15_WITNESS_ONLY", "receipt N372 audit status drift")
    req(rr["current_authority_rebase_status"] == "PENDING_MAIN_V20_AUDIT_THEN_REBASE", "receipt N372 rebase gate drift")
    req(receipt["authority"]["incremental_rejected_terminals"] == 0, "V20 synchronization changed numerical authority")
    req(receipt["authority"]["after_remaining_terminals"] == AUTH_TERMS, "receipt authority drift")
    fw = state["firewalls"]
    for key in ("receiver_credit","theorem_credit","endpoint_credit","route_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(fw[key] is False, f"firewall opened: {key}")
    print(json.dumps({"verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V20","n358_main_consumed_reaudited":True,"n372_hostile_audit_pass_current_v15_witness_only":True,"n372_candidate_exact_head":N372_HEAD,"n372_current_authority_rebased":False,"n372_main_pruning_credit":False,"cut197_main_credit":False,"authoritative_remaining_strata":AUTH_STRATA,"authoritative_remaining_terminals":AUTH_TERMS,"full178_complete":False,"merge_authorized":False}, sort_keys=True))

if __name__ == "__main__":
    main()
