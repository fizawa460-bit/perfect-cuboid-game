#!/usr/bin/env python3
"""Deterministic Stage14-tH21 predecessor, kernel, and boundary audit."""

from __future__ import annotations

from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T73 = ROOT / "stages/stage14/14-t73/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"
T75 = ROOT / "stages/stage14/14-t75/result.md"
T76 = ROOT / "stages/stage14/14-t76/result.md"
X12 = ROOT / "stages/stage14/14-X12/result.md"
TH21 = ROOT / "stages/stage14/14-tH21/result.md"
BOUNDARY = ROOT / "stages/stage14/data/tH21/balanced_clean_kappa_typeii_boundary.json"


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def predecessor_audit() -> None:
    t73 = T73.read_text()
    th20 = TH20.read_text()
    t75 = T75.read_text()
    t76 = T76.read_text()
    x12 = X12.read_text()

    need(t73, "FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY=1", "t73")
    need(th20, "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false", "tH20")
    need(t75, "HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I=true", "t75")
    need(t75, "LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED=true", "t75")
    need(
        t76,
        "STAGE14_T76=COMPLETE_CLEAN_KAPPA_COVER_PROJECTIVE_ROOTLINE_AND_DEFICIENT_TYPEII_REDUCTION",
        "t76",
    )
    need(t76, "CLEAN_KAPPA_CRT_PROJECTIVE_ROOT_LINE_PROVED=true", "t76")
    need(
        t76,
        "LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING=true",
        "t76",
    )
    need(
        t76,
        "TH21_REQUESTED_OBJECT=SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion",
        "t76",
    )
    need(x12, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128", "X12")


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def clean_modulus_conditioning_audit() -> dict[str, int]:
    """Fixed squarefree K and g determine K_clean through divisor-many data."""
    K = 3 * 5 * 7 * 11
    observed = set()
    checks = 0
    for g in range(1, 5 * K + 1):
        kbad = gcd(K, g)
        kclean = K // kbad
        assert K % kclean == 0
        assert kbad * kclean == K
        observed.add(kclean)
        checks += 1
    assert observed.issubset(set(divisors(K)))
    assert len(observed) <= len(divisors(K))
    return {
        "fixed_K_clean_conditioning_checks": checks,
        "fixed_K_distinct_K_clean_values": len(observed),
        "fixed_K_divisor_count": len(divisors(K)),
    }


def projective_line_parameterization_audit() -> dict[str, int]:
    """Check exact line parameterization t=rho*r+jQ in deficient rectangles."""
    checks = 0
    line_points = 0
    for Q in (3, 5, 7, 9, 15, 21, 35):
        for rho in range(1, Q):
            if gcd(rho, Q) != 1:
                continue
            for r in range(1, 35):
                if gcd(r, Q) != 1:
                    continue
                for t in range(1, 45):
                    on_line = (t - rho * r) % Q == 0
                    if on_line:
                        j = (t - rho * r) // Q
                        assert t == rho * r + j * Q
                        line_points += 1
                    checks += 1
    assert line_points > 1000
    return {
        "projective_rectangle_checks": checks,
        "projective_line_points": line_points,
    }


def additive_opening_integer_audit() -> dict[str, int]:
    """Finite-character orthogonality without floating point: count phases by residues.

    The sum over a mod Q of zeta_Q^(a*x) is Q for x=0 mod Q and 0 otherwise.
    We verify the exponent residues form a full permutation when x is a unit/nonzero
    in prime test moduli, and use direct residue multiplicities for composite Q.
    """
    checks = 0
    for Q in (3, 5, 7, 11, 13):
        for x in range(Q):
            residues = [(a * x) % Q for a in range(Q)]
            if x == 0:
                assert set(residues) == {0}
            else:
                assert sorted(residues) == list(range(Q))
            checks += 1
    return {"additive_orthogonality_residue_checks": checks}


def boundary_audit() -> None:
    text = TH21.read_text()
    tokens = [
        "STAGE14_TH21=COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT",
        "T76_LARGE_CLEAN_KAPPA_BRANCH_REOPENED=false",
        "T75_HIGH_IMBALANCE_BRANCH_REOPENED=false",
        "T75_LARGE_G_BRANCH_REOPENED=false",
        "PROJECTIVE_ROOTLINE_KERNEL_RETAINED=true",
        "CANONICAL_ELL_MASK_RETAINED=true",
        "SHORT_ELLIPSE_MASK_RETAINED=true",
        "SHARP_ELL_G_C_HYPERBOLA_RETAINED=true",
        "DFI_STYLE_DISPERSION_APPLICABLE=false",
        "KUZNETSOV_KLOOSTERMAN_APPLICABLE=false",
        "SPECTRAL_LARGE_SIEVE_APPLICABLE=false",
        "DIVISOR_SWITCHING_CAUCHY_POISSON_APPLICABLE=false",
        "MOVING_GAUSSIAN_PRIME_BILINEAR_APPLICABLE=false",
        "KCLEAN_DEFICIENCY_ALONE_GIVES_MODULUS_AVERAGING=false",
        "ELL_G_C_HYPERBOLA_CREATES_COMPLEMENTARY_ARITHMETIC_MODULUS=false",
        "OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false",
        "CERTIFIED_TYPEII_B_POWER_SAVING_EXPONENT=0",
        "MINIMAL_REMAINING_OBSTRUCTION=CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy",
        "PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedCleanKappaDeficientCanonicalGaussianPrimePrimitiveCoverTypeIIDispersionEnergy",
        "TH22_NEEDED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-t77",
    ]
    for token in tokens:
        need(text, token, "tH21")

    data = json.loads(BOUNDARY.read_text())
    assert data["object"] == "SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion"
    assert data["power_saving"]["CERTIFIED_TYPEII_B_POWER_SAVING_EXPONENT"] == "0"
    assert data["current_physical_whole_family_exponent"] == "71/128"
    assert data["TH22_NEEDED"] is False


def main() -> None:
    predecessor_audit()
    conditioning = clean_modulus_conditioning_audit()
    projective = projective_line_parameterization_audit()
    additive = additive_opening_integer_audit()
    boundary_audit()
    print(json.dumps({
        "stage": "14-tH21",
        "status": "COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT",
        "object": "SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion",
        "off_the_shelf_typeii_power_saving_proved": False,
        "certified_typeii_B_power_saving_exponent": "0",
        "minimal_remaining_obstruction": "CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy",
        "current_global_exponent": "71/128",
        "next": "Stage14-t77",
        **conditioning,
        **projective,
        **additive,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
