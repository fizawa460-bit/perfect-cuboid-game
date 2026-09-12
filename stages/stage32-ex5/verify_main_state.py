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
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V18_BC2_32_TARGETED_REPLAY_AUDIT_BOUNDARY", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == "c31684fb5f63d8a025eb298c91861d4c979b0e28", "current MAIN observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "FULL178 claim drift")

    p31 = s["prior_audited_authority"]["bc2_31_pr_1776"]
    req(p31["hostile_audit_status"] == "PASS", "BC2-31 PASS not consumed")
    req(p31["audit_checkpoint_exact_head"] == BC2_31_AUDIT_HEAD and p31["hostile_audit_review_id"] == BC2_31_AUDIT_REVIEW, "BC2-31 audit receipt drift")

    cp31_path = B2 / "bc2-31-fresh-all7336-replay-checkpoint.json"
    cp31 = checked(cp31_path, BC2_31_CP_CANON)
    req(git_blob(cp31_path) == BC2_31_CP_BLOB, "BC2-31 checkpoint blob drift")
    fr = cp31["fresh_replay"]
    req((fr["parents_checked"], fr["unsat_count"], fr["unknown_count"]) == (7336, 7166, 170), "BC2-31 counts drift")
    req(fr["unknown_parent_indices_all_sha256"] == BC2_31_UNKNOWN_SHA and len(fr["unknown_parent_indices_all"]) == 170, "BC2-31 UNKNOWN identity drift")

    src = B2 / "bc2_32_replay_explicit_fresh_unknown170.py"
    pf_path = B2 / "bc2-32-fresh-unknown170-replay-preflight.json"
    cp32_path = B2 / "bc2-32-fresh-unknown170-replay-checkpoint.json"
    req(git_blob(src) == BC2_32_SOURCE_BLOB, "BC2-32 source blob drift")
    req(git_blob(pf_path) == BC2_32_PREFLIGHT_BLOB, "BC2-32 preflight blob drift")
    pf = checked(pf_path, BC2_32_PREFLIGHT_CANON)
    req(pf["target"]["audited_fresh_unknown_parent_count"] == 170 and pf["target"]["audited_fresh_unknown_parent_indices_sha256"] == BC2_31_UNKNOWN_SHA, "preflight target drift")
    req(git_blob(cp32_path) == BC2_32_CP_BLOB, "BC2-32 checkpoint blob drift")
    cp32 = checked(cp32_path, BC2_32_CP_CANON)
    req(cp32["status"] == "PASS_TARGETED_REPLAY_REDUCED_OR_RETAINED_UNKNOWN_SET", "BC2-32 status drift")
    r = cp32["replay"]
    req((r["parents_checked"], r["unsat_count"], r["unknown_count"], r["sat_count"]) == (170, 63, 107, 0), "BC2-32 partition drift")
    req(r["unknown_parent_indices_sha256"] == BC2_32_UNKNOWN_SHA and len(r["unknown_parent_indices"]) == 107, "BC2-32 UNKNOWN identity drift")
    req(r["status_stream_sha256"] == BC2_32_STATUS_SHA and r["all_remaining_unknown_identities_explicitly_retained"] is True, "BC2-32 status stream drift")
    req(cp32["credit"]["new_exact_parent_unsat_count"] == 63 and cp32["credit"]["known_parent_unsat_count_lower_bound"] == 7229, "BC2-32 lower-bound drift")
    req(cp32["credit"]["whole_first_block_picard64_unsat_candidate"] is False, "BC2-32 overclaim")
    req(cp32["sat_witnesses"] == [], "unexpected BC2-32 SAT witness")

    rk = json.loads((HERE / "runkeys/bc2-32-fresh-unknown170-replay.json").read_text())
    req(rk["generation"] == 1 and rk["armed"] is False, "BC2-32 runkey not consumed/disarmed")
    rc = rk.get("consumed_run") or {}
    req((rc.get("workflow_run_id"), rc.get("authorize_job_id"), rc.get("compute_job_id"), rc.get("artifact_id")) == (BC2_32_RUN, BC2_32_AUTH_JOB, BC2_32_JOB, BC2_32_ART), "BC2-32 workflow receipt drift")
    req(rc.get("result_canonical") == BC2_32_CP_CANON and rc.get("status_stream_sha256") == BC2_32_STATUS_SHA, "BC2-32 result lock drift")
    req(rc.get("remaining_unknown_parent_indices_sha256") == BC2_32_UNKNOWN_SHA and rc.get("known_parent_unsat_count_lower_bound") == 7229, "BC2-32 retained result drift")
    req(rc.get("accepted_for_hostile_audit") is True, "BC2-32 result not marked audit candidate")

    cur = s["current"]
    req(cur["status"] == "BC2_32_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "current status drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_32_TARGETED_REPLAY", "current route drift")
    req("NO_BC2_33" in cur["stop_semantics"] and "NO_MAIN_PROMOTION" in cur["stop_semantics"], "stop firewall drift")
    f = s["frontier"]
    req(f["e8_bc2_31_audited"] is True and f["e8_bc2_32_executed"] is True, "frontier execution receipt drift")
    req((f["e8_bc2_32_new_parent_unsat_count"], f["e8_bc2_32_remaining_unknown_count"], f["e8_bc2_32_sat_count"]) == (63, 107, 0), "frontier partition drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7229 and f["e8_bc2_32_remaining_unknown_parent_indices_sha256"] == BC2_32_UNKNOWN_SHA, "frontier lower-bound/identity drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_31_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_31_AUDIT_REVIEW, "predecessor audit receipt drift")
    req(a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True, "BC2-32 audit freeze drift")
    req(a["bc2_32_execution_authorized"] is False, "BC2-32 execution left authorized")
    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_32_TARGETED_REPLAY" and ns["bc2_33_blocked_until_bc2_32_hostile_audit_pass"] is True, "next-step drift")
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
    for token in ("authorize-bc2-32-fresh-unknown170:", "bc2-32-fresh-unknown170:", "bc2-32-fresh-unknown170-replay.json", BC2_32_SOURCE_BLOB):
        req(token in wf, f"main workflow missing BC2-32 token: {token}")
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

    print("PASS: Stage32EX5 BC2-32 targeted replay retained and frozen for hostile audit")
    print("bc2_32=63_UNSAT_107_UNKNOWN_0_SAT; known_parent_unsat_lower_bound=7229")
    print("remaining 107 UNKNOWN identities explicit; whole_first_block_unsat=NO; Stage32_MAIN_credit=NO; merge=NO")
    print("next=stage32ex5-audit")


if __name__ == "__main__":
    main()
