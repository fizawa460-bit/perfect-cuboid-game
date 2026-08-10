#!/usr/bin/env python3
"""Deterministic Stage14-tH20 boundary and geometry audit."""

from __future__ import annotations

from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T73 = ROOT / "stages/stage14/14-t73/result.md"
TH19 = ROOT / "stages/stage14/14-t73/th19-consumption.md"
T74 = ROOT / "stages/stage14/14-t74/result.md"
T74_TARGET = ROOT / "stages/stage14/14-t74/th20-target.md"
S736 = ROOT / "stages/stage14/14-s7-36/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def predecessor_audit() -> None:
    t73 = T73.read_text()
    th19 = TH19.read_text()
    t74 = T74.read_text()
    t74_target = T74_TARGET.read_text()
    s736 = S736.read_text()

    need(t73, "FIXED_KAPPA_BETA_PMINUS_SQUARE_SCALE_FIBER=Bo1", "t73")
    need(th19, "STAGE14_TH19=COMPLETE_INDEPENDENT_PELL_SMOOTH_ENERGY_AUDIT", "tH19")
    need(
        t74,
        "STAGE14_T74=COMPLETE_CANONICAL_HOST_ELL_FREE_COFACTOR_BALANCE_AND_SHORT_ANGULAR_COVER_REDUCTION",
        "t74",
    )
    need(t74, "FIXED_TAGGED_PACKET_ELL_C_PHYSICAL_FIBER=Bo1", "t74")
    need(t74, "COVER_LINEAR_FACTORS_LT_SQRT_ELL=true", "t74")
    need(t74, "SHARP_ELL_G_C_HYPERBOLA_PROVED=true", "t74")
    need(
        t74,
        "TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve",
        "t74",
    )
    need(t74_target, "SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve", "t74 target")
    need(s736, "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16", "s7-36")


def short_cover_geometry_audit() -> dict[str, int]:
    checks = 0
    for p in range(1, 80):
        for q in range(p + 1, 100):
            if gcd(p, q) != 1:
                continue
            n = p * p + q * q
            r = q - p
            t = q + p
            assert r * r + t * t == 2 * n
            assert gcd(r, t) in (1, 2)

            ell = 2 * n + 1
            while not is_prime(ell):
                ell += 1
            assert ell > 2 * n
            assert r * r < ell
            assert t * t < ell
            checks += 1
    assert checks > 1000
    return {"short_cover_geometry_checks": checks}


def hyperbola_density_guard() -> dict[str, int]:
    """Diagnostic: ell-prime plus ell*c hyperbola alone is not power sparse."""
    B = 10**6
    lo = 2 * isqrt(B)
    hi = 3 * isqrt(B)
    pairs = 0
    primes = 0
    for ell in range(lo + 1, hi + 1):
        if not is_prime(ell):
            continue
        primes += 1
        cmax = min(isqrt(B) - 1, (2 * B - 1) // ell, (ell - 1) // 2)
        if cmax > 0:
            pairs += cmax
    assert primes > 0
    assert pairs > B // 20
    return {
        "diagnostic_B": B,
        "diagnostic_primes": primes,
        "diagnostic_hyperbola_pairs": pairs,
    }


def boundary_audit() -> None:
    text = TH20.read_text()
    tokens = [
        "STAGE14_TH20=COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT",
        "TH20_CURRENT_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve",
        "FIXED_NORM_PELL_ORBIT_MULTIPLICITY_REOPENED=false",
        "CLASS_NUMBER_REOPENED=false",
        "REGULATOR_REOPENED=false",
        "CANONICAL_LPF_SIEVE_POST_T74_MINIMAL=false",
        "BUCHSTAB_HARMAN_POST_T74_MINIMAL=false",
        "ANGULAR_SHORT_FACTOR_DIVISOR_SWITCHING_VALID=true",
        "SHARP_ELL_C_HYPERBOLA_RETAINED=true",
        "SHARP_ELL_G_C_HYPERBOLA_RETAINED=true",
        "SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true",
        "POST_T74_STANDARD_DISPERSION_DIRECT_IMPORT_VALID=false",
        "PRE_T74_TWO_COMPANION_TYPEII_IS_MINIMAL=false",
        "CERTIFIED_DIRECT_EXTERNAL_SIEVE_B_POWER_SAVING_EXPONENT=0",
        "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=9/16",
        "TH21_NEEDED=false",
        "NEXT=Stage14-t75",
    ]
    for token in tokens:
        need(text, token, "tH20")


def main() -> None:
    predecessor_audit()
    geometry = short_cover_geometry_audit()
    guard = hyperbola_density_guard()
    boundary_audit()
    print(json.dumps({
        "stage": "14-tH20",
        "status": "COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT",
        "object": "SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve",
        "direct_external_fixed_B_power_saving": False,
        "certified_direct_external_sieve_B_power_saving_exponent": "0",
        "preferred_immediate_tool": "angular short-factor divisor switching before external dispersion",
        "possible_future_theorem": "CanonicalPrimeShortPrimitiveCoverBilinearDispersion",
        "current_global_exponent": "9/16",
        "next": "Stage14-t75",
        **geometry,
        **guard,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
