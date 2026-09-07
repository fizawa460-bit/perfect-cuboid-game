#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ST32R = ROOT / "stages" / "stage32" / "residual-32-01-production"
ST33 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"

sys.path.insert(0, str(ST32R))
from pairing_prefix_engine import INDLIST, close_permutation_group  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "ex6_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "ex6_base")
    gram = Matrix(bundle["picard_gram_64x64"])
    raw_perms = marking["aut_action"]["permutations_1based"]
    group1 = close_permutation_group(raw_perms)
    if len(group1) != 1536:
        raise ValueError(f"Aut group order regression: {len(group1)}")

    # Reconstruct the exact 140x140 intersection pairing from the retained
    # primitive 64-basis Gram and the exact Aut action, without exposing the
    # giant retained payloads outside the runner.
    basis = [i - 1 for i in INDLIST]
    known: dict[tuple[int, int], int] = {}
    for bi, a in enumerate(basis):
        for bj, b in enumerate(basis):
            value = int(gram[bi, bj])
            for gp1 in group1:
                gp = [int(x) - 1 for x in gp1]
                key = (gp[a], gp[b])
                prior = known.get(key)
                if prior is not None and prior != value:
                    raise ValueError(f"pairing propagation conflict at {key}: {prior} vs {value}")
                known[key] = value
    if len(known) != 140 * 140:
        raise ValueError(f"incomplete pairing propagation: {len(known)}")

    def pair(i1: int, j1: int) -> int:
        return known[(i1 - 1, j1 - 1)]

    v6 = json.loads(V6_PATH.read_text())
    if v6["canonical_sha256_without_this_field"] != "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8":
        raise ValueError("V6 canonical regression")
    vp = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(vp) != 140:
        raise ValueError("V6 all140 length regression")

    # Stoll--Testa Section 5 representative fib3 has t=0 equations
    # a1+a2=0, b2-b1=0. In cuboids.magma's retained C3 ordering these split
    # into labels 46 and 48. The resolved special fiber contains these two
    # strict transforms joined by their four common exceptional curves.
    c3_labels = (46, 48)
    common_exc = tuple(
        e for e in range(93, 141)
        if pair(c3_labels[0], e) == 1 and pair(c3_labels[1], e) == 1
    )
    if len(common_exc) != 4:
        raise ValueError(f"expected four common exceptional curves, got {common_exc}")
    support = tuple(sorted(c3_labels + common_exc))

    rep_degree = sum(vp[i - 1] for i in support)
    if pair(46, 48) != 0:
        raise ValueError(f"resolved C3 components should be disjoint, pairing={pair(46,48)}")

    orbit_supports: set[tuple[int, ...]] = set()
    degrees: list[int] = []
    shape_failures = []
    for gp1 in group1:
        mapped = tuple(sorted(int(gp1[i - 1]) for i in support))
        orbit_supports.add(mapped)
    for mapped in sorted(orbit_supports):
        normals = [x for x in mapped if 45 <= x <= 92]
        excs = [x for x in mapped if 93 <= x <= 140]
        if len(normals) != 2 or len(excs) != 4:
            shape_failures.append({"support": mapped, "normal_45_92": normals, "exceptional": excs})
        degrees.append(sum(vp[i - 1] for i in mapped))
    if shape_failures:
        raise ValueError(f"Aut image support type regression: {shape_failures[:3]}")

    counts = Counter(degrees)
    result = {
        "schema": "STAGE32_EX6_RANK4_FIBRATION_ORBIT_DEGREE_DIAGNOSTIC_V1",
        "status": "EXPLORATORY_EXACT_DIAGNOSTIC_NO_MAIN_CREDIT",
        "source_locks": {
            "stoll_testa_verification_repo_cuboids_magma_blob": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
            "stoll_testa_section5_log_blob": "9cfef75aa58335655d6ae3e78597f5924b6c2433",
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "v6_all140_pairings_sha256": v6["witness"]["all140_pairings_sha256"],
            "retained_aut_group_order": len(group1),
        },
        "representative": {
            "section5_type": "NEXT_SIX_RANK4_QUADRICS_FIB3_T0",
            "c3_labels": list(c3_labels),
            "common_exceptional_labels": list(common_exc),
            "resolved_special_fiber_support": list(support),
            "v6_intersection_degree": rep_degree,
        },
        "aut_orbit": {
            "distinct_special_fiber_supports": len(orbit_supports),
            "degree_min": min(degrees),
            "degree_max": max(degrees),
            "distinct_degrees": sorted(counts),
            "degree_multiplicities_over_distinct_supports": {str(k): counts[k] for k in sorted(counts)},
            "supports_with_degree_at_least_133": sum(v >= 133 for v in degrees),
            "supports_with_degree_at_least_134": sum(v >= 134 for v in degrees),
        },
        "firewalls": {
            "arbitrary_rank4_fibration_degree_implies_O_ge_2degree": False,
            "new_fibration_O_adapter_proved": False,
            "O266_excluded": False,
            "V6_carrier_excluded": False,
            "stage32_main_changed": False,
            "runner_side_giant_payload_import_only": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
