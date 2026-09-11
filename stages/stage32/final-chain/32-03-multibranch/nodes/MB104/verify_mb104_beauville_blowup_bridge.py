#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"


def main() -> None:
    cert = json.loads((NODE / "BEAUVILLE-BLOWUP-BRIDGE.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BEAUVILLE_BLOWUP_BRIDGE_V1"
    s = cert["resolution_surface_S"]
    xh = cert["resolved_double_cover_Xhat"]
    x = cert["minimal_beauville_surface_X"]

    assert s["K2"] == 16 and s["c2"] == 80
    assert s["exceptional_count"] == 48 and s["exceptional_self_intersection"] == -2
    assert xh["B2"] == 48 * (-2) == -96
    assert xh["L2"] == xh["B2"] // 4 == -24
    assert xh["K2"] == 2 * (s["K2"] + xh["L2"]) == -16
    assert xh["c2"] == 2 * s["c2"] - 48 * 2 == 64
    assert xh["ramification_curve_self_intersection"] == -1
    assert x["K2"] == xh["K2"] + 48 == 32
    assert x["c2"] == xh["c2"] - 48 == 16
    assert x["K2_gt_c2"] is True

    ca = cert["carrier_adapter"]
    assert ca["ramification_parity_read_on_Xhat_to_S"] is True
    assert ca["normalization_genus_unchanged_by_ambient_blowdown_Xhat_to_X"] is True
    assert ca["miyaoka_applied_on_minimal_X_only"] is True

    fw = cert["firewalls"]
    assert fw["Xhat_equals_X"] is False
    assert fw["miyaoka_applied_on_Xhat"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 Beauville blow-up bridge verifier PASS")
    print("Xhat: K2=-16 c2=64; blow down 48 ramification (-1)-curves -> X: K2=32 c2=16")


if __name__ == "__main__":
    main()
