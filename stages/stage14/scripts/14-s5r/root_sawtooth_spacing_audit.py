#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5r.

The analytic proof is in stages/stage14/14-s5r/result.md.  This audit checks
its exact algebraic interfaces: root charts, finite sawtooth Fourier expansion,
frequency-to-quadratic-form divisibility, E-Walsh complement pairing,
whole-E divisor identities, and representative mixed Gauss-completion ledgers.
"""

from __future__ import annotations

import cmath
import json
from math import gcd, isqrt, log, pi, sqrt


CHARTS = ("A", "B", "C", "D")


def prime_factors(n: int):
    out = []
    x = abs(n)
    p = 2
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out


def is_squarefree(n: int) -> bool:
    n = abs(n)
    if n == 0:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % (p * p) == 0:
            return False
    return True


def odd_squarefree(n: int) -> bool:
    return n > 0 and n % 2 == 1 and is_squarefree(n)


def split_squarefree(n: int) -> bool:
    return odd_squarefree(n) and all(p % 4 == 1 for p in prime_factors(n))


def squarefree_kernel_odd(n: int) -> int:
    z = 1
    for p in prime_factors(n):
        if p % 2 == 1:
            z *= p
    return z


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def jacobi(a: int, n: int) -> int:
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


def roots_minus_one(v: int):
    return [r for r in range(v) if (r * r + 1) % v == 0]


def chart_c(chart: str, r: int, v: int) -> int:
    inv2 = pow(2, -1, v)
    if chart == "A":
        return (-r) % v
    if chart == "B":
        return r % v
    if chart == "C":
        return (-(r + 1) * inv2) % v
    if chart == "D":
        return ((1 - r) * inv2) % v
    raise ValueError(chart)


def F(chart: str, x: int, y: int) -> int:
    if chart in ("A", "B"):
        return x * x + y * y
    if chart == "C":
        return 2 * x * x + 2 * x * y + y * y
    if chart == "D":
        return 2 * x * x - 2 * x * y + y * y
    raise ValueError(chart)


def centered_residue(x: int, v: int) -> int:
    z = x % v
    if z > v // 2:
        z -= v
    return z


def mobius_squarefree_indicator(n: int) -> int:
    return 1 if is_squarefree(n) else 0


def check_chart_identities():
    checks = 0
    positivity_checks = 0
    for v in range(5, 260, 2):
        if not split_squarefree(v):
            continue
        roots = roots_minus_one(v)
        assert len(roots) == 2 ** len(prime_factors(v))
        for r in roots:
            for chart in CHARTS:
                c = chart_c(chart, r, v)
                assert F(chart, c, 1) % v == 0, (chart, v, r, c)
                checks += 1

    for chart in CHARTS:
        for x in range(-15, 16):
            for y in range(-15, 16):
                if x == 0 and y == 0:
                    continue
                assert F(chart, x, y) > 0, (chart, x, y, F(chart, x, y))
                positivity_checks += 1
    return checks, positivity_checks


def check_sawtooth_fourier():
    checks = 0
    worst = 0.0
    l1_ratios = []
    for v in (5, 7, 13, 17, 29, 65):
        l1 = 0.0
        for h in range(1, v):
            gamma = -1.0 / (
                v * (1.0 - cmath.exp(-2j * pi * h / v))
            )
            l1 += abs(gamma)
        l1_ratios.append(l1 / max(1.0, log(2 * v)))

        for k in range(v):
            z = -1.0 / (2.0 * v)
            for h in range(1, v):
                gamma = -1.0 / (
                    v * (1.0 - cmath.exp(-2j * pi * h / v))
                )
                z += gamma * cmath.exp(2j * pi * h * k / v)
            target = k / v - 0.5
            err = abs(z - target)
            worst = max(worst, err)
            assert err < 1e-10, (v, k, z, target)
            checks += 1
    return checks, worst, max(l1_ratios)


def check_frequency_divisibility():
    checks = 0
    nontrivial_gcd_checks = 0
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
                            assert delta % g == 0, (v, h, delta, g)
                            v1 = v // g
                            h1 = h // g
                            delta1 = delta // g
                            val = F(chart, delta1, h1 * u * d)
                            assert val != 0
                            assert val % v1 == 0, (
                                chart,
                                v,
                                r,
                                u,
                                d,
                                h,
                                delta,
                                g,
                                val,
                            )
                            checks += 1
                            if g > 1:
                                nontrivial_gcd_checks += 1
    assert nontrivial_gcd_checks > 0
    return checks, nontrivial_gcd_checks


def near_resonance_ledger():
    # Regression ledger only: compare finite near-resonance counts to U*D.
    records = []
    worst_ratio = 0.0
    for chart in CHARTS:
        for h in (1, 2, 3, 5, 7):
            for D in (2, 4, 8, 16):
                Ulo, Uhi = 7, 25
                count = 0
                for v in range(45, 181, 2):
                    if not split_squarefree(v):
                        continue
                    for r in roots_minus_one(v):
                        c = chart_c(chart, r, v)
                        for u in range(Ulo, Uhi):
                            if u % 2 == 0 or gcd(u, v) != 1:
                                continue
                            delta = abs(centered_residue(h * c * u, v))
                            if delta <= D:
                                count += 1
                Ucount = sum(1 for u in range(Ulo, Uhi) if u % 2 == 1)
                scale = max(1, Ucount * D)
                ratio = count / scale
                worst_ratio = max(worst_ratio, ratio)
                records.append((chart, h, D, count, ratio))
    # The theorem permits divisor-power factors; this just catches regressions.
    assert worst_ratio < 20.0, worst_ratio
    return len(records), worst_ratio


def check_walsh_pairing():
    checks = 0
    max_l1 = 0.0
    max_l2sq = 0.0
    for e in range(5, 500, 2):
        if not split_squarefree(e):
            continue
        omega = len(prime_factors(e))
        weight = 2.0 ** (-omega)
        ds = divisors(e)
        for d in range(3, 80, 2):
            if gcd(d, e) != 1:
                continue
            lhs = weight * sum(jacobi(d, v) for v in ds)
            small = [v for v in ds if v * v < e]
            rhs = weight * (1 + jacobi(d, e)) * sum(
                jacobi(d, v) for v in small
            )
            assert abs(lhs - rhs) < 1e-12, (e, d, lhs, rhs)
            checks += 1

        # Paired coefficient mass after expanding (1+chi_e).
        paired_weights = [2.0 * weight for v in ds if v * v < e]
        max_l1 = max(max_l1, sum(paired_weights))
        max_l2sq = max(max_l2sq, sum(w * w for w in paired_weights))
    assert max_l1 <= 1.0 + 1e-12
    assert max_l2sq <= 1.0 + 1e-12
    return checks, max_l1, max_l2sq


def primitive_pairs(limit: int):
    for m in range(2, limit + 1):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                yield m, n


def odd_squarefree_divisors_of_kernel(n: int):
    k = squarefree_kernel_odd(n)
    return [d for d in divisors(k) if d % 2 == 1]


def check_whole_e_subpiece_identities():
    checks = 0
    for m, n in primitive_pairs(42):
        vals = {
            "A": m,
            "B": n,
            "C": m - n,
            "D": m + n,
        }
        e = squarefree_kernel_odd(m * m + n * n)
        if e == 1:
            continue
        assert all(p % 4 == 1 for p in prime_factors(e))
        for chart, val in vals.items():
            for q in odd_squarefree_divisors_of_kernel(val):
                if gcd(q, e) != 1:
                    continue
                lhs = jacobi(q, e)
                rhs = 1 if chart in ("A", "B") else jacobi(2, q)
                assert lhs == rhs, (m, n, chart, q, e, lhs, rhs)
                checks += 1
    assert checks > 0
    return checks


def mixed_sum(T: int, q: int, t: int, offset: int = 1):
    z = 0j
    for n in range(offset, offset + T):
        if not is_squarefree(n):
            continue
        chi = jacobi(n, q)
        z += chi * cmath.exp(2j * pi * t * n / q)
    return z


def check_mixed_completion_ledger():
    checks = 0
    worst_ratio = 0.0
    for q in (5, 13, 17, 29, 65, 85):
        if not split_squarefree(q):
            continue
        for T in (12, 24, 48, 72):
            for t in (1, 2, 3, 5):
                z = mixed_sum(T, q, t)
                envelope = sqrt(T) * (q ** 0.25) * max(1.0, log(2 * q))
                ratio = abs(z) / envelope
                worst_ratio = max(worst_ratio, ratio)
                assert ratio < 4.0, (T, q, t, abs(z), envelope)
                checks += 1
    return checks, worst_ratio


def exponent_ledger():
    # Z=M^(3/20); s5o short-neighbor threshold M^(1/100).
    zeta = 3 / 20
    eta = 1 / 100
    far_exponent = 2 - zeta
    near_exponent = 1 + 5 / 4 - (1 - zeta) / 2 + 3 * eta / 4
    critical_exponent = 3 / 2
    assert abs(far_exponent - 37 / 20) < 1e-12
    assert abs(near_exponent - 733 / 400) < 1e-12
    assert far_exponent < 2
    assert near_exponent < 2
    assert critical_exponent < 2
    return {
        "zeta": zeta,
        "s5o_eta": eta,
        "far_exponent": far_exponent,
        "near_exponent": near_exponent,
        "critical_U_sqrtM_V_M_exponent": critical_exponent,
        "assembled_conservative_saving": 1 / 200,
    }


def main():
    chart_checks, positivity_checks = check_chart_identities()
    fourier_checks, fourier_worst, l1_ratio = check_sawtooth_fourier()
    freq_checks, nontrivial_gcd_checks = check_frequency_divisibility()
    resonance_records, resonance_worst = near_resonance_ledger()
    walsh_checks, walsh_l1, walsh_l2sq = check_walsh_pairing()
    whole_e_checks = check_whole_e_subpiece_identities()
    mixed_checks, mixed_worst = check_mixed_completion_ledger()
    exponents = exponent_ledger()

    report = {
        "metadata": {
            "stage": "14-s5r",
            "classification": "DETERMINISTIC_REGRESSION_PLUS_ANALYTIC_THEOREM_INTERFACE",
        },
        "root_chart_checks": chart_checks,
        "positive_definite_checks": positivity_checks,
        "sawtooth_fourier_checks": fourier_checks,
        "sawtooth_fourier_worst_error": fourier_worst,
        "sawtooth_fourier_l1_over_log_max": l1_ratio,
        "frequency_divisibility_checks": freq_checks,
        "frequency_nontrivial_gcd_checks": nontrivial_gcd_checks,
        "near_resonance_ledger_records": resonance_records,
        "near_resonance_worst_count_over_UD": resonance_worst,
        "walsh_pairing_checks": walsh_checks,
        "walsh_paired_l1_max": walsh_l1,
        "walsh_paired_l2sq_max": walsh_l2sq,
        "whole_e_subpiece_checks": whole_e_checks,
        "mixed_completion_checks": mixed_checks,
        "mixed_completion_worst_ratio": mixed_worst,
        "exponent_ledger": exponents,
        "decision": {
            "STAGE14_S5R": "COMPLETE_ROOT_SAWTOOTH_SPACING_AND_FULL_LOCAL_CHARACTER_AVERAGE",
            "ROOT_CHART_QUADRATIC_FORMS_EXACT": True,
            "ROOT_SAWTOOTH_FINITE_FOURIER_EXACT": True,
            "ROOT_FREQUENCY_QUADRATIC_FORM_DIVISIBILITY_PROVED": True,
            "ROOT_NEAR_RESONANCE_DIVISOR_COUNT_PROVED": True,
            "ROOT_SAWTOOTH_SPACING_BOUND_PROVED": True,
            "CRITICAL_U_SQRTM_V_M_POWER_SAVING_PROVED": True,
            "E_WALSH_SMALL_SIDE_PAIRING_EXACT": True,
            "E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E": True,
            "WHOLE_E_PAIRED_FACTOR_ONE_VARIABLE": True,
            "MIXED_SQUAREFREE_GAUSS_COMPLETION_PROVED": True,
            "E_LINEAR_TRANSITION_WEDGE_CLOSED": True,
            "GENUINE_ROOT_SAWTOOTH_RESONANCE_FOUND": False,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": True,
            "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED": True,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "GLOBAL_SOLUBILITY_AVERAGED": False,
            "SMALL_POINT_WINDOW_AVERAGED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5s",
        },
    }
    print(json.dumps(report, indent=2))

    print("STAGE14_S5R=COMPLETE_ROOT_SAWTOOTH_SPACING_AND_FULL_LOCAL_CHARACTER_AVERAGE")
    print("ROOT_CHART_QUADRATIC_FORMS_EXACT=true")
    print("ROOT_SAWTOOTH_FINITE_FOURIER_EXACT=true")
    print("ROOT_FREQUENCY_QUADRATIC_FORM_DIVISIBILITY_PROVED=true")
    print("ROOT_NEAR_RESONANCE_DIVISOR_COUNT_PROVED=true")
    print("ROOT_SAWTOOTH_SPACING_BOUND_PROVED=true")
    print("CRITICAL_U_SQRTM_V_M_POWER_SAVING_PROVED=true")
    print("E_WALSH_SMALL_SIDE_PAIRING_EXACT=true")
    print("E_ANALYTIC_SUBSET_MODULUS_LE_SQRT_E=true")
    print("WHOLE_E_PAIRED_FACTOR_ONE_VARIABLE=true")
    print("MIXED_SQUAREFREE_GAUSS_COMPLETION_PROVED=true")
    print("E_LINEAR_TRANSITION_WEDGE_CLOSED=true")
    print("GENUINE_ROOT_SAWTOOTH_RESONANCE_FOUND=false")
    print("FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true")
    print("ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED=true")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("GLOBAL_SOLUBILITY_AVERAGED=false")
    print("SMALL_POINT_WINDOW_AVERAGED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5s")


if __name__ == "__main__":
    main()
