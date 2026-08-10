#!/usr/bin/env python3
"""Stage14-t79: principal ray density and active-support deficit audit."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T78 = ROOT / "stages/stage14/14-t78/result.md"
MAINLINE = ROOT / "stages/stage14/14-4cx/result.md"


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


def divisors_squarefree(n: int) -> list[int]:
    ds = [1]
    for p in prime_divisors(n):
        ds += [d * p for d in list(ds)]
    return sorted(ds)


def local_projective_order(p: int) -> int:
    assert p % 2 == 1
    chi4 = 1 if p % 4 == 1 else -1
    return p - chi4


def ray_group_order(M: int) -> int:
    out = 1
    for p in prime_divisors(M):
        out *= local_projective_order(p)
    return out


def support_character_count(M: int, d: int) -> int:
    assert M % d == 0
    out = 1
    for p in prime_divisors(d):
        out *= local_projective_order(p) - 1
    return out


def euler_phi_squarefree(n: int) -> int:
    out = n
    for p in prime_divisors(n):
        out = out // p * (p - 1)
    return out


def main() -> None:
    t78_text = T78.read_text()
    assert "STAGE14_T78=COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION" in t78_text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44" in MAINLINE.read_text()

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    support_partition_checks = 0
    principal_checks = 0
    deficit_checks = 0
    phi_lower_checks = 0
    endpoint_ray_checks = 0
    total_support_strata = 0
    max_omega_M = 0
    max_support_strata = 0
    max_M = 1
    max_Kext = 1
    min_principal_mass = Fraction(1, 1)
    max_principal_mass = Fraction(0, 1)
    min_full_support_mass = Fraction(1, 1)
    max_full_support_mass = Fraction(0, 1)
    M_hist = Counter()
    Kext_hist = Counter()
    omega_hist = Counter()

    for st in invisible:
        a, b, cp, cq = st["a"], st["b"], st["p"], st["q"]
        kappa = st["kernel"]
        n, delta = st["n"], st["delta"]
        k = n // delta

        A, Bdir = b - a, b + a
        r, t = cq - cp, cq + cp
        K = oddpart(kappa)
        g = gcd(oddpart(A * Bdir), oddpart(r * t))
        Kext = K // gcd(K, k)
        M = K // gcd(K, g * k)
        assert M == Kext // gcd(Kext, g)
        assert Kext % M == 0

        G = ray_group_order(M)
        ds = divisors_squarefree(M)
        counts = {d: support_character_count(M, d) for d in ds}
        assert sum(counts.values()) == G
        support_partition_checks += 1

        principal = Fraction(1, G)
        assert counts[1] == 1
        principal_checks += 1

        # Exact support-deficit inequality N_M(d)/|G(M)| <= 1/|G(M/d)|.
        for d in ds:
            e = M // d
            mass = Fraction(counts[d], G)
            bound = Fraction(1, ray_group_order(e))
            assert mass <= bound
            assert ray_group_order(e) >= euler_phi_squarefree(e)
            deficit_checks += 1
            phi_lower_checks += 1

        full_mass = Fraction(counts[M], G)
        assert full_mass <= 1

        # Endpoint implication is exact: M divides K_ext, hence endpoint-small K_ext
        # automatically forces endpoint-small M.  Frozen data only records integer sizes.
        assert Kext % M == 0
        endpoint_ray_checks += 1

        total_support_strata += len(ds)
        max_support_strata = max(max_support_strata, len(ds))
        omega = len(prime_divisors(M))
        max_omega_M = max(max_omega_M, omega)
        max_M = max(max_M, M)
        max_Kext = max(max_Kext, Kext)
        min_principal_mass = min(min_principal_mass, principal)
        max_principal_mass = max(max_principal_mass, principal)
        min_full_support_mass = min(min_full_support_mass, full_mass)
        max_full_support_mass = max(max_full_support_mass, full_mass)
        M_hist[M] += 1
        Kext_hist[Kext] += 1
        omega_hist[omega] += 1

    # Independent finite-group regressions over many squarefree odd moduli.
    independent_moduli = 0
    independent_support_checks = 0
    for M in range(1, 1200, 2):
        fac = factor(M)
        if any(e != 1 for e in fac.values()):
            continue
        independent_moduli += 1
        G = ray_group_order(M)
        total = 0
        for d in divisors_squarefree(M):
            c = support_character_count(M, d)
            total += c
            e = M // d
            assert Fraction(c, G) <= Fraction(1, ray_group_order(e))
            independent_support_checks += 1
        assert total == G

    report = {
        "stage": "14-t79",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "support_partition_checks": support_partition_checks,
        "principal_density_checks": principal_checks,
        "support_deficit_checks": deficit_checks,
        "ray_order_phi_lower_checks": phi_lower_checks,
        "endpoint_ray_implication_checks": endpoint_ray_checks,
        "total_physical_support_strata": total_support_strata,
        "max_support_strata_per_state": max_support_strata,
        "max_omega_M": max_omega_M,
        "max_M": max_M,
        "max_Kext": max_Kext,
        "min_principal_mass": f"{min_principal_mass.numerator}/{min_principal_mass.denominator}",
        "max_principal_mass": f"{max_principal_mass.numerator}/{max_principal_mass.denominator}",
        "min_full_support_mass": f"{min_full_support_mass.numerator}/{min_full_support_mass.denominator}",
        "max_full_support_mass": f"{max_full_support_mass.numerator}/{max_full_support_mass.denominator}",
        "independent_squarefree_moduli": independent_moduli,
        "independent_support_checks": independent_support_checks,
        "most_common_M": M_hist.most_common(12),
        "most_common_Kext": Kext_hist.most_common(12),
        "omega_M_histogram": sorted(omega_hist.items()),
        "boundary": {
            "STAGE14_T79": "COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION",
            "MERGED_T78_IMPORTED": True,
            "PROJECTIVE_CHARACTER_ACTIVE_SUPPORT_DECOMPOSITION_PROVED": True,
            "PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY": True,
            "PRINCIPAL_RAY_CHARACTER_REQUIRES_LARGE_SIEVE": False,
            "FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED": True,
            "SUPPORT_DEFICIT_NORMALIZED_MASS_BOUND": "E^-1*Bo1",
            "HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT": True,
            "ENDPOINT_SMALL_EXTERNAL_KAPPA_IMPLIES_ENDPOINT_SMALL_RAY_GROUP": True,
            "ENDPOINT_SMALL_RAY_GROUP_CHARACTER_ENUMERATION_COST": "Bo1",
            "ENDPOINT_SMALL_EXTERNAL_KAPPA_PHYSICAL_ENERGY_PROVED": False,
            "RAY_ACTIVE_NEAR_FULL_SUPPORT_HYBRID_ENERGY_PROVED": False,
            "TH22_NEEDED": True,
            "TH22_PR_MERGED_AT_T79_START": False,
            "TH23_NEEDED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "23/44",
            "T79_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "NEXT": "Stage14-t80",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
