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
EXPECTED_ACTION_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_PARENT_SCHEMA = "STAGE32_D8_E2_A54_EXACT_NUMERICAL_PARENT_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
EXPECTED_SELECTED_DET = 274877906944
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
SCHEMA = "STAGE32_D8_E2_A54_AUT_ORBIT_DEDUP_V2"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def verify_core(core: dict[str, Any]) -> None:
    assert core["schema"] == EXPECTED_CORE_SCHEMA
    assert core["rank"] == 64
    assert core["known_class_count"] == 140
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    copy = dict(core)
    claimed = copy.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(copy) == claimed


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    # Image convention: i -> p[i], then -> q[p[i]].
    return tuple(q[p[i]] for i in range(len(p)))


def close_permutation_group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
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
                    raise AssertionError("geometric permutation group exceeded expected order")
    return sorted(seen)


def verify_permutations(core: dict[str, Any], action: dict[str, Any]) -> tuple[list[tuple[int, ...]], dict[str, Any]]:
    assert action["schema"] == EXPECTED_ACTION_SCHEMA
    assert action["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert action["permutation_count"] == 9
    copy = dict(action)
    claimed = copy.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(copy) == claimed

    generators = [tuple(int(x) - 1 for x in p) for p in action["permutations_1based"]]
    assert len(generators) == 9
    assert all(sorted(p) == list(range(140)) for p in generators)
    # Automorphisms preserve curve type: 92 nonexceptional known curves and 48 exceptional divisors.
    assert all(all(p[i] < 92 for i in range(92)) for p in generators)
    assert all(all(p[i] >= 92 for i in range(92, 140)) for p in generators)

    K = np.array(core["known_classes"], dtype=np.int64)
    G = np.array(core["basis_gram"], dtype=np.int64)
    I = np.array(core["raw_cross_pairings_with_basis"], dtype=np.int64)
    H = np.array(core["hyperplane"], dtype=np.int64)
    # Bound every integer matrix product far below signed-int64 overflow.
    safety_bound = 64 * int(np.max(np.abs(K))) * int(np.max(np.abs(G))) * int(np.max(np.abs(K)))
    assert safety_bound < 2**62
    assert np.array_equal(K @ G, I)
    known_pairing = I @ K.T
    h_known = I @ H

    for gi, p in enumerate(generators):
        idx = np.array(p, dtype=np.int64)
        # Exact geometric sanity: each source permutation preserves the complete
        # 140x140 intersection matrix and H-degrees.
        if not np.array_equal(known_pairing[np.ix_(idx, idx)], known_pairing):
            raise AssertionError(f"generator {gi+1} does not preserve known-class pairings")
        if not np.array_equal(h_known[idx], h_known):
            raise AssertionError(f"generator {gi+1} does not preserve H-degrees")

    group = close_permutation_group(generators)
    assert len(group) == EXPECTED_GROUP_ORDER
    return group, {
        "generator_count": 9,
        "independently_recomputed_permutation_group_order": len(group),
        "all_generators_preserve_140x140_pairing": True,
        "all_generators_preserve_H_degrees": True,
        "all_generators_preserve_92_48_type_partition": True,
        "source_permutation_canonical_sha256": action["canonical_sha256_without_this_field"],
    }


def invert_perm(p: tuple[int, ...]) -> tuple[int, ...]:
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def canonical_intersection_vector(v: tuple[int, ...], group: list[tuple[int, ...]]) -> tuple[int, ...]:
    # If g sends known class i to p[i], then intersections of g(C) with class j
    # are v[p^{-1}[j]].  Since group is closed under inverse, either orientation
    # gives the identical orbit set; use the explicit inverse convention here.
    best = v
    for p in group:
        inv = invert_perm(p)
        image = tuple(v[inv[j]] for j in range(140))
        if image < best:
            best = image
    return best


def recover_basis_from_intersections(core: dict[str, Any], intersections: tuple[int, ...]) -> list[int]:
    I = Matrix(core["raw_cross_pairings_with_basis"])
    selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
    assert abs(int(selected.det())) == EXPECTED_SELECTED_DET
    target = Matrix([intersections[i] for i in SELECTED_ROWS])
    x = selected.inv() * target
    assert all(sympy.denom(a) == 1 for a in x)
    coords = [int(a) for a in x]
    assert [int(a) for a in I * Matrix(coords)] == list(intersections)
    return coords


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
    group, action_certificate = verify_permutations(core, action)

    assert parent["schema"] == EXPECTED_PARENT_SCHEMA
    assert parent["degree"] == 8 and parent["genus"] == 0
    assert parent["exceptional_mass"] == 2 and parent["curve_group_mass"] == 54
    assert parent["parent_numerical_class_enumeration_complete"] is True
    assert parent["numerical_survivor_count"] == 160
    survivors = parent["numerical_survivors"]
    assert len(survivors) == 160
    assert all(s["known_class_matches_1based"] == [] for s in survivors)

    I = np.array(core["raw_cross_pairings_with_basis"], dtype=np.int64)
    G = np.array(core["basis_gram"], dtype=np.int64)
    H = np.array(core["hyperplane"], dtype=np.int64)
    selected_index = np.array(SELECTED_ROWS, dtype=np.int64)

    grouped: dict[tuple[int, ...], list[dict[str, Any]]] = {}
    for survivor in survivors:
        basis = np.array(survivor["basis_coordinates"], dtype=np.int64)
        intersections_arr = I @ basis
        intersections = tuple(int(x) for x in intersections_arr.tolist())
        assert tuple(int(x) for x in intersections_arr[selected_index].tolist()) == tuple(
            int(x) for x in survivor["selected_coordinates"]
        )
        assert int(basis @ G @ basis) == int(survivor["self_intersection"])
        assert int(H @ G @ basis) == 8
        assert all(0 <= x <= 4 for x in intersections[:92])
        assert all(0 <= x <= 2 for x in intersections[92:])
        canonical = canonical_intersection_vector(intersections, group)
        grouped.setdefault(canonical, []).append(survivor)

    rows = []
    for canonical in sorted(grouped):
        members = sorted(grouped[canonical], key=lambda s: s["survivor_id"])
        canonical_basis = recover_basis_from_intersections(core, canonical)
        basis_np = np.array(canonical_basis, dtype=np.int64)
        assert int(H @ G @ basis_np) == 8
        assert int(basis_np @ G @ basis_np) == -2
        orbit_size = len({
            tuple(canonical[invert_perm(p)[j]] for j in range(140))
            for p in group
        })
        assert EXPECTED_GROUP_ORDER % orbit_size == 0
        rows.append({
            "orbit_id": canonical_sha256(list(canonical))[:24],
            "canonical_intersection_vector_sha256": canonical_sha256(list(canonical)),
            "canonical_basis_coordinates": canonical_basis,
            "canonical_basis_coordinates_sha256": canonical_sha256(canonical_basis),
            "full_aut_orbit_size": orbit_size,
            "stabilizer_order": EXPECTED_GROUP_ORDER // orbit_size,
            "parent_member_count": len(members),
            "parent_member_survivor_ids": [s["survivor_id"] for s in members],
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
            **action_certificate,
            "intersection_representation_injective_rank": 64,
            "selected_64_determinant_abs": EXPECTED_SELECTED_DET,
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
    print(
        json.dumps(
            {
                "input_survivors": 160,
                "orbit_count": len(rows),
                "orbit_sizes": sorted(
                    collections.Counter(r["full_aut_orbit_size"] for r in rows).items()
                ),
                "group_order": len(group),
                "canonical_sha256": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
