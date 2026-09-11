#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B2 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(B2))
sys.path.insert(0, str(RESIDUAL))

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18
from compressed_terminal_family import exceptional_terminal_count
from compressed_terminal_indexer import CompressedTerminalIndexer

SCHEMA = "STAGE32EX5_E8_TERMINAL_POPULATION_ADAPTER_V1"
ROW_ID = "g1-d008"
TARGET_G = 1
TARGET_D = 8
TARGET_E = 8
NORMAL_BUDGET = 112
BLOCK_WIDTH = NORMAL_BUDGET + 1
BLOCK_COUNT = 11318
TERMINAL_COUNT = 1278934
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X4_LABEL = 49
EXPECTED_DEN = 8
EXPECTED_SELECTED_EXCEPTIONAL = 29
EXPECTED_FIXED_EXCEPTIONAL = 10
EXPECTED_FREE_SELECTED_EXCEPTIONAL = 19
FIRST_BLOCK_PARENT_COUNT = 7336
FIRST_BLOCK_STREAM_SHA256 = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
BC217 = B2 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def stream_update(h, record: dict) -> None:
    h.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n")


def indexer() -> CompressedTerminalIndexer:
    idx = CompressedTerminalIndexer(TARGET_E, TARGET_D)
    if idx.normal_budget != NORMAL_BUDGET:
        raise ValueError("e8 normal-budget regression")
    if idx.exceptional_count != BLOCK_COUNT:
        raise ValueError(f"e8 block-count regression: {idx.exceptional_count}")
    if idx.terminal_count != TERMINAL_COUNT:
        raise ValueError(f"e8 terminal-count regression: {idx.terminal_count}")
    return idx


def block_terminal_range(block_index: int) -> tuple[int, int]:
    block_index = int(block_index)
    if not 0 <= block_index < BLOCK_COUNT:
        raise ValueError(f"block index outside 0..{BLOCK_COUNT - 1}: {block_index}")
    lo = block_index * BLOCK_WIDTH
    return lo, lo + BLOCK_WIDTH - 1


def block_signature(block_index: int) -> dict:
    idx = indexer()
    lo, hi = block_terminal_range(block_index)
    base = tuple(int(v) for v in idx.unrank(lo))
    if base[4] != 0 or idx.rank(base) != lo:
        raise ValueError("block-base rank/unrank regression")
    top = tuple(int(v) for v in idx.unrank(hi))
    if top[4] != NORMAL_BUDGET or idx.rank(top) != hi:
        raise ValueError("block-top rank/unrank regression")
    if base[:4] + base[5:] != top[:4] + top[5:]:
        raise ValueError("exceptional signature changed across block")
    by_label = {int(label): int(value) for label, value in zip(ASSIGNMENT_ORDER, base)}
    fixed = {label: value for label, value in by_label.items() if label != X4_LABEL}
    if any(label <= d18.NORMAL_COUNT for label in fixed):
        raise ValueError("terminal fixed coordinate unexpectedly nonexceptional")
    fixed_mass = sum(fixed.values())
    if not 0 <= fixed_mass <= TARGET_E:
        raise ValueError("terminal fixed exceptional mass regression")
    residual = TARGET_E - fixed_mass
    expected_candidates = math.comb(residual + EXPECTED_FREE_SELECTED_EXCEPTIONAL, EXPECTED_FREE_SELECTED_EXCEPTIONAL)
    return {
        "block_index": int(block_index),
        "terminal_rank_range": [lo, hi],
        "terminal_count": BLOCK_WIDTH,
        "base_terminal": list(base),
        "exceptional_signature": list(base[:4] + base[5:]),
        "fixed_exceptional_pairings": {str(k): int(v) for k, v in sorted(fixed.items())},
        "fixed_exceptional_mass": fixed_mass,
        "residual_exceptional_mass": residual,
        "raw_selected_parent_candidate_count": expected_candidates,
    }


@dataclass
class Geometry:
    selected_labels: list[int]
    exceptional_labels: list[int]
    normal_positions: list[int]
    exceptional_positions: list[int]
    pos_by_label: dict[int, int]
    den: int
    B: Matrix
    full_check: dict
    x4_check: dict


