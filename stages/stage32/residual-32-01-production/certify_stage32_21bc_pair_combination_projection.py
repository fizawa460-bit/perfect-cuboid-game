#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import And, Or, Real, SolverFor, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_21BB_LOCK_SHA256 = "370bc29433006c5a5ac0b8ee977212f0a274449ab85c736e62b3f5cbf7e51405"
EXPECTED_MATRIX_SHA256 = "77d62f4473f315212efaad8e4852bb097b2a8584838a5f1299d6528ab8a29bc3"
EXPECTED_U_SHA256 = "fdbf00267e3835efa9e1e77fc628c8a62779f6c42e16076b244cded276934c4f"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
CANDIDATE_BOUNDS = {
    20: (86, 132),
    54: (-178, -132),
    56: (14, 60),
    57: (0, 46),
    42: (33, 79),
    49: (132, 178),
    51: (-178, -132),
}
CANDIDATES = tuple(CANDIDATE_BOUNDS)
SCHEMA = "STAGE32_21BC_EXACT_SMALL_PAIR_COMBINATION_PROJECTION_V1"


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def derive_initial_bounds(selected_red: Matrix, pivots: tuple[int, ...], y0: Matrix,
                          orbit_totals: list[int], curve_to_orbit: dict[int, int]) -> list[tuple[int, int]]:
    import math
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
            raise ValueError(f"initial integer-valid bound empty at {rj}")
        bounds.append((int(ilo), int(ihi)))
    return bounds


