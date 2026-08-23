#!/usr/bin/env python3
"""Stage32-05 performance-only feasibility probe for a fixed-weight MITM backend.

This program deliberately does NOT claim closure.  It source-locks the Stage32
Picard core, reconstructs the exact 64 selected-intersection coordinate map,
verifies the Smith invariant factors, and measures whether the 48 exceptional
binary variables are small enough for a fixed-Hamming-weight meet-in-the-middle
representation.

For large weight layers it uses a deterministic uniform sample only.  Sampled
pruning rates are engineering evidence, never theorem evidence.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import pathlib
import random
import time
from typing import Iterable

import numpy as np
import sympy
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

SCHEMA = "STAGE32_FIXED_WEIGHT_MITM_FEASIBILITY_V1"
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_SELECTED_DETERMINANT = 274877906944
EXPECTED_INVERSE_DENOMINATOR = 8
EXPECTED_SNF = [1] * 40 + [2] * 14 + [4] * 6 + [8] * 4


def canonical_sha256(value: object) -> str:
    blob = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(blob).hexdigest()


def matrix_list(matrix: Matrix) -> list[list[int]]:
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def build_transform(core: dict) -> dict:
    rows = Matrix(core["raw_cross_pairings_with_basis"])
    gram = Matrix(core["basis_gram"])
    selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
    determinant = int(selected.det())
    if abs(determinant) != EXPECTED_SELECTED_DETERMINANT:
        raise SystemExit(f"selected determinant mismatch: {determinant}")

    inverse = selected.inv()
    denominator = 1
    for value in inverse:
        denominator = math.lcm(denominator, int(sympy.denom(value)))
    if denominator != EXPECTED_INVERSE_DENOMINATOR:
        raise SystemExit(f"inverse denominator mismatch: {denominator}")

    inverse_integer = inverse * denominator
    if not all(sympy.denom(value) == 1 for value in inverse_integer):
        raise SystemExit("nonintegral denominator-cleared inverse")
    inverse_integer = Matrix([[int(inverse_integer[i, j]) for j in range(64)] for i in range(64)])
    if selected * inverse_integer != denominator * Matrix.eye(64):
        raise SystemExit("inverse identity failed")

    transformed_pairings = rows * inverse_integer
    if not all(sympy.denom(value) == 1 for value in transformed_pairings):
        raise SystemExit("nonintegral transformed pairings")
    transformed_pairings = Matrix(
        [[int(transformed_pairings[i, j]) for j in range(64)] for i in range(140)]
    )

    transformed_hform = Matrix(core["hyperplane"]).T * gram * inverse_integer
    hrow = [int(transformed_hform[0, j]) for j in range(64)]

    diagonal = smith_normal_form(selected, domain=ZZ)
    invariants = sorted(abs(int(diagonal[i, i])) for i in range(64))
    if invariants != EXPECTED_SNF:
        raise SystemExit(f"SNF invariant mismatch: {collections.Counter(invariants)}")

    return {
        "denominator": denominator,
        "inverse_integer": np.asarray(matrix_list(inverse_integer), dtype=np.int64),
        "pairings": np.asarray(matrix_list(transformed_pairings), dtype=np.int64),
        "hform": np.asarray(hrow, dtype=np.int64),
        "certificate": {
            "selected_rows_1based": [i + 1 for i in SELECTED_ROWS],
            "selected_matrix_determinant": determinant,
            "inverse_denominator": denominator,
            "snf_invariant_counts": {"1": 40, "2": 14, "4": 6, "8": 4},
            "selected_matrix_sha256": canonical_sha256(matrix_list(selected)),
            "inverse_integer_matrix_sha256": canonical_sha256(matrix_list(inverse_integer)),
            "transformed_pairing_matrix_sha256": canonical_sha256(matrix_list(transformed_pairings)),
            "transformed_hform_sha256": canonical_sha256(hrow),
        },
    }


def unrank_combination(n: int, k: int, rank: int) -> tuple[int, ...]:
    if k == 0:
        if rank != 0:
            raise ValueError("rank out of range")
        return ()
    out: list[int] = []
    lower = 0
    for picked in range(k):
        remaining = k - picked - 1
        for value in range(lower, n):
            count = math.comb(n - value - 1, remaining) if remaining else 1
            if rank < count:
                out.append(value)
                lower = value + 1
                break
            rank -= count
        else:
            raise ValueError("combination unrank failed")
    return tuple(out)


def sampled_combinations(n: int, k: int, limit: int, seed: int) -> tuple[list[tuple[int, ...]], bool]:
    total = math.comb(n, k)
    if total <= limit:
        import itertools
        return list(itertools.combinations(range(n), k)), True
    rng = random.Random(seed)
    ranks = sorted(rng.sample(range(total), limit))
    return [unrank_combination(n, k, rank) for rank in ranks], False


def exact_weight_bounds(coefficients: np.ndarray, weight: int) -> tuple[np.ndarray, np.ndarray]:
    """Min/max sum from selecting exactly `weight` binary columns, row-wise."""
    if weight == 0:
        zeros = np.zeros(coefficients.shape[0], dtype=np.int64)
        return zeros, zeros
    ordered = np.sort(coefficients, axis=1)
    return ordered[:, :weight].sum(axis=1), ordered[:, -weight:].sum(axis=1)


def box_bounds(coefficients: np.ndarray, upper: int) -> tuple[np.ndarray, np.ndarray]:
    low = np.minimum(0, upper * coefficients).sum(axis=1)
    high = np.maximum(0, upper * coefficients).sum(axis=1)
    return low.astype(np.int64), high.astype(np.int64)


def contribution_matrix(coefficients: np.ndarray, combos: list[tuple[int, ...]]) -> np.ndarray:
    if not combos:
        return np.empty((0, coefficients.shape[0]), dtype=np.int64)
    k = len(combos[0])
    if k == 0:
        return np.zeros((len(combos), coefficients.shape[0]), dtype=np.int64)
    indices = np.asarray(combos, dtype=np.int64)
    # coefficients: forms x 24; gather -> forms x samples x k.
    return coefficients[:, indices].sum(axis=2).T.astype(np.int64, copy=False)


def side_probe(
    *,
    side_name: str,
    side_pair: np.ndarray,
    side_inv: np.ndarray,
    side_h: np.ndarray,
    side_a: np.ndarray,
    side_n: np.ndarray,
    side_weight: int,
    completion_pair_min: np.ndarray,
    completion_pair_max: np.ndarray,
    completion_h_min: int,
    completion_h_max: int,
    completion_a_min: int,
    completion_a_max: int,
    completion_n_min: int,
    completion_n_max: int,
    denominator: int,
    degree: int,
    exceptional_mass: int,
    curve_group_mass: int,
    sample_limit: int,
    seed: int,
) -> dict:
    combos, exhaustive = sampled_combinations(24, side_weight, sample_limit, seed)
    raw_count = math.comb(24, side_weight)
    pair_contrib = contribution_matrix(side_pair, combos)
    h_contrib = contribution_matrix(side_h.reshape(1, -1), combos)[:, 0]
    a_contrib = contribution_matrix(side_a.reshape(1, -1), combos)[:, 0]
    n_contrib = contribution_matrix(side_n.reshape(1, -1), combos)[:, 0]
    inv_contrib = contribution_matrix(side_inv, combos) % denominator

    curve_cap = degree // 2
    exceptional_cap = degree // 4
    upper = np.asarray([denominator * curve_cap] * 92 + [denominator * exceptional_cap] * 48, dtype=np.int64)

    low_possible = pair_contrib + completion_pair_min
    high_possible = pair_contrib + completion_pair_max
    viable = np.all(low_possible <= upper, axis=1) & np.all(high_possible >= 0, axis=1)

    h_target = denominator * degree
    a_target = denominator * curve_group_mass
    n_target = denominator * (19 * degree - 5 * exceptional_mass)
    viable &= (h_contrib + completion_h_min <= h_target) & (h_contrib + completion_h_max >= h_target)
    viable &= (a_contrib + completion_a_min <= a_target) & (a_contrib + completion_a_max >= a_target)
    viable &= (n_contrib + completion_n_min <= n_target) & (n_contrib + completion_n_max >= n_target)

    viable_indices = np.flatnonzero(viable)
    sampled = len(combos)
    viable_sample = int(len(viable_indices))
    estimated_viable = viable_sample if exhaustive else int(round(raw_count * viable_sample / sampled))

    residue_buckets: collections.Counter[bytes] = collections.Counter()
    aggregate_buckets: collections.Counter[tuple] = collections.Counter()
    for idx in viable_indices:
        residue = np.asarray(inv_contrib[idx], dtype=np.uint8).tobytes()
        residue_buckets[residue] += 1
        aggregate_buckets[(residue, int(h_contrib[idx]), int(a_contrib[idx]), int(n_contrib[idx]))] += 1

    def stats(counter: collections.Counter) -> dict:
        if not counter:
            return {"unique": 0, "max_bucket": 0, "mean_bucket": 0.0}
        values = list(counter.values())
        return {
            "unique": len(values),
            "max_bucket": max(values),
            "mean_bucket": sum(values) / len(values),
        }

    return {
        "side": side_name,
        "weight": side_weight,
        "raw_state_count": raw_count,
        "sampled_state_count": sampled,
        "sample_is_exhaustive": exhaustive,
        "interval_viable_sample_count": viable_sample,
        "interval_viable_sample_fraction": (viable_sample / sampled) if sampled else 0.0,
        "estimated_interval_viable_full_count": estimated_viable,
        "denom8_residue_bucket_stats_on_viable_sample": stats(residue_buckets),
        "residue_plus_aggregate_bucket_stats_on_viable_sample": stats(aggregate_buckets),
    }


def scalar_weight_bounds(coeff: np.ndarray, weight: int) -> tuple[int, int]:
    lo, hi = exact_weight_bounds(coeff.reshape(1, -1), weight)
    return int(lo[0]), int(hi[0])


def scalar_box_bounds(coeff: np.ndarray, upper: int) -> tuple[int, int]:
    lo, hi = box_bounds(coeff.reshape(1, -1), upper)
    return int(lo[0]), int(hi[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    parser.add_argument("--degree", type=int, default=6)
    parser.add_argument("--genus", type=int, default=1)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--sample-limit", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=3205)
    args = parser.parse_args()

    started = time.perf_counter()
    core = json.loads(args.core.read_text(encoding="utf-8"))
    transform = build_transform(core)
    denominator = int(transform["denominator"])
    pair = transform["pairings"]
    inv = transform["inverse_integer"]
    h = transform["hform"]

    # Selected intersection coordinates are [48 exceptionals | 16 normals].
    left = slice(0, 24)
    right = slice(24, 48)
    quat = slice(48, 64)
    q_upper = args.degree // 2

    arow = pair[:46].sum(axis=0)
    nrow = pair[:92].sum(axis=0)

    q_pair_min, q_pair_max = box_bounds(pair[:, quat], q_upper)
    q_h_min, q_h_max = scalar_box_bounds(h[quat], q_upper)
    q_a_min, q_a_max = scalar_box_bounds(arow[quat], q_upper)
    q_n_min, q_n_max = scalar_box_bounds(nrow[quat], q_upper)

    layers: list[dict] = []
    e = args.exceptional_mass
    for left_weight in range(max(0, e - 24), min(24, e) + 1):
        right_weight = e - left_weight

        r_pair_min, r_pair_max = exact_weight_bounds(pair[:, right], right_weight)
        r_h_min, r_h_max = scalar_weight_bounds(h[right], right_weight)
        r_a_min, r_a_max = scalar_weight_bounds(arow[right], right_weight)
        r_n_min, r_n_max = scalar_weight_bounds(nrow[right], right_weight)
        left_result = side_probe(
            side_name="left24",
            side_pair=pair[:, left], side_inv=inv[:, left], side_h=h[left], side_a=arow[left], side_n=nrow[left],
            side_weight=left_weight,
            completion_pair_min=r_pair_min + q_pair_min,
            completion_pair_max=r_pair_max + q_pair_max,
            completion_h_min=r_h_min + q_h_min, completion_h_max=r_h_max + q_h_max,
            completion_a_min=r_a_min + q_a_min, completion_a_max=r_a_max + q_a_max,
            completion_n_min=r_n_min + q_n_min, completion_n_max=r_n_max + q_n_max,
            denominator=denominator, degree=args.degree, exceptional_mass=e, curve_group_mass=args.curve_group_mass,
            sample_limit=args.sample_limit, seed=args.seed + 1000 * left_weight + right_weight,
        )

        l_pair_min, l_pair_max = exact_weight_bounds(pair[:, left], left_weight)
        l_h_min, l_h_max = scalar_weight_bounds(h[left], left_weight)
        l_a_min, l_a_max = scalar_weight_bounds(arow[left], left_weight)
        l_n_min, l_n_max = scalar_weight_bounds(nrow[left], left_weight)
        right_result = side_probe(
            side_name="right24",
            side_pair=pair[:, right], side_inv=inv[:, right], side_h=h[right], side_a=arow[right], side_n=nrow[right],
            side_weight=right_weight,
            completion_pair_min=l_pair_min + q_pair_min,
            completion_pair_max=l_pair_max + q_pair_max,
            completion_h_min=l_h_min + q_h_min, completion_h_max=l_h_max + q_h_max,
            completion_a_min=l_a_min + q_a_min, completion_a_max=l_a_max + q_a_max,
            completion_n_min=l_n_min + q_n_min, completion_n_max=l_n_max + q_n_max,
            denominator=denominator, degree=args.degree, exceptional_mass=e, curve_group_mass=args.curve_group_mass,
            sample_limit=args.sample_limit, seed=args.seed + 2000 * right_weight + left_weight,
        )
        layers.append({"left_weight": left_weight, "right_weight": right_weight, "left": left_result, "right": right_result})

    raw_left_all_layers = sum(math.comb(24, j) for j in range(max(0, e - 24), min(24, e) + 1))
    estimated_viable_left = sum(item["left"]["estimated_interval_viable_full_count"] for item in layers)
    estimated_viable_right = sum(item["right"]["estimated_interval_viable_full_count"] for item in layers)

    report = {
        "schema": SCHEMA,
        "purpose": "performance feasibility only",
        "theorem_credit": False,
        "receiver_credit": False,
        "unsat_claim": False,
        "low_degree_prefix_complete": False,
        "full_d176_d192_numerical_orbit_census": False,
        "parameters": {
            "degree": args.degree,
            "genus": args.genus,
            "exceptional_mass": e,
            "curve_group_mass": args.curve_group_mass,
            "sample_limit_per_weight_layer": args.sample_limit,
            "seed": args.seed,
        },
        "transform_certificate": transform["certificate"],
        "architecture": {
            "exceptional_split": "24+24 fixed-Hamming-weight layers; all weight splits are covered in accounting",
            "quaternary_side": "16 selected nonexceptional coordinates in [0,3]; represented only by exact box completion bounds in this feasibility probe",
            "lattice_image_signature": "64 exact denominator-8 congruence residues; SNF invariants independently checked as 1^40,2^14,4^6,8^4",
            "linear_pruning": "all 140 transformed pairing intervals plus exact degree, first-46 mass, and total-nonexceptional mass interval completion tests",
            "quadratic_constraint": "not used in this feasibility probe",
        },
        "all_weight_split_layers": layers,
        "summary": {
            "raw_left_layer_state_sum": raw_left_all_layers,
            "estimated_interval_viable_left_state_sum": estimated_viable_left,
            "estimated_interval_viable_right_state_sum": estimated_viable_right,
            "compact_record_bytes_assumption": 40,
            "estimated_compact_left_memory_bytes": 40 * estimated_viable_left,
            "estimated_compact_right_memory_bytes": 40 * estimated_viable_right,
        },
        "elapsed_seconds": time.perf_counter() - started,
    }
    report["canonical_sha256_without_this_field"] = canonical_sha256(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "schema": SCHEMA,
        "e": e,
        "a": args.curve_group_mass,
        "layers": len(layers),
        "raw_left_layer_state_sum": raw_left_all_layers,
        "estimated_interval_viable_left_state_sum": estimated_viable_left,
        "estimated_interval_viable_right_state_sum": estimated_viable_right,
        "elapsed_seconds": report["elapsed_seconds"],
        "theorem_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
