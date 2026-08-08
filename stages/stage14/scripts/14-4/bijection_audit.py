#!/usr/bin/env python3
"""Stage14-4ab independent audit of the exact two-face bijection.

This script enumerates pairs of oriented primitive Pythagorean face data,
performs the minimal shared-edge gluing, imposes the exact space-diagonal
square condition, and classifies the shared-edge chamber.  It does not use
the Stage14-2 cuboid-edge-first enumerator.
"""

from math import gcd, isqrt

CUTOFFS = [1_000, 2_000, 5_000, 10_000]
EXPECTED = {
    1_000: (2, 0, 0, 0),
    2_000: (2, 2, 1, 0),
    5_000: (6, 6, 3, 0),
    10_000: (9, 11, 5, 0),
}


def primitive_oriented_faces(B):
    """Return (S,X,H,m,n,role) with H<=B and S the distinguished shared leg."""
    out = []
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            H = m * m + n * n
            if H > B:
                continue
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            D = m * m - n * n
            P = 2 * m * n
            out.append((D, P, H, m, n, "D"))
            out.append((P, D, H, m, n, "P"))
        m += 1
    return out


def is_square(n):
    r = isqrt(n)
    return r * r == n


def census(B):
    faces = primitive_oriented_faces(B)
    exact = {"a": 0, "b": 0, "c": 0}
    triple_incidences = {"a": 0, "b": 0, "c": 0}

    for S1, X1, H1, *_ in faces:
        for S2, X2, H2, *_ in faces:
            g = gcd(S1, S2)
            alpha = S1 // g
            beta = S2 // g

            # Minimal primitive gluing; the common scale t is forced to 1.
            e = g * alpha * beta
            x = beta * X1
            y = alpha * X2
            if not x < y:
                continue

            u = beta * H1
            d2 = u * u + y * y
            d = isqrt(d2)
            if d * d != d2 or d > B:
                continue

            # Sanity identities from the second face and automatic fourth triangle.
            v = alpha * H2
            assert e * e + x * x == u * u
            assert e * e + y * y == v * v
            assert v * v + x * x == d * d
            assert gcd(e, x, y) == 1

            if e < x:
                direction = "a"
            elif e < y:
                direction = "b"
            else:
                direction = "c"

            if is_square(x * x + y * y):
                triple_incidences[direction] += 1
            else:
                exact[direction] += 1

    return {
        "B": B,
        "N_a2": exact["a"],
        "N_b2": exact["b"],
        "N_c2": exact["c"],
        "T_a_incidence": triple_incidences["a"],
        "T_b_incidence": triple_incidences["b"],
        "T_c_incidence": triple_incidences["c"],
        "oriented_primitive_face_data": len(faces),
    }


def main():
    all_pass = True
    for B in CUTOFFS:
        row = census(B)
        got = (
            row["N_a2"], row["N_b2"], row["N_c2"],
            row["T_a_incidence"] + row["T_b_incidence"] + row["T_c_incidence"],
        )
        ok = got == EXPECTED[B]
        all_pass &= ok
        print(B, got, "PASS" if ok else "FAIL")
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
