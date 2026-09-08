#!/usr/bin/env python3
"""Replay Stage32EX5 EX5-02 current coverage/dependency graph.

This proves graph coverage/topology only. It does not discharge any receiver,
qualify a route, or grant Stage32 MAIN/theorem/endpoint credit.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
GRAPH = HERE / "ex5-02-current-coverage-dependency-graph.json"
LEDGER = HERE / "ex5-01-exact-receiver-ledger.json"
ACTIVE = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"


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
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    expected = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == expected, "graph canonical SHA256 mismatch")
    require(expected == "36f782aa6948b0e43a7bfc3d812ff43079051c871ab4e92c63056fbb6159d1bc",
            "unexpected graph canonical SHA256")
    require(data.get("schema") == "STAGE32EX5_EX5_02_CURRENT_COVERAGE_DEPENDENCY_GRAPH_V1",
            "wrong graph schema")
    require(data.get("status") == "EX5_02_CURRENT_COVERAGE_DEPENDENCY_GRAPH_COMPLETE_UNAUDITED_RETAINED",
            "wrong EX5-02 status")

    for lock in data["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            obj = json.loads(path.read_text(encoding="utf-8"))
            stored = obj.pop("canonical_sha256_without_this_field")
            require(stored == lock["canonical_sha256"], f"stored canonical drift {lock['path']}")
            require(csha(obj) == stored, f"recomputed canonical drift {lock['path']}")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    open_rows = [r["ledger_row_id"] for r in ledger["receiver_rows"] if r["current_status"] == "OPEN"]
    closed_rows = [r["ledger_row_id"] for r in ledger["receiver_rows"] if r["current_status"] == "CLOSED"]
    require(len(open_rows) == 180, "ledger open-row count drift")
    require(len(closed_rows) == 5, "ledger closed-row count drift")

    groups = data["primary_receiver_groups"]
    mapped = [rid for g in groups for rid in g["ledger_row_ids"]]
    require(len(mapped) == 180, "primary mapping count mismatch")
    require(Counter(mapped) == Counter(open_rows), "open rows are not mapped exactly once")
    require(len(set(mapped)) == 180, "duplicate primary receiver mapping")

    by_group = {g["group_id"]: g for g in groups}
    require(by_group["GRP-NUM-178"]["row_count"] == 178, "numerical group count drift")
    require(by_group["GRP-EFF-1"]["ledger_row_ids"] == ["R29-LG2-EFF::ALL_NUMERICAL_SURVIVORS"],
            "effectivity meta receiver drift")
    require(by_group["GRP-MB-1"]["ledger_row_ids"] == ["R29-LG2-MB::MULTIBRANCH_AT_NODE_LOWGENUS"],
            "multibranch meta receiver drift")

    interfaces = {x["interface_id"]: x for x in data["interface_nodes"]}
    blockers = {x["blocker_id"]: x for x in data["blocker_nodes"]}
    require(interfaces["IF-NUM-FULL178"]["blocker_id"] == "BLK-FULL178-NUMERICAL-CENSUS",
            "numerical interface/blocker drift")
    require(blockers["BLK-FULL178-NUMERICAL-CENSUS"]["primary_receiver_row_count"] == 178,
            "numerical blocker multiplicity drift")
    require(blockers["BLK-EFFECTIVITY-DISPOSAL"]["primary_receiver_row_count"] == 1,
            "effectivity blocker multiplicity drift")
    require(blockers["BLK-MULTIBRANCH-LEDGER"]["primary_receiver_row_count"] == 1,
            "multibranch blocker multiplicity drift")

    overlay = data["special_overlays"]
    require(len(overlay) == 1, "special overlay count drift")
    require(overlay[0]["ledger_row_id"] == "R29-LG2::g1-d186", "V6 overlay row drift")
    require(overlay[0]["primary_mapping_remains"] == "IF-NUM-FULL178",
            "V6 overlay cannot replace numerical primary mapping")

    active = json.loads(ACTIVE.read_text(encoding="utf-8"))
    claims = {c["claim_id"]: c for c in active["claims"]}
    special = interfaces["IF-V6-O210-Q602-SPECIAL"]
    for cid in special["claim_refs"]:
        require(cid in claims, f"special overlay references unknown active-frontier claim {cid}")
    surv = claims["S32.Q602.SURVIVORS_73_97_235.V1"]
    require(surv["authority_status"] == "AUDITED" and surv["frontier_status"] == "AUDITED_TRUE",
            "Q602 survivor audited status drift")
    require(surv["scope"]["surviving_residues"] == [73, 97, 235], "Q602 survivor set drift")

    coverage = data["coverage_contract"]
    require(coverage["primary_open_mapping_exact_once"] is True, "primary coverage flag lost")
    require(coverage["unmapped_open_rows"] == 0, "unmapped open rows")
    require(coverage["duplicate_primary_mappings"] == 0, "duplicate primary mappings")
    require(coverage["v6_overlay_replaces_primary_mapping"] is False, "V6 overlay scope firewall lost")

    dep = data["dependency_graph"]
    require(dep["all_open_rows_have_primary_path_to_named_blocker"] is True,
            "not every open row has a named blocker path")
    require(dep["v6_current_branch_is_global_receiver_definition"] is False,
            "V6 branch cannot define global receiver")
    require(dep["numerical_census_is_effectivity"] is False,
            "numerical census cannot become effectivity")
    require(dep["unibranch_cap_covers_multibranch"] is False,
            "unibranch cap cannot cover multibranch")

    ex5 = data["ex5_contract"]
    require(ex5["current_coverage_dependency_graph_complete"] is True, "EX5-02 not complete")
    require(ex5["next_leaf"] == "EX5-03_CLEAN_ROOM_MATERIALLY_DISTINCT_ROUTE_GENERATION",
            "wrong EX5-02 successor")
    require(ex5["arsenal_or_existing_solution_discovery_performed"] is False,
            "EX5-02 must precede Arsenal solution lookup")
    require(ex5["route_credit_granted"] is False, "EX5-02 grants no route credit")

    print("PASS: Stage32EX5 EX5-02 current coverage/dependency graph")


if __name__ == "__main__":
    main()
