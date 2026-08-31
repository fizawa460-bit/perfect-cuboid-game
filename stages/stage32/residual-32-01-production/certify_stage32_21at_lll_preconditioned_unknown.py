#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_21AK_CONSTRAINT_ROWS_SHA256 = "1c8ea0443dcf80dcaec80964618eac97385d85bfa7d009e60d471cd70f3a5169"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
SCHEMA = "STAGE32_21AT_LLL_PRECONDITIONED_SINGLE_UNKNOWN_V1"


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def max_abs(m: Matrix) -> int:
    return max(abs(int(v)) for v in m) if m.rows and m.cols else 0


def load_frontier(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_FRONTIER_SHA256 or csha(raw) != claimed:
        raise ValueError("21ap frontier canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_21AP_CANONICAL_SHA256:
        raise ValueError("21ap source canonical regression")
    if len(raw.get("frontier", [])) != 1:
        raise ValueError("21at expects exactly one source-locked UNKNOWN")
    return raw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=300000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    frontier = load_frontier(args.frontier)
    target = frontier["frontier"][0]
    z = tuple(int(v) for v in target["z"])
    orbit_totals_expected = tuple(int(v) for v in target["orbit_totals"])

    bundle = load_retained(args.retained, "s32_21at_picard")
    marking = load_retained(args.marking, "s32_21at_marking")
    data = reconstruct_translation_data(marking, bundle)
    if csha(list(data["constraint_rows"])) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak constraint regression")

    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    if M.shape != (EXPECTED_PAIRINGS, EXPECTED_RANK) or len(pivots) != EXPECTED_RANK:
        raise ValueError("pairing translation shape regression")
    selected_M = M.extract(list(pivots), list(range(EXPECTED_RANK)))
    if selected_M.det() == 0:
        raise ValueError("selected original pairing minor is singular")

    # Exact unimodular LLL change of variables. SymPy reduces row bases, so reduce
    # selected_M.T; then U = T.T satisfies selected_M * U = reduced_selected.
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    det_u = int(U.det())
    if abs(det_u) != 1:
        raise ValueError(f"LLL transform is not unimodular: det={det_u}")
    selected_red = selected_M * U
    if selected_red != reduced_rows.T:
        raise ValueError("column LLL reconstruction regression")
    Mred = M * U

    y0 = data["pairing_x0_map"] * Matrix(z)
    if y0.shape != (EXPECTED_PAIRINGS, 1):
        raise ValueError("affine pairing origin shape regression")

    curve_to_orbit = {}
    for oid, orbit in enumerate(data["orbits"]):
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    if len(curve_to_orbit) != EXPECTED_PAIRINGS:
        raise ValueError("orbit coverage regression")

    orbit_totals = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        # Anti-fixed translations must preserve every stabilizer-orbit total.
        for j in range(EXPECTED_RANK):
            if sum(int(Mred[int(i), j]) for i in orbit) != 0:
                raise ValueError(f"orbit {oid} translation-sum regression")
        orbit_totals.append(total0)
    if tuple(orbit_totals) != orbit_totals_expected:
        raise ValueError(f"source-locked orbit totals regression: {orbit_totals}")

    # Derive exact finite integer bounds for the reduced coordinates from the
    # implied boxes 0 <= selected pairing <= its fixed orbit total.
    selected_red_inv = selected_red.inv()
    selected_y0 = [int(y0[i, 0]) for i in pivots]
    r_bounds = []
    for rj in range(EXPECTED_RANK):
        lo = Fraction(0, 1)
        hi = Fraction(0, 1)
        for k, curve_idx in enumerate(pivots):
            oid = curve_to_orbit[curve_idx]
            d_lo = Fraction(-selected_y0[k], 1)
            d_hi = Fraction(orbit_totals[oid] - selected_y0[k], 1)
            a = frac(selected_red_inv[rj, k])
            if a >= 0:
                lo += a * d_lo
                hi += a * d_hi
            else:
                lo += a * d_hi
                hi += a * d_lo
        ilo = math.ceil(lo)
        ihi = math.floor(hi)
        if ilo > ihi:
            raise ValueError(f"derived reduced-coordinate box empty at {rj}: {ilo}>{ihi}")
        r_bounds.append((int(ilo), int(ihi)))

    rvars = [Int(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)
    for j, v in enumerate(rvars):
        lo, hi = r_bounds[j]
        solver.add(v >= lo, v <= hi)

    yexpr = []
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        oid = curve_to_orbit[i]
        # Upper bound is redundant but exact: nonnegative pairings in one orbit
        # have fixed total, so every coordinate is <= that total.
        solver.add(expr >= 0, expr <= orbit_totals[oid])
        yexpr.append(expr)
    for oid, orbit in enumerate(data["orbits"]):
        solver.add(sum(yexpr[int(i)] for i in orbit) == orbit_totals[oid])

    result = solver.check()
    status = "UNKNOWN"
    reason_unknown = None
    t_witness = None
    pairings = None
    reduced_witness = None
    if result == sat:
        status = "SAT"
        model = solver.model()
        reduced_witness = tuple(int(model.eval(v, model_completion=True).as_long()) for v in rvars)
        tvec = U * Matrix(reduced_witness)
        t_witness = tuple(int(v) for v in tvec)
        exact = y0 + M * Matrix(t_witness)
        pairings = tuple(int(exact[i, 0]) for i in range(EXPECTED_PAIRINGS))
        if min(pairings) < 0:
            raise ValueError("21at SAT witness has negative pairing")
        for oid, orbit in enumerate(data["orbits"]):
            if sum(pairings[int(i)] for i in orbit) != orbit_totals[oid]:
                raise ValueError("21at SAT orbit-total regression")
        # Recheck reduced and original parameterizations are identical.
        exact_red = y0 + Mred * Matrix(reduced_witness)
        if tuple(int(exact_red[i, 0]) for i in range(EXPECTED_PAIRINGS)) != pairings:
            raise ValueError("21at reduced/original witness mismatch")
    elif result == unsat:
        status = "UNSAT"
    elif result == unknown:
        status = "UNKNOWN"
        reason_unknown = solver.reason_unknown()
    else:
        raise ValueError(f"unexpected solver result {result}")

    widths = [hi - lo for lo, hi in r_bounds]
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21at",
        "mode": "EXACT_UNIMODULAR_LLL_PRECONDITIONED_ORIGINAL_Z59_PAIRING_LATTICE_WITH_IMPLIED_FINITE_COORDINATE_BOUNDS",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "z3_version": get_version_string(),
        "solver_timeout_ms": args.solver_timeout_ms,
        "target": {
            "row_id": target["row_id"], "e": int(target["e"]), "a": int(target["a"]),
            "u": int(target["u"]), "v": int(target["v"]), "z": list(z),
        },
        "lattice_preconditioning": {
            "rank": EXPECTED_RANK,
            "unimodular_transform_det": det_u,
            "unimodular_transform_sha256": csha(matrix_payload(U)),
            "selected_original_matrix_sha256": csha(matrix_payload(selected_M)),
            "selected_reduced_matrix_sha256": csha(matrix_payload(selected_red)),
            "all140_reduced_matrix_sha256": csha(matrix_payload(Mred)),
            "max_abs_coefficient_before": max_abs(M),
            "max_abs_coefficient_after": max_abs(Mred),
            "coordinate_bounds": [[lo, hi] for lo, hi in r_bounds],
            "maximum_coordinate_width": max(widths),
            "minimum_coordinate_width": min(widths),
            "all_coordinate_bounds_finite": True,
            "bounds_derived_only_from_implied_selected_pairing_boxes": True,
            "same_integer_pairing_lattice_as_21ap": True,
        },
        "result": {
            "status": status,
            "reason_unknown": reason_unknown,
            "combined_representative_sample_sat": 1 if status == "SAT" else 0,
            "combined_representative_sample_unsat": 55 + (1 if status == "UNSAT" else 0),
            "combined_representative_sample_unknown": 1 if status == "UNKNOWN" else 0,
            "reduced_coordinate_witness_sha256": csha(list(reduced_witness)) if reduced_witness is not None else None,
            "translation_witness_sha256": csha(list(t_witness)) if t_witness is not None else None,
            "all140_pairings_sha256": csha(list(pairings)) if pairings is not None else None,
            "all140_pairing_minimum": min(pairings) if pairings is not None else None,
            "all140_pairing_maximum": max(pairings) if pairings is not None else None,
            "orbit_totals": orbit_totals,
        },
        "interpretation": {
            "unsat_closes_the_complete_56_state_representative_sample": status == "UNSAT",
            "sat_is_an_exact_original_t_Z59_lift_for_this_fixed_projection": status == "SAT",
            "unknown_is_not_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "canonical": payload["canonical_sha256_without_this_field"], "max_before": max_abs(M), "max_after": max_abs(Mred), "max_width": max(widths)}))


if __name__ == "__main__":
    main()
