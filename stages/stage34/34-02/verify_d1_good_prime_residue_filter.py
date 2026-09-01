#!/usr/bin/env python3
"""Exact necessary-residue replay for Stage34-02 D1 squareclass covers.

For q=a/b, x=X/Z with gcd(X,Z)=1, a rational receiver point on squareclass d
forces all three integer forms below to be squares modulo every good prime p
not dividing 2ab(a^2-b^2)(a^2+b^2)d:

  E_h = X Z (X+Z) (b^2 X + a^2 Z),
  A_h/d,
  B_h/d.

We exhaust P^1(F_p). No residue class => no rational point in that d-cover.
"""

CASES = [
    (20, 21, 5, 23),
    (20, 21, 10, 23),
    (84, 13, 13, 31),
    (84, 13, 26, 31),
    (48, 55, 5, 23),
    (48, 55, 10, 23),
    (20, 99, 5, 23),
    (20, 99, 10, 23),
]


def is_square(v, p):
    v %= p
    return v == 0 or pow(v, (p - 1) // 2, p) == 1


def residues(a, b, d, p):
    bad = 2 * a * b * (a * a - b * b) * (a * a + b * b) * d
    assert bad % p != 0
    invd = pow(d, -1, p)
    out = []
    for X, Z in [(x, 1) for x in range(p)] + [(1, 0)]:
        E = X * Z * (X + Z) * (b * b * X + a * a * Z)
        A = b * b * X * X + a * a * Z * Z
        B = (
            b * b * (a * a + b * b) * X * X
            + 4 * a * a * b * b * X * Z
            + a * a * (a * a + b * b) * Z * Z
        )
        if is_square(E, p) and is_square(A * invd, p) and is_square(B * invd, p):
            out.append([X % p, Z % p])
    return out


for a, b, d, p in CASES:
    r = residues(a, b, d, p)
    if r:
        raise SystemExit(f"unexpected residue q={a}/{b} d={d} p={p}: {r}")
    print(f"PASS q={a}/{b} d={d} obstructed_mod_p={p}")

print("PASS exact D1 good-prime residue obstruction: 8 squareclasses eliminated")
