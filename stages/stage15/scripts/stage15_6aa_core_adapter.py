#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass

from stage15_4_normal_form import normal_form, prime_factors


@dataclass(frozen=True)
class ChannelSplit:
    k: int
    k_odd: int
    k_S: int
    k_O: int
    S_primes: tuple[int, ...]
    O_primes: tuple[int, ...]


def odd_part(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def is_square(n: int) -> bool:
    if n < 0:
        return False
    q = math.isqrt(n)
    return q * q == n


def physical_exact_two(m: int, n: int, r: int, s: int) -> bool:
    nf = normal_form(m, n, r, s)
    e, x, y, _, _ = nf["physical"]
    return not is_square(x * x + y * y)


def classify_core(m: int, n: int, r: int, s: int) -> ChannelSplit:
    nf = normal_form(m, n, r, s)
    if not nf["space_integral"]:
        raise ValueError("Stage15-6aa channel split is defined on survivors")

    k = int(nf["k"])
    k_odd = odd_part(k)
    S: list[int] = []
    O: list[int] = []

    for p in prime_factors(k_odd):
        if p == 2:
            raise AssertionError("odd core unexpectedly contains 2")
        if p % 4 != 1:
            raise AssertionError(f"odd core prime is not 1 mod 4: {p}")

        # Unit lemma: no odd common-core prime divides any toric parameter.
        if any(z % p == 0 for z in (m, n, r, s)):
            raise AssertionError(f"core prime {p} divides toric parameter")

        s_channel = (m * m + n * n) % p == 0 and (r * r - s * s) % p == 0
        o_channel = (m * m - n * n) % p == 0 and (r * r + s * s) % p == 0
        if s_channel == o_channel:
            raise AssertionError(f"prime {p} does not lie in exactly one channel")

        # Root/diagonal line formulation.
        inv_n = pow(n, -1, p)
        inv_s = pow(s, -1, p)
        x = (m * inv_n) % p
        y = (r * inv_s) % p
        if s_channel:
            if (x * x + 1) % p or (y * y - 1) % p:
                raise AssertionError("S-channel ratio check failed")
            S.append(p)
        else:
            if (x * x - 1) % p or (y * y + 1) % p:
                raise AssertionError("O-channel ratio check failed")
            O.append(p)

    k_S = math.prod(S)
    k_O = math.prod(O)
    if k_S * k_O != k_odd or math.gcd(k_S, k_O) != 1:
        raise AssertionError("channel factorization failed")

    if (m * m + n * n) % k_S or (r * r - s * s) % k_S:
        raise AssertionError("S-channel composite divisibility failed")
    if (m * m - n * n) % k_O or (r * r + s * s) % k_O:
        raise AssertionError("O-channel composite divisibility failed")

    host = (m**4 - n**4) * (r**4 - s**4)
    if host % (k_odd * k_odd):
        raise AssertionError("odd-core square-divisor lock failed")

    return ChannelSplit(
        k=k,
        k_odd=k_odd,
        k_S=k_S,
        k_O=k_O,
        S_primes=tuple(S),
        O_primes=tuple(O),
    )


def scan_small_survivors(limit: int = 18) -> dict[str, int]:
    survivors = exact_two = mixed = s_only = o_only = 0
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            for r in range(2, limit + 1):
                for s in range(1, r):
                    if math.gcd(r, s) != 1:
                        continue
                    nf = normal_form(m, n, r, s)
                    if not nf["space_integral"]:
                        continue
                    survivors += 1
                    split = classify_core(m, n, r, s)
                    if physical_exact_two(m, n, r, s):
                        exact_two += 1
                    if split.k_S > 1 and split.k_O > 1:
                        mixed += 1
                    elif split.k_S > 1:
                        s_only += 1
                    elif split.k_O > 1:
                        o_only += 1
    return {
        "survivors": survivors,
        "physical_exact_two_survivors": exact_two,
        "mixed": mixed,
        "S_only": s_only,
        "O_only": o_only,
    }


def witness_report() -> list[dict]:
    witnesses = [
        (13, 1, 9, 1),   # S only, odd core 5
        (13, 4, 13, 1),  # O only, odd core 17
        (9, 1, 27, 14),  # mixed, 41 in S and 5 in O
    ]
    out = []
    for params in witnesses:
        split = classify_core(*params)
        nf = normal_form(*params)
        if not physical_exact_two(*params):
            raise AssertionError(f"witness is not exactly-two: {params}")
        out.append(
            {
                "params": list(params),
                "physical": nf["physical"],
                "k": split.k,
                "k_odd": split.k_odd,
                "k_S": split.k_S,
                "k_O": split.k_O,
                "S_primes": list(split.S_primes),
                "O_primes": list(split.O_primes),
            }
        )
    return out


if __name__ == "__main__":
    stats = scan_small_survivors()
    print("STAGE15_6AA_CORE_ADAPTER=PASS")
    print(f"SMALL_SURVIVORS={stats['survivors']}")
    print(f"SMALL_EXACT_TWO_SURVIVORS={stats['physical_exact_two_survivors']}")
    for row in witness_report():
        print(
            "WITNESS="
            f"{row['params']} k={row['k']} kS={row['k_S']} kO={row['k_O']}"
        )
