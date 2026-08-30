#!/usr/bin/env python3
from __future__ import annotations

import functools
import math
from dataclasses import dataclass
from typing import Sequence

from compressed_terminal_family import exceptional_terminal_count, terminal_predicate


def _comp_count(total: int, parts: int) -> int:
    if total < 0 or parts <= 0:
        return 0
    return math.comb(total + parts - 1, parts - 1)


def _unrank_weak_composition(total: int, parts: int, rank: int) -> tuple[int, ...]:
    total = int(total)
    parts = int(parts)
    rank = int(rank)
    count = _comp_count(total, parts)
    if not 0 <= rank < count:
        raise ValueError(f"composition rank outside 0..{count - 1}: {rank}")
    if parts == 1:
        return (total,)
    out: list[int] = []
    remaining = total
    for k in range(parts, 1, -1):
        for value in range(remaining + 1):
            block = _comp_count(remaining - value, k - 1)
            if rank < block:
                out.append(value)
                remaining -= value
                break
            rank -= block
        else:
            raise AssertionError("weak-composition unrank fell through")
    out.append(remaining)
    return tuple(out)


def _rank_weak_composition(total: int, values: Sequence[int]) -> int:
    values = tuple(int(v) for v in values)
    if not values or any(v < 0 for v in values) or sum(values) != int(total):
        raise ValueError("invalid weak composition")
    rank = 0
    remaining = int(total)
    parts = len(values)
    for pos, value in enumerate(values[:-1]):
        suffix_parts = parts - pos - 1
        for smaller in range(value):
            rank += _comp_count(remaining - smaller, suffix_parts)
        remaining -= value
    return rank


def _unrank_sum_at_most(limit: int, parts: int, rank: int) -> tuple[int, ...]:
    # Add a final slack coordinate. Lexicographic order on the requested
    # coordinates is unchanged because slack appears only after all of them.
    full = _unrank_weak_composition(int(limit), int(parts) + 1, int(rank))
    return full[:-1]


def _rank_sum_at_most(limit: int, values: Sequence[int]) -> int:
    values = tuple(int(v) for v in values)
    slack = int(limit) - sum(values)
    if slack < 0:
        raise ValueError("sum exceeds at-most limit")
    return _rank_weak_composition(int(limit), values + (slack,))


@functools.lru_cache(maxsize=None)
def _F(rem: int, parity: int) -> int:
    """Unequal branch suffix count from compressed_terminal_family.F."""
    rem = int(rem)
    parity = int(parity) & 1
    if rem < 0:
        return 0
    total = 0
    for q in range(parity, rem + 1, 2):
        total += math.comb(q + 2, 2) * math.comb(rem - q + 5, 5)
    return total


@functools.lru_cache(maxsize=None)
def _T(limit: int, parity: int) -> int:
    """Equal branch x10+three-free suffix count."""
    limit = int(limit)
    parity = int(parity) & 1
    if limit < 0:
        return 0
    return sum(
        math.comb(limit - x10 + 3, 3)
        for x10 in range(parity, limit + 1, 2)
    )


def _pair_lex_count(*, b_sum: int, a_sum: int) -> int:
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


@functools.lru_cache(maxsize=None)
def _W(total_pair_mass: int, b_parity: int) -> int:
    u = int(total_pair_mass)
    p = int(b_parity) & 1
    if u < 0:
        return 0
    return sum(
        _pair_lex_count(b_sum=q, a_sum=u - q)
        for q in range(p, u + 1, 2)
    )


@functools.lru_cache(maxsize=None)
def _G(rem: int, target_parity: int) -> int:
    """Equal branch suffix count from compressed_terminal_family.G."""
    rem = int(rem)
    target = int(target_parity) & 1
    if rem < 0:
        return 0
    total = 0
    for u in range(rem + 1):
        limit = rem - u
        for bpar in (0, 1):
            total += _W(u, bpar) * _T(limit, target ^ bpar)
    return total


def _pair_unrank(a_sum: int, b_sum: int, rank: int) -> tuple[int, int, int, int]:
    s = int(a_sum)
    q = int(b_sum)
    rank = int(rank)
    count = _pair_lex_count(b_sum=q, a_sum=s)
    if not 0 <= rank < count:
        raise ValueError("pair-lex rank outside family")
    for x5 in range(s + 1):
        x6 = s - x5
        allowed: list[int] = []
        if s <= q and x5 <= q:
            allowed.append(x5)
        allowed.extend(range(x5 + 1, q + 1))
        if rank < len(allowed):
            x8 = allowed[rank]
            return x5, x6, x8, q - x8
        rank -= len(allowed)
    raise AssertionError("pair-lex unrank fell through")


