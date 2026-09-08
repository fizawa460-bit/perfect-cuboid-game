#!/usr/bin/env python3
"""Replay EX5-00 Stage29 -> Stage32 receiver/population source lock.

This verifier checks source blobs and the typed population contract only.
It grants no receiver closure, route qualification, theorem, endpoint, or MAIN credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "ex5-00-source-lock-target-contract.json"


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    expected_canonical = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == expected_canonical, "artifact canonical SHA256 mismatch")

    require(data.get("schema") == "STAGE32EX5_EX5_00_SOURCE_LOCK_TARGET_CONTRACT_V1", "wrong schema")
    require(data.get("stage") == "32EX5", "wrong stage")
    require(data.get("leaf") == "EX5-00", "wrong leaf")
    require(data.get("status") == "EX5_00_SOURCE_LOCK_COMPLETE_UNAUDITED_RETAINED", "wrong status")

    for lock in data.get("source_locks", []):
        path = ROOT / lock["path"]
        require(path.exists(), f"missing source lock: {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift: {lock['path']}")

    kernel = data["kernel"]
    require(kernel["id"] == "K16-C2-LOWGENUS-PICARD-PRODUCTION", "wrong kernel")
    require(kernel["receiver_ids"] == ["R29-LG2", "R29-LG2-EFF", "R29-LG2-MB"], "receiver set drift")
    require(kernel["endpoint_decisive_alone"] is False, "kernel cannot become endpoint-decisive by contract")

    pop = data["unibranch_degree_population"]
    rows = [f"g0-d{d}" for d in range(2, 177, 2)] + [f"g1-d{d}" for d in range(4, 193, 2)]
    require(len(rows) == 183, "internal row construction mismatch")
    require(pop["geometric_genus_0"]["row_count"] == 88, "G0 row count mismatch")
    require(pop["geometric_genus_1"]["row_count"] == 95, "G1 row count mismatch")
    require(pop["frozen_genus_degree_row_count"] == 183, "frozen 183-row contract lost")
    require(pop["frozen_row_ids"] == rows, "frozen row IDs mismatch")
    require(
        pop["frozen_row_ids_sha256"]
        == hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest(),
        "frozen row checksum mismatch",
    )
    require(pop["numerical_census_is_effectivity"] is False, "numerical/effectivity firewall lost")
    require(pop["full_enumeration_completed"] is False, "EX5-00 cannot claim enumeration completion")

    eff = data["effectivity_population"]
    require(eff["receiver_id"] == "R29-LG2-EFF", "effectivity receiver mismatch")
    require(eff["necessary_intersection_filters_are_effectivity_proofs"] is False,
            "necessary filters cannot become effectivity proof")
    require(eff["effectivity_certified_for_all_survivors"] is False,
            "EX5-00 cannot claim effectivity completion")

    mb = data["multibranch_population"]
    require(mb["receiver_id"] == "R29-LG2-MB", "multibranch receiver mismatch")
    require(mb["covered_by_FSM_Theorem_3_1_bijective_normalization_cap"] is False,
            "multibranch must remain outside bijective-normalization cap")
    require(mb["silently_capped_by_unibranch_176_192_windows"] is False,
            "multibranch cannot inherit 176/192 cap silently")
    require(mb["ledger_complete"] is False, "EX5-00 cannot claim multibranch ledger completion")

    current = data["current_stage32_residual_context"]
    require(current["current_fixed_target_is_global_receiver_definition"] is False,
            "current fixed target cannot define all Stage32 receivers")
    require(current["V6_O210_Q602_is_one_current_branch_not_entire_receiver_population"] is True,
            "V6/O210/Q602 scope firewall lost")
    require(current["current_fixed_target"]["surviving_residues"] == [73, 97, 235],
            "current survivor context drift")

    closure = data["closure_boundaries"]
    for key in (
        "R29_LG2_discharged",
        "R29_LG2_EFF_discharged",
        "R29_LG2_MB_discharged",
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS",
        "STAGE32_CLOSED",
        "isolated_rational_points_excluded",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ):
        require(closure[key] is False, f"closure firewall must remain false: {key}")

    ex5 = data["ex5_contract"]
    require(ex5["typed_target_contract_complete"] is True, "EX5-00 target contract not complete")
    require(ex5["receiver_ledger_complete"] is False, "EX5-01 ledger cannot be pre-credited")
    require(ex5["next_leaf"] == "EX5-01_EXACT_RECEIVER_LEDGER_RECONSTRUCTION", "wrong next leaf")
    require(ex5["arsenal_or_existing_solution_discovery_performed"] is False,
            "EX5-00 must precede repository asset solution lookup")
    require(ex5["route_credit_granted"] is False, "EX5-00 grants no route credit")

    print("PASS: Stage32EX5 EX5-00 source lock / target receiver contract")


if __name__ == "__main__":
    main()
