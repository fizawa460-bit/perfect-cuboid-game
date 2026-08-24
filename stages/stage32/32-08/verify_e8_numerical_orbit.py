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
MATERIALIZED_SCHEMA = "STAGE32_D8_MATERIALIZED_SIGNATURE_CELL_QTAIL_PILOT_V1"
OUTPUT_SCHEMA = "STAGE32_D8_E8_NEW_NUMERICAL_AUT_ORBIT_VERIFICATION_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
EXPECTED_ORBIT_SIZE = 6
EXPECTED_STABILIZER_ORDER = 256
EXPECTED_WITNESS_BASIS_SHA = "8798773deb003c06dc91ef14cd3a952c90d4ba23dcd4ee1cbd66810fbb9942e0"
SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_SELECTED_DET = 274877906944


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify_core(core: dict[str, Any]) -> None:
    assert core["schema"] == CORE_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert core["rank"] == 64 and core["known_class_count"] == 140
    assert core["h2"] == 16
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed


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
        for i in range(140):
            assert h_known[0, p[i]] == h_known[0, i], (gi, i)
        for i in range(140):
            for j in range(140):
                assert known_pairing[p[i], p[j]] == known_pairing[i, j], (gi, i, j)
    return close_group(generators)


def recover_basis(core: dict[str, Any], intersections: tuple[int, ...]) -> tuple[int, ...]:
    selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
    assert abs(int(selected.det())) == EXPECTED_SELECTED_DET
    target = Matrix([intersections[i] for i in SELECTED_ROWS])
    basis = selected.inv() * target
    assert all(v.q == 1 for v in basis)
    out = tuple(int(v) for v in basis)
    I = Matrix(core["raw_cross_pairings_with_basis"])
    assert tuple(int(v) for v in I * Matrix(out)) == intersections
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--action", type=pathlib.Path, required=True)
    ap.add_argument("--materialized", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    action = json.loads(args.action.read_text())
    materialized = json.loads(args.materialized.read_text())
    verify_core(core)
    group = verify_action(core, action)

    assert materialized["schema"] == MATERIALIZED_SCHEMA
    assert materialized["parameters"]["degree"] == 8
    assert materialized["parameters"]["genus"] == 0
    assert materialized["parameters"]["exceptional_mass"] == 8
    assert materialized["parameters"]["curve_group_mass"] == 36
    assert materialized["parameters"]["cell_id"] == "0451bcae6084559bbb842530"
    assert materialized["solver_result"] == "SAT_WITNESS"
    assert materialized["complete_for_existence"] is True
    witness = materialized["witness"]
    basis = tuple(int(v) for v in witness["basis_coordinates"])
    assert len(basis) == 64
    assert canonical_sha256(list(basis)) == EXPECTED_WITNESS_BASIS_SHA

    G = Matrix(core["basis_gram"])
    I = Matrix(core["raw_cross_pairings_with_basis"])
    H = Matrix([core["hyperplane"]])
    K = [tuple(int(v) for v in row) for row in core["known_classes"]]
    x = Matrix(basis)
    intersections = tuple(int(v) for v in I * x)
    degree = int((H * G * x)[0])
    square = int((x.T * G * x)[0])
    assert degree == 8
    assert square == 0
    assert all(0 <= v <= 4 for v in intersections[:92])
    assert all(0 <= v <= 2 for v in intersections[92:])
    assert sum(intersections[92:]) == 8
    assert sum(intersections[:46]) == 36
    assert basis not in set(K)

    orbit_by_intersections: dict[tuple[int, ...], tuple[int, ...]] = {}
    for p in group:
        inv = invert_perm(p)
        image_intersections = tuple(intersections[inv[j]] for j in range(140))
        image_basis = recover_basis(core, image_intersections)
        orbit_by_intersections[image_intersections] = image_basis
    assert len(orbit_by_intersections) == EXPECTED_ORBIT_SIZE
    assert EXPECTED_GROUP_ORDER // len(orbit_by_intersections) == EXPECTED_STABILIZER_ORDER

    known_set = set(K)
    rows = []
    a_distribution: collections.Counter[int] = collections.Counter()
    for image_intersections, image_basis in sorted(orbit_by_intersections.items()):
        xi = Matrix(image_basis)
        image_degree = int((H * G * xi)[0])
        image_square = int((xi.T * G * xi)[0])
        e_mass = sum(image_intersections[92:])
        a_mass = sum(image_intersections[:46])
        normal_mass = sum(image_intersections[:92])
        assert image_degree == 8
        assert image_square == 0
        assert e_mass == 8
        assert normal_mass + 5 * e_mass == 19 * 8
        assert all(0 <= v <= 4 for v in image_intersections[:92])
        assert all(0 <= v <= 2 for v in image_intersections[92:])
        assert image_basis not in known_set
        a_distribution[a_mass] += 1
        rows.append({
            "basis_coordinates_sha256": canonical_sha256(list(image_basis)),
            "intersection_vector_sha256": canonical_sha256(list(image_intersections)),
            "degree": image_degree,
            "self_intersection": image_square,
            "exceptional_mass": e_mass,
            "curve_group_mass_a": a_mass,
            "normal_mass": normal_mass,
            "known_140_match": False,
        })
    assert dict(sorted(a_distribution.items())) == {32: 1, 36: 5}

    report = {
        "schema": OUTPUT_SCHEMA,
        "source_materialized": {
            "workflow_run": 32678030657,
            "cell_id": materialized["parameters"]["cell_id"],
            "witness_basis_sha256": EXPECTED_WITNESS_BASIS_SHA,
        },
        "source_lock": {
            "git_blob_sha1": EXPECTED_BLOB,
            "aut_generator_count": 9,
            "independently_recomputed_aut_order": len(group),
        },
        "witness_verification": {
            "degree": degree,
            "self_intersection": square,
            "exceptional_mass": 8,
            "curve_group_mass_a": 36,
            "normal_intersection_histogram": dict(sorted(collections.Counter(intersections[:92]).items())),
            "exceptional_intersection_histogram": dict(sorted(collections.Counter(intersections[92:]).items())),
            "all_140_cap_bounds_verified": True,
            "known_140_exact_match": False,
        },
        "full_aut_orbit": {
            "orbit_size": len(rows),
            "stabilizer_order": EXPECTED_GROUP_ORDER // len(rows),
            "a_distribution": {str(k): v for k, v in sorted(a_distribution.items())},
            "all_orbit_members_integral_picard_classes": True,
            "all_orbit_members_new_against_known_140": True,
            "members": rows,
        },
        "scope": "NUMERICAL_PICARD_CANDIDATE_ORBIT_ONLY",
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
    report["canonical_sha256_without_this_field"] = canonical_sha256(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "degree": degree,
        "self_intersection": square,
        "orbit_size": len(rows),
        "stabilizer_order": EXPECTED_GROUP_ORDER // len(rows),
        "a_distribution": dict(sorted(a_distribution.items())),
        "known_match": False,
        "canonical_sha256": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
