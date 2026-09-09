#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from filtered_survivor_execution_adapter import FilteredSurvivorExecutionAdapter

LEAF_CONTRACT = "N240_TEST_LEAF_CONTRACT_NO_NUMERICAL_CREDIT_V1"


def expect_fail(fn, label: str) -> None:
    try:
        fn()
    except (ValueError, AssertionError, KeyError):
        return
    raise AssertionError(f"expected failure did not occur: {label}")


def exhaustive_old_partition(adapter: FilteredSurvivorExecutionAdapter) -> dict:
    seen_filtered = []
    rejected = 0
    for old_rank in range(adapter.old_terminal_count):
        disposition = adapter.disposition_of_old_rank(old_rank)
        if disposition["disposition"] == "N220_REJECTED":
            rejected += 1
        else:
            filtered_rank = int(disposition["filtered_rank"])
            replay = adapter.replay_filtered_rank(filtered_rank)
            if replay["old_rank"] != old_rank:
                raise AssertionError("old/filtered exhaustive replay mismatch")
            seen_filtered.append(filtered_rank)
    if rejected != adapter.n220_rejected_terminal_count:
        raise AssertionError("exhaustive rejected count mismatch")
    if seen_filtered != list(range(adapter.filtered_terminal_count)):
        raise AssertionError("filtered survivor ranks are not exact order-preserving cover")
    return {
        "old_terminal_count": adapter.old_terminal_count,
        "rejected": rejected,
        "survivors": len(seen_filtered),
        "exact_old_partition_replay": True,
    }


def planned_cover_test(adapter: FilteredSurvivorExecutionAdapter, chunk_size: int) -> dict:
    count = adapter.planned_work_unit_count(chunk_size)
    units = [adapter.planned_work_unit(i, chunk_size) for i in range(count)]
    cert = adapter.validate_planned_cover(units)
    if units:
        bad = copy.deepcopy(units)
        bad[0]["work_unit_id"] = "0" * 64
        expect_fail(lambda: adapter.validate_planned_cover(bad), "bad work_unit_id")
        if len(units) >= 2:
            bad = copy.deepcopy(units)
            bad[1]["filtered_rank_lo"] += 1
            body = {k: v for k, v in bad[1].items() if k != "work_unit_id"}
            # A stale digest must fail before the gap can receive any credit.
            expect_fail(lambda: adapter.validate_planned_cover(bad), "gap/stale digest")
    return cert


def validator_mechanics_test(adapter: FilteredSurvivorExecutionAdapter, chunk_size: int) -> dict:
    """Unit-test the COMPLETE-cover validator with explicit synthetic records.

    These records are validator fixtures only and are never emitted as numerical
    evidence or retained leaf results.
    """
    count = adapter.planned_work_unit_count(chunk_size)
    records = []
    for i in range(count):
        unit = adapter.planned_work_unit(i, chunk_size)
        width = int(unit["filtered_rank_hi"]) - int(unit["filtered_rank_lo"])
        fixture_digest = hashlib.sha256(f"fixture:{unit['work_unit_id']}".encode()).hexdigest()
        records.append({
            "work_unit": unit,
            "state": "COMPLETE",
            "unknown_count": 0,
            "resource_wall_count": 0,
            "registered_exact_leaf_disposition_count": width,
            "leaf_disposition_commitment_sha256": fixture_digest,
            "test_fixture_only": True,
        })
    cert = adapter.validate_complete_execution_cover(records)
    if records:
        bad = copy.deepcopy(records)
        bad[0]["unknown_count"] = 1
        expect_fail(lambda: adapter.validate_complete_execution_cover(bad), "unknown fail-closed")
        bad = copy.deepcopy(records)
        bad[0]["registered_exact_leaf_disposition_count"] -= 1
        expect_fail(lambda: adapter.validate_complete_execution_cover(bad), "leaf-count fail-closed")
    return {
        "validator_fixture_only": True,
        "accepted_fixture_record_count": len(records),
        "validator_mechanics_pass": True,
        "no_numerical_credit": True,
        "certificate_shape_sha256": cert["canonical_sha256"],
    }


def large_random_access(adapter: FilteredSurvivorExecutionAdapter, chunk_size: int) -> dict:
    cert = adapter.partition_certificate()
    count = adapter.planned_work_unit_count(chunk_size)
    unit_samples = []
    if count:
        for i in sorted({0, count // 2, count - 1}):
            unit = adapter.planned_work_unit(i, chunk_size)
            adapter.verify_work_unit(unit)
            unit_samples.append({
                "index": i,
                "lo": unit["filtered_rank_lo"],
                "hi": unit["filtered_rank_hi"],
                "work_unit_id": unit["work_unit_id"],
            })
    rank_samples = []
    if adapter.filtered_terminal_count:
        for rank in sorted({0, adapter.filtered_terminal_count // 2, adapter.filtered_terminal_count - 1}):
            replay = adapter.replay_filtered_rank(rank)
            rank_samples.append({"filtered_rank": rank, "old_rank": replay["old_rank"]})
    return {
        "row_id": adapter.row_id,
        "e": adapter.e,
        "old_terminal_count": cert["old_stratum_terminal_count"],
        "filtered_terminal_count": cert["filtered_terminal_count"],
        "n220_rejected_terminal_count": cert["n220_rejected_terminal_count"],
        "planned_work_unit_count": count,
        "unit_samples": unit_samples,
        "rank_samples": rank_samples,
        "materialized_full_population": False,
    }


def main() -> None:
    small_cases = []
    expected = {
        (1, 8, 4): (36575, 35644),
        (1, 8, 5): (102912, 102528),
    }
    for key, (old_expected, filtered_expected) in expected.items():
        adapter = FilteredSurvivorExecutionAdapter(*key, leaf_contract_rev=LEAF_CONTRACT)
        if adapter.old_terminal_count != old_expected or adapter.filtered_terminal_count != filtered_expected:
            raise AssertionError(f"retained count regression: {key}")
        exhaustive = exhaustive_old_partition(adapter)
        plan = planned_cover_test(adapter, 4096)
        validator = validator_mechanics_test(adapter, 8192)
        small_cases.append({
            "g": key[0], "d": key[1], "e": key[2],
            "exhaustive": exhaustive,
            "planned_cover": plan,
            "validator": validator,
        })

    large_cases = []
    for key in ((0, 100, 29), (0, 176, 50), (0, 176, 100)):
        adapter = FilteredSurvivorExecutionAdapter(*key, leaf_contract_rev=LEAF_CONTRACT)
        large_cases.append(large_random_access(adapter, 1_000_000_000))

    result = {
        "verdict": "PASS_N240_FILTERED_EXECUTION_COMPLETENESS_ADAPTER_REPLAY",
        "small_exhaustive_old_partition_cases": small_cases,
        "large_nonmaterializing_random_access_cases": large_cases,
        "old_canonical_rank_remains_completeness_authority": True,
        "filtered_rank_secondary_execution_only": True,
        "n220_rejections_and_filtered_survivors_partition_old_domain_exactly": True,
        "complete_execution_validator_tested_with_synthetic_fixtures_only": True,
        "numerical_picard_leaf_credit": False,
        "full178_complete": False,
        "heavy_compute": False,
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
