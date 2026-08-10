#!/usr/bin/env python3
"""Stage14-t71: physical Gaussian angular chart / kappa four-cell transfer audit."""

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
T70 = ROOT / "stages/stage14/14-t70/result.md"
S731 = ROOT / "stages/stage14/14-s7-31/result.md"


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


def vp(n: int, p: int) -> int:
    n = abs(n)
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def pairwise_coprime(xs: list[int]) -> bool:
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if gcd(xs[i], xs[j]) != 1:
                return False
    return True


def gaussian_mul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def gaussian_conj(z: tuple[int, int]) -> tuple[int, int]:
    return z[0], -z[1]


def synthetic_split_switch_guard() -> dict[str, object]:
    kappa = 15
    states = []
    for N, D in ((4, 1), (17, 7)):
        assert gcd(N, D) == 1 and N > D > 0
        s = Fraction(N - D, N + D)
        q = s / kappa
        ur, vr = isqrt(q.numerator), isqrt(q.denominator)
        assert ur * ur == q.numerator and vr * vr == q.denominator
        d0 = gcd(N - D, N + D)
        aa, bb = (N - D) // d0, (N + D) // d0
        alpha, beta = squarefree_kernel(aa), squarefree_kernel(bb)
        assert alpha * beta == kappa
        states.append({"N": N, "D": D, "s": str(s), "alpha": alpha, "beta": beta})

    x, y = states
    cells = [
        gcd(x["alpha"], y["alpha"]),
        gcd(x["alpha"], y["beta"]),
        gcd(x["beta"], y["alpha"]),
        gcd(x["beta"], y["beta"]),
    ]
    assert pairwise_coprime(cells)
    prod = 1
    for z in cells:
        prod *= z
    assert prod == kappa
    Kagree = cells[0] * cells[3]
    Kswitch = cells[1] * cells[2]
    assert Kagree == 1 and Kswitch == 15
    assert gcd(x["N"] * x["D"], y["N"] * y["D"]) == 1
    return {
        "kappa": kappa,
        "state1": x,
        "state2": y,
        "cells": cells,
        "K_agree": Kagree,
        "K_switch": Kswitch,
        "cayley_common_support": 1,
    }


