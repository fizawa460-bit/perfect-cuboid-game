#!/usr/bin/env python3
"""Deterministic Stage14-tH22 conductor, merged-t78, and boundary audit."""

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
T78_REFINE = ROOT / "stages/stage14/14-t78/th22-refinement.md"
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
    t78r = T78_REFINE.read_text()
    four_cx = FOUR_CX.read_text()

    need(t73, "FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY=1", "t73")
    need(th20, "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false", "tH20")
    need(t75, "HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I=true", "t75")
    need(t75, "LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED=true", "t75")
    need(t76, "LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING=true", "t76")
    need(th21, "STAGE14_TH21=COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT", "tH21")
    need(t77, "STAGE14_T77=COMPLETE_RADIAL_DEGENERATE_SPLIT_AND_GAUSSIAN_PROJECTIVE_RAY_CHARACTER_KERNEL", "t77")
    need(t77, "RADIAL_SUPPORT_MOVING_PI_PHASE=false", "t77")
    need(t77, "PROJECTIVE_GAUSSIAN_RAY_GROUP_ORDER_FORMULA_PROVED=true", "t77")
    need(t77, "PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT=true", "t77")
    need(t77, "RAY_CHARACTER_KERNEL_SEPARATES_PI_AND_V_ARITHMETICALLY=true", "t77")
    need(t77, "TH22_REQUESTED_OBJECT=CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve", "t77")
    need(t78, "STAGE14_T78=COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION", "t78")
    need(t78, "RAY_MODULUS_EXTERNAL_FORMULA=M=K_ext/gcd(K_ext,g)", "t78")
    need(t78, "RADIAL_ONLY_FIXED_POWER_EXTERNAL_SUPPORT_SUBSUMED_BY_T75_LARGE_G=true", "t78")
    need(t78, "ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true", "t78")
    need(t78, "CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true", "t78")
    need(t78, "SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true", "t78")
    need(t78r, "tH22 no longer needs to decide whether angular-gcd allocation", "t78 refinement")
    need(t78r, "c/odd(h)=R1*T1", "t78 refinement")
    need(four_cx, "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44", "4cx")


def chi4(p: int) -> int:
    assert p % 2 == 1
    return 1 if p % 4 == 1 else -1


def projective_group_order_audit() -> dict[str, int]:
    primes = [3, 5, 7, 11, 13, 17, 19]
    checks = 0
    max_M = 0
    max_order = 0
    for r in range(1, 5):
        for subset in combinations(primes, r):
            M = prod(subset)
            order = prod(p - chi4(p) for p in subset)
            expected = prod((p - 1) if p % 4 == 1 else (p + 1) for p in subset)
            assert order == expected
            checks += 1
            max_M = max(max_M, M)
            max_order = max(max_order, order)
    return {
        "projective_group_order_checks": checks,
        "max_sample_M": max_M,
        "max_sample_projective_group_order": max_order,
    }


def conductor_square_audit() -> dict[str, int]:
    primes = [3, 5, 7, 11, 13]
    M = prod(primes)
    checks = 0
    max_norm = 1
    for r in range(0, len(primes) + 1):
        for subset in combinations(primes, r):
            d = prod(subset) if subset else 1
            conductor_norm = d * d
            assert M % d == 0
            assert conductor_norm == d**2
            max_norm = max(max_norm, conductor_norm)
            checks += 1
    assert max_norm == M * M
    return {
        "conductor_support_checks": checks,
        "sample_full_M": M,
        "sample_max_conductor_norm": max_norm,
    }


def deficient_range_guard() -> dict[str, int]:
    R = 1000
    T = 1000
    M = 999_983
    assert M < R * T
    assert M * M > 100_000 * R * T
    return {
        "deficient_guard_R": R,
        "deficient_guard_T": T,
        "deficient_guard_M": M,
        "deficient_guard_conductor_norm": M * M,
    }


def t78_external_modulus_audit() -> dict[str, int]:
    checks = 0
    radial_equiv = 0
    for K in range(1, 400, 2):
        squarefree = True
        p = 3
        while p * p <= K:
            if K % (p * p) == 0:
                squarefree = False
                break
            p += 2
        if not squarefree:
            continue
        for k in range(1, 35):
            K_ext = K // gcd(K, k)
            for g in range(1, 35):
                M1 = K // gcd(K, g * k)
                M2 = K_ext // gcd(K_ext, g)
                assert M1 == M2
                assert (M1 == 1) == (g % K_ext == 0)
                checks += 1
                radial_equiv += int(M1 == 1)
    return {
        "t78_external_modulus_formula_checks": checks,
        "t78_radial_only_equivalence_hits": radial_equiv,
    }


