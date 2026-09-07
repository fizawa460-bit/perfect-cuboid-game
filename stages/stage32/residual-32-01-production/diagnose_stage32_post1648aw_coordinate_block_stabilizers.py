#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(HERE))
from pairing_prefix_engine import close_permutation_group  # noqa: E402

AV = HERE / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"
ZDIAG = HERE / "diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py"


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def run_json(path: Path) -> dict:
    p = subprocess.run([sys.executable, "-B", str(path)], cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(p.stdout)


def image(block: set[int], g: tuple[int, ...]) -> set[int]:
    return {g[i - 1] + 1 for i in block}


def orbit_sizes(points: set[int], group: list[tuple[int, ...]]) -> list[int]:
    unseen = set(points)
    sizes = []
    while unseen:
        a = min(unseen)
        orb = {g[a - 1] + 1 for g in group}
        if not orb <= points:
            raise ValueError("stabilizer orbit escaped exceptional set")
        sizes.append(len(orb))
        unseen -= orb
    return sorted(sizes)


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_aw_stab_marking")
    G = close_permutation_group(marking["aut_action"]["permutations_1based"])
    if len(G) != 1536:
        raise ValueError("retained group order regression")
    av = run_json(AV)
    zd = run_json(ZDIAG)
    zparts = zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"]
    if len(zparts) != 1:
        raise ValueError("Z partition no longer unique")
    zblocks = [set(b["exceptional_labels_1based"]) for b in zparts[0]["blocks"]]
    covers = av["coordinate_W1_W2_W3_C_recovery"]["global_four_hyperplane_exact_covers"]
    exceptional = set(range(93, 141))

    records = []
    for c in covers:
        wblocks = [set(g["exceptional_labels_1based"]) for g in c["groups"]]
        blocks = zblocks + wblocks
        stab = [g for g in G if all(image(b, g) == b for b in blocks)]
        records.append({
            "candidate_indices_zero_based": c["candidate_indices_zero_based"],
            "coordinate_block_pointwise_set_stabilizer_order": len(stab),
            "exceptional_orbit_sizes_under_stabilizer": orbit_sizes(exceptional, stab),
            "exceptional_mass_sums": c["exceptional_mass_sums"],
        })

    histogram = Counter(r["coordinate_block_pointwise_set_stabilizer_order"] for r in records)
    max_order = max(histogram)
    print(json.dumps({
        "mode": "SCRATCH_POST1648AW_COORDINATE_BLOCK_STABILIZERS",
        "retained_group_order": len(G),
        "input_WC_exact_cover_count": len(covers),
        "stabilizer_order_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "maximum_stabilizer_order": max_order,
        "records_at_maximum": [r for r in records if r["coordinate_block_pointwise_set_stabilizer_order"] == max_order],
        "all_records": records,
        "source_comparison_target": {
            "obvious_projective_coordinate_sign_change_group_order": 64,
            "note": "comparison target only; equality is necessary evidence for a sign-level common model, not semantic adapter credit by itself"
        },
        "firewalls": {
            "scratch_only": True,
            "finite_action_adapter_credit": False,
            "semantic_node_matching_obtained": False,
            "v6_carrier_excluded": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
