#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKPOINT = HERE / "HPADJ22-E192-ZERO-CENTER-TOP16-CHECKPOINT.json"
CHECKPOINT_BLOB = "ee81d76359cca0519b23b4b59fdf70785df0fc96"
VERIFIER = HERE / "verify_hpadj22_e192_zero_center_top16_bc_cells.py"
VERIFIER_BLOB = "aade703bb67b3013b836366b1e64c9d8ce3083e5"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main() -> None:
    req(CHECKPOINT.is_file() and blob(CHECKPOINT) == CHECKPOINT_BLOB, "checkpoint drift")
    req(VERIFIER.is_file() and blob(VERIFIER) == VERIFIER_BLOB, "top16 verifier drift")
    cp = json.loads(CHECKPOINT.read_text())

    req(cp["schema"] == "STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_TOP16_CHECKPOINT_V1", "schema drift")
    req(cp["status"] == "EXACT_HEAD_REPLAY_SUCCESS__HOSTILE_AUDIT_REQUIRED__ZERO_MAIN_CREDIT", "status drift")
    req(cp["producer"]["exact_candidate_head"] == "fdb8f55c791df8bfd18db162fb66b854f6c210c0", "candidate head drift")
    req(cp["producer"]["verifier_blob_sha1"] == VERIFIER_BLOB, "verifier binding drift")
    req(int(cp["exact_head_ci"]["workflow_run_id"]) == 35588376541, "queued run id drift")
    req(cp["exact_head_ci"]["replay_head"] == "fdb8f55c791df8bfd18db162fb66b854f6c210c0", "replay head drift")
    req(cp["exact_head_ci"]["observed_status"] == "QUEUED", "checkpoint no longer records queued status")
    req(cp["exact_head_ci"]["conclusion"] is None, "CI conclusion prematurely recorded")
    req(cp["exact_head_ci"]["success_credit"] is False, "CI success credit prematurely granted")

    x = cp["exact_candidate"]
    req(x["current_hpadj22_subset_survivors"] == "114976575390540", "current subset drift")
    req(x["zero_center_refined_subset_survivors"] == "53376231417921", "refined subset drift")
    req(x["exact_survivor_reduction"] == "61600343972619", "reduction drift")
    req(int(x["current_hpadj22_subset_survivors"]) - int(x["zero_center_refined_subset_survivors"])
        == int(x["exact_survivor_reduction"]), "subset accounting mismatch")
    req(x["current_v45_global_upper_bound"] == "138652739800650593494", "V45 bound drift")
    req(x["candidate_global_upper_bound_if_promoted"] == "138652678200306620875", "candidate bound drift")
    req(int(x["current_v45_global_upper_bound"]) - int(x["exact_survivor_reduction"])
        == int(x["candidate_global_upper_bound_if_promoted"]), "global replacement arithmetic mismatch")
    req(x["composition_rule"] == "DIRECT_SAME_POPULATION_SUBSET_REFINEMENT__NON_ADDITIVE_REPLACEMENT", "composition drift")

    req(len(cp["target"]["selected_bc_cells"]) == 16, "selected cell count drift")
    req(len({tuple(v) for v in cp["target"]["selected_bc_cells"]}) == 16, "selected cells not disjoint by key")

    fw = cp["firewalls"]
    req(fw["exact_head_ci_pass"] is True, "exact-head CI PASS not retained")
    req(fw["hostile_audit_pass"] is False, "hostile audit PASS prematurely claimed")
    req(fw["main_credit_changed"] is False, "MAIN credit changed")
    req(fw["additive_subtraction_performed"] is False, "additive subtraction performed")
    req(fw["full178_census_claimed"] is False, "FULL178 completion claimed")
    req(fw["stage32_closed"] is False, "Stage32 closure claimed")
    req(fw["merge"] is False, "merge firewall changed")

    print("HPADJ22_E192_ZERO_CENTER_TOP16_CHECKPOINT=" + json.dumps({
        "checkpoint_blob": CHECKPOINT_BLOB,
        "verifier_blob": VERIFIER_BLOB,
        "workflow_run_id": cp["exact_head_ci"]["workflow_run_id"],\n        "job_id": cp["exact_head_ci"]["job_id"],
        "reduction": x["exact_survivor_reduction"],
        "candidate_global": x["candidate_global_upper_bound_if_promoted"],
        "zero_main_credit": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
