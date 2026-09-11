#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
RUNKEY = HERE / "runkeys/bc2-26-boundary34-partition.json"
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
BC2_25 = "fc4e4541a4f349e6c249f7dadd85f91edfd1c0dc1cb56d92b18bbf13054a4518"
BC2_26_MANIFEST = "39d816977fed0c770e155422ab7209ea3dd98dee49eb96daabb5b30557708a3a"
BC2_26_PREFLIGHT = "92c6e53d8e2e3f5bf6576983c042667b5c56c154206c5514877ab4f1e6af3bcd"
BC2_26_SOURCE_BLOB = "f795dcf24ea77a99c6c4a85bec64910ca02f65f9"
AUDIT_HEAD = "1d2e04486e170336ce02af144aabb08e4a80a31d"
AUDIT_REVIEW = 5177354131


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected, f"canonical field drift: {path.name}")
    q = dict(obj); q.pop("canonical_sha256_without_this_field", None)
    req(csha(q) == expected, f"canonical replay drift: {path.name}")
    return obj


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V7_BC2_25_AUDIT_CONSUMED_BC2_26_PREFLIGHT", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["latest_merged_pr"] == 1765 and b["merge_authorized"] is False, "merge provenance/authorization drift")

    a = s["stage32_main_authority"]
    req(a["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN" and a["primary_incomplete_id"] == "32-01", "Stage32 route drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")
    for k in ("V6_is_current_attack_target","O210_is_current_attack_target","Q602_is_current_attack_target"):
        req(a[k] is False, f"historical target reactivated: {k}")

    cur = s["current"]
    req(cur["status"] == "BC2_25_HOSTILE_AUDIT_PASS_CONSUMED_BC2_26_PREFLIGHT_READY", "BC2-26 status drift")
    req(cur["leaf"] == "BC2_26_BOUNDARY34_PARTITION_PREFLIGHT" and cur["next_route"] == "BC2_26_BOUNDARY34_PARTITION_BOUNDED", "BC2-26 route drift")
    req(cur["stop_semantics"] == "BC2_26_MAX110_ONLY_THEN_FREEZE_NEW_AUDIT_BOUNDARY_BEFORE_BC2_27", "BC2-26 stop gate drift")

    f = s["frontier"]
    req((f["e8_bc2_25_new_parent_unsat_count"],f["e8_bc2_25_retained_unknown_count"],f["e8_bc2_25_parent_sat_count"]) == (3,16,0), "BC2-25 parent accounting drift")
    req((f["e8_bc2_25_branch_unknown_count"],f["e8_bc2_25_subbranch_unknown_count"]) == (36,38), "BC2-25 residual accounting drift")
    req((f["e8_bc2_26_target_parent_count"],f["e8_bc2_26_target_branch_count"],f["e8_bc2_26_target_p33_subbranch_count"],f["e8_bc2_26_maximum_p34_leaf_checks"]) == (16,36,38,110), "BC2-26 target accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7148 and f["e8_bc2_25_unretained_unknown_identity_count"] == 172, "BC2-25 lower-bound/firewall drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_25_checkpoint_canonical"] == BC2_25, "BC2-25 checkpoint lock drift")
    req(rp["bc2_25_hostile_audit_exact_head"] == AUDIT_HEAD and rp["bc2_25_hostile_audit_review_id"] == AUDIT_REVIEW, "BC2-25 PASS receipt drift")
    req(rp["bc2_26_residual_manifest_canonical"] == BC2_26_MANIFEST and rp["bc2_26_preflight_canonical"] == BC2_26_PREFLIGHT, "BC2-26 retained preflight lock drift")
    req(rp["bc2_26_source_git_blob_sha"] == BC2_26_SOURCE_BLOB, "BC2-26 source state lock drift")

    audit = s["intermediate_audit_boundary"]
    req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == AUDIT_HEAD and audit["last_hostile_audit_review_id"] == AUDIT_REVIEW, "audit PASS not consumed")
    req(audit["prior_failed_audit_review_id"] == 5176133548, "prior FAIL receipt lost")
    req(audit["new_audit_boundary_exists"] is False and audit["bc2_26_execution_authorized"] is True, "BC2-26 audit-consumption gate drift")
    req(audit["bc2_26_authorization_scope"] == "BOUNDARY34_MAX110_ONLY", "BC2-26 scope drift")
    req(audit["merged"] is False and b["merge_authorized"] is False, "merge authorization leak")

    ns = s["next_step"]
    req(ns["id"] == "BC2_26_BOUNDARY34_PARTITION_BOUNDED" and ns["bc2_26_bounded_execution_authorized"] is True and ns["bc2_26_maximum_subbranch_checks"] == 110, "BC2-26 next-step drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")
    for section_name in ("credit","historical_credit_firewall","firewalls"):
        for key, value in s[section_name].items():
            if key != "level": req(value is False, f"credit/firewall leak: {section_name}.{key}")

    subprocess.run([sys.executable, str(B2 / "verify_bc2_25_boundary33_partition_checkpoint.py")], check=True)
    man = checked(B2 / "bc2-26-residual-p33-subbranch-manifest.json", BC2_26_MANIFEST)
    pf = checked(B2 / "bc2-26-boundary34-partition-preflight.json", BC2_26_PREFLIGHT)
    req(len(man["target"]["residual_unknown_p33_subbranches"]) == 38, "BC2-26 manifest residual count drift")
    req(len(set((r["parent_index"],r["n1"],r["n2"],r["p33"]) for r in man["target"]["residual_unknown_p33_subbranches"])) == 38, "BC2-26 manifest duplicate target")
    req(man["partition_candidate"]["maximum_subbranch_checks"] == 110 and pf["partition"]["maximum_subbranch_checks"] == 110, "BC2-26 max110 drift")
    source = B2 / "bc2_26_boundary34_partition.py"
    req(git_blob_sha(source) == BC2_26_SOURCE_BLOB, "BC2-26 source blob drift")
    rk = json.loads(RUNKEY.read_text(encoding="utf-8"))
    req(rk["schema"] == "STAGE32EX5_BC2_26_BOUNDARY34_PARTITION_RUNKEY_V1" and rk["generation"] == 1, "BC2-26 runkey drift")
    req(rk["source_git_blob_sha"] == BC2_26_SOURCE_BLOB and rk["target"]["maximum_subbranch_checks"] == 110, "BC2-26 runkey source/target drift")
    req(isinstance(rk["armed"], bool), "BC2-26 runkey armed must be boolean")

    docs = {name:(HERE/name).read_text(encoding="utf-8") for name in ["README.md","MAIN-START-HERE.md","CURRENT-ROADMAP.md","CURRENT-AUDIT-CONTRACT.md","MAINBATCH-OPERATIONS.md"]}
    for name,text in docs.items():
        for token in ("BC2-25","BC2-26","7148","16","38","110","172","#1776"):
            req(token in text, f"{name} missing live-boundary token: {token}")
    req(str(AUDIT_REVIEW) in docs["CURRENT-AUDIT-CONTRACT.md"] and AUDIT_HEAD in docs["CURRENT-AUDIT-CONTRACT.md"], "audit contract missing PASS receipt")

    print("PASS: Stage32EX5 BC2-25 hostile-audit PASS consumed; BC2-26 bounded preflight coherent")
    print(f"bc2_26=16_PARENTS_36_BRANCHES_38_P33_UNKNOWN_MAX110_P34_LEAVES;armed={rk['armed']}")
    print("known_parent_unsat_lower_bound=7148;other_unretained_unknown=172")
    print("stage32_main_credit=NO;merge_authorized=NO")


if __name__ == "__main__":
    main()
