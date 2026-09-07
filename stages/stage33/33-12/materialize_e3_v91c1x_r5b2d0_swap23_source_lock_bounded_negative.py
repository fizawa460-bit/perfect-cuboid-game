#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R2 = HERE / "e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"
C3 = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
OUT = HERE / "e3-v91c1x-r5b2d0-swap23-source-lock-bounded-negative.json"

R2_SHA = "912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1"
C3_SHA = "a49f7a77ad9aad10714e556503dbd5a84585c8f1c92241b9213d3e439819ca50"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
BLOCKER = "LITERAL_SOURCE_BOUND_SWAP23_ACTION_ON_AMBIENT_COORDINATES_OR_EQUIVALENT_SOURCE_SIDE_MARKING_DATA"

COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
TAU = {"a1":"a1", "a2":"a3", "a3":"a2", "b1":"b1", "b2":"b3", "b3":"b2", "c":"c"}
QUADRICS = {
    "F1": {"a1":1, "a2":1, "b3":-1},
    "F2": {"a2":1, "a3":1, "b1":-1},
    "F3": {"a1":1, "a3":1, "b2":-1},
    "F4": {"a1":1, "a2":1, "a3":1, "c":-1},
}
EXPECTED_QUADRIC_ACTION = {"F1":"F3", "F2":"F2", "F3":"F1", "F4":"F4"}

DISCOVERY = [
    {
        "layer": "startup_working_set",
        "scope": "MAIN-STATE.current_leaf_working_set only",
        "terms": ["swap23", "sigma23", "transposition 23", "A2_02 marking", "source-side action"],
        "result": "NO_LITERAL_SOURCE_BOUND_SWAP23_ACTION_LOCATOR_RETURNED",
    },
    {
        "layer": "repository_bounded_code_search",
        "scope": "GitHub default-branch bounded search under materially-new B2D signal",
        "terms": ["swap23", "swap_23", "sigma23", "transposition 23", "a2 a3 b2 b3", "A2_02 marking", "source-side action"],
        "result": "NO_LITERAL_SOURCE_BOUND_SWAP23_ACTION_LOCATOR_RETURNED",
    },
]


def csha(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def locked_embedded(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved: {path}: claimed={claimed} actual={actual}")
    return obj


def apply_tau(poly: dict[str, int]) -> dict[str, int]:
    out: dict[str, int] = {}
    for x, coeff in poly.items():
        y = TAU[x]
        out[y] = out.get(y, 0) + coeff
    return {k:v for k,v in out.items() if v}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    r2 = json.loads(R2.read_text(encoding="utf-8"))
    c3 = locked_embedded(C3, C3_SHA)

    if r2["swap23_action_requirements"]["cover_action_or_common_refinement_explicit"] is not True:
        raise SystemExit("R2 swap23 cover-action requirement moved")
    if r2["swap23_action_requirements"]["same_representative_transport_explicit"] is not True:
        raise SystemExit("R2 same-representative transport requirement moved")
    if r2["swap23_action_requirements"]["package_permutation_assumption_forbidden"] is not True:
        raise SystemExit("R2 package-permutation firewall moved")
    if c3["construction_status"]["swap23_cover_action_or_common_refinement_materialized"] is not False:
        raise SystemExit("C3 swap23 status moved")
    if c3["cover_index"]["total_chart_count"] != 317:
        raise SystemExit("C3 cover size moved")

    for x in COORDS:
        if TAU[TAU[x]] != x:
            raise SystemExit("target tau is not an involution")
    computed_action = {}
    for name, poly in QUADRICS.items():
        acted = apply_tau(poly)
        matches = [target for target, target_poly in QUADRICS.items() if acted == target_poly]
        if len(matches) != 1:
            raise SystemExit(f"target quadric action unresolved for {name}: {matches}")
        computed_action[name] = matches[0]
    if computed_action != EXPECTED_QUADRIC_ACTION:
        raise SystemExit(f"target quadric action moved: {computed_action}")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2d0.swap23_source_lock_bounded_negative.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2D0_SWAP23_SOURCE_LOCK_BOUNDED_NEGATIVE",
        "role": "EXACT_NONCREDIT_R5B2D0_TARGET_ACTION_PREFLIGHT_AND_BOUNDED_SOURCE_LOCK_NEGATIVE",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "parent_pr": 1684,
            "parent_merge_commit": "e6fd1aec8391c2e9a82eab45c3498afcec99ad44",
        },
        "source_locks": {
            "r2_contract_path": "stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json",
            "r2_contract_canonical_sha256": R2_SHA,
            "r5b2c3_path": "stages/stage33/33-12/e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json",
            "r5b2c3_canonical_sha256": C3_SHA,
        },
        "target_side_candidate": {
            "coordinate_order": COORDS,
            "tau_coordinate_map": TAU,
            "tau_squared_identity": True,
            "pinned_quadrics_square_term_coefficients": QUADRICS,
            "quadric_action": computed_action,
            "ambient_surface_automorphism_exact": True,
            "source_bound_a2_02_action_identification": False,
        },
        "bounded_discovery": {
            "policy": "docs/research-os/policies/repository-asset-discovery.md",
            "arsenal_index": "docs/arsenal/index.json",
            "cards": ["S33-PW04", "S33-PW07", "S33-PW08"],
            "queries": DISCOVERY,
            "literal_source_bound_swap23_action_locator_obtained": False,
            "repository_wide_absence_claim": False,
            "mathematical_nonexistence_claim": False,
            "search_miss_proves_repository_absence": False,
            "search_miss_proves_mathematical_nonexistence": False,
        },
        "exact_consequence": {
            "target_ambient_swap23_candidate_exact": True,
            "target_candidate_alone_satisfies_r2_source_transport_requirement": False,
            "r5b2c3_all_double_overlap_atlas_available": True,
            "r5b2d_cover_action_or_common_refinement_blocked": True,
            "blocker": BLOCKER,
        },
        "credit_firewall": {
            "source_bound_swap23_action": False,
            "a2_02_representative_transport": False,
            "cover_action_credit": False,
            "common_refinement_credit": False,
            "literal_mu2_2_cocycle_credit": False,
            "equivalent_unimodular_cech_glue_credit": False,
            "marked_brauer_credit": False,
            "h2_fixedness_credit": False,
            "authority_promotion": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
        "status": "BOUNDED_NEGATIVE_SOURCE_LOCK_PREFLIGHT_FAIL_CLOSED",
        "next_exact_leaf": "V91C1X_R5B2D1_LOCATE_OR_CONSTRUCT_LITERAL_SOURCE_BOUND_SWAP23_ACTION_OR_SOURCE_SIDE_MARKING_ADAPTER_THEN_BUILD_317_COVER_COMMON_REFINEMENT",
    }
    cert["canonical_sha256"] = csha(cert)
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": cert["candidate"],
        "certificate_sha256": cert["canonical_sha256"],
        "blocker": BLOCKER,
        "authority": AUTHORITY,
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
