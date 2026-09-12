#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
ROOT = HERE.parents[0]
STAGE32_MAIN = ROOT / "stage32" / "MAIN-STATE.json"
MAIN_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-main.yml"

STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
BC2_33_AUDIT_HEAD = "241d65c51f93b66b79f7e8407891cc46359a45c9"
BC2_33_AUDIT_REVIEW = 5185961173
BC2_33_SOURCE_BLOB = "efc44c368b408bf8b50c5ad9aa86cd646fb7b19c"
BC2_33_CP_CANON = "3310103df67d47d89ac121504a668158e0946070a7b15da07bbb0af7105fa73c"
BC2_33_CP_BLOB = "465dcb5c535c6cbbedc25ef2afe26915291ce38b"
BC2_33_UNKNOWN_SHA = "be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071"
BC2_33_STATUS_SHA = "e921c64caea0da8c75e2e47ade3c4b3d2105fc1583c97548cec7142e931473c5"
BC2_34_SOURCE_BLOB = "eb715ed7cc5bb350b15e35868e2f79c548f17e28"
BC2_34_PREFLIGHT_BLOB = "efbadd91e1bfea694d70791aeb77ccb8d05dbe02"
BC2_34_PREFLIGHT_CANON = "a131b1c481631b721ef8acea42c02592be5ef04ed66c401dc72990e35ac98e8e"
PC_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    q = dict(obj)
    got = q.pop("canonical_sha256_without_this_field", None)
    req(got == expected and csha(q) == expected, f"canonical drift: {path.name}")
    return obj


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text())
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V21_BC2_33_AUDIT_CONSUMED_BC2_34_EXECUTION", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == "c31684fb5f63d8a025eb298c91861d4c979b0e28", "current MAIN observation drift")
    req(b["active_work_pr"] == 1776 and b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "FULL178 claim drift")

    p33 = s["prior_audited_authority"]["bc2_33_pr_1776"]
    req(p33["hostile_audit_status"] == "PASS", "BC2-33 PASS not consumed")
    req(p33["audit_checkpoint_exact_head"] == BC2_33_AUDIT_HEAD and p33["hostile_audit_review_id"] == BC2_33_AUDIT_REVIEW, "BC2-33 audit receipt drift")

    src33 = B2 / "bc2_33_replay_explicit_fresh_unknown107.py"
    cp33p = B2 / "bc2-33-fresh-unknown107-replay-checkpoint.json"
    req(git_blob(src33) == BC2_33_SOURCE_BLOB, "BC2-33 producer blob drift")
    req(git_blob(cp33p) == BC2_33_CP_BLOB, "BC2-33 checkpoint blob drift")
    cp33 = checked(cp33p, BC2_33_CP_CANON)
    r33 = cp33["replay"]
    req((r33["parents_checked"], r33["unsat_count"], r33["unknown_count"], r33["sat_count"]) == (107, 26, 81, 0), "BC2-33 partition drift")
    req(r33["unknown_parent_indices_sha256"] == BC2_33_UNKNOWN_SHA and len(r33["unknown_parent_indices"]) == 81, "BC2-33 UNKNOWN identity drift")
    req(r33["status_stream_sha256"] == BC2_33_STATUS_SHA, "BC2-33 status stream drift")
    req(cp33["credit"]["known_parent_unsat_count_lower_bound"] == 7255, "BC2-33 lower-bound drift")

    rk33 = json.loads((HERE / "runkeys/bc2-33-fresh-unknown107-replay.json").read_text())
    req(rk33["generation"] == 2 and rk33["armed"] is False, "BC2-33 runkey not consumed/disarmed")
    rc33 = rk33.get("consumed_run") or {}
    req((rc33.get("workflow_run_id"), rc33.get("authorize_job_id"), rc33.get("compute_job_id"), rc33.get("artifact_id")) == (34681698147, 103521379130, 103521422359, 10294224700), "BC2-33 execution receipt drift")
    req(rc33.get("checkpoint_canonical") == BC2_33_CP_CANON and rc33.get("checkpoint_git_blob_sha") == BC2_33_CP_BLOB, "BC2-33 checkpoint receipt drift")
    req(rc33.get("known_parent_unsat_count_lower_bound") == 7255 and rc33.get("accepted_for_hostile_audit") is True, "BC2-33 audit-candidate receipt drift")

    src34 = B2 / "bc2_34_replay_explicit_fresh_unknown81.py"
    pf34p = B2 / "bc2-34-fresh-unknown81-replay-preflight.json"
    req(git_blob(src34) == BC2_34_SOURCE_BLOB, "BC2-34 source blob drift")
    req(git_blob(pf34p) == BC2_34_PREFLIGHT_BLOB, "BC2-34 preflight blob drift")
    pf34 = checked(pf34p, BC2_34_PREFLIGHT_CANON)
    a34 = pf34["audit_consumption"]
    t34 = pf34["target"]
    ex34 = pf34["execution"]
    req(a34["bc2_33_hostile_audit_status"] == "PASS" and a34["bc2_33_hostile_audit_exact_head"] == BC2_33_AUDIT_HEAD and a34["bc2_33_hostile_audit_review_id"] == BC2_33_AUDIT_REVIEW, "BC2-34 predecessor audit drift")
    req(t34["fresh_unknown_parent_count"] == 81 and t34["fresh_unknown_parent_indices_sha256"] == BC2_33_UNKNOWN_SHA and t34["prior_audited_unsat_count"] == 7255 and t34["targeted_replay_only"] is True, "BC2-34 target drift")
    req(ex34["per_parent_timeout_ms"] == 60000 and ex34["effective_heavy_concurrency"] == 1 and ex34["workflow_timeout_minutes"] == 90 and ex34["heavy_scaleout_authorized"] is False, "BC2-34 execution envelope drift")

    rk34 = json.loads((HERE / "runkeys/bc2-34-fresh-unknown81-replay.json").read_text())
    req(rk34["schema"] == "STAGE32EX5_BC2_34_FRESH_UNKNOWN81_REPLAY_RUNKEY_V1", "BC2-34 runkey schema drift")
    req(rk34["generation"] in (0, 1), "BC2-34 runkey generation drift")
    req(rk34["armed"] is (rk34["generation"] == 1), "BC2-34 runkey arm/generation mismatch")
    req(rk34.get("consumed_run") is None, "BC2-34 pre-execution runkey unexpectedly consumed")
    req(rk34["source_git_blob_sha"] == BC2_34_SOURCE_BLOB and rk34["preflight_git_blob_sha"] == BC2_34_PREFLIGHT_BLOB and rk34["preflight_canonical"] == BC2_34_PREFLIGHT_CANON, "BC2-34 runkey source/preflight drift")

    cur = s["current"]
    req(cur["status"] == "BC2_34_EXPLICIT_FRESH_UNKNOWN81_REPLAY_EXECUTION_AUTHORIZED", "current status drift")
    req(cur["next_route"] == "BC2_34_REFINE_REMAINING_FRESH_UNKNOWN_SET", "current route drift")
    req("NO_BC2_35_BEFORE_BC2_34_HOSTILE_AUDIT" in cur["stop_semantics"], "BC2-35 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_33_audited"] is True and f["e8_bc2_34_executed"] is False, "frontier audit/execution drift")
    req(f["e8_bc2_34_target_unknown_count"] == 81 and f["e8_known_parent_unsat_count_lower_bound"] == 7255, "BC2-34 pre-execution frontier drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_33_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_33_AUDIT_REVIEW, "BC2-33 audit receipt drift")
    req(a["freeze_active"] is False and a["new_audit_boundary_exists"] is False and a["re_audit_required"] is False, "stale audit freeze")
    req(a["bc2_33_execution_authorized"] is False and a["bc2_34_execution_authorized"] is True, "BC2-34 execution authority drift")

    ns = s["next_step"]
    req(ns["id"] == "BC2_34_REFINE_REMAINING_FRESH_UNKNOWN_SET" and ns["bc2_34_execution_authorized"] is True and ns["bc2_35_blocked_until_bc2_34_hostile_audit_pass"] is True, "next-step drift")
    for k in ("heavy_scaleout_authorized", "main_promotion_authorized", "n350_registration_authorized", "merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    req({k for k in s["firewalls"] if "cuboid" in k or "curboid" in k} == PC_KEYS, "Perfect Cuboid firewall key drift")
    for section in ("historical_credit_firewall", "firewalls"):
        for key, value in s[section].items():
            req(value is False, f"firewall leak: {section}.{key}")
    for key, value in s["credit"].items():
        if key != "level":
            req(value is False, f"credit leak: credit.{key}")

    wf = MAIN_WORKFLOW.read_text()
    for token in ("authorize-bc2-34-fresh-unknown81:", "bc2-34-fresh-unknown81:", "bc2-34-fresh-unknown81-replay.json", BC2_34_SOURCE_BLOB):
        req(token in wf, f"main workflow missing BC2-34 token: {token}")
    req("authorize-bc2-33-fresh-unknown107:" not in wf and "bc2-33-fresh-unknown107:" not in wf, "retired BC2-33 heavy path still active")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: BC2-33 hostile audit consumed; BC2-34 targeted replay narrowly authorized")
    print("target=81 audited UNKNOWN parents; timeout=60000ms; concurrency=1; heavy_scaleout=NO")
    print("known_parent_unsat_lower_bound=7255 pre-execution; Stage32_MAIN_credit=NO; merge=NO")
    print("next=arm BC2-34 generation1 only after exact-head integrity PASS")


if __name__ == "__main__":
    main()
