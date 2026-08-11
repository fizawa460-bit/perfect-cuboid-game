#!/usr/bin/env python3

import json
import math
from collections import defaultdict


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def representations(n: int):
    out = set()
    lim = math.isqrt(n)
    for x in range(-lim, lim + 1):
        y2 = n - x * x
        if y2 < 0:
            continue
        y = math.isqrt(y2)
        if y * y == y2:
            out.add((x, y))
            out.add((x, -y))
    return sorted(out)


def primitive_representations(n: int):
    return [z for z in representations(n) if math.gcd(abs(z[0]), abs(z[1])) == 1]


def split_supported_odd(n: int) -> bool:
    if n % 2 == 0:
        return False
    x = n
    p = 3
    while p * p <= x:
        if x % p == 0:
            if p % 4 != 1:
                return False
            while x % p == 0:
                x //= p
        p += 2
    return x == 1 or x % 4 == 1


def canonical_pi(ell: int):
    candidates = [(x, y) for x, y in representations(ell) if x > y > 0]
    return candidates[0] if candidates else None


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def divisors(n: int):
    out = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    p = 2
    count = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def oddpart(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    while n % 2 == 0:
        n //= 2
    return n


def main():
    # Synthetic fixed-packet charts.  These are theorem-regression data only.
    direction_pairs = [(3, 5), (5, 7), (7, 11)]
    k0_values = [1, 2, 5, 10, 13]
    ell_values = [p for p in range(5, 250) if is_prime(p) and p % 4 == 1]
    delta0_values = [n for n in range(1, 100, 2) if split_supported_odd(n)]
    selector_ds = [1, 3, 5, 7, 15]

    primitive_mobius_checks = 0
    four_cell_checks = 0
    projective_checks = 0
    projective_survivors = 0
    weight = defaultdict(int)

    for A0, B0 in direction_pairs:
        assert math.gcd(A0, B0) == 1
        for k0 in k0_values:
            for a in primitive_representations(k0):
                for delta0 in delta0_values:
                    for gamma in primitive_representations(delta0):
                        for ell in ell_values:
                            pi = canonical_pi(ell)
                            if pi is None or ell <= 2 * k0 * delta0:
                                continue

                            ag = mul(a, gamma)
                            p_coord = ag[0]
                            q_coord = -ag[1]  # sigma=+1 synthetic orientation
                            if p_coord == 0 or q_coord == 0:
                                continue

                            # Exact primitive-cover Mobius expansion.
                            common = math.gcd(abs(p_coord), abs(q_coord))
                            mobius_indicator = sum(mobius(e) for e in divisors(common))
                            assert mobius_indicator == (1 if common == 1 else 0)
                            primitive_mobius_checks += 1
                            if common != 1:
                                continue

                            # A physical primitive cover has coprime odd r/t columns.
                            r = q_coord - p_coord
                            t = q_coord + p_coord
                            R = oddpart(r)
                            T = oddpart(t)
                            assert math.gcd(R, T) == 1

                            # Exact t78 four-cell determinism.
                            d_AR = math.gcd(A0, R)
                            d_AT = math.gcd(A0, T)
                            d_BR = math.gcd(B0, R)
                            d_BT = math.gcd(B0, T)
                            g = math.gcd(A0 * B0, R * T)
                            assert d_AR * d_AT * d_BR * d_BT == g
                            cells = [d_AR, d_AT, d_BR, d_BT]
                            for i in range(4):
                                for j in range(i + 1, 4):
                                    assert math.gcd(cells[i], cells[j]) == 1
                            four_cell_checks += 1

                            # t87 endpoint projective condition in its scalar chart:
                            # z=a*gamma*pi is a rational unit modulo d iff Im(z)=0 mod d.
                            z = mul(ag, pi)
                            Q = ell * delta0
                            for d in selector_ds:
                                if math.gcd(d, ell * k0 * delta0) != 1:
                                    continue
                                direct = z[1] % d == 0
                                if direct:
                                    assert math.gcd(z[0], d) == 1
                                    projective_survivors += 1
                                    weight[(A0, B0, k0, Q, d)] += 1
                                projective_checks += 1

    result = {
        "stage": "14-t90",
        "direction_pairs": len(direction_pairs),
        "k0_values": k0_values,
        "ell_values": len(ell_values),
        "delta0_values": len(delta0_values),
        "primitive_mobius_checks": primitive_mobius_checks,
        "four_cell_determinism_checks": four_cell_checks,
        "projective_selector_checks": projective_checks,
        "projective_selector_survivors": projective_survivors,
        "weighted_q_packets": len(weight),
        "max_weight": max(weight.values()),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
