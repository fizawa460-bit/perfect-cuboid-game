#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROD = ROOT / "stages" / "stage32" / "residual-32-01-production"
if str(PROD) not in sys.path:
    sys.path.insert(0, str(PROD))

from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402
from compressed_terminal_family import terminal_predicate  # noqa: E402

SCHEMA = "STAGE32EX5_BC2_09_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT_V1"
EXPECTED_BC2_08_CHECKPOINT_CANONICAL = "af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c"
ROW_ID = "g1-d008"
DEGREE = 8
EXCEPTIONAL_MASS = 4
NORMAL_BUDGET = 132
BLOCK_WIDTH = NORMAL_BUDGET + 1


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def verify_canonical(payload: dict, expected: str, label: str) -> None:
    if payload.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"{label} canonical field regression")
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    if csha(body) != expected:
        raise ValueError(f"{label} canonical replay regression")


def exceptional_signature(term: tuple[int, ...]) -> tuple[int, ...]:
    # Coordinate 4 is the unique normal x4 coordinate in this compressed family.
    return tuple(term[:4] + term[5:])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bc2-08-checkpoint", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    cp = load_json(args.bc2_08_checkpoint)
    verify_canonical(cp, EXPECTED_BC2_08_CHECKPOINT_CANONICAL, "BC2-08 checkpoint")
    if cp["exact_result"]["rank_133_to_265_block_exact_unsat_authorized"] is not True:
        raise ValueError("BC2-08 whole-block UNSAT authority regression")
    if cp["next_exact_unit"]["id"] != "BC2_09_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT":
        raise ValueError("BC2-08 next-unit routing regression")
    if cp["scope"]["whole_rank_0_to_132_block_closed"] is not True:
        raise ValueError("rank 0..132 predecessor closure regression")
    if cp["scope"]["whole_rank_133_to_265_block_closed"] is not True:
        raise ValueError("rank 133..265 predecessor closure regression")

    previous_block = [int(q) for q in cp["proof_partition"]["terminal_rank_block"]]
    if previous_block != [133, 265]:
        raise ValueError("BC2-08 retained block boundary regression")
    previous_outer_rank = int(cp["proof_partition"]["outer_exceptional_rank"])

    indexer = CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    if indexer.normal_budget != NORMAL_BUDGET:
        raise ValueError("normal budget regression")
    if BLOCK_WIDTH != indexer.normal_budget + 1:
        raise ValueError("block width is not normal-budget + 1")
    if indexer.terminal_count % BLOCK_WIDTH != 0:
        raise ValueError("terminal family no longer decomposes into 133-wide blocks")

    next_start_rank = previous_block[1] + 1
    next_end_rank = next_start_rank + BLOCK_WIDTH - 1
    if next_end_rank >= indexer.terminal_count:
        raise ValueError("no complete next 133-rank block remains")

    previous_end = tuple(int(q) for q in indexer.unrank(previous_block[1]))
    next_start = tuple(int(q) for q in indexer.unrank(next_start_rank))
    next_end = tuple(int(q) for q in indexer.unrank(next_end_rank))
    previous_signature = exceptional_signature(previous_end)
    next_signature = exceptional_signature(next_start)

    if previous_end[4] != NORMAL_BUDGET:
        raise ValueError("previous block does not end at x4=normal_budget")
    if next_start[4] != 0 or next_end[4] != NORMAL_BUDGET:
        raise ValueError("next block x4 endpoints regression")
    if next_signature == previous_signature:
        raise ValueError("next block did not advance to a new exceptional signature")
    if indexer.rank(previous_end) != previous_block[1]:
        raise ValueError("previous boundary roundtrip regression")
    if indexer.rank(next_start) != next_start_rank:
        raise ValueError("next boundary start roundtrip regression")
    if indexer.rank(next_end) != next_end_rank:
        raise ValueError("next boundary end roundtrip regression")

    replay_stream = []
    for offset in range(BLOCK_WIDTH):
        rank = next_start_rank + offset
        term = tuple(int(q) for q in indexer.unrank(rank))
        if term[4] != offset:
            raise ValueError(f"x4 is not innermost at rank {rank}")
        if exceptional_signature(term) != next_signature:
            raise ValueError(f"exceptional signature changed inside next block at rank {rank}")
        if indexer.rank(term) != rank:
            raise ValueError(f"rank/unrank replay failed at rank {rank}")
        if not terminal_predicate(term, e=EXCEPTIONAL_MASS, d=DEGREE):
            raise ValueError(f"unranked terminal failed source terminal_predicate at rank {rank}")
        replay_stream.append([rank, offset, list(term)])

    outer_rank_start = next_start_rank // BLOCK_WIDTH
    outer_rank_end = next_end_rank // BLOCK_WIDTH
    if outer_rank_start != outer_rank_end:
        raise ValueError("next 133-rank block crosses an outer-rank boundary")
    if outer_rank_start != previous_outer_rank + 1:
        raise ValueError("next block did not advance by exactly one outer exceptional rank")

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-09",
        "unit": "BC2_09_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT",
        "status": "PASS_NEXT_EXCEPTIONAL_BLOCK_EXACTLY_REDERIVED_NO_SOLVER_CREDIT",
        "source_locks": {
            "bc2_08_checkpoint_canonical_sha256": EXPECTED_BC2_08_CHECKPOINT_CANONICAL,
            "indexer_class": "CompressedTerminalIndexer",
            "terminal_predicate": "compressed_terminal_family.terminal_predicate",
        },
        "target": {
            "row_id": ROW_ID,
            "degree": DEGREE,
            "e": EXCEPTIONAL_MASS,
            "normal_budget": NORMAL_BUDGET,
        },
        "previous_block_boundary": {
            "rank_start": previous_block[0],
            "rank_end": previous_block[1],
            "outer_exceptional_rank": previous_outer_rank,
            "terminal": list(previous_end),
            "exceptional_signature": list(previous_signature),
        },
        "next_block": {
            "terminal_rank_start": next_start_rank,
            "terminal_rank_end": next_end_rank,
            "block_width": BLOCK_WIDTH,
            "outer_exceptional_rank": outer_rank_start,
            "x4_start": 0,
            "x4_end": NORMAL_BUDGET,
            "base_terminal_x4_zero": list(next_start),
            "exceptional_signature": list(next_signature),
            "exceptional_signature_differs_from_previous_block": next_signature != previous_signature,
            "all_133_rank_unrank_replays_exact": True,
            "all_133_terminal_predicate_replays_exact": True,
            "x4_is_innermost_coordinate_over_block": True,
            "exceptional_signature_constant_over_block": True,
            "replay_stream_sha256": csha(replay_stream),
        },
        "execution": {
            "solver_invoked": False,
            "heavy_compute_invoked": False,
            "artifact_required": False,
            "new_mathematical_condition_added": False,
            "signature_assumed_in_advance": False,
            "exceptional_mass_split_assumed_in_advance": False,
        },
        "next_exact_unit": {
            "id": f"BC2_10_OUTER_RANK{outer_rank_start}_SYMBOLIC_X4_PARENT_PREFLIGHT",
            "goal": "Apply the exact symbolic-x4 Picard64 selected-exceptional parent formulation only to the rederived next 133-rank block; derive its fixed/residual exceptional mass from the actual terminal signature before constructing the parent partition.",
            "heavy_scaleout_authorized": False,
            "new_parallel_lane_required": False,
        },
        "firewalls": {
            "rank_0_to_132_block_exact_unsat_retained": True,
            "rank_133_to_265_block_exact_unsat_retained": True,
            "next_block_picard64_closed": False,
            "whole_g1_d008_e4_stratum_closed": False,
            "FULL178_complete": False,
            "stage32_main_credit": False,
            "receiver_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "rank_start": next_start_rank,
        "rank_end": next_end_rank,
        "outer_exceptional_rank": outer_rank_start,
        "base_terminal": list(next_start),
        "exceptional_signature": list(next_signature),
        "replay_stream_sha256": payload["next_block"]["replay_stream_sha256"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
