#!/usr/bin/env python3
"""Verify Stage33 micro-roadmap alignment through V58/V59 with A2.4B current."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROADMAP = HERE.parent / "ROADMAP-33-12-MICROGOALS.md"
STATE = HERE.parent / "MAIN-STATE.json"

def main():
    text = ROADMAP.read_text()
    state = STATE.read_text()
    assert "CURRENT_LOCKED_FRONTIER=V41_THROUGH_V58" in text
    assert "EFFECTIVE_DISCOVERY_ROUTING=V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP" in text
    assert "CURRENT_LEAF=A2.4B_B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX" in text
    assert "V57: the quotient-branch route is reduced exactly" in text
    assert "V58: fixed one-search cap revoked operationally" in text
    assert "no fixed per-object count cap" in text
    assert "Unbounded/open-ended search remains forbidden" in text
    assert "#### A2.4A — reduce the B1 quotient geometry to a finite membership gate — PASS V57" in text
    assert "#### A2.4B — materialize the B1 branch-H1 -> proper14 matrix and solve mask20 membership — CURRENT" in text
    assert "B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX" in text
    assert "`14 x 4` F2 matrix `M`" in text
    assert "`M*x = mask20`" in text
    assert "SOURCE_LOCK_ORDERED_B1_PIC0_2_BASIS_AND_EXACT_PROPER14_GYSIN_IMAGE_PRODUCER" in text
    assert "freeze **only** this B1 quotient route for e3" in text
    assert "must not be promoted to nonexistence of an e3 `H2(mu2)` lift" in text
    assert "Stage33 remains `6/11`" in text
    assert "MERGE_ALLOWED=false" in text
    assert "S33-PW07" in text and "S33-PW04" in text and "S30-WF03" in text
    assert "A2_4B_EXACT_B1_14X4_MATRIX_CONSTRUCTION_WITH_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH" in state
    assert '"stage33_progress":"6/11"' in state
    assert '"merge_allowed":false' in state
    print("PASS: Stage33 roadmap aligned through V58/V59; A2.4B 14x4 B1 membership matrix is current")

if __name__ == "__main__":
    main()
