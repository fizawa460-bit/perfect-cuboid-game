#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
ROOT = HERE.parents[0]
STAGE32_MAIN = ROOT / "stage32" / "MAIN-STATE.json"
BC30_TEMP_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-bc2-30.yml"
MAIN_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-main.yml"
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
BC2_29_AUDIT_HEAD = "ca8e0ea7209b898d24d5f647dcce11be1aff03b2"
BC2_29_AUDIT_REVIEW = 5183342658
BC2_30_CHECKPOINT = "2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a"
BC2_30_CHECKPOINT_BLOB = "deb35f43ba1780e58091b55a1c2e162df8bc0993"
BC2_30_RAW = "61e9ed91020c56fba0d6addda5a31daca09a9765d7472e0ca1190c7d70e49521"
BC2_30_RAW_SHA = "27607fd4266617f78515553832158bbe6b57aeb2a166c306b1ee7f83303117a8"
PERFECT_CUBOID_FIREWALL_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V14_BC2_30_RETAINED_AUDIT_BOUNDARY", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    a = s["stage32_main_authority"]
    req(a["routing_source"] == "stages/stage32/MAIN-STATE.json" and a["routing_source_blob_sha"] == STAGE32_MAIN_BLOB, "Stage32 authority projection drift")
    req(a["full178_goal_claim_id_observed"] == FULL178_GOAL_CLAIM, "FULL178 projection drift")
    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN authority blob drift")
    ma = json.loads(STAGE32_MAIN.read_text(encoding="utf-8"))
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "authoritative FULL178 claim-id drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")

    p29 = s["prior_audited_authority"]["bc2_29_pr_1776"]
    req(p29["hostile_audit_status"] == "PASS" and p29["audit_checkpoint_exact_head"] == BC2_29_AUDIT_HEAD and p29["hostile_audit_review_id"] == BC2_29_AUDIT_REVIEW, "BC2-29 PASS authority drift")

    cur = s["current"]
    req(cur["status"] == "BC2_30_RESULT_RETAINED_HOSTILE_AUDIT_REQUIRED", "BC2-30 status drift")
    req(cur["leaf"] == "BC2_30_BOUNDARY42_PARTITION_RETAINED_AUDIT_BOUNDARY", "BC2-30 leaf drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_30", "BC2-30 audit route drift")
    req(cur["stop_semantics"] == "NO_BC2_31_OR_BROAD_PROMOTION_BEFORE_BC2_30_HOSTILE_AUDIT_PASS", "BC2-31 stop firewall drift")
    req("172" in cur["blocker"] and "0_RETAINED_UNKNOWN" in cur["blocker"], "BC2-30 blocker semantics drift")

    f = s["frontier"]
    req(f["e8_bc2_29_audited"] is True, "BC2-29 audit PASS not consumed")
    req(f["e8_bc2_30_executed"] is True and f["e8_bc2_30_audited"] is False, "BC2-30 execution/audit marker drift")
    req((f["e8_bc2_30_new_parent_unsat_count"],f["e8_bc2_30_retained_unknown_count"],f["e8_bc2_30_parent_sat_count"]) == (1,0,0), "BC2-30 parent accounting drift")
    req((f["e8_bc2_30_p42_leaf_unsat_count"],f["e8_bc2_30_p42_leaf_unknown_count"],f["e8_bc2_30_p42_leaf_sat_count"]) == (4,0,0), "BC2-30 p42 accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7164, "BC2-30 lower-bound drift")
    req(f["e8_bc2_30_unretained_unknown_identity_count"] == 172, "BC2-30 172 identity firewall drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False and f["population_wide_main_consumable_result_complete"] is False, "local result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_29_hostile_audit_exact_head"] == BC2_29_AUDIT_HEAD and rp["bc2_29_hostile_audit_review_id"] == BC2_29_AUDIT_REVIEW, "BC2-29 audit receipt drift")
    req(rp["bc2_30_checkpoint_canonical"] == BC2_30_CHECKPOINT and rp["bc2_30_checkpoint_git_blob_sha"] == BC2_30_CHECKPOINT_BLOB, "BC2-30 checkpoint drift")
    req(rp["bc2_30_raw_result_canonical"] == BC2_30_RAW and rp["bc2_30_raw_json_sha256"] == BC2_30_RAW_SHA, "BC2-30 raw receipt drift")
    req(rp["bc2_30_workflow_run_id"] == 34647160641 and rp["bc2_30_compute_job_id"] == 103420643305 and rp["bc2_30_artifact_id"] == 10283165917, "BC2-30 execution receipt drift")
    req(rp["bc2_30_known_parent_unsat_count_lower_bound"] == 7164 and rp["bc2_30_retained_unknown_parent_indices"] == [], "BC2-30 residual receipt drift")

    runkey = json.loads((HERE / "runkeys/bc2-30-boundary42-partition.json").read_text(encoding="utf-8"))
    req(runkey["schema"] == "STAGE32EX5_BC2_30_BOUNDARY42_PARTITION_RUNKEY_V1" and runkey["generation"] == 1 and runkey["armed"] is False, "BC2-30 runkey not consumed/disarmed")
    consumed = runkey.get("consumed_run", {})
    req(consumed.get("checkpoint_canonical") == BC2_30_CHECKPOINT and consumed.get("checkpoint_git_blob_sha") == BC2_30_CHECKPOINT_BLOB, "BC2-30 consumed checkpoint drift")
    req(consumed.get("exact_compute_head") == "53be207f91cfd6b13ee8533efcf0af64bdccf3d6", "BC2-30 compute head drift")
    req(consumed.get("workflow_run_id") == 34647160641 and consumed.get("compute_job_id") == 103420643305, "BC2-30 run/job drift")
    req(consumed.get("artifact_id") == 10283165917 and consumed.get("artifact_zip_sha256") == "3b790a100771ffb52662f5150b8849665e758dccbc4ce991e8124780b9f1ee28", "BC2-30 artifact drift")
    req(consumed.get("raw_json_sha256") == BC2_30_RAW_SHA and consumed.get("raw_result_canonical") == BC2_30_RAW, "BC2-30 raw identity drift")
    req((consumed.get("new_parent_unsat_count"),consumed.get("retained_unknown_parent_count"),consumed.get("parent_sat_count")) == (1,0,0), "BC2-30 consumed parent accounting drift")
    req((consumed.get("p42_leaf_unsat_count"),consumed.get("p42_leaf_unknown_count"),consumed.get("p42_leaf_sat_count")) == (4,0,0), "BC2-30 consumed p42 accounting drift")
    req(consumed.get("known_parent_unsat_count_lower_bound") == 7164 and consumed.get("unretained_bc2_19_unknown_identity_count") == 172, "BC2-30 consumed boundary drift")

    claim = s["claim_sync"]
    req(claim["existing_active_goal"] == FULL178_GOAL_CLAIM and claim["lane_role"] == "ATTACKS", "claim-sync drift")
    req(claim["active_frontier_remapped"] is False and claim["main_promotion"] is False and claim["claim_registry_mutated"] is False, "claim-sync promotion leak")

    audit = s["intermediate_audit_boundary"]
    req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == BC2_29_AUDIT_HEAD and audit["last_hostile_audit_review_id"] == BC2_29_AUDIT_REVIEW, "BC2-29 audit consumption drift")
    req(audit["new_audit_boundary_exists"] is True and audit["freeze_active"] is True and audit["re_audit_required"] is True, "BC2-30 audit boundary not frozen")
    req(audit["bc2_30_execution_authorized"] is False and audit["bc2_31_execution_authorized"] is False, "BC2-30/31 authorization leak")
    req(audit["merged"] is False, "merge state leak")

    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_30_RETAINED_BOUNDARY" and ns["bc2_31_blocked_until_bc2_30_hostile_audit_pass"] is True, "BC2-30 next-step drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    fw = s["firewalls"]
    observed_pc_keys = {k for k in fw if "cuboid" in k or "curboid" in k}
    req(observed_pc_keys == PERFECT_CUBOID_FIREWALL_KEYS, "Perfect Cuboid firewall key-set drift")
    for section in ("credit","historical_credit_firewall","firewalls"):
        for key, value in s[section].items():
            if key != "level":
                req(value is False, f"credit/firewall leak: {section}.{key}")

    req(not BC30_TEMP_WORKFLOW.exists(), "temporary BC2-30 executor must be removed after retention")
    main_workflow = MAIN_WORKFLOW.read_text(encoding="utf-8")
    req("bc2-30-boundary42-bounded:" not in main_workflow and "authorize-bc2-30:" not in main_workflow, "duplicate BC2-30 heavy execution path leaked into main workflow")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    docs = {name:(HERE/name).read_text(encoding="utf-8") for name in ["README.md","MAIN-START-HERE.md","CURRENT-ROADMAP.md","CURRENT-AUDIT-CONTRACT.md","MAINBATCH-OPERATIONS.md"]}
    for name,text in docs.items():
        for token in ("BC2-30","boundary42","7164","172","#1776",str(BC2_29_AUDIT_REVIEW)):
            req(token in text, f"{name} missing BC2-30 retained-boundary token: {token}")
        req("BC2-31" in text and ("blocked" in text.lower() or "禁止" in text), f"{name} does not block BC2-31")
        req("audit" in text.lower(), f"{name} does not identify audit boundary")
        req("retained UNKNOWN=0" in text or "retained UNKNOWN は 0" in text or "retained UNKNOWN parents are `0`" in text, f"{name} does not distinguish retained UNKNOWN zero")
        req("whole first block" in text.lower() or "whole-first-block" in text.lower(), f"{name} omits whole-first-block firewall")

    print("PASS: Stage32EX5 BC2-30 retained boundary is coherent and frozen for hostile audit")
    print("bc2_30=1_NEW_UNSAT_0_RETAINED_UNKNOWN_0_SAT;4_P42_UNSAT_0_P42_UNKNOWN;known_parent_unsat_lower_bound=7164")
    print("unretained_bc2_19_unknown_identities=172;whole_first_block_unsat=NO")
    print("stage32_main_credit=NO;full178_complete=NO;merge_authorized=NO")
    print("next=HOSTILE_AUDIT_BC2_30;BC2_31_BLOCKED")


if __name__ == "__main__":
    main()
