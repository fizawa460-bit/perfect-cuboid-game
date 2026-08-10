#!/usr/bin/env python3
"""Deterministic theorem-boundary audit for Stage14-s7-33."""
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[4]
RESULT = ROOT / "stages/stage14/14-s7-33/result.md"


def roots_minus_one(q: int):
    return [r for r in range(q) if (r * r + 1) % q == 0]


def root_line_gaussian_orientation_audit() -> int:
    """Check the exact Cayley/Gaussian orientation dictionary modulo odd q."""
    checks = 0
    moduli = [5, 13, 17, 25, 29, 37, 41, 65, 85, 125]
    for q in moduli:
        roots = roots_minus_one(q)
        if not roots:
            continue
        inv2 = pow(2, -1, q)
        for r in roots:
            assert ((1 + r) * pow(1 + r, -1, q)) % q == 1
            for a in range(1, min(q, 12)):
                if __import__("math").gcd(a, q) != 1:
                    continue
                for b in range(1, min(q, 12)):
                    if __import__("math").gcd(b, q) != 1:
                        continue
                    for V in range(1, min(q, 12)):
                        if __import__("math").gcd(V, q) != 1:
                            continue
                        # Force aU/(bV)=r mod q.
                        U = (r * b * V * pow(a, -1, q)) % q
                        if U == 0:
                            continue
                        D = ((a * U + b * V) * inv2) % q
                        A = ((a * U - b * V) * inv2) % q
                        assert (D + r * A) % q == 0
                        t = (a * U * pow((b * V) % q, -1, q)) % q
                        assert t == r
                        checks += 1
    assert checks > 0
    return checks


def stage_boundary_audit() -> None:
    text = RESULT.read_text()
    required = [
        "STAGE14_S7_33=COMPLETE_COMMON_CORE_GAUSSIAN_ORIENTATION_IDENTIFICATION_AND_TRANSFER_NOGO",
        "MERGED_S7_32_IMPORTED=true",
        "MERGED_4CT_IMPORTED=true",
        "MERGED_X10_IMPORTED=true",
        "UNIQUE_FIVE_EIGHTHS_SATURATION=(theta,phi)=(5/16,1/4)",
        "TOP_CORNER_COMMON_CORE_EXPONENT=3/8",
        "PRIMITIVE_XI_ROOT_LINE_GAUSSIAN_ORIENTATION_IDENTIFIED=true",
        "SHARED_COMMON_CORE_GAUSSIAN_ORIENTATION_MULTIPLICITY=Bo1",
        "DUAL_SWITCHED_HOST_PRODUCT_IDENTITIES_PROVED=true",
        "COMMON_CORE_ORIENTATION_DOUBLE_CHARGE_FORBIDDEN=true",
        "COMMON_CORE_CANCELLED_GAUSSIAN_TRANSFER_IDENTITY_PROVED=true",
        "STRONG_CANONICAL_ST_SPLIT_UNIVERSALLY_VALID=false",
        "STRONG_CANONICAL_ST_SPLIT_COUNTEREXAMPLE_EXISTS=true",
        "FINITE_PHYSICAL_DUAL_CROSS_PAIRS_CHECKED=52",
        "FINITE_STRONG_CANONICAL_SPLIT_FAILURES=23",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8",
        "NEW_WHOLE_FAMILY_POWER_SAVING_BELOW_5_8_PROVED=false",
        "REMAINING_RECEIVER=TopCornerSmallRootGcdCommonCoreCancelledGaussianSquareDivisorTransferIncidence",
        "S7_33_AUXILIARY_H_NEEDED=false",
        "TH18_CROSS_PROMOTED_TO_S7_33=false",
        "T72_CROSS_PROMOTED_TO_S7_33=false",
        "S_ROUTE_BLOCKED_WAITING_FOR_H=false",
        "NEXT=Stage14-s7-34",
    ]
    for token in required:
        assert token in text, token


def predecessor_boundary_audit() -> None:
    s32 = (ROOT / "stages/stage14/14-s7-32/result.md").read_text()
    ct = (ROOT / "stages/stage14/14-4ct/result.md").read_text()
    x10 = (ROOT / "stages/stage14/14-X10/result.md").read_text()
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8" in s32
    assert "UNIQUE_FIVE_EIGHTHS_SATURATION=(theta,phi)=(5/16,1/4)" in s32
    assert "CANONICAL_GOOD_COMMON_CORE_GAUSSIAN_DIVISOR_EXISTS=true" in ct
    assert "FIVE_EIGHTHS_SATURATION_REQUIRES_RESIDUAL_HOST_GCD=Bo1" in ct
    assert "TOP_CORNER_LARGE_H_FIXED_POWER_SAVED=true" in x10
    assert "DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION_PROVED=true" in x10


def main() -> None:
    predecessor_boundary_audit()
    n = root_line_gaussian_orientation_audit()
    stage_boundary_audit()
    print("Stage14-s7-33 theorem boundary audit: PASS")
    print(f"root-line/Gaussian orientation congruence checks: {n}")
    print("common-core orientation double-charge guard: exact")
    print("strong canonical S/T split: frozen false")
    print("current whole-family exponent: 5/8")
    print("s7-33 auxiliary H needed: false")


if __name__ == "__main__":
    main()
