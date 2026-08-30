#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction

import sympy
from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from direct_picard_slice_quadratic_bound import DirectPicardSliceQuadraticBound

EXPECTED_SMITH_DIAGONAL = (1, 2, 2)
EXPECTED_GENERATOR_ORDERS = (20, 20, 40)
EXPECTED_RELEVANT_SUBGROUP_ORDER = 640
EXPECTED_INTEGRAL_COSET_DIAGNOSTIC_SHA256 = "25d2b425177594664abd5f5fec03fc37bb5d6751ce1fb6c2fd9d4ba376633387"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def as_fraction(value: sympy.Expr) -> Fraction:
    return Fraction(int(sympy.numer(value)), int(sympy.denom(value)))


def generator_order(column: Matrix) -> int:
    out = 1
    for value in column:
        out = math.lcm(out, int(sympy.denom(value)))
    return out


@dataclass(frozen=True)
class DirectPicardIntegralCosetLowerBound:
    bound: DirectPicardSliceQuadraticBound
    smith_diagonal: tuple[int, int, int]
    smith_left: tuple[tuple[int, int, int], ...]
    generator_orders: tuple[int, int, int]
    common_denominator: int
    residue_to_class: dict[tuple[int, int, int], int]
    class_lower_bounds: tuple[Fraction, ...]
    certificate: dict

    def smith_u(self, d: int, e: int, a: int) -> tuple[int, int, int]:
        target = (int(d), int(e), int(a))
        out = []
        for i in range(3):
            numerator = sum(self.smith_left[i][j] * target[j] for j in range(3))
            divisor = self.smith_diagonal[i]
            if numerator % divisor:
                raise ValueError(f"target is outside direct-slice image: {(d, e, a)}")
            out.append(numerator // divisor)
        return tuple(out)  # type: ignore[return-value]

    def class_id(self, d: int, e: int, a: int) -> int:
        u = self.smith_u(d, e, a)
        residue = tuple(u[i] % self.generator_orders[i] for i in range(3))
        return self.residue_to_class[residue]  # type: ignore[index]

    def class_lower_bound(self, d: int, e: int, a: int) -> Fraction:
        return self.class_lower_bounds[self.class_id(d, e, a)]

    def can_reach_selfsq_after_integrality_lb(self, d: int, e: int, a: int, lower: int) -> bool:
        slack_numerator = (
            self.bound.max_selfsq_numerator(d, e, a)
            - int(lower) * self.bound.dual_denominator
        )
        if slack_numerator < 0:
            return False
        lb = self.class_lower_bound(d, e, a)
        # continuous_max - true_integrality_penalty is at most
        # continuous_max - lb.  Keep the slice only if that safe upper bound
        # can still reach the required self-intersection.
        return slack_numerator * lb.denominator >= self.bound.dual_denominator * lb.numerator

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "DirectPicardIntegralCosetLowerBound":
        bound = DirectPicardSliceQuadraticBound.from_retained(marking, bundle)
        bridge = bound.bridge
        gram = Matrix(bundle["picard_gram_64x64"])
        phi = Matrix([
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ])

        phi_dm = DomainMatrix.from_Matrix(phi).convert_to(ZZ)
        D_dm, S_dm, T_dm = smith_normal_decomp(phi_dm)
        if S_dm * phi_dm * T_dm != D_dm:
            raise ValueError("Smith decomposition reconstruction regression")
        D = D_dm.to_Matrix()
        S = S_dm.to_Matrix()
        T = T_dm.to_Matrix()
        diagonal = tuple(int(D[i, i]) for i in range(3))
        if diagonal != EXPECTED_SMITH_DIAGONAL:
            raise ValueError(f"direct-slice Smith diagonal drift: {diagonal}")

        transformed = T.T * gram * T
        C = transformed[:3, 3:]
        B = -transformed[3:, 3:]
        if B.shape != (61, 61) or B != B.T:
            raise ValueError("slice-kernel positive Gram regression")

        # We only need B^{-1}C^T and diag(B^{-1}); no closest-vector search is
        # performed here.  For y=v-v* and any coordinate i,
        #   y_i^2 <= (y^T B y) * (B^{-1})_ii
        # by exact Cauchy-Schwarz.  Since v is integral, the fractional part of
        # v*_i therefore gives a rigorous lower bound on the integrality loss.
        B_inv = B.inv()
        Y = B_inv * C.T
        orders = tuple(generator_order(Y[:, j]) for j in range(3))
        if orders != EXPECTED_GENERATOR_ORDERS:
            raise ValueError(f"integral-shift generator-order drift: {orders}")

        common_den = 1
        for value in Y:
            common_den = math.lcm(common_den, int(sympy.denom(value)))
        scaled = Y * common_den
        if any(sympy.denom(value) != 1 for value in scaled):
            raise ValueError("integral-shift common-denominator scaling regression")
        R = Matrix([[int(scaled[i, j]) for j in range(3)] for i in range(61)])

        def class_key(residue: tuple[int, int, int]) -> tuple[int, ...]:
            return tuple(
                sum(R[i, j] * residue[j] for j in range(3)) % common_den
                for i in range(61)
            )

        residue_keys: dict[tuple[int, int, int], tuple[int, ...]] = {}
        unique_keys: set[tuple[int, ...]] = set()
        for residue in itertools.product(*(range(v) for v in orders)):
            r = tuple(int(v) for v in residue)
            key = class_key(r)
            residue_keys[r] = key
            unique_keys.add(key)
        sorted_keys = sorted(unique_keys)
        if len(sorted_keys) != EXPECTED_RELEVANT_SUBGROUP_ORDER:
            raise ValueError(
                f"reachable integral-shift subgroup drift: {len(sorted_keys)} != {EXPECTED_RELEVANT_SUBGROUP_ORDER}"
            )
        key_to_class = {key: i for i, key in enumerate(sorted_keys)}
        residue_to_class = {r: key_to_class[key] for r, key in residue_keys.items()}

        inverse_diagonal = [as_fraction(B_inv[i, i]) for i in range(61)]
        if any(v <= 0 for v in inverse_diagonal):
            raise ValueError("slice-kernel inverse diagonal is not positive")
        lower_bounds: list[Fraction] = []
        table_for_hash = []
        for class_id, key in enumerate(sorted_keys):
            lb = Fraction(0, 1)
            for i, residue in enumerate(key):
                distance = Fraction(min(residue, common_den - residue), common_den)
                candidate = distance * distance / inverse_diagonal[i]
                if candidate > lb:
                    lb = candidate
            lower_bounds.append(lb)
            table_for_hash.append({
                "class_id": class_id,
                "key": list(key),
                "lower_bound": [lb.numerator, lb.denominator],
            })

        zero_count = sum(1 for value in lower_bounds if value == 0)
        if zero_count != 1:
            raise ValueError(f"expected one zero shift class, got {zero_count}")
        positive = [value for value in lower_bounds if value > 0]
        min_positive = min(positive)
        max_lower = max(positive)

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_INTEGRAL_COSET_LOWER_BOUND_V1",
            "mode": "EXACT_COORDINATE_CAUCHY_LOWER_BOUND_ON_FINITE_INTEGRALITY_LOSS_CLASSES",
            "quadratic_certificate_sha256": bound.certificate["canonical_sha256_without_this_field"],
            "integral_coset_diagnostic_sha256": EXPECTED_INTEGRAL_COSET_DIAGNOSTIC_SHA256,
            "smith_diagonal": list(diagonal),
            "generator_orders": list(orders),
            "common_fractional_denominator": common_den,
            "residue_box_size": math.prod(orders),
            "reachable_class_count": len(sorted_keys),
            "zero_class_count": zero_count,
            "positive_lower_bound_class_count": len(positive),
            "distinct_lower_bound_count": len(set(lower_bounds)),
            "minimum_positive_lower_bound": [min_positive.numerator, min_positive.denominator],
            "maximum_coordinate_lower_bound": [max_lower.numerator, max_lower.denominator],
            "class_table_sha256": csha(table_for_hash),
            "proof": {
                "identity": "v*=B^-1*C^T*u and delta([u])=min_{v in Z^61}(v-v*)^T*B*(v-v*)",
                "coordinate_inequality": "(v_i-v*_i)^2 <= delta*(B^-1)_ii",
                "safe_class_lower_bound": "max_i dist(v*_i,Z)^2/(B^-1)_ii <= delta",
                "closest_vector_search_run": False,
                "all_2018569_prior_slices_share_only_640_reachable_classes": True,
            },
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            bound=bound,
            smith_diagonal=diagonal,
            smith_left=tuple(tuple(int(S[i, j]) for j in range(3)) for i in range(3)),
            generator_orders=orders,
            common_denominator=common_den,
            residue_to_class=residue_to_class,
            class_lower_bounds=tuple(lower_bounds),
            certificate=cert,
        )
