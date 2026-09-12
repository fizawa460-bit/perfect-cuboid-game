#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import g3_fibre_parity_lemma as probe


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def main() -> None:
    out = probe.run()
    d = out["derivation"]
    req(out["status"] == "NO_SYMBOLIC_G3_PARITY_CONTRADICTION", "pure fibre parity unexpectedly became sufficient")
    req(d["constraint_rank_representation_found"] is False, "g3 functional unexpectedly entered pure fibre parity row span")
    print(json.dumps({
        "status": "PASS_EXPECTED_NO_PURE_G3_FIBRE_PARITY_RELATION",
        "g3_labels": out["geometry"]["g3_labels"],
        "g3_cell_map": out["geometry"]["g3_label_cell_map_pack1_pack2"],
        "fixed_label_cell_map": out["geometry"]["all_fixed_terminal_label_cell_map_pack1_pack2"],
        "constraint_count": d["constraint_count"],
        "representation_found": d["constraint_rank_representation_found"],
        "next_gate": "use total exceptional mass e=8, fixed_mass>=7, g3=3, nonnegative integral fibre equations, and cross-pack incidence inequality; pure parity alone is insufficient"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
