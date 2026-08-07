#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def report() -> dict:
    # b_q - 2 = -4/(q+1), used to show the linear residual is O(q^{-1-sigma}).
    samples = []
    for q in (5, 13, 17, 29, 37, 41):
        bq = Fraction(2 * (q - 1), q + 1)
        samples.append(
            {
                "q": q,
                "b_q": str(bq),
                "b_q_minus_2": str(bq - 2),
                "expected": str(Fraction(-4, q + 1)),
            }
        )

    return {
        "classification": "A_ANALYTIC_CLOSURE_LEMMAS_WRITTEN_FINAL_REVIEW_REQUIRED",
        "bq_identity_samples": samples,
        "j_local_remainder": "O(q^(-1-sigma))+O(q^(-2sigma))",
        "analytic_half_plane": "Re(s)>1/2+epsilon",
        "rectangle_error": (
            "RS(E(R^1/2)+E(S^1/2))+R^(1/2+delta)S+RS^(1/2+delta)"
        ),
        "floor_error_policy": "O(B(log B)^(1+o(1)))",
        "arc_error_policy": "O(B(log B)^(2+o(1)))",
        "status": "PROVISIONALLY_CLOSED_DOCUMENT_PATCHED_FINAL_REVIEW_PENDING",
        "claim_scope": "primitive oriented count only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path)
    args = parser.parse_args()

    data = report()
    for item in data["bq_identity_samples"]:
        assert item["b_q_minus_2"] == item["expected"]
    assert data["analytic_half_plane"] == "Re(s)>1/2+epsilon"

    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
