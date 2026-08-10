#!/usr/bin/env python3
"""Stage14-t76: clean-kappa primitive cover root-line audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T75 = ROOT / "stages/stage14/14-t75/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"
X11 = ROOT / "stages/stage14/14-X11/result.md"
B_FROZEN = 10_000
DIAG_BALANCE = 4


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def prime_divisors(n: int) -> list[int]:
    return sorted(factor(n))


def squarefree_kernel(n: int) -> int:
    out = 1
    for p, e in factor(n).items():
        if e & 1:
            out *= p
    return out


def normalized_slope(r: int, t: int) -> tuple[int, int]:
    d = gcd(r, t)
    return (r // d, t // d)


def main() -> None:
    t75_text = T75.read_text()
    th20_text = TH20.read_text()
    x11_text = X11.read_text()
    assert "STAGE14_T75=COMPLETE_ANGULAR_GCD_COLUMN_SPLIT_PRIMITIVE_SHORT_GAP_AND_TYPE_I_TYPE_II_COVER_REDUCTION" in t75_text
    assert "STAGE14_TH20=COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT" in th20_text
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34" in x11_text

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    bad_support_checks = 0
    clean_unit_checks = 0
    signed_factor_checks = 0
    rootline_checks = 0
    balance_checks = 0
    balanced_states = 0
    balanced_nontrivial_clean = 0
    balanced_spacing_closed_diag = 0
    clean_one_states = 0
    max_orientation_bound = 1
    max_bad = 1
    max_clean = 1
    max_kappa = 1
    max_g = 1
    clean_hist = Counter()
    bad_hist = Counter()
    ratio_hist = Counter()
    packet_root_multiplicity = Counter()

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta
        h = eps * m // k
        assert h * k == eps * m

        # Rebuild the primitive square scale s=kappa*(u/v)^2 and denominator tag beta.
        s0 = Fraction(b * b * p * p - a * a * q * q,
                      b * b * q * q - a * a * p * p)
        sq = s0 / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator and gcd(u, v) == 1
        beta = gcd(kappa, v)
        alpha = kappa // beta
        assert alpha * beta == kappa and gcd(alpha, beta) == 1

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pplus, Pminus = raw_plus // G, raw_minus // G
        assert gcd(Pplus * Pminus, kappa) == 1
        assert Pminus % ell == 0

        # t71/t75 angular chart.
        A, B = b - a, b + a
        r, t = q - p, q + p
        assert A > 0 and B > A and 0 < r < t
        assert gcd(A, B) in (1, 2)
        assert gcd(r, t) in (1, 2)
        L1 = A * t - B * r
        L2 = B * t - A * r
        L3 = A * t + B * r
        L4 = B * t + A * r
        assert L1 > 0 and L2 > 0 and L3 > 0 and L4 > 0
        assert squarefree_kernel(L1 * L2 * L3 * L4) == kappa

        K = oddpart(kappa)
        g = gcd(oddpart(A * B), oddpart(r * t))
        K_bad = gcd(K, oddpart(A * B * r * t))
        assert K_bad == gcd(K, g)
        K_clean = K // K_bad
        assert K_clean * K_bad == K
        assert gcd(K_clean, A * B * r * t) == 1
        assert K_clean >= (K + g - 1) // g if g else K_clean == K
        bad_support_checks += 1
        clean_unit_checks += 1

        alpha_odd = oddpart(alpha)
        beta_odd = oddpart(beta)
        alpha_clean = gcd(alpha_odd, K_clean)
        beta_clean = gcd(beta_odd, K_clean)
        assert gcd(alpha_clean, beta_clean) == 1
        assert alpha_clean * beta_clean == K_clean
        assert (L1 * L2) % alpha_clean == 0
        assert (L3 * L4) % beta_clean == 0
        signed_factor_checks += 1

        # The actual physical slope must lie in one of the two reciprocal roots per clean prime.
        if K_clean > 1:
            rho = (t * pow(r, -1, K_clean)) % K_clean
            assert gcd(rho, K_clean) == 1
        else:
            rho = 0

        orientation_bound = 1
        for pp in prime_divisors(K_clean):
            assert gcd(A * B * r, pp) == 1
            sign = 1 if alpha_clean % pp == 0 else -1
            root1 = (sign * B * pow(A, -1, pp)) % pp
            root2 = (sign * A * pow(B, -1, pp)) % pp
            allowed = {root1, root2}
            actual = (t * pow(r, -1, pp)) % pp
            assert actual in allowed
            orientation_bound *= len(allowed)
        assert orientation_bound <= 2 ** len(prime_divisors(K_clean))
        max_orientation_bound = max(max_orientation_bound, orientation_bound)
        rootline_checks += 1

        balanced = t <= DIAG_BALANCE * r
        if balanced:
            balanced_states += 1
            if K_clean > 1:
                balanced_nontrivial_clean += 1
            if K_clean >= r * t:
                balanced_spacing_closed_diag += 1
        balance_checks += 1
        if K_clean == 1:
            clean_one_states += 1

        clean_hist[K_clean] += 1
        bad_hist[K_bad] += 1
        ratio_hist[min(16, t // r)] += 1
        max_bad = max(max_bad, K_bad)
        max_clean = max(max_clean, K_clean)
        max_kappa = max(max_kappa, K)
        max_g = max(max_g, g)

        # Diagnostic multiplicity for exactly fixed physical root-line packet.
        packet = (
            st["U"], eps, k, h, kappa, beta, ell,
            A, B, K_clean, rho,
            max(0, r.bit_length() - 1), max(0, t.bit_length() - 1),
        )
        packet_root_multiplicity[packet] += 1

    # Independent root-line determinant regression.  This tests the exact projective
    # spacing input without relying on cuboid data.
    determinant_regressions = 0
    zero_det_multiplicity_max = 0
    for K in range(3, 50, 2):
        for rho in range(1, K):
            if gcd(rho, K) != 1:
                continue
            pts = []
            for r in range(1, 32):
                if gcd(r, K) != 1:
                    continue
                for t in range(r + 1, 48):
                    if gcd(r, t) not in (1, 2):
                        continue
                    if (t - rho * r) % K == 0:
                        pts.append((r, t))
            by_slope: dict[tuple[int, int], int] = defaultdict(int)
            for pt in pts:
                by_slope[normalized_slope(*pt)] += 1
            if by_slope:
                zero_det_multiplicity_max = max(zero_det_multiplicity_max, max(by_slope.values()))
            # gcd(r,t)<=2 permits at most the primitive pair and its double.
            assert all(vv <= 2 for vv in by_slope.values())
            for i in range(len(pts)):
                r1, t1 = pts[i]
                for j in range(i + 1, len(pts)):
                    r2, t2 = pts[j]
                    det = t1 * r2 - t2 * r1
                    assert det % K == 0
                    determinant_regressions += 1

    report = {
        "stage": "14-t76",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "bad_support_checks": bad_support_checks,
        "clean_unit_checks": clean_unit_checks,
        "signed_factor_checks": signed_factor_checks,
        "rootline_checks": rootline_checks,
        "balance_checks": balance_checks,
        "diagnostic_balance_ratio": DIAG_BALANCE,
        "diagnostic_balanced_states": balanced_states,
        "diagnostic_balanced_nontrivial_clean_states": balanced_nontrivial_clean,
        "diagnostic_balanced_spacing_closed_states": balanced_spacing_closed_diag,
        "diagnostic_clean_kappa_one_states": clean_one_states,
        "max_orientation_bound": max_orientation_bound,
        "max_K_bad": max_bad,
        "max_K_clean": max_clean,
        "max_odd_kappa": max_kappa,
        "max_g": max_g,
        "max_fixed_rootline_packet_multiplicity": max(packet_root_multiplicity.values(), default=0),
        "determinant_regressions": determinant_regressions,
        "max_zero_determinant_slope_multiplicity": zero_det_multiplicity_max,
        "most_common_K_clean": clean_hist.most_common(12),
        "most_common_K_bad": bad_hist.most_common(12),
        "coarse_balance_histogram": sorted(ratio_hist.items()),
        "boundary": {
            "STAGE14_T76": "COMPLETE_CLEAN_KAPPA_COVER_PROJECTIVE_ROOTLINE_AND_DEFICIENT_TYPEII_REDUCTION",
            "MERGED_T75_IMPORTED": True,
            "MERGED_TH20_IMPORTED": True,
            "MERGED_X11_GLOBAL_19_34_LEDGER_IMPORTED": True,
            "KAPPA_NONUNIT_SUPPORT_EQUALS_KAPPA_INTERSECTION_ANGULAR_GCD": True,
            "CLEAN_KAPPA_COPRIME_TO_DIRECTION_AND_COVER_COORDINATES": True,
            "CLEAN_KAPPA_LOWER_BOUND": "K/g",
            "FIXED_BETA_DETERMINES_CLEAN_KAPPA_ROOT_SIGN": True,
            "CLEAN_KAPPA_RECIPROCAL_DIRECTION_CHOICES_PER_PRIME_AT_MOST": 2,
            "CLEAN_KAPPA_CRT_PROJECTIVE_ROOT_LINE_PROVED": True,
            "LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING": True,
            "SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_SMALL_ANGULAR_GCD_BALANCED_CLEAN_KAPPA_DEFICIENT_PRIMITIVE_COVER_TYPEII_DISPERSION_ENERGY_PROVED": False,
            "TH21_NEEDED": True,
            "TH21_REQUESTED_OBJECT": "SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion",
            "T_ROUTE_BLOCKED_WAITING_FOR_TH21": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "19/34",
            "T76_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "NEXT": "Stage14-t77",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
