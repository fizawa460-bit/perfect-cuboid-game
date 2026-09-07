#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AV = HERE / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"
ZDIAG = HERE / "diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py"


def run_json(path: Path) -> dict:
    p = subprocess.run([sys.executable, "-B", str(path)], cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(p.stdout)


def main() -> None:
    av = run_json(AV)
    zd = run_json(ZDIAG)
    zparts = zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"]
    if len(zparts) != 1:
        raise ValueError("Z partition no longer unique")
    zblocks = [set(b["exceptional_labels_1based"]) for b in zparts[0]["blocks"]]
    covers = av["coordinate_W1_W2_W3_C_recovery"]["global_four_hyperplane_exact_covers"]
    wpairs = list(itertools.combinations(range(4), 2))

    survivors = []
    all_patterns = []
    for c in covers:
        wblocks = [set(g["exceptional_labels_1based"]) for g in c["groups"]]
        rows = []
        used_pairs = []
        row_ok = True
        for z in zblocks:
            row = []
            for i, j in wpairs:
                n = len(z & wblocks[i] & wblocks[j])
                row.append(n)
                if n == 8:
                    used_pairs.append((i, j))
            rows.append(row)
            if sorted(row) != [0, 0, 0, 0, 8, 8]:
                row_ok = False
        all_six_once = sorted(used_pairs) == wpairs
        record = {
            "candidate_indices_zero_based": c["candidate_indices_zero_based"],
            "Z_by_Wpair_cell_sizes": rows,
            "used_Wpairs_with_eight_nodes": [list(p) for p in used_pairs],
            "row_pattern_ok": row_ok,
            "all_six_Wpairs_used_exactly_once": all_six_once,
            "exceptional_mass_sums": c["exceptional_mass_sums"],
        }
        all_patterns.append(record)
        if row_ok and all_six_once:
            survivors.append(record)

    print(json.dumps({
        "mode": "SCRATCH_POST1648AW_Z_WPAIR_SUPPORT_CELLS",
        "source_exact_support_design": {
            "node_zero_pattern": "exactly one Zi and exactly two of W1,W2,W3,C vanish",
            "eight_nodes_per_support_type": 8,
            "six_WC_zero_pairs": [list(p) for p in wpairs],
            "required_per_Z_pair_cell_multiset": [0, 0, 0, 0, 8, 8],
            "required_global_pair_usage": "each of the six WC pairs exactly once across the three Z blocks",
        },
        "input_WC_exact_cover_count": len(covers),
        "support_design_survivor_count": len(survivors),
        "support_design_survivors": survivors,
        "all_cover_patterns": all_patterns,
        "firewalls": {
            "scratch_only": True,
            "ordered_coordinate_names_identified": False,
            "sign_level_eight_node_matching_obtained": False,
            "semantic_node_matching_obtained": False,
            "v6_carrier_excluded": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