def main() -> None:
    t70 = T70.read_text()
    s731 = S731.read_text()
    assert "STAGE14_T70=COMPLETE_FULL_COMMON_SUPPORT_CRT_ROOTLINE_AND_SMALL_OVERLAP_REDUCTION" in t70
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8" in s731
    assert "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true" in s731

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    angular_checks = 0
    gaussian_component_checks = 0
    cancellation_matrix_checks = 0
    signed_split_checks = 0
    private_root_checks = 0
    max_split_tau = 0

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta0 = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        U = tuple(st["U"])
        k = n // delta0
        h = eps * m // k
        H, Drad = oddpart(h), oddpart(delta0)
        M = ell * H * Drad

        assert 0 < a < b and 0 < p < q
        A, B = b - a, b + a
        X, Y = q - p, q + p
        assert A > 0 and B > 0 and X > 0 and Y > 0
        assert A * A + B * B == 2 * ell * m
        assert X * X + Y * Y == 2 * k * delta0
        assert gcd(A, B) <= 2 and gcd(X, Y) <= 2

        ur, ui = U
        pc_num = a * ur + b * ui
        pd_num = b * ur - a * ui
        assert pc_num % m == 0 and pd_num % m == 0
        pc, pd = pc_num // m, pd_num // m
        assert pc * pc + pd * pd == ell
        assert gaussian_mul((pc, pd), U) == (a, b)
        assert A == (ui - ur) * pc + (ur + ui) * pd
        assert B == (ur + ui) * pc + (ur - ui) * pd
        determinant = (ui - ur) * (ur - ui) - (ur + ui) * (ur + ui)
        assert determinant == -2 * m
        assert gaussian_mul((-1, 1), gaussian_conj((a, b))) == (A, B)
        assert gaussian_mul((-1, 1), gaussian_conj((p, q))) == (X, Y)
        angular_checks += 1

        L1 = A * Y - B * X
        L2 = B * Y - A * X
        L3 = A * Y + B * X
        L4 = B * Y + A * X
        assert L1 == 2 * (b * p - a * q)
        assert L2 == 2 * (a * q + b * p)
        assert L3 == 2 * (b * q - a * p)
        assert L4 == 2 * (b * q + a * p)
        assert min(L1, L2, L3, L4) > 0
        assert gaussian_mul((2 * a, 2 * b), (p, q)) == (-L3, L2)
        assert gaussian_mul((2 * a, -2 * b), (p, q)) == (L4, -L1)
        assert L2 * L2 + L3 * L3 == 4 * ell * m * k * delta0
        assert L1 * L1 + L4 * L4 == 4 * ell * m * k * delta0

        s = Fraction(L1 * L2, L3 * L4)
        s0 = Fraction(b * b * p * p - a * a * q * q, b * b * q * q - a * a * p * p)
        assert s == s0 and 0 < s < 1
        assert Fraction(1 + s, 1 - s) == Fraction(A * B * (X * X + Y * Y), X * Y * (A * A + B * B))
        kappa = st["kernel"]
        assert squarefree_kernel(L1 * L2 * L3 * L4) == kappa
        gaussian_component_checks += 1

        oA, oB, oX, oY = map(oddpart, (A, B, X, Y))
        assert gcd(oA, oB) == 1 and gcd(oX, oY) == 1
        gAX, gAY = gcd(oA, oX), gcd(oA, oY)
        gBX, gBY = gcd(oB, oX), gcd(oB, oY)
        gcells = [gAX, gAY, gBX, gBY]
        assert pairwise_coprime(gcells)
        gcross = gcd(oA * oB, oX * oY)
        assert gAX * gAY * gBX * gBY == gcross
        assert oddpart(gcd(L1, L3)) == gAX * gBY
        assert oddpart(gcd(L2, L4)) == gAY * gBX
        cancellation_matrix_checks += 1

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
        assert gcd(A0, B0) == 1
        alpha, beta = squarefree_kernel(A0), squarefree_kernel(B0)
        assert gcd(alpha, beta) == 1 and alpha * beta == kappa
        rr2, tt2 = A0 // alpha, B0 // beta
        rr, tt = isqrt(rr2), isqrt(tt2)
        assert rr * rr == rr2 and tt * tt == tt2
        assert gcd(rr, tt) == 1
        eta = 2 // d0
        assert eta * Pplus == alpha * rr * rr + beta * tt * tt
        assert eta * Pminus == beta * tt * tt - alpha * rr * rr
        assert Pminus % ell == 0
        assert gcd(ell, kappa * rr * tt) == 1
        assert (beta * tt * tt - alpha * rr * rr) % ell == 0
        signed_split_checks += 1
        private_root_checks += 1
        max_split_tau = max(max_split_tau, len(factor(kappa)))

        records.append({
            "packet": (tuple(st["U"]), eps, k, h),
            "kappa": kappa,
            "ell": ell,
            "M": M,
            "Pplus": Pplus,
            "Pminus": Pminus,
            "Cplus": oddpart(Pplus),
            "Cminus": oddpart(Pminus) // ell,
            "alpha": alpha,
            "beta": beta,
            "L": (L1, L2, L3, L4),
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    private_pairs = 0
    four_cell_checks = 0
    j_kappa_coprime_checks = 0
    component_transfer_checks = 0
    cell_hist = Counter()
    agree_switch_hist = Counter()
    kappa_hist = Counter()
    pair_profiles = []

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

            private_pairs += 1
            J = gcd(x["Cplus"] * x["Cminus"], y["Cplus"] * y["Cminus"])
            kappa = x["kappa"]
            assert kappa == y["kappa"]
            assert gcd(J, kappa) == 1
            j_kappa_coprime_checks += 1

            Kmm = gcd(x["alpha"], y["alpha"])
            Kmp = gcd(x["alpha"], y["beta"])
            Kpm = gcd(x["beta"], y["alpha"])
            Kpp = gcd(x["beta"], y["beta"])
            cells = [Kmm, Kmp, Kpm, Kpp]
            assert pairwise_coprime(cells)
            prod = 1
            for cell in cells:
                prod *= cell
            assert prod == kappa
            Kagree = Kmm * Kpp
            Kswitch = Kmp * Kpm
            assert Kagree * Kswitch == kappa
            assert max(Kagree, Kswitch) * max(Kagree, Kswitch) >= kappa
            assert max(cells) ** 4 >= kappa
            four_cell_checks += 1

            # Refine each squarefree cell into concrete Gaussian component pairs.
            # numerator side -> L1,L2 ; denominator side -> L3,L4.
            side_indices = {"m": (0, 1), "p": (2, 3)}
            primary = [
                ("m", "m", Kmm),
                ("m", "p", Kmp),
                ("p", "m", Kpm),
                ("p", "p", Kpp),
            ]
            refined_nontrivial = 0
            for sx, sy, Kcell in primary:
                sub = defaultdict(lambda: 1)
                for prime in factor(Kcell):
                    ix = next(idx for idx in side_indices[sx] if x["L"][idx] % prime == 0)
                    iy = next(idx for idx in side_indices[sy] if y["L"][idx] % prime == 0)
                    sub[(ix, iy)] *= prime
                subprod = 1
                for (ix, iy), mod in sub.items():
                    subprod *= mod
                    assert x["L"][ix] % mod == 0
                    assert y["L"][iy] % mod == 0
                    if mod > 1:
                        refined_nontrivial += 1
                        component_transfer_checks += 1
                assert subprod == Kcell

            cell_hist[tuple(cells)] += 1
            agree_switch_hist[(Kagree, Kswitch)] += 1
            kappa_hist[kappa] += 1
            pair_profiles.append({
                "kappa": kappa,
                "J": J,
                "cells": cells,
                "K_agree": Kagree,
                "K_switch": Kswitch,
                "refined_nontrivial_component_cells": refined_nontrivial,
            })

    synthetic = synthetic_split_switch_guard()

    report = {
        "stage": "14-t71",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "angular_gaussian_linearization_checks": angular_checks,
        "gaussian_component_identity_checks": gaussian_component_checks,
        "angular_cancellation_matrix_checks": cancellation_matrix_checks,
        "signed_squareclass_split_checks": signed_split_checks,
        "private_ell_signed_split_root_checks": private_root_checks,
        "max_frozen_omega_kappa": max_split_tau,
        "mutually_cayley_private_pairs": private_pairs,
        "same_kappa_four_cell_checks": four_cell_checks,
        "J_kappa_coprime_checks": j_kappa_coprime_checks,
        "gaussian_component_transfer_checks": component_transfer_checks,
        "kappa_histogram": sorted(kappa_hist.items()),
        "four_cell_histogram": [[list(k), v] for k, v in sorted(cell_hist.items())],
        "agree_switch_histogram": [[list(k), v] for k, v in sorted(agree_switch_hist.items())],
        "pair_profiles": pair_profiles,
        "synthetic_split_switch_guard": synthetic,
        "boundary": {
            "STAGE14_T71": "COMPLETE_PHYSICAL_GAUSSIAN_ANGULAR_AND_SQUARECLASS_FOUR_CELL_TRANSFER_REDUCTION",
            "MERGED_T70_IMPORTED": True,
            "MERGED_S7_31_GLOBAL_5_8_LEDGER_IMPORTED": True,
            "FIXED_U_DIRECTION_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED": True,
            "DIRECTION_ANGULAR_MAP_DETERMINANT": "-2m",
            "COVER_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED": True,
            "ANGULAR_CAYLEY_RATIO_IDENTITY_PROVED": True,
            "PHYSICAL_KUMMER_FACTORS_ARE_GAUSSIAN_PRODUCT_COMPONENTS": True,
            "GAUSSIAN_COMPONENT_NORM_IDENTITY_PROVED": True,
            "KAPPA_EQUALS_FOUR_GAUSSIAN_COMPONENT_SQUAREFREE_KERNEL": True,
            "T65_CROSS_GCD_ANGULAR_2X2_DECOMPOSITION_PROVED": True,
            "ANGULAR_CANCELLATION_COMPONENT_DICTIONARY_PROVED": True,
            "CAYLEY_SIGNED_SQUARECLASS_SPLIT_PROVED": True,
            "CAYLEY_SIGNED_SPLIT_MULTIPLICITY": "Bo1",
            "PRIVATE_ELL_SIGNED_SPLIT_ROOT_CONGRUENCE_PROVED": True,
            "SAME_KAPPA_CAYLEY_SIGNED_FOUR_CELL_DECOMPOSITION_PROVED": True,
            "KAPPA_AGREE_SWITCH_PRODUCT_IDENTITY_PROVED": True,
            "KAPPA_FOUR_CELL_REFINES_TO_GAUSSIAN_COMPONENT_TRANSFER": True,
            "GAUSSIAN_COMPONENT_TRANSFER_ORIENTATION_MULTIPLICITY": "Bo1",
            "CAYLEY_COMMON_SUPPORT_AND_KAPPA_TRANSFER_COPRIME": True,
            "SMALL_J_DOES_NOT_ERASE_KAPPA_COMPONENT_TRANSFER": True,
            "SHARED_U_SMALL_CAYLEY_SUPPORT_GAUSSIAN_SQUARECLASS_FOUR_CELL_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "5/8",
            "T71_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH19_NEEDED": False,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH19": False,
            "NEXT": "Stage14-t72",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
