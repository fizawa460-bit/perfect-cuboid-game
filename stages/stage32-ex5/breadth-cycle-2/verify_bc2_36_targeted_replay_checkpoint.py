#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHECKPOINT = HERE / "bc2-36-fresh-unknown52-replay-checkpoint.json"
RUNKEY = ROOT / "runkeys" / "bc2-36-fresh-unknown52-replay.json"
SOURCE = HERE / "bc2_36_replay_explicit_fresh_unknown52.py"
PREFLIGHT = HERE / "bc2-36-fresh-unknown52-replay-preflight.json"
B32 = HERE / "bc2_32_replay_explicit_fresh_unknown170.py"
B19 = HERE / "bc2_19_n354_survivor_normal_positivity_mass_replay.py"
B18 = HERE / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py"
STATE = ROOT / "MAIN-STATE.json"
WORKFLOW = HERE.parents[2] / ".github/workflows/stage32-ex5-main.yml"

CP_BLOB = "09ac58349e388c479ac77e04724bef2fd9b49b7e"
CP_CANON = "e92cd6d07299b833a79fe20b81e9de032d61790cf1b7a6fb81ec6adccdb49fdf"
RUNKEY_BLOB = "78d9c847863232b10d149b651c32c668887e4b23"
SOURCE_BLOB = "18f9c2146d5dc97400c4af1a8691560523cc03cf"
PREFLIGHT_BLOB = "aa9bf40cf3550cae33cdfe8669aa51a80acddcec"
PREFLIGHT_CANON = "b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0"
B32_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
B18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
TARGET_SHA = "95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818"
UNKNOWN_SHA = "570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9"
STATUS_SHA = "59c8f444d235a7b3223d2ef4df5c2da65636f66edc3f69ebd2572c2d3354dff8"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(git_blob(CHECKPOINT) == CP_BLOB, "BC2-36 checkpoint blob drift")
    cp = json.loads(CHECKPOINT.read_text())
    req(cp["schema"] == "STAGE32EX5_BC2_36_FRESH_UNKNOWN52_REPLAY_V1", "BC2-36 checkpoint schema drift")
    req(cp["canonical_sha256_without_this_field"] == CP_CANON and canonical(cp) == CP_CANON, "BC2-36 checkpoint canonical drift")
    r = cp["replay"]
    req((r["parents_checked"], r["unsat_count"], r["unknown_count"], r["sat_count"]) == (52, 11, 41, 0), "BC2-36 partition drift")
    req(r["per_parent_timeout_ms"] == 100000, "BC2-36 timeout drift")
    req(r["unknown_parent_indices_sha256"] == UNKNOWN_SHA and len(r["unknown_parent_indices"]) == 41, "BC2-36 UNKNOWN identity drift")
    req(r["status_stream_sha256"] == STATUS_SHA, "BC2-36 status stream drift")
    req(len(r["unsat_parent_indices"]) == 11 and set(r["unsat_parent_indices"]).isdisjoint(r["unknown_parent_indices"]), "BC2-36 retained partition overlap")
    target = cp["target"]
    req(target["audited_bc2_35_unknown_count"] == 52 and target["parent_indices_sha256"] == TARGET_SHA and target["prior_audited_unsat_count"] == 7284, "BC2-36 target drift")
    req(sorted(target["parent_indices"]) == sorted(r["unsat_parent_indices"] + r["unknown_parent_indices"] + r["sat_parent_indices"]), "BC2-36 target partition is not exact")
    req(cp["credit"]["known_parent_unsat_count_lower_bound"] == 7295 and cp["credit"]["new_exact_parent_unsat_count"] == 11, "BC2-36 lower-bound drift")
    req(cp["credit"]["stage32_main_credit"] is False and cp["credit"]["full178_complete"] is False, "BC2-36 broad credit leak")
    req(cp["firewalls"]["timeout_unknown_relabelled_unsat"] is False and cp["firewalls"]["unknown_dropped"] is False, "BC2-36 UNKNOWN firewall leak")
    req(cp["audit_consumption"] == {"bc2_35_hostile_audit_status":"PASS","bc2_35_hostile_audit_exact_head":"8bea7a6be26e01db0deb138dbd8406f578447921","bc2_35_hostile_audit_review_id":5187359907}, "BC2-35 audit consumption drift")

    locks = cp["source_locks"]
    req(locks["bc2_32_producer_git_blob_sha"] == B32_BLOB and locks["bc2_19_replay_source_git_blob_sha"] == B19_BLOB and locks["bc2_18_enumerator_source_git_blob_sha"] == B18_BLOB, "BC2-36 transitive source lock drift")
    req(locks["target_unknown_parent_indices_sha256"] == TARGET_SHA, "BC2-36 source-lock target drift")
    req(git_blob(SOURCE) == SOURCE_BLOB and git_blob(PREFLIGHT) == PREFLIGHT_BLOB, "BC2-36 source/preflight blob drift")
    req(git_blob(B32) == B32_BLOB and git_blob(B19) == B19_BLOB and git_blob(B18) == B18_BLOB, "BC2-36 executable dependency identity drift")
    pf = json.loads(PREFLIGHT.read_text())
    q = dict(pf); got = q.pop("canonical_sha256_without_this_field", None)
    req(got == PREFLIGHT_CANON and hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest() == PREFLIGHT_CANON, "BC2-36 preflight canonical drift")

    req(git_blob(RUNKEY) == RUNKEY_BLOB, "BC2-36 consumed runkey blob drift")
    rk = json.loads(RUNKEY.read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_36_FRESH_UNKNOWN52_REPLAY_RUNKEY_V1" and rk["generation"] == 1 and rk["armed"] is False, "BC2-36 runkey not consumed/disarmed")
    cr = rk["consumed_run"]
    req(cr["accepted_for_hostile_audit"] is True, "BC2-36 run not accepted for hostile audit")
    req(cr["exact_head"] == "63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5" and cr["workflow_run_id"] == 34718999232, "BC2-36 execution provenance drift")
    req(cr["authorize_job_id"] == 103621253008 and cr["compute_job_id"] == 103621306508, "BC2-36 job provenance drift")
    req(cr["artifact_id"] == 10306816385 and cr["artifact_zip_sha256"] == "35de2891058d97483fd7b3c9c95ca5c1041d9d96096287b1b01652a944f63ccb", "BC2-36 artifact receipt drift")
    req(cr["raw_json_sha256"] == "a70320e767ffe87d0751a7df195fd54387201e170e8f7daad43d41257af61f92", "BC2-36 raw JSON receipt drift")
    req(cr["checkpoint_git_blob_sha"] == CP_BLOB and cr["checkpoint_canonical"] == CP_CANON, "BC2-36 checkpoint receipt drift")
    req((cr["new_unsat_count"], cr["remaining_unknown_count"], cr["sat_count"], cr["known_parent_unsat_count_lower_bound"]) == (11, 41, 0, 7295), "BC2-36 consumed counts drift")
    req(cr["remaining_unknown_parent_indices_sha256"] == UNKNOWN_SHA and cr["status_stream_sha256"] == STATUS_SHA, "BC2-36 consumed result hashes drift")

    state = json.loads(STATE.read_text())
    req(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V26_BC2_36_TARGETED_REPLAY_AUDIT_BOUNDARY", "BC2-36 live state schema drift")
    cur = state["current"]
    req(cur["status"] == "BC2_36_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED" and cur["next_route"] == "HOSTILE_AUDIT_BC2_36_TARGETED_REPLAY", "BC2-36 audit route drift")
    f = state["frontier"]
    req(f["e8_bc2_36_executed"] is True and f["e8_bc2_36_audited"] is False and f["e8_known_parent_unsat_count_lower_bound"] == 7284 and f["e8_bc2_36_candidate_known_parent_unsat_count_lower_bound"] == 7295, "BC2-36 candidate/audited frontier drift")
    a = state["intermediate_audit_boundary"]
    req(a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True and a["bc2_36_execution_authorized"] is False, "BC2-36 audit freeze drift")
    req(state["next_step"]["bc2_37_blocked_until_bc2_36_hostile_audit_pass"] is True, "BC2-37 released before BC2-36 audit")

    wf = WORKFLOW.read_text()
    req("verify_bc2_36_targeted_replay_checkpoint.py" in wf, "BC2-36 verifier not wired into EX5 CI")
    req("authorize-bc2-36-fresh-unknown52:" not in wf and "\n  bc2-36-fresh-unknown52:" not in wf, "consumed BC2-36 heavy path still executable")

    print("PASS: Stage32EX5 BC2-36 retained checkpoint/artifact receipt is fail-closed")
    print("bc2_36=11_NEW_UNSAT_41_RETAINED_UNKNOWN_0_SAT; candidate_known_parent_unsat_lower_bound=7295")
    print("execution_head=63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5; workflow=34718999232; artifact=10306816385")
    print("next=HOSTILE_AUDIT_BC2_36_TARGETED_REPLAY; BC2_37_BLOCKED")


if __name__ == "__main__":
    main()
