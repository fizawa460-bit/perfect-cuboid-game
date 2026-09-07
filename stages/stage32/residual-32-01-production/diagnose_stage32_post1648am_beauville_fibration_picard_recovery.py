#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
sys.path.insert(0, str(HERE))

from hperp_integral_adapter import (  # noqa: E402
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
    _parse_hperp,
)
from pairing_prefix_engine import close_permutation_group  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def orbit_partition(indices: set[int], group: list[tuple[int, ...]]) -> list[list[int]]:
    out, unseen = [], set(indices)
    while unseen:
        seed = min(unseen)
        orb = {g[seed] for g in group}
        if not orb <= indices:
            raise ValueError("orbit leaves requested population")
        out.append(sorted(orb)); unseen -= orb
    return sorted(out, key=lambda x: (len(x), x))


def key(v: Matrix) -> tuple[int, ...]:
    return tuple(int(v[0, j]) for j in range(v.cols))


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_am_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_am_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T
    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]

    retained_idx = [i - 1 for i in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    kq = Matrix([[degrees[i] for i in retained_idx]]) * gram.inv()
    if any(x.q != 1 for x in kq):
        raise ValueError("canonical class not integral")
    K = Matrix([[int(x) for x in kq]])
    if int((K * gram * K.T)[0, 0]) != 16:
        raise ValueError("K^2 regression")

    group = close_permutation_group(marking["aut_action"]["permutations_1based"])
    normal_orbits = orbit_partition(set(range(92)), group)
    boundary_orbits = [o for o in normal_orbits if len(o) == 12 and {degrees[i] for i in o} == {4}]
    if len(boundary_orbits) != 1:
        raise ValueError("boundary orbit not unique")
    boundary = boundary_orbits[0]

    v6 = json.loads(V6_PATH.read_text())
    C = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    if int((C * gram * K.T)[0, 0]) != 186:
        raise ValueError("V6 K-degree regression")

    rows = []
    fibre_classes: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for i in boundary:
        E = coords.row(i)
        inc = [int(full[i, j]) for j in range(92, 140)]
        if any(x < 0 for x in inc) or sum(inc) != 8 or sum(x > 0 for x in inc) != 8:
            raise ValueError("boundary exceptional incidence regression")
        S = Matrix([[0] * 64])
        for off, mult in enumerate(inc):
            if mult:
                S += mult * coords.row(92 + off)
        B = 2 * E + S
        b_sq = int((B * gram * B.T)[0, 0])
        b_k = int((B * gram * K.T)[0, 0])
        c_b = int((C * gram * B.T)[0, 0])
        if b_sq != 0 or b_k != 8:
            raise ValueError("corrected boundary fibre numerical type moved")
        fibre_classes[key(B)].append(i + 1)
        rows.append({
            "known140_label_1based": i + 1,
            "exceptional_labels_1based": [93 + j for j, x in enumerate(inc) if x],
            "B_square": b_sq,
            "K_dot_B": b_k,
            "C_dot_B_candidate_n": c_b,
            "B_coordinates": list(key(B)),
        })

    clusters = []
    for kv, labels in sorted(fibre_classes.items(), key=lambda x: x[1]):
        B = Matrix([list(kv)])
        clusters.append({
            "labels_1based": labels,
            "size": len(labels),
            "B_square": int((B * gram * B.T)[0, 0]),
            "K_dot_B": int((B * gram * K.T)[0, 0]),
            "C_dot_B_candidate_n": int((C * gram * B.T)[0, 0]),
            "coordinates": list(kv),
        })

    relation = None
    exact = False
    if len(clusters) == 2 and sorted(c["size"] for c in clusters) == [6, 6]:
        B1 = Matrix([clusters[0]["coordinates"]]); B2 = Matrix([clusters[1]["coordinates"]])
        n1 = clusters[0]["C_dot_B_candidate_n"]; n2 = clusters[1]["C_dot_B_candidate_n"]
        relation = {
            "B1_plus_B2_equals_K": B1 + B2 == K,
            "B1_dot_B2": int((B1 * gram * B2.T)[0, 0]),
            "n1": n1, "n2": n2, "n_sum": n1 + n2,
            "ramification_lower_bound_2maxn": 2 * max(n1, n2),
        }
        exact = (
            relation["B1_plus_B2_equals_K"]
            and relation["B1_dot_B2"] == 8
            and relation["n_sum"] == 186
            and all(c["B_square"] == 0 and c["K_dot_B"] == 8 for c in clusters)
        )

    print(json.dumps({
        "mode": "SCRATCH_BEAUVILLE_GENUS5_FIBRE_PICARD_RECOVERY_DIAGNOSTIC",
        "adapter_canonical": adapter.certificate["canonical_sha256_without_this_field"],
        "K_square": 16,
        "normal_aut_orbits": [
            {"size": len(o), "degrees": sorted({degrees[i] for i in o}), "labels_1based": [i+1 for i in o]}
            for o in normal_orbits
        ],
        "boundary_orbit_labels_1based": [i+1 for i in boundary],
        "boundary_rows": rows,
        "genus5_fibre_class_clusters": clusters,
        "beauville_two_fibre_relation": relation,
        "picard_pattern_exact": exact,
        "source_geometry_relation_required_for_n_identification": True,
        "firewalls": {"scratch_only": True, "no_endpoint_credit": True, "Q602_excluded": False, "O210_excluded": False},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
