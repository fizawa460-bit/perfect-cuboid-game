#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "bc2-30-boundary42-partition-checkpoint.json"
MANIFEST = HERE / "bc2-30-residual-p39-leaf-manifest.json"
PREFLIGHT = HERE / "bc2-30-boundary42-partition-preflight.json"
EXECUTED_RUNKEY = HERE / "bc2-30-executed-runkey.json"
CURRENT_RUNKEY = ROOT / "stages/stage32-ex5/runkeys/bc2-30-boundary42-partition.json"

ECHECK = "2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a"
EMAN = "c984fa8cb1b2d64fe3ae16dee56f521d25341ae08200898b8baec4739ca1ca64"
EPF = "771ef6c2fb29b0aaf7612820d8892ba32e477814819219304880f6d83c6fcd4e"
ERAW = "61e9ed91020c56fba0d6addda5a31daca09a9765d7472e0ca1190c7d70e49521"
RAW_SHA256 = "27607fd4266617f78515553832158bbe6b57aeb2a166c306b1ee7f83303117a8"
CHECKPOINT_BLOB = "deb35f43ba1780e58091b55a1c2e162df8bc0993"
EXECUTED_RUNKEY_BLOB = "b3670377516e92f5225a923737983f9a7198783d"
SOURCE_BLOBS = {
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_30_boundary42_partition.py": "9e9a681ecab2bd0a2ad0a1877a855b09e356a54d",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-29-boundary39-partition-checkpoint.json": "2200e596c1e8077f024859370c57ee263b5227a1",
    MANIFEST: "4f1dcec4d2956309cecddd79f05cd275120999f0",
    PREFLIGHT: "de79e172ad43e7b99d27b2096e2a40835eec33ed",
    EXECUTED_RUNKEY: EXECUTED_RUNKEY_BLOB,
    CHECKPOINT: CHECKPOINT_BLOB,
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected, f"canonical field drift: {path.name}")
    q = dict(obj); q.pop("canonical_sha256_without_this_field", None)
    req(csha(q) == expected, f"canonical replay drift: {path.name}")
    return obj


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def main() -> None:
    cp = checked(CHECKPOINT, ECHECK)
    manifest = checked(MANIFEST, EMAN)
    preflight = checked(PREFLIGHT, EPF)
    for path, expected in SOURCE_BLOBS.items():
        req(blob(path) == expected, f"source/dependency blob drift: {path.relative_to(ROOT)}")

    req(cp["schema"] == "STAGE32EX5_BC2_30_BOUNDARY42_PARTITION_CHECKPOINT_V1", "checkpoint schema drift")
    req(cp["status"] == "PASS_FINAL_BC2_29_RETAINED_UNKNOWN_PARENT_EXACT_UNSAT_BY_BOUNDARY42_PARTITION", "checkpoint status drift")
    r = cp["result"]
    req((r["parent_unsat_count"],r["parent_unknown_count"],r["parent_sat_count"]) == (1,0,0), "parent accounting drift")
    req(r["newly_unsat_parent_indices"] == [1064] and r["residual_unknown_parent_indices"] == [], "parent identity drift")
    req((r["p42_leaf_unsat_count"],r["p42_leaf_unknown_count"],r["p42_leaf_sat_count"]) == (4,0,0), "p42 accounting drift")
    req(r["residual_unknown_p42_leaves"] == [], "residual p42 leaf drift")
    req(cp["interpretation"]["known_parent_unsat_count_lower_bound"] == 7164, "lower-bound drift")
    req(cp["interpretation"]["known_retained_unknown_identity_count_after_this_run"] == 0, "retained UNKNOWN count drift")
    req(cp["interpretation"]["unretained_unknown_identity_count"] == 172, "172 firewall drift")
    req(cp["interpretation"]["whole_first_block_unsat_proved"] is False, "whole-first-block promotion leak")

    s = cp["source_locks"]
    req(s["exact_compute_head"] == "53be207f91cfd6b13ee8533efcf0af64bdccf3d6", "compute head drift")
    req(s["workflow_run_id"] == 34647160641 and s["authorize_job_id"] == 103420588963 and s["compute_job_id"] == 103420643305, "run/job provenance drift")
    req(s["artifact_id"] == 10283165917 and s["artifact_zip_bytes"] == 3526, "artifact metadata drift")
    req(s["artifact_zip_sha256"] == "3b790a100771ffb52662f5150b8849665e758dccbc4ce991e8124780b9f1ee28", "artifact ZIP digest drift")
    req(s["raw_json_sha256"] == RAW_SHA256 and s["raw_result_canonical"] == ERAW, "raw artifact identity drift")
    req(s["workflow_git_blob_sha"] == "727fb4cc2c83ac91db3c7175256d802ad84410e9", "executed workflow identity drift")
    req(s["executed_runkey_git_blob_sha"] == EXECUTED_RUNKEY_BLOB, "executed runkey identity drift")
    req(s["bc2_29_checkpoint_canonical"] == "e02b94819d44d0d74e5ce393746efcc4b069075f98c4c00ad2895246e941fe1d", "BC2-29 canonical drift")
    req(s["bc2_29_checkpoint_git_blob_sha"] == "2200e596c1e8077f024859370c57ee263b5227a1", "BC2-29 checkpoint blob drift")

    req(manifest["target"]["target_p39_leaf_count"] == 1 and len(manifest["target"]["residual_unknown_p39_leaves"]) == 1, "manifest target drift")
    req(manifest["target"]["residual_unknown_p39_leaves"][0] == {"parent_index":1064,"n1":2,"n2":6,"p33":1,"p34":3,"p35":3,"p38":1,"p39":3}, "manifest residual identity drift")
    req(preflight["audit_consumption"] == {"bc2_29_hostile_audit_status":"PASS","bc2_29_hostile_audit_exact_head":"ca8e0ea7209b898d24d5f647dcce11be1aff03b2","bc2_29_hostile_audit_review_id":5183342658}, "BC2-29 audit receipt drift")
    req(preflight["target"]["maximum_subbranch_checks"] == 4, "preflight maximum drift")
    req(cp["partition"]["boundary_pairing_label"] == 42 and cp["partition"]["maximum_possible_subbranch_count"] == 4, "partition contract drift")
    req(cp["partition"]["coverage_exact"] is True and cp["partition"]["disjoint"] is True, "partition exactness drift")

    runkey = json.loads(CURRENT_RUNKEY.read_text(encoding="utf-8"))
    req(runkey["generation"] == 1 and runkey["armed"] is False, "BC2-30 runkey must be consumed/disarmed")
    consumed = runkey.get("consumed_run", {})
    req(consumed.get("exact_compute_head") == s["exact_compute_head"], "runkey compute head drift")
    req(consumed.get("workflow_run_id") == s["workflow_run_id"] and consumed.get("compute_job_id") == s["compute_job_id"], "runkey run/job drift")
    req(consumed.get("artifact_id") == s["artifact_id"] and consumed.get("artifact_zip_sha256") == s["artifact_zip_sha256"], "runkey artifact drift")
    req(consumed.get("raw_json_sha256") == RAW_SHA256 and consumed.get("raw_result_canonical") == ERAW, "runkey raw identity drift")
    req(consumed.get("checkpoint_canonical") == ECHECK and consumed.get("checkpoint_git_blob_sha") == CHECKPOINT_BLOB, "runkey checkpoint drift")
    req((consumed.get("new_parent_unsat_count"),consumed.get("retained_unknown_parent_count"),consumed.get("parent_sat_count")) == (1,0,0), "runkey parent accounting drift")
    req((consumed.get("p42_leaf_unsat_count"),consumed.get("p42_leaf_unknown_count"),consumed.get("p42_leaf_sat_count")) == (4,0,0), "runkey p42 accounting drift")
    req(consumed.get("known_parent_unsat_count_lower_bound") == 7164, "runkey lower-bound drift")
    req(consumed.get("unretained_bc2_19_unknown_identity_count") == 172, "runkey 172 firewall drift")

    req(cp["credit"]["final_bc2_29_residual_parent_exact_unsat"] is True, "local exact credit missing")
    for key in ("whole_first_block_unsat","whole_stratum_closed","full178_complete","stage32_main_credit","effectivity_or_actual_curve_existence_proved","theorem_credit","endpoint_credit"):
        req(cp["credit"][key] is False, f"credit leak: {key}")
    for key, value in cp["firewalls"].items():
        req(value is False, f"firewall leak: {key}")
    req(cp["next_exact_unit"]["id"] == "BC2_31_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES", "next unit drift")
    req(cp["next_exact_unit"]["heavy_scaleout_authorized"] is False and cp["next_exact_unit"]["main_promotion_authorized"] is False, "next authorization leak")

    subprocess.run(["python", str(HERE / "verify_bc2_29_boundary39_partition_checkpoint.py")], cwd=ROOT, check=True)
    print("PASS: Stage32EX5 BC2-30 boundary42 retained checkpoint is coherent")
    print("bc2_30=1_NEW_UNSAT_0_RETAINED_UNKNOWN_0_SAT;4_P42_UNSAT_0_P42_UNKNOWN;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7164")
    print("whole_first_block_unsat=NO;stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_AUDIT_BC2_30;BC2_31_BLOCKED")


if __name__ == "__main__":
    main()
