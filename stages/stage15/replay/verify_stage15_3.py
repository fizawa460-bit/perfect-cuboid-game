#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_3_compare import (  # noqa: E402
    assert_no_three_mod_four_prime,
    build_summary,
    compact_exact_two,
    crosscheck_with_stage15_1,
)


def main() -> None:
    rows = compact_exact_two(2000)
    crosscheck_with_stage15_1(rows, 2000)
    assert_no_three_mod_four_prime(rows)
    summary = build_summary(rows, [1000, 2000], 2000)

    g1000, g2000 = summary["grid"]
    assert (g1000["M2"], g1000["N2"]) == (1838, 2)
    assert g1000["M2_direction"] == {"a": 500, "b": 833, "c": 505}
    assert g1000["N2_direction"] == {"a": 2, "b": 0, "c": 0}

    assert (g2000["M2"], g2000["N2"]) == (4812, 5)
    assert g2000["M2_direction"] == {"a": 1342, "b": 2136, "c": 1334}
    assert g2000["N2_direction"] == {"a": 2, "b": 2, "c": 1}

    # The exact local lemma predicts no prime 3 mod 4 divisor of R^2.
    for row in rows:
        for p in (3, 7, 11, 19, 23, 31):
            assert row["R2"] % p != 0

    gates = summary["predeclared_interpretation_gates"]
    assert gates["global_slope_gate_pass"] is False
    assert gates["directional_rate_gate_pass"] is False
    assert summary["claims"]["survival_asymptotic_inferred"] is False

    print("STAGE15_3_VERIFY=PASS")
    print("M2_2000=4812")
    print("N2_2000=5")
    print("COMMON_CUTOFF=R<=B")
    print("FINITE_DATA_ASYMPTOTIC_CLAIM=false")


if __name__ == "__main__":
    main()
