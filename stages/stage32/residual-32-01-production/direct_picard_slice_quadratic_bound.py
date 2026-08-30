#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction

import sympy
from sympy import Matrix

from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import _parse_hperp


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def rational_matrix_payload(m: Matrix) -> dict:
    den = 1
    for v in m:
        den = math.lcm(den, int(sympy.denom(v)))
    scaled = m * den
    assert all(sympy.denom(v) == 1 for v in scaled)
    return {
        "denominator": den,
        "integer_matrix": [[int(scaled[i, j]) for j in range(m.cols)] for i in range(m.rows)],
    }


@dataclass(frozen=True)
class DirectPicardSliceQuadraticBound:
    bridge: DirectPicardSliceBridge
    dual_denominator: int
    dual_integer_matrix: tuple[tuple[int, int, int], ...]
    certificate: dict

    def max_selfsq_numerator(self, d: int, e: int, a: int) -> int:
        t = (int(d), int(e), int(a))
        R = self.dual_integer_matrix
        return sum(t[i] * R[i][j] * t[j] for i in range(3) for j in range(3))

    def can_reach_selfsq(self, d: int, e: int, a: int, lower: int) -> bool:
        return self.max_selfsq_numerator(d, e, a) >= int(lower) * self.dual_denominator

    def feasible_a_interval(self, d: int, e: int, upper: int, lower: int) -> tuple[int, int] | None:
        """Exact integer interval where the continuous slice maximum reaches lower.

        For fixed d,e the maximum self-intersection is a concave quadratic in a.
        The a^2 coefficient is certified negative, so the feasible integer set is
        empty or one contiguous interval.  Binary searches use integer-scaled exact
        arithmetic only.
        """
        R = self.dual_integer_matrix
        A = R[2][2]
        B = 2 * (R[0][2] * int(d) + R[1][2] * int(e))
        C = (
            R[0][0] * int(d) * int(d)
            + 2 * R[0][1] * int(d) * int(e)
            + R[1][1] * int(e) * int(e)
            - int(lower) * self.dual_denominator
        )
        if A >= 0:
            raise ValueError("expected strictly concave a-quadratic")

        def f(x: int) -> int:
            return A * x * x + B * x + C

        n = int(upper)
        if n < 0:
            return None
        # Exact vertex candidates.  Fraction avoids floating-point boundary risk.
        vertex = Fraction(-B, 2 * A)
        vf = vertex.numerator // vertex.denominator
        candidates = {0, n, max(0, min(n, vf)), max(0, min(n, vf + 1))}
        peak = max(candidates, key=lambda x: (f(x), -x))
        if f(peak) < 0:
            return None

        if f(0) >= 0:
            lo = 0
        else:
            left, right = 0, peak
            while left + 1 < right:
                mid = (left + right) // 2
                if f(mid) >= 0:
                    right = mid
                else:
                    left = mid
            lo = right

        if f(n) >= 0:
            hi = n
        else:
            left, right = peak, n
            while left + 1 < right:
                mid = (left + right) // 2
                if f(mid) >= 0:
                    left = mid
                else:
                    right = mid
            hi = left
        if lo > hi:
            return None
        return lo, hi

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "DirectPicardSliceQuadraticBound":
        bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
        gram = Matrix(bundle["picard_gram_64x64"])
        phi = Matrix([
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ])
        A = phi * gram.inv() * phi.T
        if A.shape != (3, 3) or A.det() == 0:
            raise ValueError("slice dual Gram is singular")
        dual = A.inv()
        payload = rational_matrix_payload(dual)
        den = int(payload["denominator"])
        R = tuple(tuple(int(v) for v in row) for row in payload["integer_matrix"])
        if R[2][2] >= 0:
            raise ValueError("fixed-(d,e) self-square upper bound is not concave in a")

        # The retained Hperp Q is the exact positive-definite form on the degree
        # kernel.  Exact SymPy definiteness is checked here because using the
        # stationary value as an upper bound requires negativity on ker(degree).
        hperp_text = marking.get("hperp_text")
        if not isinstance(hperp_text, str):
            raise ValueError("retained marking missing hperp_text")
        q, _, _, _, hmeta = _parse_hperp(hperp_text)
        hperp_positive = q.is_positive_definite
        if hperp_positive is not True:
            raise ValueError(f"retained Hperp exact positive-definiteness not certified: {hperp_positive}")

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_SLICE_QUADRATIC_BOUND_V1",
            "mode": "EXACT_CONTINUOUS_MAX_SELF_INTERSECTION_ON_D_E_A_AFFINE_SLICE",
            "bridge_certificate_sha256": bridge.certificate["canonical_sha256_without_this_field"],
            "hperp_text_sha256": hmeta["hperp_text_sha256"],
            "hperp_positive_definite_exact": True,
            "slice_kernel_negative_definite_exact": True,
            "dual_target_gram": payload,
            "a_squared_integer_coefficient": R[2][2],
            "a_quadratic_strictly_concave": True,
            "upper_bound_formula": "max(C^2 | phi(C)=t over Picard_R) = t^T*(phi*G^-1*phi^T)^-1*t",
            "safe_prune": "if continuous_max_selfsq < -d-2+2g then no integral candidate exists",
            "closevectors_not_run": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            bridge=bridge,
            dual_denominator=den,
            dual_integer_matrix=R,
            certificate=cert,
        )
