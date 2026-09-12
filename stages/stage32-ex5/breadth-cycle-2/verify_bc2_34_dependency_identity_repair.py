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
CHECKPOINT_CANON = "e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba"
CHECKPOINT_BLOB = "e566aeda2931642d79c88dc5eeb84b142f655609"
UNKNOWN64_SHA = "00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b"
V22 = "STAGE32EX5_MAIN_COMPACT_STATE_V22_BC2_34_TARGETED_REPLAY_AUDIT_BOUNDARY"
V23 = "STAGE32EX5_MAIN_COMPACT_STATE_V23_BC2_34_AUDIT_CONSUMED_BC2_35_EXECUTION"
V24 = "STAGE32EX5_MAIN_COMPACT_STATE_V24_BC2_35_TARGETED_REPLAY_AUDIT_BOUNDARY"


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
    q = dict(repair)
    got = q.pop("canonical_sha256_without_this_field", None)
    req(got == REPAIR_CANON and csha(q) == REPAIR_CANON, "BC2-34 dependency repair receipt canonical drift")
    req(repair["schema"] == "STAGE32EX5_BC2_34_DEPENDENCY_IDENTITY_REPAIR_V1", "repair schema drift")
    req(repair["status"] == "REPAIRED_HOSTILE_REAUDIT_REQUIRED", "repair status drift")

    failed = repair["failed_audit"]
    req((failed["exact_head"], failed["review_id"], failed["verdict"]) == (FAILED_AUDIT_HEAD, FAILED_AUDIT_REVIEW, "FAIL"), "failed audit receipt drift")

    ident = repair["execution_identity"]
    req(ident["bc2_34_execution_head"] == EXECUTION_HEAD, "BC2-34 execution head identity drift")
    req(ident["bc2_34_producer_git_blob_sha"] == B34_BLOB, "BC2-34 producer identity drift")
    req(ident["bc2_32_producer_git_blob_sha"] == B32_BLOB, "retained BC2-32 identity drift")
    req(ident["execution_head_bc2_32_identity_independently_confirmed_by_failed_audit"] is True, "execution-head BC2-32 confirmation missing")
    req(ident["repair_head_must_match_execution_bc2_32_blob"] is True, "repair/current-head equality firewall missing")

    req(git_blob(B32) == B32_BLOB, "current BC2-32 producer blob differs from immutable execution-head identity")
    req(git_blob(B34) == B34_BLOB, "BC2-34 executed producer source drift")

    src = B32.read_text()
    req(f'B19_BLOB = "{B19_BLOB}"' in src, "BC2-32 B19 lock missing")
    req(f'D18_BLOB = "{D18_BLOB}"' in src, "BC2-32 D18 lock missing")
    req('if git_blob_sha(Path(b19.__file__).resolve()) != B19_BLOB:' in src, "BC2-32 B19 fail-close guard missing")
    req('if git_blob_sha(Path(d18.__file__).resolve()) != D18_BLOB:' in src, "BC2-32 D18 fail-close guard missing")

    trans = repair["transitive_dependency_contract"]
    req(trans["bc2_32_build_parent_space_directly_used"] is True, "direct BC2-32 dependency declaration missing")
    req(trans["bc2_32_bc2_19_source_git_blob_sha"] == B19_BLOB, "repair B19 lock drift")
    req(trans["bc2_32_bc2_18_source_git_blob_sha"] == D18_BLOB, "repair D18 lock drift")
    req(trans["bc2_32_source_itself_checks_bc2_19_and_bc2_18_before_parent_space_construction"] is True, "transitive guard contract drift")

    kept = repair["retained_result_unchanged"]
    req(kept["checkpoint_canonical"] == CHECKPOINT_CANON and kept["checkpoint_git_blob_sha"] == CHECKPOINT_BLOB, "retained BC2-34 checkpoint identity drift")
    req(kept["result"] == {"unsat": 17, "unknown": 64, "sat": 0}, "retained BC2-34 partition drift")
    req(kept["known_parent_unsat_count_lower_bound"] == 7272, "retained BC2-34 lower bound drift")
    req(kept["remaining_unknown_parent_indices_sha256"] == UNKNOWN64_SHA, "retained BC2-34 UNKNOWN hash drift")
    req(all(v is False for v in repair["firewalls"].values()), "repair firewall leak")

    rk = json.loads(RUNKEY.read_text())
    rc = rk.get("consumed_run") or {}
    dep = rc.get("dependency_identity_repair") or {}
    req(dep["bc2_32_producer_git_blob_sha"] == B32_BLOB, "run receipt missing BC2-32 source lock")
    req(dep["execution_head"] == EXECUTION_HEAD, "run receipt execution head drift")
    req(dep["failed_audit_exact_head"] == FAILED_AUDIT_HEAD and dep["failed_audit_review_id"] == FAILED_AUDIT_REVIEW, "run receipt failed-audit provenance drift")
    req(dep["repair_receipt_git_blob_sha"] == REPAIR_BLOB and dep["repair_receipt_canonical"] == REPAIR_CANON, "run receipt repair identity drift")
    req(dep["heavy_recompute_performed"] is False and dep["mathematical_result_rewritten"] is False, "repair improperly rewrote computation")

    state = json.loads(STATE.read_text())
    schema = state["schema"]
    req(schema in {V22, V23, V24}, "EX5 state schema drift")
    if schema == V22:
        req(state["current"]["status"] == "BC2_34_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "BC2-34 audit-required state drift")
        req(state["current"]["next_route"] == "HOSTILE_AUDIT_BC2_34_TARGETED_REPLAY", "BC2-34 re-audit route drift")
        audit = state["intermediate_audit_boundary"]
        req(audit["freeze_active"] is True and audit["new_audit_boundary_exists"] is True and audit["re_audit_required"] is True, "BC2-34 repaired boundary is not frozen")
        req(state["next_step"]["bc2_35_blocked_until_bc2_34_hostile_audit_pass"] is True, "BC2-35 released before BC2-34 re-audit PASS")
        next_label = "stage32ex5-audit"
    else:
        pa = state["prior_audited_authority"]["bc2_34_pr_1776"]
        req(pa["hostile_audit_status"] == "PASS", "BC2-34 hostile re-audit PASS not consumed")
        req(pa["audit_checkpoint_exact_head"] == REAUDIT_HEAD and pa["hostile_audit_review_id"] == REAUDIT_REVIEW, "BC2-34 re-audit receipt drift")
        req(pa["prior_failed_audit_exact_head"] == FAILED_AUDIT_HEAD and pa["prior_failed_audit_review_id"] == FAILED_AUDIT_REVIEW, "BC2-34 failed-audit provenance lost after consumption")
        req(state["frontier"]["e8_bc2_34_audited"] is True, "BC2-34 audited frontier marker missing")
        req(state["frontier"]["e8_bc2_34_remaining_unknown_count"] == 64 and state["frontier"]["e8_bc2_34_remaining_unknown_parent_indices_sha256"] == UNKNOWN64_SHA, "BC2-34 audited residual drift")
        audit = state["intermediate_audit_boundary"]
        req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == REAUDIT_HEAD and audit["last_hostile_audit_review_id"] == REAUDIT_REVIEW, "live BC2-34 re-audit receipt drift")
        req(audit["bc2_34_execution_authorized"] is False, "BC2-34 execution unexpectedly authorized")
        if schema == V23:
            req(audit["freeze_active"] is False and audit["new_audit_boundary_exists"] is False and audit["re_audit_required"] is False, "BC2-35 execution incorrectly frozen")
            req(audit["bc2_35_execution_authorized"] is True, "BC2-35 execution authorization drift")
            req(state["current"]["status"] == "BC2_35_TARGETED_REPLAY_EXECUTION_AUTHORIZED", "BC2-35 execution state drift")
            req(state["current"]["next_route"] == "BC2_35_REFINE_REMAINING_FRESH_UNKNOWN_SET", "BC2-35 route drift")
            req(state["next_step"]["bc2_35_execution_authorized"] is True and state["next_step"]["bc2_36_blocked_until_bc2_35_hostile_audit_pass"] is True, "BC2-35/36 routing firewall drift")
            next_label = "stage32ex5-mainbatch"
        else:
            req(audit["freeze_active"] is True and audit["new_audit_boundary_exists"] is True and audit["re_audit_required"] is True, "BC2-35 audit boundary is not frozen")
            req(audit["bc2_35_execution_authorized"] is False, "BC2-35 execution not retired at audit boundary")
            req(state["current"]["status"] == "BC2_35_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "BC2-35 audit-required state drift")
            req(state["current"]["next_route"] == "HOSTILE_AUDIT_BC2_35_TARGETED_REPLAY", "BC2-35 audit route drift")
            req(state["frontier"]["e8_bc2_35_executed"] is True and state["frontier"]["e8_bc2_35_audited"] is False, "BC2-35 retained/audit marker drift")
            req(state["frontier"]["e8_known_parent_unsat_count_lower_bound"] == 7272 and state["frontier"]["e8_bc2_35_candidate_known_parent_unsat_count_lower_bound"] == 7284, "BC2-35 candidate leaked into audited lower bound")
            req(state["next_step"]["bc2_35_execution_authorized"] is False and state["next_step"]["bc2_36_blocked_until_bc2_35_hostile_audit_pass"] is True, "BC2-35/36 audit routing firewall drift")
            next_label = "stage32ex5-audit"

    print("PASS: BC2-34 directly executed BC2-32 dependency identity is fail-closed")
    print(f"execution_head={EXECUTION_HEAD}; bc2_32_blob={B32_BLOB}; failed_audit_review={FAILED_AUDIT_REVIEW}")
    print(f"heavy_recompute=NO; mathematical_result_rewritten=NO; next={next_label}")


if __name__ == "__main__":
    main()
