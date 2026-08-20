#!/usr/bin/env python3
from fractions import Fraction


def add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
        if out[e] == 0:
            del out[e]
    return out


def scale(a, c):
    return {e: c * v for e, v in a.items() if c * v}


def mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[ea + eb] = out.get(ea + eb, 0) + ca * cb
    return {e: c for e, c in out.items() if c}


def power(a, n):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, a)
    return out


def det(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    n = len(a)
    d = Fraction(1)
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            d = -d
        p = a[j][j]
        d *= p
        for k in range(j, n):
            a[j][k] /= p
        for i in range(j + 1, n):
            q = a[i][j]
            if q:
                for k in range(j, n):
                    a[i][k] -= q * a[j][k]
    return d


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


def main():
    x = {1: 1}
    xinv = {-1: 1}
    z = add(power(x, 2), power(xinv, 2))

    q_of_z = add(
        add(power(z, 4), scale(power(z, 2), -20)),
        add(scale(z, 256), {0: -412}),
    )
    lhs = mul({8: 1}, q_of_z)
    f = {
        16: 1,
        12: -16,
        10: 256,
        8: -446,
        6: 256,
        4: -16,
        0: 1,
    }
    assert lhs == f

    # Coefficient rows after dropping the common factor 2 from each pullback.
    # Columns are omega_0,...,omega_6.
    rows = [
        [0, -1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, -1, 0, 1, 0, 0],
        [-1, 0, 1, 0, -1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 1],
    ]
    assert det(rows) == 8

    # q=7 branch/sign table from the exact Legendre allocation rule.
    # Result is the unique admissible leg M or N.
    table = {}
    for g in (1, 6):
        for eps in (1, -1):
            # q=7 may divide ab or d. Both source locations must give same leg.
            legs = []
            for source in ("ab", "d"):
                if source == "ab":
                    m_ok = legendre(-eps * g, 7) == 1
                    n_ok = legendre(eps * g, 7) == 1
                else:
                    m_ok = legendre(eps * (6 // g), 7) == 1
                    n_ok = legendre(-eps * (6 // g), 7) == 1
                assert m_ok ^ n_ok
                legs.append("M" if m_ok else "N")
            assert legs[0] == legs[1]
            table[(g, eps)] = legs[0]

    assert table == {
        (1, 1): "N",
        (1, -1): "M",
        (6, 1): "M",
        (6, -1): "N",
    }

    print("laurent_identity=PASS")
    print("normalized_differential_matrix_det=8")
    print("q7_branch_sign_table=", table)
    print("A1-8 exact verification: PASS")


if __name__ == "__main__":
    main()
