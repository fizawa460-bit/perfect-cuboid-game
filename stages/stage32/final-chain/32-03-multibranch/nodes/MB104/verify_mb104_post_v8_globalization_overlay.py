#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
OVERLAY = NODE / "POST-V8-GLOBALIZATION-OVERLAY.json"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    o = json.loads(OVERLAY.read_text())
    assert o["schema"] == "STAGE32_MB104_POST_V8_GLOBALIZATION_OVERLAY_V1"

    p = o["parent_v8"]
    assert git_blob_sha(ROOT / p["certificate_path"]) == p["certificate_blob_sha1"]
    assert git_blob_sha(ROOT / p["verifier_path"]) == p["verifier_blob_sha1"]

    for item in o["new_source_locks"].values():
        assert git_blob_sha(ROOT / item["path"]) == item["blob_sha1"], item["path"]

    r = o["retained_results"]
    assert r["abstract_D13_exists"] is True
    assert r["numerical_D13_known"] is False
    assert r["any_unbounded_distinct_low_genus_sequence_eventually_has_N_ge_14"] is True
    assert r["beauville_resolved_cover_invariants"] == "Xhat: K^2=-16, c2=64"
    assert r["beauville_minimal_surface_invariants"] == "X: K^2=32, c2=16"
    assert r["miyaoka_surface"] == "minimal X only"

    # Replay the two new executable contracts. Parent V8 remains immutable and
    # independently executable through its own verifier.
    runpy.run_path(str(NODE / "verify_mb104_btva_low_support_finiteness.py"), run_name="__main__")
    runpy.run_path(str(NODE / "verify_mb104_beauville_blowup_bridge.py"), run_name="__main__")

    rd = o["route_decision"]
    assert rd["low_support_N_le_13_abstractly_finite"] is True
    assert rd["low_support_effective_enumeration_released"] is False
    assert rd["remaining_potentially_unbounded_population"] == "N>=14"
    assert rd["next_subobligation"] == "MB104_N_GE_14_GLOBALIZATION_OR_EFFECTIVE_LOW_SUPPORT_BOUND"

    fw = o["credit_firewall"]
    assert fw["mb104_complete"] is False
    assert fw["finite_degree_window_proved_population_wide"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 post-V8 globalization overlay verifier PASS")
    print("retained: N<=13 low-genus subpopulation finite but non-effective")
    print("remaining unbounded route: N>=14")
    print("Beauville bridge: Xhat(-16,64) -> X(32,16) by 48 blowdowns")


if __name__ == "__main__":
    main()
