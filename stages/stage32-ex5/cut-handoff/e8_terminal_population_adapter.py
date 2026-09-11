#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B2 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
N220_AUDITED = ROOT / "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json"
N355_RESULT = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-RESULT.json"
N355_AUDIT = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-HOSTILE-AUDIT-PASS.json"
sys.path.insert(0, str(B2))
sys.path.insert(0, str(RESIDUAL))

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18
from compressed_terminal_family import exceptional_terminal_count
from compressed_terminal_indexer import CompressedTerminalIndexer

SCHEMA = "STAGE32EX5_E8_CURRENT_MAIN_TERMINAL_POPULATION_ADAPTER_V2"
ROW_ID = "g1-d008"
TARGET_G = 1
TARGET_D = 8
TARGET_E = 8
NORMAL_BUDGET = 112
BLOCK_WIDTH = NORMAL_BUDGET + 1
UNFILTERED_BLOCK_COUNT = 11318
UNFILTERED_TERMINAL_COUNT = 1278934
CURRENT_MAIN_BLOCK_COUNT = 7596
CURRENT_MAIN_TERMINAL_COUNT = 858348
CURRENT_MAIN_BLOCK_STREAM_SHA256 = "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"
CURRENT_MAIN_RAW_PARENT_CANDIDATES = 12357387
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X4_LABEL = 49
N355_GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
EXPECTED_DEN = 8
EXPECTED_SELECTED_EXCEPTIONAL = 29
EXPECTED_FIXED_EXCEPTIONAL = 10
EXPECTED_FREE_SELECTED_EXCEPTIONAL = 19
FIRST_BLOCK_PARENT_COUNT = 7336
FIRST_BLOCK_STREAM_SHA256 = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
BC217 = B2 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
SOURCE_LOCKS = {
    "n220_audited_blob": "f5f0e902062c9fafc9f03fe8a203d744cf58281e",
    "n355_result_blob": "0f30517cc5007ea435f4183201fc6cad699dd635",
    "n355_result_canonical": "7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775",
    "n355_audit_blob": "033294f56fb86d81b7aa43758a51a39747ccc082",
    "n355_audit_canonical": "d6bda89f94eb57bf021f0acbbc5000e198f1805c09da3e5f9a531d20b70ce004",
    "n355_audit_exact_head": "3f3aadd2e5ada2a0a02a69490d6d659c02762682",
    "n355_audit_review": 5165895301,
}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def checked_canonical(path: Path, blob: str, canonical: str) -> dict:
    if git_blob(path) != blob:
        raise ValueError(f"source-lock blob drift: {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    if claimed != canonical or csha(body) != canonical:
        raise ValueError(f"canonical drift: {path.relative_to(ROOT)}")
    return obj


def load_current_main_prefix_contract() -> None:
    if git_blob(N220_AUDITED) != SOURCE_LOCKS["n220_audited_blob"]:
        raise ValueError("N220 audited authority blob drift")
    n220 = json.loads(N220_AUDITED.read_text())
    if n220.get("status") != "DONE_AUDITED_EXACT_NECESSARY_PREFIX_PRUNING":
        raise ValueError("N220 audited status regression")
    if n220.get("hostile_audit", {}).get("result") != "PASS":
        raise ValueError("N220 hostile-audit status regression")
    if n220.get("audited_predicate", {}).get("necessary_form") != "S10 + min(38, e-M10) >= ceil((d-16g+16)/4)":
        raise ValueError("N220 predicate regression")

    n355 = checked_canonical(
        N355_RESULT,
        SOURCE_LOCKS["n355_result_blob"],
        SOURCE_LOCKS["n355_result_canonical"],
    )
    cut = n355.get("full_prefix_cut", {})
    if cut.get("equivalent_cut") != "max(group1_sum,group2_sum,group3_sum)<=floor(d/2)":
        raise ValueError("N355 full-prefix equivalent cut regression")
    if cut.get("known_groups") != N355_GROUPS:
        raise ValueError("N355 known-group partition regression")
    audit = checked_canonical(
        N355_AUDIT,
        SOURCE_LOCKS["n355_audit_blob"],
        SOURCE_LOCKS["n355_audit_canonical"],
    )
    if audit.get("status") != "PASS" or audit.get("audited_exact_head") != SOURCE_LOCKS["n355_audit_exact_head"] or audit.get("review_id") != SOURCE_LOCKS["n355_audit_review"]:
        raise ValueError("N355 hostile-audit receipt regression")


def stream_update(h, record: dict) -> None:
    h.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n")


def indexer() -> CompressedTerminalIndexer:
    idx = CompressedTerminalIndexer(TARGET_E, TARGET_D)
    if idx.normal_budget != NORMAL_BUDGET:
        raise ValueError("e8 normal-budget regression")
    if idx.exceptional_count != UNFILTERED_BLOCK_COUNT:
        raise ValueError(f"e8 block-count regression: {idx.exceptional_count}")
    if idx.terminal_count != UNFILTERED_TERMINAL_COUNT:
        raise ValueError(f"e8 terminal-count regression: {idx.terminal_count}")
    return idx


def block_terminal_range(block_index: int) -> tuple[int, int]:
    block_index = int(block_index)
    if not 0 <= block_index < UNFILTERED_BLOCK_COUNT:
        raise ValueError(f"block index outside 0..{UNFILTERED_BLOCK_COUNT - 1}: {block_index}")
    lo = block_index * BLOCK_WIDTH
    return lo, lo + BLOCK_WIDTH - 1


def _prefix_filter_from_base(base: tuple[int, ...]) -> dict:
    by_label = {int(label): int(value) for label, value in zip(ASSIGNMENT_ORDER, base)}
    fixed = {label: value for label, value in by_label.items() if label != X4_LABEL}
    mass = sum(fixed.values())
    support = sum(1 for value in fixed.values() if value > 0)
    n220_required = -((-(TARGET_D - 16 * TARGET_G + 16)) // 4)
    n220_pass = support + min(38, TARGET_E - mass) >= n220_required
    group_sums = [sum(fixed[label] for label in group) for group in N355_GROUPS]
    n355_pass = max(group_sums) <= TARGET_D // 2
    return {
        "fixed": fixed,
        "fixed_mass": mass,
        "support": support,
        "n220_required_support": n220_required,
        "n220_pass": n220_pass,
        "n355_group_sums": group_sums,
        "n355_pass": n355_pass,
        "current_main_audited_prefix_survivor": bool(n220_pass and n355_pass),
    }


def block_signature(block_index: int, idx: CompressedTerminalIndexer | None = None) -> dict:
    idx = idx or indexer()
    lo, hi = block_terminal_range(block_index)
    base = tuple(int(v) for v in idx.unrank(lo))
    if base[4] != 0 or idx.rank(base) != lo:
        raise ValueError("block-base rank/unrank regression")
    top = tuple(int(v) for v in idx.unrank(hi))
    if top[4] != NORMAL_BUDGET or idx.rank(top) != hi:
        raise ValueError("block-top rank/unrank regression")
    if base[:4] + base[5:] != top[:4] + top[5:]:
        raise ValueError("exceptional signature changed across block")
    f = _prefix_filter_from_base(base)
    fixed = f["fixed"]
    if any(label <= d18.NORMAL_COUNT for label in fixed):
        raise ValueError("terminal fixed coordinate unexpectedly nonexceptional")
    residual = TARGET_E - int(f["fixed_mass"])
    expected_candidates = math.comb(residual + EXPECTED_FREE_SELECTED_EXCEPTIONAL, EXPECTED_FREE_SELECTED_EXCEPTIONAL)
    return {
        "block_index": int(block_index),
        "terminal_rank_range": [lo, hi],
        "terminal_count": BLOCK_WIDTH,
        "base_terminal": list(base),
        "exceptional_signature": list(base[:4] + base[5:]),
        "fixed_exceptional_pairings": {str(k): int(v) for k, v in sorted(fixed.items())},
        "fixed_exceptional_mass": int(f["fixed_mass"]),
        "known_exceptional_support": int(f["support"]),
        "residual_exceptional_mass": residual,
        "n220_required_support": int(f["n220_required_support"]),
        "n220_support_pass": bool(f["n220_pass"]),
        "n355_known_group_sums": list(f["n355_group_sums"]),
        "n355_full_prefix_pass": bool(f["n355_pass"]),
        "current_main_audited_prefix_survivor": bool(f["current_main_audited_prefix_survivor"]),
        "raw_selected_parent_candidate_count": expected_candidates,
    }


def current_main_survivor_block_indices() -> list[int]:
    idx = indexer()
    out = []
    h = hashlib.sha256()
    raw_total = 0
    for block_index in range(UNFILTERED_BLOCK_COUNT):
        sig = block_signature(block_index, idx)
        if not sig["current_main_audited_prefix_survivor"]:
            continue
        out.append(block_index)
        h.update(f"{block_index}\n".encode())
        raw_total += int(sig["raw_selected_parent_candidate_count"])
    if len(out) != CURRENT_MAIN_BLOCK_COUNT:
        raise ValueError(f"current-MAIN e8 block-count regression: {len(out)}")
    if h.hexdigest() != CURRENT_MAIN_BLOCK_STREAM_SHA256:
        raise ValueError("current-MAIN survivor block-stream regression")
    if raw_total != CURRENT_MAIN_RAW_PARENT_CANDIDATES:
        raise ValueError("current-MAIN raw parent-candidate accounting regression")
    return out


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
    load_current_main_prefix_contract()
    bc217 = json.loads(BC217.read_text())
    if bc217.get("canonical_sha256_without_this_field") != d18.EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 target-authority canonical regression")
    target = bc217["retarget"]["selected_target"]
    if target != {"row_id": ROW_ID, "g": TARGET_G, "d": TARGET_D, "e": TARGET_E, "survives_n354": True}:
        raise ValueError("BC2-17 N354-survivor target regression")

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
    x4_check = d18.build_hnf_extension_check(B, den, exceptional_positions + [x4_pos], [j for j in normal_positions if j != x4_pos])
    return Geometry(labels, exceptional_labels, normal_positions, exceptional_positions, pos_by_label, den, B, full_check, x4_check)


def iter_parent_population(block_index: int, geometry: Geometry | None = None):
    sig = block_signature(block_index)
    if not sig["current_main_audited_prefix_survivor"]:
        raise ValueError(f"block {block_index} is rejected by audited current-MAIN N220/N355 prefix authority")
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
            yield {"selected_exceptional_pairings": yE, "selected_residual_mass": int(sum(comp)), "x4_allowed_residues_mod8": allowed}


def summarize_block(block_index: int, geometry: Geometry | None = None) -> dict:
    g = geometry or load_geometry()
    sig = block_signature(block_index)
    if not sig["current_main_audited_prefix_survivor"]:
        raise ValueError(f"cannot hand rejected block {block_index} to CUT")
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
    out = {**sig, "modular_feasible_parent_count": count, "parent_stream_sha256": h.hexdigest(), "x4_allowed_residue_union_mod8": sorted(residues), "feasible_selected_residual_mass_histogram": {str(k): v for k, v in sorted(mass_hist.items())}}
    if block_index == 0:
        if count != FIRST_BLOCK_PARENT_COUNT or h.hexdigest() != FIRST_BLOCK_STREAM_SHA256:
            raise ValueError("first-block BC2-18/CUT102 replay regression")
        out["first_block_replay"] = True
    return out


def describe() -> dict:
    load_current_main_prefix_contract()
    idx = indexer()
    exact_by_mass = []
    prior = 0
    raw_unfiltered = 0
    survivor_by_mass = {m: 0 for m in range(TARGET_E + 1)}
    rejected_by_mass = {m: 0 for m in range(TARGET_E + 1)}
    survivor_raw = 0
    survivor_h = hashlib.sha256()
    survivor_count = 0
    for block_index in range(UNFILTERED_BLOCK_COUNT):
        sig = block_signature(block_index, idx)
        m = int(sig["fixed_exceptional_mass"])
        raw = int(sig["raw_selected_parent_candidate_count"])
        if sig["current_main_audited_prefix_survivor"]:
            survivor_by_mass[m] += 1
            survivor_count += 1
            survivor_raw += raw
            survivor_h.update(f"{block_index}\n".encode())
        else:
            rejected_by_mass[m] += 1
    for mass in range(TARGET_E + 1):
        cumulative = exceptional_terminal_count(mass)
        exact = cumulative - prior
        residual = TARGET_E - mass
        raw = math.comb(residual + EXPECTED_FREE_SELECTED_EXCEPTIONAL, EXPECTED_FREE_SELECTED_EXCEPTIONAL)
        exact_by_mass.append({"fixed_exceptional_mass": mass, "unfiltered_block_count": exact, "current_main_survivor_block_count": survivor_by_mass[mass], "current_main_rejected_block_count": rejected_by_mass[mass], "residual_exceptional_mass": residual, "raw_parent_candidates_per_block": raw})
        raw_unfiltered += exact * raw
        prior = cumulative
    if prior != UNFILTERED_BLOCK_COUNT or raw_unfiltered != 12458750:
        raise ValueError("whole e8 adapter universe accounting regression")
    if survivor_count != CURRENT_MAIN_BLOCK_COUNT or survivor_h.hexdigest() != CURRENT_MAIN_BLOCK_STREAM_SHA256 or survivor_raw != CURRENT_MAIN_RAW_PARENT_CANDIDATES:
        raise ValueError("current-MAIN e8 handoff population accounting regression")
    return {
        "schema": SCHEMA,
        "target": {"row_id": ROW_ID, "g": TARGET_G, "d": TARGET_D, "e": TARGET_E, "n354_survivor_stratum": True, "current_authoritative_prefix_frontier": "AUDITED_N220_PLUS_AUDITED_N355_FULL_PREFIX"},
        "adapter_universe": {"exceptional_signature_block_count": UNFILTERED_BLOCK_COUNT, "terminal_block_width": BLOCK_WIDTH, "terminal_count": UNFILTERED_TERMINAL_COUNT, "canonical_index_order": idx.certificate()["canonical_index_order"], "full_materialization_required": False, "random_access_by_exceptional_rank": True, "raw_selected_parent_candidates_if_all_blocks_materialized": raw_unfiltered},
        "current_main_handoff_population": {"block_count": survivor_count, "terminal_count": survivor_count * BLOCK_WIDTH, "rejected_block_count": UNFILTERED_BLOCK_COUNT - survivor_count, "rejected_terminal_count": (UNFILTERED_BLOCK_COUNT - survivor_count) * BLOCK_WIDTH, "survivor_block_index_stream_sha256": survivor_h.hexdigest(), "raw_selected_parent_candidates": survivor_raw, "block_distribution_by_fixed_exceptional_mass": exact_by_mass},
        "authority": {"n220_audited_predicate": "S10 + min(38,e-M10) >= ceil((d-16g+16)/4)", "n355_audited_full_prefix_cut": "max(sum[101,102,103],sum[97,98,99],sum[93,94,95,96])<=floor(d/2)", "n355_audit_exact_head": SOURCE_LOCKS["n355_audit_exact_head"], "n355_audit_review": SOURCE_LOCKS["n355_audit_review"], "n356_candidate_not_consumed": True},
        "semantics": {"block_index": "exceptional_rank in CompressedTerminalIndexer(e=8,d=8)", "terminal_rank_range": "[block_index*113, block_index*113+112]", "x4_is_innermost_coordinate": True, "current_main_filter_is_block_constant": True, "parent_population": "all HNF-integrality-feasible selected-exceptional completions for a current-MAIN audited-prefix-surviving fixed terminal exceptional signature, carrying exact x4 residue classes mod 8", "cut_consumption": "CUT may request any surviving block lazily; no block-specific Picard64 adapter is required"},
        "credit": {"producer_interface_only": True, "stage32_main_pruning_credit": False, "full178_complete": False, "theorem_credit": False, "merge_authorized": False},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--describe", action="store_true")
    ap.add_argument("--survivor-offset", type=int)
    ap.add_argument("--survivor-count", type=int, default=1)
    ap.add_argument("--max-raw-candidates", type=int, default=1000000)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    if args.describe:
        body = describe()
    else:
        if args.survivor_offset is None or args.survivor_count <= 0:
            raise ValueError("positive --survivor-count and --survivor-offset are required")
        survivors = current_main_survivor_block_indices()
        start = int(args.survivor_offset)
        end = start + int(args.survivor_count)
        if start < 0 or end > len(survivors):
            raise ValueError("requested survivor wave outside current-MAIN e8 handoff population")
        block_indices = survivors[start:end]
        signatures = [block_signature(i) for i in block_indices]
        raw = sum(int(s["raw_selected_parent_candidate_count"]) for s in signatures)
        if raw > args.max_raw_candidates:
            raise ValueError(f"raw candidate resource gate: {raw}>{args.max_raw_candidates}")
        g = load_geometry()
        records = [summarize_block(i, g) for i in block_indices]
        body = {"schema": "STAGE32EX5_E8_CURRENT_MAIN_HANDOFF_WAVE_V1", "adapter_schema": SCHEMA, "target": {"row_id": ROW_ID, "g": TARGET_G, "d": TARGET_D, "e": TARGET_E}, "survivor_offset_range": [start, end - 1], "block_indices": block_indices, "block_index_minmax": [min(block_indices), max(block_indices)], "block_count": len(block_indices), "terminal_count": len(block_indices) * BLOCK_WIDTH, "raw_parent_candidates_checked": raw, "blocks": records, "authority": {"n220_audited": True, "n355_full_prefix_audited": True, "n356_candidate_consumed": False}, "firewalls": {"stage32_main_pruning_credit": False, "full178_complete": False, "theorem_credit": False, "merge_authorized": False}}
        body["canonical_sha256_without_this_field"] = csha(body)
    text = json.dumps(body, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
