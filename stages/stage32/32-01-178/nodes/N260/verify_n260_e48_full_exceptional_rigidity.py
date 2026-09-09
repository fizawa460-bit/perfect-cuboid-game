#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
N230 = HERE.parent / "N230"
sys.path.insert(0, str(N230))

from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

CASES = [
    (0, 174, 48, 3067),
    (0, 176, 48, 3105),
    (1, 190, 48, 3371),
    (1, 192, 48, 3409),
]
EXPECTED_EXCEPTIONAL_PREFIX = (1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1)


def prove_mass_support_rigidity(*, slots: int, mass: int, required_support: int) -> dict:
    if slots != 48 or mass != 48 or required_support != 48:
        raise ValueError("N260 rigidity proof is intentionally scoped to 48/48/48")
    # For 48 nonnegative integral coordinates q_i:
    # support(q) <= 48.  The audited lower bound requires support(q) >= 48,
    # hence support(q)=48 and every q_i>=1.  Their sum is exactly 48, so all
    # q_i=1.  This is an exact arithmetic consequence, not solver evidence.
    min_mass_if_all_positive = slots
    if min_mass_if_all_positive != mass:
        raise AssertionError("rigidity arithmetic regression")
    return {
        "exceptional_slot_count": slots,
        "exceptional_mass": mass,
        "required_positive_support": required_support,
        "support_forced": 48,
        "every_exceptional_pairing_positive": True,
        "every_exceptional_pairing_value": 1,
        "full_exceptional_vector": [1] * 48,
        "solver_required_for_exceptional_vector": False,
    }


def main() -> None:
    rigidity = prove_mass_support_rigidity(slots=48, mass=48, required_support=48)
    results = []
    for genus, degree, e, expected_normal_block in CASES:
        indexer = N220FilteredTerminalIndexer(genus, degree, e)
        if indexer.required_support != 48:
            raise AssertionError("K regression")
        if indexer.normal_block != expected_normal_block:
            raise AssertionError("normal x4 block regression")
        if indexer.accepted_exceptional_count != 1:
            raise AssertionError("expected exactly one N220-surviving exceptional prefix")
        prefix = indexer.unrank_exceptional(0)
        if prefix != EXPECTED_EXCEPTIONAL_PREFIX:
            raise AssertionError(f"unique exceptional prefix regression: {prefix}")
        if indexer.rank_exceptional(prefix) != 0:
            raise AssertionError("unique exceptional prefix rank regression")

        rank_samples = []
        for filtered_rank in sorted({0, expected_normal_block // 2, expected_normal_block - 1}):
            terminal = indexer.unrank(filtered_rank)
            if any(terminal[i] != 1 for i in range(11) if i != 4):
                raise AssertionError("filtered terminal lost forced first-ten exceptional ones")
            if terminal[4] != filtered_rank:
                raise AssertionError("single exceptional block must leave filtered rank equal to x4")
            old_rank = indexer.old_rank_of_filtered(filtered_rank)
            disposition = indexer.disposition_of_old(old_rank)
            if disposition.get("disposition") != "N220_SURVIVOR":
                raise AssertionError("filtered sample did not replay to survivor old rank")
            if int(disposition["filtered_rank"]) != filtered_rank:
                raise AssertionError("filtered/old replay regression")
            rank_samples.append({
                "filtered_rank": filtered_rank,
                "x4": terminal[4],
                "old_rank": old_rank,
            })

        results.append({
            "row_id": f"g{genus}-d{degree:03d}",
            "g": genus,
            "d": degree,
            "e": e,
            "K": indexer.required_support,
            "survivor_exceptional_blocks": indexer.accepted_exceptional_count,
            "normal_x4_block": indexer.normal_block,
            "filtered_terminal_count": indexer.terminal_count,
            "forced_first_ten_exceptional_prefix": list(prefix),
            "full_48_exceptional_vector_forced_all_ones": True,
            "rank_samples": rank_samples,
        })

    print(json.dumps({
        "verdict": "PASS_N260_E48_FULL_EXCEPTIONAL_RIGIDITY",
        "rigidity": rigidity,
        "cases": results,
        "case_count": len(results),
        "interpretation": "four FULL178 strata have exactly one exceptional outer block; only x4 remains free at indexed-terminal level",
        "existing_ex5_solver_directly_portable": False,
        "reason_existing_ex5_solver_not_directly_portable": "BC2-03 is generic in terminal rank only but source-locks g1-d008/e4 constants; a stratum-generic Picard leaf adapter is still required",
        "new_picard_unsat_credit": False,
        "full178_complete": False,
        "heavy_compute": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
