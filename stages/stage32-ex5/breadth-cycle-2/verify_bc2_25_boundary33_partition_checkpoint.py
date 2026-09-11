#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CHECKPOINT = HERE / "bc2-25-boundary33-partition-checkpoint.json"
BC2_24_CHECKPOINT = HERE / "bc2-24-explicit-fibre-degree-partition-checkpoint.json"
MANIFEST = HERE / "bc2-25-residual-branch-manifest.json"
PREFLIGHT = HERE / "bc2-25-boundary33-partition-preflight.json"
BC2_25_SOURCE = HERE / "bc2_25_boundary33_partition.py"
BC2_24_SOURCE = HERE / "bc2_24_explicit_fibre_degree_partition.py"
BC2_18_SOURCE = HERE / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py"
HPERP = REPO / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
PAIRING = REPO / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"

EXPECTED = {
    "checkpoint": "fc4e4541a4f349e6c249f7dadd85f91edfd1c0dc1cb56d92b18bbf13054a4518",
    "bc2_24_checkpoint": "ac6f8afff29a4ac969b1fd32251499f299395261c1aa96a813502cfe2b22472f",
    "manifest": "9a057a80c47b6babcec3d8ff12b4163d09bb88ccdf734ea95c5c8c344bad65b0",
    "preflight": "49ae6b46ce0d7e6e634d0bce2e2f3375b48514afe125895d89c9b8bceccf6be1",
    "bc2_25_source": "1c10dcc88059e505ab64cfad90cf1bae19b6e350",
    "bc2_24_source": "fea28d97abd21c4ee1a8a4604e38785045f4c7f5",
    "bc2_18_source": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
    "hperp": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    "pairing": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
}
EXPECTED_PARENTS = [1000,1003,1014,1048,1050,1064,1066,1103,1106,1117,1119,1133,1198,1218,1224,1243]


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def csha_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(path: Path, expected: str) -> dict:
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == expected, f"canonical field drift: {path.name}")
    req(csha_without(obj) == expected, f"canonical replay drift: {path.name}")
    return obj


