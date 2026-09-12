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
BC2_35_AUDIT_HEAD = "8bea7a6be26e01db0deb138dbd8406f578447921"
BC2_35_AUDIT_REVIEW = 5187359907
BC2_35_CP_BLOB = "ee95590c637735478c06af413835ea390000b445"
BC2_35_CP_CANON = "14f808df5db80842b87efbbc0dafb9c68ad9cc5e3529b2647cfa66ee9faccf2f"
BC2_35_UNKNOWN_SHA = "95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818"
BC2_35_RUNKEY_BLOB = "5707320cc227531292f1a868d6da20554d9fd095"
BC2_35_VERIFIER_BLOB = "3057db90284fd7aa99a2335747af5826113753b3"
BC2_34_REPAIR_VERIFIER_BLOB = "4e7916771efb6143eb605d9fd866c77a3c1e1e1a"
B32_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
BC2_36_SOURCE_BLOB = "18f9c2146d5dc97400c4af1a8691560523cc03cf"
BC2_36_PREFLIGHT_BLOB = "aa9bf40cf3550cae33cdfe8669aa51a80acddcec"
BC2_36_PREFLIGHT_CANON = "b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0"
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
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V25_BC2_35_AUDIT_CONSUMED_BC2_36_EXECUTION", "state schema drift")
    b = s["bootstrap"]
    req(b["active_work_pr"] == 1776 and b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "work surface drift")
    req(b["current_main_sha_observed"] == CURRENT_MAIN and b["merge_authorized"] is False, "MAIN observation/merge firewall drift")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED", "Stage32 MAIN schema drift")
    mf = ma["current_exact_frontier"]
    req(mf["authoritative_remaining_strata"] == 17128 and mf["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN residual drift")
    req(mf["full178_numerical_census_complete"] is False, "MAIN FULL178 unexpectedly complete")

    req(git_blob(CROSS_LANE) == CROSS_LANE_BLOB, "cross-lane registry blob drift")
    cl = json.loads(CROSS_LANE.read_text())
    req([d for d in cl["demands"] if d.get("producer_lane") == "EX5" and d.get("status") == "OPEN"] == [], "OPEN EX5 producer demand preempts BC2-36")
    cr = s["cross_lane_routing"]
    req(cr["registry_blob_sha"] == CROSS_LANE_BLOB and cr["open_ex5_producer_demand_count"] == 0 and cr["local_bc2_36_execution_may_continue"] is True, "cross-lane projection drift")
    req(s["claim_sync"]["existing_active_goal"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "claim sync drift")

    cp35p = B2 / "bc2-35-fresh-unknown64-replay-checkpoint.json"
    rk35p = HERE / "runkeys/bc2-35-fresh-unknown64-replay.json"
    ver35p = B2 / "verify_bc2_35_targeted_replay_checkpoint.py"
    req(git_blob(cp35p) == BC2_35_CP_BLOB, "BC2-35 checkpoint blob drift")
    cp35 = checked(cp35p, BC2_35_CP_CANON)
    r35 = cp35["replay"]
    req((r35["parents_checked"], r35["unsat_count"], r35["unknown_count"], r35["sat_count"]) == (64,12,52,0), "BC2-35 partition drift")
    req(r35["unknown_parent_indices_sha256"] == BC2_35_UNKNOWN_SHA and cp35["credit"]["known_parent_unsat_count_lower_bound"] == 7284, "BC2-35 retained authority drift")
    req(git_blob(rk35p) == BC2_35_RUNKEY_BLOB and git_blob(ver35p) == BC2_35_VERIFIER_BLOB, "BC2-35 receipt/verifier drift")
    rk35 = json.loads(rk35p.read_text())
    req(rk35["generation"] == 1 and rk35["armed"] is False and rk35["consumed_run"]["accepted_for_hostile_audit"] is True, "BC2-35 consumed runkey drift")
    pa35 = s["prior_audited_authority"]["bc2_35_pr_1776"]
    req(pa35["hostile_audit_status"] == "PASS" and pa35["audit_checkpoint_exact_head"] == BC2_35_AUDIT_HEAD and pa35["hostile_audit_review_id"] == BC2_35_AUDIT_REVIEW, "BC2-35 hostile audit PASS not consumed")

    repairver = B2 / "verify_bc2_34_dependency_identity_repair.py"
    req(git_blob(repairver) == BC2_34_REPAIR_VERIFIER_BLOB, "BC2-34 repair verifier blob drift")

    src36 = B2 / "bc2_36_replay_explicit_fresh_unknown52.py"
    pf36p = B2 / "bc2-36-fresh-unknown52-replay-preflight.json"
    rk36p = HERE / "runkeys/bc2-36-fresh-unknown52-replay.json"
    req(git_blob(src36) == BC2_36_SOURCE_BLOB, "BC2-36 producer blob drift")
    req(git_blob(pf36p) == BC2_36_PREFLIGHT_BLOB, "BC2-36 preflight blob drift")
    pf36 = checked(pf36p, BC2_36_PREFLIGHT_CANON)
    req(pf36["audit_consumption"] == {"bc2_35_hostile_audit_status":"PASS","bc2_35_hostile_audit_exact_head":BC2_35_AUDIT_HEAD,"bc2_35_hostile_audit_review_id":BC2_35_AUDIT_REVIEW}, "BC2-36 audit receipt drift")
    locks = pf36["source_locks"]
    req(locks["producer_git_blob_sha"] == BC2_36_SOURCE_BLOB and locks["bc2_35_checkpoint_git_blob_sha"] == BC2_35_CP_BLOB and locks["bc2_35_checkpoint_canonical"] == BC2_35_CP_CANON, "BC2-36 predecessor lock drift")
    req(locks["bc2_32_producer_git_blob_sha"] == B32_BLOB and locks["bc2_19_replay_source_git_blob_sha"] == B19_BLOB and locks["bc2_18_enumerator_source_git_blob_sha"] == D18_BLOB, "BC2-36 transitive source lock drift")
    req(pf36["target"] == {"audited_unknown_parent_count":52,"audited_unknown_parent_indices_sha256":BC2_35_UNKNOWN_SHA,"exact_audited_unknown_complement_only":True,"prior_audited_unsat_count":7284}, "BC2-36 target preflight drift")
    req(pf36["execution"]["per_parent_timeout_ms"] == 100000 and pf36["execution"]["effective_heavy_concurrency"] == 1 and pf36["execution"]["workflow_timeout_minutes"] == 110 and pf36["execution"]["heavy_scaleout_authorized"] is False, "BC2-36 execution preflight drift")
    req(git_blob(B2 / "bc2_32_replay_explicit_fresh_unknown170.py") == B32_BLOB, "current BC2-32 blob drift")
    req(git_blob(B2 / "bc2_19_n354_survivor_normal_positivity_mass_replay.py") == B19_BLOB, "current BC2-19 blob drift")
    req(git_blob(B2 / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py") == D18_BLOB, "current BC2-18 blob drift")

    rk = json.loads(rk36p.read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_36_FRESH_UNKNOWN52_REPLAY_RUNKEY_V1", "BC2-36 runkey schema drift")
    req(rk["generation"] in (0,1) and rk["armed"] is (rk["generation"] == 1), "BC2-36 runkey generation/arm drift")
    req(rk["source_git_blob_sha"] == BC2_36_SOURCE_BLOB and rk["preflight_git_blob_sha"] == BC2_36_PREFLIGHT_BLOB and rk["preflight_canonical"] == BC2_36_PREFLIGHT_CANON, "BC2-36 runkey source/preflight drift")
    req(rk["target"]["fresh_unknown_parent_count"] == 52 and rk["target"]["fresh_unknown_parent_indices_sha256"] == BC2_35_UNKNOWN_SHA and rk["target"]["prior_audited_unsat_count"] == 7284, "BC2-36 runkey target drift")
    req(rk["execution"]["per_parent_timeout_ms"] == 100000 and rk["execution"]["effective_heavy_concurrency"] == 1 and rk["execution"]["workflow_timeout_minutes"] == 110 and rk["execution"]["heavy_scaleout_authorized"] is False, "BC2-36 runkey execution drift")
    req("consumed_run" not in rk, "BC2-36 runkey unexpectedly consumed")

    cur = s["current"]
    req(cur["leaf"] == "BC2_36_REFINE_REMAINING_FRESH_UNKNOWN_SET" and cur["status"] == "BC2_36_TARGETED_REPLAY_EXECUTION_AUTHORIZED", "BC2-36 current route drift")
    req(cur["blocker"] == "BC2_36_FRESH_RUNKEY_NOT_YET_CONSUMED" and cur["next_route"] == "BC2_36_REFINE_REMAINING_FRESH_UNKNOWN_SET", "BC2-36 blocker/route drift")
    f = s["frontier"]
    req(f["e8_bc2_35_audited"] is True and f["e8_bc2_36_executed"] is False and f["e8_bc2_36_target_unknown_count"] == 52, "BC2-36 frontier drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7284 and f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "BC2-36 credit frontier drift")
    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_exact_head"] == BC2_35_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_35_AUDIT_REVIEW, "BC2-35 audit boundary receipt drift")
    req(a["freeze_active"] is False and a["new_audit_boundary_exists"] is False and a["re_audit_required"] is False and a["bc2_36_execution_authorized"] is True, "BC2-36 execution boundary drift")
    ns = s["next_step"]
    req(ns["id"] == "BC2_36_REFINE_REMAINING_FRESH_UNKNOWN_SET" and ns["bc2_36_execution_authorized"] is True and ns["bc2_37_blocked_until_bc2_36_hostile_audit_pass"] is True, "BC2-36/37 gate drift")
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
    req("authorize-bc2-36-fresh-unknown52:" in wf and "bc2-36-fresh-unknown52:" in wf, "BC2-36 heavy path missing")
    req("authorize-bc2-35-fresh-unknown64:" not in wf and "\n  bc2-35-fresh-unknown64:" not in wf, "retired BC2-35 heavy path returned")
    req("authorize-e8-cut-handoff-wave:" in wf and "bc2_36_replay_explicit_fresh_unknown52.py" in wf, "workflow route drift")

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

    print("PASS: Stage32EX5 BC2-35 hostile audit consumed; BC2-36 exact UNKNOWN52 execution boundary coherent")
    print("bc2_35=AUDITED_12_UNSAT_52_UNKNOWN_0_SAT; known_parent_unsat_lower_bound=7284")
    print(f"bc2_36_runkey_generation={rk['generation']}; armed={rk['armed']}; target=52; timeout_ms=100000")
    print("Stage32_MAIN_credit=NO; FULL178=NO; merge=NO")


if __name__ == "__main__":
    main()
