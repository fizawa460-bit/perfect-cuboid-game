#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import itertools
import json
import math
import pathlib
import time
from typing import Any

import numpy as np
import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

from cap_certificate import load_and_verify

SCHEMA = "STAGE32_EXACT_MITM_QUOTIENT_CLOSURE_V1"
ALGORITHM_ID = "FIXED_WEIGHT_MITM_QTAIL_HNF_QUOTIENT_TO_QF_NIA_V1"
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_DET = 274877906944
EXPECTED_DEN = 8
EXPECTED_SNF = [1] * 40 + [2] * 14 + [4] * 6 + [8] * 4
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"
CANDIDATE_TIMEOUT_SECONDS = 5.0


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_list(matrix: Matrix) -> list[list[int]]:
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def build_transform(core: dict[str, Any]) -> dict[str, Any]:
    rows = Matrix(core["raw_cross_pairings_with_basis"])
    gram = Matrix(core["basis_gram"])
    selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
    determinant = int(selected.det())
    assert abs(determinant) == EXPECTED_DET

    inverse = selected.inv()
    denominator = 1
    for value in inverse:
        denominator = math.lcm(denominator, int(sympy.denom(value)))
    assert denominator == EXPECTED_DEN
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
    hrow = [int(transformed_hform[0, j]) for j in range(64)]
    transformed_gram = inverse_integer.T * gram * inverse_integer
    assert all(sympy.denom(value) == 1 for value in transformed_gram)
    transformed_gram = Matrix(
        [[int(transformed_gram[i, j]) for j in range(64)] for i in range(64)]
    )

    diagonal = smith_normal_form(selected, domain=sympy.ZZ)
    invariants = sorted(abs(int(diagonal[i, i])) for i in range(64))
    assert invariants == EXPECTED_SNF

    return {
        "den": denominator,
        "inv": np.array(matrix_list(inverse_integer), dtype=np.int64),
        "pair": np.array(matrix_list(transformed_pairings), dtype=np.int64),
        "h": np.array(hrow, dtype=np.int64),
        "gram": np.array(matrix_list(transformed_gram), dtype=np.int64),
        "certificate": {
            "selected_matrix_determinant": determinant,
            "inverse_denominator": denominator,
            "selected_matrix_sha256": canonical_sha256(matrix_list(selected)),
            "inverse_integer_matrix_sha256": canonical_sha256(matrix_list(inverse_integer)),
            "transformed_pairing_matrix_sha256": canonical_sha256(matrix_list(transformed_pairings)),
            "transformed_gram_sha256": canonical_sha256(matrix_list(transformed_gram)),
            "snf_invariant_counts": {"1": 40, "2": 14, "4": 6, "8": 4},
        },
    }


def order_mod8(column: np.ndarray) -> int:
    column = column % 8
    for order in (1, 2, 4, 8):
        if np.all((order * column) % 8 == 0):
            return order
    raise AssertionError("mod-8 column order not found")


def quotient_data(inverse_integer: np.ndarray) -> dict[str, Any]:
    # q-tail = selected-normal coordinates 5..16, i.e. selected coordinates
    # 53..64 in one-based numbering.  Their aggregate degree/mass contribution
    # is zero; their only role here is congruence completion and the later exact
    # QF_NIA check.
    tail = Matrix(inverse_integer[:, 52:64].tolist())
    hnf = hermite_normal_form(tail.row_join(8 * Matrix.eye(64)))
    assert hnf.shape == (64, 64)
    determinant = 1
    for i in range(64):
        determinant *= abs(int(hnf[i, i]))
    subgroup_size = 8**64 // determinant

    annihilator = hnf.inv() * 8
    assert all(sympy.denom(value) == 1 for value in annihilator)
    annihilator = Matrix(
        [[int(annihilator[i, j]) for j in range(64)] for i in range(64)]
    )
    annihilator_np = np.array(matrix_list(annihilator), dtype=np.int64)
    signature_matrix = (annihilator_np @ inverse_integer) % 8
    assert np.all(signature_matrix[:, 52:64] == 0)

    orders = [order_mod8(inverse_integer[:, j]) for j in range(52, 64)]
    assert all(order <= 4 for order in orders)

    # Independent finite reachability check. Since each tail coordinate ranges
    # over 0..3 and every generator has order <=4, this should fill precisely
    # the subgroup certified by the HNF index.
    reachable = {bytes(64)}
    for j in range(52, 64):
        column = (inverse_integer[:, j] % 8).astype(np.uint8)
        next_set: set[bytes] = set()
        for residue_bytes in reachable:
            residue = np.frombuffer(residue_bytes, dtype=np.uint8).astype(np.int16)
            for value in range(4):
                next_set.add(
                    ((residue + value * column) % 8).astype(np.uint8).tobytes()
                )
        reachable = next_set
    assert len(reachable) == subgroup_size

    return {
        "K": signature_matrix.astype(np.uint8),
        "certificate": {
            "qtail_selected_coordinate_indices_1based": list(range(53, 65)),
            "qtail_column_orders_mod8": orders,
            "qtail_reachable_residue_count": len(reachable),
            "qtail_subgroup_size_from_hnf_index": subgroup_size,
            "qtail_hnf_diagonal_counts": dict(
                collections.Counter(str(abs(int(hnf[i, i]))) for i in range(64))
            ),
            "qtail_hnf_sha256": canonical_sha256(matrix_list(hnf)),
            "quotient_annihilator_sha256": canonical_sha256(matrix_list(annihilator)),
            "quotient_signature_matrix_sha256": canonical_sha256(
                signature_matrix.astype(int).tolist()
            ),
        },
    }


