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
EXPECTED_21AX_CANONICAL_SHA256 = "21c7b96be83f0d85a722fd16279fe3c9808918536cca258ee3e8110a695c092b"
EXPECTED_21AY_CANONICAL_SHA256 = "8c149a585d6b4f1168d1425cc89daafad4bf37e1ac3568dffb97e1628ffd14be"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_MATRIX_SHA256 = "77d62f4473f315212efaad8e4852bb097b2a8584838a5f1299d6528ab8a29bc3"
EXPECTED_U_SHA256 = "fdbf00267e3835efa9e1e77fc628c8a62779f6c42e16076b244cded276934c4f"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
TRIPLE_COORDS = (50, 55, 27)
CANDIDATES = (20, 54, 56, 57, 42, 49, 51, 58, 23, 26, 44, 1)
SCHEMA = "STAGE32_21AZ_COMPRESSED_SURVIVOR_PRISM_AND_FOURTH_COORDINATE_SELECTION_V1"


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def derive_initial_bounds(selected_red: Matrix, pivots: tuple[int, ...], y0: Matrix,
                          orbit_totals: list[int], curve_to_orbit: dict[int, int]) -> list[tuple[int, int]]:
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
            raise ValueError(f"initial integer-valid bound empty at {rj}: {ilo}>{ihi}")
        bounds.append((int(ilo), int(ihi)))
    return bounds


