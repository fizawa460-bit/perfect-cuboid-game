#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[5]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_indexer import CompressedTerminalIndexer
from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

SMALL_EXHAUSTIVE = [
    # genus, degree, e, old exceptional, accepted exceptional, old terminals, survivors
    (1, 8, 4, 275, 268, 36575, 35644),
    (1, 8, 5, 804, 801, 102912, 102528),
    (0, 8, 8, 11318, 4382, 1278934, 495166),
]

LARGE_RANDOM_ACCESS = [
    # These cases are not enumerated.  Counts are exact N230 subtree-DP outputs
    # independently cross-checked during the retained N230 research checkpoint.
    (0, 100, 29, 159281544, 288),
    (0, 176, 50, 18858396700, 20),
    (0, 176, 100, 11725306972431, 26892419113),
]


def replay_small(genus: int, degree: int, e: int) -> dict:
    filtered = N220FilteredTerminalIndexer(genus, degree, e)
    old = CompressedTerminalIndexer(e, degree)
    accepted_old_exceptional: list[int] = []
    for old_erank in range(old.exceptional_count):
        old_rank0 = old_erank * (old.normal_budget + 1)
        x = old.unrank(old_rank0)
        if filtered.accepts(x):
            accepted_old_exceptional.append(old_erank)

    if len(accepted_old_exceptional) != filtered.accepted_exceptional_count:
        raise ValueError("accepted exceptional count differs from exhaustive old-rank replay")

    for filtered_erank, old_erank in enumerate(accepted_old_exceptional):
        old_rank0 = old_erank * filtered.normal_block
        x = old.unrank(old_rank0)
        exceptional = list(x)
        exceptional[4] = 0
        got_rank = filtered.rank_exceptional(tuple(exceptional))
        if got_rank != filtered_erank:
            raise ValueError("filtered exceptional rank mismatch")
        if filtered.unrank_exceptional(filtered_erank) != tuple(exceptional):
            raise ValueError("filtered exceptional unrank mismatch")

    sample_eranks = sorted(
        set(
            [
                0,
                len(accepted_old_exceptional) // 2,
                len(accepted_old_exceptional) - 1,
            ]
        )
    )
    x4_samples = sorted(set([0, filtered.normal_block // 2, filtered.normal_block - 1]))
    for filtered_erank in sample_eranks:
        old_erank = accepted_old_exceptional[filtered_erank]
        for x4 in x4_samples:
            old_rank = old_erank * filtered.normal_block + x4
            x = old.unrank(old_rank)
            filtered_rank = filtered.rank(x)
            expected_filtered_rank = filtered_erank * filtered.normal_block + x4
            if filtered_rank != expected_filtered_rank:
                raise ValueError("x4-block filtered rank regression")
            if filtered.unrank(filtered_rank) != x:
                raise ValueError("terminal filtered rank/unrank regression")
            if filtered.old_rank_of_filtered(filtered_rank) != old_rank:
                raise ValueError("filtered -> old canonical rank replay regression")
            if filtered.filtered_rank_of_old(old_rank) != filtered_rank:
                raise ValueError("old -> filtered rank replay regression")

    cert = filtered.certificate()
    if int(cert["old_terminal_count"]) != old.terminal_count:
        raise ValueError("old terminal certificate regression")
    if int(cert["filtered_terminal_count"]) != filtered.terminal_count:
        raise ValueError("filtered terminal certificate regression")
    if int(cert["filtered_terminal_count"]) + int(cert["n220_rejected_terminal_count"]) != int(cert["old_terminal_count"]):
        raise ValueError("N220 exact old-domain partition regression")

    return {
        "genus": genus,
        "degree": degree,
        "e": e,
        "old_exceptional_count": old.exceptional_count,
        "accepted_exceptional_count": filtered.accepted_exceptional_count,
        "old_terminal_count": old.terminal_count,
        "filtered_terminal_count": filtered.terminal_count,
        "exhaustive_exceptional_replay": True,
        "sampled_terminal_x4_block_replay": True,
    }


def replay_large(genus: int, degree: int, e: int) -> dict:
    filtered = N220FilteredTerminalIndexer(genus, degree, e)
    old = CompressedTerminalIndexer(e, degree)
    count = filtered.accepted_exceptional_count
    ranks = sorted(set([0, count // 2, count - 1])) if count else []
    samples = []
    for filtered_erank in ranks:
        exceptional = filtered.unrank_exceptional(filtered_erank)
        if filtered.rank_exceptional(exceptional) != filtered_erank:
            raise ValueError("large filtered exceptional roundtrip regression")
        x = list(exceptional)
        x[4] = filtered.normal_block // 2
        x = tuple(x)
        filtered_rank = filtered.rank(x)
        old_rank = old.rank(x)
        if filtered.old_rank_of_filtered(filtered_rank) != old_rank:
            raise ValueError("large filtered/old replay regression")
        samples.append(
            {
                "filtered_exceptional_rank": filtered_erank,
                "old_exceptional_rank": old_rank // filtered.normal_block,
            }
        )
    return {
        "genus": genus,
        "degree": degree,
        "e": e,
        "old_exceptional_count": old.exceptional_count,
        "accepted_exceptional_count": count,
        "random_access_samples": samples,
    }


def main() -> None:
    small_results = []
    for genus, degree, e, expected_old_exc, expected_acc_exc, expected_old, expected_survivors in SMALL_EXHAUSTIVE:
        result = replay_small(genus, degree, e)
        observed = (
            result["old_exceptional_count"],
            result["accepted_exceptional_count"],
            result["old_terminal_count"],
            result["filtered_terminal_count"],
        )
        expected = (expected_old_exc, expected_acc_exc, expected_old, expected_survivors)
        if observed != expected:
            raise ValueError(f"small exact count regression: {observed} != {expected}")
        small_results.append(result)

    large_results = []
    for genus, degree, e, expected_old_exc, expected_acc_exc in LARGE_RANDOM_ACCESS:
        result = replay_large(genus, degree, e)
        observed = (result["old_exceptional_count"], result["accepted_exceptional_count"])
        expected = (expected_old_exc, expected_acc_exc)
        if observed != expected:
            raise ValueError(f"large exact count regression: {observed} != {expected}")
        large_results.append(result)

    print(
        json.dumps(
            {
                "verdict": "PASS_N230_EXACT_FILTERED_RANDOM_ACCESS_REPLAY",
                "small_exhaustive": small_results,
                "large_random_access": large_results,
                "old_rank_remains_completeness_authority": True,
                "secondary_filtered_rank_only": True,
                "x4_block_preserved_exactly": True,
                "full_27_digit_materialization": False,
                "heavy_compute": False,
                "full178_complete": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