def aggregate_structure(pairings: np.ndarray, hform: np.ndarray) -> dict[str, Any]:
    arow = pairings[:46].sum(axis=0)
    nrow = pairings[:92].sum(axis=0)
    triples = [
        (int(hform[j]), int(arow[j]), int(nrow[j])) for j in range(48)
    ]
    counts = collections.Counter(triples)
    expected = {(0, -24, -40): 32, (8, 32, 112): 8, (16, 96, 264): 8}
    assert dict(counts) == expected
    labels = {
        (0, -24, -40): "A",
        (8, 32, 112): "B",
        (16, 96, 264): "C",
    }
    types = [labels[triple] for triple in triples]
    qhead = [
        (int(hform[j]), int(arow[j]), int(nrow[j])) for j in range(48, 52)
    ]
    qtail = [
        (int(hform[j]), int(arow[j]), int(nrow[j])) for j in range(52, 64)
    ]
    assert len(set(qhead)) == 1 and qhead[0] == (16, 120, 304)
    assert set(qtail) == {(0, 0, 0)}
    return {
        "types": types,
        "certificate": {
            "exceptional_aggregate_type_counts": {"A": 32, "B": 8, "C": 8},
            "exceptional_type_triples": {
                "A": [0, -24, -40],
                "B": [8, 32, 112],
                "C": [16, 96, 264],
            },
            "qhead_aggregate_triple": [16, 120, 304],
            "qtail_aggregate_triple": [0, 0, 0],
        },
    }


def aggregate_solutions(e: int, a: int) -> list[tuple[int, int, int, int]]:
    out: list[tuple[int, int, int, int]] = []
    for x in range(33):
        for y in range(9):
            for z in range(9):
                if x + y + z != e:
                    continue
                for t in range(13):
                    if 8 * y + 16 * z + 16 * t != 48:
                        continue
                    if -24 * x + 32 * y + 96 * z + 120 * t != 8 * a:
                        continue
                    if -40 * x + 112 * y + 264 * z + 304 * t != 8 * (114 - 5 * e):
                        continue
                    out.append((x, y, z, t))
    return out


def mask_for(indices: tuple[int, ...]) -> int:
    mask = 0
    for j in indices:
        mask |= 1 << j
    return mask


def split_groups(types: list[str]) -> tuple[dict[str, list[int]], dict[str, list[int]]]:
    by_type = {kind: [i for i, value in enumerate(types) if value == kind] for kind in "ABC"}
    left = {
        "A": by_type["A"][:16],
        "B": by_type["B"][:4],
        "C": by_type["C"][:4],
    }
    right = {
        "A": by_type["A"][16:],
        "B": by_type["B"][4:],
        "C": by_type["C"][4:],
    }
    assert all(len(left[kind]) == len(right[kind]) for kind in "ABC")
    return left, right


def part_records(
    signature_matrix: np.ndarray, columns: list[int], count: int
) -> tuple[np.ndarray, np.ndarray]:
    combos = list(itertools.combinations(columns, count))
    masks = np.array([mask_for(combo) for combo in combos], dtype=np.uint64)
    if count == 0:
        signatures = np.zeros((1, 64), dtype=np.uint8)
    else:
        indices = np.array(combos, dtype=np.int64)
        signatures = (
            signature_matrix[:, indices].sum(axis=2).T % 8
        ).astype(np.uint8)
    return masks, signatures


