#!/usr/bin/env python3
"""Stage14-t73: kappa=1 factorization / fixed-tag / fixed-norm fiber audit."""

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
T72 = ROOT / "stages/stage14/14-t72/result.md"
S732 = ROOT / "stages/stage14/14-s7-32/result.md"


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


def tau(n: int) -> int:
    out = 1
    for e in factor(n).values():
        out *= e + 1
    return out


def is_squarefree(n: int) -> bool:
    return n > 0 and all(e == 1 for e in factor(n).values())


def lpf_odd(n: int) -> int:
    return max((p for p in factor(oddpart(n)) if p & 1), default=1)


def kappa_one_exhaustive_regression(limit: int = 80) -> int:
    checks = 0
    for u in range(1, limit + 1):
        for v in range(u + 1, limit + 1):
            if gcd(u, v) != 1:
                continue
            rp, rm = v * v + u * u, v * v - u * u
            G = gcd(rp, rm)
            assert G in (1, 2)
            eta = G
            Pm = rm // G
            Lm, Lp = (v - u) // eta, (v + u) // eta
            assert Lm > 0 and Lp > 0 and gcd(Lm, Lp) == 1
            assert Pm == eta * Lm * Lp
            assert eta * (Lp - Lm) % 2 == 0
            assert eta * (Lp + Lm) % 2 == 0
            assert eta * (Lp - Lm) // 2 == u
            assert eta * (Lp + Lm) // 2 == v
            checks += 1
    return checks


def fixed_norm_exhaustive_regression() -> int:
    """Small-box shadow of the ideal-divisor x unit-orbit theorem."""
    checks = 0
    for kappa in range(2, 31):
        if not is_squarefree(kappa):
            continue
        for n in range(1, 61):
            for H in (12, 24, 48):
                cnt = sum(
                    1
                    for x in range(1, H + 1)
                    for y in range(0, H + 1)
                    if x * x - kappa * y * y == n
                )
                assert cnt <= 8 * tau(n) * tau(n) * (1 + H.bit_length())
                checks += 1
    return checks


