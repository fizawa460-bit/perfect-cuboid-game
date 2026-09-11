#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_03_generic_indexed_terminal_adaptive_exceptional_partition as g

v1 = g.v1

SCHEMA = "STAGE32EX5_BC2_17_N354_AUTHORITY_PICARD64_RETARGET_V2"
NORMAL_COUNT = 92
PICARD_RANK = 64
ALL140_COUNT = 140
TARGET_ROW_ID = "g1-d008"
TARGET = (1, 8, 8)
OLD_TARGET = (1, 8, 4)
EXPECTED_NORMAL_MASS = 112
EXPECTED_BLOCK = [0, 112]
EXPECTED_BASE_TERMINAL = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
EXPECTED_ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_MANIFEST_CANONICAL = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PREFIX_CANONICAL = "65a5ab43e44ebb33341c250a8fa2c5ece09999203893f9a76ca46fb037df558f"
EXPECTED_ADAPTER_PREFLIGHT_CANONICAL = "824843776dbf093163a32d8af7dab12dd4e8634789f2d7a2bd0b9ff3a7bde3cf"
EXPECTED_RETAINED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_RETAINED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
N354_AUDIT_REVIEW_ID = 5164850548
N354_AUDITED_HEAD = "e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6"
N354_AUDIT_CANONICAL = "e329916a74eea4471e00f109964afdaa871d4f8614237efed7f0f6e5d9b9c808"
N354_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
EXPECTED_N354_SURVIVOR_STRATA = 17128
EXPECTED_N354_SURVIVOR_TERMINALS = 38560956534397137634780102


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parse_row(row_id: str) -> tuple[int, int]:
    m = re.fullmatch(r"g([01])-d(\d{3})", row_id)
    if not m:
        raise ValueError(f"bad row id: {row_id}")
    return int(m.group(1)), int(m.group(2))


def n354_survives(gg: int, dd: int, ee: int) -> bool:
    return ee % 2 == 0 and 2 * ceil_div(ee, 6) <= dd <= ee + 4 * gg - 4


def enumerate_n354_survivors(rows: set[str]) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for row_id in sorted(rows):
        gg, dd = parse_row(row_id)
        legacy_emin = 8 if gg == 0 else 4
        K = ceil_div(dd - 16 * gg + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * dd) // 5
        for ee in range(effective_emin, emax + 1):
            if n354_survives(gg, dd, ee):
                out.append((gg, dd, ee))
    return out


def linear_expr(coeffs, xs):
    return sum(int(coeffs[j]) * xs[j] for j in range(len(xs)))


