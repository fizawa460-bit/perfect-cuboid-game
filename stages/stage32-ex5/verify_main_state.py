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
CROSS_LANE = ROOT / "stage32" / "proof" / "CROSS-LANE-DEMANDS.json"
MAIN_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-main.yml"

CURRENT_MAIN = "e4d3b8b83626526ffeccdbd9c956081735fe1a6e"
STAGE32_MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
CROSS_LANE_BLOB = "bbf4fc2460bad22c65359bc17aa89f8717e259a2"
BC2_33_AUDIT_HEAD = "241d65c51f93b66b79f7e8407891cc46359a45c9"
BC2_33_AUDIT_REVIEW = 5185961173
BC2_33_SOURCE_BLOB = "efc44c368b408bf8b50c5ad9aa86cd646fb7b19c"
BC2_33_CP_CANON = "3310103df67d47d89ac121504a668158e0946070a7b15da07bbb0af7105fa73c"
BC2_33_CP_BLOB = "465dcb5c535c6cbbedc25ef2afe26915291ce38b"
BC2_33_UNKNOWN_SHA = "be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071"
BC2_34_SOURCE_BLOB = "eb715ed7cc5bb350b15e35868e2f79c548f17e28"
BC2_34_PREFLIGHT_BLOB = "efbadd91e1bfea694d70791aeb77ccb8d05dbe02"
BC2_34_PREFLIGHT_CANON = "a131b1c481631b721ef8acea42c02592be5ef04ed66c401dc72990e35ac98e8e"
BC2_34_CP_BLOB = "e566aeda2931642d79c88dc5eeb84b142f655609"
BC2_34_CP_CANON = "e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba"
BC2_34_UNKNOWN_SHA = "00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b"
BC2_34_STATUS_SHA = "3dfc34636f7a44093e0c93034bf74442fd5cadcdf197b28f8bf674ca7bfe19c2"
BC2_34_EXECUTION_HEAD = "79167ffcdd0be4cf3bdcb7e652fad38acb447fb4"
BC2_34_RUN = 34685719102
BC2_34_AUTH_JOB = 103532247242
BC2_34_JOB = 103532291007
BC2_34_ARTIFACT = 10296591024
BC2_34_ARTIFACT_ZIP_SHA = "1aff75ecda329d8770c7cd6c120eb0aeb8630521ed68dd93427079f8eee09792"
BC2_34_RAW_JSON_SHA = "d2b8963c21fbb3d8cf5c739169c41bdc6a0ac4036540d6cf8e6e807159033a63"
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
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V22_BC2_34_TARGETED_REPLAY_AUDIT_BOUNDARY", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == CURRENT_MAIN, "current MAIN observation drift")
    req(b["active_work_pr"] == 1776 and b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    # Current MAIN V15 authority projection.
    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED", "Stage32 MAIN schema drift")
    mt = ma["current_target"]
    mf = ma["current_exact_frontier"]
    req(mt["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN", "MAIN control-mode drift")
    req(mt["primary_incomplete_id"] == "32-01" and mt["primary_incomplete_name"] == "FULL178", "MAIN primary target drift")
    req(mf["authoritative_remaining_strata"] == 17128, "MAIN remaining-strata drift")
    req(mf["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN remaining-terminal drift")
    req(mf["full178_numerical_census_complete"] is False and mf["cut195_main_pruning_credit"] is True, "MAIN FULL178/CUT195 authority drift")

    # Current cross-lane routing: no OPEN EX5 producer demand may be silently skipped.
    req(git_blob(CROSS_LANE) == CROSS_LANE_BLOB, "cross-lane demand registry blob drift")
    cl = json.loads(CROSS_LANE.read_text())
    req(cl["schema"] == "STAGE32_CROSS_LANE_DEMANDS_V1", "cross-lane registry schema drift")
    ex5_open = [d for d in cl["demands"] if d.get("producer_lane") == "EX5" and d.get("status") == "OPEN"]
    req(ex5_open == [], "OPEN EX5 producer demand preempts local BC2-34 audit boundary")
    cut192 = [d for d in cl["demands"] if d.get("demand_id") == "S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"]
    req(len(cut192) == 1 and cut192[0]["status"] == "SATISFIED", "CUT192 EX5 handoff status drift")
    cr = s["cross_lane_routing"]
    req(cr["registry_blob_sha"] == CROSS_LANE_BLOB and cr["open_ex5_producer_demand_count"] == 0 and cr["local_bc2_34_audit_boundary_may_continue"] is True, "EX5 cross-lane projection drift")

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
    req(cp33["credit"]["known_parent_unsat_count_lower_bound"] == 7255, "BC2-33 lower-bound drift")

    src34 = B2 / "bc2_34_replay_explicit_fresh_unknown81.py"
    pf34p = B2 / "bc2-34-fresh-unknown81-replay-preflight.json"
    cp34p = B2 / "bc2-34-fresh-unknown81-replay-checkpoint.json"
    req(git_blob(src34) == BC2_34_SOURCE_BLOB, "BC2-34 source blob drift")
    req(git_blob(pf34p) == BC2_34_PREFLIGHT_BLOB, "BC2-34 preflight blob drift")
    checked(pf34p, BC2_34_PREFLIGHT_CANON)
    req(git_blob(cp34p) == BC2_34_CP_BLOB, "BC2-34 checkpoint blob drift")
    cp34 = checked(cp34p, BC2_34_CP_CANON)
    r34 = cp34["replay"]
    req((r34["parents_checked"], r34["unsat_count"], r34["unknown_count"], r34["sat_count"]) == (81, 17, 64, 0), "BC2-34 partition drift")
    req(r34["per_parent_timeout_ms"] == 60000, "BC2-34 timeout drift")
    req(r34["unknown_parent_indices_sha256"] == BC2_34_UNKNOWN_SHA and len(r34["unknown_parent_indices"]) == 64, "BC2-34 UNKNOWN identity drift")
    req(r34["status_stream_sha256"] == BC2_34_STATUS_SHA, "BC2-34 status stream drift")
    req(r34["all_remaining_unknown_identities_explicitly_retained"] is True, "BC2-34 UNKNOWN retention drift")
    req(cp34["credit"]["known_parent_unsat_count_lower_bound"] == 7272, "BC2-34 lower-bound drift")
    req(cp34["credit"]["whole_first_block_picard64_unsat_candidate"] is False, "BC2-34 closure overclaim")
    req(cp34["sat_witnesses"] == [], "unexpected BC2-34 SAT witness")

    rk34 = json.loads((HERE / "runkeys/bc2-34-fresh-unknown81-replay.json").read_text())
    req(rk34["schema"] == "STAGE32EX5_BC2_34_FRESH_UNKNOWN81_REPLAY_RUNKEY_V1", "BC2-34 runkey schema drift")
    req(rk34["generation"] == 1 and rk34["armed"] is False, "BC2-34 runkey not consumed/disarmed")
    req(rk34["source_git_blob_sha"] == BC2_34_SOURCE_BLOB and rk34["preflight_git_blob_sha"] == BC2_34_PREFLIGHT_BLOB and rk34["preflight_canonical"] == BC2_34_PREFLIGHT_CANON, "BC2-34 runkey source/preflight drift")
    rc = rk34.get("consumed_run") or {}
    req((rc.get("workflow_run_id"), rc.get("authorize_job_id"), rc.get("compute_job_id"), rc.get("artifact_id")) == (BC2_34_RUN, BC2_34_AUTH_JOB, BC2_34_JOB, BC2_34_ARTIFACT), "BC2-34 execution receipt drift")
    req(rc.get("exact_head") == BC2_34_EXECUTION_HEAD and rc.get("generation") == 1, "BC2-34 execution head drift")
    req(rc.get("artifact_zip_sha256") == BC2_34_ARTIFACT_ZIP_SHA and rc.get("raw_json_sha256") == BC2_34_RAW_JSON_SHA, "BC2-34 artifact hash drift")
    req(rc.get("checkpoint_canonical") == BC2_34_CP_CANON and rc.get("checkpoint_git_blob_sha") == BC2_34_CP_BLOB, "BC2-34 checkpoint receipt drift")
    req(rc.get("new_unsat_count") == 17 and rc.get("remaining_unknown_count") == 64 and rc.get("sat_count") == 0, "BC2-34 result receipt drift")
    req(rc.get("remaining_unknown_parent_indices_sha256") == BC2_34_UNKNOWN_SHA and rc.get("status_stream_sha256") == BC2_34_STATUS_SHA, "BC2-34 retained hashes drift")
    req(rc.get("known_parent_unsat_count_lower_bound") == 7272 and rc.get("accepted_for_hostile_audit") is True, "BC2-34 audit candidate receipt drift")

    cur = s["current"]
    req(cur["status"] == "BC2_34_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "current status drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_34_TARGETED_REPLAY", "audit route drift")
    req("NO_BC2_35_BEFORE_BC2_34_HOSTILE_AUDIT_PASS" in cur["stop_semantics"], "BC2-35 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_33_audited"] is True and f["e8_bc2_34_executed"] is True, "BC2-34 frontier receipt drift")
    req((f["e8_bc2_34_new_parent_unsat_count"], f["e8_bc2_34_remaining_unknown_count"], f["e8_bc2_34_sat_count"]) == (17, 64, 0), "BC2-34 frontier partition drift")
    req(f["e8_bc2_34_remaining_unknown_parent_indices_sha256"] == BC2_34_UNKNOWN_SHA, "BC2-34 frontier UNKNOWN hash drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7272, "BC2-34 frontier lower-bound drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_33_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_33_AUDIT_REVIEW, "predecessor audit receipt drift")
    req(a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True, "BC2-34 audit freeze drift")
    req(a["bc2_34_execution_authorized"] is False, "BC2-34 execution left authorized")

    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_34_TARGETED_REPLAY", "next-step drift")
    req(ns["bc2_34_execution_authorized"] is False and ns["bc2_35_blocked_until_bc2_34_hostile_audit_pass"] is True, "BC2-35 gate drift")
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
    req("authorize-bc2-34-fresh-unknown81:" not in wf and "bc2-34-fresh-unknown81:" not in wf, "consumed BC2-34 heavy path still active")
    req("authorize-bc2-33-fresh-unknown107:" not in wf and "bc2-33-fresh-unknown107:" not in wf, "retired BC2-33 heavy path still active")
    req("authorize-e8-cut-handoff-wave:" in wf, "current e8 handoff lifecycle unexpectedly removed")
    req("verify_cross_lane_demands.py" in wf and "CROSS-LANE-DEMANDS.json" in wf, "current cross-lane workflow gate missing")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-34 targeted replay retained and frozen for hostile audit")
    print("bc2_34=17_UNSAT_64_UNKNOWN_0_SAT; known_parent_unsat_lower_bound=7272")
    print("generation1=CONSUMED_DISARMED; heavy_path=RETIRED; open_EX5_demand=0")
    print("Stage32_MAIN_credit=NO; FULL178=NO; merge=NO; next=stage32ex5-audit")


if __name__ == "__main__":
    main()
