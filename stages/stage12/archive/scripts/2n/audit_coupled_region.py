#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def report() -> dict:
    # Integral over y,z >= 0, 2 max(y,z) < L, normalized by L=1.
    # By symmetry: 2 * int_0^{1/2} int_0^y (1-2y) dz dy = 1/12.
    volume = 2 * (Fraction(1, 8) - Fraction(1, 12))

    # Shallow region max(y,z) in [(1-tau)/2, 1/2].
    # Normalized fraction relative to total volume is 3 tau^2 - 2 tau^3.
    samples = []
    for numerator in (1, 2, 3, 5, 8):
        tau = Fraction(numerator, 10)
        ratio = 3 * tau * tau - 2 * tau * tau * tau
        samples.append({"tau": str(tau), "ratio": str(ratio)})

    return {
        "classification": "A_FINAL_ROUTE_REPAIRED_AT_STANDARD_ONE_VARIABLE_THEOREM_LEVEL_REVIEW_REQUIRED",
        "normalized_log_volume": str(volume),
        "expected_normalized_log_volume": "1/12",
        "shallow_ratio_formula": "3*tau^2-2*tau^3",
        "shallow_ratio_samples": samples,
        "final_route": [
            "2j_primitive_first",
            "2k_fixed_circle_height",
            "2l_dlb_rejected",
            "2m_iterated_selberg_delange",
            "2n_dyadic_abel_transfer",
        ],
        "poisson_2h_2i_required": False,
        "claim_scope": "algebraic and bookkeeping audit; cited one-variable theorem supplies analytic error",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path)
    args = parser.parse_args()
    data = report()
    assert data["normalized_log_volume"] == "1/12"
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
