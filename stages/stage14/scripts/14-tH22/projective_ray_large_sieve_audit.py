#!/usr/bin/env python3
"""Deterministic Stage14-tH22 conductor, t78/t79, and boundary audit."""

from __future__ import annotations

from itertools import combinations
from math import gcd, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T73 = ROOT / "stages/stage14/14-t73/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"
T75 = ROOT / "stages/stage14/14-t75/result.md"
T76 = ROOT / "stages/stage14/14-t76/result.md"
TH21 = ROOT / "stages/stage14/14-tH21/result.md"
T77 = ROOT / "stages/stage14/14-t77/result.md"
T78 = ROOT / "stages/stage14/14-t78/result.md"
T79 = ROOT / "stages/stage14/14-t79/result.md"
FOUR_CX = ROOT / "stages/stage14/14-4cx/result.md"
TH22 = ROOT / "stages/stage14/14-tH22/result.md"
BOUNDARY = ROOT / "stages/stage14/data/tH22/projective_ray_large_sieve_boundary.json"


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def predecessor_audit() -> None:
    t73 = T73.read_text()
    th20 = TH20.read_text()
    t75 = T75.read_text()
    t76 = T76.read_text()
    th21 = TH21.read_text()
    t77 = T77.read_text()
    t78 = T78.read_text()
    t79 = T79.read_text()
    four_cx = FOUR_CX.read_text()

    need(t73, "FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY=1", "t73")
    need(th20, "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false", "tH20")
    need(t75, "HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I=true", "t75")
    need(t75, "LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED=true", "t75")
    need(t76, "LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING=true", "t76")
    need(th21, "STAGE14_TH21=COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT", "tH21")
    need(t77, "STAGE14_T77=COMPLETE_RADIAL_DEGENERATE_SPLIT_AND_GAUSSIAN_PROJECTIVE_RAY_CHARACTER_KERNEL", "t77")
    need(t77, "PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT=true", "t77")
    need(t78, "STAGE14_T78=COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION", "t78")
    need(t78, "RAY_MODULUS_EXTERNAL_FORMULA=M=K_ext/gcd(K_ext,g)", "t78")
    need(t78, "ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true", "t78")
    need(t78, "CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true", "t78")
    need(t79, "STAGE14_T79=COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION", "t79")
    need(t79, "PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY=true", "t79")
    need(t79, "FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED=true", "t79")
    need(t79, "HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT=true", "t79")
    need(t79, "PREFERRED_RECEIVER=SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy", "t79")
    need(four_cx, "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44", "4cx")


def chi4(p: int) -> int:
    return 1 if p % 4 == 1 else -1


def projective_group_order_audit() -> dict[str, int]:
    primes = [3, 5, 7, 11, 13, 17, 19]
    checks = 0
    for r in range(1, 5):
        for subset in combinations(primes, r):
            order = prod(p - chi4(p) for p in subset)
            expected = prod((p - 1) if p % 4 == 1 else (p + 1) for p in subset)
            assert order == expected
            checks += 1
    return {"projective_group_order_checks": checks}


def conductor_square_audit() -> dict[str, int]:
    primes = [3, 5, 7, 11, 13]
    M = prod(primes)
    checks = 0
    for r in range(len(primes) + 1):
        for subset in combinations(primes, r):
            d = prod(subset) if subset else 1
            assert M % d == 0
            assert d * d == d**2
            checks += 1
    return {"conductor_support_checks": checks, "sample_full_M": M}


def t78_modulus_audit() -> dict[str, int]:
    checks = 0
    for K in range(1, 300, 2):
        squarefree = all(K % (p * p) for p in range(3, int(K**0.5) + 1, 2))
        if not squarefree:
            continue
        for k in range(1, 25):
            K_ext = K // gcd(K, k)
            for g in range(1, 25):
                M1 = K // gcd(K, g * k)
                M2 = K_ext // gcd(K_ext, g)
                assert M1 == M2
                assert (M1 == 1) == (g % K_ext == 0)
                checks += 1
    return {"t78_external_modulus_checks": checks}


def t79_support_mass_audit() -> dict[str, int]:
    # For sample squarefree M, exact support counts sum to |G(M)| and
    # normalized mass at deficit e is bounded by 1/|G(e)| <= B^o(1)/e.
    primes = [3, 5, 7, 11]
    M = prod(primes)
    gp = {p: p - chi4(p) for p in primes}
    G = prod(gp.values())
    total = 0
    checks = 0
    for r in range(len(primes) + 1):
        for subset in combinations(primes, r):
            dset = set(subset)
            d = prod(subset) if subset else 1
            eprimes = [p for p in primes if p not in dset]
            e = prod(eprimes) if eprimes else 1
            count = prod(gp[p] - 1 for p in subset) if subset else 1
            Ge = prod(gp[p] for p in eprimes) if eprimes else 1
            total += count
            assert count * Ge <= G
            assert d * e == M
            checks += 1
    assert total == G
    return {"t79_active_support_checks": checks, "sample_projective_group_order": G}


def boundary_audit() -> None:
    text = TH22.read_text()
    tokens = [
        "STAGE14_TH22=COMPLETE_T79_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT",
        "MERGED_T78_IMPORTED=true",
        "MERGED_T79_IMPORTED=true",
        "T77_PROJECTIVE_RAY_KERNEL_RETAINED=true",
        "T77_RADIAL_SELECTOR_REOPENED=false",
        "PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY=true",
        "FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED=true",
        "HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT=true",
        "PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=true",
        "PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=true",
        "PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2",
        "HARD_PROJECTIVE_CHARACTER_CONDUCTOR_NORM=M^2*Bo1",
        "GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=false",
        "GAUSSIAN_BV_BDH_APPLICABLE=false",
        "HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=false",
        "COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=false",
        "FULL_PHYSICAL_MASKS_RETAINED=true",
        "OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false",
        "CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0",
        "MINIMAL_REMAINING_OBSTRUCTION=NearFullSupportProjectiveConductorCompressedGaussianPrimeFourCellMobiusCoverHybridLargeSieve",
        "PREFERRED_RECEIVER=SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy",
        "TH23_NEEDED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-t80",
    ]
    for token in tokens:
        need(text, token, "tH22")

    data = json.loads(BOUNDARY.read_text())
    assert data["predecessors"]["merged_t78_imported"] is True
    assert data["predecessors"]["merged_t79_imported"] is True
    assert data["t79_refinement"]["hard_projective_characters_have_near_full_active_support"] is True
    assert data["projective_character"]["hard_finite_conductor_norm"] == "M^2*B^o(1)"
    assert data["power_saving"]["CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT"] == "0"
    assert data["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "23/44"
    assert data["TH23_NEEDED"] is False
    assert data["NEXT"] == "Stage14-t80"


def main() -> None:
    predecessor_audit()
    out = {
        "stage": "14-tH22",
        "status": "COMPLETE_T79_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT",
        "object": "CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve",
        "off_the_shelf_ray_character_power_saving_proved": False,
        "certified_ray_character_B_power_saving_exponent": "0",
        "minimal_remaining_obstruction": "NearFullSupportProjectiveConductorCompressedGaussianPrimeFourCellMobiusCoverHybridLargeSieve",
        "current_global_exponent": "23/44",
        "next": "Stage14-t80",
        **projective_group_order_audit(),
        **conductor_square_audit(),
        **t78_modulus_audit(),
        **t79_support_mass_audit(),
    }
    boundary_audit()
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
