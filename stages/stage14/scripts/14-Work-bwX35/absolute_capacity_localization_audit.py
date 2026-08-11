#!/usr/bin/env python3
"""Deterministic locks for Stage14-Work-bwX35.

This audit checks only finite logical implications and publication locks.  It does
not numerically simulate the Stage14 families or promote any literature theorem.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-Work-bwX35/result.md"
MATRIX = ROOT / "docs/stage14-toolbox/work-bwX35-receiver-matrix.md"


def require(path: Path, *tokens: str) -> None:
    text = path.read_text(encoding="utf-8")
    missing = [t for t in tokens if t not in text]
    if missing:
        raise AssertionError(f"{path}: missing locks: {missing}")


def audit_upper_envelope_lemma() -> None:
    # Finite-model sanity check for A subset B subset O.
    omega = set(range(12))
    O = {1, 2, 3, 4}
    B = {1, 2, 4}
    A = {1, 4}
    assert A <= B <= O <= omega
    assert len(A) <= len(O)

    # No converse / bounded distortion is licensed by inclusion.
    O2 = set(range(10))
    B2 = {0}
    A2 = {0}
    assert A2 <= B2 <= O2
    assert len(O2) / len(B2) == 10


def audit_endpoint_capacity_threshold() -> None:
    # t140/t141 exponent ledger: capacity exponent is 2*lambda.
    for lam in (0.00, 0.10, 0.20, 0.249):
        assert 2 * lam < 0.5
    assert 2 * 0.25 == 0.5
    for lam in (0.251, 0.30):
        assert 2 * lam > 0.5


def audit_no_cross_promotion() -> None:
    require(
        RESULT,
        "UPPER_ENVELOPE_ABSOLUTE_CAPACITY_LEMMA_PROVED=true",
        "COMMON_ABSOLUTE_CAPACITY_FIRST_PRINCIPLE_PROVED=true",
        "COMMON_ARITHMETIC_RESIDUAL_RECEIVER_ADAPTER_PROVED=false",
        "COMMON_ADAPTER_PROVED=false",
        "SAVING_CROSS_PROMOTABLE=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    )


def audit_q15_boundary() -> None:
    require(
        RESULT,
        "Q15_UNITARY_TO_ORDINARY_TRANSFER_RESOLVED_FOR_UPPER_BOUND=true",
        "Q15_UNITARY_UPPER_ENVELOPE_ADAPTER_COMPLETE=true",
        "Q15_BOUNDED_DISTORTION_UNITARY_ORDINARY_TRANSFER_PROVED=false",
        "Q15_LOCALIZED_DIVISOR_WIDTH_COMPATIBILITY_REMAINS=true",
        "Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=true",
    )


def audit_h_boundary() -> None:
    require(
        RESULT,
        "MAINLINE_H_NEEDED=true",
        "NEW_HEAVY_MAIN_H_NEEDED=false",
        "S_ROUTE_H_NEEDED=false",
        "FIXED_U_H_NEEDED=true",
        "TH32_NEEDED=true",
        "TH32_EXECUTED=false",
        "T_ROUTE_H_BLOCKING=false",
        "WHOLE_MAINLINE_BLOCKED_BY_H=false",
    )


def audit_matrix() -> None:
    require(
        MATRIX,
        "COMMON_ABSOLUTE_CAPACITY_LOCALIZATION_LANGUAGE_PROVED=true",
        "COMMON_ADAPTER_PROVED=false",
        "Q15_UNITARY_TO_ORDINARY_TRANSFER_RESOLVED_FOR_UPPER_BOUND=true",
        "TH32_NEEDED=true",
        "TH32_EXECUTED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    )


def main() -> None:
    audit_upper_envelope_lemma()
    audit_endpoint_capacity_threshold()
    audit_no_cross_promotion()
    audit_q15_boundary()
    audit_h_boundary()
    audit_matrix()
    print("Stage14-Work-bwX35 absolute-capacity localization audit: OK")


if __name__ == "__main__":
    main()