def vector_int(v: Matrix) -> list[int]:
    return [int(v[i, 0]) for i in range(v.rows)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=60000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    manifest, manifest_can = v1.load_canonical_json(args.manifest)
    prefix, prefix_can = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_can = v1.load_canonical_json(args.adapter_preflight)
    if manifest_can != EXPECTED_MANIFEST_CANONICAL:
        raise ValueError("FULL178 manifest canonical regression")
    if prefix_can != EXPECTED_PREFIX_CANONICAL:
        raise ValueError("prefix canonical regression")
    if preflight_can != EXPECTED_ADAPTER_PREFLIGHT_CANONICAL:
        raise ValueError("adapter-preflight canonical regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("assignment-order regression")
    if list(v1.KNOWN_LABEL_ORDER) != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("runtime label-order regression")
    if preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct index-to-z shortcut became authorized")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or TARGET_ROW_ID not in rows:
        raise ValueError("FULL178 row population regression")
    survivors = enumerate_n354_survivors(rows)
    if len(survivors) != EXPECTED_N354_SURVIVOR_STRATA:
        raise ValueError(f"N354 survivor replay drift: {len(survivors)}")
    if n354_survives(*OLD_TARGET):
        raise ValueError("old e4 target unexpectedly survives audited N354 filter")
    if TARGET not in survivors:
        raise ValueError("g1-d008/e8 left audited N354 survivor filter")
    same_row = [t for t in survivors if t[:2] == OLD_TARGET[:2]]
    selected = min(same_row, key=lambda t: (abs(t[2] - OLD_TARGET[2]), t[2]))
    if selected != TARGET:
        raise ValueError(f"nearest same-row survivor drift: {selected}")

    indexer = v1.CompressedTerminalIndexer(TARGET[2], TARGET[1])
    if indexer.normal_budget != EXPECTED_NORMAL_MASS:
        raise ValueError("normal-budget regression")
    block_width = indexer.normal_budget + 1
    if [0, block_width - 1] != EXPECTED_BLOCK:
        raise ValueError("first-block width regression")
    base = tuple(int(q) for q in indexer.unrank(0))
    if list(base) != EXPECTED_BASE_TERMINAL:
        raise ValueError(f"rank0 terminal regression: {base}")
    signature = base[:4] + base[5:]
    replay = []
    for rank in range(block_width):
        terminal = tuple(int(q) for q in indexer.unrank(rank))
        if terminal[4] != rank:
            raise ValueError(f"x4 not innermost at rank {rank}")
        if terminal[:4] + terminal[5:] != signature:
            raise ValueError(f"exceptional signature changed inside first block at {rank}")
        if indexer.rank(terminal) != rank:
            raise ValueError(f"rank/unrank regression at {rank}")
        replay.append([rank, list(terminal)])

    terminal_by_label = {int(label): int(value) for label, value in zip(EXPECTED_ASSIGNMENT_ORDER, base)}
    fixed_exceptional = {label: value for label, value in terminal_by_label.items() if label > NORMAL_COUNT}
    fixed_mass = sum(fixed_exceptional.values())
    residual_mass = TARGET[2] - fixed_mass
    if fixed_mass != 2 or residual_mass != 6:
        raise ValueError(f"e8 fixed/residual mass regression: {fixed_mass}/{residual_mass}")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_17_v2_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_17_v2_marking")
    if bundle["canonical_sha256"] != EXPECTED_RETAINED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle regression")
    if marking["canonical_sha256"] != EXPECTED_RETAINED_MARKING_CANONICAL:
        raise ValueError("retained marking regression")
    data = v1.reconstruct_translation_data(marking, bundle)
    P = data["adapter"].pairing_matrix
    bridge = data["bridge"]
    if P.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    xs = [Int(f"x_{j}") for j in range(PICARD_RANK)]
    s = SolverFor("QF_LIA")
    s.set(timeout=args.solver_timeout_ms)
    pairings = [linear_expr(P.row(i), xs) for i in range(ALL140_COUNT)]
    for q in pairings:
        s.add(q >= 0)
    s.add(linear_expr(bridge.degree_functional, xs) == TARGET[1])
    s.add(linear_expr(bridge.exceptional_mass_functional, xs) == TARGET[2])
    s.add(sum(pairings[:NORMAL_COUNT]) == EXPECTED_NORMAL_MASS)
    s.add(sum(pairings[NORMAL_COUNT:]) == TARGET[2])
    for label, value in fixed_exceptional.items():
        s.add(pairings[label - 1] == value)
    x4 = pairings[48]
    s.add(x4 >= 0, x4 <= EXPECTED_NORMAL_MASS)

    result = s.check()
    if result == sat:
        result_status = "SAT"
    elif result == unsat:
        result_status = "UNSAT"
    elif result == unknown:
        result_status = "UNKNOWN"
    else:
        raise ValueError(f"unexpected solver result: {result}")

    witness = None
    if result == sat:
        m = s.model()
        xv = [int(m.eval(q, model_completion=True).as_long()) for q in xs]
        pv = [int(m.eval(q, model_completion=True).as_long()) for q in pairings]
        sat_x4 = pv[48]
        sat_terminal = tuple(int(q) for q in indexer.unrank(sat_x4))
        for label, value in zip(EXPECTED_ASSIGNMENT_ORDER, sat_terminal):
            if pv[label - 1] != int(value):
                raise ValueError("SAT witness fails compressed-terminal replay")
        if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != EXPECTED_NORMAL_MASS or sum(pv[NORMAL_COUNT:]) != TARGET[2]:
            raise ValueError("SAT witness mass/nonnegativity replay regression")
        if v1.evaluate_functional(bridge.degree_functional, xv) != TARGET[1]:
            raise ValueError("SAT witness degree replay regression")
        if v1.evaluate_functional(bridge.exceptional_mass_functional, xv) != TARGET[2]:
            raise ValueError("SAT witness exceptional-mass replay regression")

        x = Matrix(xv)
        translation = {"status": "NOT_INTEGRAL", "rational_solution_exists": False, "integral_solution": False}
        try:
            z = data["C"] * x
            x0 = data["x0_map"] * z
            delta = x - x0
            t, params = data["K"].gauss_jordan_solve(delta)
            unique = params.rows == 0
            integral = unique and all(q.q == 1 for q in t)
            translation = {
                "status": "INTEGRAL" if integral else ("RATIONAL_NONINTEGRAL" if unique else "PARAMETRIC"),
                "rational_solution_exists": True,
                "unique": unique,
                "integral_solution": integral,
                "denominators_sha256": csha([int(q.q) for q in t]) if unique else None,
                "translation_sha256": csha([int(q) for q in t]) if integral else None,
            }
        except ValueError:
            translation = {"status": "NO_RATIONAL_SOLUTION", "rational_solution_exists": False, "integral_solution": False}

        gram = Matrix(bundle["picard_gram_64x64"])
        selfsq = (x.T * gram * x)[0, 0]
        witness = {
            "x4": sat_x4,
            "terminal_rank": sat_x4,
            "terminal": list(sat_terminal),
            "picard64_coordinates_sha256": csha(xv),
            "all140_pairings_sha256": csha(pv),
            "positive_exceptional_support": sum(1 for q in pv[NORMAL_COUNT:] if q > 0),
            "picard_self_intersection": int(selfsq),
            "translation_59d": translation,
        }

    if result_status == "UNSAT":
        status = "PASS_N354_SURVIVOR_FIRST_BLOCK_EXACT_PICARD64_UNSAT"
        next_id = "BC2_18_UNIFORMIZE_PICARD64_INTEGRALITY_ACROSS_N354_SURVIVOR_STRATA"
    elif result_status == "SAT":
        status = "PASS_N354_SURVIVOR_PICARD64_SAT_BOUNDARY_FOUND"
        next_id = "BC2_18_ANALYZE_SAT_WITNESS_59D_INTEGRALITY_AND_DERIVE_MISSING_FILTER"
    else:
        status = "BLOCKED_N354_SURVIVOR_PICARD64_SOLVER_UNKNOWN"
        next_id = "BC2_18_DECOMPOSE_N354_SURVIVOR_PICARD64_PROBE"

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-17",
        "unit": "BC2_17_N354_AUTHORITY_PICARD64_RETARGET_V2",
        "status": status,
        "main_authority": {
            "n354_hostile_audit_review_id": N354_AUDIT_REVIEW_ID,
            "n354_audited_exact_head": N354_AUDITED_HEAD,
            "n354_audit_receipt_canonical_sha256": N354_AUDIT_CANONICAL,
            "n354_result_canonical_sha256": N354_RESULT_CANONICAL,
            "n354_survivor_strata": EXPECTED_N354_SURVIVOR_STRATA,
            "n354_survivor_terminals": EXPECTED_N354_SURVIVOR_TERMINALS,
            "survivor_strata_replayed_from_manifest": len(survivors),
            "n354_is_authority_for_target_selection": True,
            "full178_complete": False,
        },
        "retarget": {
            "prior_e4_target": {"g": 1, "d": 8, "e": 4, "survives_n354": False},
            "selected_target": {"row_id": TARGET_ROW_ID, "g": 1, "d": 8, "e": 8, "survives_n354": True},
            "selection_rule": "nearest audited N354 survivor on the same g1-d008 row as the prior EX5 target",
            "normal_mass": EXPECTED_NORMAL_MASS,
            "first_block": EXPECTED_BLOCK,
            "first_block_width": block_width,
            "base_terminal": list(base),
            "exceptional_signature": list(signature),
            "fixed_exceptional_pairings": {str(k): v for k, v in sorted(fixed_exceptional.items())},
            "fixed_exceptional_mass": fixed_mass,
            "residual_exceptional_mass": residual_mass,
            "rank_unrank_replay_count": block_width,
            "replay_stream_sha256": csha(replay),
        },
        "picard64_probe": {
            "solver": "Z3_QF_LIA",
            "z3_version": get_version_string(),
            "timeout_ms": args.solver_timeout_ms,
            "picard_coordinates_integral": True,
            "all140_nonnegative": True,
            "degree_fixed": TARGET[1],
            "exceptional_mass_fixed": TARGET[2],
            "normal_pairing_mass_fixed": EXPECTED_NORMAL_MASS,
            "terminal_exceptional_pairings_fixed_to_source_rank0_signature": True,
            "x4_symbolic_rank_range": EXPECTED_BLOCK,
            "remaining_exceptional_distribution_free_subject_to_integral_picard64_constraints": True,
            "result": result_status,
            "reason_unknown": s.reason_unknown() if result_status == "UNKNOWN" else None,
            "whole_first_block_picard64_unsat": result_status == "UNSAT",
            "sat_witness": witness,
        },
        "source_locks": {
            "manifest_canonical_sha256": manifest_can,
            "prefix_canonical_sha256": prefix_can,
            "adapter_preflight_canonical_sha256": preflight_can,
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
        },
        "next_exact_unit": {"id": next_id, "heavy_scaleout_authorized": False, "main_promotion_authorized": False},
        "firewalls": {
            "old_e4_prefix_treated_as_current_main_survivors": False,
            "first_block_promoted_to_whole_g1_d008_e8_stratum": False,
            "first_block_promoted_to_full178": False,
            "stage32_main_credit": False,
            "n350_production_coverage_credit": False,
            "receiver_credit": False,
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
        "status": status,
        "n354_survivor_strata": len(survivors),
        "target": list(TARGET),
        "first_block": EXPECTED_BLOCK,
        "fixed_residual_exceptional_mass": [fixed_mass, residual_mass],
        "result": result_status,
        "sat_x4": None if witness is None else witness["x4"],
        "translation_59d": None if witness is None else witness["translation_59d"]["status"],
        "canonical": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
