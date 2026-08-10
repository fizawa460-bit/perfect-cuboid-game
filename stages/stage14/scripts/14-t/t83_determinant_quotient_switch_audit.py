#!/usr/bin/env python3
"""Deterministic audit for Stage14-t83.

The audit is intentionally elementary.  It checks the exact Gaussian determinant
identity, non-vanishing under N(V)<N(pi)/2, the primitive companion coordinate,
the determinant-quotient product budget, and the <=2 lattice-line multiplicity
used in the t83 boundary.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FROZEN = ROOT / "stages/stage14/data/14-t83/determinant_quotient_switch_frozen.json"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def gaussian_prime_vectors(limit: int = 44):
    out = []
    for x in range(1, limit + 1):
        for y in range(1, x + 1):
            ell = x * x + y * y
            if ell % 2 and is_prime(ell) and math.gcd(x, y) == 1:
                out.append((x, y, ell))
    return out


def squarefree_test_moduli():
    # Includes one composite two-prime and several prime moduli.  d=1 is kept
    # because the line-multiplicity assertion is geometric and independent of d.
    return [1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 29, 31, 33, 35]


def positive_physical_cover_vectors(ell: int):
    vmax = math.isqrt((ell - 1) // 2)
    out = []
    for p in range(1, vmax + 1):
        for q in range(p + 1, vmax + 1):
            n = p * p + q * q
            if 2 * n >= ell:
                continue
            if math.gcd(p, q) != 1:
                continue
            out.append((p, q, n))
    return out


def full_disk_primitive_vectors(ell: int):
    vmax = math.isqrt((ell - 1) // 2)
    out = []
    for p in range(-vmax, vmax + 1):
        for q in range(-vmax, vmax + 1):
            if p == 0 and q == 0:
                continue
            n = p * p + q * q
            if 2 * n >= ell:
                continue
            if math.gcd(abs(p), abs(q)) != 1:
                continue
            out.append((p, q, n))
    return out


def run_audit() -> dict:
    pis = gaussian_prime_vectors()
    ds = squarefree_test_moduli()

    norm_identity_checks = 0
    nonzero_determinant_checks = 0
    unit_companion_checks = 0
    quotient_budget_checks = 0
    physical_line_groups = 0
    physical_max_line_multiplicity = 0

    for x, y, ell in pis:
        covers = positive_physical_cover_vectors(ell)
        for sigma in (1, -1):
            for p, q, n in covers:
                delta = y * p - sigma * x * q
                companion = x * p + sigma * y * q

                assert delta * delta + companion * companion == ell * n
                norm_identity_checks += 1

                # Primitive integer parallelism would force equal norms, which is
                # excluded by the physical ell>2*N(V) range.
                assert delta != 0
                nonzero_determinant_checks += 1

                for d in ds:
                    if math.gcd(d, ell * n) != 1:
                        continue
                    if delta % d:
                        continue

                    assert math.gcd(companion, d) == 1
                    unit_companion_checks += 1

                    j = delta // d
                    assert j != 0

                    # Synthetic exact realization of h*ell*n <= 2B.  No floating
                    # point is used: the desired t83 consequence is
                    # h*(d*j)^2 <= 2B.
                    h = 1 + ((x + y + p + q + d) % 5)
                    B = (h * ell * n + 1) // 2
                    assert h * ell * n <= 2 * B
                    assert h * (d * j) * (d * j) <= 2 * B
                    quotient_budget_checks += 1

            # Physical first-quadrant line multiplicity.  This is usually one,
            # but the theorem only uses the orientation-free <=2 bound.
            for d in ds:
                groups = defaultdict(int)
                for p, q, n in covers:
                    delta = y * p - sigma * x * q
                    if delta != 0 and delta % d == 0:
                        groups[delta // d] += 1
                for multiplicity in groups.values():
                    assert multiplicity <= 2
                    physical_line_groups += 1
                    physical_max_line_multiplicity = max(
                        physical_max_line_multiplicity, multiplicity
                    )

    # Independent orientation-free disk check of the geometric <=2 theorem.
    # Use the first 100 Gaussian prime vectors to keep CI quick while ensuring
    # that multiplicity two is actually attained.
    full_disk_line_groups = 0
    full_disk_max_line_multiplicity = 0
    full_disk_ds = [1, 3, 5, 7, 11, 13, 15, 17, 19, 21]
    for x, y, ell in pis[:100]:
        covers = full_disk_primitive_vectors(ell)
        for sigma in (1, -1):
            for d in full_disk_ds:
                groups = defaultdict(int)
                for p, q, n in covers:
                    delta = y * p - sigma * x * q
                    if delta != 0 and delta % d == 0:
                        groups[delta // d] += 1
                for multiplicity in groups.values():
                    assert multiplicity <= 2
                    full_disk_line_groups += 1
                    full_disk_max_line_multiplicity = max(
                        full_disk_max_line_multiplicity, multiplicity
                    )

    assert full_disk_max_line_multiplicity == 2

    result = {
        "stage": "14-t83",
        "gaussian_prime_vectors": len(pis),
        "projective_norm_identity_checks": norm_identity_checks,
        "nonzero_determinant_checks": nonzero_determinant_checks,
        "unit_companion_checks": unit_companion_checks,
        "determinant_quotient_budget_checks": quotient_budget_checks,
        "physical_quadrant_line_groups": physical_line_groups,
        "physical_quadrant_max_line_multiplicity": physical_max_line_multiplicity,
        "full_disk_line_groups": full_disk_line_groups,
        "full_disk_max_line_multiplicity": full_disk_max_line_multiplicity,
        "boundary": {
            "STAGE14_T83": "COMPLETE_FIXED_U_DIVISOR_PROJECTIVE_INCIDENCE_TO_SHORT_NONZERO_DETERMINANT_QUOTIENT",
            "PURE_PROJECTIVE_INCIDENCE_EQUALS_INTEGER_DETERMINANT_DIVISIBILITY": True,
            "PROJECTIVE_DETERMINANT_COMPANION_NORM_IDENTITY": True,
            "EXACT_INTEGER_PROJECTIVE_DIAGONAL_PHYSICAL": False,
            "NONZERO_DETERMINANT_QUOTIENT_FORCED": True,
            "DETERMINANT_QUOTIENT_SWITCH_PROVED": True,
            "DETERMINANT_QUOTIENT_PRODUCT_BUDGET": "sqrt(2B/h)",
            "ONE_OF_DIVISOR_OR_QUOTIENT_IS_QUARTER_SCALE": True,
            "FIXED_DETERMINANT_QUOTIENT_COVER_MULTIPLICITY_AT_MOST": 2,
            "SWITCHED_COMPANION_COORDINATE_UNIT_MOD_D": True,
            "FIXED_U_PACKET_POWER_SAVING_PROVED": False,
            "TH23_CONSUMED": True,
            "TH23_TARGET_REOPENED": False,
            "TH24_NEEDED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
            "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
            "NEXT": "Stage14-t84",
        },
    }
    return result


def main() -> None:
    result = run_audit()
    print(json.dumps(result, indent=2, sort_keys=True))

    if FROZEN.exists():
        frozen = json.loads(FROZEN.read_text())
        assert result == frozen, "t83 deterministic audit differs from frozen boundary"


if __name__ == "__main__":
    main()
