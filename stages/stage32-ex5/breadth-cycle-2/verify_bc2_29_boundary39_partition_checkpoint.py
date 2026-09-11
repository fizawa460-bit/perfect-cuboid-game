#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "bc2-29-boundary39-partition-checkpoint.json"
MANIFEST = HERE / "bc2-29-residual-p38-leaf-manifest.json"
PREFLIGHT = HERE / "bc2-29-boundary39-partition-preflight.json"
EXECUTED_RUNKEY = HERE / "bc2-29-executed-runkey.json"
CURRENT_RUNKEY = ROOT / "stages/stage32-ex5/runkeys/bc2-29-boundary39-partition.json"

ECHECK = "e02b94819d44d0d74e5ce393746efcc4b069075f98c4c00ad2895246e941fe1d"
EMAN = "f04ffdd2c34f145e7650208e7fc39d69dbf08530ab699a9884f056db3c4402e4"
EPF = "1ea7f9d509f42ad688a696c8011b858e48e25a7b11909726c92cc9732d8858e9"
ERAW = "e3284337761fd966a26a4c8b720b132de7e6a481746343403454707eff28a77b"
RAW_SHA256 = "cf2ff678247cd46efcb9558a1890dd27b1f799831a1b2073ec545d7dea97c50d"
CHECKPOINT_BLOB = "2200e596c1e8077f024859370c57ee263b5227a1"
EXECUTED_RUNKEY_BLOB = "6422169f05bb0d91a75f18a1587f2d5fc2408cfb"
SOURCE_BLOBS = {
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_29_boundary39_partition.py": "5586ca655d0fb87cc9fabb2511b11699aa0ca298",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-28-boundary38-partition-checkpoint.json": "bec4b7c06de727339b8eaf42f5158b7f28ba0376",
    MANIFEST: "5f74aceb08822f51e9602d4883f84c9a84ed8f76",
    PREFLIGHT: "84246d50e6bab17bf6e2d3eeb9dba33fb52e332a",
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

    req(cp["schema"] == "STAGE32EX5_BC2_29_BOUNDARY39_PARTITION_CHECKPOINT_V1", "checkpoint schema drift")
    req(cp["status"] == "BLOCKED_BOUNDARY39_PARTITION_LEAVES_RETAINED_UNKNOWN", "checkpoint status drift")
    r = cp["result"]
    req((r["parent_unsat_count"],r["parent_unknown_count"],r["parent_sat_count"]) == (3,1,0), "parent accounting drift")
    req(r["newly_unsat_parent_indices"] == [1048,1050,1103], "new UNSAT parent set drift")
    req(r["residual_unknown_parent_indices"] == [1064], "residual parent drift")
    for prefix in ("branch","p33_subbranch","p34_target","p35_target","p38_target"):
        req((r[f"{prefix}_unsat_count"],r[f"{prefix}_unknown_count"],r[f"{prefix}_sat_count"]) == (3,1,0), f"{prefix} accounting drift")
    req((r["p39_leaf_unsat_count"],r["p39_leaf_unknown_count"],r["p39_leaf_sat_count"]) == (15,1,0), "p39 accounting drift")
    req(r["residual_unknown_p38_leaves"] == [{"n1":2,"n2":6,"p33":1,"p34":3,"p35":3,"p38":1,"parent_index":1064}], "residual p38 identity drift")
    req(cp["interpretation"]["known_parent_unsat_count_lower_bound"] == 7163, "lower-bound drift")
    req(cp["interpretation"]["unretained_unknown_identity_count"] == 172, "172 firewall drift")

    s = cp["source_locks"]
    req(s["exact_compute_head"] == "ddbb75a8d07a6d5c8f3a466bb713708b80488efc", "compute head drift")
    req(s["workflow_run_id"] == 34644942182 and s["authorize_job_id"] == 103413347381 and s["compute_job_id"] == 103413402930, "run/job provenance drift")
    req(s["artifact_id"] == 10281797941 and s["artifact_zip_bytes"] == 9576, "artifact metadata drift")
    req(s["artifact_zip_sha256"] == "cef9a3e9d6eb748140bb5e8ed5b908ca16361f1c598fd2d7ced0698bb398e762", "artifact ZIP digest drift")
    req(s["raw_json_sha256"] == RAW_SHA256 and s["raw_result_canonical"] == ERAW, "raw artifact identity drift")
    req(s["workflow_git_blob_sha"] == "0c3eb8ea5ce3074cb17d44a01761d42b15c4ef4e", "executed workflow identity drift")
    req(s["executed_runkey_git_blob_sha"] == EXECUTED_RUNKEY_BLOB, "executed runkey identity drift")
    req(s["bc2_28_checkpoint_canonical"] == "52138e7c417d69814d5007479420b56fcc27031679bf88f432916e6c89c77ec4", "BC2-28 canonical drift")

    req(manifest["target"]["target_p38_leaf_count"] == 4 and len(manifest["target"]["residual_unknown_p38_leaves"]) == 4, "manifest target drift")
    req(preflight["target"]["maximum_subbranch_checks"] == 16, "preflight maximum drift")
    req(cp["partition"]["boundary_pairing_label"] == 39 and cp["partition"]["maximum_possible_subbranch_count"] == 16, "partition contract drift")
    req(cp["partition"]["coverage_exact"] is True and cp["partition"]["disjoint"] is True, "partition exactness drift")

    runkey = json.loads(CURRENT_RUNKEY.read_text(encoding="utf-8"))
    req(runkey["generation"] == 1 and runkey["armed"] is False, "BC2-29 runkey must be consumed/disarmed")
    consumed = runkey.get("consumed_run", {})
    req(consumed.get("exact_compute_head") == s["exact_compute_head"], "runkey compute head drift")
    req(consumed.get("workflow_run_id") == s["workflow_run_id"] and consumed.get("compute_job_id") == s["compute_job_id"], "runkey run/job drift")
    req(consumed.get("artifact_id") == s["artifact_id"] and consumed.get("artifact_zip_sha256") == s["artifact_zip_sha256"], "runkey artifact drift")
    req(consumed.get("raw_json_sha256") == RAW_SHA256 and consumed.get("raw_result_canonical") == ERAW, "runkey raw identity drift")
    req(consumed.get("checkpoint_canonical") == ECHECK and consumed.get("checkpoint_git_blob_sha") == CHECKPOINT_BLOB, "runkey checkpoint drift")
    req((consumed.get("new_parent_unsat_count"),consumed.get("retained_unknown_parent_count"),consumed.get("parent_sat_count")) == (3,1,0), "runkey parent accounting drift")
    req((consumed.get("p39_leaf_unsat_count"),consumed.get("p39_leaf_unknown_count")) == (15,1), "runkey p39 accounting drift")
    req(consumed.get("known_parent_unsat_count_lower_bound") == 7163, "runkey lower-bound drift")

    for key in ("whole_first_block_unsat","whole_stratum_closed","full178_complete","stage32_main_credit","effectivity_or_actual_curve_existence_proved","theorem_credit","endpoint_credit"):
        req(cp["credit"][key] is False, f"credit leak: {key}")
    for key, value in cp["firewalls"].items():
        req(value is False, f"firewall leak: {key}")
    req(cp["next_exact_unit"]["id"] == "BC2_30_REFINE_RESIDUAL_BY_BOUNDARY42_OR_NEXT_EXACT_PAIRING", "next unit drift")
    req(cp["next_exact_unit"]["heavy_scaleout_authorized"] is False and cp["next_exact_unit"]["main_promotion_authorized"] is False, "next authorization leak")

    subprocess.run(["python", str(HERE / "verify_bc2_28_boundary38_partition_checkpoint.py")], cwd=ROOT, check=True)
    print("PASS: Stage32EX5 BC2-29 boundary39 retained checkpoint is coherent")
    print("bc2_29=3_NEW_UNSAT_1_RETAINED_UNKNOWN_0_SAT;15_P39_UNSAT_1_P39_UNKNOWN;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7163")
    print("stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_AUDIT_BC2_29;BC2_30_BLOCKED")


if __name__ == "__main__":
    main()
