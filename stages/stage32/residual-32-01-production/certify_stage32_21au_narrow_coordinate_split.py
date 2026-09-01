#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

from certify_stage32_21at_lll_preconditioned_unknown import (
    EXPECTED_21AP_CANONICAL_SHA256,
    EXPECTED_FRONTIER_SHA256,
    EXPECTED_PAIRINGS,
    EXPECTED_RANK,
    frac,
    load_frontier,
    matrix_payload,
)
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_21AT_CANONICAL_SHA256 = "fbc7773868f51e712d52f6ed5cedd510e95c9f6c84f6e088147e66bb5cb5694e"
EXPECTED_21AT_U_SHA256 = "fdbf00267e3835efa9e1e77fc628c8a62779f6c42e16076b244cded276934c4f"
EXPECTED_21AT_MRED_SHA256 = "77d62f4473f315212efaad8e4852bb097b2a8584838a5f1299d6528ab8a29bc3"
EXPECTED_MIN_WIDTH = 10
EXPECTED_BRANCH_COUNT = 11
SCHEMA = "STAGE32_21AU_EXACT_NARROW_COORDINATE_DISJOINT_SPLIT_V1"


def build_problem(frontier_path: Path, retained_path: Path, marking_path: Path):
    frontier = load_frontier(frontier_path)
    target = frontier["frontier"][0]
    z = tuple(int(v) for v in target["z"])
    expected_totals = tuple(int(v) for v in target["orbit_totals"])

    bundle = load_retained(retained_path, "s32_21au_picard")
    marking = load_retained(marking_path, "s32_21au_marking")
    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_RANK)))

    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("21au LLL reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("21au non-unimodular transform")
    selected_red = selected_M * U
    Mred = M * U
    if csha(matrix_payload(U)) != EXPECTED_21AT_U_SHA256:
        raise ValueError("21at unimodular transform regression")
    if csha(matrix_payload(Mred)) != EXPECTED_21AT_MRED_SHA256:
        raise ValueError("21at reduced matrix regression")

    y0 = data["pairing_x0_map"] * Matrix(z)
    curve_to_orbit = {}
    for oid, orbit in enumerate(data["orbits"]):
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    orbit_totals = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        for j in range(EXPECTED_RANK):
            if sum(int(Mred[int(i), j]) for i in orbit) != 0:
                raise ValueError("21au orbit translation sum regression")
        orbit_totals.append(total0)
    if tuple(orbit_totals) != expected_totals:
        raise ValueError("21au orbit total regression")

    inv = selected_red.inv()
    selected_y0 = [int(y0[i, 0]) for i in pivots]
    bounds = []
    for rj in range(EXPECTED_RANK):
        lo = Fraction(0, 1)
        hi = Fraction(0, 1)
        for k, curve_idx in enumerate(pivots):
            oid = curve_to_orbit[curve_idx]
            dlo = Fraction(-selected_y0[k], 1)
            dhi = Fraction(orbit_totals[oid] - selected_y0[k], 1)
            a = frac(inv[rj, k])
            if a >= 0:
                lo += a * dlo; hi += a * dhi
            else:
                lo += a * dhi; hi += a * dlo
        ilo, ihi = math.ceil(lo), math.floor(hi)
        if ilo > ihi:
            raise ValueError("21au empty implied coordinate bound")
        bounds.append((int(ilo), int(ihi)))

    widths = [hi - lo for lo, hi in bounds]
    if min(widths) != EXPECTED_MIN_WIDTH:
        raise ValueError(f"21at minimum-width regression: {min(widths)}")
    tied = [j for j, w in enumerate(widths) if w == min(widths)]
    # Among equally narrow coordinates choose the column touching the most/largest
    # pairing coefficients, then the lower index for deterministic tie-breaking.
    def score(j: int):
        col = [abs(int(Mred[i, j])) for i in range(EXPECTED_PAIRINGS)]
        return (sum(col), max(col), -j)
    split_j = max(tied, key=score)
    lo, hi = bounds[split_j]
    if hi - lo + 1 != EXPECTED_BRANCH_COUNT:
        raise ValueError("21au branch-count regression")

    return target, data, M, Mred, U, y0, curve_to_orbit, orbit_totals, bounds, split_j


def make_solver(Mred, y0, curve_to_orbit, orbit_totals, bounds, timeout_ms: int):
    rvars = [Int(f"r_{j}") for j in range(EXPECTED_RANK)]
    s = SolverFor("QF_LIA")
    s.set(timeout=timeout_ms)
    for j, v in enumerate(rvars):
        lo, hi = bounds[j]
        s.add(v >= lo, v <= hi)
    yexpr = []
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        oid = curve_to_orbit[i]
        s.add(expr >= 0, expr <= orbit_totals[oid])
        yexpr.append(expr)
    return s, rvars, yexpr


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--branch-timeout-ms", type=int, default=25000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    target, data, M, Mred, U, y0, curve_to_orbit, orbit_totals, bounds, split_j = build_problem(
        args.frontier, args.retained, args.marking
    )
    split_lo, split_hi = bounds[split_j]

    branches = []
    sat_witness = None
    pairings = None
    t_witness = None
    for value in range(split_lo, split_hi + 1):
        solver, rvars, _ = make_solver(Mred, y0, curve_to_orbit, orbit_totals, bounds, args.branch_timeout_ms)
        solver.add(rvars[split_j] == value)
        res = solver.check()
        if res == sat:
            model = solver.model()
            rw = tuple(int(model.eval(v, model_completion=True).as_long()) for v in rvars)
            tvec = U * Matrix(rw)
            tw = tuple(int(v) for v in tvec)
            exact = y0 + M * Matrix(tw)
            pp = tuple(int(exact[i, 0]) for i in range(EXPECTED_PAIRINGS))
            if min(pp) < 0 or rw[split_j] != value:
                raise ValueError("21au SAT witness regression")
            for oid, orbit in enumerate(data["orbits"]):
                if sum(pp[int(i)] for i in orbit) != orbit_totals[oid]:
                    raise ValueError("21au SAT orbit-total regression")
            branches.append({"value": value, "status": "SAT", "reason_unknown": None})
            sat_witness, t_witness, pairings = rw, tw, pp
            break
        if res == unsat:
            branches.append({"value": value, "status": "UNSAT", "reason_unknown": None})
        elif res == unknown:
            branches.append({"value": value, "status": "UNKNOWN", "reason_unknown": solver.reason_unknown()})
        else:
            raise ValueError(f"unexpected result {res}")

    satc = sum(b["status"] == "SAT" for b in branches)
    unsatc = sum(b["status"] == "UNSAT" for b in branches)
    unknownc = sum(b["status"] == "UNKNOWN" for b in branches)
    if satc:
        overall = "SAT"
    elif len(branches) == EXPECTED_BRANCH_COUNT and unsatc == EXPECTED_BRANCH_COUNT:
        overall = "UNSAT"
    else:
        overall = "UNKNOWN"

    unknown_values = [int(b["value"]) for b in branches if b["status"] == "UNKNOWN"]
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21au",
        "mode": "EXACT_DISJOINT_ENUMERATION_OF_THE_NARROWEST_FINITE_LLL_COORDINATE",
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21at_canonical_sha256": EXPECTED_21AT_CANONICAL_SHA256,
        "z3_version": get_version_string(),
        "target": {"row_id": target["row_id"], "e": int(target["e"]), "a": int(target["a"]), "u": int(target["u"]), "v": int(target["v"]), "z": list(target["z"])},
        "split": {
            "coordinate_0based": split_j,
            "lower": split_lo,
            "upper": split_hi,
            "branch_count": EXPECTED_BRANCH_COUNT,
            "branch_timeout_ms": args.branch_timeout_ms,
            "coverage_is_complete_disjoint_integer_interval": True,
            "split_coordinate_width": split_hi - split_lo,
            "tied_min_width_coordinates_0based": [j for j, (lo, hi) in enumerate(bounds) if hi - lo == EXPECTED_MIN_WIDTH],
        },
        "branches": branches,
        "result": {
            "status": overall,
            "checked_branch_count": len(branches),
            "sat_branch_count": satc,
            "unsat_branch_count": unsatc,
            "unknown_branch_count": unknownc,
            "unknown_values": unknown_values,
            "combined_representative_sample_sat": 1 if overall == "SAT" else 0,
            "combined_representative_sample_unsat": 55 + (1 if overall == "UNSAT" else 0),
            "combined_representative_sample_unknown": 1 if overall == "UNKNOWN" else 0,
            "reduced_coordinate_witness_sha256": csha(list(sat_witness)) if sat_witness is not None else None,
            "translation_witness_sha256": csha(list(t_witness)) if t_witness is not None else None,
            "all140_pairings_sha256": csha(list(pairings)) if pairings is not None else None,
            "all140_pairing_minimum": min(pairings) if pairings is not None else None,
            "all140_pairing_maximum": max(pairings) if pairings is not None else None,
        },
        "interpretation": {
            "all_branches_unsat_implies_fixed_projection_unsat": True,
            "sat_branch_is_exact_original_Z59_lift": True,
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
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": overall, "split_j": split_j, "unsat": unsatc, "unknown": unknownc, "sat": satc, "canonical": payload["canonical_sha256_without_this_field"]}))


if __name__ == "__main__":
    main()