def main() -> None:
    t72 = T72.read_text()
    s732 = S732.read_text()
    assert "STAGE14_T72=COMPLETE_KAPPA_DENOMINATOR_TAG_FULL_CAYLEY_ROOTLINE_AND_PELL_SMOOTH_REDUCTION" in t72
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8" in t72
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8" in s732

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    tagged_normal_checks = canonical_filter_checks = kappa_one_states = 0
    tag_hist = Counter()
    records = []

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta0 = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta0
        h = eps * m // k
        Mroot = ell * oddpart(h) * oddpart(delta0)

        s = Fraction(b * b * p * p - a * a * q * q, b * b * q * q - a * a * p * p)
        sq = s / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator and gcd(u, v) == 1

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pplus, Pminus = raw_plus // G, raw_minus // G
        assert gcd(Pplus, Pminus) == 1 and Pplus > Pminus > 0

        beta = gcd(kappa, v)
        alpha = kappa // beta
        assert v % beta == 0 and G in (beta, 2 * beta)
        w, eta = v // beta, G // beta
        assert eta in (1, 2)
        assert eta * Pplus == beta * w * w + alpha * u * u
        assert eta * Pminus == beta * w * w - alpha * u * u
        x = beta * w
        assert x * x - kappa * u * u == beta * eta * Pminus
        assert x * x + kappa * u * u == beta * eta * Pplus
        tagged_normal_checks += 1
        tag_hist[beta] += 1

        assert Pminus % ell == 0
        assert factor(Pminus).get(ell, 0) == 1
        assert lpf_odd(Pplus * Pminus) == ell
        assert 2 * (oddpart(Pminus) // ell) < ell
        canonical_filter_checks += 1

        if kappa == 1:
            assert alpha == beta == 1
            Lm, Lp = (v - u) // eta, (v + u) // eta
            assert gcd(Lm, Lp) == 1 and Pminus == eta * Lm * Lp
            assert (Lm % ell == 0) != (Lp % ell == 0)
            kappa_one_states += 1

        records.append({
            "packet": (tuple(st["U"]), eps, k, h),
            "kappa": kappa,
            "Kodd": oddpart(kappa),
            "beta": beta,
            "Pplus": Pplus,
            "Pminus": Pminus,
            "ell": ell,
            "Mroot": Mroot,
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    pair_tag_checks = same_tag_checks = private_pairs = 0
    orientation_hist = Counter()
    for vals in groups.values():
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                x, y = vals[i], vals[j]
                if x["ell"] == y["ell"]:
                    continue
                if x["Mroot"] % y["ell"] == 0 or y["Mroot"] % x["ell"] == 0:
                    continue
                if (
                    y["Pplus"] % x["ell"] == 0
                    or y["Pminus"] % x["ell"] == 0
                    or x["Pplus"] % y["ell"] == 0
                    or x["Pminus"] % y["ell"] == 0
                ):
                    continue
                private_pairs += 1

                K = x["Kodd"]
                assert K == y["Kodd"]
                di, dj = gcd(K, x["beta"]), gcd(K, y["beta"])
                gd = gcd(di, dj)
                Kswitch = di * dj // (gd * gd)
                Kagree = K // Kswitch
                assert gcd(Kswitch, Kagree) == 1 and Kswitch * Kagree == K

                for prime in factor(K):
                    in_i, in_j = di % prime == 0, dj % prime == 0
                    assert (Kswitch % prime == 0) == (in_i != in_j)
                    assert (Kagree % prime == 0) == (in_i == in_j)

                lam, mod = 0, 1
                for prime in factor(K):
                    sign = -1 if Kswitch % prime == 0 else 1
                    t = ((sign - lam) * pow(mod, -1, prime)) % prime
                    lam = (lam + mod * t) % (mod * prime)
                    mod *= prime
                if K > 1:
                    assert mod == K and (lam * lam - 1) % K == 0
                    assert (y["Pplus"] * x["Pminus"] - lam * x["Pplus"] * y["Pminus"]) % K == 0
                orientation_hist[lam] += 1
                pair_tag_checks += 1

                if x["beta"] == y["beta"]:
                    assert Kswitch == 1 and Kagree == K
                    same_tag_checks += 1

    assert private_pairs == 5

    fixed_value_groups = Counter(
        (rec["packet"], rec["kappa"], rec["beta"], rec["Pminus"])
        for rec in records
    )
    max_frozen_fixed_value_multiplicity = max(fixed_value_groups.values(), default=0)

    report = {
        "stage": "14-t73",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "tagged_normal_form_checks": tagged_normal_checks,
        "canonical_filter_checks": canonical_filter_checks,
        "kappa_one_frozen_states": kappa_one_states,
        "private_pair_fixed_tag_orientation_checks": pair_tag_checks,
        "same_denominator_tag_private_pairs": same_tag_checks,
        "kappa_one_exhaustive_factorization_checks": kappa_one_exhaustive_regression(),
        "fixed_norm_small_box_regression_checks": fixed_norm_exhaustive_regression(),
        "max_frozen_fixed_kappa_beta_pminus_multiplicity": max_frozen_fixed_value_multiplicity,
        "most_common_denominator_tags": tag_hist.most_common(12),
        "orientation_histogram_private_pairs": orientation_hist.most_common(12),
        "boundary": {
            "STAGE14_T73": "COMPLETE_KAPPA_ONE_LINEAR_FACTORIZATION_FIXED_TAG_CONDITIONING_AND_UNIFORM_FIXED_NORM_FIBER_REDUCTION",
            "TAGGED_NORMAL_FORM_PROVED": True,
            "KAPPA_ONE_PELL_ORBIT_EXISTS": False,
            "KAPPA_ONE_COPRIME_LINEAR_FACTORIZATION_PROVED": True,
            "KAPPA_ONE_FIXED_DENOMINATOR_VALUE_FIBER": "Bo1",
            "DENOMINATOR_TAG_CONDITIONING_COST": "Bo1",
            "FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY": 1,
            "TAG_SWITCH_EQUALS_ODD_SUPPORT_SYMMETRIC_DIFFERENCE": True,
            "UNIFORM_FIXED_NORM_REAL_QUADRATIC_ELEMENT_COUNT": "Bo1",
            "FIXED_KAPPA_BETA_PMINUS_SQUARE_SCALE_FIBER": "Bo1",
            "CLASS_NUMBER_FIXED_NORM_COST": 0,
            "UNIT_ORBIT_FIXED_NORM_COST": "Bo1",
            "REGULATOR_FIXED_POWER_LOSS": 0,
            "SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_MOVING_CANONICAL_NORM_VALUE_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "5/8",
            "T73_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH19_NEEDED": True,
            "TH19_REQUESTED_OBJECT": "SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy",
            "TH19_FIXED_NORM_PELL_ORBIT_SUBPROBLEM_SUPERSEDED": True,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH19": False,
            "NEXT": "Stage14-t74",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
