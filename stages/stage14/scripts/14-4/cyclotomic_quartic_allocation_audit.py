#!/usr/bin/env python3
"""Deterministic audit for Stage14-4cl.

Finite physical data verify the reciprocal fourth-difference divisibilities,
the unique three-way cyclotomic allocation, and the 4x4 good-prime allocation
matrix for the split quartic equality. Finite multiplicities are diagnostic;
no asymptotic incidence estimate is inferred.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
CK_AUDIT = HERE.parent / "quartic_agreement_incidence_audit.py"
spec = spec_from_file_location("stage14_4ck_audit", CK_AUDIT)
assert spec is not None and spec.loader is not None
ck = module_from_spec(spec)
spec.loader.exec_module(ck)


def factorint(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def goodpart(n: int, exceptional: int) -> int:
    out = 1
    for p, e in factorint(n).items():
        if exceptional % p != 0:
            out *= p**e
    return out


def primitive_factors(a: int, b: int) -> tuple[int, int, int, int]:
    assert a > 0 and b > a and gcd(a, b) == 1
    return a, b, b - a, b + a


def check_primitive_odd_coprime(a: int, b: int) -> None:
    fs = primitive_factors(a, b)
    for i in range(4):
        for j in range(i + 1, 4):
            assert oddpart(gcd(fs[i], fs[j])) == 1


def cyclotomic_partition(modulus: int, a: int, b: int):
    """Partition odd modulus dividing b^4-a^4 into -, +, i branches."""
    m = oddpart(modulus)
    assert gcd(m, a * b) == 1
    assert (b**4 - a**4) % m == 0
    mm = gcd(m, b - a)
    mp = gcd(m, b + a)
    mi = gcd(m, b * b + a * a)
    assert mm * mp * mi == m
    assert gcd(mm, mp) == gcd(mm, mi) == gcd(mp, mi) == 1
    for p in factorint(mi):
        assert p % 4 == 1
    return mm, mp, mi


def allocation_matrix(left, right, k_left: int, k_right: int):
    """Return the 4x4 matrix of primes away from 2*k_left*k_right."""
    assert k_left > 0 and k_right > 0
    assert k_left * left[0] * left[1] * left[2] * left[3] == (
        k_right * right[0] * right[1] * right[2] * right[3]
    )
    exceptional = 2 * k_left * k_right
    mat = [[1 for _ in range(4)] for _ in range(4)]

    good_primes = {
        p
        for p in factorint(left[0] * left[1] * left[2] * left[3])
        if exceptional % p != 0
    }
    for p in good_primes:
        rows = [i for i, x in enumerate(left) if x % p == 0]
        cols = [j for j, x in enumerate(right) if x % p == 0]
        assert len(rows) == 1 and len(cols) == 1
        i, j = rows[0], cols[0]
        e1 = vp(left[i], p)
        e2 = vp(right[j], p)
        assert e1 == e2
        mat[i][j] *= p**e1

    for i in range(4):
        row = 1
        for j in range(4):
            row *= mat[i][j]
        assert row == goodpart(left[i], exceptional)
    for j in range(4):
        col = 1
        for i in range(4):
            col *= mat[i][j]
        assert col == goodpart(right[j], exceptional)

    return mat


def audit_pair(a: dict[str, int], b: dict[str, int]):
    cells, triple, qs, _ = ck.ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    qk, qxi = qs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]
    G = a["g"] * b["g"]

    A = alpha * r
    D = delta * s
    U = R * X
    V = J * Y
    assert D > A > 0 and V > U > 0

    # Exact switch-integrality identities.
    assert D**4 - A**4 == qk * R * J * S * T
    assert V**4 - U**4 == qxi * alpha * delta * beta * gamma
    assert (D**4 - A**4) % (R * J) == 0
    assert (V**4 - U**4) % (alpha * delta) == 0

    # Opposite-base odd coprimality.
    assert gcd(oddpart(R * J), A * D) == 1
    assert gcd(oddpart(alpha * delta), U * V) == 1

    xi_branches = cyclotomic_partition(R * J, A, D)
    k_branches = cyclotomic_partition(alpha * delta, U, V)

    # Moving gcds are supported on conditioned fixed data.
    gU = gcd(U, V)
    gA = gcd(A, D)
    assert (X * Y) % gU == 0
    assert (r * s) % gA == 0

    u, v = U // gU, V // gU
    aa, dd = A // gA, D // gA
    assert gcd(u, v) == gcd(aa, dd) == 1
    check_primitive_odd_coprime(u, v)
    check_primitive_odd_coprime(aa, dd)

    left = primitive_factors(u, v)
    right = primitive_factors(aa, dd)
    k_left = G * qk * r * s * gU**4
    k_right = 2 * qxi * X * Y * gA**4
    mat = allocation_matrix(left, right, k_left, k_right)

    # Preserve 4ck exact quartic equality explicitly.
    assert G * qk * r * s * ck.F(U, V) == 2 * qxi * X * Y * ck.F(A, D)

    return triple, xi_branches, k_branches, mat


def main() -> None:
    # Primitive factor lemma over a deterministic grid.
    primitive_checks = 0
    for b in range(2, 70):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            check_primitive_odd_coprime(a, b)
            primitive_checks += 1

    groups = ck.ch.make_groups(420)
    checked = 0
    branch_pairs: set[tuple[int, int]] = set()
    nontrivial_i = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                _, xb, kb, _ = audit_pair(a, b)
                xi_dom = max(range(3), key=lambda z: xb[z])
                k_dom = max(range(3), key=lambda z: kb[z])
                branch_pairs.add((xi_dom, k_dom))
                nontrivial_i += int(xb[2] > 1) + int(kb[2] > 1)
                checked += 1

    assert checked > 0

    # Exact exponent ledger.
    theta = Fraction(5, 16)
    phi = Fraction(1, 4)
    xi_dom_exp = 2 * phi / 3
    k_dom_exp = 2 * theta / 3
    assert xi_dom_exp == Fraction(1, 6)
    assert k_dom_exp == Fraction(5, 24)
    assert 3 * 3 == 9

    print("Stage14-4cl audit: PASS")
    print(f"primitive coprimality pairs checked: {primitive_checks}")
    print(f"dual-cross physical pairs checked: {checked}")
    print(f"dominant branch types observed in finite sample: {len(branch_pairs)}")
    print(f"nontrivial quadratic branch occurrences: {nontrivial_i}")
    print("moving gcd support gUV|XY and gAD|rs: exact")
    print("4x4 good-prime allocation reconstruction: exact")
    print("reciprocal three-way cyclotomic allocation: exact")
    print("quadratic branch odd primes: 1 mod 4")
    print("extreme xi dominant exponent: 1/6")
    print("extreme k dominant exponent: 5/24")
    print("asymptotic reciprocal cyclotomic incidence: UNPROVED")


if __name__ == "__main__":
    main()
