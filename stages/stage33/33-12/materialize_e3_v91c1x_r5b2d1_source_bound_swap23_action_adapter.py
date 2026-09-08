#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R1 = HERE / "e3-v91c1x-r1-chain-level-action-difference-preflight.json"
C3 = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
DIAG = HERE / "diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py"
OUT = HERE / "e3-v91c1x-r5b2d1-source-bound-swap23-action-adapter.json"

R1_SHA = "b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb"
C3_SHA = "a49f7a77ad9aad10714e556503dbd5a84585c8f1c92241b9213d3e439819ca50"
DIAG_BLOB = "5119c130cf9316efd666fd99410e7e58345d08a6"
SWAP_SOURCE_SHA = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
PERM = [0, 2, 1, 3, 5, 4, 6]
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
NEXT_BLOCKER = "EXPLICIT_SWAP23_PULLBACK_OF_317_COVER_CHART_DOMAINS_AND_COMMON_REFINEMENT_INDEX_WITH_TRANSITION_COMPATIBILITY"


def csha(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def embedded_lock(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved: {path}: {claimed} {actual}")
    return obj


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def replay_literal_transport() -> dict:
    if git_blob_sha(DIAG.read_bytes()) != DIAG_BLOB:
        raise SystemExit("literal swap23 transport diagnostic blob moved")
    run = subprocess.run([sys.executable, str(DIAG)], check=True, capture_output=True, text=True)
    rows = [json.loads(line) for line in run.stdout.splitlines() if line.startswith("{")]
    if len(rows) != 1:
        raise SystemExit(f"unexpected literal transport replay rows: {len(rows)}")
    row = rows[0]
    if row["marker"] != "V91C1R_SWAP23_LITERAL_BOUNDARY_FUNCTION_PACKAGE_TRANSPORT_DIAGNOSTIC":
        raise SystemExit("literal transport marker moved")
    if row["q_word"] != ["swap12", "swap13", "swap12"]:
        raise SystemExit("swap23 word moved")
    if row["coordinate_order"] != COORDS:
        raise SystemExit("coordinate order moved")
    if row["composed_coordinate_permutation"] != PERM:
        raise SystemExit("source-bound swap23 permutation moved")
    if row["composed_coordinate_action"] != "a2<->a3,b2<->b3,a1/b1/c fixed":
        raise SystemExit("source-bound swap23 coordinate action moved")
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    r1 = embedded_lock(R1, R1_SHA)
    c3 = embedded_lock(C3, C3_SHA)
    if r1["source_locks"]["swap23_literal_package_transport"] != "stages/stage33/33-12/diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py":
        raise SystemExit("R1 literal transport locator moved")
    if c3["cover_index"]["total_chart_count"] != 317:
        raise SystemExit("C3 cover size moved")
    if c3["construction_status"]["swap23_cover_action_or_common_refinement_materialized"] is not False:
        raise SystemExit("C3 swap23 common-refinement status moved")

    replay = replay_literal_transport()
    cert = {
        "schema": "stage33.e3.v91c1x_r5b2d1.source_bound_swap23_action_adapter.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2D1_SOURCE_BOUND_SWAP23_ACTION_ADAPTER",
        "role": "EXACT_NONCREDIT_SOURCE_BOUND_SWAP23_COORDINATE_ACTION_ADAPTER_FOR_R5_FINITE_COVER",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "pr": 1695,
            "parent_pr": 1684,
            "parent_merge_commit": "e6fd1aec8391c2e9a82eab45c3498afcec99ad44",
        },
        "source_locks": {
            "r1_chain_preflight_path": "stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json",
            "r1_chain_preflight_canonical_sha256": R1_SHA,
            "literal_transport_path": "stages/stage33/33-12/diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py",
            "literal_transport_git_blob_sha1": DIAG_BLOB,
            "stage33_11d_source_lock_canonical_sha256": SWAP_SOURCE_SHA,
            "r5b2c3_path": "stages/stage33/33-12/e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json",
            "r5b2c3_canonical_sha256": C3_SHA,
        },
        "source_bound_action": {
            "word": replay["q_word"],
            "coordinate_order": COORDS,
            "composed_coordinate_permutation_zero_based": PERM,
            "coordinate_action": replay["composed_coordinate_action"],
            "literal_boundary_package_transport_replayed": True,
            "source_bound_coordinate_action_locator_materialized": True,
            "package_level_literal_closure": replay["literal_package_action_is_permutation_of_same_eight"],
            "package_level_closure_required_for_action_adapter": False,
            "reason": "R1 already fail-closes same-eight package permutation; B2D1 only recovers the certified source-bound ambient coordinate action needed to transport the finite cover.",
        },
        "construction_status": {
            "source_bound_swap23_coordinate_action_materialized": True,
            "r5b2c3_317_chart_cover_available": True,
            "swap23_pullback_of_each_317_chart_domain_materialized": False,
            "cover_action_or_common_refinement_materialized": False,
            "same_representative_transport_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "exact_consequence": {
            "previous_missing_source_action_locator_resolved": True,
            "target_side_automorphism_no_longer_used_as_an_unbound_surrogate": True,
            "next_blocker": NEXT_BLOCKER,
        },
        "credit_firewall": {
            "cover_action_credit": False,
            "common_refinement_credit": False,
            "a2_02_representative_transport_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_credit": False,
            "mask20_credit": False,
            "authority_promotion": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
        "next_exact_leaf": "V91C1X_R5B2D2_MATERIALIZE_SWAP23_PULLBACK_OF_ALL_317_CHART_DOMAINS_AND_EXPLICIT_COMMON_REFINEMENT_INDEX",
    }
    cert["canonical_sha256"] = csha(cert)
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": cert["candidate"],
        "certificate_sha256": cert["canonical_sha256"],
        "source_bound_coordinate_action": replay["composed_coordinate_action"],
        "next_blocker": NEXT_BLOCKER,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
