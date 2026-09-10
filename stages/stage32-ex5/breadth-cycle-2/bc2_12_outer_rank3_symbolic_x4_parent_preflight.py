#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

import bc2_03_generic_indexed_terminal_adaptive_exceptional_partition as g
import bc2_07_outer_rank1_symbolic_x4_parent_preflight as engine

SCHEMA = "STAGE32EX5_BC2_12_OUTER_RANK3_SYMBOLIC_X4_PARENT_PREFLIGHT_V1"
EXPECTED_BC2_11_CANONICAL = "b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d"
EXPECTED_BC2_11_REPLAY_STREAM = "2c823dec0523d2e16b182f7213fb55468011c72328f09d487e9692941e994f60"
BLOCK_EXCEPTIONAL_RANK = 3
BLOCK_START = 399
BLOCK_END = 531
EXPECTED_BASE_TERMINAL = (0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1)
EXPECTED_EXCEPTIONAL_SIGNATURE = (0, 1, 0, 0, 0, 1, 0, 0, 0, 1)


def _synthetic_bc2_06(block: dict) -> dict:
    replay = {
        "terminal_rank_start": block["terminal_rank_start"],
        "terminal_rank_end": block["terminal_rank_end"],
        "outer_exceptional_rank": block["outer_exceptional_rank"],
        "base_terminal_x4_zero": block["base_terminal_x4_zero"],
        "exceptional_signature": block["exceptional_signature"],
        "all_133_rank_unrank_replays_exact": block["all_133_rank_unrank_replays_exact"],
        "all_133_terminal_predicate_replays_exact": block["all_133_terminal_predicate_replays_exact"],
        "x4_is_innermost_coordinate_over_block": block["x4_is_innermost_coordinate_over_block"],
        "exceptional_signature_constant_over_block": block["exceptional_signature_constant_over_block"],
        "replay_stream_sha256": block["replay_stream_sha256"],
    }
    payload = {
        "schema": "BC2_12_ENGINE_COMPATIBILITY_SHIM_V1",
        "exact_replay": replay,
        "next_exact_unit": {"id": "BC2_07_OUTER_RANK1_SYMBOLIC_X4_PARENT_PREFLIGHT"},
        "predecessor": {"rank_0_to_132_block_exact_unsat": True},
        "firewalls": {"rank_133_to_265_block_picard64_closed": False},
    }
    payload["canonical_sha256_without_this_field"] = g.csha(payload)
    return payload


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--bc2-11-checkpoint", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--parent-timeout-ms", type=int, default=1500)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    v1 = g.v1
    bc2_11, bc2_11_canonical = v1.load_canonical_json(args.bc2_11_checkpoint)
    if bc2_11_canonical != EXPECTED_BC2_11_CANONICAL:
        raise ValueError("BC2-11 checkpoint canonical regression")
    if bc2_11.get("next_exact_unit", {}).get("id") != "BC2_12_OUTER_RANK3_SYMBOLIC_X4_PARENT_PREFLIGHT":
        raise ValueError("BC2-11 next-unit routing regression")
    for key in (
        "rank_0_to_132_block_exact_unsat_retained",
        "rank_133_to_265_block_exact_unsat_retained",
        "rank_266_to_398_block_exact_unsat_retained",
    ):
        if bc2_11.get("firewalls", {}).get(key) is not True:
            raise ValueError(f"BC2-11 predecessor authority regression: {key}")
    if bc2_11.get("firewalls", {}).get("next_block_picard64_closed") is not False:
        raise ValueError("BC2-11 next-block credit firewall regression")

    block = bc2_11["next_block"]
    if block.get("terminal_rank_start") != BLOCK_START or block.get("terminal_rank_end") != BLOCK_END:
        raise ValueError("BC2-11 rank-block regression")
    if block.get("outer_exceptional_rank") != BLOCK_EXCEPTIONAL_RANK:
        raise ValueError("BC2-11 outer exceptional-rank regression")
    if tuple(block.get("base_terminal_x4_zero", [])) != EXPECTED_BASE_TERMINAL:
        raise ValueError("BC2-11 base-terminal regression")
    if tuple(block.get("exceptional_signature", [])) != EXPECTED_EXCEPTIONAL_SIGNATURE:
        raise ValueError("BC2-11 exceptional-signature regression")
    if block.get("replay_stream_sha256") != EXPECTED_BC2_11_REPLAY_STREAM:
        raise ValueError("BC2-11 replay-stream regression")
    for key in (
        "all_133_rank_unrank_replays_exact",
        "all_133_terminal_predicate_replays_exact",
        "x4_is_innermost_coordinate_over_block",
        "exceptional_signature_constant_over_block",
    ):
        if block.get(key) is not True:
            raise ValueError(f"BC2-11 replay authority regression: {key}")

    synthetic = _synthetic_bc2_06(block)
    synthetic_canonical = synthetic["canonical_sha256_without_this_field"]

    engine.SCHEMA = SCHEMA
    engine.BLOCK_EXCEPTIONAL_RANK = BLOCK_EXCEPTIONAL_RANK
    engine.BLOCK_START = BLOCK_START
    engine.BLOCK_END = BLOCK_END
    engine.EXPECTED_BC2_06_CANONICAL = synthetic_canonical
    engine.EXPECTED_BASE_TERMINAL = EXPECTED_BASE_TERMINAL
    engine.EXPECTED_EXCEPTIONAL_SIGNATURE = EXPECTED_EXCEPTIONAL_SIGNATURE

    with tempfile.TemporaryDirectory(prefix="stage32ex5-bc2-12-") as td:
        td_path = Path(td)
        shim_path = td_path / "bc2-11-engine-shim.json"
        raw_path = td_path / "bc2-12-engine-raw.json"
        shim_path.write_text(json.dumps(synthetic, indent=2, sort_keys=True) + "\n")

        old_argv = sys.argv
        try:
            sys.argv = [
                old_argv[0],
                "--manifest", str(args.manifest),
                "--prefix-checkpoint", str(args.prefix_checkpoint),
                "--adapter-preflight", str(args.adapter_preflight),
                "--bc2-06-checkpoint", str(shim_path),
                "--retained", str(args.retained),
                "--marking", str(args.marking),
                "--parent-timeout-ms", str(args.parent_timeout_ms),
                "--output", str(raw_path),
            ]
            engine.main()
        finally:
            sys.argv = old_argv

        payload = json.loads(raw_path.read_text())

    aggregate = payload["parent_result"]["aggregate_result"]
    payload["schema"] = SCHEMA
    payload["leaf"] = "BC2-12"
    payload["unit"] = "BC2_12_OUTER_RANK3_SYMBOLIC_X4_PARENT_PREFLIGHT"
    payload["status"] = (
        "PASS_OUTER_RANK3_SYMBOLIC_X4_HAS_EXACT_PICARD64_COMPLETION"
        if aggregate == "SAT"
        else "PASS_OUTER_RANK3_SYMBOLIC_X4_PARENT_EXACT_UNSAT"
        if aggregate == "UNSAT"
        else "PASS_OUTER_RANK3_SYMBOLIC_X4_PARENT_REFINEMENT_REQUIRED"
    )

    locks = payload["source_locks"]
    locks.pop("bc2_06_checkpoint_canonical_sha256", None)
    locks.pop("bc2_06_replay_stream_sha256", None)
    locks["bc2_11_checkpoint_canonical_sha256"] = bc2_11_canonical
    locks["bc2_11_replay_stream_sha256"] = block["replay_stream_sha256"]
    locks["engine_reuse"] = "BC2-07 exact symbolic-x4 parent engine; BC2-11 inputs independently source-locked before compatibility shim"

    semantics = payload["block_semantics"]
    semantics.pop("bc2_06_exact_replay_consumed", None)
    semantics["bc2_11_exact_replay_consumed"] = True

    result = payload["result"]
    result.pop("rank_133_to_265_block_exact_unsat_authorized", None)
    result["rank_399_to_531_block_exact_unsat_authorized"] = aggregate == "UNSAT"

    if aggregate == "SAT":
        next_id = "BC2_12_SAT_NODE_SUPPORT_CONSUMPTION"
    elif aggregate == "UNSAT":
        next_id = "BC2_13_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
    else:
        next_id = "BC2_13_OUTER_RANK3_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT"
    payload["next_exact_unit"]["id"] = next_id

    firewalls = payload["firewalls"]
    firewalls["rank_0_to_132_block_exact_unsat_retained"] = True
    firewalls.pop("rank_133_to_265_block_picard64_closed", None)
    firewalls["rank_133_to_265_block_exact_unsat_retained"] = True
    firewalls["rank_266_to_398_block_exact_unsat_retained"] = True
    firewalls["rank_399_to_531_block_picard64_closed"] = aggregate == "UNSAT"

    payload.pop("canonical_sha256_without_this_field", None)
    payload["canonical_sha256_without_this_field"] = g.csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(json.dumps({
        "aggregate_result": aggregate,
        "block": [BLOCK_START, BLOCK_END],
        "fixed_exceptional_mass": payload["adaptive_exceptional_partition"]["fixed_exceptional_mass"],
        "residual_exceptional_mass": payload["adaptive_exceptional_partition"]["residual_exceptional_mass"],
        "parent_branches": payload["adaptive_exceptional_partition"]["parent_branch_count"],
        "parent_unsat": payload["parent_result"]["exact_unsat_parent_branches"],
        "parent_unknown": payload["parent_result"]["unknown_parent_branches"],
        "refined_subcases_if_needed": payload["parent_result"]["exact_full_exceptional_refinement_subcase_count_if_needed"],
        "sat_parent": payload["parent_result"]["sat_parent"],
        "next_exact_unit": next_id,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
