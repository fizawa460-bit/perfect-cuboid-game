#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
from typing import Any

import numpy as np
import sympy
from sympy import Matrix

EXPECTED_CORE_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
EXPECTED_ACTION_SCHEMA = "STAGE32_AUT_ACTION_SOURCELOCK_V1"
EXPECTED_PARENT_SCHEMA = "STAGE32_D8_E2_A54_EXACT_NUMERICAL_PARENT_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
SCHEMA = "STAGE32_D8_E2_A54_AUT_ORBIT_DEDUP_V1"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify_core(core: dict[str, Any]) -> None:
    assert core["schema"] == EXPECTED_CORE_SCHEMA
    assert core["rank"] == 64
    assert core["known_class_count"] == 140
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    copy = dict(core)
    claimed = copy.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(copy) == claimed


def verify_action(core: dict[str, Any], action: dict[str, Any]) -> tuple[list[np.ndarray], list[tuple[int, ...]]]:
    assert action["schema"] == EXPECTED_ACTION_SCHEMA
    assert action["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert action["magma_group_order"] == EXPECTED_GROUP_ORDER
    assert action["generator_count"] == 9
    copy = dict(action)
    claimed = copy.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(copy) == claimed

    G = Matrix(core["basis_gram"])
    H = Matrix([core["hyperplane"]])
    known = [tuple(int(x) for x in row) for row in core["known_classes"]]
    known_index = {row: i for i, row in enumerate(known)}
    assert len(known_index) == 140

    generators_np: list[np.ndarray] = []
    induced: list[tuple[int, ...]] = []
    for gi, raw in enumerate(action["generators"]):
        M = Matrix(raw)
        assert M.shape == (64, 64)
        assert M * G * M.T == G
        assert H * M == H
        assert abs(int(M.det())) == 1
        arr = np.array(raw, dtype=np.int64)
        perm = []
        for row in known:
            vec = np.array(row, dtype=np.int64)
            image = tuple(int(x) for x in (vec @ arr).tolist())
            if image not in known_index:
                raise AssertionError(f"generator {gi+1} does not permute the 140 known classes")
            perm.append(known_index[image])
        assert sorted(perm) == list(range(140))
        generators_np.append(arr)
        induced.append(tuple(perm))
    return generators_np, induced


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    # Apply p first, then q.
    return tuple(q[p[i]] for i in range(len(p)))


def permutation_group_order(generators: list[tuple[int, ...]]) -> int:
    identity = tuple(range(140))
    seen = {identity}
    queue = collections.deque([identity])
    while queue:
        current = queue.popleft()
        for gen in generators:
            nxt = compose(current, gen)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
                if len(seen) > EXPECTED_GROUP_ORDER:
                    raise AssertionError("induced permutation group exceeded expected order")
    return len(seen)


def full_orbit(seed: tuple[int, ...], generators: list[np.ndarray]) -> set[tuple[int, ...]]:
    seen = {seed}
    queue = collections.deque([seed])
    while queue:
        current = queue.popleft()
        vec = np.array(current, dtype=np.int64)
        for gen in generators:
            image_arr = vec @ gen
            if int(np.max(np.abs(image_arr))) > 10**12:
                raise AssertionError("unexpected coordinate growth in finite Aut orbit")
            image = tuple(int(x) for x in image_arr.tolist())
            if image not in seen:
                seen.add(image)
                queue.append(image)
                if len(seen) > EXPECTED_GROUP_ORDER:
                    raise AssertionError("vector orbit exceeded Aut(S) order")
    return seen


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--action", type=pathlib.Path, required=True)
    ap.add_argument("--parent-summary", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    action = json.loads(args.action.read_text())
    parent = json.loads(args.parent_summary.read_text())
    verify_core(core)
    generators, induced = verify_action(core, action)
    independent_order = permutation_group_order(induced)
    assert independent_order == EXPECTED_GROUP_ORDER

    assert parent["schema"] == EXPECTED_PARENT_SCHEMA
    assert parent["degree"] == 8 and parent["genus"] == 0
    assert parent["exceptional_mass"] == 2 and parent["curve_group_mass"] == 54
    assert parent["parent_numerical_class_enumeration_complete"] is True
    assert parent["numerical_survivor_count"] == 160
    survivors = parent["numerical_survivors"]
    assert len(survivors) == 160
    assert all(s["known_class_matches_1based"] == [] for s in survivors)

    orbit_cache: dict[tuple[int, ...], tuple[int, ...]] = {}
    orbit_sizes: dict[tuple[int, ...], int] = {}
    grouped: dict[tuple[int, ...], list[dict[str, Any]]] = {}

    for survivor in survivors:
        basis = tuple(int(x) for x in survivor["basis_coordinates"])
        canonical = orbit_cache.get(basis)
        if canonical is None:
            orbit = full_orbit(basis, generators)
            canonical = min(orbit)
            size = len(orbit)
            assert EXPECTED_GROUP_ORDER % size == 0
            orbit_sizes[canonical] = size
            for image in orbit:
                prior = orbit_cache.get(image)
                if prior is not None:
                    assert prior == canonical
                orbit_cache[image] = canonical
        grouped.setdefault(canonical, []).append(survivor)

    rows = []
    for canonical in sorted(grouped):
        members = sorted(grouped[canonical], key=lambda s: s["survivor_id"])
        size = orbit_sizes[canonical]
        rows.append({
            "orbit_id": canonical_sha256(list(canonical))[:24],
            "canonical_basis_coordinates": list(canonical),
            "canonical_basis_coordinates_sha256": canonical_sha256(list(canonical)),
            "full_aut_orbit_size": size,
            "stabilizer_order": EXPECTED_GROUP_ORDER // size,
            "parent_member_count": len(members),
            "parent_member_survivor_ids": [s["survivor_id"] for s in members],
            "parent_member_basis_sha256": canonical_sha256([s["basis_coordinates"] for s in members]),
        })

    all_member_ids = [sid for row in rows for sid in row["parent_member_survivor_ids"]]
    assert len(all_member_ids) == 160
    assert len(set(all_member_ids)) == 160
    assert set(all_member_ids) == {s["survivor_id"] for s in survivors}

    report = {
        "schema": SCHEMA,
        "source_parent": {
            "degree": 8,
            "genus": 0,
            "exceptional_mass": 2,
            "curve_group_mass": 54,
            "numerical_survivor_count": 160,
            "parent_summary_canonical_sha256": parent["canonical_sha256"],
        },
        "aut_action": {
            "source_blob_sha1": EXPECTED_BLOB,
            "generator_count": 9,
            "magma_reported_group_order": action["magma_group_order"],
            "independently_recomputed_permutation_group_order": independent_order,
            "action_canonical_sha256": action["canonical_sha256_without_this_field"],
            "all_generators_preserve_gram": True,
            "all_generators_fix_hyperplane": True,
            "all_generators_permute_140_known_classes": True,
        },
        "input_numerical_survivor_count": 160,
        "aut_orbit_count_intersecting_parent": len(rows),
        "orbits": rows,
        "parent_orbit_dedup_complete": True,
        "full_d8g0_row_complete": False,
        "effectivity_classification_complete": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = canonical_sha256(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "input_survivors": 160,
        "orbit_count": len(rows),
        "orbit_sizes": sorted(collections.Counter(r["full_aut_orbit_size"] for r in rows).items()),
        "group_order": independent_order,
        "canonical_sha256": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
