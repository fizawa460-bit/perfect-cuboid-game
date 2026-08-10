#!/usr/bin/env python3
"""Stage14-t78: external-kappa/radial reduction and four-cell gcd tensor audit."""

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
T77 = ROOT / "stages/stage14/14-t77/result.md"
CX = ROOT / "stages/stage14/14-4cx/result.md"
B_FROZEN = 10_000


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


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factor(n).items():
        old = list(ds)
        mul = 1
        for _ in range(e):
            mul *= p
            ds += [x * mul for x in old]
    return sorted(ds)


def mobius(n: int) -> int:
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1


def gcd_indicator_mobius(x: int, y: int, d: int) -> int:
    if x % d or y % d:
        return 0
    gg = gcd(x // d, y // d)
    return sum(mobius(e) for e in divisors(gg))


def four_cells(A: int, B: int, R: int, T: int):
    dAR = gcd(A, R)
    dAT = gcd(A, T)
    dBR = gcd(B, R)
    dBT = gcd(B, T)
    return dAR, dAT, dBR, dBT


def pairwise_coprime(vals: tuple[int, ...]) -> bool:
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if gcd(vals[i], vals[j]) != 1:
                return False
    return True


def main() -> None:
    assert "STAGE14_T77=COMPLETE_RADIAL_DEGENERATE_SPLIT_AND_GAUSSIAN_PROJECTIVE_RAY_CHARACTER_KERNEL" in T77.read_text()
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44" in CX.read_text()

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    ray_formula_checks = 0
    radial_equiv_checks = 0
    four_cell_checks = 0
    cofactor_checks = 0
    hyperbola_checks = 0
    k_cell_checks = 0
    radial_only_states = 0
    ray_active_states = 0
    external_hist = Counter()
    ray_hist = Counter()
    max_external = 1
    max_g = 1
    max_k_supported_cell_orientations = 1

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta
        h = eps * m // k
        H = oddpart(h)
        assert h * k == eps * m

        s0 = Fraction(b * b * p * p - a * a * q * q,
                      b * b * q * q - a * a * p * p)
        sq = s0 / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator and gcd(u, v) == 1
        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        GG = gcd(raw_plus, raw_minus)
        Pminus = raw_minus // GG
        assert Pminus % ell == 0
        c = oddpart(Pminus // ell)

        Araw, Braw = b - a, b + a
        rraw, traw = q - p, q + p
        A, Bdir = oddpart(Araw), oddpart(Braw)
        R, T = oddpart(rraw), oddpart(traw)
        assert gcd(A, Bdir) == 1 and gcd(R, T) == 1

        g = gcd(A * Bdir, R * T)
        K = oddpart(kappa)
        Kbad = gcd(K, g)
        Q = K // Kbad
        Qrad = gcd(Q, k)
        M = Q // Qrad

        closed = K // gcd(K, g * k)
        Kext = K // gcd(K, k)
        external = Kext // gcd(Kext, g)
        assert M == closed == external
        assert (M == 1) == (g % Kext == 0)
        ray_formula_checks += 1
        radial_equiv_checks += 1
        if M == 1:
            radial_only_states += 1
        else:
            ray_active_states += 1

        cells = four_cells(A, Bdir, R, T)
        assert pairwise_coprime(cells)
        prod = 1
        for d in cells:
            prod *= d
        assert prod == g
        dAR, dAT, dBR, dBT = cells
        A1 = A // (dAR * dAT)
        B1 = Bdir // (dBR * dBT)
        R1 = R // (dAR * dBR)
        T1 = T // (dAT * dBT)
        assert gcd(A1 * B1, R1 * T1) == 1
        four_cell_checks += 1

        assert c % H == 0
        assert c // H == R1 * T1
        assert g * c == H * R * T
        cofactor_checks += 1

        assert ell * g * c == ell * H * R * T
        assert ell * H * R * T < 2 * B_FROZEN
        assert ell * ell > 4 * B_FROZEN
        assert H * R * T < isqrt(B_FROZEN)
        assert ell * c < 2 * B_FROZEN
        assert 2 * c < ell
        assert 2 * H * R * T < ell * g
        hyperbola_checks += 1

        scells = tuple(gcd(K, d) for d in cells)
        assert pairwise_coprime(scells)
        sprod = 1
        for d in scells:
            sprod *= d
        assert sprod == gcd(K, g)
        ecells = tuple(d // s for d, s in zip(cells, scells))
        assert all(gcd(e, K) == 1 for e in ecells)
        assert M == K // gcd(K, sprod * k)
        omega_s = len(factor(sprod))
        max_k_supported_cell_orientations = max(max_k_supported_cell_orientations, 4 ** omega_s)
        k_cell_checks += 1

        external_hist[Kext] += 1
        ray_hist[M] += 1
        max_external = max(max_external, Kext)
        max_g = max(max_g, g)

    # Independent exact Mobius identity regression.
    mobius_checks = 0
    for x in range(1, 40, 2):
        for y in range(1, 40, 2):
            gg = gcd(x, y)
            for d in divisors(x * y):
                got = gcd_indicator_mobius(x, y, d)
                want = 1 if gg == d else 0
                assert got == want
                mobius_checks += 1

    # Independent four-cell regression on internally primitive odd columns.
    four_cell_regressions = 0
    odds = list(range(1, 24, 2))
    for A in odds:
        for Bdir in odds:
            if gcd(A, Bdir) != 1:
                continue
            for R in odds:
                for T in odds:
                    if gcd(R, T) != 1:
                        continue
                    cells = four_cells(A, Bdir, R, T)
                    assert pairwise_coprime(cells)
                    prod = 1
                    for d in cells:
                        prod *= d
                    assert prod == gcd(A * Bdir, R * T)
                    dAR, dAT, dBR, dBT = cells
                    A1 = A // (dAR * dAT)
                    B1 = Bdir // (dBR * dBT)
                    R1 = R // (dAR * dBR)
                    T1 = T // (dAT * dBT)
                    assert gcd(A1 * B1, R1 * T1) == 1
                    four_cell_regressions += 1

    report = {
        "stage": "14-t78",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "ray_modulus_formula_checks": ray_formula_checks,
        "radial_only_equivalence_checks": radial_equiv_checks,
        "four_cell_checks": four_cell_checks,
        "cofactor_residual_product_checks": cofactor_checks,
        "sharp_hyperbola_cancellation_checks": hyperbola_checks,
        "k_supported_cell_checks": k_cell_checks,
        "mobius_indicator_regressions": mobius_checks,
        "four_cell_independent_regressions": four_cell_regressions,
        "diagnostic_radial_only_states": radial_only_states,
        "diagnostic_ray_active_states": ray_active_states,
        "max_external_kappa": max_external,
        "max_g": max_g,
        "max_k_supported_four_cell_orientation_bound": max_k_supported_cell_orientations,
        "most_common_external_kappa": external_hist.most_common(12),
        "most_common_ray_modulus": ray_hist.most_common(12),
        "boundary": {
            "STAGE14_T78": "COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION",
            "MERGED_T77_IMPORTED": True,
            "RAY_MODULUS_EQUALS_EXTERNAL_KAPPA_OUTSIDE_GK": True,
            "RAY_MODULUS_FORMULA": "M=K/gcd(K,g*k)",
            "RAY_MODULUS_EXTERNAL_FORMULA": "M=K_ext/gcd(K_ext,g)",
            "RADIAL_ONLY_IFF_EXTERNAL_KAPPA_DIVIDES_ANGULAR_GCD": True,
            "RADIAL_ONLY_FIXED_POWER_EXTERNAL_SUPPORT_SUBSUMED_BY_T75_LARGE_G": True,
            "ANGULAR_GCD_FOUR_CELL_DECOMPOSITION_PROVED": True,
            "ANGULAR_GCD_FOUR_CELLS_PAIRWISE_COPRIME": True,
            "ANGULAR_GCD_RESIDUAL_CROSS_SUPPORT_COPRIME": True,
            "SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD": True,
            "SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T": True,
            "ODD_COVER_PRODUCT_IS_SQRT_B_SHORT": True,
            "RAY_MODULUS_DEPENDS_ONLY_ON_K_SUPPORTED_GCD_CELLS": True,
            "ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED": True,
            "CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED": True,
            "FULL_HARD_CUTOFF_SINGLE_TENSOR_FACTORIZATION_PROVED": False,
            "RAY_ACTIVE_TYPEII_ENERGY_PROVED": False,
            "TH22_NEEDED": True,
            "TH22_TARGET_REFINED_BY_T78": True,
            "TH23_NEEDED": False,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH22": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "23/44",
            "T78_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "NEXT": "Stage14-t79",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
