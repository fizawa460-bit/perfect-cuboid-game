#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROD = ROOT / "stage32" / "residual-32-01-production"
if str(PROD) not in sys.path:
    sys.path.insert(0, str(PROD))

from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402
from compressed_terminal_family import terminal_predicate  # noqa: E402

SCHEMA = "STAGE32EX5_BC2_06_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT_V1"
EXPECTED_BC2_05_CHECKPOINT_CANONICAL = "cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e"
ROW_ID = "g1-d008"
DEGREE = 8
EXCEPTIONAL_MASS = 4
NORMAL_BUDGET = 132
BLOCK_WIDTH = 133
PREVIOUS_BLOCK = [0, 132]
NEXT_BLOCK = [133, 265]
EXPECTED_OUTER_EXCEPTIONAL_RANK = 1


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
    return tuple(term[:4] + term[5:])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bc2-05-checkpoint", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    cp = load_json(args.bc2_05_checkpoint)
    verify_canonical(cp, EXPECTED_BC2_05_CHECKPOINT_CANONICAL, "BC2-05 checkpoint")
    if cp["exact_result"]["whole_rank_0_to_132_block_exact_unsat_authorized"] is not True:
        raise ValueError("BC2-05 whole-block UNSAT authority regression")
    if cp["next_exact_unit"]["id"] != "BC2_06_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT":
        raise ValueError("BC2-05 next-unit routing regression")

    indexer = CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    if indexer.normal_budget != NORMAL_BUDGET:
        raise ValueError("normal budget regression")
    if indexer.terminal_count % BLOCK_WIDTH != 0:
        raise ValueError("terminal family no longer decomposes into 133-wide blocks")
    if BLOCK_WIDTH != indexer.normal_budget + 1:
        raise ValueError("block width is not normal-budget + 1")

    previous_end = tuple(int(q) for q in indexer.unrank(PREVIOUS_BLOCK[1]))
    next_start = tuple(int(q) for q in indexer.unrank(NEXT_BLOCK[0]))
    next_end = tuple(int(q) for q in indexer.unrank(NEXT_BLOCK[1]))
    previous_signature = exceptional_signature(previous_end)
    next_signature = exceptional_signature(next_start)

    if previous_end[4] != NORMAL_BUDGET:
        raise ValueError("previous block does not end at x4=normal_budget")
    if next_start[4] != 0 or next_end[4] != NORMAL_BUDGET:
        raise ValueError("next block x4 endpoints regression")
    if next_signature == previous_signature:
        raise ValueError("rank 133 did not advance to a new exceptional signature")
    if indexer.rank(previous_end) != PREVIOUS_BLOCK[1]:
        raise ValueError("previous boundary roundtrip regression")
    if indexer.rank(next_start) != NEXT_BLOCK[0]:
        raise ValueError("next boundary start roundtrip regression")
    if indexer.rank(next_end) != NEXT_BLOCK[1]:
        raise ValueError("next boundary end roundtrip regression")

    replay_stream = []
    for offset in range(BLOCK_WIDTH):
        rank = NEXT_BLOCK[0] + offset
        term = tuple(int(q) for q in indexer.unrank(rank))
        if term[4] != offset:
            raise ValueError(f"x4 is not innermost at rank {rank}")
        if exceptional_signature(term) != next_signature:
            raise ValueError(f"exceptional signature changed inside next block at rank {rank}")
        if indexer.rank(term) != rank:
            raise ValueError(f"rank/unrank replay failed at rank {rank}")
        if not terminal_predicate(term, EXCEPTIONAL_MASS, DEGREE):
            raise ValueError(f"unranked terminal failed source terminal_predicate at rank {rank}")
        replay_stream.append([rank, offset, list(term)])

    outer_rank_start = NEXT_BLOCK[0] // BLOCK_WIDTH
    outer_rank_end = NEXT_BLOCK[1] // BLOCK_WIDTH
    if outer_rank_start != EXPECTED_OUTER_EXCEPTIONAL_RANK or outer_rank_end != EXPECTED_OUTER_EXCEPTIONAL_RANK:
        raise ValueError("next block does not have exceptional outer rank 1")

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-06",
        "unit": "BC2_06_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT",
        "status": "PASS_NEXT_EXCEPTIONAL_BLOCK_EXACTLY_REDERIVED_NO_SOLVER_CREDIT",
        "source_locks": {
            "bc2_05_checkpoint_canonical_sha256": EXPECTED_BC2_05_CHECKPOINT_CANONICAL,
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
            "rank_end": PREVIOUS_BLOCK[1],
            "terminal": list(previous_end),
            "exceptional_signature": list(previous_signature),
        },
        "next_block": {
            "terminal_rank_start": NEXT_BLOCK[0],
            "terminal_rank_end": NEXT_BLOCK[1],
            "block_width": BLOCK_WIDTH,
            "outer_exceptional_rank": EXPECTED_OUTER_EXCEPTIONAL_RANK,
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
        },
        "next_exact_unit": {
            "id": "BC2_07_OUTER_RANK1_SYMBOLIC_X4_PARENT_PREFLIGHT",
            "goal": "Reuse the exact symbolic-x4 Picard64 parent formulation on only ranks 133..265, with the newly rederived outer-rank-1 exceptional signature, before any full-exceptional refinement or scaleout.",
            "heavy_scaleout_authorized": False,
            "new_parallel_lane_required": False,
        },
        "firewalls": {
            "rank_133_to_265_block_picard64_closed": False,
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
        "rank_start": NEXT_BLOCK[0],
        "rank_end": NEXT_BLOCK[1],
        "outer_exceptional_rank": EXPECTED_OUTER_EXCEPTIONAL_RANK,
        "base_terminal": list(next_start),
        "exceptional_signature": list(next_signature),
        "replay_stream_sha256": payload["next_block"]["replay_stream_sha256"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
