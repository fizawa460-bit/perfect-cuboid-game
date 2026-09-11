#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_03_generic_indexed_terminal_adaptive_exceptional_partition as g

v1 = g.v1

SCHEMA = "STAGE32EX5_BC2_17_N354_FILTER_PICARD64_RETARGET_V1"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64
ALL140_COUNT = 140
TARGET_ROW_ID = "g1-d008"
TARGET_GENUS = 1
TARGET_DEGREE = 8
OLD_EXCEPTIONAL_MASS = 4
TARGET_EXCEPTIONAL_MASS = 8
EXPECTED_NORMAL_MASS = 112
EXPECTED_BLOCK_WIDTH = 113
EXPECTED_LABEL49 = 49
EXPECTED_ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_MANIFEST_CANONICAL = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PREFIX_CANONICAL = "65a5ab43e44ebb33341c250a8fa2c5ece09999203893f9a76ca46fb037df558f"
EXPECTED_ADAPTER_PREFLIGHT_CANONICAL = "824843776dbf093163a32d8af7dab12dd4e8634789f2d7a2bd0b9ff3a7bde3cf"
EXPECTED_RETAINED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_RETAINED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_SELECTED64_INVERSE_DENOMINATOR = 8
EXPECTED_N354_CANDIDATE_STRATA = 17128
OBSERVED_STAGE32_MAIN_PR = 1753
OBSERVED_STAGE32_MAIN_HEAD = "e82704d054c86fce9d55d5d7daae8f3995a8d9e5"
N353_AUDIT_REVIEW_ID = 5163144778
N353_AUDITED_HEAD = "0f8cee995e5c982cdb7ceceae14d69f91e65588d"
N354_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
N354_REAUDIT_CANDIDATE_HEAD = "e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6"
N354_HANDOFF_CANONICAL = "e5872439a39e4f52847b3f0ffa2eca3399c39a15afdcaa8d4207a4b1deb788bf"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parse_row_id(row_id: str) -> tuple[int, int]:
    m = re.fullmatch(r"g([01])-d(\d{3})", row_id)
    if not m:
        raise ValueError(f"bad row id: {row_id}")
    return int(m.group(1)), int(m.group(2))


def classify(g0: int, d0: int, e0: int) -> str:
    if d0 > e0 + 4 * g0 - 4:
        return "N353_REJECT"
    if e0 & 1:
        return "N354_ODD_E_REJECT"
    if d0 < 2 * ceil_div(e0, 6):
        return "N354_LOWER_INTERVAL_REJECT"
    return "N354_REMAIN"


def enumerate_candidate_strata(rows: set[str]) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for row_id in sorted(rows):
        gg, dd = parse_row_id(row_id)
        legacy_emin = 8 if gg == 0 else 4
        K = ceil_div(dd - 16 * gg + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * dd) // 5
        for ee in range(effective_emin, emax + 1):
            if classify(gg, dd, ee) == "N354_REMAIN":
                out.append((gg, dd, ee))
    return out


