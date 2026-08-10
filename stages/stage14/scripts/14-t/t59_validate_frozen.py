#!/usr/bin/env python3
"""Validate the frozen Stage14-t59 boundary against the generated audit."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
GENERATED = ROOT / "stages/stage14/data/14-t59/orthogonal_rectangle_reduction.json"
FROZEN = ROOT / "stages/stage14/data/14-t59/orthogonal_rectangle_reduction_frozen.json"


def main() -> None:
    generated = json.loads(GENERATED.read_text())
    frozen = json.loads(FROZEN.read_text())

    assert generated["stage"] == frozen["stage"] == "14-t59"
    assert generated["totals"] == frozen["totals"]
    for key, value in frozen["boundary"].items():
        assert generated["decision"][key] == value, (key, generated["decision"].get(key), value)

    assert generated["decision"]["TH16_NEEDED"] is True
    assert generated["decision"]["TH17_NEEDED"] is False
    assert generated["decision"]["T_ROUTE_BLOCKED_WAITING_FOR_TH16"] is False
    assert generated["decision"]["SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED"] is False
    print("Stage14-t59 frozen boundary verified")


if __name__ == "__main__":
    main()
