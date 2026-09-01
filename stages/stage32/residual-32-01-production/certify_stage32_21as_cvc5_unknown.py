#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import cvc5
from cvc5 import Kind
from sympy import Matrix

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_21ap_selected_pairing_integer_fiber import as_fraction, build_relation_interface, lcm_denominators
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_21AK_CONSTRAINT_ROWS_SHA256 = "1c8ea0443dcf80dcaec80964618eac97385d85bfa7d009e60d471cd70f3a5169"
EXPECTED_Z3_PURE_LIA_UNKNOWN_SHA256 = "a935d429e75e4b22fdc210d41e6ee1d31eae7446e319aa7d594a47f46a4f5f09"
ANTI_RANK = 59
PAIRINGS = 140
ORBITS = 14
SCHEMA = "STAGE32_21AS_CVC5_SINGLE_UNKNOWN_PURE_QF_LIA_CROSSCHECK_V1"


def csum(solver: cvc5.Solver, terms):
    terms = list(terms)
    if not terms:
        return solver.mkInteger(0)
    if len(terms) == 1:
        return terms[0]
    return solver.mkTerm(Kind.ADD, *terms)


def cmul(solver: cvc5.Solver, coeff: int, var):
    if coeff == 1:
        return var
    return solver.mkTerm(Kind.MULT, solver.mkInteger(coeff), var)


def solve_cvc5(*, z: tuple[int, ...], data: dict, relif: dict, timeout_ms: int):
    pivots = relif["pivots"]
    rel = relif["relation_matrix"]
    y0 = data["pairing_x0_map"] * Matrix(z)
    selected_y0 = Matrix([int(y0[i, 0]) for i in pivots])

    solver = cvc5.Solver()
    solver.setLogic("QF_LIA")
    solver.setOption("produce-models", "true")
    solver.setOption("tlimit-per", str(timeout_ms))
    isort = solver.getIntegerSort()
    zero = solver.mkInteger(0)
    svars = [solver.mkConst(isort, f"s_{j}") for j in range(ANTI_RANK)]
    for v in svars:
        solver.assertFormula(solver.mkTerm(Kind.GEQ, v, zero))

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
            lhs = csum(solver, (svars[j] for j in pos))
            solver.assertFormula(solver.mkTerm(Kind.LEQ, lhs, solver.mkInteger(orbit_totals[oid])))

    for ri, row in enumerate(data["constraint_rows"]):
        m = int(row["modulus"])
        coeffs = tuple(int(v) for v in row["selected_pairing_coefficients"])
        offsets = tuple(int(v) for v in row["projection_z_offset_coefficients"])
        offset = sum(offsets[k] * int(z[k]) for k in range(len(z)))
        lhs = csum(solver, (cmul(solver, coeffs[j], svars[j]) for j in range(ANTI_RANK) if coeffs[j]))
        lhs_minus_offset = csum(solver, [lhs, solver.mkInteger(-offset)])
        q = solver.mkConst(isort, f"cong_q_{ri}")
        rhs = cmul(solver, m, q)
        solver.assertFormula(solver.mkTerm(Kind.EQUAL, lhs_minus_offset, rhs))

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
        y = solver.mkConst(isort, f"omitted_y_{i}")
        solver.assertFormula(solver.mkTerm(Kind.GEQ, y, zero))
        lhs_terms = [solver.mkInteger(c0)]
        lhs_terms.extend(cmul(solver, nums[j], svars[j]) for j in range(ANTI_RANK) if nums[j])
        lhs = csum(solver, lhs_terms)
        rhs = cmul(solver, D, y)
        solver.assertFormula(solver.mkTerm(Kind.EQUAL, lhs, rhs))
        omitted_vars[i] = y
        relation_specs.append((i, D, tuple(nums), c0))

    result = solver.checkSat()
    if result.isUnknown():
        return "UNKNOWN", None, None, tuple(orbit_totals), str(result.getUnknownExplanation())
    if result.isUnsat():
        return "UNSAT", None, None, tuple(orbit_totals), None
    if not result.isSat():
        raise ValueError(str(result))

    selected = tuple(int(solver.getValue(v).getIntegerValue()) for v in svars)
    pairings = [None] * PAIRINGS
    for j, idx in enumerate(pivots):
        pairings[idx] = selected[j]
    for i, y in omitted_vars.items():
        pairings[i] = int(solver.getValue(y).getIntegerValue())
    if any(v is None or int(v) < 0 for v in pairings):
        raise ValueError("cvc5 SAT pairing reconstruction regression")
    pairings_t = tuple(int(v) for v in pairings)

    for i, D, nums, c0 in relation_specs:
        num = c0 + sum(nums[j] * selected[j] for j in range(ANTI_RANK))
        if num != D * pairings_t[i]:
            raise ValueError("cvc5 relation equality regression")

    ds = Matrix([selected[j] - int(selected_y0[j, 0]) for j in range(ANTI_RANK)])
    w = relif["square_inverse"] * ds
    if any(v.q != 1 for v in w):
        raise ValueError("cvc5 SAT not integral in saturated coordinates")
    wint = Matrix([int(v) for v in w])
    t = data["F"].inv() * wint
    if any(v.q != 1 for v in t):
        raise ValueError("cvc5 SAT failed original lattice lift")
    tint = tuple(int(v) for v in t)
    exact = data["pairing_x0_map"] * Matrix(z) + data["M"] * Matrix(tint)
    if tuple(int(exact[i, 0]) for i in range(PAIRINGS)) != pairings_t:
        raise ValueError("cvc5 original-lattice reconstruction regression")
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

    bundle = load_retained(args.retained, "s32_21as_picard")
    marking = load_retained(args.marking, "s32_21as_marking")
    data = reconstruct_translation_data(marking, bundle)
    if csha(list(data["constraint_rows"])) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak constraint rows regression")
    relif = build_relation_interface(data)

    status, t, pairings, totals, reason = solve_cvc5(
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
        "leaf": "32-21as",
        "mode": "INDEPENDENT_CVC5_EXACT_QF_LIA_CROSSCHECK_OF_THE_SINGLE_21AP_UNKNOWN",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "prior_z3_pure_lia_unknown_canonical_sha256": EXPECTED_Z3_PURE_LIA_UNKNOWN_SHA256,
        "upstream_32_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
        "cvc5_version": getattr(cvc5, "__version__", "unknown"),
        "solver_timeout_ms": args.solver_timeout_ms,
        "equivalence": {
            "same_pure_QF_LIA_equalities_as_21ar": True,
            "same_mathematical_feasible_set_as_21ap": True,
            "independent_solver_implementation_from_z3": True,
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
        "verdict": f"STAGE32_21AS_{status}",
        "status": status,
        "combined_sat": result["combined_representative_sample_sat"],
        "combined_unsat": result["combined_representative_sample_unsat"],
        "combined_unknown": result["combined_representative_sample_unknown"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
