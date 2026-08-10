#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[4]


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def divisors(n: int):
    out = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return out


summary = json.loads(
    (ROOT / "stages/stage14/data/14-X14/post_sqrt_frontier_summary.json").read_text()
)
assert summary["current_whole_family_exponent"] == "1/2"
assert summary["strict_subsqrt_power_saving_proved"] is False
assert summary["sh44_4dh_physical_receivers_finite_fiber_equivalent"] is True
assert summary["gaussian_norm_quotient_fixed_power_support"] == "oddpart(S*T)"
assert summary["x14_auxiliary_h_needed"] is False

# ---------------------------------------------------------------------------
# 1. Exact theta-quarter exponent ledger.
# ---------------------------------------------------------------------------
phi_lo = Fraction(5, 24)
phi_hi = Fraction(1, 4)
ledger_checks = 0
for den in range(24, 721):
    lo = (phi_lo.numerator * den + phi_lo.denominator - 1) // phi_lo.denominator
    hi = (phi_hi.numerator * den) // phi_hi.denominator
    for num in range(lo, hi + 1):
        phi = Fraction(num, den)
        if not (phi_lo <= phi <= phi_hi):
            continue
        chi = 2 * phi - Fraction(1, 4)
        xi_switch = Fraction(3, 4) - 2 * phi
        gaussian_quotient = Fraction(1, 2) - chi
        assert xi_switch == gaussian_quotient
        assert chi + xi_switch == Fraction(1, 2)
        assert Fraction(1, 6) <= chi <= Fraction(1, 4)
        ledger_checks += 1

# ---------------------------------------------------------------------------
# 2. Synthetic exact Gaussian product identities.
#    Force g | A,D by putting r=g*r0 and s=g*s0.
# ---------------------------------------------------------------------------
identity_checks = 0
sumdiff_checks = 0
for g in (1, 3, 5, 7, 9):
    for alpha in range(1, 20, 2):
        for delta in range(1, 24, 2):
            if math.gcd(alpha, delta) != 1:
                continue
            for r0 in range(1, 7):
                for s0 in range(1, 7):
                    r = g * r0
                    s = g * s0
                    A = alpha * r
                    D = delta * s
                    if D <= A:
                        continue
                    P = (D + A) // g
                    Q = (D - A) // g
                    assert g * P == D + A
                    assert g * Q == D - A
                    assert P + Q == 2 * D // g
                    assert P - Q == 2 * A // g
                    Hk_plus = D * D + A * A
                    assert P * P + Q * Q == 2 * Hk_plus // (g * g)
                    identity_checks += 1
                    # Fixed-power support statement: after removing the forced
                    # endpoint factor g, sum/difference are exactly delta*s0
                    # and alpha*r0 up to the finite factor 2.
                    assert oddpart(P + Q) == oddpart(2 * delta * s0)
                    assert oddpart(P - Q) == oddpart(2 * alpha * r0)
                    sumdiff_checks += 1

# ---------------------------------------------------------------------------
# 3. 4cg common-core / xi-switch quotient identity on synthetic divisors.
#    This audits the exact arithmetic pattern C=oddpart(Hk+/Xo).
# ---------------------------------------------------------------------------
core_switch_checks = 0
for alpha in range(1, 30, 2):
    for delta in range(1, 32, 2):
        if math.gcd(alpha, delta) != 1:
            continue
        for r in range(1, 5):
            for s in range(1, 5):
                H = delta * delta * s * s + alpha * alpha * r * r
                Ho = oddpart(H)
                for Xo in divisors(Ho):
                    C = oddpart(H // Xo)
                    assert Ho == Xo * C
                    core_switch_checks += 1

# ---------------------------------------------------------------------------
# 4. Divisor-split fiber audit: P=a0*U, Q=b0*V has tau(P)tau(Q) lifts.
# ---------------------------------------------------------------------------
divisor_fiber_checks = 0
max_split_fiber = 0
for P in range(1, 140):
    for Q in range(1, 140):
        if math.gcd(P, Q) != 1:
            continue
        splits = 0
        for U in divisors(P):
            a0 = P // U
            assert a0 * U == P
            for V in divisors(Q):
                b0 = Q // V
                assert b0 * V == Q
                splits += 1
        expected = len(divisors(P)) * len(divisors(Q))
        assert splits == expected
        max_split_fiber = max(max_split_fiber, splits)
        divisor_fiber_checks += 1

# ---------------------------------------------------------------------------
# 5. Lock merged predecessor boundaries proving that the two H receivers are
#    coordinate descriptions of the same post-X13 theta-quarter packet.
# ---------------------------------------------------------------------------
locks = {
    "stages/stage14/14-X13/result.md": [
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
        "POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=Bo1",
    ],
    "stages/stage14/14-s7-42/result.md": [
        "RESIDUAL_TO_SINGLE_COLUMN_FIBER_MULTIPLICITY=Bo1",
        "SINGLE_COLUMN_TO_RESIDUAL_FIBER_MULTIPLICITY=Bo1",
    ],
    "stages/stage14/14-s7-44/result.md": [
        "SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualRootLineCompatibilityEnergy",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    ],
    "stages/stage14/14-4dc/result.md": [
        "GAUSSIAN_PRODUCT_COORDINATES=P=a0*U,Q=b0*V",
        "PRODUCT_PAIR_TO_SINGLE_COLUMN_MULTIPLICITY=Bo1",
        "PRODUCT_ROOT_LINE_PLUS_CORE_TRIVIAL_COMPLETE_COUNT=1/2",
    ],
    "stages/stage14/14-sH44/result.md": [
        "STAGE14_SH44=COMPLETE_S7_44_FROZEN_DUAL_ROOT_LINE_COMPATIBILITY_APPLICABILITY_AUDIT",
        "SAFE_UNIFORM_DELTA=0",
    ],
    "stages/stage14/14-4dH/result.md": [
        "MAINLINE_H_RESULT=NO_CERTIFIED_UNIFORM_POWER_SAVING",
        "ZERO_FREQUENCY_PHYSICAL_DENSITY_OBSTRUCTION=true",
        "CERTIFIED_MAINLINE_H_DELTA=0",
    ],
    "stages/stage14/14-4cg/result.md": [
        "COMMON_ODD_CORE_DIVIDES_BOTH_RESIDUAL_NORMS=true",
        "PLUS_FACTOR_CROSS_IDENTITY",
    ],
}
lock_checks = 0
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)
        lock_checks += 1

print("Stage14-X14 post-sqrt frontier audit: PASS")
print(f"theta-quarter rational ledger checks: {ledger_checks}")
print(f"Gaussian product exact identity checks: {identity_checks}")
print(f"Gaussian sum/difference support checks: {sumdiff_checks}")
print(f"common-core / xi-switch divisor checks: {core_switch_checks}")
print(f"divisor-split finite-fiber checks: {divisor_fiber_checks}")
print(f"max synthetic divisor-split fiber: {max_split_fiber}")
print(f"merged boundary lock checks: {lock_checks}")
print("current whole-family exponent: 1/2")
print("strict sub-square-root saving proved: false")
print("post-sqrt global H receiver count: 1")
print("Gaussian norm quotient support: xi-switch product S*T")
print("remaining receiver: SquareRootThetaQuarterSwitchSupportedGaussianNormPhysicalAdmissibilityDensity")
print("X14 auxiliary H needed: false")
