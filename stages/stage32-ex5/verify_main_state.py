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
BC2_32_AUDIT_HEAD = "5c68ed03d77d6443c54340c90d457e80441fe414"
BC2_32_AUDIT_REVIEW = 5185434136
BC2_32_CP_CANON = "905b416477b23199c794a1267e143158e0dac7baaaa9f809d9cd8528e8e4aa6c"
BC2_32_CP_BLOB = "d21a3ddd3c2e06dd5523777aa3141ff41392a467"
BC2_32_UNKNOWN_SHA = "e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492"
BC2_33_SOURCE_BLOB = "efc44c368b408bf8b50c5ad9aa86cd646fb7b19c"
BC2_33_PREFLIGHT_BLOB = "b0a012ac62a98c5b5bbf3d8b7c8d120f8f37128a"
BC2_33_PREFLIGHT_CANON = "8e9925ba869e4d3d2b98220472a5fbba6985acac9d2067bc48402d3b4cb4a58e"
BC2_33_CP_CANON = "3310103df67d47d89ac121504a668158e0946070a7b15da07bbb0af7105fa73c"
BC2_33_CP_BLOB = "465dcb5c535c6cbbedc25ef2afe26915291ce38b"
BC2_33_UNKNOWN_SHA = "be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071"
BC2_33_STATUS_SHA = "e921c64caea0da8c75e2e47ade3c4b3d2105fc1583c97548cec7142e931473c5"
BC2_33_RUN = 34681698147
BC2_33_AUTH_JOB = 103521379130
BC2_33_JOB = 103521422359
BC2_33_ARTIFACT = 10294224700
BC2_33_ARTIFACT_ZIP_SHA = "2f60580c25eb6564a3daa3cd314cc0b0bf66eccc53f1da9dc32989f43da4052c"
BC2_33_RAW_JSON_SHA = "924a6b44cdba3152631a2a4ed24c9c37e6a5b23ee160d116903d25f3b7f74346"
BC2_33_EXECUTION_HEAD = "109aa38ff7e7d18e80697970489976acfd489503"
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
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V20_BC2_33_TARGETED_REPLAY_AUDIT_BOUNDARY", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == "c31684fb5f63d8a025eb298c91861d4c979b0e28", "current MAIN observation drift")
    req(b["active_work_pr"] == 1776 and b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "FULL178 claim drift")

    p32 = s["prior_audited_authority"]["bc2_32_pr_1776"]
    req(p32["hostile_audit_status"] == "PASS", "BC2-32 PASS not retained")
    req(p32["audit_checkpoint_exact_head"] == BC2_32_AUDIT_HEAD and p32["hostile_audit_review_id"] == BC2_32_AUDIT_REVIEW, "BC2-32 audit receipt drift")

    cp32p = B2 / "bc2-32-fresh-unknown170-replay-checkpoint.json"
    req(git_blob(cp32p) == BC2_32_CP_BLOB, "BC2-32 checkpoint blob drift")
    cp32 = checked(cp32p, BC2_32_CP_CANON)
    r32 = cp32["replay"]
    req((r32["parents_checked"], r32["unsat_count"], r32["unknown_count"], r32["sat_count"]) == (170, 63, 107, 0), "BC2-32 partition drift")
    req(r32["unknown_parent_indices_sha256"] == BC2_32_UNKNOWN_SHA, "BC2-32 UNKNOWN hash drift")

    src33 = B2 / "bc2_33_replay_explicit_fresh_unknown107.py"
    pf33p = B2 / "bc2-33-fresh-unknown107-replay-preflight.json"
    cp33p = B2 / "bc2-33-fresh-unknown107-replay-checkpoint.json"
    req(git_blob(src33) == BC2_33_SOURCE_BLOB, "BC2-33 producer blob drift")
    req(git_blob(pf33p) == BC2_33_PREFLIGHT_BLOB, "BC2-33 preflight blob drift")
    checked(pf33p, BC2_33_PREFLIGHT_CANON)
    req(git_blob(cp33p) == BC2_33_CP_BLOB, "BC2-33 checkpoint blob drift")
    cp33 = checked(cp33p, BC2_33_CP_CANON)
    r33 = cp33["replay"]
    req((r33["parents_checked"], r33["unsat_count"], r33["unknown_count"], r33["sat_count"]) == (107, 26, 81, 0), "BC2-33 partition drift")
    req(r33["per_parent_timeout_ms"] == 40000, "BC2-33 timeout drift")
    req(r33["unknown_parent_indices_sha256"] == BC2_33_UNKNOWN_SHA and len(r33["unknown_parent_indices"]) == 81, "BC2-33 UNKNOWN identity drift")
    req(r33["status_stream_sha256"] == BC2_33_STATUS_SHA, "BC2-33 status stream drift")
    req(r33["all_remaining_unknown_identities_explicitly_retained"] is True, "BC2-33 UNKNOWN retention drift")
    req(cp33["credit"]["known_parent_unsat_count_lower_bound"] == 7255, "BC2-33 lower-bound drift")
    req(cp33["credit"]["whole_first_block_picard64_unsat_candidate"] is False, "BC2-33 closure overclaim")
    req(cp33["sat_witnesses"] == [], "unexpected BC2-33 SAT witness")

    rk = json.loads((HERE / "runkeys/bc2-33-fresh-unknown107-replay.json").read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_33_FRESH_UNKNOWN107_REPLAY_RUNKEY_V1", "BC2-33 runkey schema drift")
    req(rk["generation"] == 2 and rk["armed"] is False, "BC2-33 runkey not consumed/disarmed")
    cancelled = rk.get("cancelled_run") or {}
    req(cancelled.get("generation") == 1 and cancelled.get("workflow_run_id") == 34681403712 and cancelled.get("compute_job_id") == 103520625439, "cancelled generation-1 receipt drift")
    req(cancelled.get("accepted_for_mathematical_credit") is False, "cancelled generation-1 credit leak")
    rc = rk.get("consumed_run") or {}
    req((rc.get("workflow_run_id"), rc.get("authorize_job_id"), rc.get("compute_job_id"), rc.get("artifact_id")) == (BC2_33_RUN, BC2_33_AUTH_JOB, BC2_33_JOB, BC2_33_ARTIFACT), "BC2-33 execution receipt drift")
    req(rc.get("exact_head") == BC2_33_EXECUTION_HEAD and rc.get("generation") == 2, "BC2-33 execution head drift")
    req(rc.get("artifact_zip_sha256") == BC2_33_ARTIFACT_ZIP_SHA and rc.get("raw_json_sha256") == BC2_33_RAW_JSON_SHA, "BC2-33 artifact hash drift")
    req(rc.get("checkpoint_canonical") == BC2_33_CP_CANON and rc.get("checkpoint_git_blob_sha") == BC2_33_CP_BLOB, "BC2-33 checkpoint receipt drift")
    req(rc.get("new_unsat_count") == 26 and rc.get("remaining_unknown_count") == 81 and rc.get("sat_count") == 0, "BC2-33 result receipt drift")
    req(rc.get("remaining_unknown_parent_indices_sha256") == BC2_33_UNKNOWN_SHA and rc.get("status_stream_sha256") == BC2_33_STATUS_SHA, "BC2-33 retained hashes drift")
    req(rc.get("known_parent_unsat_count_lower_bound") == 7255 and rc.get("accepted_for_hostile_audit") is True, "BC2-33 audit candidate receipt drift")

    cur = s["current"]
    req(cur["status"] == "BC2_33_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "current status drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_33_TARGETED_REPLAY", "audit route drift")
    req("NO_BC2_34_BEFORE_BC2_33_HOSTILE_AUDIT_PASS" in cur["stop_semantics"], "BC2-34 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_32_audited"] is True and f["e8_bc2_33_executed"] is True, "BC2-33 frontier receipt drift")
    req((f["e8_bc2_33_new_parent_unsat_count"], f["e8_bc2_33_remaining_unknown_count"], f["e8_bc2_33_sat_count"]) == (26, 81, 0), "BC2-33 frontier partition drift")
    req(f["e8_bc2_33_remaining_unknown_parent_indices_sha256"] == BC2_33_UNKNOWN_SHA, "BC2-33 frontier UNKNOWN hash drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7255, "BC2-33 frontier lower-bound drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_32_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_32_AUDIT_REVIEW, "predecessor audit receipt drift")
    req(a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True, "BC2-33 audit freeze drift")
    req(a["bc2_33_execution_authorized"] is False, "BC2-33 execution left authorized")

    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_33_TARGETED_REPLAY", "next-step drift")
    req(ns["bc2_33_execution_authorized"] is False and ns["bc2_34_blocked_until_bc2_33_hostile_audit_pass"] is True, "BC2-34 gate drift")
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
    req("authorize-bc2-33-fresh-unknown107:" not in wf and "bc2-33-fresh-unknown107:" not in wf, "consumed BC2-33 heavy path still active")
    req("authorize-bc2-32-fresh-unknown170:" not in wf and "bc2-32-fresh-unknown170:" not in wf, "retired BC2-32 heavy path still active")
    req("authorize-e8-cut-handoff-wave:" in wf, "current e8 handoff lifecycle unexpectedly removed")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-33 generation-2 targeted replay retained and frozen for hostile audit")
    print("bc2_33=26_UNSAT_81_UNKNOWN_0_SAT; known_parent_unsat_lower_bound=7255")
    print("generation1=CANCELLED_NONCREDIT; generation2=CONSUMED_DISARMED; heavy_path=RETIRED")
    print("Stage32_MAIN_credit=NO; FULL178=NO; merge=NO; next=stage32ex5-audit")


if __name__ == "__main__":
    main()
