#!/usr/bin/env python3
"""Replay Stage32EX5 EX5-03 clean-room route universe.

This verifier proves only that the required route families were classified from
frozen EX5 receiver objects before asset lookup. It grants no route,
receiver, theorem, endpoint, or Stage32 MAIN credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "ex5-03-clean-room-route-universe.json"
LEDGER = HERE / "ex5-01-exact-receiver-ledger.json"

EXPECTED_FAMILIES = {
    "EFFECTIVE_CONE_FIXED_COMPONENT_LANE",
    "EQUGENERIC_HILBERT_SEVERI_LANE",
    "MODULAR_UNIFORMIZATION_LANE",
    "GALOIS_DESCENT_LANE",
    "EXACT_ENUMERATION_LANE",
    "LOCAL_GLOBAL_SINGULARITY_LANE",
    "CROSS_STAGE_WEAPON_IMPORT_LANE",
}
REQUIRED_ROUTE_FIELDS = {
    "route_id", "family", "status", "receiver_target_group_ids",
    "receiver_target", "population_adapter_basis", "proposed_new_input",
    "forward_implication", "future_falsifiable_unit",
    "future_success_predicate", "future_failure_or_block_predicate",
    "reverse_scope_firewall", "duplicate_key", "material_distinction_key",
    "arsenal_lookup_performed", "mathematical_credit",
}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    expected = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == expected, "artifact canonical SHA256 mismatch")
    require(expected == "3e1667d88fd6a2eb0baaf7473e67b3d9000066177231ae1a6bbffe7a17da87ff",
            "unexpected EX5-03 canonical SHA256")
    require(data["schema"] == "STAGE32EX5_EX5_03_CLEAN_ROOM_ROUTE_UNIVERSE_V1",
            "wrong schema")
    require(data["status"] ==
            "EX5_03_CLEAN_ROOM_CANDIDATE_UNIVERSE_FROZEN_UNAUDITED_RETAINED",
            "wrong status")

    locks = {x["id"]: x for x in data["source_locks"]}
    require(set(locks) == {"SRC-EX5-00", "SRC-EX5-01", "SRC-EX5-02", "SRC-ROADMAP"},
            "unexpected source-lock set")
    for lock in data["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            obj = json.loads(path.read_text(encoding="utf-8"))
            stored = obj.pop("canonical_sha256_without_this_field")
            require(stored == lock["canonical_sha256"], f"stored canonical drift {lock['path']}")
            require(csha(obj) == stored, f"recomputed canonical drift {lock['path']}")

    contract = data["generation_contract"]
    require(contract["candidate_universe_version"] == "EX5_CLEANROOM_CANDIDATES_V1",
            "candidate universe version drift")
    require(set(contract["required_families"]) == EXPECTED_FAMILIES,
            "required family set drift")
    require(contract["family_record_count"] == 7, "family record count drift")
    require(contract["generated_candidate_count"] == 6, "generated candidate count drift")
    require(contract["semantically_irrelevant_family_count"] == 1,
            "semantic irrelevance count drift")
    for key in ("all_required_families_classified",
                "generated_from_frozen_receiver_objects_before_asset_lookup",
                "duplicate_classification_deferred_to_EX5_04"):
        require(contract[key] is True, f"generation contract must be true: {key}")
    for key in ("repository_asset_discovery_performed", "arsenal_index_read",
                "existing_solution_lookup_performed", "route_qualification_credit_granted"):
        require(contract[key] is False, f"EX5-03 pre-asset firewall lost: {key}")

    routes = data["route_records"]
    require(len(routes) == 7, "must classify exactly seven route families")
    require(len({r["route_id"] for r in routes}) == 7, "route IDs not unique")
    require({r["family"] for r in routes} == EXPECTED_FAMILIES,
            "one record per required family not satisfied")
    for route in routes:
        require(REQUIRED_ROUTE_FIELDS <= set(route), f"missing route fields {route.get('route_id')}")
        require(route["receiver_target_group_ids"], f"empty receiver target {route['route_id']}")
        require(route["population_adapter_basis"], f"empty population adapter basis {route['route_id']}")
        require(route["proposed_new_input"].strip(), f"empty proposed input {route['route_id']}")
        require(route["forward_implication"].strip(), f"empty implication {route['route_id']}")
        require(route["future_falsifiable_unit"].strip(), f"empty falsifiable unit {route['route_id']}")
        require(route["reverse_scope_firewall"], f"empty reverse firewall {route['route_id']}")
        require(route["arsenal_lookup_performed"] is False,
                f"Arsenal lookup occurred during clean room: {route['route_id']}")
        require(route["mathematical_credit"] is False,
                f"candidate generation cannot grant math credit: {route['route_id']}")

    statuses = [r["status"] for r in routes]
    require(statuses.count("GENERATED_CANDIDATE") == 5,
            "five ordinary generated candidates expected")
    require(statuses.count("GENERATED_CANDIDATE_INPUT_UNBOUND") == 1,
            "one unbound cross-stage candidate expected")
    require(statuses.count("SEMANTICALLY_IRRELEVANT_PURE_Q_DESCENT") == 1,
            "one pure-Q descent semantic rejection expected")

    by_family = {r["family"]: r for r in routes}
    gal = by_family["GALOIS_DESCENT_LANE"]
    require(gal["status"] == "SEMANTICALLY_IRRELEVANT_PURE_Q_DESCENT",
            "pure Q-descent classification drift")
    require("no Q-rationality restriction" in gal["receiver_target"],
            "Galois rejection must cite geometric/no-Q receiver semantics")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    require("no Q-rationality restriction" in ledger["semantics_legend"]["FM-GEO-S"],
            "frozen ledger no-Q semantics drift")

    enum = by_family["EXACT_ENUMERATION_LANE"]
    require(enum["status"] == "GENERATED_CANDIDATE", "enumeration candidate missing")
    require(data["firewalls"]["exact_enumeration_candidate_is_assumed_independent_of_main"] is False,
            "EX5-04 dedup cannot be pre-credited")
    xstage = by_family["CROSS_STAGE_WEAPON_IMPORT_LANE"]
    require(xstage["status"] == "GENERATED_CANDIDATE_INPUT_UNBOUND",
            "cross-stage candidate must remain unbound before asset discovery")

    dup_keys = [r["duplicate_key"] for r in routes]
    material_keys = [r["material_distinction_key"] for r in routes]
    require(len(set(dup_keys)) == 7, "duplicate keys collide inside clean-room universe")
    require(len(set(material_keys)) == 7, "material distinction keys collide")
    dup = data["duplicate_contract"]
    require(dup["duplicate_keys_unique_within_clean_room_set"] is True,
            "duplicate uniqueness flag lost")
    require(dup["material_distinction_keys_unique_within_clean_room_set"] is True,
            "material distinction uniqueness flag lost")

    ex5 = data["ex5_contract"]
    require(ex5["clean_room_candidate_universe_frozen"] is True,
            "clean-room universe not frozen")
    require(ex5["next_leaf"] == "EX5-04_REPOSITORY_ASSET_DISCOVERY_AND_DEDUPLICATION",
            "wrong EX5-03 successor")
    require(ex5["asset_discovery_now_authorized_by_leaf"] is True,
            "EX5-04 asset discovery authorization missing")
    for key in ("route_scorecard_complete", "primary_route_selected",
                "nontrivial_receiver_effect_obtained",
                "qualified_independent_route_established", "route_credit_granted"):
        require(ex5[key] is False, f"future EX5 credit pre-granted: {key}")

    for key, value in data["firewalls"].items():
        require(value is False, f"firewall must remain false: {key}")

    print("PASS: Stage32EX5 EX5-03 clean-room universe (7 families = 6 candidates + 1 semantic rejection)")


if __name__ == "__main__":
    main()
