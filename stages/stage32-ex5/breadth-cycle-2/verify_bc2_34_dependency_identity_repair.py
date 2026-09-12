#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
EX5 = HERE.parent
REPAIR = HERE / "bc2-34-dependency-identity-repair.json"
B32 = HERE / "bc2_32_replay_explicit_fresh_unknown170.py"
B34 = HERE / "bc2_34_replay_explicit_fresh_unknown81.py"
RUNKEY = EX5 / "runkeys" / "bc2-34-fresh-unknown81-replay.json"
STATE = EX5 / "MAIN-STATE.json"

REPAIR_BLOB = "5569d0d0c806db361ad6cafdafbe5e7911850e4c"
REPAIR_CANON = "fb111cd123eb1ee0aa99848fc7c75bd976684517cd63a2bfd44f9e9abdaed01f"
B32_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
B34_BLOB = "eb715ed7cc5bb350b15e35868e2f79c548f17e28"
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EXECUTION_HEAD = "79167ffcdd0be4cf3bdcb7e652fad38acb447fb4"
FAILED_AUDIT_HEAD = "75723b1626d7f40eb1ab75a1a52f2fc679d619bf"
FAILED_AUDIT_REVIEW = 5186319290
REAUDIT_HEAD = "cdb455860849cfd064e3ab8c83d6d4993fb5ff1b"
REAUDIT_REVIEW = 5186516652
BC2_35_AUDIT_HEAD = "8bea7a6be26e01db0deb138dbd8406f578447921"
BC2_35_AUDIT_REVIEW = 5187359907
CHECKPOINT_CANON = "e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba"
CHECKPOINT_BLOB = "e566aeda2931642d79c88dc5eeb84b142f655609"
UNKNOWN64_SHA = "00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b"
V22 = "STAGE32EX5_MAIN_COMPACT_STATE_V22_BC2_34_TARGETED_REPLAY_AUDIT_BOUNDARY"
V23 = "STAGE32EX5_MAIN_COMPACT_STATE_V23_BC2_34_AUDIT_CONSUMED_BC2_35_EXECUTION"
V24 = "STAGE32EX5_MAIN_COMPACT_STATE_V24_BC2_35_TARGETED_REPLAY_AUDIT_BOUNDARY"
V25 = "STAGE32EX5_MAIN_COMPACT_STATE_V25_BC2_35_AUDIT_CONSUMED_BC2_36_EXECUTION"
V26 = "STAGE32EX5_MAIN_COMPACT_STATE_V26_BC2_36_TARGETED_REPLAY_AUDIT_BOUNDARY"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(git_blob(REPAIR) == REPAIR_BLOB, "BC2-34 dependency repair receipt blob drift")
    repair = json.loads(REPAIR.read_text())
    q = dict(repair); got = q.pop("canonical_sha256_without_this_field", None)
    req(got == REPAIR_CANON and csha(q) == REPAIR_CANON, "BC2-34 dependency repair receipt canonical drift")
    req(repair["schema"] == "STAGE32EX5_BC2_34_DEPENDENCY_IDENTITY_REPAIR_V1" and repair["status"] == "REPAIRED_HOSTILE_REAUDIT_REQUIRED", "repair contract drift")
    failed = repair["failed_audit"]
    req((failed["exact_head"], failed["review_id"], failed["verdict"]) == (FAILED_AUDIT_HEAD, FAILED_AUDIT_REVIEW, "FAIL"), "failed audit receipt drift")
    ident = repair["execution_identity"]
    req(ident["bc2_34_execution_head"] == EXECUTION_HEAD and ident["bc2_34_producer_git_blob_sha"] == B34_BLOB and ident["bc2_32_producer_git_blob_sha"] == B32_BLOB, "BC2-34 execution identity drift")
    req(git_blob(B32) == B32_BLOB and git_blob(B34) == B34_BLOB, "BC2-34 executable source drift")
    src = B32.read_text()
    req(f'B19_BLOB = "{B19_BLOB}"' in src and f'D18_BLOB = "{D18_BLOB}"' in src, "BC2-32 transitive source locks missing")
    req('if git_blob_sha(Path(b19.__file__).resolve()) != B19_BLOB:' in src and 'if git_blob_sha(Path(d18.__file__).resolve()) != D18_BLOB:' in src, "BC2-32 transitive fail-close guards missing")
    kept = repair["retained_result_unchanged"]
    req(kept["checkpoint_canonical"] == CHECKPOINT_CANON and kept["checkpoint_git_blob_sha"] == CHECKPOINT_BLOB, "BC2-34 checkpoint identity drift")
    req(kept["result"] == {"unsat":17,"unknown":64,"sat":0} and kept["known_parent_unsat_count_lower_bound"] == 7272 and kept["remaining_unknown_parent_indices_sha256"] == UNKNOWN64_SHA, "BC2-34 retained result drift")
    req(all(v is False for v in repair["firewalls"].values()), "BC2-34 repair firewall leak")

    rk = json.loads(RUNKEY.read_text()); dep = (rk.get("consumed_run") or {}).get("dependency_identity_repair") or {}
    req(dep.get("bc2_32_producer_git_blob_sha") == B32_BLOB and dep.get("execution_head") == EXECUTION_HEAD, "BC2-34 run receipt source identity drift")
    req(dep.get("failed_audit_exact_head") == FAILED_AUDIT_HEAD and dep.get("failed_audit_review_id") == FAILED_AUDIT_REVIEW, "BC2-34 failed-audit provenance drift")
    req(dep.get("repair_receipt_git_blob_sha") == REPAIR_BLOB and dep.get("repair_receipt_canonical") == REPAIR_CANON, "BC2-34 repair receipt identity drift")
    req(dep.get("heavy_recompute_performed") is False and dep.get("mathematical_result_rewritten") is False, "BC2-34 repair improperly rewrote computation")

    state = json.loads(STATE.read_text()); schema = state["schema"]
    req(schema in {V22,V23,V24,V25,V26}, "EX5 state schema drift")
    if schema != V22:
        pa = state["prior_audited_authority"]["bc2_34_pr_1776"]
        req(pa["hostile_audit_status"] == "PASS" and pa["audit_checkpoint_exact_head"] == REAUDIT_HEAD and pa["hostile_audit_review_id"] == REAUDIT_REVIEW, "BC2-34 hostile re-audit PASS not preserved")
        req(pa["prior_failed_audit_exact_head"] == FAILED_AUDIT_HEAD and pa["prior_failed_audit_review_id"] == FAILED_AUDIT_REVIEW, "BC2-34 failed-audit provenance lost")
        req(state["frontier"]["e8_bc2_34_audited"] is True and state["frontier"]["e8_bc2_34_remaining_unknown_count"] == 64 and state["frontier"]["e8_bc2_34_remaining_unknown_parent_indices_sha256"] == UNKNOWN64_SHA, "BC2-34 audited frontier drift")
    if schema in {V25,V26}:
        pa35 = state["prior_audited_authority"]["bc2_35_pr_1776"]
        req(pa35["hostile_audit_status"] == "PASS" and pa35["audit_checkpoint_exact_head"] == BC2_35_AUDIT_HEAD and pa35["hostile_audit_review_id"] == BC2_35_AUDIT_REVIEW, "BC2-35 hostile audit PASS not consumed")
    if schema == V26:
        audit = state["intermediate_audit_boundary"]
        req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == BC2_35_AUDIT_HEAD and audit["last_hostile_audit_review_id"] == BC2_35_AUDIT_REVIEW, "live BC2-35 audit receipt drift")
        req(audit["freeze_active"] is True and audit["new_audit_boundary_exists"] is True and audit["re_audit_required"] is True and audit["bc2_36_execution_authorized"] is False, "BC2-36 audit boundary not frozen")
        req(state["current"]["status"] == "BC2_36_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED" and state["current"]["next_route"] == "HOSTILE_AUDIT_BC2_36_TARGETED_REPLAY", "BC2-36 audit route drift")
        req(state["next_step"]["bc2_37_blocked_until_bc2_36_hostile_audit_pass"] is True, "BC2-37 released early")
        next_label = "stage32ex5-audit"
    elif schema == V25:
        next_label = "stage32ex5-mainbatch"
    else:
        next_label = "stage32ex5-audit" if schema in {V22,V24} else "stage32ex5-mainbatch"

    print("PASS: BC2-34 directly executed BC2-32 dependency identity is fail-closed")
    print(f"execution_head={EXECUTION_HEAD}; bc2_32_blob={B32_BLOB}; failed_audit_review={FAILED_AUDIT_REVIEW}")
    print(f"heavy_recompute=NO; mathematical_result_rewritten=NO; next={next_label}")


if __name__ == "__main__":
    main()
