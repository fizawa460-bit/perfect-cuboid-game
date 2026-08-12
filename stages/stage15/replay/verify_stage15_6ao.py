#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ao_projective_curve_bound import find_witnesses  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    rows = find_witnesses()
    assert len(rows) >= 6
    assert all(math_row["kappa"] > 0 for math_row in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6ao_projective_curve_bound.json").read_text())
    assert evidence["exact_model"] == "TWO_QUADRICS_IN_P3"
    assert evidence["degree"] == 4
    assert evidence["geometrically_integral"] is True
    assert evidence["primary_theorem"]["uniform_in_coefficients"] is True
    assert evidence["averaged_theorem_used"] is False

    result = (ROOT / "15-6ao/result.md").read_text()
    for needle in [
        "STAGE15_6AO_EXACT_P3_MODEL=TWO_QUADRICS",
        "STAGE15_6AO_P3_CURVE_DEGREE=4",
        "STAGE15_6AO_P3_CURVE_GEOMETRICALLY_INTEGRAL=true",
        "STAGE15_6AO_HEATH_BROWN_THEOREM_APPLIED=true",
        "STAGE15_6AO_POINTWISE_KAPPA_FIBER_BOUND=k^(1/8)*Z^(1/4)*B^epsilon",
        "STAGE15_6AO_EXIT=TWO_SIDED_KAPPA_FIBER_COUPLING_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6an/result.md").read_text()
    require(predecessor, "STAGE15_6AN_EXIT=UNIFORM_DEGREE4_P3_HEIGHT_ADAPTER_READY")

    print("STAGE15_6AO_VERIFY=PASS")
    print("P3_DEGREE=4")
    print("UNIFORM_CURVE_THEOREM_APPLIED=true")
    print("POINTWISE_KAPPA_FIBER_EXPONENT_Z=1/4")


if __name__ == "__main__":
    main()
