#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import pathlib
import sys
import time
from typing import Any

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
STAGE32_05 = HERE.parent / "32-05"
sys.path.insert(0, str(STAGE32_05))

import cap_certificate  # type: ignore
import run_exact_mitm_closure as base  # type: ignore

SCHEMA = "STAGE32_EXACT_MITM_DEGREE4_CLOSURE_V1"
ALGORITHM_ID = "FIXED_WEIGHT_MITM_D4_QTAIL_SUBGROUP_OVERRELAX_TO_QF_NIA_V1"
DEGREE = 4
GENUS = 0
NORMAL_CAP = DEGREE // 2
EXCEPTIONAL_CAP = DEGREE // 4
assert NORMAL_CAP == 2 and EXCEPTIONAL_CAP == 1
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def aggregate_solutions(e: int, a: int) -> list[tuple[int, int, int, int]]:
    out: list[tuple[int, int, int, int]] = []
    for x in range(33):
        for y in range(9):
            for z in range(9):
                if x + y + z != e:
                    continue
                # q1..q4 are selected normal intersections, each in 0..2.
                for t in range(4 * NORMAL_CAP + 1):
                    if 8 * y + 16 * z + 16 * t != 8 * DEGREE:
                        continue
                    if -24 * x + 32 * y + 96 * z + 120 * t != 8 * a:
                        continue
                    if (
                        -40 * x + 112 * y + 264 * z + 304 * t
                        != 8 * (19 * DEGREE - 5 * e)
                    ):
                        continue
                    out.append((x, y, z, t))
    return out


