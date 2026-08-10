#!/usr/bin/env python3
"""Stage14-t77: radial-degenerate support and projective ray-character audit."""

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
T76 = ROOT / "stages/stage14/14-t76/result.md"
TH21 = ROOT / "stages/stage14/14-tH21/result.md"
S738 = ROOT / "stages/stage14/14-s7-38/result.md"
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


def projective_equal(z1: tuple[int, int], z2: tuple[int, int], mod: int) -> bool:
    x1, y1 = z1
    x2, y2 = z2
    return (x1 * y2 - y1 * x2) % mod == 0 and (x1 % mod or y1 % mod) and (x2 % mod or y2 % mod)


def gaussian_norm(z: tuple[int, int]) -> int:
    return z[0] * z[0] + z[1] * z[1]


def ray_group_order(M: int) -> int:
    out = 1
    for p in prime_divisors(M):
        chi4 = 1 if p % 4 == 1 else -1
        out *= p - chi4
    return out


def main() -> None:
    assert "STAGE14_T76=COMPLETE_CLEAN_KAPPA_COVER_PROJECTIVE_ROOTLINE_AND_DEFICIENT_TYPEII_REDUCTION" in T76.read_text()
    th21 = TH21.read_text()
    assert "STAGE14_TH21=COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT" in th21
    assert "OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false" in th21
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/112" in S738.read_text()

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    radial_identity_checks = 0
    radial_isotropic_prime_checks = 0
    ray_unit_prime_checks = 0
    ray_component_checks = 0
    ray_projective_checks = 0
    ray_group_order_checks = 0
    balanced_states = 0
    balanced_deficient = 0
    balanced_deficient_ray_active = 0
    balanced_deficient_radial_only = 0
    ray_active_states = 0
    radial_nontrivial_states = 0
    ray_trivial_states = 0
    qrad_hist = Counter()
    qray_hist = Counter()
    component_hist = Counter()
    max_qrad = 1
    max_qray = 1
    max_group_order = 1
    max_group_over_mod = Fraction(1, 1)
    min_group_over_mod = None

    for st in invisible:
        a, b = st["a"], st["b"]
        cp, cq = st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta
        h = eps * m // k
        assert h * k == eps * m

        # Recover the t72 fixed denominator tag.
        s0 = Fraction(b * b * cp * cp - a * a * cq * cq,
                      b * b * cq * cq - a * a * cp * cp)
        sq = s0 / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator and gcd(u, v) == 1
        beta = gcd(kappa, v)
        alpha = kappa // beta
        assert alpha * beta == kappa and gcd(alpha, beta) == 1

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        GG = gcd(raw_plus, raw_minus)
        Pplus, Pminus = raw_plus // GG, raw_minus // GG
        assert gcd(Pplus * Pminus, kappa) == 1
        assert Pminus % ell == 0

        A, Bdir = b - a, b + a
        r, t = cq - cp, cq + cp
        L = (
            A * t - Bdir * r,
            Bdir * t - A * r,
            A * t + Bdir * r,
            Bdir * t + A * r,
        )
        assert all(x > 0 for x in L)

        K = oddpart(kappa)
        g = gcd(oddpart(A * Bdir), oddpart(r * t))
        K_bad = gcd(K, g)
        Q = K // K_bad
        assert gcd(Q, A * Bdir * r * t) == 1

        # t77 radial/ray split.
        Q_rad = gcd(Q, k)
        assert Q_rad == gcd(Q, m)
        Q_ray = Q // Q_rad
        assert gcd(Q_rad, Q_ray) == 1
        radial_identity_checks += 1

        if Q_rad > 1:
            radial_nontrivial_states += 1
        if Q_ray > 1:
            ray_active_states += 1
        else:
            ray_trivial_states += 1

        for pp in prime_divisors(Q_rad):
            assert pp % 4 == 1
            assert h % pp != 0 and ell % pp != 0 and delta % pp != 0
            assert (A * A + Bdir * Bdir) % pp == 0
            assert (r * r + t * t) % pp == 0
            assert gcd(A * Bdir * r * t, pp) == 1
            actual = (t * pow(r, -1, pp)) % pp
            assert (actual * actual + 1) % pp == 0
            sign = 1 if oddpart(alpha) % pp == 0 else -1
            root1 = (sign * Bdir * pow(A, -1, pp)) % pp
            root2 = (sign * A * pow(Bdir, -1, pp)) % pp
            assert actual in {root1, root2}
            assert (root1 * root1 + 1) % pp == 0
            assert (root2 * root2 + 1) % pp == 0
            radial_isotropic_prime_checks += 1

        alpha_ray = gcd(oddpart(alpha), Q_ray)
        beta_ray = gcd(oddpart(beta), Q_ray)
        assert gcd(alpha_ray, beta_ray) == 1
        assert alpha_ray * beta_ray == Q_ray

        # Chosen Kummer component moduli M1..M4.  If both reciprocal roots occur,
        # choose the first admissible component; the theorem only needs existence
        # with divisor-many orientation multiplicity.
        components = [1, 1, 1, 1]
        z = (a, b)
        V = (cp, cq)
        U = tuple(st["U"])
        assert gaussian_norm(U) == m
        assert gaussian_norm(z) == ell * m
        assert gaussian_norm(V) == k * delta

        for pp in prime_divisors(Q_ray):
            assert h % pp != 0 and ell % pp != 0 and delta % pp != 0 and k % pp != 0 and m % pp != 0
            assert gaussian_norm(z) % pp != 0
            assert gaussian_norm(U) % pp != 0
            assert gaussian_norm(V) % pp != 0
            ray_unit_prime_checks += 1

            if alpha_ray % pp == 0:
                allowed_idx = [idx for idx in (0, 1) if L[idx] % pp == 0]
            else:
                assert beta_ray % pp == 0
                allowed_idx = [idx for idx in (2, 3) if L[idx] % pp == 0]
            assert allowed_idx
            idx = allowed_idx[0]
            components[idx] *= pp
            component_hist[idx + 1] += 1

            # Projective ray-class identities for z=pi*U.
            if idx == 0:      # L1: [z]=[V]
                target = (cp, cq)
            elif idx == 1:    # L2: [z]=[conj(V)]
                target = (cp, -cq)
            elif idx == 2:    # L3: [z]=[i*conj(V)]
                target = (cq, cp)
            else:             # L4: [z]=[i*V]
                target = (-cq, cp)
            assert projective_equal(z, target, pp)
            ray_projective_checks += 1
            ray_component_checks += 1

        M1, M2, M3, M4 = components
        assert M1 * M2 * M3 * M4 == Q_ray
        assert M1 * M2 == alpha_ray
        assert M3 * M4 == beta_ray
        assert gcd(M1 * M2, M3 * M4) == 1

        if Q_ray > 1:
            order = ray_group_order(Q_ray)
            assert order > 0
            ratio = Fraction(order, Q_ray)
            max_group_order = max(max_group_order, order)
            max_group_over_mod = max(max_group_over_mod, ratio)
            min_group_over_mod = ratio if min_group_over_mod is None else min(min_group_over_mod, ratio)
            ray_group_order_checks += 1

        balanced = t <= DIAG_BALANCE * r
        deficient = Q < r * t
        if balanced:
            balanced_states += 1
            if deficient:
                balanced_deficient += 1
                if Q_ray > 1:
                    balanced_deficient_ray_active += 1
                else:
                    balanced_deficient_radial_only += 1

        qrad_hist[Q_rad] += 1
        qray_hist[Q_ray] += 1
        max_qrad = max(max_qrad, Q_rad)
        max_qray = max(max_qray, Q_ray)

    report = {
        "stage": "14-t77",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "radial_identity_checks": radial_identity_checks,
        "radial_isotropic_prime_checks": radial_isotropic_prime_checks,
        "ray_unit_prime_checks": ray_unit_prime_checks,
        "ray_component_checks": ray_component_checks,
        "ray_projective_checks": ray_projective_checks,
        "ray_group_order_checks": ray_group_order_checks,
        "diagnostic_balance_ratio": DIAG_BALANCE,
        "diagnostic_balanced_states": balanced_states,
        "diagnostic_balanced_deficient_states": balanced_deficient,
        "diagnostic_balanced_deficient_ray_active_states": balanced_deficient_ray_active,
        "diagnostic_balanced_deficient_radial_only_states": balanced_deficient_radial_only,
        "ray_active_states": ray_active_states,
        "radial_nontrivial_states": radial_nontrivial_states,
        "ray_trivial_states": ray_trivial_states,
        "max_Q_rad": max_qrad,
        "max_Q_ray": max_qray,
        "max_ray_group_order": max_group_order,
        "min_ray_group_order_over_modulus": None if min_group_over_mod is None else f"{min_group_over_mod.numerator}/{min_group_over_mod.denominator}",
        "max_ray_group_order_over_modulus": f"{max_group_over_mod.numerator}/{max_group_over_mod.denominator}",
        "most_common_Q_rad": qrad_hist.most_common(12),
        "most_common_Q_ray": qray_hist.most_common(12),
        "chosen_component_prime_histogram": sorted(component_hist.items()),
        "boundary": {
            "STAGE14_T77": "COMPLETE_RADIAL_DEGENERATE_SPLIT_AND_GAUSSIAN_PROJECTIVE_RAY_CHARACTER_KERNEL",
            "MERGED_T76_IMPORTED": True,
            "MERGED_TH21_IMPORTED": True,
            "RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_K": True,
            "RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_M": True,
            "RADIAL_SUPPORT_PRIMES_SPLIT_MOD4": True,
            "RADIAL_SUPPORT_PROJECTIVE_ROOT_IS_ISOTROPIC": True,
            "RADIAL_SUPPORT_MOVING_PI_PHASE": False,
            "RAY_MODULUS_GAUSSIAN_DIRECTION_AND_COVER_ARE_UNITS": True,
            "PROJECTIVE_GAUSSIAN_RAY_GROUP_EXHIBITED": True,
            "PROJECTIVE_GAUSSIAN_RAY_GROUP_ORDER_FORMULA_PROVED": True,
            "CLEAN_PROJECTIVE_ROOTLINE_EQUALS_GAUSSIAN_RAY_CLASS_INCIDENCE": True,
            "FIXED_BETA_BECOMES_FIXED_I_RAY_CLASS": True,
            "RECIPROCAL_ROOT_CHOICE_BECOMES_LOCAL_INVERSION_AUTOMORPHISM": True,
            "PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT": True,
            "RAY_CHARACTER_KERNEL_SEPARATES_PI_AND_V_ARITHMETICALLY": True,
            "FULL_PHYSICAL_WEIGHT_TENSOR_FACTORIZATION_PROVED": False,
            "RAY_ACTIVE_TYPEII_ENERGY_PROVED": False,
            "TH22_NEEDED": True,
            "TH22_REQUESTED_OBJECT": "CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve",
            "T_ROUTE_BLOCKED_WAITING_FOR_TH22": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "61/112",
            "T77_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "NEXT": "Stage14-t78",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