def enumerate_side(
    signature_matrix: np.ndarray,
    groups: dict[str, list[int]],
    x: int,
    y: int,
    z: int,
) -> dict[bytes, list[int]]:
    counts = {"A": x, "B": y, "C": z}
    for kind, count in counts.items():
        if count < 0 or count > len(groups[kind]):
            return {}
    parts = [
        part_records(signature_matrix, groups[kind], counts[kind]) for kind in "ABC"
    ]
    masks = np.array([0], dtype=np.uint64)
    signatures = np.zeros((1, 64), dtype=np.uint8)
    for part_masks, part_signatures in parts:
        masks = (masks[:, None] | part_masks[None, :]).reshape(-1)
        signatures = (
            (
                signatures[:, None, :].astype(np.uint16)
                + part_signatures[None, :, :].astype(np.uint16)
            )
            % 8
        ).reshape(-1, 64).astype(np.uint8)
    out: dict[bytes, list[int]] = {}
    for row, mask in zip(signatures, masks):
        out.setdefault(row.tobytes(), []).append(int(mask))
    return out


def exact_join(
    signature_matrix: np.ndarray, types: list[str], e: int, a: int
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    left_groups, right_groups = split_groups(types)
    aggregate = aggregate_solutions(e, a)

    # Verify exhaustively over all 4^4 assignments that the quotient signature
    # of the q-head depends only on t = q1+...+q4.
    qsignatures: dict[int, bytes] = {}
    qassignment_counts: dict[int, int] = {}
    for total in range(13):
        signatures: set[bytes] = set()
        assignment_count = 0
        for values in itertools.product(range(4), repeat=4):
            if sum(values) != total:
                continue
            assignment_count += 1
            vector = np.array(values, dtype=np.int64)
            signatures.add(
                (
                    (signature_matrix[:, 48:52].astype(np.int64) @ vector) % 8
                ).astype(np.uint8).tobytes()
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
                    x_right = x - x_left
                    y_right = y - y_left
                    z_right = z - z_left
                    if (
                        x_left > 16
                        or x_right > 16
                        or y_left > 4
                        or y_right > 4
                        or z_left > 4
                        or z_right > 4
                    ):
                        continue
                    left_key = (x_left, y_left, z_left)
                    right_key = (x_right, y_right, z_right)
                    if left_key not in left_cache:
                        left_cache[left_key] = enumerate_side(
                            signature_matrix, left_groups, *left_key
                        )
                    if right_key not in right_cache:
                        right_cache[right_key] = enumerate_side(
                            signature_matrix, right_groups, *right_key
                        )
                    left_map = left_cache[left_key]
                    right_map = right_cache[right_key]
                    matched_signatures = 0
                    matched_pairs = 0
                    for left_signature_bytes, left_masks in left_map.items():
                        left_signature = np.frombuffer(
                            left_signature_bytes, dtype=np.uint8
                        ).astype(np.int16)
                        target = ((-left_signature - qsignature) % 8).astype(
                            np.uint8
                        ).tobytes()
                        right_masks = right_map.get(target)
                        if not right_masks:
                            continue
                        matched_signatures += 1
                        matched_pairs += len(left_masks) * len(right_masks)
                        for left_mask in left_masks:
                            for right_mask in right_masks:
                                candidates.append(
                                    {
                                        "exceptional_mask": left_mask | right_mask,
                                        "qhead_sum": total,
                                        "aggregate_type_counts": [x, y, z],
                                    }
                                )
                    split_records.append(
                        {
                            "aggregate": [x, y, z, total],
                            "left_counts": [x_left, y_left, z_left],
                            "right_counts": [x_right, y_right, z_right],
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
    }


def mask_vector(mask: int) -> list[int]:
    return [(mask >> j) & 1 for j in range(48)]


def solve_candidates(
    transform: dict[str, Any],
    candidates: list[dict[str, Any]],
    e: int,
    a: int,
    genus: int,
    proof_dir: pathlib.Path | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    try:
        import z3
    except Exception as exc:
        raise SystemExit("z3-solver required for exact candidate solving") from exc

    if proof_dir is not None:
        z3.set_param(proof=True)
        proof_dir.mkdir(parents=True, exist_ok=True)

    inverse_integer = transform["inv"]
    pairings = transform["pair"]
    hform = transform["h"]
    gram = transform["gram"]
    qvars = [z3.Int(f"q{j + 1}") for j in range(16)]
    rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []

    for candidate_index, candidate in enumerate(candidates):
        exceptional = np.array(mask_vector(candidate["exceptional_mask"]), dtype=np.int64)
        solver = z3.SolverFor("QF_NIA")
        solver.set(random_seed=0, threads=1)
        if CANDIDATE_TIMEOUT_SECONDS:
            solver.set(timeout=int(CANDIDATE_TIMEOUT_SECONDS * 1000))
        for variable in qvars:
            solver.add(variable >= 0, variable <= 3)

        for i in range(64):
            constant = int(inverse_integer[i, :48] @ exceptional)
            terms = [
                int(inverse_integer[i, 48 + j]) * qvars[j]
                for j in range(16)
                if inverse_integer[i, 48 + j]
            ]
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
            cap = 3 if i < 92 else 1
            solver.add(expression >= 0, expression <= 8 * cap)

        constant_h = int(hform[:48] @ exceptional)
        h_terms = [
            int(hform[48 + j]) * qvars[j]
            for j in range(16)
            if hform[48 + j]
        ]
        solver.add(constant_h + (z3.Sum(h_terms) if h_terms else 0) == 48)
        solver.add(z3.Sum(pairing_expressions[92:]) == 8 * e)
        solver.add(z3.Sum(pairing_expressions[:46]) == 8 * a)
        solver.add(
            z3.Sum(pairing_expressions[:92]) + 5 * z3.Sum(pairing_expressions[92:])
            == 8 * 19 * 6
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
        lower = -6 - 2 + 2 * genus
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
            qvalues = [
                model.eval(variable, model_completion=True).as_long() for variable in qvars
            ]
            selected = np.array(
                mask_vector(candidate["exceptional_mask"]) + qvalues, dtype=np.int64
            )
            assert np.all((inverse_integer @ selected) % 8 == 0)
            numerator = pairings @ selected
            assert np.all(numerator % 8 == 0)
            intersection_vector = numerator // 8
            assert np.all((intersection_vector[:92] >= 0) & (intersection_vector[:92] <= 3))
            assert np.all((intersection_vector[92:] >= 0) & (intersection_vector[92:] <= 1))
            assert int(intersection_vector[92:].sum()) == e
            assert int(intersection_vector[:46].sum()) == a
            assert int(hform @ selected) == 48
            assert int(selected @ gram @ selected) >= 64 * lower
            entry["q_values"] = qvalues
            entry["intersection_vector_sha256"] = canonical_sha256(
                intersection_vector.astype(int).tolist()
            )
            survivors.append(dict(entry))
        elif result == z3.unsat and proof_dir is not None:
            proof_text = solver.proof().sexpr() + "\n"
            proof_raw = proof_text.encode()
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
    global CANDIDATE_TIMEOUT_SECONDS
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--genus", type=int, default=1)
    parser.add_argument("--reducer-only", action="store_true")
    parser.add_argument("--proof", action="store_true")
    parser.add_argument("--candidate-timeout", type=float, default=5.0)
    args = parser.parse_args()
    CANDIDATE_TIMEOUT_SECONDS = max(0.0, args.candidate_timeout)

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = build_transform(core)
    quotient = quotient_data(transform["inv"])
    aggregate = aggregate_structure(transform["pair"], transform["h"])
    candidates, join_certificate = exact_join(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "candidates.json").write_text(
        json.dumps(candidates, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    solver_rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    if not args.reducer_only and candidates:
        solver_rows, survivors = solve_candidates(
            transform,
            candidates,
            args.exceptional_mass,
            args.curve_group_mass,
            args.genus,
            args.output_dir / "proofs" if args.proof else None,
        )

    complete = (not candidates) or (
        not args.reducer_only
        and len(solver_rows) == len(candidates)
        and all(row["solver_result"] == "unsat" for row in solver_rows)
    )
    closed = bool(complete and not survivors)
    report: dict[str, Any] = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": 6,
            "genus": args.genus,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "candidate_timeout_seconds": CANDIDATE_TIMEOUT_SECONDS,
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
        "reducer_only": args.reducer_only,
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
    report["canonical_sha256_without_this_field"] = canonical_sha256(report)
    (args.output_dir / "manifest.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "e": args.exceptional_mass,
                "a": args.curve_group_mass,
                "candidate_count": len(candidates),
                "closed": report["parent_exactly_closed"],
                "survivors": len(survivors),
                "elapsed": report["elapsed_seconds"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
