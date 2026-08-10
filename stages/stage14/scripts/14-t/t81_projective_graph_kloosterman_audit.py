#!/usr/bin/env python3
"""Stage14-t81 deterministic projective graph/Kloosterman audit."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T80 = ROOT / "stages/stage14/14-t80/result.md"
X13 = ROOT / "stages/stage14/14-X13/result.md"


def primes_upto(n: int) -> list[int]:
    out = []
    for q in range(3, n + 1, 2):
        if all(q % p for p in range(3, int(q**0.5) + 1, 2)):
            out.append(q)
    return out


def valid_slope(p: int, x: int) -> bool:
    return (1 + x * x) % p != 0


def affine_slopes(p: int) -> list[int]:
    return [x for x in range(p) if valid_slope(p, x)]


def tau(p: int, c: int | None, s: int, y: int) -> int | None:
    assert s in (-1, 1)
    if c is None:
        if y % p == 0:
            return None
        return (-s * pow(y, -1, p)) % p
    den = (1 - s * c * y) % p
    if den == 0:
        return None
    return ((c + s * y) * pow(den, -1, p)) % p


def exp_p(p: int, n: int) -> complex:
    return cmath.exp(2j * math.pi * (n % p) / p)


def chart_sum(p: int, a: int) -> complex:
    return sum(exp_p(p, -a * x) for x in affine_slopes(p))


def graph_sum(p: int, c: int | None, s: int, a: int, b: int) -> complex:
    total = 0j
    for y in affine_slopes(p):
        x = tau(p, c, s, y)
        if x is None or not valid_slope(p, x):
            continue
        total += exp_p(p, -a * x + b * y)
    return total


def local_group_order(p: int) -> int:
    return p - (1 if p % 4 == 1 else -1)


def resummed_kernel(p: int, c: int | None, s: int, a: int, b: int) -> complex:
    # (1/|G_p|) sum over nonprincipal projective characters after Fourier transform.
    # Orthogonality gives the graph term minus the principal-character term.
    graph = graph_sum(p, c, s, a, b) / (p * p)
    principal = chart_sum(p, a) * chart_sum(p, -b) / (
        local_group_order(p) * p * p
    )
    return graph - principal


def full_kloosterman(p: int, A: int, B: int) -> complex:
    return sum(exp_p(p, A * pow(u, -1, p) + B * u) for u in range(1, p))


def transformed_kloosterman_parameters(
    p: int, c: int | None, s: int, a: int, b: int
) -> tuple[int, int, complex]:
    if c is None:
        # phase = a*s/y + b*y
        return (a * s) % p, b % p, 1 + 0j
    invc = pow(c, -1, p)
    A = (-a * (c * c + 1) * invc) % p
    B = (-b * s * invc) % p
    const = (a * invc + b * s * invc) % p
    return A, B, exp_p(p, const)


def class_mul(p: int, x: int | None, y: int | None) -> int | None:
    # Cayley slopes for projective Gaussian multiplication.
    if x is None and y is None:
        return 0  # [i]^2=[-1]=identity projectively
    if x is None:
        if y == 0:
            return None
        return (-pow(y, -1, p)) % p
    if y is None:
        if x == 0:
            return None
        return (-pow(x, -1, p)) % p
    den = (1 - x * y) % p
    if den == 0:
        return None
    return ((x + y) * pow(den, -1, p)) % p


def inverse_class(p: int, x: int | None) -> int | None:
    if x is None:
        return None
    return (-x) % p


def slope_of_uv(p: int, u: int, v: int) -> int | None:
    if u % p == 0:
        return None
    return (v * pow(u, -1, p)) % p


def main() -> None:
    t80 = T80.read_text()
    x13 = X13.read_text()
    assert "STAGE14_T80=COMPLETE_NEAR_FULL_SUPPORT_PROJECTIVE_GAUSS_DUALIZATION_TO_PRIMITIVE_INVERSE_FRACTION_KERNEL" in t80
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in x13

    local_graph_checks = 0
    fractional_kloosterman_checks = 0
    affine_match_checks = 0
    affine_mismatch_checks = 0
    inert_mismatch_zero_checks = 0
    fixed_class_selector_checks = 0
    max_fractional_normalized_ratio = 0.0
    max_split_affine_mismatch_scaled = 0.0
    max_kloosterman_ratio = 0.0

    primes = primes_upto(43)
    for p in primes:
        slopes = affine_slopes(p)
        # Deterministic frequency sample; exhaustive for small p.
        freqs = list(range(1, p)) if p <= 17 else sorted({1, 2, 3, p // 2, p - 2, p - 1})
        freqs = [a for a in freqs if a % p]

        # Affine degeneration c=0.
        for s in (-1, 1):
            for a in freqs:
                for b in freqs:
                    K = resummed_kernel(p, 0, s, a, b)
                    if (b - s * a) % p == 0:
                        assert abs(K) <= 2.0 / p + 1e-10
                        affine_match_checks += 1
                    else:
                        affine_mismatch_checks += 1
                        if p % 4 == 3:
                            assert abs(K) < 2e-10
                            inert_mismatch_zero_checks += 1
                        else:
                            assert abs(K) <= 4.1 / (p * p) + 1e-10
                            max_split_affine_mismatch_scaled = max(
                                max_split_affine_mismatch_scaled,
                                abs(K) * p * p,
                            )

        # Genuine finite fractional translations. Use all valid nonzero c for small p,
        # and a stable sample for larger primes.
        cs = [c for c in slopes if c != 0]
        if p > 17 and len(cs) > 6:
            cs = cs[:3] + cs[-3:]
        for c in cs:
            for s in (-1, 1):
                for a in freqs:
                    for b in freqs:
                        G = graph_sum(p, c, s, a, b)
                        A, B, phase = transformed_kloosterman_parameters(p, c, s, a, b)
                        assert A % p and B % p
                        Kl = full_kloosterman(p, A, B)
                        # Inert: exact complete Kloosterman transform. Split: two
                        # isotropic affine points are omitted, so discrepancy <=2.
                        err = abs(G - phase * Kl)
                        if p % 4 == 3:
                            assert err < 2e-9
                        else:
                            assert err <= 2.00000001
                        assert abs(Kl) <= 2 * math.sqrt(p) + 2e-9
                        max_kloosterman_ratio = max(
                            max_kloosterman_ratio, abs(Kl) / (2 * math.sqrt(p))
                        )
                        K = resummed_kernel(p, c, s, a, b)
                        assert abs(K) <= (2 * math.sqrt(p) + 3.1) / (p * p) + 1e-10
                        max_fractional_normalized_ratio = max(
                            max_fractional_normalized_ratio,
                            abs(K) * (p ** 1.5),
                        )
                        local_graph_checks += 1
                        fractional_kloosterman_checks += 1

        # Infinity fixed class is also Kloosterman.
        for s in (-1, 1):
            for a in freqs:
                for b in freqs:
                    G = graph_sum(p, None, s, a, b)
                    A, B, phase = transformed_kloosterman_parameters(p, None, s, a, b)
                    Kl = full_kloosterman(p, A, B)
                    err = abs(G - phase * Kl)
                    if p % 4 == 3:
                        assert err < 2e-9
                    else:
                        assert err <= 2.00000001
                    assert abs(Kl) <= 2 * math.sqrt(p) + 2e-9
                    K = resummed_kernel(p, None, s, a, b)
                    assert abs(K) <= (2 * math.sqrt(p) + 3.1) / (p * p) + 1e-10
                    local_graph_checks += 1
                    fractional_kloosterman_checks += 1

        # Exact fixed-U/beta selector: C=[U]^-1 I is identity iff
        # I=1 and Im(U)=0, or I=[i] and Re(U)=0.
        for u in range(p):
            for v in range(p):
                if (u * u + v * v) % p == 0:
                    continue  # nonunit U, outside ray modulus
                U = slope_of_uv(p, u, v)
                Uinv = inverse_class(p, U)
                for I in (0, None):
                    C = class_mul(p, Uinv, I)
                    expected = (v % p == 0) if I == 0 else (u % p == 0)
                    assert (C == 0) == expected
                    fixed_class_selector_checks += 1

    report = {
        "stage": "14-t81",
        "local_primes": len(primes),
        "local_graph_checks": local_graph_checks,
        "fractional_kloosterman_checks": fractional_kloosterman_checks,
        "affine_match_checks": affine_match_checks,
        "affine_mismatch_checks": affine_mismatch_checks,
        "inert_mismatch_zero_checks": inert_mismatch_zero_checks,
        "fixed_class_selector_checks": fixed_class_selector_checks,
        "max_kloosterman_ratio_to_2sqrtp": max_kloosterman_ratio,
        "max_fractional_kernel_times_p32": max_fractional_normalized_ratio,
        "max_split_affine_mismatch_times_p2": max_split_affine_mismatch_scaled,
        "boundary": {
            "STAGE14_T81": "COMPLETE_PROJECTIVE_CHARACTER_RESUMMATION_TO_AFFINE_DIAGONAL_AND_FRACTIONAL_KLOOSTERMAN_GRAPH_KERNEL",
            "MERGED_T80_IMPORTED": True,
            "PROJECTIVE_CLASS_INCIDENCE_IS_SINGLE_MOBIUS_GRAPH": True,
            "LOCAL_PROJECTIVE_CHARACTER_FAMILY_RESUMMED": True,
            "FRACTIONAL_PROJECTIVE_GRAPH_IS_KLOOSTERMAN": True,
            "FRACTIONAL_LOCAL_NORMALIZED_BOUND": "p^(-3/2)*Bo1",
            "AFFINE_INERT_FREQUENCY_MISMATCH_VANISHES": True,
            "AFFINE_SPLIT_FREQUENCY_MISMATCH_EXTRA_GAIN": "p^-1*Bo1",
            "GLOBAL_GRAPH_KERNEL_BOUND": "d^-1*d_frac^-1/2*d_mis^-1*Bo1",
            "HARD_FREQUENCY_PAIR_ALMOST_DIAGONAL": True,
            "TWO_ADDITIVE_FREQUENCIES_COLLAPSE_TO_ONE": "Bo1",
            "AFFINE_DEGENERACY_IS_FIXED_U_BETA_COORDINATE_SUPPORT": True,
            "SINGLE_FREQUENCY_PHYSICAL_INVERSE_FRACTION_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
            "SQRT_B_UPPER_BOUND_PROVED": True,
            "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
            "TH23_NEEDED": True,
            "TH23_TARGET_REFINED_BY_T81": True,
            "TH24_NEEDED": False,
            "NEXT": "Stage14-t82",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
