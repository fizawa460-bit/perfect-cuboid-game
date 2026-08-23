#!/usr/bin/env python3
"""Exact bounded intersection-coordinate solver for Stage32 residual cells.

The 64 selected known-class intersections are bounded coordinates.  The exact
inverse has denominator 8, so Picard-lattice membership is imposed by 64
congruences.  Optional deterministic budget sums (b,f,c,h,k,l,m) are the same
ones used by the audited Stage32-02 partition tree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import time
from typing import Any

import sympy
import z3
from sympy import Matrix

from cap_certificate import canonical_sha256, load_and_verify

SCHEMA = "STAGE32_INTERSECTION_COORD_BUDGET_V2"
ALGORITHM_ID = "INTERSECTION_COORD_DENOM8_QF_NIA_CAP140_PARTITION_V2"
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_SELECTED_DETERMINANT = 274877906944
EXPECTED_INVERSE_DENOMINATOR = 8
OPTION_KEYS = (
    "curve_quarter_mass",
    "exceptional_half_mass",
    "second_curve_quarter_mass",
    "exceptional_quarter_mass",
    "second_exceptional_quarter_mass",
    "curve_eighth_mass",
    "curve_sixteenth_mass",
)


def matrix_list(matrix: Matrix) -> list[list[int]]:
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def matrix_sha256(matrix: Matrix) -> str:
    return canonical_sha256(matrix_list(matrix))


def linear(coefficients: list[int], variables: list[z3.ArithRef]) -> z3.ArithRef:
    terms = [coefficient * variables[j] for j, coefficient in enumerate(coefficients) if coefficient]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def build_transform(core: dict[str, Any]) -> dict[str, Any]:
    rows = Matrix(core["raw_cross_pairings_with_basis"])
    gram = Matrix(core["basis_gram"])
    selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
    determinant = int(selected.det())
    assert abs(determinant) == EXPECTED_SELECTED_DETERMINANT
    inverse = selected.inv()
    denominator = 1
    for value in inverse:
        denominator = math.lcm(denominator, int(sympy.denom(value)))
    assert denominator == EXPECTED_INVERSE_DENOMINATOR
    inverse_integer = inverse * denominator
    assert all(sympy.denom(value) == 1 for value in inverse_integer)
    inverse_integer = Matrix(
        [[int(inverse_integer[i, j]) for j in range(64)] for i in range(64)]
    )
    assert selected * inverse_integer == denominator * Matrix.eye(64)

    transformed_pairings = rows * inverse_integer
    assert all(sympy.denom(value) == 1 for value in transformed_pairings)
    transformed_pairings = Matrix(
        [[int(transformed_pairings[i, j]) for j in range(64)] for i in range(140)]
    )
    transformed_hform = Matrix(core["hyperplane"]).T * gram * inverse_integer
    assert all(sympy.denom(value) == 1 for value in transformed_hform)
    hrow = [int(transformed_hform[0, j]) for j in range(64)]
    transformed_gram = inverse_integer.T * gram * inverse_integer
    assert all(sympy.denom(value) == 1 for value in transformed_gram)
    transformed_gram = Matrix(
        [[int(transformed_gram[i, j]) for j in range(64)] for i in range(64)]
    )
    certificate = {
        "algorithm_id": ALGORITHM_ID,
        "selected_rows_1based": [i + 1 for i in SELECTED_ROWS],
        "selected_matrix_determinant": determinant,
        "inverse_denominator": denominator,
        "selected_matrix_sha256": matrix_sha256(selected),
        "inverse_integer_matrix_sha256": matrix_sha256(inverse_integer),
        "transformed_pairing_matrix_sha256": matrix_sha256(transformed_pairings),
        "transformed_gram_sha256": matrix_sha256(transformed_gram),
        "transformed_hform_sha256": canonical_sha256(hrow),
    }
    return {
        "denominator": denominator,
        "inverse_integer": inverse_integer,
        "pairings": transformed_pairings,
        "hform": hrow,
        "gram": transformed_gram,
        "certificate": certificate,
    }


def option_values(args: argparse.Namespace) -> dict[str, int | None]:
    return {key: getattr(args, key) for key in OPTION_KEYS}


def validate_options(args: argparse.Namespace) -> None:
    degree = args.degree
    e = args.exceptional_mass
    a = args.curve_group_mass
    nonexceptional_total = 19 * degree - 5 * e
    second_curve_group = nonexceptional_total - a
    if not 0 <= e <= 19 * degree // 5:
        raise SystemExit("exceptional mass is outside exact weighted budget")
    if not 0 <= a <= nonexceptional_total:
        raise SystemExit("curve-group mass is outside exact weighted budget")
    if args.curve_quarter_mass is not None and not 0 <= args.curve_quarter_mass <= a:
        raise SystemExit("curve-quarter mass is outside first curve-group budget")
    if args.exceptional_half_mass is not None and not 0 <= args.exceptional_half_mass <= e:
        raise SystemExit("exceptional-half mass is outside exceptional budget")
    if args.second_curve_quarter_mass is not None and not 0 <= args.second_curve_quarter_mass <= second_curve_group:
        raise SystemExit("second curve-quarter mass is outside second curve-group budget")
    if args.exceptional_quarter_mass is not None:
        if args.exceptional_half_mass is None or not 0 <= args.exceptional_quarter_mass <= args.exceptional_half_mass:
            raise SystemExit("exceptional-quarter mass requires/inherits exceptional-half budget")
    if args.second_exceptional_quarter_mass is not None:
        if args.exceptional_half_mass is None:
            raise SystemExit("second exceptional-quarter mass requires exceptional-half mass")
        second_half = e - args.exceptional_half_mass
        if not 0 <= args.second_exceptional_quarter_mass <= second_half:
            raise SystemExit("second exceptional-quarter mass is outside second half budget")
    if args.curve_eighth_mass is not None:
        if args.curve_quarter_mass is None or not 0 <= args.curve_eighth_mass <= args.curve_quarter_mass:
            raise SystemExit("curve-eighth mass requires/inherits curve-quarter budget")
    if args.curve_sixteenth_mass is not None:
        if args.curve_eighth_mass is None or not 0 <= args.curve_sixteenth_mass <= args.curve_eighth_mass:
            raise SystemExit("curve-sixteenth mass requires/inherits curve-eighth budget")


def add_partition_constraints(
    solver: z3.Solver,
    pairing_numerators: list[z3.ArithRef],
    denominator: int,
    args: argparse.Namespace,
) -> None:
    constraints = (
        (args.curve_quarter_mass, pairing_numerators[:23]),
        (args.exceptional_half_mass, pairing_numerators[92:116]),
        (args.second_curve_quarter_mass, pairing_numerators[46:69]),
        (args.exceptional_quarter_mass, pairing_numerators[92:104]),
        (args.second_exceptional_quarter_mass, pairing_numerators[116:128]),
        (args.curve_eighth_mass, pairing_numerators[:11]),
        (args.curve_sixteenth_mass, pairing_numerators[:5]),
    )
    for target, expressions in constraints:
        if target is not None:
            solver.add(z3.Sum(expressions) == denominator * target)


def verify_model(
    core: dict[str, Any],
    transform: dict[str, Any],
    selected_intersections: list[int],
    args: argparse.Namespace,
) -> dict[str, Any]:
    denominator = transform["denominator"]
    numerators = transform["inverse_integer"] * Matrix(selected_intersections)
    assert all(int(value) % denominator == 0 for value in numerators)
    vector = [int(value) // denominator for value in numerators]
    rows = core["raw_cross_pairings_with_basis"]
    pairings = [sum(int(row[j]) * vector[j] for j in range(64)) for row in rows]
    curve_cap = args.degree // 2
    exceptional_cap = args.degree // 4
    assert all(0 <= value <= curve_cap for value in pairings[:92])
    assert all(0 <= value <= exceptional_cap for value in pairings[92:])
    assert sum(pairings[92:]) == args.exceptional_mass
    assert sum(pairings[:46]) == args.curve_group_mass
    assert sum(pairings[:92]) + 5 * sum(pairings[92:]) == 19 * args.degree
    optional_checks = (
        (args.curve_quarter_mass, sum(pairings[:23])),
        (args.exceptional_half_mass, sum(pairings[92:116])),
        (args.second_curve_quarter_mass, sum(pairings[46:69])),
        (args.exceptional_quarter_mass, sum(pairings[92:104])),
        (args.second_exceptional_quarter_mass, sum(pairings[116:128])),
        (args.curve_eighth_mass, sum(pairings[:11])),
        (args.curve_sixteenth_mass, sum(pairings[:5])),
    )
    for target, observed in optional_checks:
        if target is not None:
            assert observed == target
    gram = core["basis_gram"]
    square = sum(
        vector[i] * int(gram[i][j]) * vector[j]
        for i in range(64)
        for j in range(64)
    )
    assert square >= -args.degree - 2 + 2 * args.genus
    hyperplane = core["hyperplane"]
    degree = sum(
        int(hyperplane[i]) * int(gram[i][j]) * vector[j]
        for i in range(64)
        for j in range(64)
    )
    assert degree == args.degree
    assert [pairings[i] for i in SELECTED_ROWS] == selected_intersections
    return {
        "picard_coordinates": vector,
        "selected_intersections": selected_intersections,
        "self_intersection": square,
        "intersection_vector_sha256": canonical_sha256(pairings),
    }


def make_label(args: argparse.Namespace) -> str:
    label = f"d{args.degree}-g{args.genus}-e{args.exceptional_mass}-a{args.curve_group_mass}"
    suffixes = (
        ("b", args.curve_quarter_mass),
        ("f", args.exceptional_half_mass),
        ("c", args.second_curve_quarter_mass),
        ("h", args.exceptional_quarter_mass),
        ("k", args.second_exceptional_quarter_mass),
        ("l", args.curve_eighth_mass),
        ("m", args.curve_sixteenth_mass),
    )
    for prefix, value in suffixes:
        if value is not None:
            label += f"-{prefix}{value}"
    return label


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--curve-quarter-mass", type=int)
    parser.add_argument("--exceptional-half-mass", type=int)
    parser.add_argument("--second-curve-quarter-mass", type=int)
    parser.add_argument("--exceptional-quarter-mass", type=int)
    parser.add_argument("--second-exceptional-quarter-mass", type=int)
    parser.add_argument("--curve-eighth-mass", type=int)
    parser.add_argument("--curve-sixteenth-mass", type=int)
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()
    if args.degree <= 0 or args.degree % 2:
        raise SystemExit("degree must be positive and even")
    validate_options(args)

    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    transform = build_transform(core)
    denominator = transform["denominator"]
    transformed_pairings = transform["pairings"]
    inverse_integer = transform["inverse_integer"]
    transformed_gram = transform["gram"]
    curve_cap = args.degree // 2
    exceptional_cap = args.degree // 4

    if args.proof:
        z3.set_param(proof=True)
    variables = [z3.Int(f"intersection_coord_{j + 1}") for j in range(64)]
    solver = z3.SolverFor("QF_NIA")
    solver.set(random_seed=0, threads=1)
    if args.timeout:
        solver.set(timeout=int(args.timeout * 1000))

    for j in range(48):
        solver.add(variables[j] >= 0, variables[j] <= exceptional_cap)
    for j in range(48, 64):
        solver.add(variables[j] >= 0, variables[j] <= curve_cap)
    for i in range(64):
        solver.add(
            linear([int(inverse_integer[i, j]) for j in range(64)], variables)
            % denominator
            == 0
        )

    pairing_numerators: list[z3.ArithRef] = []
    for i in range(140):
        numerator = linear(
            [int(transformed_pairings[i, j]) for j in range(64)], variables
        )
        pairing_numerators.append(numerator)
        cap = curve_cap if i < 92 else exceptional_cap
        solver.add(numerator >= 0, numerator <= denominator * cap)

    solver.add(linear(transform["hform"], variables) == denominator * args.degree)
    solver.add(z3.Sum(pairing_numerators[92:]) == denominator * args.exceptional_mass)
    solver.add(z3.Sum(pairing_numerators[:46]) == denominator * args.curve_group_mass)
    solver.add(
        z3.Sum(pairing_numerators[:92]) + 5 * z3.Sum(pairing_numerators[92:])
        == denominator * 19 * args.degree
    )
    add_partition_constraints(solver, pairing_numerators, denominator, args)

    quadratic = [
        int(transformed_gram[i, j]) * variables[i] * variables[j]
        for i in range(64)
        for j in range(64)
        if transformed_gram[i, j]
    ]
    lower = -args.degree - 2 + 2 * args.genus
    solver.add(z3.Sum(quadratic) >= denominator * denominator * lower)

    label = make_label(args)
    shard = args.output_dir / label
    shard.mkdir(parents=True, exist_ok=True)
    smt_text = solver.to_smt2()
    (shard / "problem.smt2").write_text(smt_text, encoding="utf-8", newline="\n")
    smt_sha256 = hashlib.sha256(smt_text.encode()).hexdigest()

    survivors: list[dict[str, Any]] = []
    started = time.perf_counter()
    result = solver.check()
    while result == z3.sat:
        model = solver.model()
        values = [model.eval(variable, model_completion=True).as_long() for variable in variables]
        survivors.append(verify_model(core, transform, values, args))
        solver.add(z3.Or([variable != value for variable, value in zip(variables, values)]))
        result = solver.check()
    elapsed = time.perf_counter() - started

    proof_sha256 = None
    proof_name = None
    if result == z3.unsat and args.proof:
        proof_text = solver.proof().sexpr() + "\n"
        proof_name = "proof.sexpr"
        (shard / proof_name).write_text(proof_text, encoding="utf-8", newline="\n")
        proof_sha256 = hashlib.sha256(proof_text.encode()).hexdigest()
    complete = result == z3.unsat
    deterministic = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "degree": args.degree,
        "genus": args.genus,
        "exceptional_mass": args.exceptional_mass,
        "curve_group_mass": args.curve_group_mass,
        **option_values(args),
        "core_canonical_sha256": core["canonical_sha256_without_this_field"],
        "cap_certificate_canonical_sha256": cap_summary["certificate_canonical_sha256"],
        "transform_certificate": transform["certificate"],
        "solver_result": str(result),
        "complete": complete,
        "exact_survivor_count": len(survivors) if complete else None,
        "survivors": survivors if complete else [],
        "smt2_sha256": smt_sha256,
        "proof_sha256": proof_sha256,
        "random_seed": 0,
        "threads": 1,
    }
    payload = {
        **deterministic,
        "unknown_reason": solver.reason_unknown() if result == z3.unknown else None,
        "elapsed_seconds": round(elapsed, 6),
        "files": {"problem": "problem.smt2", "proof": proof_name},
        "deterministic_result_sha256": canonical_sha256(deterministic),
        "floating_point_feasibility_credit": False,
        "receiver_credit": False,
    }
    unsigned = dict(payload)
    payload["checkpoint_sha256_without_this_field"] = canonical_sha256(unsigned)
    (shard / "checkpoint.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, sort_keys=True))
    if not complete:
        raise SystemExit("intersection-coordinate exact enumeration did not close this cell")


if __name__ == "__main__":
    main()
