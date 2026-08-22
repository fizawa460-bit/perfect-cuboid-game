#!/usr/bin/env python3
"""Independent fail-closed verifier for Stage30 Task-A certificates."""

from __future__ import annotations

import json
import hashlib
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
LABELS = ("A1", "A2", "A3", "B3", "B2", "B1", "C")
LINES = {
    "A1": (1, 0, 0), "A2": (0, 1, 0), "A3": (0, 0, 1),
    "B3": (1, 1, 0), "B2": (1, 0, 1), "B1": (0, 1, 1), "C": (1, 1, 1),
}


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def proportional(v, w):
    ratios = {Fraction(x, y) for x, y in zip(v, w) if y}
    return len(ratios) == 1 and all(y or x == 0 for x, y in zip(v, w)) and next(iter(ratios)) != 0


def matrix_action(matrix):
    out = {}
    for label, vector in LINES.items():
        image = tuple(sum(Fraction(matrix[i][j]) * vector[j] for j in range(3)) for i in range(3))
        matches = [target for target, form in LINES.items() if proportional(image, form)]
        assert len(matches) == 1
        out[label] = matches[0]
    return out


def compose_maps(p, q):
    return {x: p[q[x]] for x in LABELS}


def arrangement_closure(generators):
    identity = {x: x for x in LABELS}
    key = lambda p: tuple(p[x] for x in LABELS)
    known = {key(identity): identity}
    frontier = [identity]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = compose_maps(g, x)
            if key(y) not in known:
                known[key(y)] = y
                frontier.append(y)
    return known


def det(m, n):
    return (m[0] * m[3] - m[1] * m[2]) % n


def mul(a, b, n=4):
    raw = (
        (a[0]*b[0] + a[1]*b[2]) % n,
        (a[0]*b[1] + a[1]*b[3]) % n,
        (a[2]*b[0] + a[3]*b[2]) % n,
        (a[2]*b[1] + a[3]*b[3]) % n,
    )
    if n == 4:
        neg = tuple(-x % 4 for x in raw)
        return min(raw, neg)
    return raw


def canon(m):
    m = tuple(m)
    return min(m, tuple(-x % 4 for x in m))


def inv(m):
    return canon((m[3], -m[1] % 4, -m[2] % 4, m[0]))


def subgroup(h, identity):
    return identity in h and all(inv(x) in h for x in h) and all(mul(x, y) in h for x in h for y in h)


def conjugate(g, x):
    return mul(mul(g, x), inv(g))


