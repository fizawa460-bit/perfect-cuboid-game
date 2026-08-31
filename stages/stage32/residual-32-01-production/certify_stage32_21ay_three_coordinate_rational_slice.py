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

EXPECTED_SEED_SHA256 = "f946942434594d80960eea79d04eee3b0df22553928e1d1f3d26721d412d7ad7"
EXPECTED_SOURCE_21AX_SHA256 = "21c7b96be83f0d85a722fd16279fe3c9808918536cca258ee3e8110a695c092b"
EXPECTED_SOURCE_21AP_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_MATRIX_SHA256 = "77d62f4473f315212efaad8e4852bb097b2a8584838a5f1299d6528ab8a29bc3"
EXPECTED_U_SHA256 = "fdbf00267e3835efa9e1e77fc628c8a62779f6c42e16076b244cded276934c4f"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
TRIPLE_COORDS = (50, 55, 27)
SCHEMA = "STAGE32_21AY_EXACT_THREE_COORDINATE_RATIONAL_SLICE_CENSUS_V1"


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def derive_initial_bounds(selected_red: Matrix, pivots: tuple[int, ...], y0: Matrix, orbit_totals: list[int], curve_to_orbit: dict[int, int]) -> list[tuple[int, int]]:
    inv = selected_red.inv()
    selected_y0 = [int(y0[i, 0]) for i in pivots]
    bounds = []
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
            raise ValueError(f"derived initial integer bound empty at {rj}")
        bounds.append((int(ilo), int(ihi)))
    return bounds