def _pair_rank(a_sum: int, b_sum: int, values: Sequence[int]) -> int:
    x5, x6, x8, x9 = (int(v) for v in values)
    s = int(a_sum)
    q = int(b_sum)
    if x5 + x6 != s or x8 + x9 != q or (x5, x6) > (x8, x9):
        raise ValueError("pair is outside lex-canonical fixed-sum family")
    rank = 0
    for prior_x5 in range(x5):
        allowed = 0
        if s <= q and prior_x5 <= q:
            allowed += 1
        allowed += max(q - prior_x5, 0)
        rank += allowed
    allowed_current: list[int] = []
    if s <= q and x5 <= q:
        allowed_current.append(x5)
    allowed_current.extend(range(x5 + 1, q + 1))
    try:
        rank += allowed_current.index(x8)
    except ValueError as exc:
        raise ValueError("pair is outside lex-canonical family") from exc
    return rank


@dataclass(frozen=True)
class CompressedTerminalIndexer:
    """Exact random access to the current Stage32 11-pairing terminal family.

    This does not preserve the legacy DFS stream order. It defines a new,
    source-controlled canonical compressed order whose set is exactly the same
    as `terminal_predicate`. The normal variable x4 is the innermost coordinate;
    exceptional families are ordered UNEQUAL(x0<x1) then EQUAL(x0=x1).
    """

    e: int
    d: int

    def __post_init__(self) -> None:
        e = int(self.e)
        d = int(self.d)
        if e < 0 or 19 * d - 5 * e < 0:
            raise ValueError("invalid Stage32 stratum")
        object.__setattr__(self, "e", e)
        object.__setattr__(self, "d", d)

    @property
    def normal_budget(self) -> int:
        return 19 * self.d - 5 * self.e

    @property
    def exceptional_count(self) -> int:
        return exceptional_terminal_count(self.e)

    @property
    def terminal_count(self) -> int:
        return (self.normal_budget + 1) * self.exceptional_count

    def unequal_count(self) -> int:
        total = 0
        for x0 in range(self.e + 1):
            for x1 in range(x0 + 1, self.e - x0 + 1):
                total += _F(self.e - x0 - x1, x1 & 1)
        return total

    def equal_count(self) -> int:
        return sum(_G(self.e - 2 * a, a & 1) for a in range(self.e // 2 + 1))

    def _unrank_unequal(self, rank: int) -> tuple[int, ...]:
        rank = int(rank)
        for x0 in range(self.e + 1):
            for x1 in range(x0 + 1, self.e - x0 + 1):
                rem = self.e - x0 - x1
                block = _F(rem, x1 & 1)
                if rank >= block:
                    rank -= block
                    continue

                for q in range(x1 & 1, rem + 1, 2):
                    triple_count = math.comb(q + 2, 2)
                    free_count = math.comb(rem - q + 5, 5)
                    qblock = triple_count * free_count
                    if rank >= qblock:
                        rank -= qblock
                        continue
                    triple_rank, free_rank = divmod(rank, free_count)
                    x8, x9, x10 = _unrank_weak_composition(q, 3, triple_rank)
                    x2, x3, x5, x6, x7 = _unrank_sum_at_most(
                        rem - q, 5, free_rank
                    )
                    return (x0, x1, x2, x3, 0, x5, x6, x7, x8, x9, x10)
                raise AssertionError("unequal q-unrank fell through")
        raise ValueError("unequal rank outside family")

    def _rank_unequal(self, x: Sequence[int]) -> int:
        x = tuple(int(v) for v in x)
        x0, x1 = x[0], x[1]
        if not x0 < x1:
            raise ValueError("not an unequal terminal")
        rank = 0
        for a0 in range(self.e + 1):
            for a1 in range(a0 + 1, self.e - a0 + 1):
                rem = self.e - a0 - a1
                if (a0, a1) == (x0, x1):
                    q = x[8] + x[9] + x[10]
                    if q > rem or (q & 1) != (x1 & 1):
                        raise ValueError("unequal parity/budget regression")
                    for prior_q in range(x1 & 1, q, 2):
                        rank += math.comb(prior_q + 2, 2) * math.comb(
                            rem - prior_q + 5, 5
                        )
                    free_limit = rem - q
                    free_count = math.comb(free_limit + 5, 5)
                    triple_rank = _rank_weak_composition(q, (x[8], x[9], x[10]))
                    free_rank = _rank_sum_at_most(
                        free_limit, (x[2], x[3], x[5], x[6], x[7])
                    )
                    return rank + triple_rank * free_count + free_rank
                rank += _F(rem, a1 & 1)
        raise ValueError("unequal terminal pair outside family")

    def _unrank_equal(self, rank: int) -> tuple[int, ...]:
        rank = int(rank)
        for a in range(self.e // 2 + 1):
            rem = self.e - 2 * a
            block = _G(rem, a & 1)
            if rank >= block:
                rank -= block
                continue
            target = a & 1
            for u in range(rem + 1):
                limit = rem - u
                for bpar in (0, 1):
                    p10 = target ^ bpar
                    block2 = _W(u, bpar) * _T(limit, p10)
                    if rank >= block2:
                        rank -= block2
                        continue
                    tcount = _T(limit, p10)
                    pair_family_rank, tail_rank = divmod(rank, tcount)

                    for q in range(bpar, u + 1, 2):
                        s = u - q
                        pair_count = _pair_lex_count(b_sum=q, a_sum=s)
                        if pair_family_rank >= pair_count:
                            pair_family_rank -= pair_count
                            continue
                        x5, x6, x8, x9 = _pair_unrank(s, q, pair_family_rank)
                        break
                    else:
                        raise AssertionError("equal pair-family unrank fell through")

                    for x10 in range(p10, limit + 1, 2):
                        free_count = math.comb(limit - x10 + 3, 3)
                        if tail_rank >= free_count:
                            tail_rank -= free_count
                            continue
                        x2, x3, x7 = _unrank_sum_at_most(
                            limit - x10, 3, tail_rank
                        )
                        return (a, a, x2, x3, 0, x5, x6, x7, x8, x9, x10)
                    raise AssertionError("equal tail unrank fell through")
            raise AssertionError("equal u-unrank fell through")
        raise ValueError("equal rank outside family")

    def _rank_equal(self, x: Sequence[int]) -> int:
        x = tuple(int(v) for v in x)
        a = x[0]
        if x[1] != a:
            raise ValueError("not an equal terminal")
        rank = 0
        for prior_a in range(a):
            if 2 * prior_a <= self.e:
                rank += _G(self.e - 2 * prior_a, prior_a & 1)
        rem = self.e - 2 * a
        if rem < 0:
            raise ValueError("equal terminal exceeds exceptional budget")

        u = x[5] + x[6] + x[8] + x[9]
        q = x[8] + x[9]
        s = x[5] + x[6]
        bpar = q & 1
        target = a & 1
        p10 = target ^ bpar
        if (x[10] & 1) != p10:
            raise ValueError("equal terminal parity regression")

        for prior_u in range(u):
            limit = rem - prior_u
            for prior_bpar in (0, 1):
                rank += _W(prior_u, prior_bpar) * _T(
                    limit, target ^ prior_bpar
                )
        limit = rem - u
        if limit < 0:
            raise ValueError("equal terminal exceeds exceptional budget")
        for prior_bpar in range(bpar):
            rank += _W(u, prior_bpar) * _T(limit, target ^ prior_bpar)

        tcount = _T(limit, p10)
        pair_family_rank = 0
        for prior_q in range(bpar, q, 2):
            pair_family_rank += _pair_lex_count(
                b_sum=prior_q, a_sum=u - prior_q
            )
        pair_family_rank += _pair_rank(s, q, (x[5], x[6], x[8], x[9]))
        rank += pair_family_rank * tcount

        tail_rank = 0
        for prior_x10 in range(p10, x[10], 2):
            tail_rank += math.comb(limit - prior_x10 + 3, 3)
        free_limit = limit - x[10]
        if free_limit < 0:
            raise ValueError("equal tail exceeds exceptional budget")
        tail_rank += _rank_sum_at_most(free_limit, (x[2], x[3], x[7]))
        return rank + tail_rank

    def unrank(self, rank: int) -> tuple[int, ...]:
        rank = int(rank)
        if not 0 <= rank < self.terminal_count:
            raise ValueError(f"terminal rank outside 0..{self.terminal_count - 1}: {rank}")
        exceptional_rank, x4 = divmod(rank, self.normal_budget + 1)
        unequal = self.unequal_count()
        if exceptional_rank < unequal:
            x = list(self._unrank_unequal(exceptional_rank))
        else:
            x = list(self._unrank_equal(exceptional_rank - unequal))
        x[4] = x4
        out = tuple(x)
        if not terminal_predicate(out, e=self.e, d=self.d):
            raise AssertionError("indexed terminal failed exact terminal predicate")
        return out

    def rank(self, values: Sequence[int]) -> int:
        x = tuple(int(v) for v in values)
        if len(x) != 11 or not terminal_predicate(x, e=self.e, d=self.d):
            raise ValueError("values are outside this Stage32 terminal family")
        if x[0] < x[1]:
            exceptional_rank = self._rank_unequal(x)
        else:
            exceptional_rank = self.unequal_count() + self._rank_equal(x)
        rank = exceptional_rank * (self.normal_budget + 1) + x[4]
        if self.unrank(rank) != x:
            raise AssertionError("terminal rank/unrank roundtrip regression")
        return rank

    def certificate(self) -> dict:
        unequal = self.unequal_count()
        equal = self.equal_count()
        if unequal + equal != self.exceptional_count:
            raise ValueError(
                f"compressed branch count regression: {unequal}+{equal}!={self.exceptional_count}"
            )
        return {
            "schema": "STAGE32_RESIDUAL32_01_COMPRESSED_TERMINAL_INDEXER_V1",
            "e": self.e,
            "d": self.d,
            "normal_budget": self.normal_budget,
            "exceptional_terminal_count": str(self.exceptional_count),
            "unequal_exceptional_count": str(unequal),
            "equal_exceptional_count": str(equal),
            "terminal_count": str(self.terminal_count),
            "canonical_index_order": "EXCEPTIONAL_UNEQUAL_THEN_EQUAL__NORMAL_X4_INNERMOST",
            "legacy_dfs_stream_order_preserved": False,
            "terminal_set_exactly_current_prefix_terminal_predicate": True,
            "random_access_unrank_available": True,
            "inverse_rank_available": True,
            "full_terminal_materialization_required_for_random_access": False,
        }
