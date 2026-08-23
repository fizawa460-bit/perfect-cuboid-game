#!/usr/bin/env python3
"""Exact Stage32 Picard enumeration using Z3 integer arithmetic.

The search variables are the 64 integral coordinates in the source-locked
primitive Picard basis.  The solver sees all 140 nonnegative intersections,
the exact positive-dual weighted budget, optional immutable (e,a) subshards,
and the exact integral adjunction quadratic inequality.  QF_NIA results are
logical SAT/UNSAT results; no floating-point feasibility result is accepted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import time
from typing import Any

import z3


EXPECTED_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def load_core(path: pathlib.Path) -> tuple[dict[str, Any], str]:
    core = json.loads(path.read_text(encoding="utf-8"))
    assert core["schema"] == EXPECTED_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert core["rank"] == 64 and core["known_class_count"] == 140
    assert core["h2"] == 16 and core["basis_gram_determinant"] == -268435456
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    actual = canonical_sha256(unsigned)
    assert actual == claimed
    return core, actual


def linear_form(vector: list[int], variables: list[z3.ArithRef]) -> z3.ArithRef:
    terms = [coefficient * variables[j] for j, coefficient in enumerate(vector) if coefficient]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def integer_pairing(left: list[int], gram: list[list[int]], right: list[int]) -> int:
    return sum(left[i] * gram[i][j] * right[j] for i in range(64) for j in range(64))


def exact_forms(core: dict[str, Any]) -> tuple[list[int], list[int], list[int]]:
    gram = core["basis_gram"]
    intersections = core["raw_cross_pairings_with_basis"]
    hyperplane = core["hyperplane"]
    hform = [sum(hyperplane[i] * gram[i][j] for i in range(64)) for j in range(64)]
    exceptional = [sum(intersections[k][j] for k in range(92, 140)) for j in range(64)]
    first_curve_group = [sum(intersections[k][j] for k in range(46)) for j in range(64)]
    weighted = [
        sum(intersections[k][j] for k in range(92))
        + 5 * sum(intersections[k][j] for k in range(92, 140))
        for j in range(64)
    ]
    assert weighted == [19 * value for value in hform]
    known_self = [integer_pairing(c, gram, c) for c in core["known_classes"]]
    assert all(value < 0 for value in known_self)
    return hform, exceptional, first_curve_group


def add_exact_constraints(
    solver: z3.Solver,
    core: dict[str, Any],
    variables: list[z3.ArithRef],
    degree: int,
    genus: int,
    exceptional_mass: int | None,
    curve_group_mass: int | None,
    curve_quarter_mass: int | None,
    exceptional_half_mass: int | None,
    second_curve_quarter_mass: int | None,
    exceptional_quarter_mass: int | None,
    second_exceptional_quarter_mass: int | None,
    curve_eighth_mass: int | None,
    curve_sixteenth_mass: int | None,
) -> tuple[list[z3.ArithRef], z3.ArithRef]:
    gram = core["basis_gram"]
    rows = core["raw_cross_pairings_with_basis"]
    hform, exceptional, first_curve_group = exact_forms(core)
    pairings = [linear_form(row, variables) for row in rows]
    solver.add(*(value >= 0 for value in pairings))
    solver.add(linear_form(hform, variables) == degree)
    solver.add(z3.Sum(pairings[:92]) + 5 * z3.Sum(pairings[92:]) == 19 * degree)

    if exceptional_mass is None:
        solver.add(*(value <= 19 * degree for value in pairings[:92]))
        solver.add(*(value <= 19 * degree // 5 for value in pairings[92:]))
    else:
        nonexceptional_mass = 19 * degree - 5 * exceptional_mass
        solver.add(linear_form(exceptional, variables) == exceptional_mass)
        solver.add(z3.Sum(pairings[92:]) == exceptional_mass)
        solver.add(*(value <= exceptional_mass for value in pairings[92:]))
        if exceptional_half_mass is not None:
            solver.add(z3.Sum(pairings[92:116]) == exceptional_half_mass)
            solver.add(z3.Sum(pairings[116:]) == exceptional_mass - exceptional_half_mass)
            solver.add(*(value <= exceptional_half_mass for value in pairings[92:116]))
            solver.add(
                *(value <= exceptional_mass - exceptional_half_mass for value in pairings[116:])
            )
            if exceptional_quarter_mass is not None:
                solver.add(z3.Sum(pairings[92:104]) == exceptional_quarter_mass)
                solver.add(
                    z3.Sum(pairings[104:116])
                    == exceptional_half_mass - exceptional_quarter_mass
                )
                solver.add(*(value <= exceptional_quarter_mass for value in pairings[92:104]))
                solver.add(
                    *(
                        value <= exceptional_half_mass - exceptional_quarter_mass
                        for value in pairings[104:116]
                    )
                )
            if second_exceptional_quarter_mass is not None:
                second_half_mass = exceptional_mass - exceptional_half_mass
                solver.add(
                    z3.Sum(pairings[116:128]) == second_exceptional_quarter_mass
                )
                solver.add(
                    z3.Sum(pairings[128:])
                    == second_half_mass - second_exceptional_quarter_mass
                )
                solver.add(
                    *(
                        value <= second_exceptional_quarter_mass
                        for value in pairings[116:128]
                    )
                )
                solver.add(
                    *(
                        value <= second_half_mass - second_exceptional_quarter_mass
                        for value in pairings[128:]
                    )
                )
        if curve_group_mass is None:
            solver.add(*(value <= nonexceptional_mass for value in pairings[:92]))
        else:
            second_curve_group_mass = nonexceptional_mass - curve_group_mass
            solver.add(linear_form(first_curve_group, variables) == curve_group_mass)
            solver.add(z3.Sum(pairings[:46]) == curve_group_mass)
            solver.add(z3.Sum(pairings[46:92]) == second_curve_group_mass)
            solver.add(*(value <= curve_group_mass for value in pairings[:46]))
            solver.add(*(value <= second_curve_group_mass for value in pairings[46:92]))
            if curve_quarter_mass is not None:
                solver.add(z3.Sum(pairings[:23]) == curve_quarter_mass)
                solver.add(z3.Sum(pairings[23:46]) == curve_group_mass - curve_quarter_mass)
                solver.add(*(value <= curve_quarter_mass for value in pairings[:23]))
                solver.add(
                    *(value <= curve_group_mass - curve_quarter_mass for value in pairings[23:46])
                )
                if curve_eighth_mass is not None:
                    solver.add(z3.Sum(pairings[:11]) == curve_eighth_mass)
                    solver.add(
                        z3.Sum(pairings[11:23])
                        == curve_quarter_mass - curve_eighth_mass
                    )
                    if curve_sixteenth_mass is not None:
                        solver.add(z3.Sum(pairings[:5]) == curve_sixteenth_mass)
                        solver.add(
                            z3.Sum(pairings[5:11])
                            == curve_eighth_mass - curve_sixteenth_mass
                        )
                        solver.add(
                            *(value <= curve_sixteenth_mass for value in pairings[:5])
                        )
                        solver.add(
                            *(
                                value <= curve_eighth_mass - curve_sixteenth_mass
                                for value in pairings[5:11]
                            )
                        )
                    solver.add(*(value <= curve_eighth_mass for value in pairings[:11]))
                    solver.add(
                        *(
                            value <= curve_quarter_mass - curve_eighth_mass
                            for value in pairings[11:23]
                        )
                    )
            if second_curve_quarter_mass is not None:
                solver.add(z3.Sum(pairings[46:69]) == second_curve_quarter_mass)
                solver.add(
                    z3.Sum(pairings[69:92])
                    == second_curve_group_mass - second_curve_quarter_mass
                )
                solver.add(
                    *(value <= second_curve_quarter_mass for value in pairings[46:69])
                )
                solver.add(
                    *(
                        value <= second_curve_group_mass - second_curve_quarter_mass
                        for value in pairings[69:92]
                    )
                )

    quadratic = z3.Sum(
        [
            gram[i][j] * variables[i] * variables[j]
            for i in range(64)
            for j in range(64)
            if gram[i][j]
        ]
    )
    lower = -degree - 2 + 2 * genus
    solver.add(quadratic >= lower)
    return pairings, quadratic


def verify_model(
    core: dict[str, Any],
    vector: list[int],
    degree: int,
    genus: int,
    exceptional_mass: int | None,
    curve_group_mass: int | None,
    curve_quarter_mass: int | None,
    exceptional_half_mass: int | None,
    second_curve_quarter_mass: int | None,
    exceptional_quarter_mass: int | None,
    second_exceptional_quarter_mass: int | None,
    curve_eighth_mass: int | None,
    curve_sixteenth_mass: int | None,
) -> dict[str, Any]:
    gram = core["basis_gram"]
    rows = core["raw_cross_pairings_with_basis"]
    hform, _, _ = exact_forms(core)
    pairings = [sum(row[j] * vector[j] for j in range(64)) for row in rows]
    square = integer_pairing(vector, gram, vector)
    assert sum(hform[j] * vector[j] for j in range(64)) == degree
    assert all(value >= 0 for value in pairings)
    assert sum(pairings[:92]) + 5 * sum(pairings[92:]) == 19 * degree
    assert square >= -degree - 2 + 2 * genus
    if exceptional_mass is not None:
        assert sum(pairings[92:]) == exceptional_mass
    if curve_group_mass is not None:
        assert sum(pairings[:46]) == curve_group_mass
    if curve_quarter_mass is not None:
        assert sum(pairings[:23]) == curve_quarter_mass
    if exceptional_half_mass is not None:
        assert sum(pairings[92:116]) == exceptional_half_mass
    if second_curve_quarter_mass is not None:
        assert sum(pairings[46:69]) == second_curve_quarter_mass
    if exceptional_quarter_mass is not None:
        assert sum(pairings[92:104]) == exceptional_quarter_mass
    if second_exceptional_quarter_mass is not None:
        assert sum(pairings[116:128]) == second_exceptional_quarter_mass
    if curve_eighth_mass is not None:
        assert sum(pairings[:11]) == curve_eighth_mass
    if curve_sixteenth_mass is not None:
        assert sum(pairings[:5]) == curve_sixteenth_mass
    return {
        "picard_coordinates": vector,
        "self_intersection": square,
        "intersection_vector_sha256": hashlib.sha256(
            json.dumps(pairings, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def statistics_dict(statistics: z3.Statistics) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key in statistics.keys():
        value = statistics.get_key_value(key)
        result[key] = value
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), required=True)
    parser.add_argument("--exceptional-mass", type=int)
    parser.add_argument("--curve-group-mass", type=int)
    parser.add_argument("--curve-quarter-mass", type=int)
    parser.add_argument("--exceptional-half-mass", type=int)
    parser.add_argument("--second-curve-quarter-mass", type=int)
    parser.add_argument("--exceptional-quarter-mass", type=int)
    parser.add_argument("--second-exceptional-quarter-mass", type=int)
    parser.add_argument("--curve-eighth-mass", type=int)
    parser.add_argument("--curve-sixteenth-mass", type=int)
    parser.add_argument("--timeout", type=float, default=0.0)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--max-models", type=int, default=0)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()

    if args.degree <= 0 or args.degree % 2:
        raise SystemExit("degree must be positive and even")
    if args.curve_group_mass is not None and args.exceptional_mass is None:
        raise SystemExit("curve-group mass requires exceptional mass")
    if args.curve_quarter_mass is not None and args.curve_group_mass is None:
        raise SystemExit("curve-quarter mass requires curve-group mass")
    if args.exceptional_half_mass is not None and args.exceptional_mass is None:
        raise SystemExit("exceptional-half mass requires exceptional mass")
    if args.second_curve_quarter_mass is not None and args.curve_group_mass is None:
        raise SystemExit("second curve-quarter mass requires curve-group mass")
    if args.exceptional_quarter_mass is not None and args.exceptional_half_mass is None:
        raise SystemExit("exceptional-quarter mass requires exceptional-half mass")
    if args.second_exceptional_quarter_mass is not None and args.exceptional_half_mass is None:
        raise SystemExit("second exceptional-quarter mass requires exceptional-half mass")
    if args.curve_eighth_mass is not None and args.curve_quarter_mass is None:
        raise SystemExit("curve-eighth mass requires curve-quarter mass")
    if args.curve_sixteenth_mass is not None and args.curve_eighth_mass is None:
        raise SystemExit("curve-sixteenth mass requires curve-eighth mass")
    if args.exceptional_mass is not None:
        if not 0 <= args.exceptional_mass <= 19 * args.degree // 5:
            raise SystemExit("exceptional mass is outside the exact budget")
        remaining = 19 * args.degree - 5 * args.exceptional_mass
        if args.curve_group_mass is not None and not 0 <= args.curve_group_mass <= remaining:
            raise SystemExit("curve-group mass is outside the exact budget")
        if args.curve_quarter_mass is not None and not 0 <= args.curve_quarter_mass <= args.curve_group_mass:
            raise SystemExit("curve-quarter mass is outside the exact group budget")
        if args.curve_eighth_mass is not None and not 0 <= args.curve_eighth_mass <= args.curve_quarter_mass:
            raise SystemExit("curve-eighth mass is outside the exact quarter budget")
        if args.curve_sixteenth_mass is not None and not 0 <= args.curve_sixteenth_mass <= args.curve_eighth_mass:
            raise SystemExit("curve-sixteenth mass is outside the exact eighth budget")
        if args.exceptional_half_mass is not None and not 0 <= args.exceptional_half_mass <= args.exceptional_mass:
            raise SystemExit("exceptional-half mass is outside the exact exceptional budget")
        if args.exceptional_quarter_mass is not None and not 0 <= args.exceptional_quarter_mass <= args.exceptional_half_mass:
            raise SystemExit("exceptional-quarter mass is outside the exact half budget")
        second_exceptional_half = args.exceptional_mass - (args.exceptional_half_mass or 0)
        if args.second_exceptional_quarter_mass is not None and not 0 <= args.second_exceptional_quarter_mass <= second_exceptional_half:
            raise SystemExit("second exceptional-quarter mass is outside the exact half budget")
        second_group = remaining - (args.curve_group_mass or 0)
        if args.second_curve_quarter_mass is not None and not 0 <= args.second_curve_quarter_mass <= second_group:
            raise SystemExit("second curve-quarter mass is outside the exact second-group budget")

    if args.proof:
        z3.set_param(proof=True)
    core, core_sha256 = load_core(args.core)
    variables = [z3.Int(f"picard_{i + 1}") for i in range(64)]
    solver = z3.SolverFor("QF_NIA")
    solver.set(random_seed=0, threads=args.threads)
    if args.timeout:
        solver.set(timeout=int(args.timeout * 1000))
    add_exact_constraints(
        solver,
        core,
        variables,
        args.degree,
        args.genus,
        args.exceptional_mass,
        args.curve_group_mass,
        args.curve_quarter_mass,
        args.exceptional_half_mass,
        args.second_curve_quarter_mass,
        args.exceptional_quarter_mass,
        args.second_exceptional_quarter_mass,
        args.curve_eighth_mass,
        args.curve_sixteenth_mass,
    )

    label = f"d{args.degree}-g{args.genus}"
    if args.exceptional_mass is not None:
        label += f"-e{args.exceptional_mass}"
    if args.curve_group_mass is not None:
        label += f"-a{args.curve_group_mass}"
    if args.curve_quarter_mass is not None:
        label += f"-b{args.curve_quarter_mass}"
    if args.exceptional_half_mass is not None:
        label += f"-f{args.exceptional_half_mass}"
    if args.second_curve_quarter_mass is not None:
        label += f"-c{args.second_curve_quarter_mass}"
    if args.exceptional_quarter_mass is not None:
        label += f"-h{args.exceptional_quarter_mass}"
    if args.second_exceptional_quarter_mass is not None:
        label += f"-k{args.second_exceptional_quarter_mass}"
    if args.curve_eighth_mass is not None:
        label += f"-l{args.curve_eighth_mass}"
    if args.curve_sixteenth_mass is not None:
        label += f"-m{args.curve_sixteenth_mass}"
    shard_dir = args.output_dir / label
    shard_dir.mkdir(parents=True, exist_ok=True)
    smt_text = solver.to_smt2()
    smt_path = shard_dir / "problem.smt2"
    smt_path.write_text(smt_text, encoding="utf-8", newline="\n")
    smt_sha256 = hashlib.sha256(smt_text.encode()).hexdigest()

    survivors: list[dict[str, Any]] = []
    proof_sha256: str | None = None
    proof_path: pathlib.Path | None = None
    start = time.perf_counter()
    final_result = solver.check()
    while final_result == z3.sat:
        model = solver.model()
        vector = [model.eval(variable, model_completion=True).as_long() for variable in variables]
        survivors.append(
            verify_model(
                core,
                vector,
                args.degree,
                args.genus,
                args.exceptional_mass,
                args.curve_group_mass,
                args.curve_quarter_mass,
                args.exceptional_half_mass,
                args.second_curve_quarter_mass,
                args.exceptional_quarter_mass,
                args.second_exceptional_quarter_mass,
                args.curve_eighth_mass,
                args.curve_sixteenth_mass,
            )
        )
        if args.max_models and len(survivors) >= args.max_models:
            break
        solver.add(z3.Or([variable != value for variable, value in zip(variables, vector)]))
        final_result = solver.check()
    elapsed = time.perf_counter() - start
    if final_result == z3.unsat and args.proof:
        proof_text = solver.proof().sexpr() + "\n"
        proof_path = shard_dir / "proof.sexpr"
        proof_path.write_text(proof_text, encoding="utf-8", newline="\n")
        proof_sha256 = hashlib.sha256(proof_text.encode()).hexdigest()

    complete = final_result == z3.unsat
    payload: dict[str, Any] = {
        "schema": "STAGE32_EXACT_Z3_BUDGET_SHARD_V1",
        "backend": "Z3 QF_NIA exact integer branch-and-bound",
        "z3_version": z3.get_version_string(),
        "degree": args.degree,
        "genus": args.genus,
        "exceptional_mass": args.exceptional_mass,
        "curve_group_mass": args.curve_group_mass,
        "curve_quarter_mass": args.curve_quarter_mass,
        "exceptional_half_mass": args.exceptional_half_mass,
        "second_curve_quarter_mass": args.second_curve_quarter_mass,
        "exceptional_quarter_mass": args.exceptional_quarter_mass,
        "second_exceptional_quarter_mass": args.second_exceptional_quarter_mass,
        "curve_eighth_mass": args.curve_eighth_mass,
        "curve_sixteenth_mass": args.curve_sixteenth_mass,
        "weighted_intersection_budget": 19 * args.degree,
        "adjunction_self_intersection_lower_bound": -args.degree - 2 + 2 * args.genus,
        "picard_core_sha256": core_sha256,
        "smt2_sha256": smt_sha256,
        "proof_sha256": proof_sha256,
        "solver_result": str(final_result),
        "unknown_reason": solver.reason_unknown() if final_result == z3.unknown else None,
        "complete": complete,
        "exact_survivor_count": len(survivors) if complete else None,
        "survivors": survivors,
        "known_class_subtraction": "all 140 excluded by their negative self-intersection constraint",
        "known_class_count_excluded": 140,
        "floating_point_feasibility_credit": False,
        "threads": args.threads,
        "random_seed": 0,
        "elapsed_seconds": round(elapsed, 6),
        "solver_statistics": statistics_dict(solver.statistics()),
        "files": {
            "problem": smt_path.name,
            "proof": proof_path.name if proof_path else None,
        },
    }
    deterministic_result = {
        key: payload[key]
        for key in (
            "schema",
            "backend",
            "z3_version",
            "degree",
            "genus",
            "exceptional_mass",
            "curve_group_mass",
            "curve_quarter_mass",
            "exceptional_half_mass",
            "second_curve_quarter_mass",
            "exceptional_quarter_mass",
            "second_exceptional_quarter_mass",
            "curve_eighth_mass",
            "curve_sixteenth_mass",
            "weighted_intersection_budget",
            "adjunction_self_intersection_lower_bound",
            "picard_core_sha256",
            "smt2_sha256",
            "proof_sha256",
            "solver_result",
            "complete",
            "exact_survivor_count",
            "survivors",
            "known_class_count_excluded",
            "floating_point_feasibility_credit",
            "random_seed",
        )
    }
    payload["deterministic_result_sha256"] = canonical_sha256(deterministic_result)
    unsigned = dict(payload)
    payload["checkpoint_sha256_without_this_field"] = canonical_sha256(unsigned)
    checkpoint_path = shard_dir / "checkpoint.json"
    checkpoint_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))
    if not complete:
        raise SystemExit("exact enumeration did not close this shard")


if __name__ == "__main__":
    main()
