#!/usr/bin/env python3
"""Stage14-t70: full common-support CRT root-line / small-J audit."""

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
T69 = ROOT / "stages/stage14/14-t69/result.md"
TH18 = ROOT / "stages/stage14/14-tH18/result.md"
S730 = ROOT / "stages/stage14/14-s7-30/result.md"


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
    return all(gcd(xs[i], xs[j]) == 1 for i in range(len(xs)) for j in range(i + 1, len(xs)))


def prime_powers(n: int) -> list[int]:
    return [p**e for p, e in factor(n).items() if p & 1]


def crt(residues: list[tuple[int, int]]) -> tuple[int, int]:
    x, mod = 0, 1
    for a, q in residues:
        assert gcd(mod, q) == 1
        t = ((a - x) * pow(mod, -1, q)) % q
        x += mod * t
        mod *= q
        x %= mod
    return x, mod


def synthetic_small_j_clique() -> dict[str, object]:
    kappa = 1
    raw = [
        (7, 3, 4),
        (19, 5, 14),
        (41, 20, 21),
        (47, 12, 35),
        (127, 42, 85),
        (151, 60, 91),
    ]
    states = []
    for ell, u, v in raw:
        assert gcd(u, v) == 1
        rp = v * v + kappa * u * u
        rm = v * v - kappa * u * u
        G = gcd(rp, rm)
        pp, pm = rp // G, rm // G
        assert gcd(pp, pm) == 1
        assert pm % ell == 0
        assert factor(pm).get(ell, 0) == 1
        assert lpf_odd(pp * pm) == ell
        assert 2 * (oddpart(pm) // ell) < ell
        c = oddpart(pp) * (oddpart(pm) // ell)
        states.append({"ell": ell, "u": u, "v": v, "Pplus": pp, "Pminus": pm, "C": c})

    pair_checks = 0
    for x, y in combinations(states, 2):
        assert gcd(x["C"], y["C"]) == 1
        assert (y["Pplus"] * y["Pminus"]) % x["ell"] != 0
        assert (x["Pplus"] * x["Pminus"]) % y["ell"] != 0
        pair_checks += 1
    assert pair_checks == 15
    return {"size": len(states), "pairwise_J_one_pairs": pair_checks, "states": states}


def exhaustive_rootline_regression() -> int:
    checks = 0
    for Q in range(3, 42, 2):
        for r in range(1, Q):
            if gcd(r, Q) != 1:
                continue
            for U in (5, 8, 11, 14):
                for V in (5, 9, 13):
                    pts = [
                        (u, v)
                        for u in range(1, U + 1)
                        for v in range(1, V + 1)
                        if gcd(u, v) == 1 and (v - r * u) % Q == 0
                    ]
                    # Integer-safe form of N <= 1 + 6 U V / Q.
                    assert max(0, len(pts) - 1) * Q <= 6 * U * V
                    # Direct determinant divisibility for every pair on the line.
                    for x, y in combinations(pts, 2):
                        assert (x[0] * y[1] - x[1] * y[0]) % Q == 0
                    checks += 1
    return checks


def main() -> None:
    t69 = T69.read_text()
    th18 = TH18.read_text()
    s730 = S730.read_text()
    assert "STAGE14_T69=COMPLETE_NONCANONICAL_CAYLEY_FACTOR_AND_COMMON_SUPPORT_REDUCTION" in t69
    assert "STAGE14_TH18=COMPLETE_PRIVATE_CANONICAL_ROOT_MODULUS_LARGE_SIEVE_APPLICABILITY_AUDIT" in th18
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/16" in s730

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta0 = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta0
        h = eps * m // k
        H, D = oddpart(h), oddpart(delta0)
        Mroot = ell * H * D

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
        Cplus = oddpart(Pplus)
        Cminus = oddpart(Pminus) // ell
        assert gcd(Cplus * Cminus, kappa * u * v) == 1

        records.append({
            "packet": (tuple(st["U"]), eps, k, h),
            "kappa": kappa,
            "ell": ell,
            "Mroot": Mroot,
            "D": D,
            "H": H,
            "u": u,
            "v": v,
            "Pplus": Pplus,
            "Pminus": Pminus,
            "Cplus": Cplus,
            "Cminus": Cminus,
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    private_pairs = 0
    crt_rootline_checks = 0
    same_sign_local_checks = 0
    opposite_sign_local_checks = 0
    max_orientation_upper = 1
    max_frozen_J = 1
    max_frozen_area_over_J = Fraction(0, 1)
    J_hist = Counter()
    ratio_hist = Counter()

    for vals in groups.values():
        for x, y in combinations(vals, 2):
            if x["ell"] == y["ell"]:
                continue
            if x["Mroot"] % y["ell"] == 0 or y["Mroot"] % x["ell"] == 0:
                continue
            contaminated = (
                y["Pplus"] % x["ell"] == 0
                or y["Pminus"] % x["ell"] == 0
                or x["Pplus"] % y["ell"] == 0
                or x["Pminus"] % y["ell"] == 0
            )
            if contaminated:
                continue

            private_pairs += 1
            jpp = gcd(x["Cplus"], y["Cplus"])
            jmm = gcd(x["Cminus"], y["Cminus"])
            jpm = gcd(x["Cplus"], y["Cminus"])
            jmp = gcd(x["Cminus"], y["Cplus"])
            comps = [(jpp, +1), (jmm, +1), (jpm, -1), (jmp, -1)]
            assert pairwise_coprime([c for c, _ in comps])
            J = jpp * jmm * jpm * jmp
            assert J == gcd(x["Cplus"] * x["Cminus"], y["Cplus"] * y["Cminus"])

            local = []
            for comp, sign in comps:
                for pe in prime_powers(comp):
                    assert gcd(pe, x["u"] * x["v"] * y["u"] * y["v"] * x["kappa"]) == 1
                    zi = (x["v"] * pow(x["u"], -1, pe)) % pe
                    zj = (y["v"] * pow(y["u"], -1, pe)) % pe
                    lam = (zj * pow(zi, -1, pe)) % pe
                    assert (lam * lam - sign) % pe == 0
                    if sign == +1:
                        assert lam == 1 or lam == pe - 1
                        same_sign_local_checks += 1
                    else:
                        # A root of -1 at an odd prime power forces all underlying primes to be 1 mod 4.
                        for r in factor(pe):
                            assert r % 4 == 1
                        opposite_sign_local_checks += 1
                    local.append((lam, pe))

            lam, mod = crt(local)
            assert mod == J
            if J > 1:
                assert (y["v"] * x["u"] - lam * y["u"] * x["v"]) % J == 0
            crt_rootline_checks += 1

            omega = len(factor(J))
            orientation_upper = 4**omega
            max_orientation_upper = max(max_orientation_upper, orientation_upper)
            # tau(J)^2 dominates 4^omega(J).
            tau = 1
            for e in factor(J).values():
                tau *= e + 1
            assert orientation_upper <= tau * tau

            base = x["H"] * gcd(x["D"], y["D"])
            assert J % base == 0
            extra = J // base
            J_hist[J] += 1
            ratio_hist[extra] += 1
            max_frozen_J = max(max_frozen_J, J)
            area = max(x["u"] * x["v"], y["u"] * y["v"])
            max_frozen_area_over_J = max(max_frozen_area_over_J, Fraction(area, J))

    assert private_pairs == 5
    rootline_regression_checks = exhaustive_rootline_regression()
    clique = synthetic_small_j_clique()

    report = {
        "stage": "14-t70",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "mutually_cayley_private_pairs": private_pairs,
        "crt_rootline_checks": crt_rootline_checks,
        "same_sign_prime_power_orientation_checks": same_sign_local_checks,
        "opposite_sign_prime_power_orientation_checks": opposite_sign_local_checks,
        "primitive_rootline_exhaustive_regression_checks": rootline_regression_checks,
        "max_frozen_orientation_upper_bound": max_orientation_upper,
        "max_frozen_J": max_frozen_J,
        "max_frozen_area_over_J": [max_frozen_area_over_J.numerator, max_frozen_area_over_J.denominator],
        "most_common_J": J_hist.most_common(12),
        "most_common_extra_support": ratio_hist.most_common(12),
        "synthetic_small_J_clique": clique,
        "rootline_bound": "fixed anchor: N_i(J;M) <= (1+M/J) B^o(1)",
        "boundary": {
            "STAGE14_T70": "COMPLETE_FULL_COMMON_SUPPORT_CRT_ROOTLINE_AND_SMALL_OVERLAP_REDUCTION",
            "MERGED_T69_IMPORTED": True,
            "MERGED_TH18_IMPORTED": True,
            "MERGED_S7_30_GLOBAL_11_16_LEDGER_IMPORTED": True,
            "COMMON_SUPPORT_PRIME_POWER_ROOT_ORIENTATION_PROVED": True,
            "OPPOSITE_SIGN_COMMON_SUPPORT_PRIMES_SPLIT_MOD4": True,
            "FOUR_ORIENTATION_COMMON_SUPPORT_CRT_COMPRESSES_TO_ONE_LINEAR_ROOT_LINE": True,
            "COMMON_SUPPORT_ROOT_LINE_MULTIPLICITY": "Bo1",
            "T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED": True,
            "FULL_COMMON_SUPPORT_MUST_BE_USED_BEFORE_RADIAL_UNCHARGING": True,
            "FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND_PROVED": True,
            "FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND": "(1+M/J)*Bo1",
            "LARGE_FULL_COMMON_SUPPORT_ROOTLINE_BRANCH_NEAR_LINEAR": True,
            "LARGE_EXTRA_COMMON_SUPPORT_PARAMETRIC_BOUND_PROVED": True,
            "GENERIC_SMALL_J_CAYLEY_RECONSTRUCTION_VALID": False,
            "SMALL_J_SYNTHETIC_PAIRWISE_DISJOINT_CLIQUE_SIZE": 6,
            "SHARED_U_PRIVATE_LARGEST_PRIME_SMALL_COMMON_SUPPORT_PHYSICAL_SQUARE_SCALE_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "11/16",
            "T70_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH18_CONSUMED": True,
            "TH19_NEEDED": False,
            "NEXT": "Stage14-t71",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
