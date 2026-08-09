#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-4bd.

Checks the merged 4bc/s5r interfaces and the exact exponent ledger used to
freeze the complete nonconstant reciprocal error.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PREV = ROOT / "stages/stage14/14-4bc/result.md"
S5R = ROOT / "stages/stage14/14-s5r/result.md"
RESULT = ROOT / "stages/stage14/14-4bd/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/reciprocal_exponent_freeze_summary.json"


def check_flags(path: Path, flags: list[str]) -> None:
    text = path.read_text()
    for flag in flags:
        assert flag in text, (path, flag)


def audit_imports() -> None:
    check_flags(PREV, [
        "FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT=true",
        "ROOT_SAWTOOTH_HANDOFF_BAND=R_E>-1/200",
        "MAIN_TRACK_RECIPROCAL_TARGET_SAVING=1/200",
    ])
    check_flags(S5R, [
        "STAGE14_S5R=COMPLETE_ROOT_SAWTOOTH_SPACING_AND_FULL_LOCAL_CHARACTER_AVERAGE",
        "ROOT_SAWTOOTH_SPACING_BOUND_PROVED=true",
        "CRITICAL_U_SQRTM_V_M_POWER_SAVING_PROVED=true",
        "E_WALSH_SMALL_SIDE_PAIRING_EXACT=true",
        "E_LINEAR_TRANSITION_WEDGE_CLOSED=true",
        "GENUINE_ROOT_SAWTOOTH_RESONANCE_FOUND=false",
        "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true",
        "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED=true",
    ])


def audit_exponents() -> dict[str, Fraction]:
    far = Fraction(3, 20)
    long_edge = Fraction(1, 200)
    mixed_exp = Fraction(733, 400)
    mixed_save = Fraction(2) - mixed_exp
    assert mixed_save == Fraction(67, 400)
    assert mixed_save > Fraction(1, 6)

    # s5r mixed-completion exponent:
    # 1 + 5/4 - 17/40 + 3/400 = 733/400.
    assert (
        Fraction(1)
        + Fraction(5, 4)
        - Fraction(17, 40)
        + Fraction(3, 400)
    ) == mixed_exp

    final_delta = min(far, long_edge, mixed_save)
    assert final_delta == Fraction(1, 200)
    m_exp = Fraction(2) - final_delta
    b_exp = m_exp / 2
    assert m_exp == Fraction(399, 200)
    assert b_exp == Fraction(399, 400)

    # At the old critical point the spacing theorem gives UV=M^(3/2).
    critical = Fraction(1, 2) + Fraction(1)
    assert critical == Fraction(3, 2)
    assert Fraction(2) - critical == Fraction(1, 2)

    return {
        "far": far,
        "long": long_edge,
        "mixed_exp": mixed_exp,
        "mixed_save": mixed_save,
        "final": final_delta,
        "m_exp": m_exp,
        "b_exp": b_exp,
        "critical": critical,
    }


def audit_summary(vals: dict[str, Fraction]) -> None:
    obj = json.loads(SUMMARY.read_text())
    assert obj["stage"] == "14-4bd"
    assert obj["imports"]["stage14_s5r"] is True
    assert obj["root_spacing"]["genuine_resonance_found"] is False
    assert obj["e_walsh"]["small_side_pairing_exact"] is True
    assert obj["sector_ledger"]["far_sector_saving_M"] == "3/20"
    assert obj["sector_ledger"]["near_area_long_edge_saving_M"] == "1/200"
    assert obj["sector_ledger"]["near_area_mixed_completion_saving_M"] == "67/400"
    assert obj["reciprocal_error"]["saving_M"] == "1/200"
    assert obj["reciprocal_error"]["bound_M"] == "M^(399/200+o(1))"
    assert obj["reciprocal_error"]["bound_B"] == "B^(399/400+o(1))"
    assert obj["remaining"]["explicit_nontrivial_rho_loc_proved"] is False
    assert vals["final"] == Fraction(1, 200)
    assert vals["b_exp"] == Fraction(399, 400)


def audit_result() -> None:
    check_flags(RESULT, [
        "STAGE14_4BD=S5R_ROOT_SAWTOOTH_IMPORTED_AND_COMPLETE_RECIPROCAL_EXPONENT_FROZEN",
        "S5R_ROOT_SPACING_THEOREM_IMPORTED=true",
        "ROOT_SAWTOOTH_SPACING_BOUND_PROVED=true",
        "E_WALSH_SMALL_SIDE_PAIRING_EXACT=true",
        "E_LINEAR_TRANSITION_WEDGE_CLOSED=true",
        "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true",
        "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_PROVED=true",
        "ROOT_SPACING_FAR_SECTOR_SAVING_M_SCALE=3/20",
        "NEAR_AREA_LONG_EDGE_SAVING_M_SCALE=1/200",
        "NEAR_AREA_MIXED_COMPLETION_SAVING_M_SCALE=67/400",
        "COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=true",
        "COMPLETE_RECIPROCAL_SAVING_EXPONENT_M_SCALE=1/200",
        "COMPLETE_RECIPROCAL_ERROR_M_SCALE=M^(399/200+o(1))",
        "COMPLETE_RECIPROCAL_ERROR_B_SCALE=B^(399/400+o(1))",
        "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false",
        "NEXT=Stage14-4be",
    ])


def main() -> None:
    audit_imports()
    vals = audit_exponents()
    audit_summary(vals)
    audit_result()
    print("Stage14-4bd reciprocal exponent audit: OK")
    print(f"far-sector saving: {vals['far']}")
    print(f"near-area long-edge saving: {vals['long']}")
    print(f"near-area mixed-completion saving: {vals['mixed_save']}")
    print(f"frozen reciprocal saving: {vals['final']}")
    print(f"M-scale exponent: {vals['m_exp']}")
    print(f"B-scale exponent: {vals['b_exp']}")
    print(f"old critical spacing exponent: {vals['critical']}")


if __name__ == "__main__":
    main()
