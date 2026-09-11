#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "bc2-27-boundary35-partition-checkpoint.json"
MANIFEST = HERE / "bc2-27-residual-p34-leaf-manifest.json"
PREFLIGHT = HERE / "bc2-27-boundary35-partition-preflight.json"
EXECUTED_RUNKEY = HERE / "bc2-27-executed-runkey.json"
CURRENT_RUNKEY = ROOT / "stages/stage32-ex5/runkeys/bc2-27-boundary35-partition.json"

ECHECK = "0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462"
EMAN = "c723b63c1f61dc8f637b69cbca5888e16b6f3fb94f6bb71a8f9c57e7822a4cf1"
EPF = "1767c15cfd1064863f79f20af413651a818e1009bf37b7b471471ef89f60160b"
ERUNKEY_BLOB = "fdfa0fb893948ee6d1109ff10bf29c3e05dabc6d"
SOURCE_BLOBS = {
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_27_boundary35_partition.py": "864f9dd0955d244cdba8f0efd3471f6505e883e8",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_26_boundary34_partition.py": "f795dcf24ea77a99c6c4a85bec64910ca02f65f9",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_25_boundary33_partition.py": "1c10dcc88059e505ab64cfad90cf1bae19b6e350",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_24_explicit_fibre_degree_partition.py": "fea28d97abd21c4ee1a8a4604e38785045f4c7f5",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_18_n354_survivor_exceptional_mod8_decomposition.py": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-26-boundary34-partition-checkpoint.json": "67ef24894b23034cec237768dd4a57ebd92ca40d",
    MANIFEST: "be1eb9aef2ad5fcdb5143d84f498bd8f78d72b20",
    PREFLIGHT: "34ab0f6c7fa129b3b9712ea0431a7eefebb987e3",
    EXECUTED_RUNKEY: ERUNKEY_BLOB,
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

    runkey = json.loads(CURRENT_RUNKEY.read_text(encoding="utf-8"))
    req(runkey["armed"] is False, "BC2-27 runkey must be consumed/disarmed")
    consumed = runkey.get("consumed_run", {})
    req(consumed.get("exact_compute_head") == "21828bcf36ea33d1e6c26465eea74c646ba26901", "compute head drift")
    req(consumed.get("workflow_run_id") == 34593864110 and consumed.get("compute_job_id") == 103245141239, "workflow/job provenance drift")
    req(consumed.get("integrity_job_id") == 103245034147, "integrity job provenance drift")
    req(consumed.get("artifact_id") == 10262350002, "artifact id drift")
    req(consumed.get("artifact_zip_sha256") == "e42f8aba7ed0092e770051a732ac9c0733a9681064c7f600c9db3a7d45d6356b", "artifact digest drift")
    req(consumed.get("raw_json_sha256") == "087b8a3ad195b8bc3d6329f6170bae7e3cd0c1080326708e34d6e0e4cf50b756", "raw json digest drift")
    req(consumed.get("raw_result_canonical") == "6537cdece0d03e80fb704e9ee8b95de240ec7dc043e872004ca78d4199a08fbd", "raw result canonical drift")
    req(consumed.get("checkpoint_canonical") == ECHECK, "checkpoint consumption drift")

    s = cp["source_locks"]
    req(s["exact_compute_head"] == "21828bcf36ea33d1e6c26465eea74c646ba26901", "checkpoint compute head drift")
    req(s["workflow_run_id"] == 34593864110 and s["compute_job_id"] == 103245141239, "checkpoint run/job drift")
    req(s["integrity_job_id"] == 103245034147, "checkpoint integrity job drift")
    req(s["artifact_id"] == 10262350002 and s["artifact_zip_bytes"] == 26501, "checkpoint artifact metadata drift")
    req(s["artifact_zip_sha256"] == "e42f8aba7ed0092e770051a732ac9c0733a9681064c7f600c9db3a7d45d6356b", "checkpoint artifact digest drift")
    req(s["raw_json_sha256"] == "087b8a3ad195b8bc3d6329f6170bae7e3cd0c1080326708e34d6e0e4cf50b756", "checkpoint raw json digest drift")
    req(s["raw_result_canonical"] == "6537cdece0d03e80fb704e9ee8b95de240ec7dc043e872004ca78d4199a08fbd", "checkpoint raw canonical drift")
    req(s["workflow_git_blob_sha"] == "197e6ffe17a163cf355f6a4ebf49f8b03a5d121f", "executed workflow identity drift")
    req(s["executed_runkey_git_blob_sha"] == ERUNKEY_BLOB, "executed runkey identity drift")
    req(s["bc2_26_checkpoint_canonical"] == "b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a", "BC2-26 checkpoint lock drift")

    req(manifest["target"]["residual_unknown_p34_leaf_count"] == 23, "manifest p34 target count drift")
    req(preflight["partition"]["maximum_subbranch_checks"] == 70, "preflight leaf bound drift")
    req(cp["partition"]["boundary_pairing_label"] == 35 and cp["partition"]["maximum_possible_subbranch_count"] == 70, "partition contract drift")
    req(cp["partition"]["coverage_exact"] is True and cp["partition"]["disjoint"] is True, "partition coverage/disjointness drift")

    r = cp["result"]
    req((r["parent_unsat_count"], r["parent_unknown_count"], r["parent_sat_count"]) == (3, 9, 0), "parent accounting drift")
    req(r["newly_unsat_parent_indices"] == [1066,1117,1133], "new parent UNSAT set drift")
    req((r["branch_unsat_count"], r["branch_unknown_count"], r["branch_sat_count"]) == (7, 13, 0), "branch accounting drift")
    req((r["p33_subbranch_unsat_count"], r["p33_subbranch_unknown_count"], r["p33_subbranch_sat_count"]) == (7, 13, 0), "p33 accounting drift")
    req((r["p34_target_unsat_count"], r["p34_target_unknown_count"], r["p34_target_sat_count"]) == (10, 13, 0), "p34 accounting drift")
    req((r["p35_leaf_unsat_count"], r["p35_leaf_unknown_count"], r["p35_leaf_sat_count"]) == (57, 13, 0), "p35 accounting drift")
    req(len(r["residual_unknown_parent_indices"]) == 9, "residual parent count drift")
    req(len(r["residual_unknown_branches"]) == 13, "residual branch count drift")
    req(len(r["residual_unknown_p33_subbranches"]) == 13, "residual p33 count drift")
    req(len(r["residual_unknown_p34_leaves"]) == 13, "residual p34 count drift")
    req(len({tuple(x[k] for k in ("parent_index","n1","n2","p33","p34")) for x in r["residual_unknown_p34_leaves"]}) == 13, "residual p34 uniqueness drift")

    req(cp["interpretation"]["known_parent_unsat_count_lower_bound"] == 7155, "known UNSAT lower bound drift")
    req(cp["interpretation"]["unretained_unknown_identity_count"] == 172, "172 identity firewall drift")
    req(cp["target"]["other_unretained_bc2_19_unknown_identities_inferred"] is False, "172 identities inferred")
    for key in ("whole_first_block_unsat","whole_stratum_closed","full178_complete","stage32_main_credit","effectivity_or_actual_curve_existence_proved","theorem_credit","endpoint_credit"):
        req(cp["credit"][key] is False, f"credit leak: {key}")
    for key, value in cp["firewalls"].items():
        req(value is False, f"firewall leak: {key}")
    req(cp["next_exact_unit"]["id"] == "BC2_28_REFINE_RESIDUAL_BY_X4_OR_NEXT_EXACT_PAIRING", "next exact unit drift")
    req(cp["next_exact_unit"]["heavy_scaleout_authorized"] is False and cp["next_exact_unit"]["main_promotion_authorized"] is False, "next-step authorization leak")

    print("PASS: Stage32EX5 BC2-27 boundary35 retained checkpoint is coherent")
    print("bc2_27=3_NEW_UNSAT_9_RETAINED_UNKNOWN_0_SAT;13_BRANCH_UNKNOWN;13_P33_UNKNOWN;13_P34_UNKNOWN;13_P35_TIMEOUT_UNKNOWN;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7155")
    print("stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_AUDIT_BC2_27;BC2_28_BLOCKED")


if __name__ == "__main__":
    main()
