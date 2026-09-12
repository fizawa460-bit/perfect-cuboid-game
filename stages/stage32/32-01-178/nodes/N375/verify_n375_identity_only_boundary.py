#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT = HERE / "RESULT.json"
N376_STATE = HERE.parent / "N376/STATE.json"

RESULT_BLOB = "c2ea65b772c16906abb961e2636f2747481d299b"
RESULT_CANON = "7f2f2995118846b140e2fb5ffcc3252973ffe3044fac5b3ffd4507ec6acc176e"
N376_STATE_BLOB = "ecfc6d5c35339305f11a5de6e95c3a644cc9910e"
N376_STATE_CANON = "81f59725176ad89d0cd32cce65967a8e45bc81849081342002ad4cd551f4d7e5"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
    req(canonical(obj) == expected_canon, f"canonical replay drift: {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", type=Path, required=True)
    args = ap.parse_args()

    result = checked(RESULT, RESULT_BLOB, RESULT_CANON)
    n376 = checked(N376_STATE, N376_STATE_BLOB, N376_STATE_CANON)
    candidate = json.loads(args.candidate.read_text())
    req(candidate == result, "generated N375 candidate differs from retained RESULT")

    req(result["status"] == "IDENTITY_ONLY_E8_NUMERICAL_LEAF_SYMMETRY", "N375 status drift")
    retained = result["retained_action"]
    req(retained["group_order"] == 1, "N375 retained group order drift")
    req(retained["valid_permutations_new_from_old_indices"] == [[0, 1, 2]], "N375 valid action drift")
    req(retained["block_orbit_count"] == 7596, "N375 block orbit count drift")
    req(retained["terminal_orbit_count"] == 858348, "N375 terminal orbit count drift")
    req(retained["strict_terminal_orbit_reduction"] is False, "N375 unexpectedly claims strict reduction")

    perms = result["candidate"]["permutation_results"]
    req(len(perms) == 6, "N375 ambient S3 enumeration drift")
    identity = [p for p in perms if p["perm_new_from_old_indices"] == [0, 1, 2]]
    req(len(identity) == 1 and identity[0]["numerical_leaf_action_valid"] is True, "N375 identity action drift")
    nonidentity = [p for p in perms if p["perm_new_from_old_indices"] != [0, 1, 2]]
    req(len(nonidentity) == 5, "N375 nonidentity action count drift")
    req(all(p["current_main_survivor_block_bijection"] is True for p in nonidentity), "N375 combinatorial terminal S3 no longer closes")
    req(all(p["fibre_cross_factor_structure_preserved"] is True for p in nonidentity), "N375 fibre/cross-factor S3 no longer closes")
    req(all(p["picard_coordinate_transform_integral"] is False for p in nonidentity), "N375 nonidentity Picard-integrality diagnosis drift")
    req(all(p["numerical_leaf_action_valid"] is False for p in nonidentity), "N375 nonidentity unexpectedly became valid")

    for key, value in result["credit"].items():
        req(value is False, f"N375 credit firewall drift: {key}")

    req(n376["status"] == "STOPPED_IDENTITY_ONLY_S3_NEEDS_NEW_SIGNATURE_INPUT_NO_CREDIT", "N376 stop status drift")
    req(n376["parent"]["n375_result_blob_sha1"] == RESULT_BLOB, "N376 parent result blob drift")
    req(n376["parent"]["n375_result_canonical_sha256"] == RESULT_CANON, "N376 parent result canonical drift")
    neg = n376["retained_negative_boundary"]
    req(neg["valid_group_order"] == 1 and neg["strict_reduction"] is False, "N376 negative boundary drift")
    req(neg["nonidentity_terminal_family_bijection"] is True, "N376 terminal-family diagnosis drift")
    req(neg["nonidentity_fibre_cross_factor_structure_preserved"] is True, "N376 structure diagnosis drift")
    req(neg["nonidentity_integral_picard_coordinate_transform"] is False, "N376 Picard-integrality diagnosis drift")
    req(n376["anti_loop"]["rerun_same_s3_candidate"] is False, "N376 anti-loop drift")
    req(n376["anti_loop"]["heavy_compute_authorized"] is False, "N376 heavy-compute firewall drift")
    for key, value in n376["credit"].items():
        req(value is False, f"N376 credit firewall drift: {key}")

    print(json.dumps({
        "verdict": "PASS_N375_RETAINED_IDENTITY_ONLY_BOUNDARY",
        "n375_result_canonical": RESULT_CANON,
        "valid_group_order": 1,
        "block_orbit_count": 7596,
        "terminal_orbit_count": 858348,
        "strict_reduction": False,
        "diagnosis": neg["diagnosis"],
        "next_gate": n376["next_gate"],
        "main_pruning_credit": False,
        "full178_complete": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
