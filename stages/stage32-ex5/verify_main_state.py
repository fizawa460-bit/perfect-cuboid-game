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
BC2_34_AUDIT_HEAD = "cdb455860849cfd064e3ab8c83d6d4993fb5ff1b"
BC2_34_AUDIT_REVIEW = 5186516652
BC2_34_CP_BLOB = "e566aeda2931642d79c88dc5eeb84b142f655609"
BC2_34_CP_CANON = "e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba"
BC2_34_UNKNOWN_SHA = "00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b"
BC2_34_REPAIR_BLOB = "5569d0d0c806db361ad6cafdafbe5e7911850e4c"
BC2_34_REPAIR_CANON = "fb111cd123eb1ee0aa99848fc7c75bd976684517cd63a2bfd44f9e9abdaed01f"
BC2_34_REPAIR_VERIFIER_BLOB = "8adab4503f4a23e778cc6374722c77849bd370f8"
B32_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
BC2_35_SOURCE_BLOB = "40111bb7619113d1c9c766089026bcf59d6bdb01"
BC2_35_PREFLIGHT_BLOB = "bf2f4b1125925a27c820dfdc49ad796e69b268b4"
BC2_35_PREFLIGHT_CANON = "e74e6c15050187d06c472c2eff6156c66837f8f9c9de3d2cfca7629b431dadb4"
BC2_35_CP_BLOB = "ee95590c637735478c06af413835ea390000b445"
BC2_35_CP_CANON = "14f808df5db80842b87efbbc0dafb9c68ad9cc5e3529b2647cfa66ee9faccf2f"
BC2_35_UNKNOWN_SHA = "95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818"
BC2_35_RUNKEY_BLOB = "5707320cc227531292f1a868d6da20554d9fd095"
BC2_35_VERIFIER_BLOB = "3057db90284fd7aa99a2335747af5826113753b3"
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
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V24_BC2_35_TARGETED_REPLAY_AUDIT_BOUNDARY", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == CURRENT_MAIN, "current MAIN observation drift")
    req(b["active_work_pr"] == 1776 and b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED", "Stage32 MAIN schema drift")
    mf = ma["current_exact_frontier"]
    req(mf["authoritative_remaining_strata"] == 17128 and mf["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN residual drift")
    req(mf["full178_numerical_census_complete"] is False, "MAIN FULL178 unexpectedly complete")

    req(git_blob(CROSS_LANE) == CROSS_LANE_BLOB, "cross-lane registry blob drift")
    cl = json.loads(CROSS_LANE.read_text())
    ex5_open = [d for d in cl["demands"] if d.get("producer_lane") == "EX5" and d.get("status") == "OPEN"]
    req(ex5_open == [], "OPEN EX5 producer demand preempts BC2-35 audit")
    cr = s["cross_lane_routing"]
    req(cr["registry_blob_sha"] == CROSS_LANE_BLOB and cr["open_ex5_producer_demand_count"] == 0 and cr["local_bc2_35_audit_boundary_may_continue"] is True, "cross-lane projection drift")

    pa = s["prior_audited_authority"]["bc2_34_pr_1776"]
    req(pa["hostile_audit_status"] == "PASS", "BC2-34 PASS not preserved")
    req(pa["audit_checkpoint_exact_head"] == BC2_34_AUDIT_HEAD and pa["hostile_audit_review_id"] == BC2_34_AUDIT_REVIEW, "BC2-34 audit receipt drift")
    req(pa["prior_failed_audit_exact_head"] == "75723b1626d7f40eb1ab75a1a52f2fc679d619bf" and pa["prior_failed_audit_review_id"] == 5186319290, "BC2-34 failed-audit provenance drift")

    cp34p = B2 / "bc2-34-fresh-unknown81-replay-checkpoint.json"
    repairp = B2 / "bc2-34-dependency-identity-repair.json"
    repairver = B2 / "verify_bc2_34_dependency_identity_repair.py"
    req(git_blob(cp34p) == BC2_34_CP_BLOB, "BC2-34 checkpoint blob drift")
    cp34 = checked(cp34p, BC2_34_CP_CANON)
    r34 = cp34["replay"]
    req((r34["parents_checked"], r34["unsat_count"], r34["unknown_count"], r34["sat_count"]) == (81,17,64,0), "BC2-34 partition drift")
    req(r34["unknown_parent_indices_sha256"] == BC2_34_UNKNOWN_SHA and len(r34["unknown_parent_indices"]) == 64, "BC2-34 target identity drift")
    req(cp34["credit"]["known_parent_unsat_count_lower_bound"] == 7272, "BC2-34 audited lower-bound drift")
    req(git_blob(repairp) == BC2_34_REPAIR_BLOB, "BC2-34 repair receipt blob drift")
    checked(repairp, BC2_34_REPAIR_CANON)
    req(git_blob(repairver) == BC2_34_REPAIR_VERIFIER_BLOB, "BC2-34 repair verifier blob drift")

    src35 = B2 / "bc2_35_replay_explicit_fresh_unknown64.py"
    pf35p = B2 / "bc2-35-fresh-unknown64-replay-preflight.json"
    cp35p = B2 / "bc2-35-fresh-unknown64-replay-checkpoint.json"
    ver35p = B2 / "verify_bc2_35_targeted_replay_checkpoint.py"
    rk35p = HERE / "runkeys/bc2-35-fresh-unknown64-replay.json"
    req(git_blob(src35) == BC2_35_SOURCE_BLOB, "BC2-35 producer blob drift")
    req(git_blob(pf35p) == BC2_35_PREFLIGHT_BLOB, "BC2-35 preflight blob drift")
    pf = checked(pf35p, BC2_35_PREFLIGHT_CANON)
    req(pf["audit_consumption"] == {"bc2_34_hostile_audit_status":"PASS","bc2_34_hostile_audit_exact_head":BC2_34_AUDIT_HEAD,"bc2_34_hostile_audit_review_id":BC2_34_AUDIT_REVIEW}, "BC2-35 preflight audit receipt drift")
    locks = pf["source_locks"]
    req(locks["producer_git_blob_sha"] == BC2_35_SOURCE_BLOB, "BC2-35 producer preflight lock drift")
    req(locks["bc2_32_producer_git_blob_sha"] == B32_BLOB and locks["bc2_19_replay_source_git_blob_sha"] == B19_BLOB and locks["bc2_18_enumerator_source_git_blob_sha"] == D18_BLOB, "BC2-35 transitive source lock drift")
    req(pf["target"]["audited_unknown_parent_count"] == 64 and pf["target"]["audited_unknown_parent_indices_sha256"] == BC2_34_UNKNOWN_SHA and pf["target"]["prior_audited_unsat_count"] == 7272, "BC2-35 target preflight drift")
    req(pf["execution"]["per_parent_timeout_ms"] == 80000 and pf["execution"]["effective_heavy_concurrency"] == 1 and pf["execution"]["workflow_timeout_minutes"] == 100 and pf["execution"]["heavy_scaleout_authorized"] is False, "BC2-35 execution preflight drift")

    req(git_blob(B2 / "bc2_32_replay_explicit_fresh_unknown170.py") == B32_BLOB, "current BC2-32 producer blob drift")
    req(git_blob(B2 / "bc2_19_n354_survivor_normal_positivity_mass_replay.py") == B19_BLOB, "current BC2-19 source blob drift")
    req(git_blob(B2 / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py") == D18_BLOB, "current BC2-18 source blob drift")

    req(git_blob(cp35p) == BC2_35_CP_BLOB, "BC2-35 checkpoint blob drift")
    cp35 = checked(cp35p, BC2_35_CP_CANON)
    r35 = cp35["replay"]
    req((r35["parents_checked"], r35["unsat_count"], r35["unknown_count"], r35["sat_count"]) == (64,12,52,0), "BC2-35 partition drift")
    req(r35["unknown_parent_indices_sha256"] == BC2_35_UNKNOWN_SHA and len(r35["unknown_parent_indices"]) == 52, "BC2-35 UNKNOWN identity drift")
    req(cp35["credit"]["known_parent_unsat_count_lower_bound"] == 7284, "BC2-35 candidate lower-bound drift")
    req(cp35["credit"]["stage32_main_credit"] is False and cp35["credit"]["full178_complete"] is False, "BC2-35 broad credit leak")
    req(git_blob(rk35p) == BC2_35_RUNKEY_BLOB, "BC2-35 consumed runkey blob drift")
    rk = json.loads(rk35p.read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_35_FRESH_UNKNOWN64_REPLAY_RUNKEY_V1" and rk["generation"] == 1 and rk["armed"] is False, "BC2-35 runkey not consumed/disarmed")
    consumed = rk["consumed_run"]
    req(consumed["accepted_for_hostile_audit"] is True and consumed["exact_head"] == "c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8", "BC2-35 execution receipt drift")
    req(consumed["workflow_run_id"] == 34696592793 and consumed["authorize_job_id"] == 103561025783 and consumed["compute_job_id"] == 103561129955, "BC2-35 workflow/job receipt drift")
    req(consumed["artifact_id"] == 10299388802 and consumed["artifact_zip_sha256"] == "7e3b5a48300af52f19a329ed8f87e2048702b3587825b8893c2d5475aab150c3", "BC2-35 artifact receipt drift")
    req(consumed["raw_json_sha256"] == "da3f19d1e7e8f72052d9046f3e1482e669a50eeada228a3b113d440081bc266c", "BC2-35 raw JSON receipt drift")
    req(consumed["checkpoint_git_blob_sha"] == BC2_35_CP_BLOB and consumed["checkpoint_canonical"] == BC2_35_CP_CANON, "BC2-35 checkpoint receipt drift")
    req((consumed["new_unsat_count"], consumed["remaining_unknown_count"], consumed["sat_count"], consumed["known_parent_unsat_count_lower_bound"]) == (12,52,0,7284), "BC2-35 consumed count drift")
    req(consumed["remaining_unknown_parent_indices_sha256"] == BC2_35_UNKNOWN_SHA, "BC2-35 consumed UNKNOWN hash drift")
    req(git_blob(ver35p) == BC2_35_VERIFIER_BLOB, "BC2-35 retained verifier blob drift")

    cur = s["current"]
    req(cur["leaf"] == "BC2_35_REFINE_REMAINING_FRESH_UNKNOWN_SET" and cur["status"] == "BC2_35_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "BC2-35 current route drift")
    req(cur["blocker"] == "HOSTILE_AUDIT_BC2_35_REQUIRED" and cur["next_route"] == "HOSTILE_AUDIT_BC2_35_TARGETED_REPLAY", "BC2-35 audit route drift")
    f = s["frontier"]
    req(f["e8_bc2_34_audited"] is True and f["e8_bc2_35_executed"] is True and f["e8_bc2_35_audited"] is False, "BC2-35 frontier audit state drift")
    req((f["e8_bc2_35_target_unknown_count"], f["e8_bc2_35_new_parent_unsat_count"], f["e8_bc2_35_remaining_unknown_count"], f["e8_bc2_35_sat_count"]) == (64,12,52,0), "BC2-35 frontier partition drift")
    req(f["e8_bc2_35_remaining_unknown_parent_indices_sha256"] == BC2_35_UNKNOWN_SHA, "BC2-35 frontier UNKNOWN hash drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7272, "unaudited BC2-35 result leaked into audited lower bound")
    req(f["e8_bc2_35_candidate_known_parent_unsat_count_lower_bound"] == 7284, "BC2-35 candidate lower bound drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "BC2-35 broad closure leak")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_34_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_34_AUDIT_REVIEW, "last consumable audit boundary drift")
    req(a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True, "BC2-35 audit boundary not frozen")
    req(a["bc2_35_execution_authorized"] is False and a["bc2_34_execution_authorized"] is False, "BC2-35 execution authority not retired")

    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_35_TARGETED_REPLAY" and ns["bc2_35_execution_authorized"] is False, "BC2-35 next-step audit gate drift")
    req(ns["bc2_36_blocked_until_bc2_35_hostile_audit_pass"] is True, "BC2-36 gate drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    req({k for k in s["firewalls"] if "cuboid" in k or "curboid" in k} == PC_KEYS, "Perfect Cuboid firewall key drift")
    for section in ("historical_credit_firewall","firewalls"):
        for key, value in s[section].items():
            req(value is False, f"firewall leak: {section}.{key}")
    for key, value in s["credit"].items():
        if key != "level":
            req(value is False, f"credit leak: credit.{key}")

    wf = MAIN_WORKFLOW.read_text()
    req("authorize-bc2-35-fresh-unknown64:" not in wf and "\n  bc2-35-fresh-unknown64:" not in wf, "retired BC2-35 heavy path still active")
    req("verify_bc2_35_targeted_replay_checkpoint.py" in wf, "BC2-35 retained verifier missing from exact-head CI")
    req("authorize-bc2-34-fresh-unknown81:" not in wf and "\n  bc2-34-fresh-unknown81:" not in wf, "retired BC2-34 heavy path returned")
    req("authorize-e8-cut-handoff-wave:" in wf, "e8 handoff lifecycle unexpectedly removed")

    subprocess.run([sys.executable, str(B2 / "verify_bc2_34_dependency_identity_repair.py")], check=True)
    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
        "verify_bc2_35_targeted_replay_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-35 targeted replay retained and frozen for hostile audit")
    print("bc2_35=CANDIDATE_12_UNSAT_52_UNKNOWN_0_SAT; audited_lower_bound=7272; candidate_lower_bound=7284")
    print("execution_head=c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8; workflow=34696592793; artifact=10299388802")
    print("next=stage32ex5-audit; BC2_36_BLOCKED; Stage32_MAIN_credit=NO; FULL178=NO; merge=NO")


if __name__ == "__main__":
    main()
