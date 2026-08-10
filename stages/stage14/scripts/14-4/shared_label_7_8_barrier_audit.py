#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4cb/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/shared_label_7_8_barrier_summary.json"
PREDECESSOR = ROOT / "stages/stage14/14-s7-13/result.md"
T49 = ROOT / "stages/stage14/14-t49/result.md"


def f_support(g):
    return Fraction(1, 2) + g / 2


def f_two(g):
    return Fraction(1, 1) - g / 6


def main():
    text = RESULT.read_text()
    prev = PREDECESSOR.read_text()
    t49 = T49.read_text()
    data = json.loads(SUMMARY.read_text())

    # merged predecessor locks
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8" in prev
    assert "CRITICAL_SHARED_LABEL_EXPONENT=3/4" in prev
    assert "STAGE14_T49=COMPLETE_EXTERNAL_SPLIT_PRIME_FROBENIUS_AMPLIFIER_AND_NONCIRCULAR_MEAN_SQUARE_REDUCTION" in t49
    assert "GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false" in t49
    assert "TH14_NEEDED=false" in t49

    # exact current crossing
    g = Fraction(3, 4)
    assert f_support(g) == Fraction(7, 8)
    assert f_two(g) == Fraction(7, 8)

    # rational grid: min(support,two-cell) never exceeds 7/8 on 0<=gamma<=1
    worst = Fraction(0, 1)
    where = None
    for den in range(1, 401):
        for num in range(0, den + 1):
            gamma = Fraction(num, den)
            e = min(f_support(gamma), f_two(gamma))
            if e > worst:
                worst = e
                where = gamma
    assert worst == Fraction(7, 8), (worst, where)

    # equality geometry
    alpha = beta = Fraction(3, 8)
    assert alpha + beta == g
    p = q = Fraction(1, 2)
    sx = (p - alpha) / 2
    sy = (q - beta) / 2
    assert sx == sy == Fraction(1, 16)

    # realized-label sparsity contract
    delta = Fraction(1, 12)
    gamma_delta = Fraction(3, 1) / (Fraction(4, 1) - 6 * delta)
    e_delta = Fraction(1, 1) - Fraction(1, 1) / (Fraction(8, 1) - 12 * delta)
    assert gamma_delta == Fraction(6, 7)
    assert e_delta == Fraction(6, 7)
    assert e_delta < Fraction(7, 8)

    for delta in [Fraction(1, 100), Fraction(1, 24), Fraction(1, 12), Fraction(1, 8), Fraction(1, 6)]:
        gd = Fraction(3, 1) / (Fraction(4, 1) - 6 * delta)
        ed = Fraction(1, 1) - Fraction(1, 1) / (Fraction(8, 1) - 12 * delta)
        assert gd <= 1
        assert ed < Fraction(7, 8)

    # stronger transverse coefficient contract
    for eta in [Fraction(1, 100), Fraction(1, 12), Fraction(1, 6)]:
        ge = Fraction(3, 1) / (Fraction(4, 1) + 3 * eta)
        ee = (Fraction(7, 1) + 3 * eta) / (Fraction(8, 1) + 6 * eta)
        assert f_support(ge) == ee
        analytic = Fraction(1, 1) - ge * (Fraction(1, 6) + eta / 2)
        assert analytic == ee
        assert ee < Fraction(7, 8)

    required = [
        "STAGE14_4CB=SHARED_LABEL_COMPRESSION_AND_7_8_CRITICAL_BARRIER",
        "MERGED_S7_13_7_8_IMPORTED=true",
        "MERGED_T49_MEAN_SQUARE_REDUCTION_IMPORTED=true",
        "SHARED_LABEL_SUPPORT_EXPONENT=1/2+gamma/2",
        "SHARED_LABEL_TWO_CELL_EXPONENT=1-gamma/6",
        "SHARED_LABEL_CRITICAL_EXPONENT=3/4",
        "SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8",
        "GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "TH14_NEEDED=false",
        "NEXT=Stage14-4cc",
    ]
    for token in required:
        assert token in text, token

    assert data["current_physical_upper_bound_exponent"] == "7/8"
    assert data["critical_gamma"] == "3/4"
    assert data["architecture_barrier"] == "7/8"
    assert data["example_result"] == "6/7"
    assert data["merged_t49_imported"] is True
    assert data["global_external_two_prime_mean_square_bound_proved"] is False
    assert data["new_whole_family_power_saving_proved"] is False
    assert data["th14_needed"] is False

    print("Stage14-4cb shared-label barrier audit: OK")


if __name__ == "__main__":
    main()
