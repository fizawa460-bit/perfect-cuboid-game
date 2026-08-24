#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

RAW_SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_BRANCH_SHARD_V1"
OUT_SCHEMA = "STAGE32_D8_E20_A0_MATERIALIZED_CELL_SHARD_COMPACT_CERT_V1"


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    row = json.loads(args.input.read_text())
    assert row["schema"] == RAW_SCHEMA
    p = row["parameters"]
    assert int(p["degree"]) == 8 and int(p["genus"]) == 0
    assert int(p["exceptional_mass"]) == 20 and int(p["curve_group_mass"]) == 0
    shard_index = int(p["shard_index"])
    shard_count = int(p["shard_count"])
    assert shard_count == 2
    assert p["branch_partition"] == "GLOBAL_BRANCH_INDEX_MOD_SHARD_COUNT"

    m = row["materialization"]
    total = int(m["total_parent_cell_branch_count"])
    want = expected_mod_count(total, shard_count, shard_index)
    assert int(m["expected_shard_branch_count"]) == want
    assert int(m["executed_shard_branch_count"]) == want
    assert row["complete_shard_numerical_enumeration"] is True
    assert row["solver_result"] in ("SHARD_UNSAT", "SHARD_SAT_EXHAUSTED")
    assert row["theorem_credit"] is False and row["receiver_credit"] is False
    assert row["FULL_D8_G0_ROW_COMPLETE"] is False
    assert row["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is False
    assert row["R29_LG2_NUMERICAL_COMPONENT_COMPLETE"] is False
    assert row["R29_LG2"] == "NOT_DISCHARGED"
    assert row["R29_LG2_EFF"] == "NOT_DISCHARGED"
    assert row["R29_LG2_MB"] == "NOT_DISCHARGED"
    assert row["G10_LOWGENUS_PICARD"] == "AMBER"

    branches = row["branches"]
    assert len(branches) == want
    branch_digest = hashlib.sha256()
    index_digest = hashlib.sha256()
    node_count = interval_reject = form_prune = leaf_count = 0
    branch_survivors: list[dict[str, Any]] = []
    expected_index = shard_index

    for branch in branches:
        idx = int(branch["branch_index"])
        assert idx == expected_index and 0 <= idx < total
        expected_index += shard_count
        search = branch["search"]
        assert search["complete_numerical_enumeration"] is True
        assert search["enumeration_exhausted"] is True
        assert search["node_budget_exhausted"] is False
        assert search["solver_result"] in ("UNSAT", "SAT_EXHAUSTED", "UNSAT_RADIUS")
        node_count += int(search["enumeration_node_count"])
        interval_reject += int(search["interval_rejection_count"])
        form_prune += int(search["intersection_bound_prune_count"])
        leaf_count += int(search["checked_leaf_count"])
        branch_survivors.extend(search["survivors"])

        leaf = {
            "branch_index": idx,
            "exceptional_coordinates_sha256": branch["exceptional_coordinates_sha256"],
            "qhead_coordinates": branch["qhead_coordinates"],
            "base_certificate_sha256": csha(branch["base_certificate"]),
            "solver_result": search["solver_result"],
            "enumeration_node_count": int(search["enumeration_node_count"]),
            "checked_leaf_count": int(search["checked_leaf_count"]),
            "exact_survivor_count": int(search["exact_survivor_count"]),
            "enumeration_transcript_sha256": search["enumeration_transcript_sha256"],
            "survivor_basis_shas": [s["basis_coordinates_sha256"] for s in search["survivors"]],
        }
        branch_digest.update(json.dumps(leaf, sort_keys=True, separators=(",", ":")).encode())
        branch_digest.update(b"\n")
        index_digest.update(f"{idx}\n".encode())

    assert expected_index >= total
    branch_survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
    raw_survivors = sorted(row["numerical_survivors"], key=lambda r: tuple(r["basis_coordinates"]))
    assert branch_survivors == raw_survivors
    keys = [tuple(r["basis_coordinates"]) for r in raw_survivors]
    assert len(keys) == len(set(keys))
    assert int(row["exact_numerical_survivor_count_in_shard"]) == len(raw_survivors)

    report = {
        "schema": OUT_SCHEMA,
        "source_raw_schema": RAW_SCHEMA,
        "source_raw_deterministic_sha256": row["deterministic_sha256_without_runtime"],
        "algorithm_id": row["algorithm_id"],
        "parameters": dict(p),
        "signature_cell_inventory_sha256": row["signature_cell_inventory_sha256"],
        "signature_cell_sha256": csha(row["signature_cell"]),
        "shared_context_certificate_sha256": csha(row["shared_context"]),
        "parent_cell_total_branch_count": total,
        "executed_shard_branch_count": want,
        "first_branch_index": shard_index if want else None,
        "last_branch_index": (shard_index + (want - 1) * shard_count) if want else None,
        "branch_index_sequence_sha256": index_digest.hexdigest(),
        "branch_exact_evidence_stream_sha256": branch_digest.hexdigest(),
        "all_branch_indices_exact_mod_partition": True,
        "all_branches_complete": True,
        "unknown_branch_count": 0,
        "total_search_nodes": node_count,
        "total_interval_rejections": interval_reject,
        "total_intersection_bound_prunes": form_prune,
        "total_checked_leaves": leaf_count,
        "exact_numerical_survivor_count_in_shard": len(raw_survivors),
        "numerical_survivors": raw_survivors,
        "raw_branch_rows_persisted": False,
        "compaction_is_post_verification_only": True,
        "effectivity_classification_complete": False,
        "actual_curve_existence_claim": False,
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "FULL_D8_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = csha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "cell": int(p["cell_index"]),
        "shard": shard_index,
        "branches": want,
        "survivors": len(raw_survivors),
        "raw_sha": row["deterministic_sha256_without_runtime"],
        "compact_sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