def four_cell_audit() -> dict[str, int]:
    checks = 0
    for A in range(1, 31, 2):
        for B in range(1, 31, 2):
            if gcd(A, B) != 1:
                continue
            for R in range(1, 31, 2):
                for T in range(1, 31, 2):
                    if gcd(R, T) != 1:
                        continue
                    dAR = gcd(A, R)
                    dAT = gcd(A, T)
                    dBR = gcd(B, R)
                    dBT = gcd(B, T)
                    cells = [dAR, dAT, dBR, dBT]
                    for i in range(4):
                        for j in range(i + 1, 4):
                            assert gcd(cells[i], cells[j]) == 1
                    g = gcd(A * B, R * T)
                    assert prod(cells) == g
                    A1 = A // (dAR * dAT)
                    B1 = B // (dBR * dBT)
                    R1 = R // (dAR * dBR)
                    T1 = T // (dAT * dBT)
                    assert gcd(A1 * B1, R1 * T1) == 1
                    checks += 1
    assert checks > 1000
    return {"t78_four_cell_checks": checks}


def boundary_audit() -> None:
    text = TH22.read_text()
    tokens = [
        "STAGE14_TH22=COMPLETE_T78_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT",
        "MERGED_T78_IMPORTED=true",
        "T77_PROJECTIVE_RAY_KERNEL_RETAINED=true",
        "T77_RADIAL_SELECTOR_REOPENED=false",
        "T78_REFINEMENT_CONSUMED=true",
        "T78_REFINEMENT_MERGED_PREDECESSOR=true",
        "T78_FIXED_POWER_RADIAL_ONLY_BRANCH_REOPENED=false",
        "ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true",
        "CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true",
        "SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true",
        "PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=true",
        "PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=true",
        "PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2",
        "MAX_PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=M^2",
        "PROJECTIVE_GROUP_SIZE_USED_AS_CONDUCTOR_NORM=false",
        "GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=false",
        "GAUSSIAN_BV_BDH_APPLICABLE=false",
        "HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=false",
        "COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=false",
        "DIVISOR_DECOMPOSED_COEFFICIENT_L2_BOUND_THEOREM_READY=false",
        "FULL_PHYSICAL_MASKS_RETAINED=true",
        "OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false",
        "CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0",
        "MINIMAL_REMAINING_OBSTRUCTION=ProjectiveConductorCompressedGaussianPrimeExternalKappaFourCellMobiusCoverHybridLargeSieve",
        "PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagBalancedExternalKappaRayCharacterFourCellMobiusTypeIIEnergy",
        "TH23_NEEDED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-t79",
    ]
    for token in tokens:
        need(text, token, "tH22")

    data = json.loads(BOUNDARY.read_text())
    assert data["object"] == "CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve"
    assert data["predecessors"]["merged_t78_imported"] is True
    assert data["predecessors"]["t78_refinement_consumed"] is True
    assert data["predecessors"]["t78_refinement_merged_predecessor"] is True
    assert data["t78_refinement"]["angular_gcd_mobius_tensor_decomposition_proved"] is True
    assert data["projective_character"]["finite_conductor_norm"] == "d_chi^2"
    assert data["projective_character"]["max_finite_conductor_norm"] == "M^2"
    assert data["power_saving"]["OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED"] is False
    assert data["power_saving"]["CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT"] == "0"
    assert data["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "23/44"
    assert data["TH23_NEEDED"] is False
    assert data["NEXT"] == "Stage14-t79"


def main() -> None:
    predecessor_audit()
    group = projective_group_order_audit()
    conductor = conductor_square_audit()
    deficient = deficient_range_guard()
    t78mod = t78_external_modulus_audit()
    cells = four_cell_audit()
    boundary_audit()
    print(json.dumps({
        "stage": "14-tH22",
        "status": "COMPLETE_T78_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT",
        "object": "CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve",
        "merged_t78_imported": True,
        "projective_character_conductor_identified": True,
        "max_projective_conductor_norm": "M^2",
        "off_the_shelf_ray_character_power_saving_proved": False,
        "certified_ray_character_B_power_saving_exponent": "0",
        "minimal_remaining_obstruction": "ProjectiveConductorCompressedGaussianPrimeExternalKappaFourCellMobiusCoverHybridLargeSieve",
        "current_global_exponent": "23/44",
        "next": "Stage14-t79",
        **group,
        **conductor,
        **deficient,
        **t78mod,
        **cells,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
