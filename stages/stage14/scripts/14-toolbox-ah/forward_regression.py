#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LIVE_INDEX = ROOT / "docs/stage14-toolbox/index.json"
ORIGINAL = HERE / "genus_one_geometry_audit.py"
AH_TERMINAL_CARD = "TB-LEDGER-current-main-after-4br"


def load_original():
    spec = importlib.util.spec_from_file_location("toolbox_ah_original", ORIGINAL)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load original toolbox-ah audit")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    data = json.loads(LIVE_INDEX.read_text(encoding="utf-8"))
    cards = data["cards"]
    terminal = next((i for i, c in enumerate(cards) if c["id"] == AH_TERMINAL_CARD), None)
    if terminal is None:
        raise AssertionError(f"missing ah terminal card {AH_TERMINAL_CARD}")

    # Freeze the registry view that existed at the end of toolbox-ah. Later
    # stages may append cards and may also supersede the then-current terminal
    # ledger. Historical ah regression must reconstruct its original metadata
    # rather than treating a legitimate later supersession as a regression.
    frozen = dict(data)
    frozen_cards = [dict(c) for c in cards[: terminal + 1]]
    if len(frozen_cards) != 48:
        raise AssertionError(f"unexpected frozen ah card count {len(frozen_cards)}")
    frozen_terminal = frozen_cards[-1]
    if frozen_terminal["id"] != AH_TERMINAL_CARD:
        raise AssertionError("ah terminal position changed")
    frozen_terminal["status"] = "CURRENT"
    frozen_terminal.pop("superseded_by", None)
    frozen["cards"] = frozen_cards

    mod = load_original()
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "index-ah-frozen.json"
        path.write_text(json.dumps(frozen, indent=2) + "\n", encoding="utf-8")
        mod.INDEX = path
        mod.main()


if __name__ == "__main__":
    main()
