#!/usr/bin/env python3
"""Stage14-t69: noncanonical Cayley cofactor/common-support audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T65 = ROOT / "stages/stage14/14-t65/result.md"
T68 = ROOT / "stages/stage14/14-t68/result.md"
TH18 = ROOT / "stages/stage14/14-tH18/result.md"
MAIN34 = ROOT / "stages/stage14/14-4cp/result.md"


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


def lpf_odd(n: int) -> int:
    return max((p for p in factor(oddpart(n)) if p & 1), default=1)


def pairwise_coprime(xs: list[int]) -> bool:
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if gcd(xs[i], xs[j]) != 1:
                return False
    return True


def synthetic_disjoint_support_guard() -> dict[str, object]:
    kappa = 1
    data = []
    for ell, u, v in ((7, 3, 4), (19, 5, 14)):
        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pplus = raw_plus // G
        Pminus = raw_minus // G
        assert Pminus % ell == 0
        assert factor(Pminus).get(ell, 0) == 1
        assert 2 * (oddpart(Pminus) // ell) < ell
        assert lpf_odd(Pplus * Pminus) == ell
        data.append((ell, u, v, Pplus, Pminus))

    e1, u1, v1, pp1, pm1 = data[0]
    e2, u2, v2, pp2, pm2 = data[1]
    assert e1 != e2
    assert (pp2 * pm2) % e1 != 0
    assert (pp1 * pm1) % e2 != 0
    c1 = oddpart(pp1) * (oddpart(pm1) // e1)
    c2 = oddpart(pp2) * (oddpart(pm2) // e2)
    assert gcd(c1, c2) == 1
    assert Fraction(u1 * u1, v1 * v1) > 0
    assert Fraction(u2 * u2, v2 * v2) > 0
    return {
        "state1": {"ell": e1, "u": u1, "v": v1, "Pplus": pp1, "Pminus": pm1},
        "state2": {"ell": e2, "u": u2, "v": v2, "Pplus": pp2, "Pminus": pm2},
        "common_noncanonical_odd_support": 1,
    }


def main() -> None:
    t65 = T65.read_text()
    t68 = T68.read_text()
    th18 = TH18.read_text()
    main34 = MAIN34.read_text()
    assert "NONCANONICAL_CAYLEY" not in t65  # t69 is the sharpening stage
    assert "STAGE14_T68=COMPLETE_CANONICAL_CROSS_RESULTANT_DICTIONARY_AND_PRIVATE_PRIME_TRANSFER_NOGO" in t68
    assert "STAGE14_TH18=COMPLETE_PRIVATE_CANONICAL_ROOT_MODULUS_LARGE_SIEVE_APPLICABILITY_AUDIT" in th18
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4" in main34

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    angular_factor_checks = 0
    kappa_coprime_checks = 0
    largest_prime_checks = 0
    max_noncanonical_prime_ratio_num = 0
    max_noncanonical_prime_ratio_den = 1

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta0 = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta0
        h = eps * m // k
        H, D = oddpart(h), oddpart(delta0)
        M = ell * H * D
        assert h * k == eps * m
        assert ell > 2 * eps * m * delta0
        assert ell > 2 * m
        assert ell > 2 * n

        A = b * b * p * p - a * a * q * q
        B0 = b * b * q * q - a * a * p * p
        s = Fraction(A, B0)
        kappa = st["kernel"]
        sq = s / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator
        assert gcd(u, v) == 1

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pplus, Pminus = raw_plus // G, raw_minus // G
        assert gcd(Pplus, Pminus) == 1
        assert Pplus > Pminus > 0

        Dpi = b * b - a * a
        DV = q * q - p * p
        assert Dpi > 0 and DV > 0
        g = gcd(oddpart(Dpi), oddpart(DV))
        Rpi = oddpart(Dpi) // g
        RV = oddpart(DV) // g
        assert gcd(Rpi, RV) == 1
        assert oddpart(Pplus) == D * Rpi
        assert oddpart(Pminus) == ell * H * RV
        angular_factor_checks += 1

        assert gcd(Pplus * Pminus, kappa) == 1
        kappa_coprime_checks += 1

        fprod = factor(oddpart(Pplus * Pminus))
        assert fprod.get(ell, 0) == 1
        assert lpf_odd(Pplus * Pminus) == ell
        for r in fprod:
            if r == ell:
                continue
            assert r < ell
            if r * max_noncanonical_prime_ratio_den > max_noncanonical_prime_ratio_num * ell:
                max_noncanonical_prime_ratio_num = r
                max_noncanonical_prime_ratio_den = ell
        largest_prime_checks += 1

        records.append({
            "packet": (tuple(st["U"]), eps, k, h),
            "kappa": kappa,
            "ell": ell,
            "M": M,
            "D": D,
            "H": H,
            "u": u,
            "v": v,
            "Pplus": Pplus,
            "Pminus": Pminus,
            "Cplus": oddpart(Pplus),
            "Cminus": oddpart(Pminus) // ell,
            "Rpi": Rpi,
            "RV": RV,
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    mutually_private_pairs = 0
    common_support_checks = 0
    j_eq_base_pairs = 0
    j_gt_base_pairs = 0
    j_eq_one_pairs = 0
    max_J = 1
    max_extra_common = 1
    J_hist = Counter()
    extra_hist = Counter()

    for vals in groups.values():
        for x, y in combinations(vals, 2):
            if x["ell"] == y["ell"]:
                continue
            if x["M"] % y["ell"] == 0 or y["M"] % x["ell"] == 0:
                continue
            contaminated = (
                y["Pplus"] % x["ell"] == 0
                or y["Pminus"] % x["ell"] == 0
                or x["Pplus"] % y["ell"] == 0
                or x["Pminus"] % y["ell"] == 0
            )
            if contaminated:
                continue

            mutually_private_pairs += 1
            jpp = gcd(x["Cplus"], y["Cplus"])
            jmm = gcd(x["Cminus"], y["Cminus"])
            jpm = gcd(x["Cplus"], y["Cminus"])
            jmp = gcd(x["Cminus"], y["Cplus"])
            js = [jpp, jmm, jpm, jmp]
            assert pairwise_coprime(js)
            J = jpp * jmm * jpm * jmp
            assert J == gcd(x["Cplus"] * x["Cminus"], y["Cplus"] * y["Cminus"])

            base = x["H"] * gcd(x["D"], y["D"])
            assert x["H"] == y["H"]
            assert gcd(x["H"], x["D"] * y["D"]) == 1
            assert jmm % x["H"] == 0
            assert jpp % gcd(x["D"], y["D"]) == 0
            assert J % base == 0
            extra = J // base

            delta_uv = x["v"] * x["v"] * y["u"] * y["u"] - x["u"] * x["u"] * y["v"] * y["v"]
            sigma_uv = x["v"] * x["v"] * y["u"] * y["u"] + x["u"] * x["u"] * y["v"] * y["v"]
            assert delta_uv % (jpp * jmm) == 0
            assert sigma_uv % (jpm * jmp) == 0
            common_support_checks += 1

            if J == base:
                j_eq_base_pairs += 1
            else:
                j_gt_base_pairs += 1
            if J == 1:
                j_eq_one_pairs += 1
            max_J = max(max_J, J)
            max_extra_common = max(max_extra_common, extra)
            J_hist[J] += 1
            extra_hist[extra] += 1

    synthetic = synthetic_disjoint_support_guard()

    report = {
        "stage": "14-t69",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "angular_factorization_checks": angular_factor_checks,
        "reduced_cayley_kappa_coprime_checks": kappa_coprime_checks,
        "full_cayley_largest_prime_checks": largest_prime_checks,
        "mutually_cayley_private_pairs": mutually_private_pairs,
        "common_support_orientation_checks": common_support_checks,
        "pairs_J_equals_radial_base": j_eq_base_pairs,
        "pairs_J_strictly_exceeds_radial_base": j_gt_base_pairs,
        "pairs_J_equals_one": j_eq_one_pairs,
        "max_frozen_J": max_J,
        "max_frozen_extra_common_support": max_extra_common,
        "most_common_J": J_hist.most_common(12),
        "most_common_extra_support": extra_hist.most_common(12),
        "max_noncanonical_prime_over_ell": [max_noncanonical_prime_ratio_num, max_noncanonical_prime_ratio_den],
        "synthetic_disjoint_support_guard": synthetic,
        "boundary": {
            "STAGE14_T69": "COMPLETE_NONCANONICAL_CAYLEY_FACTOR_AND_COMMON_SUPPORT_REDUCTION",
            "NONCANONICAL_CAYLEY_COFACTORS_IDENTIFIED_WITH_ANGULAR_DEFICITS": True,
            "REDUCED_CAYLEY_SUPPORT_COPRIME_TO_KAPPA": True,
            "CANONICAL_ELL_UNIQUE_LARGEST_ODD_PRIME_OF_FULL_CAYLEY_PAIR": True,
            "ALL_NONCANONICAL_ODD_CAYLEY_PRIMES_LT_ELL": True,
            "NONCANONICAL_COMMON_SUPPORT_MODULUS_DEFINED": True,
            "COMMON_H_NEGATIVE_ROOT_MODULUS_RETAINED": True,
            "COMMON_DELTA_GCD_POSITIVE_ROOT_MODULUS_RETAINED": True,
            "NONCANONICAL_COMMON_SUPPORT_RESULTANT_DICTIONARY_PROVED": True,
            "SAME_SQUARECLASS_FORCES_NONTRIVIAL_NONCANONICAL_OVERLAP": False,
            "GENERIC_SMALL_PRIME_OVERLAP_CLOSURE_VALID": False,
            "SHARED_U_PRIVATE_LARGEST_PRIME_CAYLEY_COMMON_MODULUS_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "3/4",
            "T69_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH18_CONSUMED": True,
            "TH19_NEEDED": False,
            "NEXT": "Stage14-t70",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
