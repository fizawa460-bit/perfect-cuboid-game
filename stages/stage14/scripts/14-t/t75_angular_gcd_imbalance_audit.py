#!/usr/bin/env python3
"""Stage14-t75: angular-gcd column split and cover imbalance audit."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T74 = ROOT / "stages/stage14/14-t74/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"
X11 = ROOT / "stages/stage14/14-X11/result.md"
B_FROZEN = 10_000
DIAG_G_THRESHOLD = 5
DIAG_IMBALANCE = 4


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def divisors(n: int) -> list[int]:
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def main() -> None:
    t74_text = T74.read_text()
    th20_text = TH20.read_text()
    x11_text = X11.read_text()
    assert "STAGE14_T74=COMPLETE_CANONICAL_HOST_ELL_FREE_COFACTOR_BALANCE_AND_SHORT_ANGULAR_COVER_REDUCTION" in t74_text
    assert "STAGE14_TH20=COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT" in th20_text
    assert "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false" in th20_text
    assert "ANGULAR_DIVISOR_SWITCHING_POST_T74_PREFERRED=true" in th20_text
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34" in x11_text

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    column_split_checks = 0
    short_gap_checks = 0
    type_i_linear_checks = 0
    imbalance_checks = 0
    large_g_divisor_checks = 0
    balanced_count = 0
    unbalanced_count = 0
    large_g_count = 0
    c_hist = Counter()
    g_hist = Counter()
    gr_hist = Counter()
    gt_hist = Counter()
    ratio_hist = Counter()
    max_gap_core_ratio = Fraction(0, 1)
    max_imbalance = Fraction(0, 1)
    seen_A: set[int] = set()

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta
        h = eps * m // k
        H = oddpart(h)

        s0 = Fraction(b * b * p * p - a * a * q * q,
                      b * b * q * q - a * a * p * p)
        sq = s0 / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator and gcd(u, v) == 1
        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pminus = raw_minus // G
        assert Pminus % ell == 0
        c = oddpart(Pminus // ell)

        r, t = q - p, q + p
        assert 0 < r < t
        assert gcd(r, t) in (1, 2)
        assert r * r + t * t == 2 * n
        assert h * ell * (r * r + t * t) <= 4 * B_FROZEN
        assert t * t < ell

        R, T = oddpart(r), oddpart(t)
        assert gcd(R, T) == 1
        A = oddpart(b * b - a * a)
        gr = gcd(A, R)
        gt = gcd(A, T)
        g = gcd(A, R * T)
        assert gcd(gr, gt) == 1
        assert g == gr * gt
        R0, T0 = R // gr, T // gt
        assert gcd(R0, T0) == 1
        assert c % H == 0
        assert c // H == R0 * T0
        assert oddpart(r * t) == R * T == g * c // H
        column_split_checks += 1

        assert r <= 2 * R * T
        assert r * H <= 2 * g * c
        gap_core_ratio = Fraction(r * H, g * c)
        max_gap_core_ratio = max(max_gap_core_ratio, gap_core_ratio)
        short_gap_checks += 1

        assert T % gt == 0
        assert c == H * R0 * (T // gt)
        type_i_linear_checks += 1

        imbalance = Fraction(t, r)
        max_imbalance = max(max_imbalance, imbalance)
        if t > DIAG_IMBALANCE * r:
            unbalanced_count += 1
            assert (1 + DIAG_IMBALANCE**2) * r * r < r * r + t * t
            assert h * ell * (1 + DIAG_IMBALANCE**2) * r * r < 4 * B_FROZEN
        else:
            balanced_count += 1
            assert t <= DIAG_IMBALANCE * r
            assert t * H <= 2 * DIAG_IMBALANCE * g * c
        imbalance_checks += 1

        if g >= DIAG_G_THRESHOLD:
            large_g_count += 1
        c_hist[c] += 1
        g_hist[g] += 1
        gr_hist[gr] += 1
        gt_hist[gt] += 1
        ratio_hist[min(16, t // r)] += 1

        if A not in seen_A:
            ds = divisors(A)
            lhs = sum(Fraction(1, d) for d in ds if d >= DIAG_G_THRESHOLD)
            rhs = Fraction(len(ds), DIAG_G_THRESHOLD)
            assert lhs <= rhs
            large_g_divisor_checks += 1
            seen_A.add(A)

    exhaustive_short_gap = 0
    for p in range(1, 90):
        for q in range(p + 1, 120):
            if gcd(p, q) != 1:
                continue
            r, t = q - p, q + p
            assert gcd(r, t) in (1, 2)
            assert gcd(oddpart(r), oddpart(t)) == 1
            assert r <= 2 * oddpart(r * t)
            exhaustive_short_gap += 1

    report = {
        "stage": "14-t75",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "column_split_checks": column_split_checks,
        "primitive_short_gap_checks": short_gap_checks,
        "type_i_linearization_checks": type_i_linear_checks,
        "imbalance_checks": imbalance_checks,
        "large_g_divisor_sum_checks": large_g_divisor_checks,
        "exhaustive_primitive_short_gap_regressions": exhaustive_short_gap,
        "diagnostic_thresholds": {
            "large_g": DIAG_G_THRESHOLD,
            "imbalance_ratio": DIAG_IMBALANCE,
        },
        "diagnostic_counts": {
            "large_g_states": large_g_count,
            "balanced_states": balanced_count,
            "highly_unbalanced_states": unbalanced_count,
        },
        "max_gap_over_gc_over_H": f"{max_gap_core_ratio.numerator}/{max_gap_core_ratio.denominator}",
        "max_imbalance": f"{max_imbalance.numerator}/{max_imbalance.denominator}",
        "most_common_c": c_hist.most_common(10),
        "most_common_g": g_hist.most_common(10),
        "most_common_g_r": gr_hist.most_common(10),
        "most_common_g_t": gt_hist.most_common(10),
        "coarse_imbalance_histogram": sorted(ratio_hist.items()),
        "boundary": {
            "STAGE14_T75": "COMPLETE_ANGULAR_GCD_COLUMN_SPLIT_PRIMITIVE_SHORT_GAP_AND_TYPE_I_TYPE_II_COVER_REDUCTION",
            "MERGED_T74_IMPORTED": True,
            "MERGED_TH20_IMPORTED": True,
            "MERGED_X11_GLOBAL_19_34_LEDGER_IMPORTED": True,
            "ANGULAR_G_SPLITS_UNIQUELY_ACROSS_COVER_COLUMNS": True,
            "SHORT_COFACTOR_OVER_H_EQUALS_UNCANCELLED_ODD_COLUMN_PRODUCT": True,
            "PRIMITIVE_SHORT_GAP_LEMMA_PROVED": True,
            "LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED": True,
            "LARGE_ANGULAR_G_PAIR_ENERGY_CLOSED": False,
            "COVER_IMBALANCE_SPLIT_EXACT": True,
            "HIGH_IMBALANCE_FORCES_SHORT_GAP": True,
            "HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I": True,
            "HIGH_IMBALANCE_TYPE_I_POWER_SAVING_PROVED": False,
            "POST_T75_GENUINE_TWO_VARIABLE_BLOCK_IS_BALANCED_SMALL_G": True,
            "SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_SMALL_ANGULAR_GCD_BALANCED_SHORT_COVER_TYPE_II_DISPERSION_ENERGY_PROVED": False,
            "TH20_MERGED": True,
            "TH20_CONSUMED_BY_T75": True,
            "TH20_USED_AS_HARD_THEOREM_PREDECESSOR": False,
            "TH21_NEEDED": False,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH20": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "19/34",
            "T75_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "NEXT": "Stage14-t76",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
