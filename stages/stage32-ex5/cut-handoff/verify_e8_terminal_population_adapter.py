#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import e8_terminal_population_adapter as a

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFLIGHT = HERE / "e8-terminal-population-preflight.json"
LOCKS = {
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py": "90ff82ed312dcc0cb32cf207935945f550e29170",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_18_n354_survivor_exceptional_mod8_decomposition.py": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-17-n354-authority-picard64-retarget-v2-evidence.json": "28c4b762c7f96a4898c62751062648cad066578c",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
}


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def main() -> None:
    for path, expected in LOCKS.items():
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")
    p = json.loads(PREFLIGHT.read_text())
    req(p["schema"] == "STAGE32EX5_E8_TERMINAL_POPULATION_PREFLIGHT_V1", "preflight schema drift")
    d = a.describe()
    pop = d["population"]
    req(pop["exceptional_signature_block_count"] == 11318, "e8 block count drift")
    req(pop["terminal_block_width"] == 113 and pop["terminal_count"] == 1278934, "e8 terminal population drift")
    req(pop["raw_selected_parent_candidates_if_all_blocks_materialized"] == 12458750, "whole-population raw parent accounting drift")
    b0 = a.block_signature(0)
    req(b0["terminal_rank_range"] == [0,112] and b0["fixed_exceptional_mass"] == 2 and b0["raw_selected_parent_candidate_count"] == 177100, "first block signature drift")
    b1 = a.block_signature(1)
    req(b1["terminal_rank_range"] == [113,225], "first disjoint block rank drift")
    req(b1["base_terminal"] == [0,1,0,0,0,0,0,1,0,0,1], "first disjoint block terminal drift")
    req(b1["fixed_exceptional_mass"] == 3 and b1["residual_exceptional_mass"] == 5 and b1["raw_selected_parent_candidate_count"] == 42504, "first disjoint block population preflight drift")
    req(p["population"]["terminal_count"] == pop["terminal_count"], "preflight/adapter population drift")
    req(p["credit"]["stage32_main_pruning_credit"] is False and p["credit"]["merge_authorized"] is False, "credit leak")
    print("PASS: Stage32EX5 common e8 terminal population adapter static contract is coherent")
    print("e8_blocks=11318;e8_terminals=1278934;block_width=113;lazy_random_access=YES")
    print("first_disjoint_block=1;terminal_ranks=113..225;raw_parent_candidates=42504")
    print("stage32_main_pruning_credit=NO;merge_authorized=NO")


if __name__ == "__main__":
    main()
