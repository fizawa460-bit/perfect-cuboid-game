#!/usr/bin/env python3
"""Replay Stage32EX5 EX5-04 repository asset discovery/dedup.

The Arsenal machine registry is read runner-side because index.json exceeds the
chat-context whole-fetch threshold. This verifier proves only discovery/dedup
bookkeeping and exact source locking. It grants no mathematical route, receiver,
theorem, endpoint, or Stage32 MAIN credit.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex5-04-repository-asset-dedup.json"
EX503 = HERE / "ex5-03-clean-room-route-universe.json"
INDEX = ROOT / "docs/arsenal/index.json"


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


def collect_index_entries(data: dict) -> list[dict]:
    entries: list[dict] = []
    for item in data.get("selectors", []):
        entries.append({**item, "maturity": "FORMAL", "kind": "selector"})
    for item in data.get("formal_router_weapons", []):
        entries.append({**item, "maturity": "FORMAL", "kind": "weapon"})
    for item in data.get("formal_workflows", []):
        entries.append({**item, "maturity": "WORKFLOW", "kind": "workflow", "role": item.get("name", "")})
    for harvest in data.get("provisional_harvests", []):
        for card_id in harvest.get("active_cards", []):
            entries.append({
                "id": card_id,
                "role": harvest.get("card_roles", {}).get(card_id, ""),
                "summary": harvest.get("card_summaries", {}).get(card_id, ""),
                "path": harvest["path"],
                "maturity": "PROVISIONAL",
                "kind": "weapon",
                "source_stage": harvest["source_stage"],
            })
        for workflow_id in harvest.get("active_workflows", []):
            entries.append({
                "id": workflow_id,
                "role": harvest.get("workflow_roles", {}).get(workflow_id, ""),
                "summary": harvest.get("workflow_summaries", {}).get(workflow_id, ""),
                "path": harvest["path"],
                "maturity": "PROVISIONAL",
                "kind": "workflow",
                "source_stage": harvest["source_stage"],
            })
    return entries


def main() -> None:
    data = json.loads(ART.read_text(encoding="utf-8"))
    expected = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == expected, "EX5-04 canonical SHA256 mismatch")
    require(expected == "2d760161b10cbb16d95d995da01804c7d8a1f9a17a06cea826a00ea94fcbae6c",
            "unexpected EX5-04 canonical SHA256")
    require(data.get("schema") == "STAGE32EX5_EX5_04_REPOSITORY_ASSET_DEDUP_V1", "wrong schema")
    require(data.get("status") == "EX5_04_REPOSITORY_ASSET_DISCOVERY_DEDUP_COMPLETE_UNAUDITED_RETAINED",
            "wrong EX5-04 status")

    for lock in data["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift {lock['path']}")
        if "byte_size" in lock:
            require(path.stat().st_size == lock["byte_size"], f"source size drift {lock['path']}")
        if "canonical_sha256" in lock:
            obj = json.loads(path.read_text(encoding="utf-8"))
            stored = obj.pop("canonical_sha256_without_this_field")
            require(stored == lock["canonical_sha256"], f"stored canonical drift {lock['path']}")
            require(csha(obj) == stored, f"recomputed canonical drift {lock['path']}")

    inspect = data["inspection_contract"]
    for key in (
        "policy_read_before_registry",
        "arsenal_index_is_canonical_machine_registry",
        "context_safe_policy_triggered",
        "machine_registry_runner_side_validation_required",
        "compact_catalog_used_for_bounded_routing",
        "selected_generated_cards_only",
    ):
        require(inspect[key] is True, f"inspection contract lost: {key}")
    for key in (
        "arsenal_index_whole_fetched_into_chat",
        "repository_wide_search_miss_used_as_absence_proof",
        "asset_keyword_match_grants_applicability",
    ):
        require(inspect[key] is False, f"inspection firewall lost: {key}")
    require(INDEX.stat().st_size == inspect["arsenal_index_byte_size"] == 101763,
            "Arsenal index byte-size lock drift")

    registry = json.loads(INDEX.read_text(encoding="utf-8"))
    require(registry.get("registry_contract", {}).get("canonical_machine_registry") is True,
            "Arsenal index is not marked canonical machine registry")
    entries = collect_index_entries(registry)
    ids = [e["id"] for e in entries]
    require(len(ids) == len(set(ids)), "duplicate active Arsenal IDs")
    by_id = {e["id"]: e for e in entries}
    for expected_entry in data["selected_index_entries"]:
        cid = expected_entry["id"]
        require(cid in by_id, f"selected Arsenal ID missing from machine registry: {cid}")
        actual = by_id[cid]
        require(actual.get("role") == expected_entry["expected_role"], f"role drift for {cid}")
        require(actual.get("maturity") == expected_entry["expected_maturity"], f"maturity drift for {cid}")
        require(actual.get("kind") == expected_entry["expected_kind"], f"kind drift for {cid}")

    # Check source-card semantics that make the dedup labels falsifiable rather than keyword-only.
    card_text = {
        "S28-W04": (ROOT / "docs/arsenal/cards/formal/S28-W04.md").read_text(encoding="utf-8"),
        "S36-PW01": (ROOT / "docs/arsenal/cards/provisional/S36-PW01.md").read_text(encoding="utf-8"),
        "S30-W01": (ROOT / "docs/arsenal/cards/formal/S30-W01.md").read_text(encoding="utf-8"),
        "S30-W02": (ROOT / "docs/arsenal/cards/formal/S30-W02.md").read_text(encoding="utf-8"),
        "S32-PW01": (ROOT / "docs/arsenal/cards/provisional/S32-PW01.md").read_text(encoding="utf-8"),
        "S34-W03": (ROOT / "docs/arsenal/cards/formal/S34-W03.md").read_text(encoding="utf-8"),
    }
    require("STRICT_M6_SOURCE_TARGET_SEPARATION=false" in card_text["S28-W04"], "S28-W04 scope marker drift")
    require("Riemann-Hurwitz" in card_text["S36-PW01"] and "rational-point classification" in card_text["S36-PW01"],
            "S36-PW01 genus-inventory firewall drift")
    require("source-lock a common geometric/moduli/algebraic anchor" in card_text["S30-W01"],
            "S30-W01 semantic-anchor requirement drift")
    require("finite action descent => rational-point / global arithmetic existence" in card_text["S30-W02"],
            "S30-W02 descent firewall drift")
    require("rank`/`unrank" in card_text["S32-PW01"] and "EXACT_ENUMERATION_COMPRESSION_AND_INDEXER" in card_text["S32-PW01"],
            "S32-PW01 exact-enumeration identity drift")
    require("B(Q) intersect K(Q) = empty" in card_text["S34-W03"] and "receiver branch closed = allowed" in card_text["S34-W03"],
            "S34-W03 receiver-intersection contract drift")

    clean = json.loads(EX503.read_text(encoding="utf-8"))
    clean_routes = {r["route_id"]: r for r in clean["route_records"]}
    records = {r["route_id"]: r for r in data["dedup_records"]}
    require(set(records) == set(clean_routes), "EX5-04 must classify every EX5-03 route record exactly once")
    require(len(records) == 7, "dedup record count drift")

    allowed = {
        "NEW_ROUTE",
        "EXISTING_BUT_UNUSED_HERE",
        "EXISTING_WITH_MISSING_ADAPTER",
        "DUPLICATE_OF_MAIN_OR_EX1_EX4",
        "DOMINATED_BY_STRONGER_EXISTING_ROUTE",
        "NOT_APPLICABLE_TO_FROZEN_POPULATION",
    }
    require(all(r["classification"] in allowed for r in records.values()), "unknown dedup classification")
    counts = Counter(r["classification"] for r in records.values())
    require(dict(counts) == {k: v for k, v in data["dedup_contract"]["classification_counts"].items() if v},
            "dedup classification counts drift")

    require(records["EX5R-EFC-001"]["classification"] == "NEW_ROUTE", "EFC classification drift")
    require(records["EX5R-EHS-001"]["classification"] == "NEW_ROUTE", "EHS classification drift")
    require(records["EX5R-MOD-001"]["classification"] == "EXISTING_WITH_MISSING_ADAPTER", "MOD classification drift")
    require(records["EX5R-GAL-001"]["classification"] == "NOT_APPLICABLE_TO_FROZEN_POPULATION", "GAL classification drift")
    require(records["EX5R-GAL-001"]["nearest_asset_ids"] == ["S30-W02"], "GAL nearest asset drift")
    require(records["EX5R-ENUM-001"]["classification"] == "DUPLICATE_OF_MAIN_OR_EX1_EX4", "ENUM classification drift")
    require(records["EX5R-ENUM-001"]["nearest_asset_ids"] == ["S32-PW01"], "ENUM duplicate parent drift")
    require(records["EX5R-LGS-001"]["classification"] == "EXISTING_WITH_MISSING_ADAPTER", "LGS classification drift")
    require(records["EX5R-XSTAGE-001"]["classification"] == "EXISTING_WITH_MISSING_ADAPTER", "XSTAGE classification drift")
    require(records["EX5R-XSTAGE-001"]["bound_external_weapon"] == "S34-W03", "XSTAGE weapon binding drift")

    retained = sorted(rid for rid, r in records.items() if r["retained_for_EX5_05"])
    expected_retained = sorted(data["dedup_contract"]["deduplicated_executable_candidate_ids"])
    require(retained == expected_retained, "deduplicated executable candidate set drift")
    require(expected_retained == sorted(["EX5R-EFC-001","EX5R-EHS-001","EX5R-MOD-001","EX5R-LGS-001","EX5R-XSTAGE-001"]),
            "unexpected EX5-05 candidate set")
    require(data["dedup_contract"]["removed_or_rejected_ids"] == ["EX5R-GAL-001","EX5R-ENUM-001"],
            "removed/rejected route list drift")
    require(all(r["independent_route_credit"] is False for r in records.values()),
            "dedup record cannot grant independent route credit")

    ex5 = data["ex5_contract"]
    require(ex5["repository_asset_discovery_performed"] is True, "asset discovery not complete")
    require(ex5["arsenal_index_read_via_runner_side_machine_registry_validation"] is True,
            "machine registry validation flag lost")
    require(ex5["deduplication_performed"] is True and ex5["arsenal_dedup_complete"] is True,
            "dedup completion flag lost")
    require(ex5["next_leaf"] == "EX5-05_ROUTE_TYPING_PROOF_OBLIGATIONS_AND_SCORECARD",
            "wrong EX5-04 successor")
    for key in ("route_scorecard_complete","primary_route_selected","nontrivial_receiver_effect_obtained",
                "qualified_independent_route_established","route_credit_granted"):
        require(ex5[key] is False, f"EX5-04 pre-credits future state: {key}")

    for key, value in data["firewalls"].items():
        require(value is False, f"firewall must remain false: {key}")

    print("PASS: Stage32EX5 EX5-04 repository asset discovery/dedup")


if __name__ == "__main__":
    main()