def main() -> None:
    p = canonical(CHECKPOINT, EXPECTED["checkpoint"])
    canonical(BC2_24_CHECKPOINT, EXPECTED["bc2_24_checkpoint"])
    canonical(MANIFEST, EXPECTED["manifest"])
    canonical(PREFLIGHT, EXPECTED["preflight"])

    actual_blobs = {
        "bc2_25_source": blob(BC2_25_SOURCE),
        "bc2_24_source": blob(BC2_24_SOURCE),
        "bc2_18_source": blob(BC2_18_SOURCE),
        "hperp": blob(HPERP),
        "pairing": blob(PAIRING),
    }
    for name, expected in EXPECTED.items():
        if name in actual_blobs:
            req(actual_blobs[name] == expected, f"source identity drift: {name}")

    locks = p["source_locks"]
    req(locks["bc2_24_checkpoint_canonical"] == EXPECTED["bc2_24_checkpoint"], "BC2-24 checkpoint lock drift")
    req(locks["bc2_25_residual_manifest_canonical"] == EXPECTED["manifest"], "manifest lock drift")
    req(locks["preflight_canonical"] == EXPECTED["preflight"], "preflight lock drift")
    req(locks["source_git_blob_sha"] == EXPECTED["bc2_25_source"], "BC2-25 source lock drift")
    req(locks["bc2_24_source_git_blob_sha"] == EXPECTED["bc2_24_source"], "BC2-24 source lock drift")
    req(locks["bc2_18_source_git_blob_sha"] == EXPECTED["bc2_18_source"], "BC2-18 source lock drift")
    req(locks["hperp_integral_adapter_git_blob_sha"] == EXPECTED["hperp"], "hperp transitive lock drift")
    req(locks["pairing_prefix_engine_git_blob_sha"] == EXPECTED["pairing"], "pairing transitive lock drift")
    req((locks["workflow_run_id"], locks["authorize_job_id"], locks["compute_job_id"], locks["artifact_id"]) == (34574409241,103183497300,103183566458,10189289425), "compute identity drift")
    req(locks["exact_compute_head"] == "01e6e23ce90b24efda37303d81df3820a948061a", "exact compute head drift")
    req(locks["artifact_zip_sha256"] == "95201967ea288e88c973b3e7ef43494a8093bcb4f5ebf9072b17001c7118b791" and locks["artifact_zip_bytes"] == 34343, "artifact identity drift")
    req(locks["raw_result_canonical"] == "9f854cb180acdc7309f4f797a5cdf668d30556567d147bac8ac9b3cdd91a081b", "raw result lock drift")

    b18 = BC2_18_SOURCE.read_text(encoding="utf-8")
    req("from hperp_integral_adapter import HperpIntegralPairingAdapter" in b18, "BC2-18 hperp import drift")
    req("from pairing_prefix_engine import INDLIST" in b18, "BC2-18 pairing import drift")
    b24 = BC2_24_SOURCE.read_text(encoding="utf-8")
    req("import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18" in b24, "BC2-24 -> BC2-18 edge drift")
    b25 = BC2_25_SOURCE.read_text(encoding="utf-8")
    req("import bc2_24_explicit_fibre_degree_partition as b24" in b25, "BC2-25 -> BC2-24 edge drift")

    r = p["result"]
    req((r["parent_unsat_count"], r["parent_unknown_count"], r["parent_sat_count"]) == (3,16,0), "parent partition drift")
    req(r["newly_unsat_parent_indices"] == [584,1030,1056], "new UNSAT parent drift")
    req(r["residual_unknown_parent_indices"] == EXPECTED_PARENTS, "residual UNKNOWN parent drift")
    req((r["branch_unsat_count"], r["branch_unknown_count"], r["branch_sat_count"]) == (24,36,0), "branch partition drift")
    req((r["subbranch_unsat_count"], r["subbranch_unknown_count"], r["subbranch_sat_count"]) == (128,38,0), "subbranch partition drift")
    req(len(r["residual_unknown_branches"]) == 36, "residual UNKNOWN branch count drift")
    req(p["interpretation"]["known_parent_unsat_count_lower_bound"] == 7148, "UNSAT lower bound drift")
    req(p["interpretation"]["known_retained_unknown_identity_count"] == 16, "retained UNKNOWN identity drift")
    req(p["interpretation"]["unretained_unknown_identity_count"] == 172, "unretained UNKNOWN identity drift")
    req(p["target"]["other_unretained_bc2_19_unknown_identities_inferred"] is False, "172 identities inferred")
    req(p["interpretation"]["sat_witness_found"] is False and r["parent_sat_count"] == 0, "SAT semantics drift")

    for key in ("stage32_main_credit","full178_complete","effectivity_or_actual_curve_existence_proved","theorem_credit","endpoint_credit","whole_first_block_unsat","whole_stratum_closed"):
        req(p["credit"][key] is False, f"credit leak: {key}")
    for key in ("main_promotion","merge_authorized","partition_subbranch_unknown_dropped","sat_relabelled_actual_curve","unknown_relabelled_unsat","unretained_172_parent_identities_inferred","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"):
        req(p["firewalls"][key] is False, f"firewall leak: {key}")

    print("PASS: BC2-25 retained checkpoint and transitive executable dependency identities are fail-closed")
    print("parents=3_UNSAT_16_UNKNOWN_0_SAT branches=24_UNSAT_36_UNKNOWN_0_SAT subbranches=128_UNSAT_38_UNKNOWN_0_SAT")
    print("known_parent_unsat_lower_bound=7148 other_unretained_unknown=172")
    print("next=HOSTILE_AUDIT_BEFORE_BC2_26")


if __name__ == "__main__":
    main()
