#!/usr/bin/env python3
"""Deterministic exponent audit for Stage13-13fc.

This does not prove the analytic estimates. It checks the fixed parameter
substitutions and accumulation arithmetic used by the written Gate C lemma.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REPORT = ROOT / "stages/stage13/data/13-13fc/curved_region_error_audit.json"
LEMMA = ROOT / "stages/stage13/13-13fc/curved-region-error-lemma.md"

MESH_POWER = 8
PER_AXIS_RANGE_POWER = 1
PER_AXIS_BOX_POWER = MESH_POWER + PER_AXIS_RANGE_POWER
BOX_COUNT_POWER = 3 * PER_AXIS_BOX_POWER

FINITE_N = 64
BASE_LOG_COST = 2
PER_BOX_FINITE_POWER = BASE_LOG_COST - FINITE_N
ACCUMULATED_FINITE_POWER = BOX_COUNT_POWER + PER_BOX_FINITE_POWER

EPSILON = Fraction(1, 16)
POWER_SAVING = Fraction(1, 4) - EPSILON

SMALL_H = Fraction(2, 1) + Fraction(1, 4)
SMALL_COORD = Fraction(2, 1) + 2 * Fraction(1, 4)
MIXED_SHIFT = Fraction(2, 1)
BOUNDARY = Fraction(3, 1) - MESH_POWER
MESH = Fraction(3, 1) - MESH_POWER


def build_report() -> dict:
    checks = {
        "accumulated_finite_order_remainder_is_o_main": ACCUMULATED_FINITE_POWER < 3,
        "boundary_exponent_is_minus_5": BOUNDARY == -5,
        "box_count_exponent_is_27": BOX_COUNT_POWER == 27,
        "mesh_exponent_is_minus_5": MESH == -5,
        "power_tail_has_stretched_exponential_saving": POWER_SAVING > 0,
        "small_coordinate_exponent_below_3": SMALL_COORD < 3,
        "small_height_exponent_below_3": SMALL_H < 3,
    }

    required_tokens = [
        "BOX_COUNT=O((log B)^27)",
        "FINITE_REMAINDER_N=64",
        "FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)",
        "POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))",
        "CURVED_BOUNDARY=O(B(log B)^-5)+lower-order-ledger",
        "MESH_ERROR=O(B(log B)^-5)",
        "NEXT=13-13fd",
    ]
    lemma = LEMMA.read_text(encoding="utf-8")
    missing_tokens = [token for token in required_tokens if token not in lemma]
    checks["lemma_contract_tokens_present"] = not missing_tokens

    status = "PASS" if all(checks.values()) else "FAIL"

    return {
        "checks": checks,
        "exponents": {
            "accumulated_finite_order_remainder_log_power": ACCUMULATED_FINITE_POWER,
            "boundary_log_power": int(BOUNDARY),
            "box_count_log_power": BOX_COUNT_POWER,
            "mesh_log_power": int(MESH),
            "mixed_log_shift_log_power": int(MIXED_SHIFT),
            "per_box_finite_remainder_log_power": PER_BOX_FINITE_POWER,
            "power_tail_stretched_exponential_coefficient": f"{POWER_SAVING.numerator}/{POWER_SAVING.denominator}",
            "small_coordinate_log_power": f"{SMALL_COORD.numerator}/{SMALL_COORD.denominator}",
            "small_height_log_power": f"{SMALL_H.numerator}/{SMALL_H.denominator}",
        },
        "locks": {
            "BOX_COUNT": "O((log B)^27)",
            "CURVED_BOUNDARY": "O(B(log B)^-5)+lower-order-ledger",
            "FINITE_REMAINDER_AFTER_ALL_BOXES": "O(B(log B)^-35)",
            "MESH_ERROR": "O(B(log B)^-5)",
            "NEXT": "13-13fd",
            "R04_IMMUTABLE": True,
            "R05_REQUIRED": True,
            "STAGE13_13FC": "COMPLETE_CURVED_REGION_ERROR_ACCUMULATION",
            "THEOREM_CHANGED": False,
            "THEOREM_CONTRACT_REOPEN_REQUIRED": False,
        },
        "missing_lemma_tokens": missing_tokens,
        "parameters": {
            "H0": "exp((log B)^(1/4))",
            "U": "exp((log B)^(1/4))",
            "epsilon": "1/16",
            "eta": "(log B)^-8",
            "finite_order_remainder_N": FINITE_N,
            "per_axis_box_log_power": PER_AXIS_BOX_POWER,
        },
        "stage": "13-13fc",
        "status": status,
    }


def canonical_json(data: dict) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-report", action="store_true")
    args = parser.parse_args()

    report = build_report()
    text = canonical_json(report)

    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(text, encoding="utf-8")

    if args.check_report:
        if not REPORT.exists():
            print("missing committed report:", REPORT)
            return 2
        if REPORT.read_text(encoding="utf-8") != text:
            print("committed report is stale; run with --write-report")
            return 3

    print(text, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
