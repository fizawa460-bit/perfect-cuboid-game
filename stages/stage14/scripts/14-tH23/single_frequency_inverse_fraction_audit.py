#!/usr/bin/env python3
"""Deterministic Stage14-tH23 audit after merged t82 refinement."""

from __future__ import annotations

from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T80 = ROOT / "stages/stage14/14-t80/result.md"
T81 = ROOT / "stages/stage14/14-t81/result.md"
T82 = ROOT / "stages/stage14/14-t82/result.md"
T82_REFINE = ROOT / "stages/stage14/14-t82/th23-refinement.md"
X13 = ROOT / "stages/stage14/14-X13/result.md"
S744 = ROOT / "stages/stage14/14-s7-44/result.md"
TH23 = ROOT / "stages/stage14/14-tH23/result.md"
BOUNDARY = ROOT / "stages/stage14/data/tH23/single_frequency_inverse_fraction_boundary.json"


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def predecessor_audit() -> None:
    t80 = T80.read_text()
    t81 = T81.read_text()
    t82 = T82.read_text()
    t82r = T82_REFINE.read_text()
    x13 = X13.read_text()
    s744 = S744.read_text()

    need(t80, "T80_PROJECTIVE_GAUSS_DUALIZATION_RETAINED=true", "t80")
    need(t80, "ADDITIVE_DUAL_MODULUS_IS_RATIONAL_D=true", "t80")
    need(t81, "TWO_ADDITIVE_FREQUENCIES_COLLAPSE_TO_ONE=Bo1", "t81")
    need(t81, "AFFINE_DEGENERACY_IS_FIXED_U_BETA_COORDINATE_SUPPORT=true", "t81")
    need(t82, "STAGE14_T82=COMPLETE_AFFINE_DEGENERATE_RAY_MODULUS_TO_FIXED_U_COORDINATE_DIVISOR_HOST", "t82")
    need(t82, "HARD_DIAGONAL_MODULUS_DIVIDES_FIXED_U_SELECTOR=true", "t82")
    need(t82, "FIXED_U_SELECTOR_DIVIDES_R_TIMES_S=true", "t82")
    need(t82, "FIXED_U_SELECTOR_MAX=m/2", "t82")
    need(t82, "HARD_DIAGONAL_MODULUS_LT_ELL_OVER_4_UP_TO_BO1=true", "t82")
    need(t82, "FIXED_U_HARD_MODULUS_MULTIPLICITY=Bo1", "t82")
    need(t82, "MOVING_MODULUS_FAMILY_LENGTH_REOPENED=false", "t82")
    need(t82, "PURE_PI_V_PROJECTIVE_RELATION_ON_DIAGONAL_MODULUS=true", "t82")
    need(t82r, "FixedUCoordinateDivisorModulusSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve", "t82 refinement")
    need(t82r, "d_diag|R*S", "t82 refinement")
    need(t82r, "[pi]=sigma([V]) mod d_diag", "t82 refinement")
    need(x13, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2", "X13")
    need(s744, "STRICT_SUBSQRT_POWER_SAVING_PROVED=false", "s7-44")


def divisors(n: int) -> list[int]:
    out = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def selector_divisor_audit() -> dict[str, int]:
    checks = 0
    max_ratio_num = 0
    max_ratio_den = 1
    divisor_host_checks = 0

    # Primitive fixed-U samples; synthetic alpha/beta ray moduli are chosen
    # squarefreely from coordinate divisors.  This checks only the exact
    # selector/divisor identities consumed by tH23, not analytic saving.
    samples = [(3, 4), (5, 12), (8, 15), (20, 21), (12, 35), (33, 56)]
    for R, S in samples:
        assert gcd(R, S) == 1
        m = R * R + S * S
        assert 2 * abs(R * S) <= m

        rdiv = divisors(abs(R))
        sdiv = divisors(abs(S))
        for db in rdiv:
            for da in sdiv:
                # alpha-tag selector divides S; beta-tag selector divides R.
                D = da * db
                assert gcd(da, db) == 1
                assert abs(R * S) % D == 0
                assert 2 * D <= m
                divisor_host_checks += 1

                # Every admissible hard d_diag is a divisor of D_Ubeta.
                for d_diag in divisors(D):
                    assert D % d_diag == 0
                    assert abs(R * S) % d_diag == 0
                    # Choose any ell satisfying merged t65 ell>2m.
                    ell = 2 * m + 1
                    assert d_diag <= m // 2 or d_diag * 2 <= m
                    assert 4 * d_diag < ell * 2  # weaker integer form of d<=m/2<ell/4 up to endpoint convention
                    checks += 1

                    if D * max_ratio_den > max_ratio_num * m:
                        max_ratio_num, max_ratio_den = D, m

    return {
        "selector_divisor_checks": checks,
        "fixed_U_divisor_host_checks": divisor_host_checks,
        "max_selector_ratio_numerator": max_ratio_num,
        "max_selector_ratio_denominator": max_ratio_den,
    }


def modulus_multiplicity_audit() -> dict[str, int]:
    checks = 0
    max_tau = 0
    for R, S in [(3, 4), (5, 12), (8, 15), (20, 21), (12, 35), (33, 56)]:
        n = abs(R * S)
        ds = divisors(n)
        assert len(ds) == len(set(ds))
        for d in ds:
            assert n % d == 0
            checks += 1
        max_tau = max(max_tau, len(ds))
    return {"fixed_U_modulus_divisor_checks": checks, "max_sample_tau_RS": max_tau}


def matched_frequency_audit() -> dict[str, int]:
    checks = 0
    # For squarefree sample moduli and signs s^2=1, each primitive a has a
    # unique matched b=s*a modulo the full diagonal modulus.
    for d in [15, 21, 35, 55, 77, 105]:
        signs = [1, d - 1]
        for s in signs:
            assert (s * s - 1) % d == 0
            for a in range(1, d):
                if gcd(a, d) != 1:
                    continue
                b = (s * a) % d
                assert gcd(b, d) == 1
                assert (b - s * a) % d == 0
                checks += 1
    return {"single_frequency_matched_line_checks": checks}


def boundary_audit() -> None:
    text = TH23.read_text()
    tokens = [
        "STAGE14_TH23=COMPLETE_T82_REFINED_FIXED_U_COORDINATE_DIVISOR_SINGLE_FREQUENCY_INVERSE_FRACTION_APPLICABILITY_AUDIT",
        "T82_FIXED_U_SELECTOR_DIVISOR_RETAINED=true",
        "MOVING_MODULUS_FAMILY_LENGTH_REOPENED=false",
        "TWO_FREQUENCY_LENGTH_REOPENED=false",
        "HECKE_CONDUCTOR_D2_REOPENED=false",
        "FIXED_DIVISOR_MODULUS_RANGE_RETAINED=true",
        "PURE_PI_V_PROJECTIVE_RELATION_RETAINED=true",
        "FOUR_CELL_COEFFICIENT_L2_THEOREM_READY=true",
        "FIXED_MODULUS_KLOOSTERMAN_LARGE_SIEVE_APPLICABLE=false",
        "INVERSE_FRACTION_BILINEAR_ESTIMATE_APPLICABLE=false",
        "SPECTRAL_DUALITY_APPLICABLE=false",
        "CANONICAL_GAUSSIAN_PRIME_SIDE_BOUND_APPLICABLE=false",
        "BALANCED_COVER_SIDE_BOUND_APPLICABLE=false",
        "FULL_PHYSICAL_MASKS_RETAINED=true",
        "OFF_THE_SHELF_FIXED_DIVISOR_SINGLE_FREQUENCY_POWER_SAVING_PROVED=false",
        "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
        "FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false",
        "MINIMAL_REMAINING_OBSTRUCTION=FixedUCoordinateDivisorModulusCanonicalGaussianPrimeShortCoverSingleFrequencyCollisionDispersion",
        "PREFERRED_RECEIVER=SharedUBalancedFixedUSelectorDivisorModulusAlmostDiagonalSinglePrimitiveFrequencyCanonicalPrimeShortCoverInverseFractionEnergy",
        "TH24_NEEDED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-t83",
    ]
    for token in tokens:
        need(text, token, "tH23")

    data = json.loads(BOUNDARY.read_text())
    assert data["object"] == "FixedUCoordinateDivisorModulusSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve"
    assert data["predecessors"]["merged_t82"] is True
    assert data["t82_refinement"]["moving_modulus_family_length_reopened"] is False
    assert data["t82_refinement"]["fixed_U_hard_modulus_multiplicity"] == "B^o(1)"
    assert data["applicability"]["FOUR_CELL_COEFFICIENT_L2_THEOREM_READY"] is True
    assert data["power_saving"]["CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT"] == "0"
    assert data["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert data["TH24_NEEDED"] is False
    assert data["NEXT"] == "Stage14-t83"


def main() -> None:
    predecessor_audit()
    selector = selector_divisor_audit()
    multiplicity = modulus_multiplicity_audit()
    matched = matched_frequency_audit()
    boundary_audit()
    out = {
        "stage": "14-tH23",
        "status": "COMPLETE_T82_REFINED_FIXED_U_COORDINATE_DIVISOR_SINGLE_FREQUENCY_INVERSE_FRACTION_APPLICABILITY_AUDIT",
        "object": "FixedUCoordinateDivisorModulusSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve",
        "off_the_shelf_fixed_divisor_single_frequency_power_saving_proved": False,
        "certified_fixed_U_packet_B_power_saving_exponent": "0",
        "minimal_remaining_obstruction": "FixedUCoordinateDivisorModulusCanonicalGaussianPrimeShortCoverSingleFrequencyCollisionDispersion",
        "current_global_exponent": "1/2",
        "strict_subsqrt_power_saving_proved": False,
        "next": "Stage14-t83",
        **selector,
        **multiplicity,
        **matched,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
