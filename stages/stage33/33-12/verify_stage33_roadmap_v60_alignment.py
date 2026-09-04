#!/usr/bin/env python3
"""Replay the historical V60 roadmap checkpoint without pinning the live frontier to V60."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROADMAP = HERE.parent / "ROADMAP-33-12-MICROGOALS.md"
STATE = HERE.parent / "MAIN-STATE.json"

def main():
    text = ROADMAP.read_text()
    state = json.loads(STATE.read_text())
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

    # The roadmap above is an immutable V60 planning checkpoint.  A later live
    # frontier is valid as long as the global credit firewalls are preserved.
    assert state["stage33_progress"] == "6/11"
    assert state["firewalls"]["merge_allowed"] is False
    assert state["firewalls"]["stage33_12_closed_exact"] is False
    assert state["authority_sync"]["frontier_authority"] == "V65_J1_ONE_BIT_DISCRIMINATOR_GATE"
    print("PASS: historical V60 roadmap replayed; live frontier may advance beyond V60 under preserved firewalls")

if __name__ == "__main__":
    main()