def load_21bb(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BB_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21bb source-lock canonical regression")
    if raw["coverage"]["formula_failures"] != 0:
        raise ValueError("21bb formula source is not exact")
    return raw


def threshold_sat(solver, expr, relation: str, value: int):
    solver.push()
    try:
        solver.add(expr <= value if relation == "le" else expr >= value)
        result = solver.check()
        return result, solver.reason_unknown() if result == unknown else None
    finally:
        solver.pop()


def project_integer_valid_range(solver, expr, lo: int, hi: int) -> dict:
    checks = 0
    a, b = lo, hi
    while a < b:
        mid = (a + b) // 2
        result, reason = threshold_sat(solver, expr, "le", mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "checks": checks, "phase": "lower", "reason": reason}
        if result == sat:
            b = mid
        elif result == unsat:
            a = mid + 1
        else:
            raise RuntimeError(result)
    new_lo = a

    a, b = new_lo, hi
    while a < b:
        mid = (a + b + 1) // 2
        result, reason = threshold_sat(solver, expr, "ge", mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "checks": checks, "phase": "upper", "reason": reason}
        if result == sat:
            a = mid
        elif result == unsat:
            b = mid - 1
        else:
            raise RuntimeError(result)
    return {"status": "RESOLVED", "checks": checks, "lo": new_lo, "hi": a, "domain_size": a - new_lo + 1}


def combo_initial(i: int, j: int, sign: int) -> tuple[int, int]:
    ilo, ihi = CANDIDATE_BOUNDS[i]
    jlo, jhi = CANDIDATE_BOUNDS[j]
    if sign == 1:
        return ilo + jlo, ihi + jhi
    return ilo - jhi, ihi - jlo


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-lock", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--per-check-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    source = load_21bb(args.source_lock)
    target = source.get("target", {"row_id": "g1-d186", "e": 266, "a": 592, "u": -44, "v": 32, "z": [-15, 62, -44, 26, 32]})
    z = tuple(int(v) for v in target["z"])

    bundle = load_retained(args.retained, "s32_21bc_picard")
    marking = load_retained(args.marking, "s32_21bc_marking")
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
    if csha(matrix_payload(Mred)) != EXPECTED_MATRIX_SHA256:
        raise ValueError("reduced matrix regression")
    if csha(matrix_payload(U)) != EXPECTED_U_SHA256:
        raise ValueError("unimodular transform regression")

    y0 = data["pairing_x0_map"] * Matrix(z)
    curve_to_orbit: dict[int, int] = {}
    orbit_totals: list[int] = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        orbit_totals.append(total0)
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    if orbit_totals != [72, 76, 64, 168, 124, 88, 88, 176, 1080, 268, 10, 100, 104, 52]:
        raise ValueError("orbit totals regression")

    bounds = derive_initial_bounds(selected_red, pivots, y0, orbit_totals, curve_to_orbit)
    r = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.per_check_timeout_ms)
    for row in range(EXPECTED_PAIRINGS):
        expr = int(y0[row, 0]) + sum(int(Mred[row, j]) * r[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[row]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(r[j] >= lo, r[j] <= hi)
    solver.add(r[11] >= -1426)

    # Exact integer-valid 21az prism cuts.
    solver.add(r[50] >= 69, r[50] <= 79, r[55] >= -60, r[55] <= -50, r[55] <= r[50] - 129, r[27] >= -96, r[27] <= -48)
    # Exact 21bb integer-valid r51 region, encoded as three linear bands.
    d = r[50] - r[55]
    solver.add(r[51] <= -132)
    solver.add(Or(
        And(d >= 129, d <= 132, r[51] >= -176, r[51] >= r[27] - 103),
        And(d >= 133, d <= 136, r[51] >= -177, r[51] >= r[27] - 103),
        And(d >= 137, d <= 139, r[51] >= -178, r[51] >= r[27] - 103),
    ))
    # Add all seven independently certified 21az integer-valid coordinate bounds.
    for j, (lo, hi) in CANDIDATE_BOUNDS.items():
        solver.add(r[j] >= lo, r[j] <= hi)

    base = solver.check()
    if base == unknown:
        raise RuntimeError(f"base QF_LRA UNKNOWN: {solver.reason_unknown()}")
    if base != sat:
        raise RuntimeError(f"base relaxation unexpectedly {base}")

    results = []
    for pos, i in enumerate(CANDIDATES):
        for j in CANDIDATES[pos + 1:]:
            for sign in (1, -1):
                ilo, ihi = combo_initial(i, j, sign)
                expr = r[i] + sign * r[j]
                out = project_integer_valid_range(solver, expr, ilo, ihi)
                item = {
                    "i": i,
                    "j": j,
                    "sign": sign,
                    "expression": f"r{i} {'+' if sign == 1 else '-'} r{j}",
                    "initial_bound": [ilo, ihi],
                    "initial_domain_size": ihi - ilo + 1,
                    **out,
                }
                if out["status"] == "RESOLVED":
                    item["domain_reduction"] = item["initial_domain_size"] - out["domain_size"]
                results.append(item)
                print(json.dumps(item), flush=True)

    resolved = [x for x in results if x["status"] == "RESOLVED"]
    unknowns = [x for x in results if x["status"] == "UNKNOWN"]
    chosen = min(resolved, key=lambda x: (x["domain_size"], -x["domain_reduction"], x["i"], x["j"], -x["sign"])) if resolved else None
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bc",
        "mode": "EXACT_QF_LRA_PROJECTION_OF_SMALL_INTEGER_PAIR_COMBINATIONS_OVER_21BB_BANDED_RELAXATION",
        "source_21bb_lock_sha256": EXPECTED_21BB_LOCK_SHA256,
        "z3_version": get_version_string(),
        "per_check_timeout_ms": args.per_check_timeout_ms,
        "candidate_coordinates": list(CANDIDATES),
        "combination_count": len(results),
        "resolved_count": len(resolved),
        "unknown_count": len(unknowns),
        "results": results,
        "chosen": chosen,
        "interpretation": {
            "banded_relaxation_preserves_every_integer_solution": True,
            "resolved_combination_bounds_are_integer_valid": True,
            "narrow_combination_is_not_integer_sat_or_unsat": True,
            "qflra_unknown_is_not_unsat": True,
            "fixed_projection_remains_unknown": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"canonical": payload["canonical_sha256_without_this_field"], "resolved": len(resolved), "unknown": len(unknowns), "chosen": chosen}), flush=True)


if __name__ == "__main__":
    main()
