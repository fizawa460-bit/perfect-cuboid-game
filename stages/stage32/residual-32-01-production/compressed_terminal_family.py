#!/usr/bin/env python3
from __future__ import annotations

import functools
import math
from dataclasses import dataclass
from typing import Sequence

# The exact Stage32 production assignment order is
# [95,99,103,102,49,97,94,101,93,98,96].
# Write its values as x0,...,x10.  The current retained HNF/Aut certificates
# reduce the prefix filters to:
#   * x0 <= x1;
#   * if x0 == x1, then (x5,x6) <=lex (x8,x9);
#   * x1 + x8 + x9 + x10 == 0 (mod 2).
# The ten exceptional variables are every xi except x4.  Their total is <= e.
# The sole normal variable x4 is independent and lies in 0..19*d-5*e.
#
# This module does not change those mathematics.  It counts the same terminal
# family symbolically instead of visiting every DFS node one by one.

MAX_CERTIFIED_E = 729


def terminal_predicate(values: Sequence[int], *, e: int, d: int) -> bool:
    if len(values) != 11:
        raise ValueError("expected the 11 Stage32 pairing-prefix values")
    x = tuple(int(v) for v in values)
    if any(v < 0 for v in x):
        return False
    exceptional_sum = sum(x[i] for i in range(11) if i != 4)
    if exceptional_sum > int(e):
        return False
    normal_budget = 19 * int(d) - 5 * int(e)
    if normal_budget < 0 or x[4] > normal_budget:
        return False
    if x[0] > x[1]:
        return False
    if x[0] == x[1] and (x[5], x[6]) > (x[8], x[9]):
        return False
    if (x[1] + x[8] + x[9] + x[10]) % 2:
        return False
    return True


def _pair_lex_count(*, b_sum: int, a_sum: int) -> int:
    """Count ordered pair-pairs A,B with fixed sums and A <=lex B.

    A=(x5,x6), B=(x8,x9).  This is summed over every B with the requested
    b_sum, so only the two sums are needed by the symbolic convolution.
    """
    q = int(b_sum)
    s = int(a_sum)
    if q < 0 or s < 0:
        return 0
    if q <= s + 1:
        strict_first = q * (q + 1) // 2
    else:
        strict_first = (s + 1) * (2 * q - s) // 2
    diagonal_first = s + 1 if s <= q else 0
    return strict_first + diagonal_first


@dataclass(frozen=True)
class ExceptionalCountTable:
    max_e: int
    counts: tuple[int, ...]

    def count(self, e: int) -> int:
        e = int(e)
        if e < 0 or e > self.max_e:
            raise ValueError(f"e outside precomputed range 0..{self.max_e}: {e}")
        return self.counts[e]


@functools.lru_cache(maxsize=None)
def build_exceptional_count_table(max_e: int = MAX_CERTIFIED_E) -> ExceptionalCountTable:
    E = int(max_e)
    if E < 0:
        raise ValueError("max_e must be nonnegative")

    # F[R][p]: case x0<x1, after x0,x1 are fixed.  Count the remaining eight
    # exceptional variables with total <=R and parity
    # x8+x9+x10 == p (mod2).  Five other variables are parity-free.
    F = [[0, 0] for _ in range(E + 1)]
    for R in range(E + 1):
        for q in range(R + 1):
            three_with_sum_q = math.comb(q + 2, 2)
            five_with_sum_at_most = math.comb(R - q + 5, 5)
            F[R][q & 1] += three_with_sum_q * five_with_sum_at_most

    # P[u][p]: number of x0<x1 pairs with x0+x1=u and x1 parity p.
    P = [[0, 0] for _ in range(E + 1)]
    for x0 in range(E + 1):
        for x1 in range(x0 + 1, E - x0 + 1):
            P[x0 + x1][x1 & 1] += 1

    # T[L][p]: count x10 plus the three free variables x2,x3,x7 with total
    # <=L and x10 parity p.
    T = [[0, 0] for _ in range(E + 1)]
    for L in range(E + 1):
        for x10 in range(L + 1):
            T[L][x10 & 1] += math.comb(L - x10 + 3, 3)

    # W[u][p]: count the two ordered pairs A=(x5,x6), B=(x8,x9) with
    # A<=lex B, total pair mass u, and parity(sum(B))=p.
    W = [[0, 0] for _ in range(E + 1)]
    for u in range(E + 1):
        for q in range(u + 1):
            s = u - q
            W[u][q & 1] += _pair_lex_count(b_sum=q, a_sum=s)

    # G[R][p]: equal case x0=x1.  Count the remaining eight exceptional
    # variables subject to A<=lex B and sum(B)+x10 == p (mod2).
    G = [[0, 0] for _ in range(E + 1)]
    for R in range(E + 1):
        for u in range(R + 1):
            L = R - u
            for qpar in (0, 1):
                w = W[u][qpar]
                if not w:
                    continue
                G[R][qpar] += w * T[L][0]
                G[R][qpar ^ 1] += w * T[L][1]

    counts = []
    for e in range(E + 1):
        unequal = 0
        for u in range(e + 1):
            rem = e - u
            unequal += P[u][0] * F[rem][0] + P[u][1] * F[rem][1]

        equal = 0
        for a in range(e // 2 + 1):
            equal += G[e - 2 * a][a & 1]
        counts.append(unequal + equal)

    return ExceptionalCountTable(max_e=E, counts=tuple(counts))


def exceptional_terminal_count(e: int) -> int:
    e = int(e)
    if e < 0 or e > MAX_CERTIFIED_E:
        raise ValueError(f"e outside certified Stage32 range 0..{MAX_CERTIFIED_E}: {e}")
    return build_exceptional_count_table(MAX_CERTIFIED_E).count(e)


def stratum_terminal_count(*, e: int, d: int) -> int:
    e = int(e)
    d = int(d)
    normal_budget = 19 * d - 5 * e
    if e < 0 or normal_budget < 0:
        return 0
    return (normal_budget + 1) * exceptional_terminal_count(e)