def vector_int(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
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
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    prefix, prefix_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    for got, expected, name in (
        (manifest_canonical, EXPECTED_MANIFEST_CANONICAL, "manifest"),
        (prefix_canonical, EXPECTED_PREFIX_CANONICAL, "prefix checkpoint"),
        (preflight_canonical, EXPECTED_ADAPTER_PREFLIGHT_CANONICAL, "adapter preflight"),
    ):
        if got != expected:
            raise ValueError(f"{name} canonical regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("terminal assignment-order regression")
    if v1.EXPECTED_ASSIGNMENT_ORDER != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("EX5 runtime label-order regression")
    if preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct terminal-index to z shortcut became authorized")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or TARGET_ROW_ID not in rows:
        raise ValueError("FULL178 row population regression")

    old_status = classify(TARGET_GENUS, TARGET_DEGREE, OLD_EXCEPTIONAL_MASS)
    if old_status != "N353_REJECT":
        raise ValueError("old EX5 target unexpectedly re-entered current MAIN candidate filter")

    candidates = enumerate_candidate_strata(rows)
    if len(candidates) != EXPECTED_N354_CANDIDATE_STRATA:
        raise ValueError(
            f"N354 candidate-filter stratum count regression: {len(candidates)} != {EXPECTED_N354_CANDIDATE_STRATA}"
        )
    selection_rule = (
        "prefer same (g,d) as prior EX5 target; then minimize |e-4|; "
        "then minimize |d-8|; then lexicographic (g,d,e)"
    )
    selected = min(
        candidates,
        key=lambda t: (
            0 if (t[0], t[1]) == (TARGET_GENUS, TARGET_DEGREE) else 1,
            abs(t[2] - OLD_EXCEPTIONAL_MASS),
            abs(t[1] - TARGET_DEGREE),
            t,
        ),
    )
    if selected != (TARGET_GENUS, TARGET_DEGREE, TARGET_EXCEPTIONAL_MASS):
        raise ValueError(f"candidate retarget selection drift: {selected}")
    if classify(*selected) != "N354_REMAIN":
        raise ValueError("selected retarget left N354 candidate filter")

    indexer = v1.CompressedTerminalIndexer(TARGET_EXCEPTIONAL_MASS, TARGET_DEGREE)
    if indexer.normal_budget != EXPECTED_NORMAL_MASS:
        raise ValueError("retarget normal mass regression")
    block_width = indexer.normal_budget + 1
    if block_width != EXPECTED_BLOCK_WIDTH:
        raise ValueError("retarget first-block width regression")

    base_terminal = tuple(int(q) for q in indexer.unrank(0))
    base_exceptional_signature = base_terminal[:4] + base_terminal[5:]
    if any(base_exceptional_signature):
        raise ValueError("retarget rank0 exceptional signature is not zero")
    replay_stream = []
    for x4_value in range(block_width):
        terminal = tuple(int(q) for q in indexer.unrank(x4_value))
        if terminal[4] != x4_value:
            raise ValueError(f"x4 is not innermost at retarget rank {x4_value}")
        if terminal[:4] + terminal[5:] != base_exceptional_signature:
            raise ValueError(f"exceptional signature changed in retarget first block at rank {x4_value}")
        if indexer.rank(terminal) != x4_value:
            raise ValueError(f"rank/unrank regression at retarget rank {x4_value}")
        replay_stream.append([x4_value, list(terminal)])

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_17_n354_retarget_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_17_n354_retarget_marking")
    if bundle["canonical_sha256"] != EXPECTED_RETAINED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle source-lock regression")
    if marking["canonical_sha256"] != EXPECTED_RETAINED_MARKING_CANONICAL:
        raise ValueError("retained marking source-lock regression")

    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    if P.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(label) for label in g.INDLIST]
    if EXPECTED_LABEL49 not in selected_labels:
        raise ValueError("known-label-49 left selected64 basis")
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(PICARD_RANK)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = g.lcm_denominator(Pinv)
    if den != EXPECTED_SELECTED64_INVERSE_DENOMINATOR:
        raise ValueError("selected64 inverse denominator regression")
    Binv_q = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv_q):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv_q[i, j]) for j in range(Binv_q.cols)] for i in range(Binv_q.rows)])
    if Psel * Binv != den * Matrix.eye(PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")
    Anum_q = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum_q):
        raise ValueError("all140 selected-coordinate map became nonintegral")
    Anum = Matrix([[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)])

    terminal_by_label = {
        int(label): int(value)
        for label, value in zip(EXPECTED_ASSIGNMENT_ORDER, base_terminal)
    }
    if terminal_by_label[EXPECTED_LABEL49] != 0:
        raise ValueError("retarget base x4 is not zero")
    terminal_exceptional_labels = sorted(label for label in terminal_by_label if label > NORMAL_COUNT)
    if len(terminal_exceptional_labels) != 10:
        raise ValueError("retarget terminal exceptional-label count regression")
    if any(terminal_by_label[label] != 0 for label in terminal_exceptional_labels):
        raise ValueError("retarget first-block exceptional terminal values are not all zero")

    y = [Int(f"y_{j}") for j in range(PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)

    for j, label in enumerate(selected_labels):
        ub = TARGET_EXCEPTIONAL_MASS if label > NORMAL_COUNT else EXPECTED_NORMAL_MASS
        solver.add(y[j] >= 0, y[j] <= ub)
        solver.add(p[label - 1] == y[j])
    for i in range(ALL140_COUNT):
        ub = EXPECTED_NORMAL_MASS if i < NORMAL_COUNT else TARGET_EXCEPTIONAL_MASS
        solver.add(p[i] >= 0, p[i] <= ub)
        solver.add(
            den * p[i]
            == sum(int(Anum[i, j]) * y[j] for j in range(PICARD_RANK))
        )
    for i in range(PICARD_RANK):
        numerator = sum(int(Binv[i, j]) * y[j] for j in range(PICARD_RANK))
        solver.add(numerator % den == 0)
    solver.add(sum(p[:NORMAL_COUNT]) == EXPECTED_NORMAL_MASS)
    solver.add(sum(p[NORMAL_COUNT:]) == TARGET_EXCEPTIONAL_MASS)
    for label in terminal_exceptional_labels:
        solver.add(p[label - 1] == 0)
    x4 = p[EXPECTED_LABEL49 - 1]
    solver.add(x4 >= 0, x4 <= EXPECTED_NORMAL_MASS)

    result = solver.check()
    if result == sat:
        result_status = "SAT"
    elif result == unsat:
        result_status = "UNSAT"
    elif result == unknown:
        result_status = "UNKNOWN"
    else:
        raise ValueError(f"unexpected solver result: {result}")

    sat_witness = None
    if result == sat:
        model = solver.model()
        yv = [int(model.eval(q, model_completion=True).as_long()) for q in y]
        pv = [int(model.eval(q, model_completion=True).as_long()) for q in p]
        xnum = Binv * Matrix(yv)
        if any(int(q) % den for q in xnum):
            raise ValueError("SAT selected64 vector left integral Picard64 image")
        x = Matrix([int(q) // den for q in xnum])
        xv = vector_int(x)
        if vector_int(P * x) != pv:
            raise ValueError("SAT all140 pairing replay regression")
        if min(pv) < 0:
            raise ValueError("SAT all140 nonnegativity regression")
        if sum(pv[:NORMAL_COUNT]) != EXPECTED_NORMAL_MASS:
            raise ValueError("SAT normal-mass regression")
        if sum(pv[NORMAL_COUNT:]) != TARGET_EXCEPTIONAL_MASS:
            raise ValueError("SAT exceptional-mass regression")
        d_actual = v1.evaluate_functional(bridge.degree_functional, xv)
        e_actual = v1.evaluate_functional(bridge.exceptional_mass_functional, xv)
        if (d_actual, e_actual) != (TARGET_DEGREE, TARGET_EXCEPTIONAL_MASS):
            raise ValueError("SAT d/e slice regression")
        sat_x4 = int(model.eval(x4, model_completion=True).as_long())
        sat_terminal = tuple(int(q) for q in indexer.unrank(sat_x4))
        for label, value in zip(EXPECTED_ASSIGNMENT_ORDER, sat_terminal):
            if pv[label - 1] != int(value):
                raise ValueError("SAT witness does not match retarget compressed terminal")

        z = data["C"] * x
        x0 = data["x0_map"] * z
        delta = x - x0
        t, params = data["K"].gauss_jordan_solve(delta)
        translation_unique = params.rows == 0
        translation_integral = translation_unique and all(sympy.denom(q) == 1 for q in t)
        translation_sha = None
        if translation_integral:
            tint = Matrix([int(q) for q in t])
            if data["K"] * tint != delta:
                raise ValueError("SAT integral 59D translation reconstruction regression")
            translation_sha = csha(vector_int(tint))

        gram = Matrix(bundle["picard_gram_64x64"])
        selfsq_q = (x.T * gram * x)[0, 0]
        if sympy.denom(selfsq_q) != 1:
            raise ValueError("SAT Picard self-intersection became nonintegral")
        sat_witness = {
            "x4": sat_x4,
            "terminal_rank": sat_x4,
            "terminal_pairings": list(sat_terminal),
            "picard_coordinates_sha256": csha(xv),
            "selected64_pairings_sha256": csha(yv),
            "all140_pairings_sha256": csha(pv),
            "positive_exceptional_support": sum(1 for q in pv[NORMAL_COUNT:] if q > 0),
            "picard_self_intersection": int(selfsq_q),
            "translation_59d_unique": translation_unique,
            "translation_59d_integral": translation_integral,
            "translation_59d_sha256": translation_sha,
        }

    status = {
        "UNSAT": "PASS_RETARGET_FIRST_X4_BLOCK_EXACT_PICARD64_UNSAT",
        "SAT": "PASS_RETARGET_FOUND_EXACT_PICARD64_SAT_BOUNDARY",
        "UNKNOWN": "BLOCKED_RETARGET_SOLVER_UNKNOWN",
    }[result_status]
    next_unit = {
        "UNSAT": "BC2_18_DERIVE_UNIFORM_PICARD64_INTEGRALITY_LEMMA_FROM_E4_E8",
        "SAT": "BC2_18_ANALYZE_N354_RETARGET_SAT_WITNESS_AND_MISSING_INTEGRALITY_FILTER",
        "UNKNOWN": "BC2_18_RETARGET_SOLVER_DECOMPOSITION",
    }[result_status]

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-17",
        "unit": "BC2_17_N354_FILTER_PICARD64_RETARGET",
        "status": status,
        "cycle": {
            "route_status": "PASS_NEW_GATE_FROM_STRONGER_VIEW",
            "active_receiver": "N354-candidate-filtered FULL178 strata -> exact terminal/Picard64/integrality obstruction",
            "live_candidates": 1,
            "untested_candidates": 2,
            "exhaustive_view_audit": False,
            "blind_rediscovery": False,
            "split_triggered": False,
            "parking_audit_complete": False,
            "new_view": "retarget Picard64 from stale g1-d008/e4 to nearest N354 candidate g1-d008/e8 before any further rank-by-rank continuation",
            "new_view_source": "INTERNAL_DERIVATION",
        },
        "main_candidate_filter": {
            "stage32_main_pr": OBSERVED_STAGE32_MAIN_PR,
            "observed_main_head": OBSERVED_STAGE32_MAIN_HEAD,
            "n353_hostile_audit_review_id": N353_AUDIT_REVIEW_ID,
            "n353_audited_head": N353_AUDITED_HEAD,
            "n354_result_canonical_sha256": N354_RESULT_CANONICAL,
            "n354_reaudit_candidate_head": N354_REAUDIT_CANDIDATE_HEAD,
            "n354_handoff_canonical_sha256": N354_HANDOFF_CANONICAL,
            "n354_status_observed": "REAUDIT_REQUIRED_AFTER_ORDERING_REPAIR",
            "candidate_strata_count_replayed": len(candidates),
            "used_as_mathematical_authority": False,
            "used_for_target_selection_only": True,
            "selection_rule": selection_rule,
        },
        "retarget": {
            "prior_target": {"g": TARGET_GENUS, "d": TARGET_DEGREE, "e": OLD_EXCEPTIONAL_MASS, "filter_status": old_status},
            "selected_target": {"row_id": TARGET_ROW_ID, "g": TARGET_GENUS, "d": TARGET_DEGREE, "e": TARGET_EXCEPTIONAL_MASS, "filter_status": classify(TARGET_GENUS, TARGET_DEGREE, TARGET_EXCEPTIONAL_MASS)},
            "same_row_as_prior_target": True,
            "minimal_positive_e_shift_within_same_row": True,
            "normal_mass": EXPECTED_NORMAL_MASS,
            "first_block_rank_start": 0,
            "first_block_rank_end": EXPECTED_NORMAL_MASS,
            "first_block_width": block_width,
            "first_block_exceptional_signature": list(base_exceptional_signature),
            "all_rank_unrank_replays_exact": True,
            "replay_stream_sha256": csha(replay_stream),
        },
        "picard64_integrality_probe": {
            "solver": "Z3_QF_LIA",
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "selected64_inverse_denominator": den,
            "all140_nonnegativity_enforced": True,
            "normal_mass_equality_enforced": True,
            "exceptional_mass_equality_enforced": True,
            "selected64_to_picard64_integrality_congruences_enforced": True,
            "ten_terminal_exceptional_pairings_fixed_zero": True,
            "x4_symbolic_over_entire_first_block": [0, EXPECTED_NORMAL_MASS],
            "remaining_selected_and_unselected_exceptional_distribution_free_subject_to_exact_picard64_constraints": True,
            "result": result_status,
            "reason_unknown": solver.reason_unknown() if result_status == "UNKNOWN" else None,
            "whole_first_block_exact_unsat": result_status == "UNSAT",
            "sat_witness": sat_witness,
        },
        "source_locks": {
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": prefix_canonical,
            "adapter_preflight_canonical_sha256": preflight_canonical,
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
        },
        "next_exact_unit": {
            "id": next_unit,
            "heavy_scaleout_authorized": False,
            "main_promotion_authorized": False,
        },
        "firewalls": {
            "n354_candidate_filter_promoted_to_authority": False,
            "old_e4_local_prefix_promoted_to_current_main_population": False,
            "retarget_probe_promoted_to_whole_selected_stratum": False,
            "retarget_probe_promoted_to_full178": False,
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
        "candidate_strata": len(candidates),
        "old_target_status": old_status,
        "retarget": [TARGET_GENUS, TARGET_DEGREE, TARGET_EXCEPTIONAL_MASS],
        "first_block": [0, EXPECTED_NORMAL_MASS],
        "result": result_status,
        "sat_x4": None if sat_witness is None else sat_witness["x4"],
        "canonical": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
