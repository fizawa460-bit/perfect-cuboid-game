#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
STAGE32_MAIN = HERE.parent / "stage32" / "MAIN-STATE.json"
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
BC2_27 = "0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462"
BC2_27_AUDIT_HEAD = "b70bc51909f5ed78641ee3b727a2258382ef950c"
BC2_27_AUDIT_REVIEW = 5179488973
BC2_27_FAIL_HEAD = "43fce7733be95b47b2d2a4e4568300add7694224"
BC2_27_FAIL_REVIEW = 5179261378
BC2_28_MANIFEST = "635bc832c61c539333f39f3732edd9f82397f8dc3d4a8c0a00406b2c79572477"
BC2_28_MANIFEST_BLOB = "7995a64e1953149e4e2445a7e611541932cf2ebe"
BC2_28_PREFLIGHT = "afd747ef826fe0c0287d0188f5cdc7e38ae704cc50709014f1b10b7db1a471e0"
BC2_28_PREFLIGHT_BLOB = "470f3c3d3513047d1db2696aaa84ffc57b10de26"
BC2_28_SOURCE_BLOB = "5b5f8f927d5445d006eea19de9886b6e628a6150"
PERFECT_CUBOID_FIREWALL_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text())
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V10_BC2_28_BOUNDARY38_EXECUTION", "state schema drift")

    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    a = s["stage32_main_authority"]
    req(a["routing_source"] == "stages/stage32/MAIN-STATE.json", "Stage32 routing source drift")
    req(a["routing_source_blob_sha"] == STAGE32_MAIN_BLOB, "Stage32 authority blob lock drift")
    req(a["full178_goal_claim_id_observed"] == FULL178_GOAL_CLAIM, "FULL178 projection drift")
    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN authority blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "authoritative FULL178 claim-id drift")
    req(a["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN" and a["primary_incomplete_id"] == "32-01", "Stage32 route drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")

    prior = s["prior_audited_authority"]["bc2_27_pr_1776"]
    req(prior["hostile_audit_status"] == "PASS" and prior["audit_checkpoint_exact_head"] == BC2_27_AUDIT_HEAD and prior["hostile_audit_review_id"] == BC2_27_AUDIT_REVIEW, "BC2-27 PASS authority drift")
    req(prior["prior_failed_audit_exact_head"] == BC2_27_FAIL_HEAD and prior["prior_failed_audit_review_id"] == BC2_27_FAIL_REVIEW, "BC2-27 prior FAIL receipt drift")

    cur = s["current"]
    req(cur["status"] == "BC2_27_AUDIT_CONSUMED_BC2_28_BOUNDARY38_EXECUTION_AUTHORIZED", "BC2-28 status drift")
    req(cur["leaf"] == "BC2_28_BOUNDARY38_PARTITION_BOUNDED_EXECUTION", "BC2-28 leaf drift")
    req(cur["next_route"] == "BC2_28_BOUNDARY38_PARTITION_BOUNDED", "BC2-28 route drift")
    req(cur["stop_semantics"] == "NO_BC2_29_OR_BROAD_PROMOTION_BEFORE_BC2_28_RESULT_RETENTION_AND_AUDIT_BOUNDARY", "BC2-29 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_27_audited"] is True, "BC2-27 audited marker missing")
    req((f["e8_bc2_27_new_parent_unsat_count"], f["e8_bc2_27_retained_unknown_count"], f["e8_bc2_27_parent_sat_count"]) == (3,9,0), "BC2-27 parent accounting drift")
    req((f["e8_bc2_27_branch_unknown_count"], f["e8_bc2_27_p33_subbranch_unknown_count"], f["e8_bc2_27_p34_target_unknown_count"], f["e8_bc2_27_p35_leaf_unknown_count"]) == (13,13,13,13), "BC2-27 hierarchy accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7155 and f["e8_bc2_27_unretained_unknown_identity_count"] == 172, "BC2-27 lower-bound/firewall drift")
    req((f["e8_bc2_28_target_parent_count"], f["e8_bc2_28_target_p35_leaf_count"], f["e8_bc2_28_maximum_p38_subbranch_checks"]) == (9,13,42), "BC2-28 target accounting drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_27_checkpoint_canonical"] == BC2_27, "BC2-27 checkpoint drift")
    req(rp["bc2_27_hostile_audit_exact_head"] == BC2_27_AUDIT_HEAD and rp["bc2_27_hostile_audit_review_id"] == BC2_27_AUDIT_REVIEW, "BC2-27 PASS receipt drift")
    req(rp["bc2_27_prior_failed_audit_exact_head"] == BC2_27_FAIL_HEAD and rp["bc2_27_prior_failed_audit_review_id"] == BC2_27_FAIL_REVIEW, "BC2-27 FAIL provenance drift")
    req(rp["bc2_28_residual_manifest_canonical"] == BC2_28_MANIFEST and rp["bc2_28_preflight_canonical"] == BC2_28_PREFLIGHT, "BC2-28 retained preflight identity drift")
    req(rp["bc2_28_source_git_blob_sha"] == BC2_28_SOURCE_BLOB, "BC2-28 producer lock drift")

    manifest = B2 / "bc2-28-residual-p35-leaf-manifest.json"
    preflight = B2 / "bc2-28-boundary38-partition-preflight.json"
    source = B2 / "bc2_28_boundary38_partition.py"
    req(git_blob(manifest) == BC2_28_MANIFEST_BLOB, "BC2-28 manifest blob drift")
    req(git_blob(preflight) == BC2_28_PREFLIGHT_BLOB, "BC2-28 preflight blob drift")
    req(git_blob(source) == BC2_28_SOURCE_BLOB, "BC2-28 source blob drift")

    claim = s["claim_sync"]
    req(claim["existing_active_goal"] == FULL178_GOAL_CLAIM and claim["lane_role"] == "ATTACKS", "claim-sync drift")
    req(claim["active_frontier_remapped"] is False and claim["main_promotion"] is False, "claim-sync promotion leak")

    audit = s["intermediate_audit_boundary"]
    req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == BC2_27_AUDIT_HEAD and audit["last_hostile_audit_review_id"] == BC2_27_AUDIT_REVIEW, "BC2-27 PASS not consumed")
    req(audit["prior_failed_audit_exact_head"] == BC2_27_FAIL_HEAD and audit["prior_failed_audit_review_id"] == BC2_27_FAIL_REVIEW, "prior audit FAIL lost")
    req(audit["new_audit_boundary_exists"] is False and audit["freeze_active"] is False and audit["re_audit_required"] is False, "stale audit freeze leaked into BC2-28")
    req(audit["bc2_28_execution_authorized"] is True and audit["bc2_29_execution_authorized"] is False, "BC2-28/29 authorization drift")
    req(audit["merged"] is False, "merge state leak")

    ns = s["next_step"]
    req(ns["id"] == "BC2_28_BOUNDARY38_PARTITION_BOUNDED" and ns["bc2_29_blocked_until_bc2_28_retention_and_audit_boundary"] is True, "BC2-28 next-step drift")
    for k in ("heavy_scaleout_authorized", "main_promotion_authorized", "n350_registration_authorized", "merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    fw = s["firewalls"]
    observed_pc_keys = {k for k in fw if "cuboid" in k or "curboid" in k}
    req(observed_pc_keys == PERFECT_CUBOID_FIREWALL_KEYS, "Perfect Cuboid firewall key-set drift")
    for section in ("credit", "historical_credit_firewall", "firewalls"):
        for key, value in s[section].items():
            if key != "level":
                req(value is False, f"credit/firewall leak: {section}.{key}")

    rk = json.loads((HERE / "runkeys/bc2-28-boundary38-partition.json").read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_28_BOUNDARY38_PARTITION_RUNKEY_V1" and rk["generation"] == 1 and rk["armed"] is True, "BC2-28 runkey not freshly armed")
    ra = rk["audit_consumption"]
    req(ra["bc2_27_hostile_audit_status"] == "PASS" and ra["bc2_27_hostile_audit_exact_head"] == BC2_27_AUDIT_HEAD and ra["bc2_27_hostile_audit_review_id"] == BC2_27_AUDIT_REVIEW, "BC2-28 runkey audit receipt drift")
    req(rk["source_git_blob_sha"] == BC2_28_SOURCE_BLOB and rk["residual_manifest_git_blob_sha"] == BC2_28_MANIFEST_BLOB and rk["preflight_git_blob_sha"] == BC2_28_PREFLIGHT_BLOB, "BC2-28 runkey blob lock drift")
    req(rk["residual_manifest_canonical"] == BC2_28_MANIFEST and rk["preflight_canonical"] == BC2_28_PREFLIGHT, "BC2-28 runkey canonical drift")
    req((rk["target"]["retained_unknown_parent_count"], rk["target"]["residual_unknown_p35_leaf_count"], rk["target"]["maximum_subbranch_checks"]) == (9,13,42), "BC2-28 runkey target drift")
    req(rk["execution"]["effective_heavy_concurrency"] == 1 and rk["execution"]["per_subbranch_timeout_ms"] == 2000 and rk["execution"]["heavy_scaleout_authorized"] is False, "BC2-28 execution scope drift")

    subprocess.run([sys.executable, str(B2 / "verify_bc2_25_boundary33_partition_checkpoint.py")], check=True)
    subprocess.run([sys.executable, str(B2 / "verify_bc2_26_boundary34_partition_checkpoint.py")], check=True)
    subprocess.run([sys.executable, str(B2 / "verify_bc2_27_boundary35_partition_checkpoint.py")], check=True)

    docs = {name: (HERE / name).read_text() for name in ["README.md","MAIN-START-HERE.md","CURRENT-ROADMAP.md","CURRENT-AUDIT-CONTRACT.md","MAINBATCH-OPERATIONS.md"]}
    for name, text in docs.items():
        for token in ("BC2-28", "boundary38", "42", "7155", "172", "#1776", str(BC2_27_AUDIT_REVIEW)):
            req(token in text, f"{name} missing BC2-28 authorization token: {token}")
        req("BC2-29" in text and ("blocked" in text.lower() or "禁止" in text), f"{name} does not block BC2-29")

    print("PASS: Stage32EX5 BC2-27 hostile-audit PASS consumed; BC2-28 boundary38 bounded execution authorized")
    print("bc2_27_audited_lower_bound=7155;bc2_28_target=9_PARENTS_13_P35_TIMEOUT_LEAVES_MAX42_P38_CHECKS")
    print("stage32_main_credit=NO;full178_complete=NO;merge_authorized=NO")
    print("next=BC2_28_BOUNDARY38_PARTITION_BOUNDED;BC2_29_BLOCKED")


if __name__ == "__main__":
    main()
