#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import pathlib
from typing import Any

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("orbit_mod", HERE / "orbit_dedup_e2a54.py")
orbit_mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(orbit_mod)

SCHEMA = "STAGE32_D8_G0_E2_NUMERICAL_ORBIT_SLICE_V1"


def sha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def aggregate_a_values() -> list[int]:
    d = 8
    e = 2
    values = set()
    for x in range(32 * 2 + 1):
        for y in range(8 * 2 + 1):
            for z in range(8 * 2 + 1):
                if x + y + z != e:
                    continue
                for t in range(4 * 4 + 1):
                    if 8 * y + 16 * z + 16 * t != 8 * d:
                        continue
                    rhs = -24 * x + 32 * y + 96 * z + 120 * t
                    if rhs % 8:
                        continue
                    a = rhs // 8
                    if -40 * x + 112 * y + 264 * z + 304 * t != 8 * (19 * d - 5 * e):
                        continue
                    if a >= 0:
                        values.add(a)
    return sorted(values)


def verify_parent(parent: dict[str, Any], expected_a: int) -> list[dict[str, Any]]:
    assert parent["degree"] == 8 and parent["genus"] == 0
    assert parent["exceptional_mass"] == 2
    assert parent["curve_group_mass"] == expected_a
    assert parent["parent_numerical_class_enumeration_complete"] is True
    assert parent["effectivity_classification_complete"] is False
    assert parent["theorem_credit"] is False and parent["receiver_credit"] is False
    rows = parent["numerical_survivors"]
    assert len(rows) == parent["numerical_survivor_count"]
    assert len({tuple(r["selected_coordinates"]) for r in rows}) == len(rows)
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--action", type=pathlib.Path, required=True)
    ap.add_argument("--a53", type=pathlib.Path, required=True)
    ap.add_argument("--a54", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    action = json.loads(args.action.read_text())
    p53 = json.loads(args.a53.read_text())
    p54 = json.loads(args.a54.read_text())
    orbit_mod.verify_core(core)
    group, action_cert = orbit_mod.verify_permutations(core, action)
    assert len(group) == 1536
    assert aggregate_a_values() == [53, 54]

    s53 = verify_parent(p53, 53)
    s54 = verify_parent(p54, 54)
    all_survivors = [(53, row) for row in s53] + [(54, row) for row in s54]
    selected_keys = [tuple(row["selected_coordinates"]) for _, row in all_survivors]
    assert len(set(selected_keys)) == len(selected_keys)

    I = np.array(core["raw_cross_pairings_with_basis"], dtype=np.int64)
    canonical_groups: dict[tuple[int, ...], list[tuple[int, dict[str, Any]]]] = {}
    for a, row in all_survivors:
        basis = np.array(row["basis_coordinates"], dtype=np.int64)
        iv = tuple(int(x) for x in (I @ basis).tolist())
        can = orbit_mod.canonical_intersection_vector(iv, group)
        canonical_groups.setdefault(can, []).append((a, row))

    orbit_rows = []
    for canonical in sorted(canonical_groups):
        members = canonical_groups[canonical]
        full_orbit = {
            tuple(canonical[orbit_mod.invert_perm(p)[j]] for j in range(140))
            for p in group
        }
        by_a = collections.Counter(a for a, _ in members)
        basis = orbit_mod.recover_basis_from_intersections(core, canonical)
        orbit_rows.append({
            "orbit_id": sha(list(canonical))[:24],
            "canonical_intersection_vector_sha256": sha(list(canonical)),
            "canonical_basis_coordinates": basis,
            "full_aut_orbit_size": len(full_orbit),
            "slice_member_count": len(members),
            "slice_member_count_by_a": {str(k): v for k, v in sorted(by_a.items())},
            "member_survivor_ids": sorted(row["survivor_id"] for _, row in members),
            "full_orbit_entirely_present_in_slice": len(full_orbit) == len(members),
        })

    report = {
        "schema": SCHEMA,
        "degree": 8,
        "genus": 0,
        "exceptional_mass": 2,
        "aggregate_feasible_curve_group_masses": [53, 54],
        "parent_count": 2,
        "a53_survivor_count": len(s53),
        "a54_survivor_count": len(s54),
        "total_distinct_numerical_class_count": len(all_survivors),
        "aut_orbit_count": len(orbit_rows),
        "orbits": orbit_rows,
        "numerical_e2_slice_complete": True,
        "orbit_dedup_e2_slice_complete": True,
        "full_d8g0_row_complete": False,
        "effectivity_classification_complete": False,
        "aut_action": action_cert,
        "parent_summary_sha256": {
            "a53": p53["canonical_sha256"],
            "a54": p54["canonical_sha256"],
        },
        "theorem_credit": False,
        "receiver_credit": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = sha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "a53": len(s53),
        "a54": len(s54),
        "total": len(all_survivors),
        "orbits": len(orbit_rows),
        "orbit_sizes": [r["full_aut_orbit_size"] for r in orbit_rows],
        "entire_orbits_present": [r["full_orbit_entirely_present_in_slice"] for r in orbit_rows],
        "canonical_sha256": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