def load_seed(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_SEED_SHA256 or csha(raw) != claimed:
        raise ValueError("21ax seed canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_SOURCE_21AX_SHA256:
        raise ValueError("21ax source canonical regression")
    if raw.get("source_21ap_canonical_sha256") != EXPECTED_SOURCE_21AP_SHA256:
        raise ValueError("21ap source canonical regression")
    return raw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--wall-seconds", type=int, default=300)
    ap.add_argument("--per-check-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    started = time.monotonic()
    deadline = started + args.wall_seconds
    seed = load_seed(args.seed)
    target = seed["target"]
    z = tuple(int(v) for v in target["z"])

    bundle = load_retained(args.retained, "s32_21ay_picard")
    marking = load_retained(args.marking, "s32_21ay_marking")
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
        raise ValueError("21ax reduced matrix regression")
    if csha(matrix_payload(U)) != EXPECTED_U_SHA256:
        raise ValueError("21ax unimodular transform regression")
    y0 = data["pairing_x0_map"] * Matrix(z)

    curve_to_orbit: dict[int, int] = {}
    orbit_totals: list[int] = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        orbit_totals.append(total0)
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    expected_totals = [72, 76, 64, 168, 124, 88, 88, 176, 1080, 268, 10, 100, 104, 52]
    if orbit_totals != expected_totals:
        raise ValueError("source orbit totals regression")
    initial_bounds = derive_initial_bounds(selected_red, pivots, y0, orbit_totals, curve_to_orbit)

    domains = {}
    for item in seed["narrowest_unmodified_coordinates"]:
        j = int(item["coordinate"])
        domains[j] = (int(item["lo"]), int(item["hi"]))
    if tuple(domains) != TRIPLE_COORDS:
        raise ValueError(f"triple coordinate regression: {tuple(domains)}")
    for j in TRIPLE_COORDS:
        if domains[j] != initial_bounds[j]:
            raise ValueError(f"triple domain is not the independently rederived exact initial bound at {j}")
    total_triples = 1
    for j in TRIPLE_COORDS:
        lo, hi = domains[j]
        total_triples *= hi - lo + 1
    if total_triples != 7865 or total_triples != int(seed["narrowest_three_domain_size"]):
        raise ValueError("triple coverage count regression")

    rvars = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.per_check_timeout_ms)
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[i]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(initial_bounds):
        solver.add(rvars[j] >= lo, rvars[j] <= hi)

    # Revalidate the one persisted 21ax cut independently before consuming it.
    cut = seed["persisted_integer_valid_cuts"][0]
    if cut != {"coordinate": 11, "relation": ">=", "value": -1426, "prior_bound": [-5529, 3621], "new_bound": [-1426, 3621]}:
        raise ValueError("21ax seed cut regression")
    if initial_bounds[11] != (-5529, 3621):
        raise ValueError("21ax seed prior bound does not match independently rederived bound")
    solver.set(timeout=max(args.per_check_timeout_ms, 10000))
    solver.push()
    solver.add(rvars[11] <= -1427)
    seed_cut_check = solver.check()
    solver.pop()
    if seed_cut_check != unsat:
        raise ValueError(f"21ax seed cut failed independent exact recheck: {seed_cut_check}")
    solver.set(timeout=args.per_check_timeout_ms)
    solver.add(rvars[11] >= -1426)

    checked = 0
    rational_sat = []
    qflra_unkown = []
    exact_unsat_count = 0
    stopped_by_wall = False

    d0 = range(domains[TRIPLE_COORDS[0]][0], domains[TRIPLE_COORDS[0]][1] + 1)
    d1 = range(domains[TRIPLE_COORDS[1]][0], domains[TRIPLE_COORDS[1]][1] + 1)
    d2 = range(domains[TRIPLE_COORDS[2]][0], domains[TRIPLE_COORDS[2]][1] + 1)

    for v0 in d0:
        if time.monotonic() >= deadline:
            stopped_by_wall = True
            break
        solver.push()
        solver.add(rvars[TRIPLE_COORDS[0]] == v0)
        try:
            for v1 in d1:
                if time.monotonic() >= deadline:
                    stopped_by_wall = True
                    break
                solver.push()
                solver.add(rvars[TRIPLE_COORDS[1]] == v1)
                try:
                    for v2 in d2:
                        if time.monotonic() >= deadline:
                            stopped_by_wall = True
                            break
                        solver.push()
                        solver.add(rvars[TRIPLE_COORDS[2]] == v2)
                        try:
                            result = solver.check()
                            reason_unknown = solver.reason_unknown() if result == unknown else None
                        finally:
                            solver.pop()
                        triple = [v0, v1, v2]
                        checked += 1
                        if result == sat:
                            rational_sat.append(triple)
                        elif result == unsat:
                            exact_unsat_count += 1
                        elif result == unknown:
                            qflra_unknown.append({"triple": triple, "reason": reason_unknown})
                        else:
                            raise RuntimeError(f"unexpected QF_LRA result {result}")
                        if checked % 500 == 0:
                            print(json.dumps({"checked": checked, "sat": len(rational_sat), "unsat": exact_unsat_count, "unknown": len(qflra_unknown)}), flush=True)
                    if stopped_by_wall:
                        break
                finally:
                    solver.pop()
            if stopped_by_wall:
                break
        finally:
            solver.pop()

    complete = checked == total_triples
    if complete and not rational_sat and not qflra_unknown:
        status = "UNSAT"
    elif complete:
        status = "OPEN_COMPLETE_TRIPLE_CENSUS"
    else:
        status = "PARTIAL_PREFIX_RESOURCE_WALL"

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ay",
        "mode": "EXACT_EXHAUSTIVE_INTEGER_TRIPLE_ASSIGNMENT_WITH_QF_LRA_FEASIBILITY_OF_REMAINING_56_REAL_COORDINATES",
        "source_seed_sha256": EXPECTED_SEED_SHA256,
        "source_21ax_canonical_sha256": EXPECTED_SOURCE_21AX_SHA256,
        "z3_version": get_version_string(),
        "wall_seconds": args.wall_seconds,
        "per_check_timeout_ms": args.per_check_timeout_ms,
        "target": target,
        "coverage": {
            "coordinates": list(TRIPLE_COORDS),
            "domains": {str(j): list(domains[j]) for j in TRIPLE_COORDS},
            "expected_total_triples": total_triples,
            "checked_triples": checked,
            "complete": complete,
            "lexicographic_prefix": True
        },
        "result": {
            "status": status,
            "exact_rational_unsat_triples": exact_unsat_count,
            "rational_sat_triple_count": len(rational_sat),
            "qflra_unknown_triple_count": len(qflra_unknown),
            "rational_sat_triples": rational_sat,
            "qflra_unknown_triples": qflra_unkown,
            "combined_representative_sample_sat": 0,
            "combined_representative_sample_unsat": 56 if status == "UNSAT" else 55,
            "combined_representative_sample_unknown": 0 if status == "UNSAT" else 1
        },
        "interpretation": {
            "unsat_if_and_only_if_complete_and_every_triple_rationally_infeasible": status == "UNSAT",
            "rational_sat_triple_is_not_integer_sat": True,
            "qflra_unknown_is_not_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "canonical": payload["canonical_sha256_without_this_field"], "checked": checked, "sat": len(rational_sat), "unsat": exact_unsat_count, "unknown": len(qflra_unknown), "elapsed_seconds": round(time.monotonic()-started,3)}), flush=True)

if __name__ == "__main__":
    main()
