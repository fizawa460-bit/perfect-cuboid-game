#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
from sympy import Matrix

CORE_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
ACTION_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
PARENT_SCHEMA = "STAGE32_D8_E10_A30_FULL_PARENT_NUMERICAL_CENSUS_V1"
OUT_SCHEMA = "STAGE32_D8_E10_A30_FULL_PARENT_AUT_ORBIT_PARTITION_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_SELECTED_DET = 274877906944


def csha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def compose(p, q):
    return tuple(q[p[i]] for i in range(len(p)))


def invert(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def close(gens):
    ident = tuple(range(140))
    seen = {ident}
    queue = collections.deque([ident])
    while queue:
        cur = queue.popleft()
        for gen in gens:
            nxt = compose(cur, gen)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
                assert len(seen) <= EXPECTED_GROUP_ORDER
    assert len(seen) == EXPECTED_GROUP_ORDER
    return sorted(seen)


def verify_core(core):
    assert core["schema"] == CORE_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert core["rank"] == 64 and core["known_class_count"] == 140 and core["h2"] == 16
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert csha(unsigned) == claimed


def verify_action(core, action):
    assert action["schema"] == ACTION_SCHEMA
    assert action["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert action["permutation_count"] == 9
    unsigned = dict(action)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert csha(unsigned) == claimed
    gens = [tuple(int(v) - 1 for v in row) for row in action["permutations_1based"]]
    assert all(sorted(p) == list(range(140)) for p in gens)
    assert all(
        all(p[i] < 92 for i in range(92))
        and all(p[i] >= 92 for i in range(92, 140))
        for p in gens
    )
    K = Matrix(core["known_classes"])
    G = Matrix(core["basis_gram"])
    I = Matrix(core["raw_cross_pairings_with_basis"])
    H = Matrix([core["hyperplane"]])
    assert K * G == I
    kp = I * K.T
    hk = H * G * K.T
    for p in gens:
        assert all(hk[0, p[i]] == hk[0, i] for i in range(140))
        assert all(
            kp[p[i], p[j]] == kp[i, j]
            for i in range(140)
            for j in range(140)
        )
    return close(gens)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--action", type=pathlib.Path, required=True)
    ap.add_argument("--parent", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    action = json.loads(args.action.read_text())
    parent = json.loads(args.parent.read_text())
    verify_core(core)
    group = verify_action(core, action)
    inverse_group = [invert(p) for p in group]

    assert parent["schema"] == PARENT_SCHEMA
    assert parent["e10_a30_parent_complete"] is True
    assert parent["parent_inventory"]["signature_cell_count"] == 134
    assert parent["parent_inventory"]["total_materialized_branch_count"] == 11205888
    survivors = parent["numerical_survivors"]
    assert len(survivors) == parent["exact_numerical_survivor_count"]

    G = Matrix(core["basis_gram"])
    I = Matrix(core["raw_cross_pairings_with_basis"])
    H = Matrix([core["hyperplane"]])
    known = {tuple(map(int, row)) for row in core["known_classes"]}
    input_map = {}
    for survivor in survivors:
        basis = tuple(map(int, survivor["basis_coordinates"]))
        assert csha(list(basis)) == survivor["basis_coordinates_sha256"]
        x = Matrix(basis)
        intersections = tuple(int(v) for v in I * x)
        assert int((H * G * x)[0]) == 8
        assert int((x.T * G * x)[0]) == int(survivor["self_intersection"])
        assert all(0 <= v <= 4 for v in intersections[:92])
        assert all(0 <= v <= 2 for v in intersections[92:])
        assert sum(intersections[92:]) == 10
        assert sum(intersections[:46]) == 30
        assert sum(intersections[:92]) + 5 * sum(intersections[92:]) == 152
        assert basis not in known
        assert intersections not in input_map
        input_map[intersections] = survivor

    selected = Matrix(
        [core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS]
    )
    assert abs(int(selected.det())) == EXPECTED_SELECTED_DET
    selected_inverse = selected.inv()

    def recover(image):
        target = Matrix([image[i] for i in SELECTED_ROWS])
        basis = selected_inverse * target
        assert all(v.q == 1 for v in basis)
        out = tuple(int(v) for v in basis)
        assert tuple(int(v) for v in I * Matrix(out)) == image
        return out

    remaining = set(input_map)
    input_keys = set(input_map)
    full_seen = set()
    orbit_rows = []
    while remaining:
        seed = min(remaining)
        orbit = {
            tuple(seed[inv[j]] for j in range(140))
            for inv in inverse_group
        }
        assert not (orbit & full_seen)
        full_seen |= orbit
        members = sorted(orbit & input_keys)
        assert members
        remaining -= set(members)
        squares = {int(input_map[m]["self_intersection"]) for m in members}
        assert len(squares) == 1
        square = next(iter(squares))
        a_distribution = collections.Counter()
        source_distribution = collections.Counter()
        basis_shas = []
        for member in members:
            row = input_map[member]
            source_distribution[
                (int(row["source_cell_index"]), row["source_cell_id"])
            ] += 1
        for image in sorted(orbit):
            basis = recover(image)
            x = Matrix(basis)
            assert int((H * G * x)[0]) == 8
            assert int((x.T * G * x)[0]) == square
            assert all(0 <= v <= 4 for v in image[:92])
            assert all(0 <= v <= 2 for v in image[92:])
            assert sum(image[92:]) == 10
            assert sum(image[:92]) + 5 * sum(image[92:]) == 152
            assert basis not in known
            a_distribution[sum(image[:46])] += 1
            basis_shas.append(csha(list(basis)))
        assert len(members) == a_distribution[30]
        orbit_rows.append(
            {
                "self_intersection": square,
                "input_a30_survivor_count": len(members),
                "full_aut_orbit_size": len(orbit),
                "stabilizer_order": EXPECTED_GROUP_ORDER // len(orbit),
                "a_distribution": {
                    str(k): v for k, v in sorted(a_distribution.items())
                },
                "input_source_cell_distribution": {
                    f"{idx}:{cid}": count
                    for (idx, cid), count in sorted(source_distribution.items())
                },
                "representative_intersection_sha256": csha(list(min(orbit))),
                "recovered_basis_set_sha256": csha(sorted(basis_shas)),
                "all_orbit_members_integral_picard_classes": True,
                "all_orbit_members_new_against_known_140": True,
            }
        )

    orbit_rows.sort(
        key=lambda r: (
            r["self_intersection"],
            r["full_aut_orbit_size"],
            r["representative_intersection_sha256"],
        )
    )
    assert sum(r["input_a30_survivor_count"] for r in orbit_rows) == len(survivors)

    report = {
        "schema": OUT_SCHEMA,
        "source_parent_sha": parent["canonical_sha256_without_this_field"],
        "source_lock": {
            "git_blob_sha1": EXPECTED_BLOB,
            "aut_generator_count": 9,
            "independently_recomputed_aut_order": len(group),
            "orbit_partition_in_140_intersection_representation": True,
        },
        "partition": {
            "input_a30_survivor_count": len(survivors),
            "full_aut_orbit_count": len(orbit_rows),
            "full_aut_orbit_sizes": [
                r["full_aut_orbit_size"] for r in orbit_rows
            ],
            "full_aut_orbit_union_size": sum(
                r["full_aut_orbit_size"] for r in orbit_rows
            ),
            "orbits_pairwise_disjoint": True,
            "every_a30_orbit_member_present_in_parent": True,
            "orbits": orbit_rows,
        },
        "scope": "E10_A30_FULL_PARENT_NUMERICAL_AUT_ORBIT_PARTITION_ONLY",
        "effectivity_classification_complete": False,
        "actual_curve_existence_claim": False,
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
    report["canonical_sha256_without_this_field"] = csha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "input_survivors": len(survivors),
                "orbit_count": len(orbit_rows),
                "orbit_sizes": report["partition"]["full_aut_orbit_sizes"],
                "square_orbit_distribution": dict(
                    collections.Counter(r["self_intersection"] for r in orbit_rows)
                ),
                "sha": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
