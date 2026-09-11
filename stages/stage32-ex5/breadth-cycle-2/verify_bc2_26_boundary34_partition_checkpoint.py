#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "bc2-26-boundary34-partition-checkpoint.json"
MANIFEST = HERE / "bc2-26-residual-p33-subbranch-manifest.json"
PREFLIGHT = HERE / "bc2-26-boundary34-partition-preflight.json"
EXECUTED_RUNKEY = HERE / "bc2-26-executed-runkey.json"
CURRENT_RUNKEY = ROOT / "stages/stage32-ex5/runkeys/bc2-26-boundary34-partition.json"

ECHECK = "b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a"
EMAN = "39d816977fed0c770e155422ab7209ea3dd98dee49eb96daabb5b30557708a3a"
EPF = "92c6e53d8e2e3f5bf6576983c042667b5c56c154206c5514877ab4f1e6af3bcd"
ERUNKEY_BLOB = "e114ed9266c8b317a91e612199c966dbb4cbf87d"
SOURCE_BLOBS = {
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_26_boundary34_partition.py": "f795dcf24ea77a99c6c4a85bec64910ca02f65f9",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_25_boundary33_partition.py": "1c10dcc88059e505ab64cfad90cf1bae19b6e350",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_24_explicit_fibre_degree_partition.py": "fea28d97abd21c4ee1a8a4604e38785045f4c7f5",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_18_n354_survivor_exceptional_mod8_decomposition.py": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-25-boundary33-partition-checkpoint.json": "3b2fe6423696a56c0c871e82529c11c6bdfbe4a1",
    MANIFEST: "4ca8dedefbb3a05fbb3d45e1e16b98ff6bd5dde1",
    PREFLIGHT: "6cdccc8fda776a88c398be2171c8eb102245b508",
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
    req(runkey["armed"] is False, "BC2-26 runkey must be consumed/disarmed")
    consumed = runkey.get("consumed_run", {})
    req(consumed.get("exact_compute_head") == "7d5c35057b480ebe6bf3b0cdf047c0d7bdfde18f", "compute head drift")
    req(consumed.get("workflow_run_id") == 34588771756 and consumed.get("compute_job_id") == 103229111936, "workflow/job provenance drift")
    req(consumed.get("artifact_id") == 10194988584, "artifact id drift")
    req(consumed.get("artifact_zip_sha256") == "6844041386ce9ebf198e2dd7c88c545bca8ce524a9f2659e7f81351b2aa23465", "artifact digest drift")
    req(consumed.get("raw_result_canonical") == "f61f60804829c63b2090b42e142824411120f4d1a80d04ea323e04127e94e831", "raw result canonical drift")
    req(consumed.get("checkpoint_canonical") == ECHECK, "checkpoint consumption drift")

    s = cp["source_locks"]
    req(s["exact_compute_head"] == "7d5c35057b480ebe6bf3b0cdf047c0d7bdfde18f", "checkpoint compute head drift")
    req(s["workflow_run_id"] == 34588771756 and s["compute_job_id"] == 103229111936, "checkpoint run/job drift")
    req(s["artifact_id"] == 10194988584 and s["artifact_zip_bytes"] == 32835, "checkpoint artifact metadata drift")
    req(s["artifact_zip_sha256"] == "6844041386ce9ebf198e2dd7c88c545bca8ce524a9f2659e7f81351b2aa23465", "checkpoint artifact digest drift")
    req(s["raw_json_sha256"] == "7e4531cd9539e446ad1977129320bb94a9eb3d0523771a08fdc7b37d747d0959", "raw json digest drift")
    req(s["raw_result_canonical"] == "f61f60804829c63b2090b42e142824411120f4d1a80d04ea323e04127e94e831", "raw canonical drift")
    req(s["workflow_git_blob_sha"] == "4791774b07e9b6f62eff7ab369b3e7eed6b1ce7e", "executed workflow identity drift")
    req(s["executed_runkey_git_blob_sha"] == ERUNKEY_BLOB, "executed runkey identity drift")

    req(manifest["target"]["residual_unknown_p33_subbranch_count"] == 38, "manifest p33 target count drift")
    req(preflight["partition"]["maximum_subbranch_checks"] == 110, "preflight leaf bound drift")
    req(cp["partition"]["boundary_pairing_label"] == 34 and cp["partition"]["maximum_possible_subbranch_count"] == 110, "partition contract drift")

    r = cp["result"]
    req((r["parent_unsat_count"], r["parent_unknown_count"], r["parent_sat_count"]) == (4, 12, 0), "parent accounting drift")
    req(r["newly_unsat_parent_indices"] == [1106,1119,1218,1224], "new parent UNSAT set drift")
    req((r["branch_unsat_count"], r["branch_unknown_count"], r["branch_sat_count"]) == (16, 20, 0), "branch accounting drift")
    req((r["p33_subbranch_unsat_count"], r["p33_subbranch_unknown_count"], r["p33_subbranch_sat_count"]) == (18, 20, 0), "p33 accounting drift")
    req((r["p34_leaf_unsat_count"], r["p34_leaf_unknown_count"], r["p34_leaf_sat_count"]) == (87, 23, 0), "p34 leaf accounting drift")
    req(len(r["residual_unknown_parent_indices"]) == 12, "residual parent count drift")
    req(len(r["residual_unknown_branches"]) == 20, "residual branch count drift")
    req(len(r["residual_unknown_p33_subbranches"]) == 20, "residual p33 count drift")
    req(len(r["residual_unknown_p34_leaves"]) == 23, "residual p34 leaf count drift")
    req(len({tuple(x[k] for k in ("parent_index","n1","n2","p33","p34")) for x in r["residual_unknown_p34_leaves"]}) == 23, "residual p34 leaf uniqueness drift")

    req(cp["interpretation"]["known_parent_unsat_count_lower_bound"] == 7152, "known UNSAT lower bound drift")
    req(cp["interpretation"]["unretained_unknown_identity_count"] == 172, "172 identity firewall drift")
    req(cp["target"]["other_unretained_bc2_19_unknown_identities_inferred"] is False, "172 identities inferred")
    for key in ("whole_first_block_unsat","whole_stratum_closed","full178_complete","stage32_main_credit","effectivity_or_actual_curve_existence_proved","theorem_credit","endpoint_credit"):
        req(cp["credit"][key] is False, f"credit leak: {key}")
    for key, value in cp["firewalls"].items():
        req(value is False, f"firewall leak: {key}")
    req(cp["next_exact_unit"]["id"] == "BC2_27_REFINE_RESIDUAL_BY_X4_OR_THIRD_EXACT_PAIRING", "next exact unit drift")
    req(cp["next_exact_unit"]["heavy_scaleout_authorized"] is False and cp["next_exact_unit"]["main_promotion_authorized"] is False, "next-step authorization leak")

    print("PASS: Stage32EX5 BC2-26 boundary34 retained checkpoint is coherent")
    print("bc2_26=4_NEW_UNSAT_12_RETAINED_UNKNOWN_0_SAT;23_P34_UNKNOWN_LEAVES;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7152")
    print("stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_AUDIT_BC2_26;BC2_27_BLOCKED")


if __name__ == "__main__":
    main()
