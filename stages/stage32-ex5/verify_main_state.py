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
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
BC2_31_AUDIT_HEAD = "72118efafdd25ca3b08d408463db46e2800e22df"
BC2_31_AUDIT_REVIEW = 5184996992
BC2_31_CP_CANON = "f2aec1d923ff43393d24364864be36e223d43674149e6655a920d3b3d5de3ae4"
BC2_31_CP_BLOB = "188601efcb99d33fe00fc60dc3c2f40f51e65b20"
BC2_31_UNKNOWN_SHA = "df7db2159df41d93ce64b7d2ccf230b9363711bbdf769280e1df0560cfbae1ae"
BC2_32_AUDIT_HEAD = "5c68ed03d77d6443c54340c90d457e80441fe414"
BC2_32_AUDIT_REVIEW = 5185434136
BC2_32_SOURCE_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
BC2_32_PREFLIGHT_BLOB = "45f2bb716266898a33ad49ea79ef1136907c8a09"
BC2_32_PREFLIGHT_CANON = "2fba662ed105bd3a2b8e8b0989483364b62a6feb6b04f5ce909c462d8ca93cb9"
BC2_32_CP_CANON = "905b416477b23199c794a1267e143158e0dac7baaaa9f809d9cd8528e8e4aa6c"
BC2_32_CP_BLOB = "d21a3ddd3c2e06dd5523777aa3141ff41392a467"
BC2_32_UNKNOWN_SHA = "e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492"
BC2_32_STATUS_SHA = "bdbd63978e0fdd34687661cf2b60e74553e7108e93fc7c773dd3e3406fdaf320"
BC2_32_RUN = 34672718019
BC2_32_AUTH_JOB = 103497019707
BC2_32_JOB = 103497078073
BC2_32_ART = 10292081214
BC2_33_SOURCE_BLOB = "efc44c368b408bf8b50c5ad9aa86cd646fb7b19c"
BC2_33_PREFLIGHT_BLOB = "b0a012ac62a98c5b5bbf3d8b7c8d120f8f37128a"
BC2_33_PREFLIGHT_CANON = "8e9925ba869e4d3d2b98220472a5fbba6985acac9d2067bc48402d3b4cb4a58e"
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
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V19_BC2_32_AUDIT_CONSUMED_BC2_33_EXECUTION", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == "c31684fb5f63d8a025eb298c91861d4c979b0e28", "current MAIN observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "FULL178 claim drift")

    p32 = s["prior_audited_authority"]["bc2_32_pr_1776"]
    req(p32["hostile_audit_status"] == "PASS", "BC2-32 PASS not consumed")
    req(p32["audit_checkpoint_exact_head"] == BC2_32_AUDIT_HEAD and p32["hostile_audit_review_id"] == BC2_32_AUDIT_REVIEW, "BC2-32 audit receipt drift")

    cp31_path = B2 / "bc2-31-fresh-all7336-replay-checkpoint.json"
    cp31 = checked(cp31_path, BC2_31_CP_CANON)
    req(git_blob(cp31_path) == BC2_31_CP_BLOB, "BC2-31 checkpoint blob drift")
    fr = cp31["fresh_replay"]
    req((fr["parents_checked"], fr["unsat_count"], fr["unknown_count"]) == (7336, 7166, 170), "BC2-31 counts drift")
    req(fr["unknown_parent_indices_all_sha256"] == BC2_31_UNKNOWN_SHA and len(fr["unknown_parent_indices_all"]) == 170, "BC2-31 UNKNOWN identity drift")

    src32 = B2 / "bc2_32_replay_explicit_fresh_unknown170.py"
    pf32_path = B2 / "bc2-32-fresh-unknown170-replay-preflight.json"
    cp32_path = B2 / "bc2-32-fresh-unknown170-replay-checkpoint.json"
    req(git_blob(src32) == BC2_32_SOURCE_BLOB, "BC2-32 source blob drift")
    req(git_blob(pf32_path) == BC2_32_PREFLIGHT_BLOB, "BC2-32 preflight blob drift")
    checked(pf32_path, BC2_32_PREFLIGHT_CANON)
    req(git_blob(cp32_path) == BC2_32_CP_BLOB, "BC2-32 checkpoint blob drift")
    cp32 = checked(cp32_path, BC2_32_CP_CANON)
    r = cp32["replay"]
    req((r["parents_checked"], r["unsat_count"], r["unknown_count"], r["sat_count"]) == (170, 63, 107, 0), "BC2-32 partition drift")
    req(r["unknown_parent_indices_sha256"] == BC2_32_UNKNOWN_SHA and len(r["unknown_parent_indices"]) == 107, "BC2-32 UNKNOWN identity drift")
    req(r["status_stream_sha256"] == BC2_32_STATUS_SHA and r["all_remaining_unknown_identities_explicitly_retained"] is True, "BC2-32 status stream drift")
    req(cp32["credit"]["known_parent_unsat_count_lower_bound"] == 7229 and cp32["sat_witnesses"] == [], "BC2-32 retained result drift")

    rk32 = json.loads((HERE / "runkeys/bc2-32-fresh-unknown170-replay.json").read_text())
    req(rk32["generation"] == 1 and rk32["armed"] is False, "BC2-32 runkey not consumed/disarmed")
    rc = rk32.get("consumed_run") or {}
    req((rc.get("workflow_run_id"), rc.get("authorize_job_id"), rc.get("compute_job_id"), rc.get("artifact_id")) == (BC2_32_RUN, BC2_32_AUTH_JOB, BC2_32_JOB, BC2_32_ART), "BC2-32 workflow receipt drift")
    req(rc.get("result_canonical") == BC2_32_CP_CANON and rc.get("status_stream_sha256") == BC2_32_STATUS_SHA, "BC2-32 result lock drift")
    req(rc.get("remaining_unknown_parent_indices_sha256") == BC2_32_UNKNOWN_SHA and rc.get("known_parent_unsat_count_lower_bound") == 7229, "BC2-32 retained result drift")
    req(rc.get("accepted_for_hostile_audit") is True, "BC2-32 result not marked audit candidate")

    src33 = B2 / "bc2_33_replay_explicit_fresh_unknown107.py"
    pf33_path = B2 / "bc2-33-fresh-unknown107-replay-preflight.json"
    req(git_blob(src33) == BC2_33_SOURCE_BLOB, "BC2-33 source blob drift")
    req(git_blob(pf33_path) == BC2_33_PREFLIGHT_BLOB, "BC2-33 preflight blob drift")
    pf33 = checked(pf33_path, BC2_33_PREFLIGHT_CANON)
    a33 = pf33["audit_consumption"]; t33 = pf33["target"]; ex33 = pf33["execution"]
    req(a33["bc2_32_hostile_audit_status"] == "PASS" and a33["bc2_32_hostile_audit_exact_head"] == BC2_32_AUDIT_HEAD and a33["bc2_32_hostile_audit_review_id"] == BC2_32_AUDIT_REVIEW, "BC2-33 predecessor audit drift")
    req(t33["fresh_unknown_parent_count"] == 107 and t33["fresh_unknown_parent_indices_sha256"] == BC2_32_UNKNOWN_SHA and t33["prior_audited_unsat_count"] == 7229, "BC2-33 target drift")
    req(ex33["per_parent_timeout_ms"] == 40000 and ex33["effective_heavy_concurrency"] == 1 and ex33["workflow_timeout_minutes"] == 90 and ex33["heavy_scaleout_authorized"] is False, "BC2-33 execution envelope drift")

    rk33 = json.loads((HERE / "runkeys/bc2-33-fresh-unknown107-replay.json").read_text())
    req(rk33["schema"] == "STAGE32EX5_BC2_33_FRESH_UNKNOWN107_REPLAY_RUNKEY_V1", "BC2-33 runkey schema drift")
    req(rk33["generation"] in (0, 1), "BC2-33 runkey generation drift")
    req(rk33["armed"] is (rk33["generation"] == 1), "BC2-33 runkey arm/generation mismatch")
    req(rk33.get("consumed_run") is None, "BC2-33 pre-execution runkey unexpectedly consumed")
    req(rk33["source_git_blob_sha"] == BC2_33_SOURCE_BLOB and rk33["preflight_git_blob_sha"] == BC2_33_PREFLIGHT_BLOB and rk33["preflight_canonical"] == BC2_33_PREFLIGHT_CANON, "BC2-33 runkey source/preflight drift")

    cur = s["current"]
    req(cur["status"] == "BC2_33_EXPLICIT_FRESH_UNKNOWN107_REPLAY_EXECUTION_AUTHORIZED", "current status drift")
    req(cur["next_route"] == "BC2_33_REFINE_REMAINING_FRESH_UNKNOWN_SET", "current route drift")
    req("NO_MAIN_PROMOTION" in cur["stop_semantics"] and "NO_BC2_34_BEFORE_BC2_33_HOSTILE_AUDIT" in cur["stop_semantics"], "stop firewall drift")
    f = s["frontier"]
    req(f["e8_bc2_32_audited"] is True and f["e8_bc2_33_executed"] is False, "frontier audit/execution drift")
    req(f["e8_bc2_33_target_unknown_count"] == 107 and f["e8_known_parent_unsat_count_lower_bound"] == 7229, "BC2-33 pre-execution frontier drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_32_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_32_AUDIT_REVIEW, "BC2-32 audit receipt drift")
    req(a["freeze_active"] is False and a["new_audit_boundary_exists"] is False and a["re_audit_required"] is False, "stale audit freeze")
    req(a["bc2_32_execution_authorized"] is False and a["bc2_33_execution_authorized"] is True, "BC2-33 execution authority drift")
    ns = s["next_step"]
    req(ns["id"] == "BC2_33_REFINE_REMAINING_FRESH_UNKNOWN_SET" and ns["bc2_33_execution_authorized"] is True and ns["bc2_34_blocked_until_bc2_33_hostile_audit_pass"] is True, "next-step drift")
    for k in ("heavy_scaleout_authorized", "main_promotion_authorized", "n350_registration_authorized", "merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    observed = {k for k in s["firewalls"] if "cuboid" in k or "curboid" in k}
    req(observed == PC_KEYS, "Perfect Cuboid firewall key set drift")
    for section in ("historical_credit_firewall", "firewalls"):
        for key, value in s[section].items():
            req(value is False, f"firewall leak: {section}.{key}")
    for key, value in s["credit"].items():
        if key != "level":
            req(value is False, f"credit leak: credit.{key}")

    wf = MAIN_WORKFLOW.read_text()
    for token in ("authorize-bc2-33-fresh-unknown107:", "bc2-33-fresh-unknown107:", "bc2-33-fresh-unknown107-replay.json", BC2_33_SOURCE_BLOB):
        req(token in wf, f"main workflow missing BC2-33 token: {token}")
    req("authorize-bc2-32-fresh-unknown170:" not in wf and "bc2-32-fresh-unknown170:" not in wf, "retired BC2-32 heavy path still present")
    req("authorize-bc2-31-recovery:" not in wf, "retired BC2-31 recovery auto job still present")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-32 hostile audit consumed; BC2-33 targeted replay narrowly authorized")
    print("target=107 audited UNKNOWN parents; timeout=40000ms; concurrency=1; heavy_scaleout=NO")
    print("known_parent_unsat_lower_bound=7229 pre-execution; Stage32_MAIN_credit=NO; merge=NO")
    print("next=arm BC2-33 generation1 only after exact-head integrity PASS")


if __name__ == "__main__":
    main()
