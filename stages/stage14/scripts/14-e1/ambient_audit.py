#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path("stages/stage14/data/14-e1/ambient_audit.json")
CUTOFFS = [50, 100, 200, 500, 1000, 2000]


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def primitive_oriented_faces(B: int):
    faces = []
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a = m * m - n * n
            b = 2 * m * n
            h = m * m + n * n
            if h > B:
                continue
            faces.append((a, b, h))
            faces.append((b, a, h))
        m += 1
    return faces


def pythagorean_neighbors(B: int):
    nbr = defaultdict(set)
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a = m * m - n * n
            b = 2 * m * n
            h = m * m + n * n
            if h > B:
                continue
            k = 1
            while k * h <= B:
                A = k * a
                C = k * b
                nbr[A].add(C)
                nbr[C].add(A)
                k += 1
        m += 1
    return nbr


def direction(e: int, x: int, y: int) -> str:
    assert x < y
    if e < x:
        return "a"
    if e < y:
        return "b"
    return "c"


def edge_first(B: int):
    """Enumerate from physical Pythagorean adjacencies around the shared edge."""
    nbr = pythagorean_neighbors(B)
    objects = set()
    for e, others in nbr.items():
        vals = sorted(v for v in others if v <= B)
        for i, x in enumerate(vals):
            for y in vals[i + 1 :]:
                if e * e + x * x + y * y > B * B:
                    continue
                if math.gcd(math.gcd(e, x), y) != 1:
                    continue
                objects.add((e, x, y))
    return objects


def face_pair_first(B: int):
    """Enumerate from two oriented primitive face data and minimal gluing."""
    faces = primitive_oriented_faces(B)
    fibers = Counter()

    for S1, X1, H1 in faces:
        for S2, X2, H2 in faces:
            g = math.gcd(S1, S2)
            alpha = S1 // g
            beta = S2 // g

            e = g * alpha * beta
            x = beta * X1
            y = alpha * X2

            if not x < y:
                continue
            if e * e + x * x + y * y > B * B:
                continue

            # Minimal gluing is globally primitive; this is also rechecked here.
            assert math.gcd(math.gcd(e, x), y) == 1
            fibers[(e, x, y)] += 1

    assert all(v == 1 for v in fibers.values())
    return set(fibers), fibers


def summarize(objects):
    raw = Counter()
    exact = Counter()
    euler_bricks = set()

    for e, x, y in objects:
        assert x < y
        assert math.gcd(math.gcd(e, x), y) == 1
        assert is_square(e * e + x * x)
        assert is_square(e * e + y * y)

        q = direction(e, x, y)
        raw[q] += 1

        third_square = is_square(x * x + y * y)
        if third_square:
            euler_bricks.add(tuple(sorted((e, x, y))))
        else:
            exact[q] += 1

    third_inc = sum(raw.values()) - sum(exact.values())
    # Every all-three-face Euler brick has three intended raw pair incidences.
    assert third_inc == 3 * len(euler_bricks)

    return {
        "raw_directional": {q: raw[q] for q in ("a", "b", "c")},
        "raw_total": sum(raw.values()),
        "exactly_two_directional": {q: exact[q] for q in ("a", "b", "c")},
        "exactly_two_total": sum(exact.values()),
        "third_face_square_incidence_count": third_inc,
        "ambient_euler_brick_object_count": len(euler_bricks),
    }


def row(B: int):
    edge = edge_first(B)
    face, fibers = face_pair_first(B)

    assert edge == face
    summary = summarize(edge)

    return {
        "B": B,
        "edge_first_object_count": len(edge),
        "face_pair_object_count": len(face),
        "set_equality": True,
        "face_pair_max_fiber_multiplicity": max(fibers.values(), default=0),
        **summary,
    }


def main():
    rows = [row(B) for B in CUTOFFS]

    report = {
        "metadata": {
            "stage": "14-e1",
            "track": "front-side two-face ambient control population",
            "integer_space_diagonal_required": False,
            "height": "D_R=sqrt(e^2+x^2+y^2)<=B",
            "primitive": "gcd(e,x,y)=1",
            "ordering": "x<y; direction determined by the position of e",
            "raw_faces": "e^2+x^2 and e^2+y^2 are squares",
            "exactly_two_filter": "x^2+y^2 is not a square",
        },
        "bijection": {
            "face_data": "F_i=(S_i,X_i,H_i) oriented primitive Pythagorean face data",
            "g": "gcd(S1,S2)",
            "alpha": "S1/g",
            "beta": "S2/g",
            "e": "g*alpha*beta=lcm(S1,S2)",
            "x": "beta*X1",
            "y": "alpha*X2",
            "fiber_multiplicity": 1,
            "uses_space_diagonal_square_condition": False,
        },
        "height_identity": {
            "t1": "X1/S1",
            "t2": "X2/S2",
            "L": "lcm(S1,S2)",
            "edge_vector": "(e,x,y)=L(1,t1,t2)",
            "D_R": "L*sqrt(1+t1^2+t2^2)",
            "integer_or_rational_D_R_required": False,
        },
        "cutoffs": rows,
        "status": {
            "STAGE14_E1": "COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT",
            "ROADMAP_CREATED_BEFORE_E1_IMPLEMENTATION": True,
            "INTEGER_SPACE_DIAGONAL_CONDITION_REMOVED": True,
            "REAL_SPACE_DIAGONAL_HEIGHT_ONLY": True,
            "EDGE_FIRST_FACE_PAIR_FIRST_SET_EQUALITY": True,
            "FACE_PAIR_FIBER_MULTIPLICITY_ONE": True,
            "ASYMPTOTIC_CLAIM_MADE": False,
            "NEXT_E_TASK": "Stage14-e2 finite ambient reconnaissance",
        },
        "pass": True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
