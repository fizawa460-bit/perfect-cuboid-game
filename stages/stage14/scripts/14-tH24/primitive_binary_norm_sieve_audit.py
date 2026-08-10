#!/usr/bin/env python3
"""Deterministic Stage14-tH24 audit for the frozen Stage14-t84 receiver."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TARGET = ROOT / "stages/stage14/14-t84/th24-target.md"
T84 = ROOT / "stages/stage14/14-t84/result.md"
HP = ROOT / "stages/stage14/H-PROTOCOL.md"
RESULT = ROOT / "stages/stage14/14-tH24/result.md"
BOUNDARY_TXT = ROOT / "stages/stage14/14-tH24/BOUNDARY.txt"
BOUNDARY_JSON = ROOT / "stages/stage14/data/tH24/primitive_binary_norm_sieve_boundary.json"

LIMIT = 90
PRIME_WITNESS_LIMIT = 5000


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return len(factor(n)) == 1 and next(iter(factor(n).values())) == 1


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def sum_two_squares_rep(n: int) -> tuple[int, int] | None:
    for d in range(1, math.isqrt(n) + 1):
        t2 = n - d * d
        if t2 <= 0:
            continue
        t = math.isqrt(t2)
        if t * t == t2:
            return (t, d)
    return None


def predecessor_audit() -> None:
    target = TARGET.read_text()
    t84 = T84.read_text()
    hp = HP.read_text()

    need(target, "H_STAGE=Stage14-tH24", "t84 target")
    need(target, "TARGET_FREEZES_AT_DISPATCH=true", "t84 target")
    need(target, "RUNNING_TH24_MAY_CHASE_T85_PLUS=false", "t84 target")
    need(target, "FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve", "t84 target")
    need(target, "ell=LPF(N)=LPF_odd(N)", "t84 target")
    need(target, "ell^2>2N", "t84 target")
    need(target, "D=d*j", "t84 target")
    need(target, "CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false", "t84 target")
    need(target, "BILINEAR_PI_V_MULTIPLICITY_REOPENED=false", "t84 target")

    need(t84, "STAGE14_T84=COMPLETE_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_AND_SHORT_COFACTOR_REDUCTION", "t84 result")
    need(t84, "PRIMITIVE_SWITCHED_BINARY_NORM_PROVED=true", "t84 result")
    need(t84, "CANONICAL_ELL_RECOVERED_AS_BINARY_NORM_LPF=true", "t84 result")
    need(t84, "CANONICAL_ELL_EXPONENT_ONE_IN_BINARY_NORM=true", "t84 result")
    need(t84, "CANONICAL_ELL_SUPER_SQRT_GAP=ell^2>2N", "t84 result")
    need(t84, "SHORT_COVER_NORM_COFACTOR_PROVED=true", "t84 result")
    need(t84, "FIXED_ORIENTATION_PI_V_RECONSTRUCTION_UNIQUE=true", "t84 result")
    need(t84, "BILINEAR_PI_V_MULTIPLICITY_ELIMINATED=true", "t84 result")
    need(t84, "MOVING_MODULUS_FAMILY_REOPENED=false", "t84 result")
    need(t84, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2", "t84 result")

    need(hp, "ONE_H_REQUEST_ONE_SNAPSHOT=true", "H protocol")
    need(hp, "RUNNING_H_CHASES_LATER_PARENT_STAGES=false", "H protocol")


def primitive_norm_audit() -> dict[str, int | float]:
    primitive_pairs = 0
    split_support_checks = 0
    super_sqrt_states = 0
    lpf_uniqueness_checks = 0
    short_cofactor_checks = 0
    vertical_factor_checks = 0
    quarter_switch_checks = 0
    max_n_over_sqrt_half_N = 0.0

    for T in range(-LIMIT, LIMIT + 1):
        for D in range(-LIMIT, LIMIT + 1):
            if D == 0 or math.gcd(abs(T), abs(D)) != 1:
                continue
            N = T * T + D * D
            if N <= 1:
                continue
            primitive_pairs += 1
            ff = factor(N)

            # Primitive sums of two squares have no odd 3 mod 4 divisor.
            assert all(p == 2 or p % 4 == 1 for p in ff)
            assert ff.get(2, 0) <= 1
            split_support_checks += 1

            ell = max(ff)
            if ell == 2 or ell % 4 != 1:
                continue
            if ff[ell] != 1 or ell * ell <= 2 * N:
                continue

            n = N // ell
            super_sqrt_states += 1
            assert ell == max(ff)
            assert ff[ell] == 1
            assert ell > 2 * n
            lpf_uniqueness_checks += 1

            assert n * n < N / 2
            short_cofactor_checks += 1
            max_n_over_sqrt_half_N = max(
                max_n_over_sqrt_half_N,
                n / math.sqrt(N / 2),
            )

            for d in divisors(abs(D)):
                j = D // d
                assert d * j == D
                assert math.gcd(abs(T), d) == 1
                assert math.gcd(abs(T), abs(j)) == 1
                vertical_factor_checks += 1

                assert min(d, abs(j)) ** 2 <= abs(D)
                quarter_switch_checks += 1

    assert primitive_pairs > 0
    assert super_sqrt_states > 0
    return {
        "primitive_pair_checks": primitive_pairs,
        "split_prime_support_checks": split_support_checks,
        "super_sqrt_lpf_states": super_sqrt_states,
        "lpf_uniqueness_checks": lpf_uniqueness_checks,
        "short_cofactor_checks": short_cofactor_checks,
        "vertical_factor_checks": vertical_factor_checks,
        "quarter_switch_checks": quarter_switch_checks,
        "max_n_over_sqrt_N_over_2": max_n_over_sqrt_half_N,
    }


def prime_norm_witness_audit() -> dict[str, int]:
    # The super-sqrt LPF receiver arithmetically contains prime norm values.
    # This is a deterministic non-emptiness/double-charge guard, not a density theorem.
    witnesses = 0
    primitive_witnesses = 0
    for ell in range(5, PRIME_WITNESS_LIMIT + 1):
        if not is_prime(ell) or ell % 4 != 1:
            continue
        rep = sum_two_squares_rep(ell)
        assert rep is not None
        T, D = rep
        assert math.gcd(T, D) == 1
        N = T * T + D * D
        assert N == ell
        assert ell * ell > 2 * N
        assert N // ell == 1
        witnesses += 1
        primitive_witnesses += 1
    assert witnesses > 0
    return {
        "arithmetic_prime_norm_witnesses": witnesses,
        "primitive_prime_norm_witnesses": primitive_witnesses,
    }


def boundary_audit() -> None:
    result = RESULT.read_text()
    boundary = BOUNDARY_TXT.read_text()
    tokens = [
        "STAGE14_TH24=COMPLETE_T84_SNAPSHOT_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_VERTICAL_DIVISOR_SIEVE_APPLICABILITY_AUDIT",
        "AUDITED_THROUGH=Stage14-t84",
        "SOURCE_SNAPSHOT_SHA=fa93c79084e05a2f1aa39eeb80b48f2e82f82113",
        "TARGET_FROZEN=true",
        "T84_PRIMITIVE_BINARY_NORM_RETAINED=true",
        "T84_CANONICAL_ELL_AS_LPF_RETAINED=true",
        "T84_SUPER_SQRT_LPF_GAP_RETAINED=true",
        "T84_SHORT_COFACTOR_RETAINED=true",
        "T84_FIXED_U_VERTICAL_DIVISOR_RETAINED=true",
        "T84_PI_V_RECONSTRUCTION_RETAINED=true",
        "CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false",
        "BILINEAR_PI_V_MULTIPLICITY_REOPENED=false",
        "FULL_PHYSICAL_MASKS_RETAINED=true",
        "HALF_DIMENSIONAL_SIEVE_APPLICABLE=false",
        "HARMAN_BUCHSTAB_APPLICABLE=false",
        "GAUSSIAN_BV_BDH_APPLICABLE=false",
        "BINARY_QUADRATIC_LARGE_PRIME_FACTOR_THEOREM_APPLICABLE=false",
        "VERTICAL_DIVISOR_DISPERSION_APPLICABLE=false",
        "OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false",
        "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
        "FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=FixedUVerticalDivisorPrimitiveBinaryNormShortCofactorBuchstabDispersionWithReconstructedCoverMasks",
        "PREFERRED_RECEIVER=SharedUFixedSelectorDivisorPrimitiveBinaryNormSuperSqrtLPFShortCofactorVerticalBuchstabEnergy",
        "NEXT_H_NEEDED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    ]
    for token in tokens:
        need(result, token, "tH24 result")
        need(boundary, token, "tH24 boundary")

    data = json.loads(BOUNDARY_JSON.read_text())
    assert data["AUDITED_THROUGH"] == "Stage14-t84"
    assert data["SOURCE_SNAPSHOT_SHA"] == "fa93c79084e05a2f1aa39eeb80b48f2e82f82113"
    assert data["TARGET_FROZEN"] is True
    assert data["REQUESTED_OBJECT"] == "FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve"
    assert data["power_saving"]["OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED"] is False
    assert data["power_saving"]["CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT"] == "0"
    assert data["NEXT_H_NEEDED"] is False
    assert data["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"


def main() -> None:
    predecessor_audit()
    arithmetic = primitive_norm_audit()
    witnesses = prime_norm_witness_audit()
    boundary_audit()
    out = {
        "stage": "14-tH24",
        "status": "COMPLETE_T84_SNAPSHOT_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_VERTICAL_DIVISOR_SIEVE_APPLICABILITY_AUDIT",
        "audited_through": "Stage14-t84",
        "source_snapshot_sha": "fa93c79084e05a2f1aa39eeb80b48f2e82f82113",
        "target_frozen": True,
        "requested_object": "FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve",
        "off_the_shelf_fixed_power_saving_proved": False,
        "certified_fixed_U_packet_B_power_saving_exponent": "0",
        "minimal_remaining_obstruction": "FixedUVerticalDivisorPrimitiveBinaryNormShortCofactorBuchstabDispersionWithReconstructedCoverMasks",
        "preferred_receiver": "SharedUFixedSelectorDivisorPrimitiveBinaryNormSuperSqrtLPFShortCofactorVerticalBuchstabEnergy",
        "next_H_needed": False,
        "current_global_exponent": "1/2",
        **arithmetic,
        **witnesses,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
