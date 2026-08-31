#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Real, SolverFor, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
SCHEMA = "STAGE32_21AX_EXACT_INTEGER_BOUND_CLOSURE_V2_INCREMENTAL"


class DeadlineReached(RuntimeError):
    pass


class QflraResourceWall(RuntimeError):
    pass


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def load_frontier(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_FRONTIER_SHA256 or csha(raw) != claimed:
        raise ValueError("21ap frontier canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_21AP_CANONICAL_SHA256:
        raise ValueError("21ap source canonical regression")
    if len(raw.get("frontier", [])) != 1:
        raise ValueError("21ax expects exactly one source-locked UNKNOWN")
    return raw


def derive_initial_bounds(
    selected_red: Matrix,
    pivots: tuple[int, ...],
    y0: Matrix,
    orbit_totals: list[int],
    curve_to_orbit: dict[int, int],
) -> list[tuple[int, int]]:
    inv = selected_red.inv()
    selected_y0 = [int(y0[i, 0]) for i in pivots]
    bounds: list[tuple[int, int]] = []
    for rj in range(EXPECTED_RANK):
        lo = Fraction(0, 1)
        hi = Fraction(0, 1)
        for k, curve_idx in enumerate(pivots):
            oid = curve_to_orbit[curve_idx]
            d_lo = Fraction(-selected_y0[k], 1)
            d_hi = Fraction(orbit_totals[oid] - selected_y0[k], 1)
            a = frac(inv[rj, k])
            if a >= 0:
                lo += a * d_lo
                hi += a * d_hi
            else:
                lo += a * d_hi
                hi += a * d_lo
        ilo, ihi = math.ceil(lo), math.floor(hi)
        if ilo > ihi:
            raise ValueError(f"initial exact integer bound empty at {rj}: {ilo}>{ihi}")
        bounds.append((int(ilo), int(ihi)))
    return bounds


def ensure_time(deadline: float) -> None:
    if time.monotonic() >= deadline:
        raise DeadlineReached("internal wall reached")


def exact_check(solver, deadline: float, counter: list[int]) -> bool:
    ensure_time(deadline)
    counter[0] += 1
    result = solver.check()
    if result == sat:
        return True
    if result == unsat:
        return False
    if result == unknown:
        raise QflraResourceWall(solver.reason_unknown())
    raise RuntimeError(f"unexpected QF_LRA result {result}")


def threshold_feasible(solver, constraint, deadline: float, counter: list[int]) -> bool:
    solver.push()
    try:
        solver.add(constraint)
        return exact_check(solver, deadline, counter)
    finally:
        solver.pop()


def projected_integer_lower(solver, var, lo: int, hi: int, deadline: float, counter: list[int]) -> int:
    a, b = lo, hi
    while a < b:
        mid = (a + b) // 2
        if threshold_feasible(solver, var <= mid, deadline, counter):
            b = mid
        else:
            a = mid + 1
    return a


def projected_integer_upper(solver, var, lo: int, hi: int, deadline: float, counter: list[int]) -> int:
    a, b = lo, hi
    while a < b:
        mid = (a + b + 1) // 2
        if threshold_feasible(solver, var >= mid, deadline, counter):
            a = mid
        else:
            b = mid - 1
    return a


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--max-rounds", type=int, default=8)
    ap.add_argument("--wall-seconds", type=int, default=330)
    ap.add_argument("--per-check-timeout-ms", type=int, default=5000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    started = time.monotonic()
    deadline = started + args.wall_seconds
    frontier = load_frontier(args.frontier)
    target = frontier["frontier"][0]
    z = tuple(int(v) for v in target["z"])
    orbit_totals_expected = tuple(int(v) for v in target["orbit_totals"])

    bundle = load_retained(args.retained, "s32_21ax_picard")
    marking = load_retained(args.marking, "s32_21ax_marking")
    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_RANK)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("LLL transform is not unimodular")
    Mred = M * U
    selected_red = selected_M * U
    y0 = data["pairing_x0_map"] * Matrix(z)

    curve_to_orbit: dict[int, int] = {}
    orbit_totals: list[int] = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        for j in range(EXPECTED_RANK):
            if sum(int(Mred[int(i), j]) for i in orbit) != 0:
                raise ValueError(f"orbit {oid} translation-sum regression")
        orbit_totals.append(total0)
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    if tuple(orbit_totals) != orbit_totals_expected:
        raise ValueError("source-locked orbit totals regression")

    bounds = derive_initial_bounds(selected_red, pivots, y0, orbit_totals, curve_to_orbit)
    initial_bounds = list(bounds)
    rvars = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]

    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.per_check_timeout_ms)
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[i]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(rvars[j] >= lo, rvars[j] <= hi)

    checks = [0]
    rounds: list[dict] = []
    status = "OPEN_MAX_ROUNDS"
    exact_unsat_reason = None
    resource_wall_reason = None
    completed_coordinate_updates = 0

    try:
        if not exact_check(solver, deadline, checks):
            status = "UNSAT"
            exact_unsat_reason = "initial integer-valid finite box already empties the rational all140 polytope"
        else:
            for round_idx in range(args.max_rounds):
                ensure_time(deadline)
                order = sorted(range(EXPECTED_RANK), key=lambda j: (-(bounds[j][1] - bounds[j][0]), j))
                changed = []
                completed = 0
                for j in order:
                    ensure_time(deadline)
                    lo, hi = bounds[j]
                    before = (lo, hi)

                    nlo = projected_integer_lower(solver, rvars[j], lo, hi, deadline, checks)
                    if nlo > lo:
                        solver.add(rvars[j] >= nlo)
                        bounds[j] = (nlo, hi)
                        lo = nlo
                        changed.append({"index": j, "side": "lower", "before": list(before), "after": [lo, hi]})
                        if not exact_check(solver, deadline, checks):
                            status = "UNSAT"
                            exact_unsat_reason = f"integer-valid lower cut on reduced coordinate {j} empties rational polytope"
                            completed += 1
                            completed_coordinate_updates += 1
                            break

                    nhi = projected_integer_upper(solver, rvars[j], lo, hi, deadline, checks)
                    if nhi < hi:
                        old = bounds[j]
                        solver.add(rvars[j] <= nhi)
                        bounds[j] = (lo, nhi)
                        changed.append({"index": j, "side": "upper", "before": list(old), "after": [lo, nhi]})
                        if not exact_check(solver, deadline, checks):
                            status = "UNSAT"
                            exact_unsat_reason = f"integer-valid upper cut on reduced coordinate {j} empties rational polytope"
                            completed += 1
                            completed_coordinate_updates += 1
                            break

                    completed += 1
                    completed_coordinate_updates += 1
                    if completed % 10 == 0:
                        print(json.dumps({"round": round_idx + 1, "completed_coordinates": completed, "checks": checks[0]}), flush=True)

                rounds.append({
                    "round": round_idx + 1,
                    "coordinate_order": order,
                    "completed_coordinate_count": completed,
                    "changed_cut_count": len(changed),
                    "changes": changed,
                })
                if status == "UNSAT":
                    break
                if completed < EXPECTED_RANK:
                    status = "PARTIAL_DEADLINE"
                    break
                if not changed:
                    status = "OPEN_STABILIZED"
                    break
            else:
                status = "OPEN_MAX_ROUNDS"
    except DeadlineReached as exc:
        status = "PARTIAL_DEADLINE"
        resource_wall_reason = str(exc)
    except QflraResourceWall as exc:
        status = "PARTIAL_QF_LRA_RESOURCE_WALL"
        resource_wall_reason = str(exc)

    widths_initial = [hi - lo for lo, hi in initial_bounds]
    widths_final = [hi - lo for lo, hi in bounds]
    narrow_order = sorted(range(EXPECTED_RANK), key=lambda j: (widths_final[j], j))
    narrowest = [
        {"index": j, "lo": bounds[j][0], "hi": bounds[j][1], "width": widths_final[j]}
        for j in narrow_order[:12]
    ]
    product_smallest_3 = math.prod(widths_final[j] + 1 for j in narrow_order[:3])
    product_smallest_5 = math.prod(widths_final[j] + 1 for j in narrow_order[:5])
    elapsed = time.monotonic() - started

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ax",
        "mode": "EXACT_INCREMENTAL_QF_LRA_INTEGER_VALID_COORDINATE_CUT_CLOSURE_ON_ALL140_PAIRING_POLYTOPE",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "z3_version": get_version_string(),
        "wall_seconds": args.wall_seconds,
        "per_check_timeout_ms": args.per_check_timeout_ms,
        "target": {
            "row_id": target["row_id"], "e": int(target["e"]), "a": int(target["a"]),
            "u": int(target["u"]), "v": int(target["v"]), "z": list(z),
        },
        "exact_system": {
            "rank": EXPECTED_RANK,
            "pairing_count": EXPECTED_PAIRINGS,
            "all140_reduced_matrix_sha256": csha(matrix_payload(Mred)),
            "unimodular_transform_sha256": csha(matrix_payload(U)),
            "floating_point_used": False,
            "single_incremental_solver_used": True,
            "every_persisted_bound_cut_is_valid_for_all_integer_solutions": True,
        },
        "result": {
            "status": status,
            "exact_unsat_reason": exact_unsat_reason,
            "resource_wall_reason": resource_wall_reason,
            "round_count": len(rounds),
            "completed_coordinate_updates": completed_coordinate_updates,
            "total_exact_qf_lra_checks": checks[0],
            "elapsed_seconds": round(elapsed, 6),
            "initial_bounds": [[lo, hi] for lo, hi in initial_bounds],
            "final_bounds": [[lo, hi] for lo, hi in bounds],
            "initial_min_width": min(widths_initial),
            "initial_max_width": max(widths_initial),
            "final_min_width": min(widths_final),
            "final_max_width": max(widths_final),
            "narrowest_final_coordinates": narrowest,
            "product_smallest_3_domain_sizes": product_smallest_3,
            "product_smallest_5_domain_sizes": product_smallest_5,
            "combined_representative_sample_sat": 0,
            "combined_representative_sample_unsat": 56 if status == "UNSAT" else 55,
            "combined_representative_sample_unknown": 0 if status == "UNSAT" else 1,
        },
        "rounds": rounds,
        "interpretation": {
            "unsat_closes_the_complete_56_fixed_projection_representative_sample": status == "UNSAT",
            "non_unsat_status_is_not_sat": status != "UNSAT",
            "partial_cut_closure_remains_exact_but_incomplete": status.startswith("PARTIAL_"),
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": status,
        "canonical": payload["canonical_sha256_without_this_field"],
        "rounds": len(rounds),
        "checks": checks[0],
        "min_width": min(widths_final),
        "max_width": max(widths_final),
        "small3": product_smallest_3,
        "elapsed_seconds": round(elapsed, 3),
    }), flush=True)


if __name__ == "__main__":
    main()
