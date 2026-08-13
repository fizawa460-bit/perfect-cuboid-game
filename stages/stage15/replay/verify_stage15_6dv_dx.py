#!/usr/bin/env python3
from __future__ import annotations

from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE15 = ROOT / "stages/stage15"


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing marker: {needle}")


def main() -> None:
    dv = (STAGE15 / "15-6dv/result.md").read_text(encoding="utf-8")
    dw = (STAGE15 / "15-6dw/result.md").read_text(encoding="utf-8")
    dx = (STAGE15 / "15-6dx/result.md").read_text(encoding="utf-8")

    for needle in (
        "STAGE15_6DV_RESIDUAL_FORMS_EXACT=true",
        "STAGE15_6DV_DECORATED_DE_PRESERVED=true",
        "STAGE15_6DV_CELL_COEFFICIENT_REMOVAL_MOD_Q_EXACT=true",
        "STAGE15_6DV_COMPLEMENTARY_SWITCH_MULTIPLICITY_ONE=true",
        "STAGE15_6DV_SWITCH_COMMUTES_WITH_6CF=true",
        "STAGE15_6DV_INTEGER_SWITCH_EQUIVALENT_TO_6CF=true",
        "STAGE15_6DV_NEW_SIZE_GAIN_PROVED=false",
        "STAGE15_6DV_BRANCH_COMPLETION_POSTFILTER_ONLY=true",
    ):
        require(dv, needle)

    for needle in (
        "STAGE15_6DW_LARGE_SWITCH_EQUIVALENT_TO_6CI=true",
        "STAGE15_6DW_CELL_ADAPTER_EXPONENT_NEUTRAL=true",
        "STAGE15_6DW_INVERSE_D0_MOMENT_PROVED=false",
        "STAGE15_6DW_SMALL_ROOT_LINE_INDEX_UNCHANGED=true",
        "STAGE15_6DW_SMALL_FRINGE_POWER_GAIN_PROVED=false",
        "STAGE15_6DW_DELTA_PROVED=false",
        "STAGE15_6DW_SIGMA_PROVED=false",
        "STAGE15_6DW_NEGATIVE_CERTIFICATE=CURRENT_INPUT_EQUIVALENCE",
    ):
        require(dw, needle)

    for needle in (
        "STAGE15_6DX_RESIDUAL_SWITCH_NEGATIVE_CERTIFICATE_FROZEN=true",
        "STAGE15_6DX_ARSENAL_TRIGGER_SEARCH=true",
        "STAGE15_6DX_EXACT_RECONSTRUCTION_SEARCH=true",
        "STAGE15_6DX_EXHAUSTIVE_VIEW_AUDIT=true",
        "STAGE15_6DX_BLIND_REDISCOVERY=true",
        "STAGE15_6DX_SELECTED_ROUTE=RECONSTRUCTED_BASE_FIXED_PRIME_OVERLAP_SIEVE",
        "STAGE15_6DX_PARKING_ALLOWED=false",
        "STAGE15_6DX_SPLIT_TRIGGER=false",
        "CURRENT_SUBSTAGE=Stage15-6dx",
    ):
        require(dx, needle)

    # Regression for the exact ambient/cell complementary identity from 6cv.
    # This point is used only for algebraic switch verification, not asserted
    # here to be an exact Stage15 survivor.
    a = b = c = d = 1
    H = a * b * c * d
    M, N, U, V = 77, 36, 71, 65

    fsp = (a * b * M) ** 2 + (c * d * N) ** 2
    tsm = abs((a * c * U) ** 2 - (b * d * V) ** 2)
    fom = abs((a * b * M) ** 2 - (c * d * N) ** 2)
    top = (a * c * U) ** 2 + (b * d * V) ** 2

    d_s = gcd(fsp, tsm)
    e_o = gcd(fom, top)
    assert (d_s, e_o) == (17, 4633)
    q = d_s * e_o
    assert gcd(q, H) == 1

    u_s, v_s = fsp // d_s, tsm // d_s
    u_o, v_o = fom // e_o, top // e_o
    assert (u_s, v_s, u_o, v_o) == (425, 48, 1, 2)

    delta_mn = abs((a * b * M) ** 4 - (c * d * N) ** 4)
    delta_uv = abs((a * c * U) ** 4 - (b * d * V) ** 4)
    assert fsp * fom == delta_mn
    assert tsm * top == delta_uv
    assert q * q * u_s * v_s * u_o * v_o == delta_mn * delta_uv

    # The cell map is literally the ambient four-form map in this witness.
    m, n, r, s = a * b * M, c * d * N, a * c * U, b * d * V
    assert fsp == m * m + n * n
    assert tsm == abs(r * r - s * s)
    assert fom == abs(m * m - n * n)
    assert top == r * r + s * s

    print("Stage15-6 residual cell switch dv-dx: PASS")


if __name__ == "__main__":
    main()
