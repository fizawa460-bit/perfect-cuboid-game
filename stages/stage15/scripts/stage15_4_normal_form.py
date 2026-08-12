#!/usr/bin/env python3
from __future__ import annotations

import math
from fractions import Fraction
from functools import reduce


def is_square(n: int) -> bool:
    if n < 0:
        return False
    q = math.isqrt(n)
    return q * q == n


def squarefree_kernel(n: int) -> int:
    if n <= 0:
        raise ValueError("squarefree_kernel expects n>0")
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def gcd_many(values: tuple[int, ...]) -> int:
    return reduce(math.gcd, (abs(x) for x in values), 0)


def toric_raw(m: int, n: int, r: int, s: int) -> tuple[int, int, int, int, int]:
    if not (m > n > 0 and r > s > 0):
        raise ValueError("positive toric chamber requires m>n>0 and r>s>0")
    if math.gcd(m, n) != 1 or math.gcd(r, s) != 1:
        raise ValueError("toric P1 representatives must be primitive")
    e = 4 * m * n * r * s
    x = 2 * r * s * (m * m - n * n)
    y = 2 * m * n * (r * r - s * s)
    u = 2 * r * s * (m * m + n * n)
    v = 2 * m * n * (r * r + s * s)
    return e, x, y, u, v


def primitive_reduce(raw: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    g = gcd_many(raw)
    if g <= 0:
        raise ValueError("zero raw point")
    return tuple(x // g for x in raw), g


def recover_toric_params(e: int, x: int, y: int, u: int, v: int) -> tuple[int, int, int, int]:
    if not all(z > 0 for z in (e, x, y, u, v)):
        raise ValueError("positive shared-edge incidence required")
    if u * u != e * e + x * x or v * v != e * e + y * y:
        raise ValueError("not a two-face shared-edge incidence")
    t = Fraction(u + x, e)
    w = Fraction(v + y, e)
    m, n = t.numerator, t.denominator
    r, s = w.numerator, w.denominator
    if not (m > n > 0 and r > s > 0):
        raise ArithmeticError("recovered parameters outside positive toric chamber")
    return m, n, r, s


def norm_factors(m: int, n: int, r: int, s: int) -> tuple[int, int]:
    a = m * m * r * r + n * n * s * s
    b = m * m * s * s + n * n * r * r
    return a, b


def normal_form(m: int, n: int, r: int, s: int) -> dict:
    raw = toric_raw(m, n, r, s)
    physical, g = primitive_reduce(raw)
    e, x, y, u, v = raw
    a, b = norm_factors(m, n, r, s)
    raw_r2 = e * e + x * x + y * y
    if raw_r2 != 4 * a * b:
        raise ArithmeticError("Stage15-4 factorization identity failed")
    physical_r2 = sum(z * z for z in physical[:3])
    if raw_r2 != g * g * physical_r2:
        raise ArithmeticError("primitive height scaling failed")

    ka = squarefree_kernel(a)
    kb = squarefree_kernel(b)
    survivor = ka == kb
    out = {
        "params": [m, n, r, s],
        "raw": list(raw),
        "physical": list(physical),
        "G": g,
        "A": a,
        "B": b,
        "sf_A": ka,
        "sf_B": kb,
        "AB_square": is_square(a * b),
        "space_integral": is_square(physical_r2),
        "physical_R2": physical_r2,
    }
    if out["AB_square"] != survivor or out["space_integral"] != survivor:
        raise ArithmeticError("equivalent normal forms disagree")

    if survivor:
        k = ka
        p2, q2 = a // k, b // k
        p, q = math.isqrt(p2), math.isqrt(q2)
        if p * p != p2 or q * q != q2:
            raise ArithmeticError("common squarefree kernel did not leave squares")
        raw_d = 2 * k * p * q
        if raw_d * raw_d != raw_r2 or raw_d % g != 0:
            raise ArithmeticError("raw/physical diagonal reconstruction failed")
        out.update({"k": k, "P": p, "Q": q, "raw_d": raw_d, "physical_d": raw_d // g})
    else:
        out.update({"k": None, "P": None, "Q": None, "raw_d": None, "physical_d": None})
    return out


def prime_factors(n: int) -> list[int]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append(n)
    return out
