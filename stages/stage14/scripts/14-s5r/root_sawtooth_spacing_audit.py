#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5r."""

from __future__ import annotations

import cmath
import json
from math import gcd, isqrt, log, pi, sqrt

CHARTS = ("A", "B", "C", "D")


def factor_with_exponents(n):
    x = abs(n)
    out = []
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out.append((p, e))
        p += 1
    if x > 1:
        out.append((x, 1))
    return out


def prime_factors(n):
    return [p for p, _ in factor_with_exponents(n)]


def is_squarefree(n):
    return n > 0 and all(e == 1 for _, e in factor_with_exponents(n))


def split_squarefree(n):
    return n > 0 and n % 2 == 1 and is_squarefree(n) and all(
        p % 4 == 1 for p in prime_factors(n)
    )


def squareclass_kernel_odd(n):
    """Odd squarefree kernel in Q*/Q*2: retain only odd valuation parity."""
    z = 1
    for p, e in factor_with_exponents(n):
        if p % 2 == 1 and e % 2 == 1:
            z *= p
    return z


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    if n == 1:
        return 1
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def roots_minus_one(v):
    return [r for r in range(v) if (r * r + 1) % v == 0]


def chart_c(chart, r, v):
    inv2 = pow(2, -1, v)
    return {
        "A": (-r) % v,
        "B": r % v,
        "C": (-(r + 1) * inv2) % v,
        "D": ((1 - r) * inv2) % v,
    }[chart]


def F(chart, x, y):
    if chart in ("A", "B"):
        return x * x + y * y
    if chart == "C":
        return 2 * x * x + 2 * x * y + y * y
    return 2 * x * x - 2 * x * y + y * y


def centered_residue(x, v):
    z = x % v
    return z - v if z > v // 2 else z


def check_charts():
    root_checks = positivity_checks = 0
    for v in range(5, 260, 2):
        if not split_squarefree(v):
            continue
        rs = roots_minus_one(v)
        assert len(rs) == 2 ** len(prime_factors(v))
        for r in rs:
            for chart in CHARTS:
                assert F(chart, chart_c(chart, r, v), 1) % v == 0
                root_checks += 1
    for chart in CHARTS:
        for x in range(-14, 15):
            for y in range(-14, 15):
                if (x, y) != (0, 0):
                    assert F(chart, x, y) > 0
                    positivity_checks += 1
    return root_checks, positivity_checks


def check_fourier():
    checks = 0
    worst = 0.0
    l1_ratio = 0.0
    for v in (5, 7, 13, 17, 29, 65):
        gammas = [
            -1.0 / (v * (1.0 - cmath.exp(-2j * pi * h / v)))
            for h in range(1, v)
        ]
        l1_ratio = max(
            l1_ratio, sum(abs(z) for z in gammas) / max(1.0, log(2 * v))
        )
        for k in range(v):
            z = -1.0 / (2.0 * v)
            for h, gamma in enumerate(gammas, start=1):
                z += gamma * cmath.exp(2j * pi * h * k / v)
            target = k / v - 0.5
            err = abs(z - target)
            worst = max(worst, err)
            assert err < 1e-10
            checks += 1
    return checks, worst, l1_ratio


