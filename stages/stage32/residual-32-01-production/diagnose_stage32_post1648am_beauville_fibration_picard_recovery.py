#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import math
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
    out = []
    unseen = set(indices)
    while unseen:
        seed = min(unseen)
        orb = {g[seed] for g in group}
        if not orb <= indices:
            raise ValueError("orbit leaves requested population")
        out.append(sorted(orb))
        unseen -= orb
    return sorted(out, key=lambda x: (len(x), x))


def vec_list(v: Matrix) -> list[int]:
    return [int(v[0, j]) for j in range(v.cols)]


def gcd_vec(v: Matrix) -> int:
    g = 0
    for x in vec_list(v):
        g = math.gcd(g, abs(x))
    return g


def key(v: Matrix) -> tuple[int, ...]:
    return tuple(vec_list(v))


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_am_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_am_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    q, degree, linear, caps, hmeta = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]

    # Recover the canonical/hyperplane class from its pairings with the retained basis.
    retained_idx = [i - 1 for i in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    k_pair = Matrix([[degrees[i] for i in retained_idx]])
    k_q = k_pair * gram.inv()
    if any(x.q != 1 for x in k_q):
        raise ValueError("canonical class not integral in retained basis")
    K = Matrix([[int(x) for x in k_q]])
    if int((K * gram * K.T)[0, 0]) != 16:
        raise ValueError("K^2 regression")

    gens = marking["aut_action"]["permutations_1based"]
    group = close_permutation_group(gens)
    normal_orbits = orbit_partition(set(range(92)), group)
    orbit_summary = []
    for orb in normal_orbits:
        ds = sorted({degrees[i] for i in orb})
        orbit_summary.append({"size": len(orb), "degrees": ds, "labels_1based": [i + 1 for i in orb]})
    boundary_orbits = [o for o in normal_orbits if len(o) == 12 and {degrees[i] for i in o} == {4}]
    if len(boundary_orbits) != 1:
        raise ValueError(f"boundary orbit not uniquely isolated: {[(len(o), sorted({degrees[i] for i in o})) for o in normal_orbits]}")
    boundary = boundary_orbits[0]

    v6 = json.loads(V6_PATH.read_text())
    C = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    if int((C * gram * K.T)[0, 0]) != 186:
        raise ValueError("V6 K-degree regression")

    rows = []
    primitive_classes: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for i in boundary:
        E = coords.row(i)
        inc = [int(full[i, j]) for j in range(92, 140)]
        if any(x < 0 for x in inc):
            raise ValueError("negative boundary-exceptional incidence")
        S = Matrix([[0] * 64])
        for off, mult in enumerate(inc):
            if mult:
                S += mult * coords.row(92 + off)
        raw = 2 * E + S
        raw_gcd = gcd_vec(raw)
        raw_sq = int((raw * gram * raw.T)[0, 0])
        raw_k = int((raw * gram * K.T)[0, 0])
        row = {
            "known140_label_1based": i + 1,
            "degree": degrees[i],
            "exceptional_incidence_support": sum(x > 0 for x in inc),
            "exceptional_incidence_mass": sum(inc),
            "exceptional_labels_1based": [93 + j for j, x in enumerate(inc) if x > 0],
            "exceptional_intersections": [x for x in inc if x > 0],
            "raw_2E_plus_exc_square": raw_sq,
            "raw_2E_plus_exc_K_degree": raw_k,
            "raw_coordinate_gcd": raw_gcd,
        }
        if raw_gcd >= 2:
            A = raw / 2
            if any(x.q != 1 for x in A):
                raise ValueError("half-corrected class unexpectedly nonintegral")
            A = Matrix([[int(x) for x in A]])
            a_sq = int((A * gram * A.T)[0, 0])
            a_k = int((A * gram * K.T)[0, 0])
            c_a = int((C * gram * A.T)[0, 0])
            row.update({
                "half_corrected_integral": True,
                "A_square": a_sq,
                "K_dot_A": a_k,
                "C_dot_A": c_a,
                "candidate_projection_degree_2CdotA": 2 * c_a,
            })
            primitive_classes[key(A)].append(i + 1)
        else:
            row["half_corrected_integral"] = False
        rows.append(row)

    clusters = []
    for kv, labels in sorted(primitive_classes.items(), key=lambda x: (len(x[1]), x[1])):
        A = Matrix([list(kv)])
        clusters.append({
            "labels_1based": labels,
            "size": len(labels),
            "A_square": int((A * gram * A.T)[0, 0]),
            "K_dot_A": int((A * gram * K.T)[0, 0]),
            "C_dot_A": int((C * gram * A.T)[0, 0]),
            "candidate_n_equals_2CdotA": 2 * int((C * gram * A.T)[0, 0]),
            "coordinates": list(kv),
        })

    beauville_exact = False
    relation = None
    if len(clusters) == 2 and sorted(c["size"] for c in clusters) == [6, 6]:
        A1 = Matrix([clusters[0]["coordinates"]])
        A2 = Matrix([clusters[1]["coordinates"]])
        relation = {
            "two_A_sum_equals_K": 2 * (A1 + A2) == K,
            "A1_dot_A2": int((A1 * gram * A2.T)[0, 0]),
            "n1": clusters[0]["candidate_n_equals_2CdotA"],
            "n2": clusters[1]["candidate_n_equals_2CdotA"],
        }
        relation["n_sum"] = relation["n1"] + relation["n2"]
        beauville_exact = (
            relation["two_A_sum_equals_K"]
            and relation["A1_dot_A2"] == 2
            and relation["n_sum"] == 186
            and all(c["A_square"] == 0 and c["K_dot_A"] == 4 for c in clusters)
        )

    out = {
        "mode": "SCRATCH_BEAUVILLE_FIBRATION_PICARD_RECOVERY_DIAGNOSTIC",
        "adapter_canonical": adapter.certificate["canonical_sha256_without_this_field"],
        "K_square": int((K * gram * K.T)[0, 0]),
        "normal_aut_orbits": orbit_summary,
        "boundary_orbit_labels_1based": [i + 1 for i in boundary],
        "boundary_rows": rows,
        "half_corrected_class_clusters": clusters,
        "beauville_two_pencil_relation": relation,
        "individual_projection_degrees_source_geometry_still_required": True,
        "picard_pattern_exact": beauville_exact,
        "firewalls": {
            "scratch_only": True,
            "pattern_does_not_by_itself_source_identify_pencils": True,
            "no_endpoint_credit": True,
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
