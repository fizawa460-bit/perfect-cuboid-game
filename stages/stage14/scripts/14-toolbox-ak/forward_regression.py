#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LIVE_INDEX = ROOT / "docs/stage14-toolbox/index.json"
ORIGINAL = HERE / "proof_receiver_dependency_audit.py"
AK_TERMINAL_CARD = "TB-LEDGER-current-whole-family-after-s7-08"


def load_original():
    spec = importlib.util.spec_from_file_location("toolbox_ak_original", ORIGINAL)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load toolbox-ak audit")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    data = json.loads(LIVE_INDEX.read_text(encoding="utf-8"))
    cards = data["cards"]
    terminal = next((i for i, c in enumerate(cards) if c["id"] == AK_TERMINAL_CARD), None)
    if terminal is None:
        raise AssertionError(f"missing ak terminal card {AK_TERMINAL_CARD}")

    frozen = dict(data)
    frozen["cards"] = cards[: terminal + 1]
    if len(frozen["cards"]) != 76:
        raise AssertionError(f"unexpected frozen ak card count {len(frozen['cards'])}")
    frozen["next_stage"] = "Stage14-toolbox-al"
    frozen["next_theme"] = "proof recipe cookbook and receiver checklists"

    mod = load_original()
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "index-ak-frozen.json"
        path.write_text(json.dumps(frozen, indent=2) + "\n", encoding="utf-8")
        mod.INDEX = path
        mod.main()


if __name__ == "__main__":
    main()
