#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6an_isotrivial_quartic import audit_examples  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    rows = audit_examples()
    assert len(rows) >= 4
    assert all(row["I"] == 12 * row["k"] * row["k"] for row in rows)
    assert all(row["J"] == 0 for row in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6an_isotrivial_quartic.json").read_text())
    assert evidence["qbar_isotrivial"] is True
    assert evidence["universal_geometric_model"] == "Y^2=P^4-Q^4"
    assert evidence["binary_quartic_invariants"]["geometric_j"] == 1728
    assert evidence["theorem_audit"]["species_match"] is True
    assert evidence["theorem_audit"]["applied_in_6an"] is False

    result = (ROOT / "15-6an/result.md").read_text()
    for needle in [
        "STAGE15_6AN_QBAR_ISOTRIVIAL=true",
        "STAGE15_6AN_UNIVERSAL_GEOMETRIC_MODEL=Y^2=P^4-Q^4",
        "STAGE15_6AN_BINARY_QUARTIC_J=0",
        "STAGE15_6AN_GEOMETRIC_J=1728",
        "STAGE15_6AN_HEATH_BROWN_CURVE_THEOREM_SPECIES_MATCH=true",
        "STAGE15_6AN_HEATH_BROWN_THEOREM_APPLIED=false",
        "STAGE15_6AN_EXIT=UNIFORM_DEGREE4_P3_HEIGHT_ADAPTER_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6am/result.md").read_text()
    require(predecessor, "STAGE15_6AM_EXIT=LARGE_COORDINATE_CORE_CONTROLLED_SMALL_KAPPA_QUARTIC_THEOREM_GATE")

    print("STAGE15_6AN_VERIFY=PASS")
    print("QBAR_ISOTRIVIAL=true")
    print("GEOMETRIC_J=1728")
    print("HEATH_BROWN_SPECIES_MATCH=true")
    print("HEATH_BROWN_APPLIED=false")


if __name__ == "__main__":
    main()
