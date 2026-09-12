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
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
BC2_30_AUDIT_HEAD = "38b60be7d0390ad5fa89ddb4dcd9511cfe36c57f"
BC2_30_AUDIT_REVIEW = 5184226057
BC2_30_CHECKPOINT = "2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a"
BC2_31_PREFLIGHT = "edd1bf6198d054277f828795f4e7a9d5372bc3094886e7afea420484bd899328"
BC2_31_SOURCE_BLOB = "bd6ba2a0048b565354319598ff5811a9edf9a7a3"
BC2_31_PREFLIGHT_BLOB = "15633233f18bf66815ca149ac3009156d0ef57e3"
BC2_19_SOURCE_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
BC2_18_SOURCE_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
BC2_19_RAW = "fcfecfc4dbd3592095c1c0302991c2b29bee22b6f3652d73612deea7775d7755"
BC2_19_STATUS_STREAM = "7a551339ab56ef34ed346b7586fd3d1f1ab81de042a3be9c1a9af2bc1d9ab18a"
PERFECT_CUBOID_FIREWALL_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected, f"canonical field drift: {path.name}")
    q = dict(obj); q.pop("canonical_sha256_without_this_field", None)
    req(csha(q) == expected, f"canonical replay drift: {path.name}")
    return obj


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V15_BC2_30_AUDIT_CONSUMED_BC2_31_RECOVERY_EXECUTION", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    a = s["stage32_main_authority"]
    req(a["routing_source_blob_sha"] == STAGE32_MAIN_BLOB and a["full178_goal_claim_id_observed"] == FULL178_GOAL_CLAIM, "Stage32 authority projection drift")
    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text(encoding="utf-8"))
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "FULL178 claim drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")

    p30 = s["prior_audited_authority"]["bc2_30_pr_1776"]
    req(p30["hostile_audit_status"] == "PASS" and p30["audit_checkpoint_exact_head"] == BC2_30_AUDIT_HEAD and p30["hostile_audit_review_id"] == BC2_30_AUDIT_REVIEW, "BC2-30 PASS authority drift")

    cur = s["current"]
    req(cur["status"] == "BC2_31_EXACT_IDENTITY_RECOVERY_EXECUTION_AUTHORIZED", "BC2-31 status drift")
    req(cur["leaf"] == "BC2_31_RECOVER_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES", "BC2-31 leaf drift")
    req(cur["next_route"] == "BC2_31_EXACT_RECOVERY_OF_UNRETAINED_BC2_19_UNKNOWN_IDENTITIES", "BC2-31 route drift")
    req("NO_STATUS_INFERENCE" in cur["stop_semantics"] and "NO_BC2_32" in cur["stop_semantics"], "BC2-31 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_30_audited"] is True, "BC2-30 audit PASS not consumed")
    req(f["e8_bc2_31_identity_recovery_executed"] is False and f["e8_bc2_31_exact_remaining172_recovered"] is False, "BC2-31 result claimed before execution")
    req(f["e8_bc2_19_unknown_parent_count"] == 236 and f["e8_bc2_30_unretained_unknown_identity_count"] == 172, "historical UNKNOWN accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7164, "lower-bound drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False and f["population_wide_main_consumable_result_complete"] is False, "local result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_30_checkpoint_canonical"] == BC2_30_CHECKPOINT, "BC2-30 checkpoint drift")
    req(rp["bc2_30_hostile_audit_exact_head"] == BC2_30_AUDIT_HEAD and rp["bc2_30_hostile_audit_review_id"] == BC2_30_AUDIT_REVIEW, "BC2-30 audit receipt drift")
    req(rp["bc2_31_preflight_canonical"] == BC2_31_PREFLIGHT and rp["bc2_31_source_git_blob_sha"] == BC2_31_SOURCE_BLOB, "BC2-31 execution lock drift")

    pf = checked(B2 / "bc2-31-recover-remaining172-preflight.json", BC2_31_PREFLIGHT)
    req(git_blob(B2 / "bc2-31-recover-remaining172-preflight.json") == BC2_31_PREFLIGHT_BLOB, "BC2-31 preflight blob drift")
    req(git_blob(B2 / "bc2_31_recover_remaining172_bc2_19_unknown.py") == BC2_31_SOURCE_BLOB, "BC2-31 source blob drift")
    req(git_blob(B2 / "bc2_19_n354_survivor_normal_positivity_mass_replay.py") == BC2_19_SOURCE_BLOB, "BC2-19 source blob drift")
    req(git_blob(B2 / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py") == BC2_18_SOURCE_BLOB, "BC2-18 source blob drift")
    req(pf["recovery"]["historical_raw_result_canonical"] == BC2_19_RAW and pf["recovery"]["historical_status_stream_sha256"] == BC2_19_STATUS_STREAM, "historical replay lock drift")
    req((pf["recovery"]["historical_unknown_count"],pf["recovery"]["retained_first64_count"],pf["recovery"]["expected_remaining_count"]) == (236,64,172), "recovery count drift")

    runkey = json.loads((HERE / "runkeys/bc2-31-recover-remaining172.json").read_text(encoding="utf-8"))
    req(runkey["schema"] == "STAGE32EX5_BC2_31_RECOVER_REMAINING172_RUNKEY_V1", "runkey schema drift")
    req(runkey["source_git_blob_sha"] == BC2_31_SOURCE_BLOB and runkey["preflight_git_blob_sha"] == BC2_31_PREFLIGHT_BLOB and runkey["preflight_canonical"] == BC2_31_PREFLIGHT, "runkey source lock drift")
    req(runkey["generation"] in (0,1), "unexpected runkey generation")
    if runkey["generation"] == 0:
        req(runkey["armed"] is False and runkey["consumed_run"] is None, "cold generation-0 runkey drift")
    else:
        req(runkey["armed"] is True and runkey["consumed_run"] is None, "generation-1 execution runkey drift")
    req(runkey["audit_consumption"]["bc2_30_hostile_audit_review_id"] == BC2_30_AUDIT_REVIEW, "runkey audit receipt drift")
    req((runkey["target"]["historical_unknown_count"],runkey["target"]["retained_first64_count"],runkey["target"]["remaining_identity_count"]) == (236,64,172), "runkey target drift")
    req(runkey["target"]["identity_recovery_only"] is True and runkey["execution"]["heavy_scaleout_authorized"] is False, "runkey scope leak")

    audit = s["intermediate_audit_boundary"]
    req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == BC2_30_AUDIT_HEAD and audit["last_hostile_audit_review_id"] == BC2_30_AUDIT_REVIEW, "BC2-30 audit consumption drift")
    req(audit["freeze_active"] is False and audit["new_audit_boundary_exists"] is False and audit["re_audit_required"] is False, "execution state incorrectly frozen")
    req(audit["bc2_31_execution_authorized"] is True and audit["bc2_30_execution_authorized"] is False, "BC2-31 authorization drift")
    req(audit["merged"] is False, "merge state leak")

    ns = s["next_step"]
    req(ns["id"] == "BC2_31_EXACT_RECOVERY_OF_UNRETAINED_BC2_19_UNKNOWN_IDENTITIES" and ns["bc2_31_identity_recovery_authorized"] is True, "next-step drift")
    req(ns["bc2_32_blocked_until_bc2_31_hostile_audit_pass"] is True, "BC2-32 firewall drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    fw = s["firewalls"]
    observed_pc_keys = {k for k in fw if "cuboid" in k or "curboid" in k}
    req(observed_pc_keys == PERFECT_CUBOID_FIREWALL_KEYS, "Perfect Cuboid firewall key-set drift")
    for section in ("historical_credit_firewall","firewalls"):
        for key, value in s[section].items(): req(value is False, f"firewall leak: {section}.{key}")
    for key,value in s["credit"].items():
        if key != "level": req(value is False, f"credit leak: credit.{key}")

    wf = MAIN_WORKFLOW.read_text(encoding="utf-8")
    for token in ("authorize-bc2-31-recovery:","bc2-31-recovery:","bc2-31-recover-remaining172.json","bd6ba2a0048b565354319598ff5811a9edf9a7a3"):
        req(token in wf, f"main workflow missing BC2-31 token: {token}")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-30 audit consumed; BC2-31 exact identity recovery is narrowly authorized")
    print("bc2_19_unknown=236;retained_first64=64;remaining_to_recover=172;known_parent_unsat_lower_bound=7164")
    print("identity_recovery_only=YES;new_math_credit=NO;whole_first_block_unsat=NO;stage32_main_credit=NO")
    print("next=BC2_31_EXACT_RECOVERY;BC2_32_BLOCKED_UNTIL_HOSTILE_AUDIT")


if __name__ == "__main__":
    main()
