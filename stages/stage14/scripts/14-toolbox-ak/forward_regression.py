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
    frozen_cards = [dict(c) for c in cards[: terminal + 1]]
    if len(frozen_cards) != 76:
        raise AssertionError(f"unexpected frozen ak card count {len(frozen_cards)}")

    # Reconstruct the registry semantics at the end of toolbox-ak. Later stages
    # may supersede the terminal ledger, but that must not invalidate the
    # historical ak audit.
    term = frozen_cards[-1]
    if term["id"] != AK_TERMINAL_CARD:
        raise AssertionError("unexpected ak terminal card ordering")
    term["status"] = "CURRENT"
    term.pop("superseded_by", None)
    frozen["cards"] = frozen_cards
    frozen["next_stage"] = "Stage14-toolbox-al"
    frozen["next_theme"] = "proof recipe cookbook and receiver checklists"

    frozen_ledger = """# Frozen toolbox-ak exponent interface\n\n```text\nCURRENT_LOCAL_M_SAVING=1/21\nCURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42\nCURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19\nWHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=23/798\nCURRENT_REMAINING_GAP_TO_SQRT=17/38\nHISTORICAL_4BR_WHOLE_FAMILY_EXPONENT=20/21\nS7_08_OPTIMAL_LAMBDA=9/19\nTB-LEDGER-current-whole-family-after-s7-08 [CURRENT]\n```\n"""

    mod = load_original()
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        index_path = base / "index-ak-frozen.json"
        ledger_path = base / "ledger-ak-frozen.md"
        index_path.write_text(json.dumps(frozen, indent=2) + "\n", encoding="utf-8")
        ledger_path.write_text(frozen_ledger, encoding="utf-8")
        mod.INDEX = index_path
        mod.LEDGER = ledger_path
        mod.main()


if __name__ == "__main__":
    main()