def load_seed(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_SEED_SHA256 or csha(raw) != claimed:
        raise ValueError("21ax seed canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_21AX_CANONICAL_SHA256:
        raise ValueError("21ax source canonical regression")
    if raw.get("source_21ap_canonical_sha256") != EXPECTED_21AP_CANONICAL_SHA256:
        raise ValueError("21ap source canonical regression")
    return raw


def check_threshold(solver, var, relation: str, value: int):
    solver.push()
    try:
        solver.add(var <= value if relation == "le" else var >= value)
        result = solver.check()
        reason = solver.reason_unknown() if result == unknown else None
        return result, reason
    finally:
        solver.pop()


def tighten_integer_valid_bound(solver, var, lo: int, hi: int) -> dict:
    checks = 0
    a, b = lo, hi
    while a < b:
        mid = (a + b) // 2
        result, reason = check_threshold(solver, var, "le", mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "checks": checks, "reason": reason}
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
        result, reason = check_threshold(solver, var, "ge", mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "checks": checks, "reason": reason}
        if result == sat:
            a = mid
        elif result == unsat:
            b = mid - 1
        else:
            raise RuntimeError(result)
    return {"status": "RESOLVED", "checks": checks, "lo": new_lo, "hi": a}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--triple-check-timeout-ms", type=int, default=1000)
    ap.add_argument("--projection-check-timeout-ms", type=int, default=5000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    started = time.monotonic()
    seed = load_seed(args.seed)
    target = seed["target"]
    z = tuple(int(v) for v in target["z"])

    bundle = load_retained(args.retained, "s32_21az_picard")
    marking = load_retained(args.marking, "s32_21az_marking")
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
    if [bounds[j] for j in TRIPLE_COORDS] != [(69, 79), (-60, -50), (-96, -32)]:
        raise ValueError("21ay triple-domain regression")

    rvars = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.triple_check_timeout_ms)
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[i]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(rvars[j] >= lo, rvars[j] <= hi)

    solver.set(timeout=max(args.projection_check_timeout_ms, 10000))
    solver.push()
    solver.add(rvars[11] <= -1427)
    cut_check = solver.check()
    solver.pop()
    if cut_check != unsat:
        raise ValueError(f"21ax cut failed exact replay: {cut_check}")
    solver.add(rvars[11] >= -1426)

    observed_sat: set[tuple[int, int, int]] = set()
    exact_unsat = 0
    qflra_unknown: list[dict] = []
    checked = 0
    solver.set(timeout=args.triple_check_timeout_ms)

    for r50 in range(69, 80):
        solver.push()
        solver.add(rvars[50] == r50)
        try:
            for r55 in range(-60, -49):
                solver.push()
                solver.add(rvars[55] == r55)
                try:
                    for r27 in range(-96, -31):
                        solver.push()
                        solver.add(rvars[27] == r27)
                        try:
                            result = solver.check()
                            reason = solver.reason_unknown() if result == unknown else None
                        finally:
                            solver.pop()
                        checked += 1
                        triple = (r50, r55, r27)
                        if result == sat:
                            observed_sat.add(triple)
                        elif result == unsat:
                            exact_unsat += 1
                        elif result == unknown:
                            qflra_unknown.append({"triple": list(triple), "reason": reason})
                        else:
                            raise RuntimeError(result)
                finally:
                    solver.pop()
        finally:
            solver.pop()

    if checked != 7865 or qflra_unknown:
        raise RuntimeError(f"21ay replay incomplete/unknown: checked={checked}, unknown={len(qflra_unknown)}")

    compact_set = {
        (r50, r55, r27)
        for r50 in range(69, 80)
        for r55 in range(-60, -49)
        for r27 in range(-96, -47)
        if r55 <= r50 - 129
    }
    if len(observed_sat) != 3234 or exact_unsat != 4631:
        raise ValueError(f"21ay replay count regression: sat={len(observed_sat)} unsat={exact_unsat}")
    if observed_sat != compact_set:
        missing = sorted(compact_set - observed_sat)[:10]
        extra = sorted(observed_sat - compact_set)[:10]
        raise ValueError(f"compact survivor prism mismatch missing={missing} extra={extra}")

    solver.set(timeout=args.projection_check_timeout_ms)
    solver.add(
        rvars[50] >= 69, rvars[50] <= 79,
        rvars[55] >= -60, rvars[55] <= -50,
        rvars[55] <= rvars[50] - 129,
        rvars[27] >= -96, rvars[27] <= -48,
    )
    base_status = solver.check()
    if base_status != sat:
        raise RuntimeError(f"compressed survivor prism rational base unexpectedly {base_status}")

    projections = []
    for j in CANDIDATES:
        lo, hi = bounds[j]
        tightened = tighten_integer_valid_bound(solver, rvars[j], lo, hi)
        activity = {
            "nonzero_pairing_rows": sum(1 for i in range(EXPECTED_PAIRINGS) if int(Mred[i, j]) != 0),
            "l1_pairing_coefficient_sum": sum(abs(int(Mred[i, j])) for i in range(EXPECTED_PAIRINGS)),
            "max_abs_pairing_coefficient": max(abs(int(Mred[i, j])) for i in range(EXPECTED_PAIRINGS)),
        }
        rec = {
            "coordinate": j,
            "initial_bound": [lo, hi],
            "initial_domain_size": hi - lo + 1,
            **activity,
            **tightened,
        }
        if tightened["status"] == "RESOLVED":
            rec["residual_bound"] = [tightened["lo"], tightened["hi"]]
            rec["residual_domain_size"] = tightened["hi"] - tightened["lo"] + 1
            rec["domain_reduction"] = rec["initial_domain_size"] - rec["residual_domain_size"]
        projections.append(rec)

    resolved = [p for p in projections if p["status"] == "RESOLVED"]
    if not resolved:
        chosen = None
    else:
        chosen = min(
            resolved,
            key=lambda p: (
                p["residual_domain_size"],
                -p["domain_reduction"],
                -p["nonzero_pairing_rows"],
                -p["l1_pairing_coefficient_sum"],
                p["coordinate"],
            ),
        )

    compact_description = {
        "coordinates": [50, 55, 27],
        "integer_inequalities": [
            "69 <= r50 <= 79",
            "-60 <= r55 <= -50",
            "r55 <= r50 - 129",
            "-96 <= r27 <= -48",
        ],
        "integer_point_count": 3234,
        "replays_exactly_the_complete_21ay_rational_sat_triple_set": True,
        "raw_survivor_list_needed_for_long_term_state": False,
    }

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21az",
        "mode": "EXACT_REPLAY_COMPRESSED_21AY_SURVIVOR_PRISM_AND_CERTIFIED_FOURTH_COORDINATE_PROJECTION",
        "source_21ay_canonical_sha256": EXPECTED_21AY_CANONICAL_SHA256,
        "source_21ax_canonical_sha256": EXPECTED_21AX_CANONICAL_SHA256,
        "source_seed_sha256": EXPECTED_SEED_SHA256,
        "z3_version": get_version_string(),
        "target": target,
        "replay": {
            "checked_triples": checked,
            "rational_sat_triples": len(observed_sat),
            "exact_rational_unsat_triples": exact_unsat,
            "qflra_unknown_triples": len(qflra_unknown),
            "complete": checked == 7865 and not qflra_unknown,
        },
        "compressed_survivor_region": compact_description,
        "fourth_coordinate_selection": {
            "candidate_coordinates": list(CANDIDATES),
            "candidate_projection_results": projections,
            "chosen": chosen,
            "selection_order": [
                "minimum residual integer-valid domain size",
                "maximum domain reduction",
                "maximum nonzero all140 pairing-row activity",
                "maximum L1 all140 coefficient activity",
                "minimum coordinate index",
            ],
        },
        "interpretation": {
            "compressed_region_is_exact_for_21ay_integer_triple_index_set": True,
            "projection_bounds_are_integer_valid_but_not_integer_feasibility_proofs": True,
            "rational_sat_is_not_integer_sat": True,
            "lone_fixed_projection_remains_unknown": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
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
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "canonical": payload["canonical_sha256_without_this_field"],
        "triple_sat": len(observed_sat),
        "triple_unsat": exact_unsat,
        "chosen_coordinate": None if chosen is None else chosen["coordinate"],
        "chosen_residual_domain_size": None if chosen is None else chosen["residual_domain_size"],
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }), flush=True)


if __name__ == "__main__":
    main()
