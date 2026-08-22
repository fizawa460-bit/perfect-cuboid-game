#!/usr/bin/env python3
"""Build the exact Stage30 Task-A finite action certificates.

This construction script uses only integer and modular arithmetic.  It does not
import an abstract S4 model and grants no equivariant-adapter or descent credit.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

ARR_LABELS = ("A1", "A2", "A3", "B3", "B2", "B1", "C")
ARR_OMEGA4 = ("A1", "A2", "A3", "C")
ARR_OMEGA3 = ("B1", "B2", "B3")
LINES = {
    "A1": (1, 0, 0),
    "A2": (0, 1, 0),
    "A3": (0, 0, 1),
    "B3": (1, 1, 0),
    "B2": (1, 0, 1),
    "B1": (0, 1, 1),
    "C": (1, 1, 1),
}
S_ARR_MATRIX = ((0, 1, 0), (1, 0, 0), (0, 0, 1))
T_ARR_MATRIX = ((0, 0, 1), (-1, 0, 1), (0, -1, 1))


def mat_vec3(m, v):
    return tuple(sum(Fraction(m[i][j]) * v[j] for j in range(3)) for i in range(3))


def proportional(v, w):
    scale = None
    for x, y in zip(v, w):
        if y == 0:
            if x != 0:
                return False
            continue
        q = Fraction(x, y)
        if scale is None:
            scale = q
        elif scale != q:
            return False
    return scale not in (None, 0)


def matrix_line_permutation(matrix):
    out = {}
    for label in ARR_LABELS:
        image = mat_vec3(matrix, LINES[label])
        matches = [target for target in ARR_LABELS if proportional(image, LINES[target])]
        assert len(matches) == 1
        out[label] = matches[0]
    return out


def perm_tuple(mapping):
    return tuple(ARR_LABELS.index(mapping[x]) for x in ARR_LABELS)


def compose_perm(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse_perm(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def generated_permutations(generators):
    identity = tuple(range(len(ARR_LABELS)))
    seen = {identity}
    frontier = [identity]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = compose_perm(g, x)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return sorted(seen)


def perm_order(p):
    x = tuple(range(len(p)))
    for n in range(1, 100):
        x = compose_perm(p, x)
        if x == tuple(range(len(p))):
            return n
    raise AssertionError("permutation order overflow")


def det2(m, modulus):
    return (m[0] * m[3] - m[1] * m[2]) % modulus


def mat_mul2(a, b, modulus):
    return (
        (a[0] * b[0] + a[1] * b[2]) % modulus,
        (a[0] * b[1] + a[1] * b[3]) % modulus,
        (a[2] * b[0] + a[3] * b[2]) % modulus,
        (a[2] * b[1] + a[3] * b[3]) % modulus,
    )


def mat_inv2(a, modulus):
    det = det2(a, modulus)
    inv_det = next(x for x in range(modulus) if det * x % modulus == 1)
    return (
        a[3] * inv_det % modulus,
        -a[1] * inv_det % modulus,
        -a[2] * inv_det % modulus,
        a[0] * inv_det % modulus,
    )


def projective4(a):
    a = tuple(x % 4 for x in a)
    neg = tuple((-x) % 4 for x in a)
    return min(a, neg)


SL4 = sorted(
    m for m in product(range(4), repeat=4) if det2(m, 4) == 1
)
G_MOD = sorted({projective4(m) for m in SL4})
G_INDEX = {g: i for i, g in enumerate(G_MOD)}


def mod_mul(a, b):
    return projective4(mat_mul2(a, b, 4))


def mod_inv(a):
    return projective4(mat_inv2(a, 4))


MOD_ID = projective4((1, 0, 0, 1))
S_MOD = projective4((0, -1, 1, 0))
T_MOD = projective4((1, 1, 0, 1))


def generated_mod(generators):
    seen = {MOD_ID}
    frontier = [MOD_ID]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = mod_mul(g, x)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return seen


def mod_order(g):
    x = MOD_ID
    for n in range(1, 100):
        x = mod_mul(g, x)
        if x == MOD_ID:
            return n
    raise AssertionError("modular element order overflow")


def reduction2(g):
    return tuple(x % 2 for x in g)


def is_subgroup(subset):
    h = set(subset)
    if MOD_ID not in h:
        return False
    return all(mod_inv(x) in h for x in h) and all(mod_mul(x, y) in h for x in h for y in h)


def conjugate(g, x):
    return mod_mul(mod_mul(g, x), mod_inv(g))


def permutation_action(elements, action):
    index = {x: i for i, x in enumerate(elements)}
    return tuple(index[action(x)] for x in elements)


def orbit_stabilizer(group, points, action):
    rows = []
    for point in points:
        orbit = sorted({action(g, point) for g in group})
        stabilizer = sorted(g for g in group if action(g, point) == point)
        rows.append((point, orbit, stabilizer))
    return rows


def matrix_json(m):
    return [[m[0], m[1]], [m[2], m[3]]]


def main():
    s_map = matrix_line_permutation(S_ARR_MATRIX)
    t_map = matrix_line_permutation(T_ARR_MATRIX)
    s_arr = perm_tuple(s_map)
    t_arr = perm_tuple(t_map)
    arr_group = generated_permutations((s_arr, t_arr))
    assert len(arr_group) == 24

    arr_ids = {g: f"a{i:02d}" for i, g in enumerate(arr_group)}
    arr_elements = []
    for g in arr_group:
        mapping = {ARR_LABELS[i]: ARR_LABELS[g[i]] for i in range(7)}
        arr_elements.append({
            "id": arr_ids[g],
            "images": mapping,
            "order": perm_order(g),
            "q_liftable": mapping["C"] == "C" and set(mapping[x] for x in ARR_OMEGA4[:3]) == set(ARR_OMEGA4[:3]),
        })
    q_liftable = [row["id"] for row in arr_elements if row["q_liftable"]]
    assert len(q_liftable) == 6

    assert len(SL4) == 48 and len(G_MOD) == 24
    assert generated_mod((S_MOD, T_MOD)) == set(G_MOD)
    mod_ids = {g: f"g{i:02d}" for i, g in enumerate(G_MOD)}
    red_group = sorted({reduction2(g) for g in G_MOD})
    assert len(red_group) == 6
    v_mod = sorted(g for g in G_MOD if reduction2(g) == (1, 0, 0, 1))
    assert len(v_mod) == 4
    omega3 = sorted(g for g in v_mod if g != MOD_ID)
    assert len(omega3) == 3
    omega3_ids = {g: f"v{i}" for i, g in enumerate(omega3)}

    complements = []
    for combo in combinations(G_MOD, 6):
        h = frozenset(combo)
        if not is_subgroup(h):
            continue
        if set(h) & set(v_mod) != {MOD_ID}:
            continue
        if {mod_mul(x, v) for x in h for v in v_mod} != set(G_MOD):
            continue
        complements.append(h)
    complements.sort(key=lambda h: tuple(sorted(mod_ids[x] for x in h)))
    assert len(complements) == 4
    complement_ids = {h: f"h{i}" for i, h in enumerate(complements)}

    def conj_subgroup(g, h):
        return frozenset(conjugate(g, x) for x in h)

    arrangement = {
        "labels": list(ARR_LABELS),
        "omega4": list(ARR_OMEGA4),
        "omega3": list(ARR_OMEGA3),
        "generator_dual_matrices": {
            "s_arr": [list(row) for row in S_ARR_MATRIX],
            "t_arr": [list(row) for row in T_ARR_MATRIX],
        },
        "generators": {
            "s_arr": {x: s_map[x] for x in ARR_LABELS},
            "t_arr": {x: t_map[x] for x in ARR_LABELS},
        },
        "restricted_generator_actions": {
            "omega4": {
                "s_arr": {x: s_map[x] for x in ARR_OMEGA4},
                "t_arr": {x: t_map[x] for x in ARR_OMEGA4},
            },
            "omega3": {
                "s_arr": {x: s_map[x] for x in ARR_OMEGA3},
                "t_arr": {x: t_map[x] for x in ARR_OMEGA3},
            },
        },
        "relations": {
            "order_s_arr": perm_order(s_arr),
            "order_t_arr": perm_order(t_arr),
            "order_s_arr_times_t_arr": perm_order(compose_perm(s_arr, t_arr)),
        },
        "group_order": len(arr_group),
        "elements": arr_elements,
        "q_liftable_subgroup": q_liftable,
        "q_liftable_subgroup_order": len(q_liftable),
    }

    modular = {
        "canonicalization": "lexicographically least of M and -M modulo 4, row-major",
        "sl2_z4_order": len(SL4),
        "group_order": len(G_MOD),
        "identity": mod_ids[MOD_ID],
        "generators": {"S_mod": mod_ids[S_MOD], "T_mod": mod_ids[T_MOD]},
        "relations": {
            "order_S_mod": mod_order(S_MOD),
            "order_T_mod": mod_order(T_MOD),
            "order_S_mod_times_T_mod": mod_order(mod_mul(S_MOD, T_MOD)),
        },
        "elements": [
            {
                "id": mod_ids[g],
                "matrix": matrix_json(g),
                "inverse": mod_ids[mod_inv(g)],
                "reduction_mod_2": matrix_json(reduction2(g)),
                "order": mod_order(g),
            }
            for g in G_MOD
        ],
        "generator_multiplication_witnesses": {
            "S_times_T": mod_ids[mod_mul(S_MOD, T_MOD)],
            "T_times_S": mod_ids[mod_mul(T_MOD, S_MOD)],
            "S_inverse": mod_ids[mod_inv(S_MOD)],
            "T_inverse": mod_ids[mod_inv(T_MOD)],
        },
        "reduction_image_order": len(red_group),
        "V_mod": [mod_ids[g] for g in v_mod],
        "V_mod_order": len(v_mod),
        "V_mod_normal": all(conjugate(g, v) in v_mod for g in G_MOD for v in v_mod),
        "V_mod_is_V4": all(mod_order(v) == 2 for v in v_mod if v != MOD_ID),
        "omega3": [
            {"id": omega3_ids[g], "group_element": mod_ids[g], "matrix": matrix_json(g)}
            for g in omega3
        ],
        "omega4": [
            {"id": complement_ids[h], "members": sorted(mod_ids[g] for g in h)}
            for h in complements
        ],
        "generator_actions": {
            "omega3": {
                name: {
                    omega3_ids[x]: omega3_ids[conjugate(g, x)] for x in omega3
                }
                for name, g in (("S_mod", S_MOD), ("T_mod", T_MOD))
            },
            "omega4": {
                name: {
                    complement_ids[h]: complement_ids[conj_subgroup(g, h)] for h in complements
                }
                for name, g in (("S_mod", S_MOD), ("T_mod", T_MOD))
            },
        },
    }

    action_tables = {
        "schema": "STAGE30_TASK_A_ACTION_TABLES_V1",
        "task": "A",
        "scope": "FINITE_GROUP_ACTION_TABLES_ONLY",
        "arrangement": arrangement,
        "modular": modular,
        "marked_labels_carried_only": {
            "D4_mod_4": [[1, 0], [0, 3]],
            "D4_is_G_mod_element": False,
            "K8_order": 8,
            "sigma_action_on_K8": "TRIVIAL_AUDITED_LABEL",
            "marked_arithmetic_defect_class_count": 8,
            "q_descent_credit": False,
        },
        "claims": {
            "actions_identified": False,
            "qi_equivariance": False,
            "q_descent": False,
            "defect_elimination_count": 0,
            "perfect_cuboid_existence": False,
            "perfect_cuboid_nonexistence": False,
        },
    }

    arr_orbits = {}
    for name, points in (("omega4", ARR_OMEGA4), ("omega3", ARR_OMEGA3)):
        rows = orbit_stabilizer(
            arr_group,
            points,
            lambda g, x: ARR_LABELS[g[ARR_LABELS.index(x)]],
        )
        arr_orbits[name] = [
            {
                "point": point,
                "orbit": orbit,
                "stabilizer_order": len(stab),
                "stabilizer_elements": [arr_ids[g] for g in stab],
            }
            for point, orbit, stab in rows
        ]

    mod_orbits = {}
    rows3 = orbit_stabilizer(G_MOD, omega3, conjugate)
    mod_orbits["omega3"] = [
        {
            "point": omega3_ids[p],
            "orbit": [omega3_ids[x] for x in orb],
            "stabilizer_order": len(stab),
            "stabilizer_elements": [mod_ids[g] for g in stab],
        }
        for p, orb, stab in rows3
    ]
    rows4 = orbit_stabilizer(G_MOD, complements, conj_subgroup)
    mod_orbits["omega4"] = [
        {
            "point": complement_ids[p],
            "orbit": [complement_ids[x] for x in orb],
            "stabilizer_order": len(stab),
            "stabilizer_elements": [mod_ids[g] for g in stab],
        }
        for p, orb, stab in rows4
    ]

    orbit_data = {
        "schema": "STAGE30_TASK_A_ORBIT_STABILIZER_V1",
        "arrangement": arr_orbits,
        "modular": mod_orbits,
        "orbit_stabilizer_identity_checked": True,
    }

    (HERE / "action-tables.json").write_text(
        json.dumps(action_tables, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (HERE / "orbit-stabilizer.json").write_text(
        json.dumps(orbit_data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("built action-tables.json and orbit-stabilizer.json")


if __name__ == "__main__":
    main()