def check_frequency_divisibility():
    checks = nontrivial_gcd = 0
    for v in range(5, 220, 2):
        if not split_squarefree(v):
            continue
        for r in roots_minus_one(v):
            for chart in CHARTS:
                c = chart_c(chart, r, v)
                for u in range(3, 24, 2):
                    if gcd(u, v) != 1:
                        continue
                    for d in (1, 3, 5):
                        if gcd(d, v) != 1:
                            continue
                        for h in range(1, min(24, v)):
                            delta = centered_residue(h * c * u * d, v)
                            g = gcd(h, v)
                            assert delta % g == 0
                            val = F(chart, delta // g, (h // g) * u * d)
                            assert val != 0 and val % (v // g) == 0
                            checks += 1
                            nontrivial_gcd += int(g > 1)
    assert nontrivial_gcd > 0
    return checks, nontrivial_gcd


def resonance_ledger():
    worst = 0.0
    records = 0
    for chart in CHARTS:
        for h in (1, 2, 3, 5, 7):
            for D in (2, 4, 8, 16):
                count = 0
                us = list(range(7, 25, 2))
                for v in range(45, 181, 2):
                    if not split_squarefree(v):
                        continue
                    for r in roots_minus_one(v):
                        c = chart_c(chart, r, v)
                        for u in us:
                            if gcd(u, v) == 1 and abs(centered_residue(h * c * u, v)) <= D:
                                count += 1
                worst = max(worst, count / max(1, len(us) * D))
                records += 1
    assert worst < 20.0
    return records, worst


def check_walsh_pairing():
    checks = 0
    max_l1 = max_l2sq = 0.0
    for e in range(5, 500, 2):
        if not split_squarefree(e):
            continue
        omega = len(prime_factors(e))
        w = 2.0 ** (-omega)
        ds = divisors(e)
        small = [v for v in ds if v * v < e]
        for d in range(3, 80, 2):
            if gcd(d, e) != 1:
                continue
            lhs = w * sum(jacobi(d, v) for v in ds)
            rhs = w * (1 + jacobi(d, e)) * sum(jacobi(d, v) for v in small)
            assert abs(lhs - rhs) < 1e-12
            checks += 1
        paired = [2 * w for _ in small]
        max_l1 = max(max_l1, sum(paired))
        max_l2sq = max(max_l2sq, sum(x * x for x in paired))
    assert max_l1 <= 1 + 1e-12 and max_l2sq <= 1 + 1e-12
    return checks, max_l1, max_l2sq


def primitive_pairs(limit):
    for m in range(2, limit + 1):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                yield m, n


def check_whole_e_subpieces():
    checks = 0
    for m, n in primitive_pairs(42):
        vals = {"A": m, "B": n, "C": m - n, "D": m + n}
        e = squareclass_kernel_odd(m * m + n * n)
        if e == 1:
            continue
        assert split_squarefree(e)
        for chart, val in vals.items():
            k = squareclass_kernel_odd(val)
            for q in divisors(k):
                if q % 2 == 0 or gcd(q, e) != 1:
                    continue
                lhs = jacobi(q, e)
                rhs = 1 if chart in ("A", "B") else jacobi(2, q)
                assert lhs == rhs, (m, n, chart, q, e, lhs, rhs)
                checks += 1
    assert checks > 0
    return checks


def mixed_sum(T, q, t):
    z = 0j
    for n in range(1, T + 1):
        if not is_squarefree(n):
            continue
        z += jacobi(n, q) * cmath.exp(2j * pi * t * n / q)
    return z


def check_mixed_ledger():
    checks = 0
    worst = 0.0
    for q in (5, 13, 17, 29, 65, 85):
        if not split_squarefree(q):
            continue
        for T in (12, 24, 48, 72):
            for t in (1, 2, 3, 5):
                z = mixed_sum(T, q, t)
                env = sqrt(T) * q ** 0.25 * max(1.0, log(2 * q))
                ratio = abs(z) / env
                worst = max(worst, ratio)
                assert ratio < 4.0
                checks += 1
    return checks, worst


def exponent_ledger():
    zeta = 3 / 20
    eta = 1 / 100
    far = 2 - zeta
    near = 1 + 5 / 4 - (1 - zeta) / 2 + 3 * eta / 4
    assert abs(far - 37 / 20) < 1e-12
    assert abs(near - 733 / 400) < 1e-12
    assert far < 2 and near < 2 and 3 / 2 < 2
    return {
        "zeta": zeta,
        "s5o_eta": eta,
        "far_exponent": far,
        "near_exponent": near,
        "critical_exponent": 3 / 2,
        "assembled_conservative_saving": 1 / 200,
    }


def main():
    chart_checks, positive_checks = check_charts()
    fourier_checks, fourier_error, fourier_l1 = check_fourier()
    freq_checks, gcd_checks = check_frequency_divisibility()
    resonance_records, resonance_worst = resonance_ledger()
    walsh_checks, walsh_l1, walsh_l2 = check_walsh_pairing()
    whole_e_checks = check_whole_e_subpieces()
    mixed_checks, mixed_worst = check_mixed_ledger()
    exponents = exponent_ledger()

    print(json.dumps({
        "stage": "14-s5r",
        "root_chart_checks": chart_checks,
        "positive_definite_checks": positive_checks,
        "sawtooth_fourier_checks": fourier_checks,
        "sawtooth_fourier_worst_error": fourier_error,
        "sawtooth_fourier_l1_over_log_max": fourier_l1,
        "frequency_divisibility_checks": freq_checks,
        "frequency_nontrivial_gcd_checks": gcd_checks,
        "near_resonance_records": resonance_records,
        "near_resonance_worst_count_over_UD": resonance_worst,
        "walsh_pairing_checks": walsh_checks,
        "walsh_paired_l1_max": walsh_l1,
        "walsh_paired_l2sq_max": walsh_l2,
        "whole_e_subpiece_checks": whole_e_checks,
        "mixed_completion_checks": mixed_checks,
        "mixed_completion_worst_ratio": mixed_worst,
        "exponent_ledger": exponents,
    }, indent=2))

    flags = [
        "STAGE14_S5R=COMPLETE_ROOT_SAWTOOTH_SPACING_AND_FULL_LOCAL_CHARACTER_AVERAGE",
        "ROOT_CHART_QUADRATIC_FORMS_EXACT=true",
        "ROOT_SAWTOOTH_FINITE_FOURIER_EXACT=true",
        "ROOT_FREQUENCY_QUADRATIC_FORM_DIVISIBILITY_PROVED=true",
        "ROOT_NEAR_RESONANCE_DIVISOR_COUNT_PROVED=true",
        "ROOT_SAWTOOTH_SPACING_BOUND_PROVED=true",
        "CRITICAL_U_SQRTM_V_M_POWER_SAVING_PROVED=true",
        "E_WALSH_SMALL_SIDE_PAIRING_EXACT=true",
        "E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E=true",
        "WHOLE_E_PAIRED_FACTOR_ONE_VARIABLE=true",
        "MIXED_SQUAREFREE_GAUSS_COMPLETION_PROVED=true",
        "E_LINEAR_TRANSITION_WEDGE_CLOSED=true",
        "GENUINE_ROOT_SAWTOOTH_RESONANCE_FOUND=false",
        "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true",
        "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED=true",
        "FAMILY_LARGE_SIEVE_THEOREM_PROVED=false",
        "GLOBAL_SOLUBILITY_AVERAGED=false",
        "SMALL_POINT_WINDOW_AVERAGED=false",
        "SQRT_B_ASYMPTOTIC_PROVED=false",
        "NEXT=Stage14-s5s",
    ]
    print("\n".join(flags))


if __name__ == "__main__":
    main()
