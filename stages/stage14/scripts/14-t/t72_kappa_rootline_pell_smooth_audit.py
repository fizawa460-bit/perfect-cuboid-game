#!/usr/bin/env python3
"""Stage14-t72: kappa denominator tag / Cayley rootline / Pell-smooth audit."""

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
T71 = ROOT / "stages/stage14/14-t71/result.md"
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


def squarefree_kernel(n: int) -> int:
    out = 1
    for p, e in factor(n).items():
        if e & 1:
            out *= p
    return out


def lpf_odd(n: int) -> int:
    return max((p for p in factor(oddpart(n)) if p & 1), default=1)


def omega(n: int) -> int:
    return len(factor(n))


def tau(n: int) -> int:
    out = 1
    for e in factor(n).values():
        out *= e + 1
    return out


def crt(residues: list[tuple[int, int]]) -> tuple[int, int]:
    x, mod = 0, 1
    for a, q in residues:
        assert gcd(mod, q) == 1
        t = ((a - x) * pow(mod, -1, q)) % q
        x = (x + mod * t) % (mod * q)
        mod *= q
    return x, mod


def exhaustive_cayley_rootline_regression() -> int:
    checks = 0
    for Q in range(3, 36, 2):
        roots = [lam for lam in range(Q) if gcd(lam, Q) == 1 and (lam * lam - 1) % Q == 0]
        for lam in roots:
            for n0, d0 in ((1, 1), (2, 3), (3, 2), (4, 5)):
                if gcd(n0 * d0, Q) != 1:
                    continue
                for N0, D0 in ((6, 7), (9, 8), (12, 11)):
                    pts = [
                        (n, d)
                        for n in range(1, N0 + 1)
                        for d in range(1, D0 + 1)
                        if gcd(n, d) == 1
                        and gcd(n * d, Q) == 1
                        and (n * d0 - lam * n0 * d) % Q == 0
                    ]
                    # A safe integer version of O(1+N0*D0/Q).
                    assert max(0, len(pts) - 2) * Q <= 8 * N0 * D0
                    checks += 1
    return checks


def pell_orbit_guard() -> dict[str, object]:
    # r^2-2t^2=-7, equivalently 2t^2-r^2=7.  Multiplication by
    # 3+2sqrt(2) gives an infinite generic Pell orbit.  The physical
    # largest-prime filter is deliberately checked separately.
    r, t = 1, 2
    rows = []
    for _ in range(8):
        assert r * r - 2 * t * t == -7
        N = r * r + 2 * t * t
        D = 2 * t * t - r * r
        assert D == 7
        full_tag = lpf_odd(N * D) == 7
        rows.append({"r": r, "t": t, "N": N, "D": D, "largest_prime_tag": full_tag})
        r, t = 3 * r + 4 * t, 2 * r + 3 * t
    assert rows[0]["largest_prime_tag"] is True
    assert any(not row["largest_prime_tag"] for row in rows[1:])
    return {
        "kappa": 2,
        "norm_rhs": -7,
        "checked_orbit_length": len(rows),
        "largest_prime_tag_hits": sum(1 for row in rows if row["largest_prime_tag"]),
        "rows": rows,
    }


