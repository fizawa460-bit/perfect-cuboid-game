#!/usr/bin/env python3
from __future__ import annotations

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

    survivors = []
    for c in covers:
        matrix = []
        ok = True
        for g in c["groups"]:
            w = set(g["exceptional_labels_1based"])
            row = [len(w & z) for z in zblocks]
            matrix.append(row)
            if row != [8, 8, 8]:
                ok = False
        if ok:
            survivors.append({
                "candidate_indices_zero_based": c["candidate_indices_zero_based"],
                "Z_by_W_node_intersection_matrix": matrix,
                "exceptional_mass_sums": c["exceptional_mass_sums"],
                "groups": [
                    {
                        "rational_labels_1based": g["rational_labels_1based"],
                        "exceptional_labels_1based": g["exceptional_labels_1based"],
                    }
                    for g in c["groups"]
                ],
            })

    print(json.dumps({
        "mode": "SCRATCH_POST1648AW_JOINT_Z_WC_NODE_INCIDENCE",
        "source_exact_incidence": {
            "Z_hyperplane_node_count": 16,
            "WC_hyperplane_node_count": 24,
            "each_Zi_intersect_each_WCj_in_nodes": 8,
            "derivation": "six box-node zero-pattern types from the four defining diagonal quadrics"
        },
        "input_WC_exact_cover_count": len(covers),
        "unique_unordered_Z_partition": True,
        "joint_incidence_survivor_count": len(survivors),
        "joint_incidence_survivors": survivors,
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
