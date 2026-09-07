#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_aw_z_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_aw_z_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    boundary = list(range(32, 44))
    exceptional = list(range(92, 140))

    inc = {}
    for b in boundary:
        touched = [e for e in exceptional if int(full[b, e]) == 1]
        vals = [int(full[b, e]) for e in exceptional]
        if any(v not in (0, 1) for v in vals) or len(touched) != 8:
            raise ValueError(f"boundary incidence regression at {b+1}")
        inc[b] = touched

    candidates = []
    for comb in itertools.combinations(boundary, 4):
        # Four boundary components of one Zi=0 are separated on the minimal
        # resolution; each of the 16 coordinate nodes lies on two source
        # boundary branches, so the exceptional incidence count is 0 or 2.
        if any(int(full[a, b]) != 0 for a, b in itertools.combinations(comb, 2)):
            continue
        counts = Counter(e for b in comb for e in inc[b])
        if set(counts.values()) != {2} or len(counts) != 16:
            continue
        candidates.append({
            "boundary_labels_1based": [b + 1 for b in comb],
            "exceptional_labels_1based": sorted(e + 1 for e in counts),
        })

    exact_partitions = []
    for inds in itertools.combinations(range(len(candidates)), 3):
        bc = Counter()
        ec = Counter()
        for i in inds:
            bc.update(x - 1 for x in candidates[i]["boundary_labels_1based"])
            ec.update(x - 1 for x in candidates[i]["exceptional_labels_1based"])
        if bc != Counter({b: 1 for b in boundary}):
            continue
        if ec != Counter({e: 1 for e in exceptional}):
            continue
        exact_partitions.append({
            "candidate_indices_zero_based": list(inds),
            "blocks": [candidates[i] for i in inds],
        })

    print(json.dumps({
        "mode": "SCRATCH_POST1648AW_BOUNDARY_Z_HYPERPLANE_BLOCKS",
        "source_geometry": {
            "boundary_curve_count": 12,
            "boundary_nodes_per_curve": 8,
            "Zi_coordinate_hyperplane_count": 3,
            "nodes_per_Zi_from_box_equations": 16,
            "box_node_lies_on_exactly_one_Zi": True,
        },
        "retained": {
            "boundary_labels_1based": [b + 1 for b in boundary],
            "single_Z_hyperplane_candidate_count": len(candidates),
            "single_Z_hyperplane_candidates": candidates,
            "unordered_Z1_Z2_Z3_exact_partition_count": len(exact_partitions),
            "unordered_Z1_Z2_Z3_exact_partitions": exact_partitions,
        },
        "firewalls": {
            "scratch_only": True,
            "ordered_Z1_Z2_Z3_identified": False,
            "semantic_node_matching_obtained": False,
            "v6_carrier_excluded": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
