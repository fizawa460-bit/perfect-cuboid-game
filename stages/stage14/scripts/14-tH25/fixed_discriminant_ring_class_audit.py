#!/usr/bin/env python3
"""Deterministic Stage14-tH25 audit for the frozen Stage14-t86 receiver."""

from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
HPROTOCOL = ROOT / "stages/stage14/H-PROTOCOL.md"
T86 = ROOT / "stages/stage14/14-t86/result.md"
TARGET = ROOT / "stages/stage14/14-t86/th25-target.md"
X14 = ROOT / "stages/stage14/14-X14/result.md"
TH25 = ROOT / "stages/stage14/14-tH25/result.md"
BOUNDARY = ROOT / "stages/stage14/data/tH25/fixed_discriminant_ring_class_boundary.json"

SOURCE_SHA = "798191aa5071a344cf642a1be265f1ad8e373fd5"
CLASS_D = (3, 5, 7, 11, 15, 21, 33, 35, 55, 65, 77)
DELTA_LIMIT = 4000


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


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


def chi4(p: int) -> int:
    assert p % 2 == 1
    return 1 if p % 4 == 1 else -1


def class_number_formula(d: int) -> int:
    if d == 1:
        return 1
    v = Fraction(d, 2)
    for p in factor(d):
        v *= Fraction(p - chi4(p), p)
    assert v.denominator == 1
    return v.numerator


