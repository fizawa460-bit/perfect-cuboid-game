#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
from typing import Any

from sympy import Matrix

CORE_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
ACTION_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
TIER_SCHEMA = "STAGE32_D8_MATERIALIZED_PARENT_TIER_EXHAUSTIVE_V1"
OUTPUT_SCHEMA = "STAGE32_D8_E8_LOW_TIER_AUT_ORBIT_PARTITION_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
EXPECTED_INPUT_SURVIVORS = 17
EXPECTED_TIER_SHA = "b14f7e70ea962fe00bb8bbe6e459090a1c166414070fa5a875673dc31e22268d"
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_SELECTED_DET = 274877906944


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(q[p[i]] for i in range(len(p)))


def invert_perm(p: tuple[int, ...]) -> tuple[int, ...]:
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def close_group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
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
                assert len(seen) <= EXPECTED_GROUP_ORDER
    assert len(seen) == EXPECTED_GROUP_ORDER
    return sorted(seen)


def verify_core(core: dict[str, Any]) -> None:
    assert core["schema"] == CORE_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert core["rank"] == 64 and core["known_class_count"] == 140
    assert core["h2"] == 16
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed


def verify_action(core: dict[str, Any], action: dict[str, Any]) -> list[tuple[int, ...]]:
    assert action["schema"] == ACTION_SCHEMA
    assert action["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert action["permutation_count"] == 9
    unsigned = dict(action)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed

    generators = [tuple(int(v) - 1 for v in row) for row in action["permutations_1based"]]
    assert len(generators) == 9
    assert all(sorted(p) == list(range(140)) for p in generators)
    assert all(all(p[i] < 92 for i in range(92)) for p in generators)
    assert all(all(p[i] >= 92 for i in range(92, 140)) for p in generators)

    K = Matrix(core["known_classes"])
    G = Matrix(core["basis_gram"])
    I = Matrix(core["raw_cross_pairings_with_basis"])
    H = Matrix([core["hyperplane"]])
    assert K * G == I
    known_pairing = I * K.T
    h_known = H * G * K.T
    for gi, p in enumerate(generators):
        assert all(h_known[0, p[i]] == h_known[0, i] for i in range(140)), gi
        assert all(
            known_pairing[p[i], p[j]] == known_pairing[i, j]
            for i in range(140)
            for j in range(140)
        ), gi
    return close_group(generators)


def prepare_recovery(core: dict[str, Any]) -> tuple[Matrix, Matrix]:
    selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
    assert abs(int(selected.det())) == EXPECTED_SELECTED_DET
    return selected.inv(), Matrix(core["raw_cross_pairings_with_basis"])


def recover_basis(selected_inverse: Matrix, all_intersections: Matrix, image: tuple[int, ...]) -> tuple[int, ...]:
    target = Matrix([image[i] for i in SELECTED_ROWS])
    basis = selected_inverse * target
    assert all(v.q == 1 for v in basis)
    out = tuple(int(v) for v in basis)
    assert tuple(int(v) for v in all_intersections * Matrix(out)) == image
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--action", type=pathlib.Path, required=True)
    ap.add_argument("--tier", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    action = json.loads(args.action.read_text())
    tier = json.loads(args.tier.read_text())
    verify_core(core)
    group = verify_action(core, action)
    inverse_group = [invert_perm(p) for p in group]

    assert tier["schema"] == TIER_SCHEMA
    assert tier["parameters"]["degree"] == 8
    assert tier["parameters"]["genus"] == 0
    assert tier["parameters"]["exceptional_mass"] == 8
    assert tier["parameters"]["curve_group_mass"] == 36
    assert tier["parameters"]["branch_threshold"] == 4
    assert tier["tier_inventory"]["selected_cell_count"] == 5
    assert tier["tier_inventory"]["scheduled_materialized_branch_count"] == 17
    assert tier["tier_complete_numerical_enumeration"] is True
    assert tier["unknown_cell_count"] == 0
    assert tier["exact_numerical_survivor_count_in_complete_tier"] == EXPECTED_INPUT_SURVIVORS
    assert tier["deterministic_sha256_without_runtime"] == EXPECTED_TIER_SHA
    survivors = tier["confirmed_numerical_survivors"]
    assert len(survivors) == EXPECTED_INPUT_SURVIVORS

    G = Matrix(core["basis_gram"])
    I = Matrix(core["raw_cross_pairings_with_basis"])
    H = Matrix([core["hyperplane"]])
    known_set = {tuple(int(v) for v in row) for row in core["known_classes"]}

    input_rows: list[tuple[dict[str, Any], tuple[int, ...]]] = []
    for survivor in survivors:
        basis = tuple(int(v) for v in survivor["basis_coordinates"])
        assert len(basis) == 64
        assert canonical_sha256(list(basis)) == survivor["basis_coordinates_sha256"]
        x = Matrix(basis)
        intersections = tuple(int(v) for v in I * x)
        assert int((H * G * x)[0]) == 8
        assert int((x.T * G * x)[0]) == int(survivor["self_intersection"])
        assert all(0 <= v <= 4 for v in intersections[:92])
        assert all(0 <= v <= 2 for v in intersections[92:])
        assert sum(intersections[92:]) == 8
        assert sum(intersections[:46]) == 36
        assert sum(intersections[:92]) + 5 * sum(intersections[92:]) == 19 * 8
        assert basis not in known_set
        input_rows.append((survivor, intersections))

    # Partition all 17 input survivors by their full source-locked Aut(S) orbit
    # in the injective 140-intersection representation.
    partitions: dict[tuple[int, ...], dict[str, Any]] = {}
    for survivor, intersections in input_rows:
        orbit = {
            tuple(intersections[inv[j]] for j in range(140))
            for inv in inverse_group
        }
        representative = min(orbit)
        bucket = partitions.setdefault(representative, {"orbit": orbit, "inputs": []})
        assert bucket["orbit"] == orbit
        bucket["inputs"].append(survivor)

    assert len(partitions) == 2
    orbit_sets = [bucket["orbit"] for bucket in partitions.values()]
    assert orbit_sets[0].isdisjoint(orbit_sets[1])

    selected_inverse, all_intersections = prepare_recovery(core)
    orbit_rows: list[dict[str, Any]] = []
    for representative, bucket in partitions.items():
        orbit: set[tuple[int, ...]] = bucket["orbit"]
        inputs: list[dict[str, Any]] = bucket["inputs"]
        square_values = {int(row["self_intersection"]) for row in inputs}
        assert len(square_values) == 1
        expected_square = next(iter(square_values))
        a_distribution: collections.Counter[int] = collections.Counter()
        recovered_basis_shas: list[str] = []
        for image in sorted(orbit):
            basis = recover_basis(selected_inverse, all_intersections, image)
            x = Matrix(basis)
            degree = int((H * G * x)[0])
            square = int((x.T * G * x)[0])
            assert degree == 8
            assert square == expected_square
            assert all(0 <= v <= 4 for v in image[:92])
            assert all(0 <= v <= 2 for v in image[92:])
            assert sum(image[92:]) == 8
            assert sum(image[:92]) + 5 * sum(image[92:]) == 19 * 8
            assert basis not in known_set
            a_distribution[sum(image[:46])] += 1
            recovered_basis_shas.append(canonical_sha256(list(basis)))

        input_source_cells = collections.Counter(row["source_cell_id"] for row in inputs)
        orbit_rows.append({
            "input_survivor_count": len(inputs),
            "input_source_cell_distribution": dict(sorted(input_source_cells.items())),
            "self_intersection": expected_square,
            "full_aut_orbit_size": len(orbit),
            "stabilizer_order": EXPECTED_GROUP_ORDER // len(orbit),
            "a_distribution": {str(k): v for k, v in sorted(a_distribution.items())},
            "exceptional_mass_distribution": {"8": len(orbit)},
            "representative_intersection_sha256": canonical_sha256(list(representative)),
            "representative_normal_intersection_histogram": {
                str(k): v for k, v in sorted(collections.Counter(representative[:92]).items())
            },
            "representative_exceptional_intersection_histogram": {
                str(k): v for k, v in sorted(collections.Counter(representative[92:]).items())
            },
            "recovered_basis_set_sha256": canonical_sha256(sorted(recovered_basis_shas)),
            "all_orbit_members_integral_picard_classes": True,
            "all_orbit_members_new_against_known_140": True,
        })

    orbit_rows.sort(key=lambda row: row["full_aut_orbit_size"])
    assert [(r["input_survivor_count"], r["full_aut_orbit_size"], r["self_intersection"]) for r in orbit_rows] == [
        (1, 6, 0), (16, 192, -4)
    ]
    assert orbit_rows[0]["stabilizer_order"] == 256
    assert orbit_rows[0]["a_distribution"] == {"32": 1, "36": 5}
    assert orbit_rows[0]["input_source_cell_distribution"] == {"0451bcae6084559bbb842530": 1}
    assert orbit_rows[1]["stabilizer_order"] == 8
    assert orbit_rows[1]["a_distribution"] == {"34": 64, "36": 128}
    assert orbit_rows[1]["input_source_cell_distribution"] == {
        "612fc6a73210c2a70b0c380b": 8,
        "8cc0a35d77aec9b61a0113f4": 8,
    }

    report = {
        "schema": OUTPUT_SCHEMA,
        "source_tier": {
            "workflow_run": 32679056299,
            "deterministic_sha256_without_runtime": EXPECTED_TIER_SHA,
            "input_survivor_count": EXPECTED_INPUT_SURVIVORS,
        },
        "source_lock": {
            "git_blob_sha1": EXPECTED_BLOB,
            "aut_generator_count": 9,
            "independently_recomputed_aut_order": len(group),
            "selected_inverse_computed_once": True,
            "orbit_partition_in_140_intersection_representation": True,
        },
        "partition": {
            "input_survivor_count": EXPECTED_INPUT_SURVIVORS,
            "full_aut_orbit_count": len(orbit_rows),
            "full_aut_orbit_sizes": [r["full_aut_orbit_size"] for r in orbit_rows],
            "full_aut_orbit_union_size": sum(r["full_aut_orbit_size"] for r in orbit_rows),
            "orbits_pairwise_disjoint": True,
            "orbits": orbit_rows,
        },
        "scope": "E8_A36_LOW_BRANCH_TIER_NUMERICAL_AUT_ORBIT_PARTITION_ONLY",
        "effectivity_classification_complete": False,
        "actual_curve_existence_claim": False,
        "full_parent_complete": False,
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "FULL_D8_G0_ROW_COMPLETE": False,
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
        "aut_order": len(group),
        "input_survivors": EXPECTED_INPUT_SURVIVORS,
        "orbit_count": len(orbit_rows),
        "orbit_sizes": [r["full_aut_orbit_size"] for r in orbit_rows],
        "input_counts": [r["input_survivor_count"] for r in orbit_rows],
        "a_distributions": [r["a_distribution"] for r in orbit_rows],
        "canonical_sha256": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
