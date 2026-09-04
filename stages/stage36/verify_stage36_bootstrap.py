#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"

EXPECTED_BASE_MAIN = "c20ee71d91af850103fd7406f9b1072448a11fcf"
EXPECTED_SOURCES = {
    "stage29_active_kernel_ledger": (
        "stages/stage29/29-16/active-kernel-ledger.json",
        "5d6d4c7709b57064aea5dc0ece672c5170c39550",
    ),
    "stage29_endpoint_hub_graph": (
        "stages/stage29/29-06/endpoint-hub-graph.json",
        "7ea59474767f81fbaa4837c8cbc94b535560617b",
    ),
    "stage29_campedelli_route_contract": (
        "stages/stage29/29-02hb/route-contract.json",
        "75045d8f15786836e8a7383fc07ef95161fa86e7",
    ),
    "stage29_campedelli_arithmetic_routing": (
        "stages/stage29/29-02hb/arithmetic-routing.md",
        "ff83f652e2c9e95b0670c0964b9c8cf0fbccd696",
    ),
    "stage29_campedelli_quotient_adapter": (
        "stages/stage29/29-02hb/campedelli-quotient-adapter.md",
        "5f959d60106243bb31df06a3961ab04182d78fc7",
    ),
    "stage29_campedelli_source_lock": (
        "stages/stage29/29-02hb/source-lock.md",
        "713f22bb1347b8c6d5f8b32bfc2a24b3ce8b2e5d",
    ),
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    state = json.loads(STATE_PATH.read_text())

    require(
        state.get("schema") == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V1_INITIAL",
        "Stage36 bootstrap schema moved",
    )
    require(state.get("stage") == "36", "Stage36 number moved")
    require(state.get("status") == "PLANNED_NOT_STARTED", "Stage36 started before bootstrap audit")
    require(state.get("base_main_sha") == EXPECTED_BASE_MAIN, "Stage36 bootstrap base-main lock moved")

    kernel = state.get("source_kernel", {})
    require(kernel.get("kernel") == "K16-C3-CAMPEDELLI-UNIFORM-TORSOR", "source kernel moved")
    require(kernel.get("execution_class") == 3, "execution class moved")
    require(kernel.get("children") == ["R29-CAMP2"], "source receiver moved")
    require(kernel.get("parent_routes") == ["Q11-CAMPEDELLI"], "parent route moved")
    require(kernel.get("endpoint_decision_capable") is True, "endpoint-decision capability moved")

    locks = state.get("source_locks", {})
    require(set(locks) == set(EXPECTED_SOURCES), "Stage36 source-lock key set moved")
    for key, (rel, expected_sha) in EXPECTED_SOURCES.items():
        row = locks[key]
        require(row.get("path") == rel, f"source path moved: {key}")
        require(row.get("blob_sha") == expected_sha, f"declared source blob moved: {key}")
        got = git_blob_sha(ROOT / rel)
        require(got == expected_sha, f"source blob mismatch: {rel}: {got} != {expected_sha}")

    frontier = state.get("audited_frontier", {})
    expected_frontier = {
        "ten_Q_defined_kernels": True,
        "H_group": "(Z/2)^3",
        "canonical_quotient_degree": 8,
        "resolved_etale_quotient_degree": 8,
        "certified_Q_symmetry_orbit_sizes": [6, 2, 2],
        "geometric_Qi_orbit_sizes": [8, 2],
        "exact_Q_isomorphism_class_count_proved": False,
        "execution_representative_count": 3,
        "endpoint_to_every_audited_quotient_Q_point_push": True,
        "quotient_Q_point_implies_endpoint_Q_point": False,
        "H1_without_ramification_is_finite": False,
    }
    require(frontier == expected_frontier, "imported Stage29 Campedelli frontier moved")

    current = state.get("current", {})
    require(current.get("unit") == "36-01", "current unit moved")
    require(
        current.get("next_exact_leaf") == "36-01_SOURCE_AUTHORITY_LOCK",
        "Stage36 next exact leaf moved",
    )
    require(current.get("next_owner") == "STAGE36_MAIN", "Stage36 owner moved")
    require(state.get("completed_units") == {}, "36-01 or later work started before bootstrap audit")

    expected_working_set = [rel for rel, _ in EXPECTED_SOURCES.values()]
    require(
        state.get("current_leaf_working_set") == expected_working_set,
        "Stage36 bootstrap working set moved",
    )

    gates = state.get("promotion_gates", {})
    require(gates, "promotion_gates missing")
    require(all(value is False for value in gates.values()), "a Stage36 promotion/closure gate is already true")

    claims = state.get("claims", {})
    require(claims, "claims missing")
    require(all(value is False for value in claims.values()), "a Stage36 credit/closure claim is already true")

    sibling = state.get("sibling_interfaces", {}).get("K16-C2-BRAUER-EXPLICIT-CHAIN", {})
    require(sibling.get("receiver") == "R29-CAMP4", "Campedelli sibling receiver moved")
    require(sibling.get("relationship") == "SIBLING_ASSET_PROVIDER_ONLY", "Campedelli sibling relation moved")
    require(sibling.get("automatic_authority_merge") is False, "sibling authority auto-merge enabled")
    require(sibling.get("automatic_R29_CAMP2_closure") is False, "sibling auto-closure enabled")

    for rel in [
        "stages/stage36/ROADMAP.md",
        "stages/stage36/MAIN-START-HERE.md",
        "stages/stage36/MAIN-BATCH-HANDOFF.md",
    ]:
        require((ROOT / rel).exists(), f"missing Stage36 bootstrap file: {rel}")

    print("PASS STAGE36_BOOTSTRAP_AUTHORITY_CI_V1")
    print("next_exact_leaf=36-01_SOURCE_AUTHORITY_LOCK")
    print("source_blob_locks=6")
    print("frontier=10 kernels; Q symmetry 6+2+2; H=(Z/2)^3; endpoint->quotient only")
    print("all promotion gates and claims remain false; 36-01 not started")


if __name__ == "__main__":
    main()
