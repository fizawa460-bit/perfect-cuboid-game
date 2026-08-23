#!/usr/bin/env python3
"""Discover nonnegative dual certificates numerically, then verify them exactly.

SciPy/HiGHS is only a candidate finder. A row receives certificate credit only
if the rationalized relation is checked coordinate-by-coordinate over Z.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
import pathlib
from typing import Any

import numpy as np
from scipy.optimize import linprog

from cap_certificate import CERT_SCHEMA, canonical_sha256, load_core, verify_certificate


def derive(core: dict[str, Any]) -> dict[str, Any]:
    known_int = core["known_classes"]
    hyperplane_int = core["hyperplane"]
    matrix = np.array(known_int, dtype=float).T
    hyperplane = np.array(hyperplane_int, dtype=float)
    rows: list[dict[str, Any]] = []

    for target in range(140):
        multiplier = 2 if target < 92 else 4
        rhs = hyperplane - multiplier * np.array(known_int[target], dtype=float)
        bounds = [(0.0, None)] * 140
        bounds[target] = (0.0, 0.0)
        result = linprog(
            np.ones(140), A_eq=matrix, b_eq=rhs, bounds=bounds, method="highs"
        )
        if not result.success:
            raise SystemExit(
                f"candidate LP failed for known class {target + 1}: {result.message}"
            )

        rationals = [
            Fraction(float(value)).limit_denominator(48)
            if value > 1e-9
            else Fraction(0)
            for value in result.x
        ]
        denominator = 1
        for value in rationals:
            denominator = math.lcm(denominator, value.denominator)
        coefficients = [
            value.numerator * (denominator // value.denominator)
            for value in rationals
        ]

        lhs = [denominator * int(v) for v in hyperplane_int]
        exact_rhs = [
            multiplier * denominator * int(v) for v in known_int[target]
        ]
        for source_index, coefficient in enumerate(coefficients):
            if coefficient:
                source = known_int[source_index]
                exact_rhs = [
                    exact_rhs[k] + coefficient * int(source[k])
                    for k in range(64)
                ]
        if exact_rhs != lhs:
            raise SystemExit(
                f"exact rationalization failed for known class {target + 1}"
            )

        rows.append(
            {
                "known_index_1based": target + 1,
                "target_multiplier": multiplier,
                "denominator": denominator,
                "combination": [
                    [index + 1, int(coefficient)]
                    for index, coefficient in enumerate(coefficients)
                    if coefficient
                ],
            }
        )

    certificate: dict[str, Any] = {
        "schema": CERT_SCHEMA,
        "source_core_canonical_sha256": core[
            "canonical_sha256_without_this_field"
        ],
        "source_blob_sha1": core["source"]["git_blob_sha1"],
        "derivation": {
            "candidate_finder": "scipy.optimize.linprog(method=highs)",
            "rationalization_max_denominator": 48,
            "credit_rule": "exact coordinatewise integer identity only",
        },
        "certificates": rows,
        "receiver_credit": False,
    }
    certificate["canonical_sha256_without_this_field"] = canonical_sha256(
        certificate
    )
    verify_certificate(core, certificate)
    return certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    core = load_core(args.core)
    certificate = derive(core)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    summary = verify_certificate(core, certificate)
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