def load_geometry() -> Geometry:
    bc217 = json.loads(BC217.read_text())
    if bc217.get("canonical_sha256_without_this_field") != d18.EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 target-authority canonical regression")
    target = bc217["retarget"]["selected_target"]
    if target != {"row_id": ROW_ID, "g": TARGET_G, "d": TARGET_D, "e": TARGET_E, "survives_n354": True}:
        raise ValueError("BC2-17 current-MAIN-survivor target regression")

    bundle = d18.load_retained(d18.RETAINED, "s32ex5_e8_handoff_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_e8_handoff_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained Picard marking canonical regression")

    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (140, 64):
        raise ValueError("all140 pairing matrix shape regression")
    labels = [int(v) for v in d18.INDLIST]
    Psel = P.extract([label - 1 for label in labels], list(range(64)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = d18.lcm_denominator(Pinv)
    if den != EXPECTED_DEN:
        raise ValueError(f"selected64 denominator regression: {den}")
    Bq = Pinv * den
    if any(q.q != 1 for q in Bq):
        raise ValueError("selected64 inverse scaling regression")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    if Psel * B != den * Matrix.eye(64):
        raise ValueError("selected64 inverse exact replay regression")

    normal_positions = [j for j, label in enumerate(labels) if label <= d18.NORMAL_COUNT]
    exceptional_positions = [j for j, label in enumerate(labels) if label > d18.NORMAL_COUNT]
    exceptional_labels = [labels[j] for j in exceptional_positions]
    if len(exceptional_labels) != EXPECTED_SELECTED_EXCEPTIONAL:
        raise ValueError("selected exceptional count regression")
    if any(label not in exceptional_labels for label in ASSIGNMENT_ORDER if label != X4_LABEL):
        raise ValueError("terminal exceptional labels left selected64 coordinates")
    pos_by_label = {label: j for j, label in enumerate(labels)}
    full_check = d18.build_hnf_extension_check(B, den, exceptional_positions, normal_positions)
    x4_pos = pos_by_label[X4_LABEL]
    x4_check = d18.build_hnf_extension_check(
        B,
        den,
        exceptional_positions + [x4_pos],
        [j for j in normal_positions if j != x4_pos],
    )
    return Geometry(labels, exceptional_labels, normal_positions, exceptional_positions, pos_by_label, den, B, full_check, x4_check)


def iter_parent_population(block_index: int, geometry: Geometry | None = None):
    sig = block_signature(block_index)
    g = geometry or load_geometry()
    fixed = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
    free_labels = [label for label in g.exceptional_labels if label not in fixed]
    if len(free_labels) != EXPECTED_FREE_SELECTED_EXCEPTIONAL:
        raise ValueError("free selected exceptional count regression")
    residual = int(sig["residual_exceptional_mass"])
    expected = math.comb(residual + len(free_labels), len(free_labels))
    if expected != sig["raw_selected_parent_candidate_count"]:
        raise ValueError("raw parent candidate count regression")

    for comp in d18.weak_compositions_at_most(residual, len(free_labels)):
        by = dict(fixed)
        by.update({label: int(value) for label, value in zip(free_labels, comp)})
        yE = [int(by[label]) for label in g.exceptional_labels]
        allowed = [r for r in range(g.den) if d18.feasible(g.x4_check, yE + [r])]
        ok = d18.feasible(g.full_check, yE)
        if ok != bool(allowed):
            raise ValueError("full HNF extension/x4-residue extension regression")
        if ok:
            yield {
                "selected_exceptional_pairings": yE,
                "selected_residual_mass": int(sum(comp)),
                "x4_allowed_residues_mod8": allowed,
            }


def summarize_block(block_index: int, geometry: Geometry | None = None) -> dict:
    g = geometry or load_geometry()
    sig = block_signature(block_index)
    h = hashlib.sha256()
    count = 0
    residues: set[int] = set()
    mass_hist: dict[int, int] = {}
    for record in iter_parent_population(block_index, g):
        count += 1
        stream_update(h, record)
        residues.update(int(v) for v in record["x4_allowed_residues_mod8"])
        m = int(record["selected_residual_mass"])
        mass_hist[m] = mass_hist.get(m, 0) + 1
    out = {
        **sig,
        "modular_feasible_parent_count": count,
        "parent_stream_sha256": h.hexdigest(),
        "x4_allowed_residue_union_mod8": sorted(residues),
        "feasible_selected_residual_mass_histogram": {str(k): v for k, v in sorted(mass_hist.items())},
    }
    if block_index == 0:
        if count != FIRST_BLOCK_PARENT_COUNT or h.hexdigest() != FIRST_BLOCK_STREAM_SHA256:
            raise ValueError("first-block BC2-18/CUT102 replay regression")
        out["first_block_replay"] = True
    return out


def describe() -> dict:
    idx = indexer()
    exact_by_mass = []
    prior = 0
    raw_total = 0
    for mass in range(TARGET_E + 1):
        cumulative = exceptional_terminal_count(mass)
        exact = cumulative - prior
        residual = TARGET_E - mass
        raw = math.comb(residual + EXPECTED_FREE_SELECTED_EXCEPTIONAL, EXPECTED_FREE_SELECTED_EXCEPTIONAL)
        exact_by_mass.append({
            "fixed_exceptional_mass": mass,
            "block_count": exact,
            "residual_exceptional_mass": residual,
            "raw_parent_candidates_per_block": raw,
            "raw_parent_candidates_total": exact * raw,
        })
        raw_total += exact * raw
        prior = cumulative
    if prior != BLOCK_COUNT or raw_total != 12458750:
        raise ValueError("whole e8 adapter population accounting regression")
    return {
        "schema": SCHEMA,
        "target": {"row_id": ROW_ID, "g": TARGET_G, "d": TARGET_D, "e": TARGET_E, "n354_survivor_stratum": True},
        "population": {
            "exceptional_signature_block_count": BLOCK_COUNT,
            "terminal_block_width": BLOCK_WIDTH,
            "terminal_count": TERMINAL_COUNT,
            "canonical_index_order": idx.certificate()["canonical_index_order"],
            "full_materialization_required": False,
            "random_access_by_exceptional_rank": True,
            "raw_selected_parent_candidates_if_all_blocks_materialized": raw_total,
            "block_distribution_by_fixed_exceptional_mass": exact_by_mass,
        },
        "semantics": {
            "block_index": "exceptional_rank in CompressedTerminalIndexer(e=8,d=8)",
            "terminal_rank_range": "[block_index*113, block_index*113+112]",
            "x4_is_innermost_coordinate": True,
            "parent_population": "all HNF-integrality-feasible selected-exceptional completions with exact fixed terminal exceptional signature and x4 residues mod 8",
            "cut_consumption": "CUT may request any block lazily; no block-specific Picard64 adapter is required",
        },
        "credit": {"stage32_main_pruning_credit": False, "full178_complete": False, "theorem_credit": False, "merge_authorized": False},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--describe", action="store_true")
    ap.add_argument("--block-start", type=int)
    ap.add_argument("--block-count", type=int, default=1)
    ap.add_argument("--max-raw-candidates", type=int, default=1000000)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    if args.describe:
        body = describe()
    else:
        if args.block_start is None or args.block_count <= 0:
            raise ValueError("positive --block-count and --block-start are required")
        end = args.block_start + args.block_count
        if args.block_start < 0 or end > BLOCK_COUNT:
            raise ValueError("requested block wave outside e8 population")
        signatures = [block_signature(i) for i in range(args.block_start, end)]
        raw = sum(int(s["raw_selected_parent_candidate_count"]) for s in signatures)
        if raw > args.max_raw_candidates:
            raise ValueError(f"raw candidate resource gate: {raw}>{args.max_raw_candidates}")
        g = load_geometry()
        records = [summarize_block(i, g) for i in range(args.block_start, end)]
        body = {
            "schema": "STAGE32EX5_E8_TERMINAL_POPULATION_WAVE_V1",
            "adapter_schema": SCHEMA,
            "target": {"row_id": ROW_ID, "g": TARGET_G, "d": TARGET_D, "e": TARGET_E},
            "block_range": [args.block_start, end - 1],
            "terminal_rank_range": [args.block_start * BLOCK_WIDTH, end * BLOCK_WIDTH - 1],
            "block_count": args.block_count,
            "terminal_count": args.block_count * BLOCK_WIDTH,
            "raw_parent_candidates_checked": raw,
            "blocks": records,
            "firewalls": {"stage32_main_pruning_credit": False, "full178_complete": False, "theorem_credit": False, "merge_authorized": False},
        }
        body["canonical_sha256_without_this_field"] = csha(body)
    text = json.dumps(body, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
