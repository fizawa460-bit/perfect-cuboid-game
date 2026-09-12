#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHECKPOINT = HERE / "bc2-35-fresh-unknown64-replay-checkpoint.json"
RUNKEY = ROOT / "runkeys" / "bc2-35-fresh-unknown64-replay.json"
SOURCE = HERE / "bc2_35_replay_explicit_fresh_unknown64.py"
PREFLIGHT = HERE / "bc2-35-fresh-unknown64-replay-preflight.json"
B32 = HERE / "bc2_32_replay_explicit_fresh_unknown170.py"
B19 = HERE / "bc2_19_n354_survivor_normal_positivity_mass_replay.py"
B18 = HERE / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py"

CP_BLOB = "ee95590c637735478c06af413835ea390000b445"
CP_CANON = "14f808df5db80842b87efbbc0dafb9c68ad9cc5e3529b2647cfa66ee9faccf2f"
RUNKEY_BLOB = "5707320cc227531292f1a868d6da20554d9fd095"
SOURCE_BLOB = "40111bb7619113d1c9c766089026bcf59d6bdb01"
PREFLIGHT_BLOB = "bf2f4b1125925a27c820dfdc49ad796e69b268b4"
PREFLIGHT_CANON = "e74e6c15050187d06c472c2eff6156c66837f8f9c9de3d2cfca7629b431dadb4"
B32_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
B18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
TARGET_SHA = "00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b"
UNKNOWN_SHA = "95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818"
STATUS_SHA = "be9c37bcda88c72916791c54238378a7d82f8738409a415a8cf39e49a9bfaaae"


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
    req(git_blob(CHECKPOINT) == CP_BLOB, "BC2-35 checkpoint blob drift")
    cp = json.loads(CHECKPOINT.read_text())
    req(cp["schema"] == "STAGE32EX5_BC2_35_FRESH_UNKNOWN64_REPLAY_V1", "BC2-35 checkpoint schema drift")
    req(cp["canonical_sha256_without_this_field"] == CP_CANON and canonical(cp) == CP_CANON, "BC2-35 checkpoint canonical drift")
    r = cp["replay"]
    req((r["parents_checked"], r["unsat_count"], r["unknown_count"], r["sat_count"]) == (64, 12, 52, 0), "BC2-35 partition drift")
    req(r["per_parent_timeout_ms"] == 80000, "BC2-35 timeout drift")
    req(r["unknown_parent_indices_sha256"] == UNKNOWN_SHA and len(r["unknown_parent_indices"]) == 52, "BC2-35 UNKNOWN identity drift")
    req(r["status_stream_sha256"] == STATUS_SHA, "BC2-35 status stream drift")
    req(len(r["unsat_parent_indices"]) == 12 and set(r["unsat_parent_indices"]).isdisjoint(r["unknown_parent_indices"]), "BC2-35 retained partition overlap")
    target = cp["target"]
    req(target["audited_bc2_34_unknown_count"] == 64 and target["parent_indices_sha256"] == TARGET_SHA and target["prior_audited_unsat_count"] == 7272, "BC2-35 target drift")
    req(sorted(target["parent_indices"]) == sorted(r["unsat_parent_indices"] + r["unknown_parent_indices"] + r["sat_parent_indices"]), "BC2-35 target partition is not exact")
    req(cp["credit"]["known_parent_unsat_count_lower_bound"] == 7284 and cp["credit"]["new_exact_parent_unsat_count"] == 12, "BC2-35 lower-bound drift")
    req(cp["credit"]["stage32_main_credit"] is False and cp["credit"]["full178_complete"] is False, "BC2-35 broad credit leak")
    req(cp["firewalls"]["timeout_unknown_relabelled_unsat"] is False and cp["firewalls"]["unknown_dropped"] is False, "BC2-35 UNKNOWN firewall leak")
    req(cp["audit_consumption"] == {"bc2_34_hostile_audit_status":"PASS","bc2_34_hostile_audit_exact_head":"cdb455860849cfd064e3ab8c83d6d4993fb5ff1b","bc2_34_hostile_audit_review_id":5186516652}, "BC2-34 audit consumption drift")

    locks = cp["source_locks"]
    req(locks["bc2_32_producer_git_blob_sha"] == B32_BLOB and locks["bc2_19_replay_source_git_blob_sha"] == B19_BLOB and locks["bc2_18_enumerator_source_git_blob_sha"] == B18_BLOB, "BC2-35 transitive source lock drift")
    req(locks["target_unknown_parent_indices_sha256"] == TARGET_SHA, "BC2-35 source-lock target drift")
    req(git_blob(SOURCE) == SOURCE_BLOB and git_blob(PREFLIGHT) == PREFLIGHT_BLOB, "BC2-35 source/preflight blob drift")
    req(git_blob(B32) == B32_BLOB and git_blob(B19) == B19_BLOB and git_blob(B18) == B18_BLOB, "BC2-35 executable dependency identity drift")
    pf = json.loads(PREFLIGHT.read_text())
    q = dict(pf); got = q.pop("canonical_sha256_without_this_field", None)
    req(got == PREFLIGHT_CANON and hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest() == PREFLIGHT_CANON, "BC2-35 preflight canonical drift")

    req(git_blob(RUNKEY) == RUNKEY_BLOB, "BC2-35 consumed runkey blob drift")
    rk = json.loads(RUNKEY.read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_35_FRESH_UNKNOWN64_REPLAY_RUNKEY_V1" and rk["generation"] == 1 and rk["armed"] is False, "BC2-35 runkey not consumed/disarmed")
    cr = rk["consumed_run"]
    req(cr["accepted_for_hostile_audit"] is True, "BC2-35 run not accepted for hostile audit")
    req(cr["exact_head"] == "c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8" and cr["workflow_run_id"] == 34696592793, "BC2-35 execution provenance drift")
    req(cr["authorize_job_id"] == 103561025783 and cr["compute_job_id"] == 103561129955, "BC2-35 job provenance drift")
    req(cr["artifact_id"] == 10299388802 and cr["artifact_zip_sha256"] == "7e3b5a48300af52f19a329ed8f87e2048702b3587825b8893c2d5475aab150c3", "BC2-35 artifact receipt drift")
    req(cr["raw_json_sha256"] == "da3f19d1e7e8f72052d9046f3e1482e669a50eeada228a3b113d440081bc266c", "BC2-35 raw JSON receipt drift")
    req(cr["checkpoint_git_blob_sha"] == CP_BLOB and cr["checkpoint_canonical"] == CP_CANON, "BC2-35 checkpoint receipt drift")
    req((cr["new_unsat_count"], cr["remaining_unknown_count"], cr["sat_count"], cr["known_parent_unsat_count_lower_bound"]) == (12, 52, 0, 7284), "BC2-35 consumed counts drift")
    req(cr["remaining_unknown_parent_indices_sha256"] == UNKNOWN_SHA and cr["status_stream_sha256"] == STATUS_SHA, "BC2-35 consumed result hashes drift")

    print("PASS: Stage32EX5 BC2-35 retained checkpoint/artifact receipt is fail-closed")
    print("bc2_35=12_NEW_UNSAT_52_RETAINED_UNKNOWN_0_SAT; known_parent_unsat_lower_bound=7284")
    print("execution_head=c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8; workflow=34696592793; artifact=10299388802")
    print("next=HOSTILE_AUDIT_BC2_35_TARGETED_REPLAY; BC2_36_BLOCKED")


if __name__ == "__main__":
    main()