def verify():
    tables = load("action-tables.json")
    orbits = load("orbit-stabilizer.json")
    repro = load("repro-manifest.json")
    assert tables["schema"] == "STAGE30_TASK_A_ACTION_TABLES_V1"
    assert tables["scope"] == "FINITE_GROUP_ACTION_TABLES_ONLY"

    arr = tables["arrangement"]
    recovered = {
        name: matrix_action(matrix)
        for name, matrix in arr["generator_dual_matrices"].items()
    }
    assert recovered == arr["generators"]
    for action_name, points in (("omega4", ("A1", "A2", "A3", "C")), ("omega3", ("B1", "B2", "B3"))):
        for gen_name in ("s_arr", "t_arr"):
            assert arr["restricted_generator_actions"][action_name][gen_name] == {
                point: recovered[gen_name][point] for point in points
            }
    arr_closure = arrangement_closure([recovered["s_arr"], recovered["t_arr"]])
    assert len(arr_closure) == 24 == arr["group_order"]
    certified_arr = {tuple(row["images"][x] for x in LABELS): row for row in arr["elements"]}
    assert set(certified_arr) == set(arr_closure)
    assert len({row["id"] for row in arr["elements"]}) == 24
    q_rows = [row for row in arr["elements"] if row["q_liftable"]]
    assert len(q_rows) == arr["q_liftable_subgroup_order"] == 6
    assert {row["id"] for row in q_rows} == set(arr["q_liftable_subgroup"])
    assert arr["relations"] == {"order_s_arr": 2, "order_t_arr": 4, "order_s_arr_times_t_arr": 3}

    sl4 = [m for m in product(range(4), repeat=4) if det(m, 4) == 1]
    group = sorted({canon(m) for m in sl4})
    assert len(sl4) == 48 and len(group) == 24
    rows = tables["modular"]["elements"]
    from_json = {
        tuple(x for row in item["matrix"] for x in row): item for item in rows
    }
    assert set(from_json) == set(group)
    assert len({item["id"] for item in rows}) == 24
    by_id = {item["id"]: g for g, item in from_json.items()}
    identity = canon((1, 0, 0, 1))
    modular = tables["modular"]
    assert by_id[modular["identity"]] == identity
    for g, item in from_json.items():
        assert by_id[item["inverse"]] == inv(g)
        assert mul(g, inv(g)) == identity
        assert item["reduction_mod_2"] == [[g[0] % 2, g[1] % 2], [g[2] % 2, g[3] % 2]]

    s = by_id[modular["generators"]["S_mod"]]
    t = by_id[modular["generators"]["T_mod"]]
    generated = {identity}
    frontier = [identity]
    while frontier:
        x = frontier.pop()
        for g in (s, t):
            y = mul(g, x)
            if y not in generated:
                generated.add(y)
                frontier.append(y)
    assert generated == set(group)
    assert modular["relations"] == {"order_S_mod": 2, "order_T_mod": 4, "order_S_mod_times_T_mod": 3}

    v = sorted(g for g in group if tuple(x % 2 for x in g) == (1, 0, 0, 1))
    assert len(v) == modular["V_mod_order"] == 4
    assert {by_id[x] for x in modular["V_mod"]} == set(v)
    assert all(conjugate(g, x) in v for g in group for x in v)
    assert modular["V_mod_normal"] is True
    assert modular["V_mod_is_V4"] is True
    assert all(mul(x, x) == identity for x in v)
    nonidentity_v = set(v) - {identity}
    omega3 = {item["id"]: by_id[item["group_element"]] for item in modular["omega3"]}
    assert set(omega3.values()) == nonidentity_v and len(omega3) == 3

    complements = []
    for combo in combinations(group, 6):
        h = frozenset(combo)
        if subgroup(h, identity) and set(h) & set(v) == {identity}:
            if {mul(x, y) for x in h for y in v} == set(group):
                complements.append(h)
    assert len(complements) == 4
    omega4 = {
        item["id"]: frozenset(by_id[x] for x in item["members"])
        for item in modular["omega4"]
    }
    assert set(omega4.values()) == set(complements) and len(omega4) == 4

    for gen_name, g in (("S_mod", s), ("T_mod", t)):
        for point_id, point in omega3.items():
            target = modular["generator_actions"]["omega3"][gen_name][point_id]
            assert omega3[target] == conjugate(g, point)
        for point_id, h in omega4.items():
            target = modular["generator_actions"]["omega4"][gen_name][point_id]
            assert omega4[target] == frozenset(conjugate(g, x) for x in h)

    arr_ids = {row["id"]: row["images"] for row in arr["elements"]}
    for action_name, expected_size in (("omega3", 3), ("omega4", 4)):
        for row in orbits["arrangement"][action_name]:
            assert len(row["orbit"]) == expected_size
            assert len(row["stabilizer_elements"]) == row["stabilizer_order"] == 24 // expected_size
            assert all(arr_ids[g][row["point"]] == row["point"] for g in row["stabilizer_elements"])
        lookup = omega3 if action_name == "omega3" else omega4
        for row in orbits["modular"][action_name]:
            assert len(row["orbit"]) == expected_size
            assert len(row["stabilizer_elements"]) == row["stabilizer_order"] == 24 // expected_size
            point = lookup[row["point"]]
            for gid in row["stabilizer_elements"]:
                g = by_id[gid]
                image = conjugate(g, point) if action_name == "omega3" else frozenset(conjugate(g, x) for x in point)
                assert image == point

    marked = tables["marked_labels_carried_only"]
    assert marked["D4_is_G_mod_element"] is False
    assert marked["K8_order"] == 8
    assert marked["q_descent_credit"] is False
    assert tables["claims"] == {
        "actions_identified": False,
        "defect_elimination_count": 0,
        "perfect_cuboid_existence": False,
        "perfect_cuboid_nonexistence": False,
        "q_descent": False,
        "qi_equivariance": False,
    }
    for filename in ("build_actions.py", "action-tables.json", "orbit-stabilizer.json"):
        digest = hashlib.sha256((HERE / filename).read_bytes()).hexdigest()
        assert digest == repro["artifact_sha256"][filename]


if __name__ == "__main__":
    verify()
    print("ARRANGEMENT_GENERATORS=PASS")
    print("ARRANGEMENT_GROUP_ORDER=24")
    print("ARRANGEMENT_4_PLUS_3_ACTION=PASS")
    print("MODULAR_PROJECTIVE_GROUP_ORDER=24")
    print("MODULAR_GENERATORS=PASS")
    print("MODULAR_REDUCTION_KERNEL_ORDER=4")
    print("MODULAR_OMEGA3_COUNT=3")
    print("MODULAR_OMEGA4_COUNT=4")
    print("MODULAR_ACTION_TABLES=PASS")
    print("ORBIT_STABILIZER_CERTIFICATE=PASS")
    print("TASK_A_Q_DESCENT_CREDIT=false")
    print("PERFECT_CUBOID_EXISTENCE_CLAIM=false")
    print("PERFECT_CUBOID_NONEXISTENCE_CLAIM=false")
