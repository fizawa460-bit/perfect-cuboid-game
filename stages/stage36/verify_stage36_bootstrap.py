#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
INITIAL_BASE = "c20ee71d91af850103fd7406f9b1072448a11fcf"
SUCCESSOR_BASE = "5ed32fa53bdecb735f461d7c27e85851d9ad8c21"
SOURCES = {
    "stage29_active_kernel_ledger": ("stages/stage29/29-16/active-kernel-ledger.json", "5d6d4c7709b57064aea5dc0ece672c5170c39550"),
    "stage29_endpoint_hub_graph": ("stages/stage29/29-06/endpoint-hub-graph.json", "7ea59474767f81fbaa4837c8cbc94b535560617b"),
    "stage29_campedelli_route_contract": ("stages/stage29/29-02hb/route-contract.json", "75045d8f15786836e8a7383fc07ef95161fa86e7"),
    "stage29_campedelli_arithmetic_routing": ("stages/stage29/29-02hb/arithmetic-routing.md", "ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_campedelli_source_lock": ("stages/stage29/29-02hb/source-lock.md", "713f22bb1347b8c6d5f8b32bfc2a24b3ce8b2e5d"),
}
FRONTIER = {
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


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    require(state.get("stage") == "36", "Stage36 number moved")
    schema = state.get("schema")
    require(schema in {
        "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V1_INITIAL",
        "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V2_36_01_PENDING_AUDIT",
    }, "unrecognized Stage36 bootstrap successor schema")

    k = state.get("source_kernel", {})
    require(k.get("kernel") == "K16-C3-CAMPEDELLI-UNIFORM-TORSOR", "source kernel moved")
    require(k.get("execution_class") == 3, "execution class moved")
    require(k.get("children") == ["R29-CAMP2"], "source receiver moved")
    require(k.get("parent_routes") == ["Q11-CAMPEDELLI"], "parent route moved")
    require(k.get("endpoint_decision_capable") is True, "endpoint capability moved")

    expected_locks = {key: {"path": rel, "blob_sha": sha} for key, (rel, sha) in SOURCES.items()}
    require(state.get("source_locks") == expected_locks, "source-lock set moved")
    for key, (rel, sha) in SOURCES.items():
        require(blob_sha(ROOT / rel) == sha, f"source blob mismatch: {key}")
    require(state.get("audited_frontier") == FRONTIER, "imported Stage29 Campedelli frontier moved")

    sib = state.get("sibling_interfaces", {}).get("K16-C2-BRAUER-EXPLICIT-CHAIN", {})
    require(sib.get("receiver") == "R29-CAMP4", "Campedelli sibling receiver moved")
    require(sib.get("relationship") == "SIBLING_ASSET_PROVIDER_ONLY", "Campedelli sibling relation moved")
    require(sib.get("automatic_authority_merge") is False, "sibling auto-merge enabled")
    require(sib.get("automatic_R29_CAMP2_closure") is False, "sibling auto-close enabled")
    require(all(v is False for v in state.get("claims", {}).values()), "Stage36 higher credit is true")

    current = state.get("current", {})
    require(current.get("unit") == "36-01", "current unit moved past 36-01")
    require(current.get("next_exact_leaf") == "36-01_SOURCE_AUTHORITY_LOCK", "36-02 started before audit")
    require(all(v is False for v in state.get("promotion_gates", {}).values()), "promotion gate true before audit")

    if schema == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V1_INITIAL":
        require(state.get("status") == "PLANNED_NOT_STARTED", "initial status moved")
        require(state.get("base_main_sha") == INITIAL_BASE, "initial base lock moved")
        require(state.get("completed_units") == {}, "36-01 started in initial schema")
        print("PASS STAGE36_BOOTSTRAP_AUTHORITY_CI_V1_INITIAL")
    else:
        require(state.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT", "36-01 successor status moved")
        require(state.get("base_main_sha") == SUCCESSOR_BASE, "36-01 successor base lock moved")
        unit = state.get("completed_units", {}).get("36-01", {})
        require(unit.get("status") == "EXACT_SOURCE_FRONTIER_LOCK_PENDING_HOSTILE_AUDIT", "36-01 successor status moved")
        require(unit.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-01 prematurely promoted")
        require(current.get("provisional_successor_after_hostile_audit") == "36-02_THREE_Q_REPRESENTATIVE_INVENTORY", "36-02 successor moved")
        print("PASS STAGE36_BOOTSTRAP_AUTHORITY_CI_V1_SUCCESSOR_SAFE")

    for rel in ["stages/stage36/ROADMAP.md", "stages/stage36/MAIN-START-HERE.md", "stages/stage36/MAIN-BATCH-HANDOFF.md"]:
        require((ROOT / rel).exists(), f"missing Stage36 bootstrap file: {rel}")
    print("source_blob_locks=6")
    print("frontier=10 kernels; Q symmetry 6+2+2; H=(Z/2)^3; endpoint->quotient only")
    print("no route/theorem/endpoint/perfect-cuboid credit")


if __name__ == "__main__":
    main()
