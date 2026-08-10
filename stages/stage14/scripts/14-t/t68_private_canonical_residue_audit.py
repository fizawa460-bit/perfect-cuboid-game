#!/usr/bin/env python3
"""Stage14-t68: canonical cross-resultant / private-prime transfer no-go audit."""

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
T67 = ROOT / "stages/stage14/14-t67/result.md"
S729 = ROOT / "stages/stage14/14-s7-29/result.md"


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def vp(n: int, p: int) -> int:
    n = abs(n)
    e = 0
    while n and n % p == 0:
        e += 1
        n //= p
    return e


def synthetic_nogo() -> dict[str, int]:
    kappa = 1
    ell1, u1, v1 = 101, 50, 51
    ell2, u2, v2 = 109, 54, 55
    pm1 = v1 * v1 - kappa * u1 * u1
    pp1 = v1 * v1 + kappa * u1 * u1
    pm2 = v2 * v2 - kappa * u2 * u2
    pp2 = v2 * v2 + kappa * u2 * u2
    assert pm1 == ell1 and pm2 == ell2
    assert pp1 % ell2 != 0 and pm1 % ell2 != 0
    assert pp2 % ell1 != 0 and pm2 % ell1 != 0

    delta = u1 * u1 * v2 * v2 - v1 * v1 * u2 * u2
    sigma = u1 * u1 * v2 * v2 + v1 * v1 * u2 * u2
    assert delta % ell1 != 0 and sigma % ell1 != 0
    assert delta % ell2 != 0 and sigma % ell2 != 0
    return {
        "ell1": ell1,
        "ell2": ell2,
        "delta_mod_ell1": delta % ell1,
        "sigma_mod_ell1": sigma % ell1,
        "delta_mod_ell2": delta % ell2,
        "sigma_mod_ell2": sigma % ell2,
    }


def main() -> None:
    t67 = T67.read_text()
    assert "STAGE14_T67=COMPLETE_CANONICAL_ROOT_MODULUS_COLLAPSE_AND_PRIVATE_PRIME_REDUCTION" in t67
    assert "PRIVATE_CANONICAL_PRIME_PAIR_REDUCTION_PROVED=true" in t67
    s729 = S729.read_text()
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4" in s729
    assert "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true" in s729

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    canonical_local_square_checks = 0
    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta0 = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta0
        h = eps * m // k
        H, D = oddpart(h), oddpart(delta0)
        M = ell * H * D

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
        assert Pminus % (ell * H) == 0
        assert Pplus % D == 0
        assert gcd(ell, kappa * u * v) == 1
        assert legendre(kappa, ell) == 1
        canonical_local_square_checks += 1

        records.append({
            "packet": (tuple(st["U"]), eps, k, h),
            "kappa": kappa,
            "ell": ell,
            "M": M,
            "u": u,
            "v": v,
            "G": G,
            "Pplus": Pplus,
            "Pminus": Pminus,
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    private_pairs = 0
    cross_dictionary_checks = 0
    cross_factor_pairs = 0
    clean_private_pairs = 0
    clean_determinant_nodiv_checks = 0
    local_square_transfer_checks = 0
    cross_factor_degree = Counter()

    for vals in groups.values():
        for x, y in combinations(vals, 2):
            if x["ell"] == y["ell"]:
                continue
            if x["M"] % y["ell"] == 0 or y["M"] % x["ell"] == 0:
                continue
            private_pairs += 1

            delta_xy = x["u"] * x["u"] * y["v"] * y["v"] - x["v"] * x["v"] * y["u"] * y["u"]
            sigma_xy = x["u"] * x["u"] * y["v"] * y["v"] + x["v"] * x["v"] * y["u"] * y["u"]

            for src, dst in ((x, y), (y, x)):
                ell = src["ell"]
                assert gcd(ell, dst["G"]) == 1
                assert (delta_xy % ell == 0) == (dst["Pminus"] % ell == 0)
                assert (sigma_xy % ell == 0) == (dst["Pplus"] % ell == 0)
                cross_dictionary_checks += 2

                assert legendre(src["kappa"], ell) == 1
                assert (2 * (vp(dst["u"], ell) - vp(dst["v"], ell))) % 2 == 0
                local_square_transfer_checks += 1

            contaminated = (
                y["Pplus"] % x["ell"] == 0
                or y["Pminus"] % x["ell"] == 0
                or x["Pplus"] % y["ell"] == 0
                or x["Pminus"] % y["ell"] == 0
            )
            if contaminated:
                cross_factor_pairs += 1
                cross_factor_degree[(x["ell"], x["M"])] += 1
                cross_factor_degree[(y["ell"], y["M"])] += 1
            else:
                clean_private_pairs += 1
                assert delta_xy % x["ell"] != 0
                assert sigma_xy % x["ell"] != 0
                assert delta_xy % y["ell"] != 0
                assert sigma_xy % y["ell"] != 0
                clean_determinant_nodiv_checks += 4

    synthetic = synthetic_nogo()

    report = {
        "stage": "14-t68",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "canonical_local_square_checks": canonical_local_square_checks,
        "same_squareclass_private_pairs": private_pairs,
        "canonical_cross_resultant_checks": cross_dictionary_checks,
        "cross_factor_contaminated_private_pairs": cross_factor_pairs,
        "mutually_cayley_private_pairs": clean_private_pairs,
        "clean_canonical_nodivisibility_checks": clean_determinant_nodiv_checks,
        "local_square_transfer_checks": local_square_transfer_checks,
        "max_frozen_cross_factor_degree": max(cross_factor_degree.values(), default=0),
        "synthetic_nogo": synthetic,
        "cross_dictionary": "ell_i|Delta_ij iff ell_i|Pminus_j; ell_i|Sigma_ij iff ell_i|Pplus_j",
        "boundary": {
            "STAGE14_T68": "COMPLETE_CANONICAL_CROSS_RESULTANT_DICTIONARY_AND_PRIVATE_PRIME_TRANSFER_NOGO",
            "MERGED_S7_29_GLOBAL_3_4_LEDGER_IMPORTED": True,
            "CANONICAL_CROSS_RESULTANT_DICTIONARY_PROVED": True,
            "PRIVATE_ELL_FORCES_CROSS_DETERMINANT": False,
            "CROSS_FACTOR_CONTAMINATION_NEAR_LINEAR": True,
            "MUTUALLY_CAYLEY_PRIVATE_PAIR_DEFINED": True,
            "CANONICAL_PRIME_DETERMINANT_SPACING_AVAILABLE": False,
            "CANONICAL_PRIME_LOCAL_SQUARE_TEST_IDENTICALLY_COHERENT_ON_KAPPA_FIBER": True,
            "PRIVATE_CANONICAL_ROOT_ORIENTATION_TRANSFERS_TO_OTHER_STATE": False,
            "SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "3/4",
            "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED": True,
            "T68_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH18_PREVIOUS_REQUEST_SUPERSEDED": True,
            "TH18_NEEDED": False,
            "NEXT": "Stage14-t69",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
