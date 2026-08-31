#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Real, SolverFor, get_version_string, sat, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
SCHEMA = "STAGE32_21AX_EXACT_INTEGER_BOUND_CLOSURE_V1"


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


def derive_initial_bounds(selected_red: Matrix, pivots: tuple[int, ...], y0: Matrix, orbit_totals: list[int], curve_to_orbit: dict[int, int]) -> list[tuple[int, int]]:
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


def feasible_with_threshold(base_constraints, var, relation: str, value: int) -> bool:
    s = SolverFor("QF_LRA")
    s.add(*base_constraints)
    if relation == "le":
        s.add(var <= value)
    elif relation == "ge":
        s.add(var >= value)
    else:
        raise ValueError(relation)
    result = s.check()
    if result == sat:
        return True
    if result == unsat:
        return False
    raise RuntimeError(f"QF_LRA returned unexpected {result}")


def tighten_coordinate(base_constraints, var, lo: int, hi: int) -> tuple[int, int, int]:
    checks = 0
    a, b = lo, hi
    while a < b:
        mid = (a + b) // 2
        checks += 1
        if feasible_with_threshold(base_constraints, var, "le", mid):
            b = mid
        else:
            a = mid + 1
    new_lo = a

    a, b = new_lo, hi
    while a < b:
        mid = (a + b + 1) // 2
        checks += 1
        if feasible_with_threshold(base_constraints, var, "ge", mid):
            a = mid
        else:
            b = mid - 1
    return new_lo, a, checks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--max-rounds", type=int, default=8)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

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
    all140 = []
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[i]]
        all140.extend([expr >= 0, expr <= total])

    rounds = []
    total_lra_checks = 0
    status = "OPEN_AFTER_BOUND_CLOSURE"
    exact_unsat_reason = None

    for round_idx in range(args.max_rounds):
        base = list(all140)
        for j, (lo, hi) in enumerate(bounds):
            base.extend([rvars[j] >= lo, rvars[j] <= hi])
        s0 = SolverFor("QF_LRA")
        s0.add(*base)
        base_result = s0.check()
        total_lra_checks += 1
        if base_result == unsat:
            status = "UNSAT"
            exact_unsat_reason = "integer-valid coordinate-bound cuts made the rational polytope empty"
            rounds.append({"round": round_idx + 1, "base_rational_status": "UNSAT", "changed_coordinates": []})
            break
        if base_result != sat:
            raise RuntimeError(f"unexpected QF_LRA base result {base_result}")

        proposed = list(bounds)
        changed = []
        for j, (lo, hi) in enumerate(bounds):
            nlo, nhi, checks = tighten_coordinate(base, rvars[j], lo, hi)
            total_lra_checks += checks
            if nlo > nhi:
                status = "UNSAT"
                exact_unsat_reason = f"coordinate {j} has no integer in its exact rational projection"
                proposed[j] = (nlo, nhi)
                changed.append({"index": j, "before": [lo, hi], "after": [nlo, nhi]})
                break
            proposed[j] = (nlo, nhi)
            if (nlo, nhi) != (lo, hi):
                changed.append({"index": j, "before": [lo, hi], "after": [nlo, nhi]})
        rounds.append({
            "round": round_idx + 1,
            "base_rational_status": "SAT",
            "changed_coordinate_count": len(changed),
            "changed_coordinates": changed,
        })
        bounds = proposed
        if status == "UNSAT":
            break
        if not changed:
            break

    widths_initial = [hi - lo for lo, hi in initial_bounds]
    widths_final = [hi - lo for lo, hi in bounds]
    narrow_order = sorted(range(EXPECTED_RANK), key=lambda j: (widths_final[j], j))
    narrowest = [
        {"index": j, "lo": bounds[j][0], "hi": bounds[j][1], "width": widths_final[j]}
        for j in narrow_order[:12]
    ]
    product_smallest_3 = math.prod(widths_final[j] + 1 for j in narrow_order[:3])
    product_smallest_5 = math.prod(widths_final[j] + 1 for j in narrow_order[:5])

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ax",
        "mode": "EXACT_QF_LRA_ITERATED_INTEGER_COORDINATE_BOUND_CLOSURE_ON_ALL140_PAIRING_POLYTOPE",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "z3_version": get_version_string(),
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
            "every_added_bound_is_valid_for_all_integer_solutions": True,
        },
        "result": {
            "status": status,
            "exact_unsat_reason": exact_unsat_reason,
            "round_count": len(rounds),
            "total_exact_qf_lra_checks": total_lra_checks,
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
            "open_after_bound_closure_is_not_sat": status != "UNSAT",
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
        "checks": total_lra_checks,
        "min_width": min(widths_final),
        "max_width": max(widths_final),
        "small3": product_smallest_3,
    }))


if __name__ == "__main__":
    main()
