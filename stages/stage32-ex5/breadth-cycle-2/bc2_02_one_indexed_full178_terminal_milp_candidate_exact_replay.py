#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
import sympy
from scipy.optimize import Bounds, LinearConstraint, milp
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat

import bc2_02_one_indexed_full178_terminal_to_picard64_completion as v1
from pairing_prefix_engine import INDLIST

SCHEMA = "STAGE32EX5_BC2_02_ONE_INDEXED_FULL178_TERMINAL_MILP_CANDIDATE_EXACT_REPLAY_V1"
NORMAL_COUNT = 92


def ceil_div(a: int, b: int) -> int:
    return -((-int(a)) // int(b))


def lcm_denominator(m: Matrix) -> int:
    den = 1
    for value in m:
        den = math.lcm(den, int(sympy.denom(value)))
    return den


def vector_int(v: Matrix) -> list[int]:
    return [int(v[i, 0]) for i in range(v.rows)]


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--prior-v1", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--milp-wall-seconds", type=int, default=60)
    ap.add_argument("--exact-replay-timeout-ms", type=int, default=30000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.milp_wall_seconds <= 0 or args.exact_replay_timeout_ms <= 0:
        raise ValueError("timeouts must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    if v1.ROW_ID not in v1.parse_manifest_rows(manifest):
        raise ValueError("representative row absent from FULL178 manifest")
    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    adapter_preflight, adapter_preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    prior, prior_canonical = v1.load_canonical_json(args.prior_v1)
    if prior["schema"] != v1.SCHEMA or prior["result"]["status"] != "UNKNOWN":
        raise ValueError("expected retained V1 UNKNOWN timeout prototype")
    if prior["exact_completion_problem"]["reason_unknown"] != "timeout":
        raise ValueError("retained V1 UNKNOWN is not timeout")
    if adapter_preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct index-to-z shortcut became authorized")
    if checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("compressed terminal label-order regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    terminal = tuple(int(q) for q in indexer.unrank(v1.TERMINAL_RANK))
    if indexer.rank(terminal) != v1.TERMINAL_RANK:
        raise ValueError("compressed terminal rank/unrank regression")
    if list(terminal) != prior["indexed_terminal"]["pairings"]:
        raise ValueError("retained V1 terminal pairing regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_02_milp_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_02_milp_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    if P.shape != (v1.ALL140_COUNT, v1.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != 132:
        raise ValueError("representative normal-mass regression")
    if bridge.certificate.get("mass_identity_exact_on_picard64") is not True:
        raise ValueError("Picard64 mass identity source-lock regression")

    # Coordinate-correct redundant Picard64 bounds derived from the ACTUAL
    # all140 pairing matrix in the retained x basis used by this script.
    selected_indices = [int(label) - 1 for label in INDLIST]
    Psel = P.extract(selected_indices, list(range(v1.PICARD_RANK)))
    if int(Psel.det()) == 0:
        raise ValueError("actual selected64 pairing matrix is singular")
    Pinv = Psel.inv()
    den = lcm_denominator(Pinv)
    Binv = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv[i, j]) for j in range(Binv.cols)] for i in range(Binv.rows)])
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("actual selected64 inverse reconstruction regression")
    selected_ubs = [v1.EXCEPTIONAL_MASS if int(label) > NORMAL_COUNT else normal_mass for label in INDLIST]
    x_bounds: list[tuple[int, int]] = []
    for i in range(v1.PICARD_RANK):
        nlo = 0
        nhi = 0
        for j, ub in enumerate(selected_ubs):
            coeff = int(Binv[i, j])
            if coeff < 0:
                nlo += coeff * int(ub)
            elif coeff > 0:
                nhi += coeff * int(ub)
        lo = ceil_div(nlo, den)
        hi = nhi // den
        if lo > hi:
            raise ValueError("derived exact Picard64 coordinate bound is empty")
        x_bounds.append((lo, hi))

    rows: list[np.ndarray] = []
    lbs: list[float] = []
    ubs: list[float] = []

    def add_row(coeffs, lo, hi) -> None:
        row = np.asarray([float(int(q)) for q in coeffs], dtype=np.float64)
        if not np.isfinite(row).all():
            raise ValueError("MILP coefficient overflow")
        rows.append(row)
        lbs.append(float(lo))
        ubs.append(float(hi))

    for i in range(v1.ALL140_COUNT):
        ub = normal_mass if i < NORMAL_COUNT else v1.EXCEPTIONAL_MASS
        add_row(P.row(i), 0, ub)
    add_row(bridge.degree_functional, v1.DEGREE, v1.DEGREE)
    add_row(bridge.exceptional_mass_functional, v1.EXCEPTIONAL_MASS, v1.EXCEPTIONAL_MASS)
    add_row([sum(int(P[i, j]) for i in range(NORMAL_COUNT)) for j in range(v1.PICARD_RANK)], normal_mass, normal_mass)
    add_row([sum(int(P[i, j]) for i in range(NORMAL_COUNT, v1.ALL140_COUNT)) for j in range(v1.PICARD_RANK)], v1.EXCEPTIONAL_MASS, v1.EXCEPTIONAL_MASS)
    for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal):
        add_row(P.row(int(label) - 1), int(value), int(value))

    A = np.vstack(rows)
    lb = np.asarray(lbs, dtype=np.float64)
    ub = np.asarray(ubs, dtype=np.float64)
    lower = np.asarray([float(lo) for lo, _ in x_bounds], dtype=np.float64)
    upper = np.asarray([float(hi) for _, hi in x_bounds], dtype=np.float64)
    integrality = np.ones(v1.PICARD_RANK, dtype=np.int8)

    started = time.perf_counter()
    candidate_result = milp(
        c=np.zeros(v1.PICARD_RANK, dtype=np.float64),
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(A, lb, ub),
        options={"time_limit": float(args.milp_wall_seconds), "presolve": True, "mip_rel_gap": 0.0},
    )
    elapsed = time.perf_counter() - started

    status = "UNKNOWN_NO_EXACT_CANDIDATE"
    reject_reason = None
    candidate_x = None
    witness_r_reduced = None
    completion = None
    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank": v1.TERMINAL_RANK,
        "terminal_pairings": list(terminal),
    }

    if candidate_result.x is not None:
        rounded = [int(round(float(q))) for q in candidate_result.x]
        max_rounding_error = max(abs(float(candidate_result.x[i]) - rounded[i]) for i in range(v1.PICARD_RANK))
        candidate_x = rounded

        # Exact replay first in integer arithmetic.
        x = Matrix(rounded)
        pv = vector_int(P * x)
        exact_ok = True
        reasons = []
        if min(pv) < 0:
            exact_ok = False; reasons.append("negative_pairing")
        if any(pv[i] > (normal_mass if i < NORMAL_COUNT else v1.EXCEPTIONAL_MASS) for i in range(v1.ALL140_COUNT)):
            exact_ok = False; reasons.append("pairing_upper_bound")
        if sum(pv[:NORMAL_COUNT]) != normal_mass:
            exact_ok = False; reasons.append("normal_mass")
        if sum(pv[NORMAL_COUNT:]) != v1.EXCEPTIONAL_MASS:
            exact_ok = False; reasons.append("exceptional_mass")
        d_actual = v1.evaluate_functional(bridge.degree_functional, rounded)
        e_actual = v1.evaluate_functional(bridge.exceptional_mass_functional, rounded)
        a_actual = v1.evaluate_functional(bridge.first_normal_half_functional, rounded)
        if (d_actual, e_actual) != (v1.DEGREE, v1.EXCEPTIONAL_MASS):
            exact_ok = False; reasons.append("d_e_slice")
        for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal):
            if pv[int(label) - 1] != int(value):
                exact_ok = False; reasons.append(f"terminal_{label}")

        # Pin the numerical candidate into the exact original QF_LIA model.
        xv = [Int(f"x_{j}") for j in range(v1.PICARD_RANK)]
        exact = SolverFor("QF_LIA")
        exact.set(timeout=args.exact_replay_timeout_ms)
        for j, value in enumerate(rounded):
            exact.add(xv[j] == int(value))
        for i in range(v1.ALL140_COUNT):
            expr = v1.linear_expr(P.row(i), xv)
            ub_i = normal_mass if i < NORMAL_COUNT else v1.EXCEPTIONAL_MASS
            exact.add(expr >= 0, expr <= ub_i)
        exact.add(v1.linear_expr(bridge.degree_functional, xv) == v1.DEGREE)
        exact.add(v1.linear_expr(bridge.exceptional_mass_functional, xv) == v1.EXCEPTIONAL_MASS)
        for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal):
            exact.add(v1.linear_expr(P.row(int(label) - 1), xv) == int(value))
        replay = exact.check()

        if exact_ok and replay == sat:
            z = data["C"] * x
            zv = vector_int(z)
            x0 = data["x0_map"] * z
            delta = x - x0
            t, params = data["K"].gauss_jordan_solve(delta)
            if params.rows != 0 or any(sympy.denom(q) != 1 for q in t):
                raise ValueError("exact-replayed Picard64 candidate lacks integral 59D translation")
            t = Matrix([int(q) for q in t])
            if data["K"] * t != delta:
                raise ValueError("59D translation reconstruction regression")
            M = data["M"]
            pivots = tuple(int(q) for q in data["pivot_rows"])
            selected_M = M.extract(list(pivots), list(range(v1.ANTI_RANK)))
            reduced_rows, Trow = selected_M.T.lll_transform()
            if reduced_rows != Trow * selected_M.T:
                raise ValueError("LLL reduced-coordinate transform regression")
            U = Trow.T
            if abs(int(U.det())) != 1:
                raise ValueError("reduced-coordinate transform is not unimodular")
            r = U.inv() * t
            if any(sympy.denom(q) != 1 for q in r):
                raise ValueError("reduced 59D witness became nonintegral")
            r = Matrix([int(q) for q in r])
            witness_r_reduced = vector_int(r)
            if x0 + data["K"] * U * r != x:
                raise ValueError("reduced 59D witness reconstruction regression")

            gram = Matrix(bundle["picard_gram_64x64"])
            selfsq_q = (x.T * gram * x)[0, 0]
            if sympy.denom(selfsq_q) != 1:
                raise ValueError("Picard self-intersection became nonintegral")
            selfsq = int(selfsq_q)
            lower_selfsq = -v1.DEGREE - 2 + 2 * v1.GENUS
            support = sum(1 for q in pv[NORMAL_COUNT:] if q > 0)
            support_lower = math.ceil((v1.DEGREE - 16 * v1.GENUS + 16) / 4)
            target.update({"a": a_actual, "z": zv})
            completion = {
                "picard_coordinates": rounded,
                "picard_coordinates_sha256": v1.csha(rounded),
                "all140_pairings": pv,
                "all140_pairings_sha256": v1.csha(pv),
                "all140_nonnegative": True,
                "normal_pairing_sum": sum(pv[:NORMAL_COUNT]),
                "exceptional_pairing_sum": sum(pv[NORMAL_COUNT:]),
                "first_normal_half_a": a_actual,
                "projection_z": zv,
                "projection_z_equals_C_times_picard": True,
                "original_59d_translation_sha256": v1.csha(vector_int(t)),
                "reduced_59d_translation_sha256": v1.csha(witness_r_reduced),
                "reduced_59d_reconstructs_same_picard64": True,
                "self_intersection": selfsq,
                "project_native_self_intersection_lower_formula": "-d-2+2g",
                "project_native_self_intersection_lower_bound": lower_selfsq,
                "passes_project_native_self_intersection_lower_bound": selfsq >= lower_selfsq,
                "positive_exceptional_support": support,
                "bijective_node_support_required_lower_bound": support_lower,
                "passes_bijective_node_support_lower_bound": support >= support_lower,
            }
            status = "SAT_EXACT_REPLAY"
        else:
            reject_reason = {"integer_replay_reasons": reasons, "z3_replay": str(replay), "max_rounding_error": max_rounding_error}

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_ONE_INDEXED_FULL178_TERMINAL_MILP_CANDIDATE_EXACT_REPLAY",
        "status": (
            "PASS_ONE_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION_AND_59D_PROJECTION"
            if status == "SAT_EXACT_REPLAY"
            else "PASS_MILP_CANDIDATE_SEARCH_NO_EXACT_COMPLETION_CREDIT"
        ),
        "source_locks": {
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": checkpoint_canonical,
            "adapter_preflight_canonical_sha256": adapter_preflight_canonical,
            "prior_v1_unknown_canonical_sha256": prior_canonical,
            "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
            "actual_all140_pairing_matrix_sha256": v1.csha(matrix_payload(P)),
            "actual_selected64_pairing_matrix_sha256": v1.csha(matrix_payload(Psel)),
        },
        "indexed_terminal": {
            "row_id": v1.ROW_ID,
            "genus": v1.GENUS,
            "degree": v1.DEGREE,
            "e": v1.EXCEPTIONAL_MASS,
            "terminal_rank": v1.TERMINAL_RANK,
            "terminal_count_in_stratum": int(indexer.terminal_count),
            "rank_unrank_replay_exact": True,
            "assignment_order_known_labels_1based": v1.EXPECTED_ASSIGNMENT_ORDER,
            "pairings": list(terminal),
        },
        "candidate_search": {
            "engine": "SCIPY_HIGHS_MILP_INTEGER_CANDIDATE_ONLY",
            "wall_seconds": args.milp_wall_seconds,
            "elapsed_seconds": round(elapsed, 6),
            "scipy_status": int(candidate_result.status),
            "scipy_message": str(candidate_result.message),
            "candidate_present": candidate_result.x is not None,
            "milp_infeasible_or_timeout_is_not_unsat_credit": True,
            "coordinate_correct_bounds_from_actual_selected64_pairing_matrix": True,
            "picard_coordinate_bounds": [[lo, hi] for lo, hi in x_bounds],
            "candidate_x": candidate_x,
            "reject_reason": reject_reason,
        },
        "exact_replay": {
            "required_for_any_sat_credit": True,
            "solver": "Z3_QF_LIA_PINNED_CANDIDATE",
            "z3_version": get_version_string(),
            "timeout_ms": args.exact_replay_timeout_ms,
            "status": status,
            "original_v1_constraints_replayed": True,
            "new_mathematical_condition_added_over_v1": False,
            "21az_fixed_projection_prism_imported": False,
            "21bk_21bh_21bi_21bj_chain_bands_imported": False,
        },
        "target": target,
        "result": {"status": "SAT" if status == "SAT_EXACT_REPLAY" else "UNKNOWN", "witness_r_reduced": witness_r_reduced, "completion": completion},
        "semantics": {
            "numerical_milp_never_authorizes_unsat": True,
            "sat_credit_requires_exact_integer_and_z3_replay": True,
            "sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "one_terminal_result_is_not_full178_completion": True,
        },
        "firewalls": {
            "heavy_scaleout_authorized": False,
            "FULL178_complete": False,
            "receiver_credit": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = v1.csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "candidate_status": status,
        "scipy_status": int(candidate_result.status),
        "candidate_present": candidate_result.x is not None,
        "projection_z": target.get("z"),
        "self_intersection": completion.get("self_intersection") if completion else None,
        "support": completion.get("positive_exceptional_support") if completion else None,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