def reduced_forms(discriminant: int) -> list[tuple[int, int, int]]:
    assert discriminant < 0
    out: list[tuple[int, int, int]] = []
    limit = isqrt(abs(discriminant) // 3) + 3
    for a in range(1, limit + 1):
        for b in range(-a, a + 1):
            num = b * b - discriminant
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if a > c:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            if gcd(a, gcd(abs(b), c)) != 1:
                continue
            out.append((a, b, c))
    return out


def reduce_form(a: int, b: int, c: int) -> tuple[int, int, int]:
    discriminant = b * b - 4 * a * c
    assert discriminant < 0
    for _ in range(1000):
        # Proper shear: choose b' in (-a,a].
        q = (b + a - 1) // (2 * a)
        b -= 2 * a * q
        num = b * b - discriminant
        assert num % (4 * a) == 0
        c = num // (4 * a)

        if a > c:
            a, c = c, a
            b = -b
            continue

        if abs(b) <= a <= c:
            if (abs(b) == a or a == c) and b < 0:
                b = -b
            return a, b, c
    raise AssertionError("binary quadratic form reduction did not terminate")


def roots_minus_one(n: int) -> list[int]:
    if n == 1:
        return [0]
    return [r for r in range(n) if (r * r + 1) % n == 0]


def predecessor_audit() -> None:
    hp = HPROTOCOL.read_text()
    t86 = T86.read_text()
    target = TARGET.read_text()
    x14 = X14.read_text()

    need(hp, "ONE_H_REQUEST_ONE_SNAPSHOT=true", "H-PROTOCOL")
    need(hp, "RUNNING_H_CHASES_LATER_PARENT_STAGES=false", "H-PROTOCOL")

    need(target, "H_STAGE=Stage14-tH25", "t86 target")
    need(target, "TARGET_FREEZES_AT_DISPATCH=true", "t86 target")
    need(target, "RUNNING_TH25_MAY_CHASE_T87_PLUS=false", "t86 target")
    need(
        target,
        "FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve",
        "t86 target",
    )

    need(
        t86,
        "COMPLETE_COFACTOR_ROOT_LINE_TO_FIXED_DISCRIMINANT_FIXED_COFACTOR_PRIME_VALUE_FORM",
        "t86",
    )
    need(t86, "FORM_DISCRIMINANT=-4*d^2", "t86")
    need(t86, "FIXED_COFACTOR_PRIME_VALUE_FORM_PROVED=true", "t86")
    need(t86, "DELTA_GAUSSIAN_IDEAL_EXTRACTION_PROVED=true", "t86")
    need(t86, "FIXED_K_GAUSSIAN_FACTOR_PEEL_PROVED=true", "t86")
    need(t86, "TH25_NEEDED=true", "t86")
    need(x14, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2", "X14")
    need(x14, "STRICT_SUBSQRT_POWER_SAVING_PROVED=false", "X14")


def class_family_audit() -> dict[str, int]:
    # Precompute exactly the odd delta0 <= DELTA_LIMIT that admit rho^2=-1.
    candidate_deltas: list[tuple[int, list[int]]] = []
    for delta0 in range(1, DELTA_LIMIT + 1, 2):
        ff = factor(delta0)
        if not all(p % 4 == 1 for p in ff):
            continue
        roots = roots_minus_one(delta0)
        assert len(roots) == (1 if delta0 == 1 else 2 ** len(ff))
        candidate_deltas.append((delta0, roots))

    class_number_formula_checks = 0
    physical_shape_checks = 0
    full_class_coverage_samples = 0
    total_reduced_classes = 0
    max_sample_class_number = 0
    max_delta_needed_for_full_sample_coverage = 0

    for d in CLASS_D:
        discriminant = -4 * d * d
        classes = set(reduced_forms(discriminant))
        expected_h = class_number_formula(d)
        assert len(classes) == expected_h
        class_number_formula_checks += 1
        total_reduced_classes += len(classes)
        max_sample_class_number = max(max_sample_class_number, len(classes))

        seen: dict[tuple[int, int, int], int] = {}
        for delta0, roots in candidate_deltas:
            if gcd(delta0, d) != 1:
                continue
            for rho in roots:
                c0 = (rho * rho + 1) // delta0
                a = delta0
                b = 2 * rho * d
                c = c0 * d * d

                assert b * b - 4 * a * c == discriminant
                assert gcd(a, gcd(abs(b), c)) == 1
                reduced = reduce_form(a, b, c)
                assert reduced in classes
                seen.setdefault(reduced, delta0)
                physical_shape_checks += 1

        # Finite no-collapse regression: small t86-shaped forms already realize
        # all reduced classes for each selected conductor.
        assert set(seen) == classes, (d, classes - set(seen))
        full_class_coverage_samples += 1
        max_delta_needed_for_full_sample_coverage = max(
            max_delta_needed_for_full_sample_coverage, max(seen.values())
        )

    return {
        "candidate_delta0_count": len(candidate_deltas),
        "candidate_root_pair_count": sum(len(r) for _, r in candidate_deltas),
        "class_number_formula_checks": class_number_formula_checks,
        "physical_t86_form_shape_checks": physical_shape_checks,
        "full_class_coverage_samples": full_class_coverage_samples,
        "total_reduced_classes": total_reduced_classes,
        "max_sample_class_number": max_sample_class_number,
        "max_delta_needed_for_full_sample_coverage": max_delta_needed_for_full_sample_coverage,
    }


def range_guard_audit() -> dict[str, str | int]:
    # Exponent witness allowed by the target, with fixed epsilon, eta, k0.
    # d=B^alpha, delta0=B^beta, ell=B^lam, Y_U=B^y.
    alpha = Fraction(3, 20)
    beta = Fraction(3, 20)
    lam = Fraction(1, 5)
    y = Fraction(47, 100)

    checks = 0
    assert alpha + beta < Fraction(1, 2)
    checks += 1
    assert alpha + 2 * beta < y
    checks += 1
    assert lam + beta < y
    checks += 1
    assert lam > beta
    checks += 1

    # General Zaman unconditional form-independent range for
    # |Disc|=4d^2 is ell >= |Disc|^(2+eps), i.e. exponent >4alpha.
    assert lam < 4 * alpha
    checks += 1

    # Even the most optimistic a~sqrt(|Disc|) version of the unconditional
    # reduced-form scale has baseline d^3, still not forced by the target.
    assert lam < 3 * alpha
    checks += 1

    # The allowed delta0 exponent can be as large as the class-number exponent;
    # the target alone does not enforce a power-small label family.
    assert beta >= alpha
    checks += 1

    return {
        "range_guard_checks": checks,
        "witness_d_exponent": "3/20",
        "witness_delta0_exponent": "3/20",
        "witness_ell_exponent": "1/5",
        "witness_YU_exponent": "47/100",
        "target_forces_Zaman_unconditional_range": "false",
        "target_forces_power_small_class_index_range": "false",
    }


def boundary_audit() -> None:
    text = TH25.read_text()
    tokens = [
        "STAGE14_TH25=COMPLETE_T86_SNAPSHOT_FIXED_DISCRIMINANT_RING_CLASS_PRIME_VALUE_APPLICABILITY_AUDIT",
        "AUDITED_THROUGH=Stage14-t86",
        f"SOURCE_SNAPSHOT_SHA={SOURCE_SHA}",
        "TARGET_FROZEN=true",
        "T86_FIXED_DISCRIMINANT_RETAINED=true",
        "T86_FORM_DISCRIMINANT=-4*d^2",
        "T86_FIXED_VALUE_COFACTOR_RETAINED=true",
        "T86_MOVING_DELTA_VALUE_SIDE_ELIMINATED=true",
        "T86_FORM_CLASS_FAMILY_RETAINED=true",
        "T86_GAUSSIAN_IDEAL_FACTORIZATION_RETAINED=true",
        "T86_FIXED_K_PEEL_RETAINED=true",
        "BILINEAR_PI_V_MULTIPLICITY_REOPENED=false",
        "RING_CLASS_NUMBER_SCALE=d*Bo1",
        "UNRESTRICTED_T86_FORM_SHAPE_SPANS_FULL_RING_CLASS_GROUP=true",
        "PHYSICAL_FORM_CLASS_SUBFAMILY_BO1_PROVED=false",
        "FULL_PHYSICAL_MASKS_RETAINED=true",
        "RING_CLASS_PRIME_THEOREM_APPLICABLE=false",
        "GROWING_DISCRIMINANT_FORM_PRIME_THEOREM_APPLICABLE=false",
        "RING_CLASS_LARGE_SIEVE_APPLICABLE=false",
        "GAUSSIAN_SHORT_COFACTOR_PRIME_BILINEAR_APPLICABLE=false",
        "FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED=true",
        "FORM_CLASS_FAMILY_POWER_COST_CONTROLLED=false",
        "OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false",
        "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
        "FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=FixedUPhysicalDeltaRootRingClassFamilyCompressionWithReconstructedCoverMasks",
        "PREFERRED_RECEIVER=SharedUFixedSelectorRingClassCompressedFixedCofactorPrimeValuePhysicalEnergy",
        "NEXT_H_NEEDED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    ]
    for token in tokens:
        need(text, token, "tH25 result")

    data = json.loads(BOUNDARY.read_text())
    assert data["stage"] == "14-tH25"
    assert data["source_snapshot_sha"] == SOURCE_SHA
    assert data["target_frozen"] is True
    assert data["ring_class"]["ambient_class_number_scale"] == "d*B^o(1)"
    assert data["ring_class"]["unrestricted_t86_form_shape_spans_full_ring_class_group"] is True
    assert data["ring_class"]["physical_form_class_power_sparse_proved"] is False
    assert data["applicability"]["RING_CLASS_PRIME_THEOREM_APPLICABLE"] is False
    assert data["applicability"]["FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED"] is True
    assert data["applicability"]["FORM_CLASS_FAMILY_POWER_COST_CONTROLLED"] is False
    assert data["power_saving"]["CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT"] == "0"
    assert data["NEXT_H_NEEDED"] is False
    assert data["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"


def main() -> None:
    predecessor_audit()
    classes = class_family_audit()
    range_guard = range_guard_audit()
    boundary_audit()

    out = {
        "stage": "14-tH25",
        "status": "COMPLETE_T86_SNAPSHOT_FIXED_DISCRIMINANT_RING_CLASS_PRIME_VALUE_APPLICABILITY_AUDIT",
        "audited_through": "Stage14-t86",
        "source_snapshot_sha": SOURCE_SHA,
        "requested_object": "FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve",
        "target_frozen": True,
        "ambient_ring_class_number_scale": "d*B^o(1)",
        "unrestricted_t86_form_shape_spans_full_ring_class_group": True,
        "physical_form_class_power_sparse_proved": False,
        "fixed_k_ideal_composition_adapter_proved": True,
        "off_the_shelf_fixed_power_saving_proved": False,
        "certified_fixed_U_packet_B_power_saving_exponent": "0",
        "minimal_remaining_obstruction": "FixedUPhysicalDeltaRootRingClassFamilyCompressionWithReconstructedCoverMasks",
        "preferred_receiver": "SharedUFixedSelectorRingClassCompressedFixedCofactorPrimeValuePhysicalEnergy",
        "next_H_needed": False,
        "current_global_exponent": "1/2",
        **classes,
        **range_guard,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
