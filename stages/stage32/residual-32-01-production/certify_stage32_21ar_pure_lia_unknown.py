#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_21ap_selected_pairing_integer_fiber import as_fraction, build_relation_interface, lcm_denominators
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_21AK_CONSTRAINT_ROWS_SHA256 = "1c8ea0443dcf80dcaec80964618eac97385d85bfa7d009e60d471cd70f3a5169"
ANTI_RANK = 59
PAIRINGS = 140
ORBITS = 14
SCHEMA = "STAGE32_21AR_SINGLE_UNKNOWN_PURE_QF_LIA_CLOSURE_V1"


def solve_pure_lia(*, z: tuple[int, ...], data: dict, relif: dict, timeout_ms: int):
    pivots = relif["pivots"]
    rel = relif["relation_matrix"]
    y0 = data["pairing_x0_map"] * Matrix(z)
    selected_y0 = Matrix([int(y0[i, 0]) for i in pivots])

    svars = [Int(f"s_{j}") for j in range(ANTI_RANK)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=timeout_ms)
    for v in svars:
        solver.add(v >= 0)

    curve_to_orbit = {}
    orbit_totals = []
    selected_positions = [[] for _ in range(ORBITS)]
    for oid, orbit in enumerate(data["orbits"]):
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
        total = sum(int(y0[int(idx), 0]) for idx in orbit)
        if total < 0:
            raise ValueError("negative fixed orbit total")
        orbit_totals.append(total)
    for j, idx in enumerate(pivots):
        selected_positions[curve_to_orbit[int(idx)]].append(j)
    for oid, pos in enumerate(selected_positions):
        if pos:
            solver.add(sum((svars[j] for j in pos), 0) <= orbit_totals[oid])

    for ri, row in enumerate(data["constraint_rows"]):
        m = int(row["modulus"])
        coeffs = tuple(int(v) for v in row["selected_pairing_coefficients"])
        offsets = tuple(int(v) for v in row["projection_z_offset_coefficients"])
        lhs = sum(coeffs[j] * svars[j] for j in range(ANTI_RANK))
        offset = sum(offsets[k] * int(z[k]) for k in range(len(z)))
        q = Int(f"cong_q_{ri}")
        solver.add(lhs - offset == m * q)

    omitted_vars = {}
    relation_specs = []
    for i in relif["omitted"]:
        coeff = [as_fraction(rel[i, j]) for j in range(ANTI_RANK)]
        const = Fraction(int(y0[i, 0]), 1) - sum(
            coeff[j] * Fraction(int(selected_y0[j, 0]), 1) for j in range(ANTI_RANK)
        )
        D = lcm_denominators(coeff + [const])
        nums = [int(c * D) for c in coeff]
        c0 = int(const * D)
        y = Int(f"omitted_y_{i}")
        solver.add(y >= 0)
        solver.add(c0 + sum(nums[j] * svars[j] for j in range(ANTI_RANK)) == D * y)
        omitted_vars[i] = y
        relation_specs.append((i, D, tuple(nums), c0))

    result = solver.check()
    if result == unknown:
        return "UNKNOWN", None, None, tuple(orbit_totals), solver.reason_unknown()
    if result == unsat:
        return "UNSAT", None, None, tuple(orbit_totals), None
    if result != sat:
        raise ValueError(result)

    model = solver.model()
    selected = tuple(int(model.eval(v, model_completion=True).as_long()) for v in svars)
    pairings = [None] * PAIRINGS
    for j, idx in enumerate(pivots):
        pairings[idx] = selected[j]
    for i, y in omitted_vars.items():
        pairings[i] = int(model.eval(y, model_completion=True).as_long())
    if any(v is None or int(v) < 0 for v in pairings):
        raise ValueError("pure-LIA SAT pairing reconstruction regression")
    pairings_t = tuple(int(v) for v in pairings)

    for i, D, nums, c0 in relation_specs:
        num = c0 + sum(nums[j] * selected[j] for j in range(ANTI_RANK))
        if num != D * pairings_t[i]:
            raise ValueError("pure-LIA relation equality regression")

    ds = Matrix([selected[j] - int(selected_y0[j, 0]) for j in range(ANTI_RANK)])
    w = relif["square_inverse"] * ds
    if any(v.q != 1 for v in w):
        raise ValueError("pure-LIA SAT not integral in saturated coordinates")
    wint = Matrix([int(v) for v in w])
    t = data["F"].inv() * wint
    if any(v.q != 1 for v in t):
        raise ValueError("pure-LIA SAT failed original lattice lift")
    tint = tuple(int(v) for v in t)
    exact = data["pairing_x0_map"] * Matrix(z) + data["M"] * Matrix(tint)
    if tuple(int(exact[i, 0]) for i in range(PAIRINGS)) != pairings_t:
        raise ValueError("pure-LIA original-lattice reconstruction regression")
    return "SAT", tint, pairings_t, tuple(orbit_totals), None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=300000)
    args = ap.parse_args()

    frontier = json.loads(args.frontier.read_text())
    claimed = frontier.pop("canonical_sha256_without_this_field")
    if csha(frontier) != claimed or claimed != EXPECTED_FRONTIER_SHA256:
        raise ValueError("source frontier hash regression")
    if frontier["source_canonical_sha256"] != EXPECTED_21AP_CANONICAL_SHA256:
        raise ValueError("21ap canonical regression")
    target = frontier["frontier"][0]
    z = tuple(int(v) for v in target["z"])

    bundle = load_retained(args.retained, "s32_21ar_picard")
    marking = load_retained(args.marking, "s32_21ar_marking")
    data = reconstruct_translation_data(marking, bundle)
    if csha(list(data["constraint_rows"])) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak constraint rows regression")
    relif = build_relation_interface(data)

    status, t, pairings, totals, reason = solve_pure_lia(
        z=z, data=data, relif=relif, timeout_ms=args.solver_timeout_ms
    )
    if tuple(totals) != tuple(int(v) for v in target["orbit_totals"]):
        raise ValueError("orbit total regression")

    result = {
        "target": {k: target[k] for k in ("row_id", "e", "a", "u", "v", "z")},
        "status": status,
        "reason_unknown": reason,
        "orbit_totals": list(totals),
        "translation_witness_sha256": csha(list(t)) if t is not None else None,
        "all140_pairings_sha256": csha(list(pairings)) if pairings is not None else None,
        "all140_pairing_minimum": min(pairings) if pairings is not None else None,
        "all140_pairing_maximum": max(pairings) if pairings is not None else None,
        "combined_representative_sample_sat": 1 if status == "SAT" else 0,
        "combined_representative_sample_unsat": 56 if status == "UNSAT" else 55,
        "combined_representative_sample_unknown": 1 if status == "UNKNOWN" else 0,
    }
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ar",
        "mode": "EXACT_SAME_21AP_INTEGER_FIBER_REWRITTEN_AS_PURE_QF_LIA_WITH_AUXILIARY_INTEGER_EQUALITIES",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "upstream_32_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
        "z3_version": get_version_string(),
        "solver_timeout_ms": args.solver_timeout_ms,
        "equivalence": {
            "congruence_modulo_replaced_by_exact_integer_quotient_equality": True,
            "omitted_pairing_divisibility_and_nonnegativity_replaced_by_exact_nonnegative_integer_pairing_variable": True,
            "mathematical_feasible_set_unchanged_from_21ap": True,
            "sat_independently_lifted_to_original_t_Z59": True
        },
        "result": result,
        "interpretation": {
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
            "unknown_is_not_unsat": True,
            "complete_representative_sample_closed_if_unsat": status == "UNSAT"
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
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": f"STAGE32_21AR_{status}",
        "status": status,
        "combined_sat": result["combined_representative_sample_sat"],
        "combined_unsat": result["combined_representative_sample_unsat"],
        "combined_unknown": result["combined_representative_sample_unknown"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
