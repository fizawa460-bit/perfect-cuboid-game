#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "bc2-28-boundary38-partition-checkpoint.json"
MANIFEST = HERE / "bc2-28-residual-p35-leaf-manifest.json"
PREFLIGHT = HERE / "bc2-28-boundary38-partition-preflight.json"
EXECUTED_RUNKEY = HERE / "bc2-28-executed-runkey.json"
CURRENT_RUNKEY = ROOT / "stages/stage32-ex5/runkeys/bc2-28-boundary38-partition.json"

ECHECK = "52138e7c417d69814d5007479420b56fcc27031679bf88f432916e6c89c77ec4"
ECHECK_BLOB = "bec4b7c06de727339b8eaf42f5158b7f28ba0376"
PRIOR_MALFORMED_ECHECK_BLOB = "a4ea686f58d51ab451f9dbac420bfc97ca41d6ed"
ERAW = "f77cad8d03035514e43e992ccdee25c1d4f6a386789fac33e488e198c35a998d"
EMAN = "635bc832c61c539333f39f3732edd9f82397f8dc3d4a8c0a00406b2c79572477"
EPF = "afd747ef826fe0c0287d0188f5cdc7e38ae704cc50709014f1b10b7db1a471e0"
ARTIFACT_RAW_SHA256 = "768c4209d2162cd85a2c93a3bfcb3a71e8ea9a600e62b1323b8f7b372139f843"
EXECUTED_RUNKEY_BLOB = "8c18f3d05ce79d86664ae2947fb84528912cceba"
SOURCE_BLOBS = {
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_28_boundary38_partition.py": "5b5f8f927d5445d006eea19de9886b6e628a6150",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-27-boundary35-partition-checkpoint.json": "833ab2b5c87022a5d74fd6c3ecff416cfacad5ef",
    MANIFEST: "7995a64e1953149e4e2445a7e611541932cf2ebe",
    PREFLIGHT: "470f3c3d3513047d1db2696aaa84ffc57b10de26",
    EXECUTED_RUNKEY: EXECUTED_RUNKEY_BLOB,
    CHECKPOINT: ECHECK_BLOB,
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected, f"canonical field drift: {path.name}")
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
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

    req(cp["schema"] == "STAGE32EX5_BC2_28_BOUNDARY38_PARTITION_CHECKPOINT_V1", "checkpoint schema drift")
    req(cp["status"] == "BLOCKED_BOUNDARY38_PARTITION_LEAVES_RETAINED_UNKNOWN", "checkpoint status drift")
    r = cp["result"]
    req((r["parent_unsat_count"], r["parent_unknown_count"], r["parent_sat_count"]) == (5, 4, 0), "parent accounting drift")
    req(r["newly_unsat_parent_indices"] == [1000, 1003, 1014, 1198, 1243], "new parent UNSAT set drift")
    req(r["residual_unknown_parent_indices"] == [1048, 1050, 1064, 1103], "residual parent set drift")
    req((r["branch_unsat_count"], r["branch_unknown_count"], r["branch_sat_count"]) == (9, 4, 0), "branch accounting drift")
    req((r["p33_subbranch_unsat_count"], r["p33_subbranch_unknown_count"], r["p33_subbranch_sat_count"]) == (9, 4, 0), "p33 accounting drift")
    req((r["p34_target_unsat_count"], r["p34_target_unknown_count"], r["p34_target_sat_count"]) == (9, 4, 0), "p34 accounting drift")
    req((r["p35_target_unsat_count"], r["p35_target_unknown_count"], r["p35_target_sat_count"]) == (9, 4, 0), "p35 accounting drift")
    req((r["p38_leaf_unsat_count"], r["p38_leaf_unknown_count"], r["p38_leaf_sat_count"]) == (38, 4, 0), "p38 leaf accounting drift")
    req(len(r["residual_unknown_p35_leaves"]) == 4, "residual p35 count drift")
    req(cp["interpretation"]["known_parent_unsat_count_lower_bound"] == 7160, "known UNSAT lower-bound drift")
    req(cp["interpretation"]["unretained_unknown_identity_count"] == 172, "172 identity firewall drift")

    s = cp["source_locks"]
    req(s["exact_compute_head"] == "47c522ae4ee93e6fff19339048f982f48f932bab", "compute head drift")
    req(s["workflow_run_id"] == 34609454583 and s["compute_job_id"] == 103296259426, "workflow/job provenance drift")
    req(s["authorize_job_id"] == 103295985357 and s["integrity_job_id"] == 103295985700, "gate/integrity provenance drift")
    req(s["artifact_id"] == 10268117064 and s["artifact_zip_bytes"] == 19958, "artifact metadata drift")
    req(s["artifact_zip_sha256"] == "d23645cca6e4bcf011ae1b0626934feaa2dafebf2563c2ced3d6c804cd89931c", "artifact digest drift")
    req(s["raw_json_sha256"] == ARTIFACT_RAW_SHA256 and s["raw_result_canonical"] == ERAW, "artifact raw/canonical identity drift")
    req(s["workflow_git_blob_sha"] == "f90dee770e771ef64ca4295d3ad9225a5e3adc20", "executed workflow identity drift")
    req(s["executed_runkey_git_blob_sha"] == EXECUTED_RUNKEY_BLOB, "executed runkey identity drift")
    req(s["bc2_27_checkpoint_canonical"] == "0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462", "BC2-27 checkpoint lock drift")

    runkey = json.loads(CURRENT_RUNKEY.read_text(encoding="utf-8"))
    req(runkey["armed"] is False and runkey["generation"] == 1, "BC2-28 runkey must be consumed/disarmed")
    consumed = runkey.get("consumed_run", {})
    req(consumed.get("exact_compute_head") == s["exact_compute_head"], "runkey compute head drift")
    req(consumed.get("workflow_run_id") == s["workflow_run_id"] and consumed.get("compute_job_id") == s["compute_job_id"], "runkey workflow/job drift")
    req(consumed.get("artifact_id") == s["artifact_id"] and consumed.get("artifact_zip_sha256") == s["artifact_zip_sha256"], "runkey artifact drift")
    req(consumed.get("raw_json_sha256") == ARTIFACT_RAW_SHA256 and consumed.get("raw_result_canonical") == ERAW, "runkey raw identity drift")
    req(consumed.get("raw_repository_mirror_authoritative") is False, "raw mirror authority leak")
    req(consumed.get("checkpoint_canonical") == ECHECK and consumed.get("checkpoint_git_blob_sha") == ECHECK_BLOB, "runkey checkpoint drift")
    req(consumed.get("prior_malformed_checkpoint_git_blob_sha") == PRIOR_MALFORMED_ECHECK_BLOB, "checkpoint repair provenance lost")
    req((consumed.get("new_parent_unsat_count"), consumed.get("retained_unknown_parent_count"), consumed.get("parent_sat_count")) == (5, 4, 0), "runkey parent accounting drift")
    req((consumed.get("p38_leaf_unsat_count"), consumed.get("p38_leaf_unknown_count")) == (38, 4), "runkey p38 accounting drift")
    req(consumed.get("known_parent_unsat_count_lower_bound") == 7160, "runkey lower-bound drift")

    mt = manifest["target"]
    req(mt["target_p35_leaf_count"] == 13 and len(mt["residual_unknown_p35_leaves"]) == 13, "manifest p35 target count drift")
    req(mt["target_parent_count"] == 9, "manifest parent target count drift")
    pt = preflight["target"]
    req(pt["maximum_subbranch_checks"] == 42 and pt["residual_unknown_p35_leaf_count"] == 13, "preflight leaf bound drift")
    req(pt["retained_unknown_parent_count"] == 9, "preflight parent target count drift")
    req(cp["partition"]["boundary_pairing_label"] == 38 and cp["partition"]["maximum_possible_subbranch_count"] == 42, "partition contract drift")
    req(cp["partition"]["coverage_exact"] is True and cp["partition"]["disjoint"] is True, "partition coverage/disjointness drift")
    for key in ("whole_first_block_unsat", "whole_stratum_closed", "full178_complete", "stage32_main_credit", "effectivity_or_actual_curve_existence_proved", "theorem_credit", "endpoint_credit"):
        req(cp["credit"][key] is False, f"credit leak: {key}")
    for key, value in cp["firewalls"].items():
        req(value is False, f"firewall leak: {key}")
    req(cp["next_exact_unit"]["id"] == "BC2_29_REFINE_RESIDUAL_BY_BOUNDARY39_OR_NEXT_EXACT_PAIRING", "next exact unit drift")
    req(cp["next_exact_unit"]["heavy_scaleout_authorized"] is False and cp["next_exact_unit"]["main_promotion_authorized"] is False, "next-step authorization leak")

    subprocess.run(["python", str(HERE / "verify_bc2_27_boundary35_partition_checkpoint.py")], cwd=ROOT, check=True)
    print("PASS: Stage32EX5 BC2-28 repaired retained checkpoint/artifact receipt is coherent")
    print("bc2_28=5_NEW_UNSAT_4_RETAINED_UNKNOWN_0_SAT;38_P38_UNSAT_4_P38_UNKNOWN;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7160")
    print("stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_AUDIT_BC2_28;BC2_29_BLOCKED")


if __name__ == "__main__":
    main()
