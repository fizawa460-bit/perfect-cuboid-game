#!/usr/bin/env python3
"""Deterministic audit for Stage14-4bx.

Checks only the algebra/exponent bookkeeping of the reoptimization.
The analytic input is the already merged Stage14-4bv packet inequality.
"""

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bx/result.md"
PREV = ROOT / "stages/stage14/14-4bw/result.md"
S709 = ROOT / "stages/stage14/14-s7-09/result.md"


def audit_predecessor_boundaries():
    prev = PREV.read_text()
    s709 = S709.read_text()
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19" in prev
    assert "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=false" in s709
    assert "CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17" in s709


def audit_packet_scale():
    a = Fraction(4, 5)  # L = H^a

    # Relative exponents in one correlation bracket after dividing by A=XY:
    # L^-2, H^-1, L^2/H^2.
    e_lminus2 = -2 * a
    e_hminus1 = Fraction(-1, 1)
    e_l2_h2 = 2 * a - 2
    bracket = max(e_lminus2, e_hminus1, e_l2_h2)
    correlation = 2 * bracket
    diagonal = -a

    assert e_lminus2 == Fraction(-8, 5)
    assert e_l2_h2 == Fraction(-2, 5)
    assert bracket == Fraction(-2, 5)
    assert correlation == Fraction(-4, 5)
    assert diagonal == Fraction(-4, 5)

    # Exact packet-level minimax in a>=1/2: balance -a and 4a-4.
    assert -a == 4 * a - 4
    return -diagonal


def sector_exponents(lam, nu, tau):
    return {
        "small_denominator": 2 * lam,
        "small_numerator": 1 + nu - lam,
        "thick": 1 - Fraction(4, 5) * tau,
        "thin_numerator_cell": 1 - (nu - 2 * tau) / 4,
        "thin_denominator_cell": 1 - (lam - 2 * tau) / 4,
    }


def audit_unconditional_minimax():
    lam = Fraction(15, 32)
    nu = Fraction(13, 32)
    tau = Fraction(5, 64)
    target = Fraction(15, 16)

    assert 0 < 2 * tau < nu <= lam < Fraction(1, 2)
    ex = sector_exponents(lam, nu, tau)
    assert ex["small_denominator"] == target
    assert ex["small_numerator"] == target
    assert ex["thick"] == target
    assert ex["thin_numerator_cell"] == target
    assert ex["thin_denominator_cell"] == Fraction(59, 64)
    assert ex["thin_denominator_cell"] < target

    # Lower-bound certificate for every threshold choice in this architecture.
    # If all active terms <=E then:
    # lambda <= E/2,
    # nu <= 3E/2-1,
    # tau >= 5(1-E)/4,
    # nu >= 2tau+4(1-E) >= 13(1-E)/2.
    E = target
    upper_nu = Fraction(3, 2) * E - 1
    lower_nu = Fraction(13, 2) * (1 - E)
    assert upper_nu == lower_nu == Fraction(13, 32)

    # At any E<15/16 the required lower_nu exceeds the allowed upper_nu.
    test = target - Fraction(1, 10000)
    assert Fraction(13, 2) * (1 - test) > Fraction(3, 2) * test - 1

    return lam, nu, tau, target, ex


def audit_saving_ledger(target):
    old_18_19 = Fraction(18, 19)
    old_20_21 = Fraction(20, 21)
    post_local = Fraction(41, 42)
    sqrt_target = Fraction(1, 2)

    assert old_18_19 - target == Fraction(3, 304)
    assert old_20_21 - target == Fraction(5, 336)
    assert post_local - target == Fraction(13, 336)
    assert target - sqrt_target == Fraction(7, 16)


def audit_updated_conditional_two_cell():
    # If future s7-10 proves the s7-09 two-cell coefficient saving a^(-1/3),
    # combine it with the already proved 4/5 thick saving.
    lam = Fraction(13, 28)
    nu = Fraction(11, 28)
    tau = Fraction(5, 56)
    target = Fraction(13, 14)

    e1 = 2 * lam
    e2 = 1 + nu - lam
    e3 = 1 - Fraction(4, 5) * tau
    e4 = 1 - (nu - 2 * tau) / 3
    e5 = 1 - (lam - 2 * tau) / 3

    assert e1 == e2 == e3 == e4 == target
    assert e5 == Fraction(19, 21)
    assert e5 < target
    return target


def audit_boundary_text():
    txt = RESULT.read_text()
    required = [
        "STAGE14_4BX=REOPTIMIZED_THICK_PACKET_SQUARE_SIEVE_AND_15_16_WHOLE_FAMILY_BOUND",
        "THICK_PACKET_RELATIVE_SAVING=H^(-4/5)",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=15/16",
        "IMPROVEMENT_OVER_18_19=3/304",
        "CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=13/336",
        "S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false",
        "UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
        "SQRT_B_UPPER_BOUND_PROVED=false",
    ]
    for flag in required:
        assert flag in txt, flag


def main():
    audit_predecessor_boundaries()
    packet_saving = audit_packet_scale()
    lam, nu, tau, target, ex = audit_unconditional_minimax()
    audit_saving_ledger(target)
    conditional = audit_updated_conditional_two_cell()
    audit_boundary_text()

    print(f"OPTIMAL_PACKET_RELATIVE_SAVING_EXPONENT={packet_saving}")
    print(f"OPTIMAL_DENOMINATOR_CUTOFF={lam}")
    print(f"OPTIMAL_NUMERATOR_CUTOFF={nu}")
    print(f"OPTIMAL_SQUAREPART_THRESHOLD={tau}")
    print(f"NEW_WHOLE_FAMILY_EXPONENT={target}")
    print(f"THIN_DENOMINATOR_CELL_EXPONENT={ex['thin_denominator_cell']}")
    print(f"UPDATED_CONDITIONAL_TWO_CELL_EXPONENT={conditional}")
    print("MERGED_4BV_PACKET_REOPTIMIZATION_AUDIT=true")
    print("EXACT_15_16_MINIMAX_AUDIT=true")
    print("S7_09_CONDITIONAL_LEDGER_UPDATE_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