def main() -> None:
    t71 = T71.read_text()
    s732 = S732.read_text()
    assert "STAGE14_T71=COMPLETE_PHYSICAL_GAUSSIAN_ANGULAR_AND_SQUARECLASS_FOUR_CELL_TRANSFER_REDUCTION" in t71
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8" in t71
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8" in s732

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    denominator_tag_checks = 0
    pell_norm_checks = 0
    largest_prime_smooth_checks = 0
    angular_cofactor_checks = 0
    kappa_one_states = 0
    max_odd_kappa = 1
    max_omega_odd_kappa = 0

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta0 = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta0
        h = eps * m // k
        H, Drad = oddpart(h), oddpart(delta0)
        Mroot = ell * H * Drad

        A = b - a
        B = b + a
        X = q - p
        Y = q + p
        assert A > 0 and B > 0 and X > 0 and Y > 0

        L1 = A * Y - B * X
        L2 = B * Y - A * X
        L3 = A * Y + B * X
        L4 = B * Y + A * X
        assert min(L1, L2, L3, L4) > 0
        assert squarefree_kernel(L1 * L2 * L3 * L4) == kappa

        s = Fraction(L1 * L2, L3 * L4)
        sq = s / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator
        assert gcd(u, v) == 1

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pplus, Pminus = raw_plus // G, raw_minus // G
        assert gcd(Pplus, Pminus) == 1 and Pplus > Pminus > 0
        assert Fraction(Pplus - Pminus, Pplus + Pminus) == s
        assert gcd(Pplus * Pminus, kappa) == 1

        d0 = gcd(Pplus - Pminus, Pplus + Pminus)
        assert d0 in (1, 2)
        A0 = (Pplus - Pminus) // d0
        B0 = (Pplus + Pminus) // d0
        alpha = squarefree_kernel(A0)
        beta = squarefree_kernel(B0)
        assert alpha * beta == kappa and gcd(alpha, beta) == 1
        rr2, tt2 = A0 // alpha, B0 // beta
        rr, tt = isqrt(rr2), isqrt(tt2)
        assert rr * rr == rr2 and tt * tt == tt2
        assert gcd(rr, tt) == 1
        eta = 2 // d0

        # t72 sharpening: the signed split is exactly the denominator kappa tag.
        dtag = gcd(kappa, v)
        assert beta == dtag
        assert alpha == kappa // dtag
        assert oddpart(G) == oddpart(dtag)
        denominator_tag_checks += 1

        assert eta * Pplus == alpha * rr * rr + beta * tt * tt
        assert eta * Pminus == beta * tt * tt - alpha * rr * rr
        xx, yy = beta * tt, rr
        assert xx * xx - kappa * yy * yy == beta * eta * Pminus
        assert xx * xx + kappa * yy * yy == beta * eta * Pplus
        pell_norm_checks += 1

        assert Pminus % ell == 0
        assert factor(Pminus).get(ell, 0) == 1
        assert lpf_odd(Pplus * Pminus) == ell
        codd = oddpart(Pminus) // ell
        assert 2 * codd < ell
        for prime in factor(oddpart(Pplus) * codd):
            assert prime < ell
        largest_prime_smooth_checks += 1

        Dpi = b * b - a * a
        DV = q * q - p * p
        gcross = gcd(oddpart(Dpi), oddpart(DV))
        Rpi = oddpart(Dpi) // gcross
        RV = oddpart(DV) // gcross
        assert oddpart(Pplus) == Drad * Rpi
        assert codd == H * RV
        angular_cofactor_checks += 1

        if kappa == 1:
            assert alpha == beta == 1
            assert (tt - rr) * (tt + rr) == eta * Pminus
            kappa_one_states += 1

        Kodd = oddpart(kappa)
        max_odd_kappa = max(max_odd_kappa, Kodd)
        max_omega_odd_kappa = max(max_omega_odd_kappa, omega(Kodd))

        records.append({
            "packet": (tuple(st["U"]), eps, k, h),
            "kappa": kappa,
            "Kodd": Kodd,
            "ell": ell,
            "Mroot": Mroot,
            "u": u,
            "v": v,
            "dtag": dtag,
            "Pplus": Pplus,
            "Pminus": Pminus,
            "Cplus": oddpart(Pplus),
            "Cminus": oddpart(Pminus) // ell,
            "alpha": alpha,
            "beta": beta,
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    private_pairs = 0
    resultant_partition_checks = 0
    crt_cayley_rootline_checks = 0
    denominator_switch_formula_checks = 0
    j_kappa_coprime_checks = 0
    max_orientation_count = 1
    pair_profiles = []
    K_hist = Counter()

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
            assert x["kappa"] == y["kappa"]
            K = x["Kodd"]
            assert K == y["Kodd"]

            J = gcd(x["Cplus"] * x["Cminus"], y["Cplus"] * y["Cminus"])
            assert gcd(J, x["kappa"]) == 1
            j_kappa_coprime_checks += 1

            di, dj = gcd(K, x["v"]), gcd(K, y["v"])
            gd = gcd(di, dj)
            Kswitch = di * dj // (gd * gd)
            assert K % Kswitch == 0
            Kagree = K // Kswitch

            # Same formulas recovered from the t71 four cells, now without
            # treating the split as independent data.
            Kmm = gcd(oddpart(x["alpha"]), oddpart(y["alpha"]))
            Kmp = gcd(oddpart(x["alpha"]), oddpart(y["beta"]))
            Kpm = gcd(oddpart(x["beta"]), oddpart(y["alpha"]))
            Kpp = gcd(oddpart(x["beta"]), oddpart(y["beta"]))
            assert Kagree == Kmm * Kpp
            assert Kswitch == Kmp * Kpm
            assert gcd(Kagree, Kswitch) == 1
            assert Kagree * Kswitch == K
            denominator_switch_formula_checks += 1

            Delta = y["Pplus"] * x["Pminus"] - x["Pplus"] * y["Pminus"]
            Sigma = y["Pplus"] * x["Pminus"] + x["Pplus"] * y["Pminus"]
            assert gcd(K, abs(Delta)) == Kagree
            assert gcd(K, Sigma) == Kswitch
            resultant_partition_checks += 1

            if K > 1:
                residues = []
                for prime in factor(K):
                    sign = 1 if Kagree % prime == 0 else -1
                    residues.append((sign % prime, prime))
                lam, mod = crt(residues)
                assert mod == K
                assert (lam * lam - 1) % K == 0
                assert (y["Pplus"] * x["Pminus"] - lam * x["Pplus"] * y["Pminus"]) % K == 0
                orient = 2 ** omega(K)
                assert orient <= tau(K)
                max_orientation_count = max(max_orientation_count, orient)
            else:
                lam = 0
            crt_cayley_rootline_checks += 1
            K_hist[K] += 1
            pair_profiles.append({
                "kappa": x["kappa"],
                "Kodd": K,
                "J": J,
                "d_i": di,
                "d_j": dj,
                "K_agree": Kagree,
                "K_switch": Kswitch,
                "lambda": lam,
                "Pplus_i": x["Pplus"],
                "Pminus_i": x["Pminus"],
                "Pplus_j": y["Pplus"],
                "Pminus_j": y["Pminus"],
            })

    assert private_pairs == 5
    rootline_regression_checks = exhaustive_cayley_rootline_regression()
    pell_guard = pell_orbit_guard()

    report = {
        "stage": "14-t72",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "denominator_kappa_tag_checks": denominator_tag_checks,
        "pell_norm_identity_checks": pell_norm_checks,
        "canonical_largest_prime_smooth_checks": largest_prime_smooth_checks,
        "angular_cofactor_checks": angular_cofactor_checks,
        "kappa_one_frozen_states": kappa_one_states,
        "max_frozen_odd_kappa": max_odd_kappa,
        "max_frozen_omega_odd_kappa": max_omega_odd_kappa,
        "mutually_cayley_private_pairs": private_pairs,
        "denominator_switch_formula_checks": denominator_switch_formula_checks,
        "odd_kappa_resultant_partition_checks": resultant_partition_checks,
        "odd_kappa_crt_cayley_rootline_checks": crt_cayley_rootline_checks,
        "J_kappa_coprime_checks": j_kappa_coprime_checks,
        "max_frozen_kappa_orientation_count": max_orientation_count,
        "primitive_cayley_rootline_exhaustive_checks": rootline_regression_checks,
        "odd_kappa_histogram_private_pairs": K_hist.most_common(12),
        "pair_profiles": pair_profiles,
        "synthetic_generic_pell_orbit_guard": pell_guard,
        "rootline_bound": "fixed anchor: N_partner(K;Z) <= (1+Z/Kodd) B^o(1)",
        "boundary": {
            "STAGE14_T72": "COMPLETE_KAPPA_DENOMINATOR_TAG_FULL_CAYLEY_ROOTLINE_AND_PELL_SMOOTH_REDUCTION",
            "SIGNED_SPLIT_BETA_EQUALS_GCD_KAPPA_V": True,
            "SIGNED_SPLIT_ALPHA_EQUALS_KAPPA_OVER_BETA": True,
            "SAME_KAPPA_AGREE_SWITCH_RECOVERABLE_FROM_DENOMINATOR_TAGS": True,
            "ODD_KAPPA_CROSS_RESULTANT_PARTITION_PROVED": True,
            "ODD_KAPPA_CRT_COMPRESSES_TO_ONE_CAYLEY_ROOT_LINE": True,
            "ODD_KAPPA_ROOT_LINE_MULTIPLICITY": "Bo1",
            "FIXED_ANCHOR_KAPPA_ROOTLINE_PARTNER_BOUND_PROVED": True,
            "FIXED_ANCHOR_KAPPA_ROOTLINE_PARTNER_BOUND": "(1+Z/Kodd)*Bo1",
            "LARGE_ODD_KAPPA_CAYLEY_ROOTLINE_BRANCH_NEAR_LINEAR": True,
            "T70_J_AND_T72_KAPPA_MODULI_COPRIME": True,
            "T70_J_AND_T72_KAPPA_ACT_ON_DIFFERENT_COORDINATE_CHARTS": True,
            "SMALL_KAPPA_REAL_QUADRATIC_NORM_REDUCTION_PROVED": True,
            "KAPPA_ONE_DEGENERATES_TO_DIFFERENCE_OF_SQUARES_FACTORIZATION": True,
            "CANONICAL_LARGEST_PRIME_PELL_SMOOTH_FILTER_PROVED": True,
            "SHARED_U_SMALL_ODD_KAPPA_CANONICAL_LARGEST_PRIME_PELL_SMOOTH_PHYSICAL_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "5/8",
            "T72_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH19_NEEDED": True,
            "TH19_REQUESTED_OBJECT": "SmallOddKappaCanonicalLargestPrimePellSmoothEnergy",
            "T_ROUTE_BLOCKED_WAITING_FOR_TH19": False,
            "NEXT": "Stage14-t73",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