def exact_join(
    signature_matrix: np.ndarray, types: list[str], e: int, a: int
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    left_groups, right_groups = base.split_groups(types)
    aggregate = aggregate_solutions(e, a)

    # In the full q-tail subgroup quotient the q-head signature must depend
    # only on the q-head sum. Verify that statement using only legal d=4
    # q-head values 0..2.
    qsignatures: dict[int, bytes] = {}
    qassignment_counts: dict[int, int] = {}
    for total in range(4 * NORMAL_CAP + 1):
        signatures: set[bytes] = set()
        assignment_count = 0
        for values in itertools.product(range(NORMAL_CAP + 1), repeat=4):
            if sum(values) != total:
                continue
            assignment_count += 1
            vector = np.array(values, dtype=np.int64)
            signatures.add(
                ((signature_matrix[:, 48:52].astype(np.int64) @ vector) % 8)
                .astype(np.uint8)
                .tobytes()
            )
        if signatures:
            assert len(signatures) == 1
            qsignatures[total] = next(iter(signatures))
            qassignment_counts[total] = assignment_count

    left_cache: dict[tuple[int, int, int], dict[bytes, list[int]]] = {}
    right_cache: dict[tuple[int, int, int], dict[bytes, list[int]]] = {}
    candidates: list[dict[str, Any]] = []
    split_records: list[dict[str, Any]] = []

    for x, y, z, total in aggregate:
        qsignature = np.frombuffer(qsignatures[total], dtype=np.uint8).astype(np.int16)
        for x_left in range(x + 1):
            for y_left in range(y + 1):
                for z_left in range(z + 1):
                    x_right, y_right, z_right = x - x_left, y - y_left, z - z_left
                    if (
                        x_left > 16
                        or x_right > 16
                        or y_left > 4
                        or y_right > 4
                        or z_left > 4
                        or z_right > 4
                    ):
                        continue
                    lk = (x_left, y_left, z_left)
                    rk = (x_right, y_right, z_right)
                    if lk not in left_cache:
                        left_cache[lk] = base.enumerate_side(signature_matrix, left_groups, *lk)
                    if rk not in right_cache:
                        right_cache[rk] = base.enumerate_side(signature_matrix, right_groups, *rk)
                    left_map, right_map = left_cache[lk], right_cache[rk]
                    matched_signatures = 0
                    matched_pairs = 0
                    for left_sig_bytes, left_masks in left_map.items():
                        left_sig = np.frombuffer(left_sig_bytes, dtype=np.uint8).astype(np.int16)
                        target = ((-left_sig - qsignature) % 8).astype(np.uint8).tobytes()
                        right_masks = right_map.get(target)
                        if not right_masks:
                            continue
                        matched_signatures += 1
                        matched_pairs += len(left_masks) * len(right_masks)
                        for lm in left_masks:
                            for rm in right_masks:
                                candidates.append(
                                    {
                                        "exceptional_mask": lm | rm,
                                        "qhead_sum": total,
                                        "aggregate_type_counts": [x, y, z],
                                    }
                                )
                    split_records.append(
                        {
                            "aggregate": [x, y, z, total],
                            "left_counts": list(lk),
                            "right_counts": list(rk),
                            "left_state_count": sum(map(len, left_map.values())),
                            "right_state_count": sum(map(len, right_map.values())),
                            "left_signature_count": len(left_map),
                            "right_signature_count": len(right_map),
                            "matched_signature_count": matched_signatures,
                            "matched_exceptional_pair_count": matched_pairs,
                        }
                    )

    unique = {
        (candidate["exceptional_mask"], candidate["qhead_sum"]): candidate
        for candidate in candidates
    }
    candidates = [unique[key] for key in sorted(unique)]
    return candidates, {
        "aggregate_solutions": [list(solution) for solution in aggregate],
        "qhead_assignment_counts_by_sum": {
            str(key): value for key, value in qassignment_counts.items()
        },
        "split_records": split_records,
        "matched_exceptional_candidate_count": len(candidates),
        "qtail_quotient_role": "NECESSARY_OVERRELAXATION_ONLY",
        "qtail_reason": (
            "The HNF quotient annihilates the subgroup generated by q-tail values 0..3. "
            "At degree 4 the legal q-tail range is only 0..2, so quotient membership is "
            "used only as a necessary condition; exact 0..2 feasibility is restored in QF_NIA."
        ),
    }


def mask_vector(mask: int) -> list[int]:
    return [(mask >> j) & 1 for j in range(48)]


def solve_candidates(
    transform: dict[str, Any],
    candidates: list[dict[str, Any]],
    e: int,
    a: int,
    proof_dir: pathlib.Path | None,
    timeout_seconds: float,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    import z3

    if proof_dir is not None:
        z3.set_param(proof=True)
        proof_dir.mkdir(parents=True, exist_ok=True)

    inv = transform["inv"]
    pairings = transform["pair"]
    hform = transform["h"]
    gram = transform["gram"]
    qvars = [z3.Int(f"q{j + 1}") for j in range(16)]
    rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    lower = -DEGREE - 2 + 2 * GENUS

    for candidate_index, candidate in enumerate(candidates):
        exceptional = np.array(mask_vector(candidate["exceptional_mask"]), dtype=np.int64)
        solver = z3.SolverFor("QF_NIA")
        solver.set(random_seed=0, threads=1)
        if timeout_seconds:
            solver.set(timeout=int(timeout_seconds * 1000))
        for variable in qvars:
            solver.add(variable >= 0, variable <= NORMAL_CAP)

        for i in range(64):
            constant = int(inv[i, :48] @ exceptional)
            terms = [int(inv[i, 48 + j]) * qvars[j] for j in range(16) if inv[i, 48 + j]]
            solver.add((constant + (z3.Sum(terms) if terms else 0)) % 8 == 0)

        pairing_expressions = []
        for i in range(140):
            constant = int(pairings[i, :48] @ exceptional)
            terms = [
                int(pairings[i, 48 + j]) * qvars[j]
                for j in range(16)
                if pairings[i, 48 + j]
            ]
            expression = constant + (z3.Sum(terms) if terms else 0)
            pairing_expressions.append(expression)
            cap = NORMAL_CAP if i < 92 else EXCEPTIONAL_CAP
            solver.add(expression >= 0, expression <= 8 * cap)

        constant_h = int(hform[:48] @ exceptional)
        h_terms = [int(hform[48 + j]) * qvars[j] for j in range(16) if hform[48 + j]]
        solver.add(constant_h + (z3.Sum(h_terms) if h_terms else 0) == 8 * DEGREE)
        solver.add(z3.Sum(pairing_expressions[92:]) == 8 * e)
        solver.add(z3.Sum(pairing_expressions[:46]) == 8 * a)
        solver.add(
            z3.Sum(pairing_expressions[:92]) + 5 * z3.Sum(pairing_expressions[92:])
            == 8 * 19 * DEGREE
        )
        solver.add(z3.Sum(qvars[:4]) == candidate["qhead_sum"])

        constant_square = int(exceptional @ gram[:48, :48] @ exceptional)
        linear_terms = []
        for j in range(16):
            coefficient = int(2 * (exceptional @ gram[:48, 48 + j]))
            if coefficient:
                linear_terms.append(coefficient * qvars[j])
        quadratic_terms = []
        for i in range(16):
            for j in range(16):
                coefficient = int(gram[48 + i, 48 + j])
                if coefficient:
                    quadratic_terms.append(coefficient * qvars[i] * qvars[j])
        solver.add(
            constant_square
            + (z3.Sum(linear_terms) if linear_terms else 0)
            + (z3.Sum(quadratic_terms) if quadratic_terms else 0)
            >= 64 * lower
        )

        started = time.perf_counter()
        result = solver.check()
        elapsed = time.perf_counter() - started
        entry: dict[str, Any] = {
            "candidate_index": candidate_index,
            "exceptional_mask_hex": hex(candidate["exceptional_mask"]),
            "qhead_sum": candidate["qhead_sum"],
            "solver_result": str(result),
            "elapsed_seconds": elapsed,
        }
        if result == z3.sat:
            model = solver.model()
            qvalues = [model.eval(variable, model_completion=True).as_long() for variable in qvars]
            selected = np.array(mask_vector(candidate["exceptional_mask"]) + qvalues, dtype=np.int64)
            assert np.all((inv @ selected) % 8 == 0)
            numerator = pairings @ selected
            assert np.all(numerator % 8 == 0)
            intersection_vector = numerator // 8
            assert np.all((intersection_vector[:92] >= 0) & (intersection_vector[:92] <= NORMAL_CAP))
            assert np.all((intersection_vector[92:] >= 0) & (intersection_vector[92:] <= EXCEPTIONAL_CAP))
            assert int(intersection_vector[92:].sum()) == e
            assert int(intersection_vector[:46].sum()) == a
            assert int(hform @ selected) == 8 * DEGREE
            assert int(selected @ gram @ selected) >= 64 * lower
            entry["q_values"] = qvalues
            entry["intersection_vector_sha256"] = canonical_sha256(intersection_vector.astype(int).tolist())
            survivors.append(dict(entry))
        elif result == z3.unsat and proof_dir is not None:
            proof_raw = (solver.proof().sexpr() + "\n").encode()
            proof_sha = hashlib.sha256(proof_raw).hexdigest()
            proof_name = f"candidate-{candidate_index:04d}.sexpr.gz"
            with gzip.open(proof_dir / proof_name, "wb", compresslevel=9) as handle:
                handle.write(proof_raw)
            entry["proof_sha256"] = proof_sha
            entry["proof_gzip_name"] = proof_name
        elif result != z3.unsat:
            entry["unknown_reason"] = solver.reason_unknown()
        rows.append(entry)

    return rows, survivors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--candidate-timeout", type=float, default=5.0)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = cap_certificate.load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = base.build_transform(core)
    quotient = base.quotient_data(transform["inv"])
    aggregate = base.aggregate_structure(transform["pair"], transform["h"])
    candidates, join_certificate = exact_join(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "candidates.json").write_text(
        json.dumps(candidates, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    solver_rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    if candidates:
        solver_rows, survivors = solve_candidates(
            transform,
            candidates,
            args.exceptional_mass,
            args.curve_group_mass,
            args.output_dir / "proofs" if args.proof else None,
            max(0.0, args.candidate_timeout),
        )

    complete = (not candidates) or (
        len(solver_rows) == len(candidates)
        and all(row["solver_result"] == "unsat" for row in solver_rows)
    )
    closed = bool(complete and not survivors)
    report: dict[str, Any] = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": DEGREE,
            "genus": GENUS,
            "normal_cap": NORMAL_CAP,
            "exceptional_cap": EXCEPTIONAL_CAP,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "candidate_timeout_seconds": max(0.0, args.candidate_timeout),
        },
        "cap_verification": cap_summary,
        "transform_certificate": transform["certificate"],
        "quotient_certificate": quotient["certificate"],
        "aggregate_certificate": aggregate["certificate"],
        "join_certificate": join_certificate,
        "candidate_list_sha256": canonical_sha256(candidates),
        "candidate_count": len(candidates),
        "solver_rows": solver_rows,
        "survivor_count": len(survivors),
        "parent_exactly_closed": closed,
        "bounded_parent_exact_closure_claim": closed,
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "low_degree_prefix_complete": False,
        "full_d176_d192_numerical_orbit_census": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
        "elapsed_seconds": time.perf_counter() - started,
    }
    (args.output_dir / "manifest.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "e": args.exceptional_mass,
                "a": args.curve_group_mass,
                "candidate_count": len(candidates),
                "survivors": len(survivors),
                "closed": closed,
                "elapsed": report["elapsed_seconds"],
            },
            sort_keys=True,
        )
    )
    if not closed:
        raise SystemExit("degree-4 pilot parent not exactly closed")


if __name__ == "__main__":
    main()
