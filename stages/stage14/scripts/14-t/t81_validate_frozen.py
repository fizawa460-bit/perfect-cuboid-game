#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t81/projective_graph_kloosterman_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    assert d["stage"] == "14-t81"
    assert d["local_primes"] == 13
    assert d["fractional_kloosterman_checks"] == 17200
    assert d["affine_mismatch_checks"] == 1446
    assert d["inert_mismatch_zero_checks"] == 492
    assert d["fixed_class_selector_checks"] == 15936
    b = d["boundary"]
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["TH23_NEEDED"] is True
    assert b["TH24_NEEDED"] is False
    assert b["TWO_ADDITIVE_FREQUENCIES_COLLAPSE_TO_ONE"] == "Bo1"
    print("Stage14-t81 frozen boundary OK")


if __name__ == "__main__":
    main()
