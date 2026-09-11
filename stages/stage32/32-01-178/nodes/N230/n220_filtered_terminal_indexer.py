#!/usr/bin/env python3
from __future__ import annotations

import functools
import hashlib
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[5]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_indexer import CompressedTerminalIndexer

EXPECTED_OLD_INDEXER_GIT_BLOB_SHA1 = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"
OLD_INDEXER_PATH = RESIDUAL / "compressed_terminal_indexer.py"
CANONICAL_OLD_ORDER = "EXCEPTIONAL_UNEQUAL_THEN_EQUAL__NORMAL_X4_INNERMOST"


def ceil_div(a: int, b: int) -> int:
    return -((-int(a)) // int(b))


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    header = f"blob {len(raw)}\0".encode()
    return hashlib.sha1(header + raw).hexdigest()


def composition_support_count(parts: int, mass: int, support: int) -> int:
    parts = int(parts)
    mass = int(mass)
    support = int(support)
    if mass == 0:
        return int(support == 0)
    if support <= 0 or support > parts or support > mass:
        return 0
    return math.comb(parts, support) * math.comb(mass - 1, support - 1)


def _add_unbounded_variable(dp: list, max_e: int, *, parity_marked: bool) -> list:
    max_support = len(dp[0]) - 1
    out = [[[0, 0] for _ in range(max_support + 2)] for __ in range(max_e + 1)]
    for s in range(max_support + 1):
        for p in (0, 1):
            for m in range(max_e + 1):
                value = dp[m][s][p]
                if value:
                    out[m][s][p] += value
            if not parity_marked:
                prefix = 0
                for m in range(1, max_e + 1):
                    prefix += dp[m - 1][s][p]
                    out[m][s + 1][p] += prefix
            else:
                even_prefix = 0
                odd_prefix = 0
                for m in range(1, max_e + 1):
                    old_index = m - 1
                    if old_index & 1:
                        odd_prefix += dp[old_index][s][p]
                    else:
                        even_prefix += dp[old_index][s][p]
                    if m & 1:
                        same, opposite = odd_prefix, even_prefix
                    else:
                        same, opposite = even_prefix, odd_prefix
                    out[m][s + 1][p] += same
                    out[m][s + 1][p ^ 1] += opposite
    return out


def build_free_distribution(max_e: int, *, unmarked: int, marked: int) -> list:
    dp = [[[0, 0]] for _ in range(max_e + 1)]
    dp[0][0][0] = 1
    for _ in range(unmarked):
        dp = _add_unbounded_variable(dp, max_e, parity_marked=False)
    for _ in range(marked):
        dp = _add_unbounded_variable(dp, max_e, parity_marked=True)
    return dp


def support_intervals(pair_sum: int) -> dict[int, list[tuple[int, int]]]:
    pair_sum = int(pair_sum)
    if pair_sum == 0:
        return {0: [(0, 0)]}
    out = {1: [(0, 0), (pair_sum, pair_sum)]}
    if pair_sum >= 2:
        out[2] = [(1, pair_sum - 1)]
    return out


def interval_less(a_lo: int, a_hi: int, b_lo: int, b_hi: int) -> int:
    total = 0
    lo, hi = a_lo, min(a_hi, b_lo - 1)
    if lo <= hi:
        total += (hi - lo + 1) * (b_hi - b_lo + 1)
    lo, hi = max(a_lo, b_lo), min(a_hi, b_hi - 1)
    if lo <= hi:
        n = hi - lo + 1
        total += n * b_hi - (lo + hi) * n // 2
    return total


def interval_equal(a_lo: int, a_hi: int, b_lo: int, b_hi: int) -> int:
    return max(0, min(a_hi, b_hi) - max(a_lo, b_lo) + 1)


@functools.lru_cache(maxsize=None)
def lex_pair_support_distribution(a_sum: int, b_sum: int) -> tuple[tuple[int, int], ...]:
    ai = support_intervals(a_sum)
    bi = support_intervals(b_sum)
    allow_equal_first = int(a_sum) <= int(b_sum)
    out: dict[int, int] = defaultdict(int)
    for sa, a_intervals in ai.items():
        for sb, b_intervals in bi.items():
            count = 0
            for a_lo, a_hi in a_intervals:
                for b_lo, b_hi in b_intervals:
                    count += interval_less(a_lo, a_hi, b_lo, b_hi)
                    if allow_equal_first:
                        count += interval_equal(a_lo, a_hi, b_lo, b_hi)
            if count:
                out[sa + sb] += count
    return tuple(sorted(out.items()))


class N220FilteredTerminalIndexer:
    """Exact N220 survivor random access preserving the old canonical rank.

    The authoritative identity remains the old stratum-local
    CompressedTerminalIndexer(e,d) rank.  This class adds only a secondary
    survivor rank.  N220 is independent of x4, so filtering is performed on
    the exceptional-rank axis and the old x4 innermost block is preserved.
    """

    def __init__(self, genus: int, degree: int, e: int) -> None:
        self.genus = int(genus)
        self.degree = int(degree)
        self.e = int(e)
        if git_blob_sha1(OLD_INDEXER_PATH) != EXPECTED_OLD_INDEXER_GIT_BLOB_SHA1:
            raise ValueError("compressed_terminal_indexer.py source-lock regression")
        self.old = CompressedTerminalIndexer(self.e, self.degree)
        cert = self.old.certificate()
        if cert["canonical_index_order"] != CANONICAL_OLD_ORDER:
            raise ValueError("old canonical index order regression")
        self.normal_block = self.old.normal_budget + 1
        self.required_support = ceil_div(self.degree - 16 * self.genus + 16, 4)
        self._free8 = build_free_distribution(self.e, unmarked=5, marked=3)
        self._equal_remainder = None

    def accepts(self, values: Sequence[int]) -> bool:
        x = tuple(int(v) for v in values)
        if len(x) != 11:
            raise ValueError("expected 11 indexed-terminal coordinates")
        mass = sum(x[i] for i in range(11) if i != 4)
        support = sum(1 for i in range(11) if i != 4 and x[i] > 0)
        if mass > self.e:
            return False
        return support + min(38, self.e - mass) >= self.required_support

    @functools.lru_cache(maxsize=None)
    def _free_at_most_count(self, parts: int, limit: int, support_base: int) -> int:
        if limit < 0:
            return 0
        total = 0
        for mass in range(limit + 1):
            remaining = limit - mass
            max_support = min(parts, mass) if mass else 0
            for support in range(max_support + 1):
                count = composition_support_count(parts, mass, support)
                if count and support_base + support + min(38, remaining) >= self.required_support:
                    total += count
        return total

    @functools.lru_cache(maxsize=None)
    def _unequal_pair_count_by(self, rem: int, parity: int, support_base: int) -> int:
        total = 0
        for mass in range(rem + 1):
            remaining = rem - mass
            row = self._free8[mass]
            for support in range(len(row)):
                count = row[support][parity & 1]
                if count and support_base + support + min(38, remaining) >= self.required_support:
                    total += count
        return total

    def _unequal_pair_count(self, x0: int, x1: int) -> int:
        rem = self.e - x0 - x1
        support_base = int(x0 > 0) + 1
        return self._unequal_pair_count_by(rem, x1 & 1, support_base)

    @functools.lru_cache(maxsize=None)
    def _unequal_q_count(self, rem: int, parity: int, support_base: int, q: int) -> int:
        if q < 0 or q > rem or (q & 1) != (parity & 1):
            return 0
        free_limit = rem - q
        total = 0
        max_support = min(3, q) if q else 0
        for triple_support in range(max_support + 1):
            count = composition_support_count(3, q, triple_support)
            if count:
                total += count * self._free_at_most_count(
                    5, free_limit, support_base + triple_support
                )
        return total

    @functools.lru_cache(maxsize=None)
    def _tail_count(self, limit: int, x10_parity: int, support_base: int) -> int:
        total = 0
        for x10 in range(x10_parity & 1, limit + 1, 2):
            total += self._free_at_most_count(
                3, limit - x10, support_base + int(x10 > 0)
            )
        return total

    @functools.lru_cache(maxsize=None)
    def _equal_u_block_count(self, a: int, u: int, b_parity: int) -> int:
        rem = self.e - 2 * a
        limit = rem - u
        if limit < 0:
            return 0
        support_base = 0 if a == 0 else 2
        x10_parity = (a & 1) ^ (b_parity & 1)
        total = 0
        for q in range(b_parity & 1, u + 1, 2):
            a_sum = u - q
            for pair_support, count in lex_pair_support_distribution(a_sum, q):
                total += count * self._tail_count(
                    limit, x10_parity, support_base + pair_support
                )
        return total

    def _build_equal_remainder(self) -> None:
        if self._equal_remainder is not None:
            return
        pair_pairs = [[[0, 0] for _ in range(5)] for __ in range(self.e + 1)]
        for a_sum in range(self.e + 1):
            for b_sum in range(self.e - a_sum + 1):
                mass = a_sum + b_sum
                parity = b_sum & 1
                for support, count in lex_pair_support_distribution(a_sum, b_sum):
                    pair_pairs[mass][support][parity] += count

        free4 = build_free_distribution(self.e, unmarked=3, marked=1)
        equal_remainder = [[[0, 0] for _ in range(9)] for __ in range(self.e + 1)]
        for pair_mass in range(self.e + 1):
            for free_mass in range(self.e - pair_mass + 1):
                total_mass = pair_mass + free_mass
                for pair_support in range(5):
                    w0, w1 = pair_pairs[pair_mass][pair_support]
                    if not (w0 or w1):
                        continue
                    for free_support in range(5):
                        t0, t1 = free4[free_mass][free_support]
                        if t0:
                            if w0:
                                equal_remainder[total_mass][pair_support + free_support][0] += w0 * t0
                            if w1:
                                equal_remainder[total_mass][pair_support + free_support][1] += w1 * t0
                        if t1:
                            if w0:
                                equal_remainder[total_mass][pair_support + free_support][1] += w0 * t1
                            if w1:
                                equal_remainder[total_mass][pair_support + free_support][0] += w1 * t1
        self._equal_remainder = equal_remainder

    @functools.lru_cache(maxsize=None)
    def _equal_a_count(self, a: int) -> int:
        self._build_equal_remainder()
        rem = self.e - 2 * a
        if rem < 0:
            return 0
        support_base = 0 if a == 0 else 2
        required_parity = a & 1
        total = 0
        for mass in range(rem + 1):
            remaining = rem - mass
            row = self._equal_remainder[mass]
            for support in range(9):
                count = row[support][required_parity]
                if count and support_base + support + min(38, remaining) >= self.required_support:
                    total += count
        return total

    @property
    def accepted_exceptional_count(self) -> int:
        total = 0
        for x0 in range(self.e + 1):
            for x1 in range(x0 + 1, self.e - x0 + 1):
                total += self._unequal_pair_count(x0, x1)
        for a in range(self.e // 2 + 1):
            total += self._equal_a_count(a)
        return total

    @property
    def terminal_count(self) -> int:
        return self.accepted_exceptional_count * self.normal_block

    def _rank_free_at_most(
        self, values: Sequence[int], limit: int, support_base: int
    ) -> int:
        values = tuple(int(v) for v in values)
        rank = 0
        used = 0
        support = 0
        for pos, value in enumerate(values):
            remaining_parts = len(values) - pos - 1
            remaining_limit = limit - used
            for smaller in range(value):
                rank += self._free_at_most_count(
                    remaining_parts,
                    remaining_limit - smaller,
                    support_base + support + int(smaller > 0),
                )
            used += value
            support += int(value > 0)
        return rank

    def _unrank_free_at_most(
        self, parts: int, limit: int, support_base: int, rank: int
    ) -> tuple[int, ...]:
        out: list[int] = []
        used = 0
        support = 0
        for pos in range(parts):
            remaining_parts = parts - pos - 1
            remaining_limit = limit - used
            for value in range(remaining_limit + 1):
                count = self._free_at_most_count(
                    remaining_parts,
                    remaining_limit - value,
                    support_base + support + int(value > 0),
                )
                if rank < count:
                    out.append(value)
                    used += value
                    support += int(value > 0)
                    break
                rank -= count
            else:
                raise ValueError("filtered free-composition unrank fell through")
        return tuple(out)

    def rank_exceptional(self, values: Sequence[int]) -> int:
        x = tuple(int(v) for v in values)
        if not self.accepts(x):
            raise ValueError("terminal is rejected by audited N220 predicate")
        rank = 0
        if x[0] < x[1]:
            target_x0, target_x1 = x[0], x[1]
            for x0 in range(self.e + 1):
                for x1 in range(x0 + 1, self.e - x0 + 1):
                    if (x0, x1) == (target_x0, target_x1):
                        rem = self.e - x0 - x1
                        support_base = int(x0 > 0) + 1
                        q = x[8] + x[9] + x[10]
                        for prior_q in range(x1 & 1, q, 2):
                            rank += self._unequal_q_count(
                                rem, x1 & 1, support_base, prior_q
                            )
                        free_limit = rem - q
                        for x8 in range(x[8] + 1):
                            x9_stop = x[9] if x8 == x[8] else q - x8 + 1
                            for x9 in range(x9_stop):
                                x10 = q - x8 - x9
                                triple_support = sum(
                                    int(v > 0) for v in (x8, x9, x10)
                                )
                                rank += self._free_at_most_count(
                                    5, free_limit, support_base + triple_support
                                )
                        triple_support = sum(
                            int(v > 0) for v in (x[8], x[9], x[10])
                        )
                        rank += self._rank_free_at_most(
                            (x[2], x[3], x[5], x[6], x[7]),
                            free_limit,
                            support_base + triple_support,
                        )
                        return rank
                    rank += self._unequal_pair_count(x0, x1)
            raise ValueError("unequal terminal outside filtered family")

        for x0 in range(self.e + 1):
            for x1 in range(x0 + 1, self.e - x0 + 1):
                rank += self._unequal_pair_count(x0, x1)
        a = x[0]
        for prior_a in range(a):
            rank += self._equal_a_count(prior_a)
        rem = self.e - 2 * a
        target_parity = a & 1
        u = x[5] + x[6] + x[8] + x[9]
        q = x[8] + x[9]
        a_sum = u - q
        b_parity = q & 1
        for prior_u in range(u):
            for prior_parity in (0, 1):
                rank += self._equal_u_block_count(a, prior_u, prior_parity)
        for prior_parity in range(b_parity):
            rank += self._equal_u_block_count(a, u, prior_parity)

        limit = rem - u
        x10_parity = target_parity ^ b_parity
        support_base = 0 if a == 0 else 2
        for prior_q in range(b_parity, q, 2):
            prior_a_sum = u - prior_q
            for pair_support, count in lex_pair_support_distribution(
                prior_a_sum, prior_q
            ):
                rank += count * self._tail_count(
                    limit, x10_parity, support_base + pair_support
                )

        target_x5, target_x8 = x[5], x[8]
        for x5 in range(a_sum + 1):
            allowed_x8: list[int] = []
            if a_sum <= q and x5 <= q:
                allowed_x8.append(x5)
            allowed_x8.extend(range(x5 + 1, q + 1))
            if x5 < target_x5:
                candidates = allowed_x8
            elif x5 == target_x5:
                candidates = allowed_x8[: allowed_x8.index(target_x8)]
            else:
                candidates = []
            for x8 in candidates:
                pair_support = sum(
                    int(v > 0) for v in (x5, a_sum - x5, x8, q - x8)
                )
                rank += self._tail_count(
                    limit, x10_parity, support_base + pair_support
                )
            if x5 == target_x5:
                break

        pair_support = sum(
            int(v > 0) for v in (x[5], x[6], x[8], x[9])
        )
        for prior_x10 in range(x10_parity, x[10], 2):
            rank += self._free_at_most_count(
                3,
                limit - prior_x10,
                support_base + pair_support + int(prior_x10 > 0),
            )
        rank += self._rank_free_at_most(
            (x[2], x[3], x[7]),
            limit - x[10],
            support_base + pair_support + int(x[10] > 0),
        )
        return rank

    def unrank_exceptional(self, rank: int) -> tuple[int, ...]:
        rank = int(rank)
        if not 0 <= rank < self.accepted_exceptional_count:
            raise ValueError("filtered exceptional rank outside family")

        for x0 in range(self.e + 1):
            for x1 in range(x0 + 1, self.e - x0 + 1):
                count = self._unequal_pair_count(x0, x1)
                if rank >= count:
                    rank -= count
                    continue
                rem = self.e - x0 - x1
                support_base = int(x0 > 0) + 1
                for q in range(x1 & 1, rem + 1, 2):
                    count = self._unequal_q_count(rem, x1 & 1, support_base, q)
                    if rank >= count:
                        rank -= count
                        continue
                    free_limit = rem - q
                    for x8 in range(q + 1):
                        for x9 in range(q - x8 + 1):
                            x10 = q - x8 - x9
                            triple_support = sum(
                                int(v > 0) for v in (x8, x9, x10)
                            )
                            count = self._free_at_most_count(
                                5, free_limit, support_base + triple_support
                            )
                            if rank >= count:
                                rank -= count
                                continue
                            x2, x3, x5, x6, x7 = self._unrank_free_at_most(
                                5,
                                free_limit,
                                support_base + triple_support,
                                rank,
                            )
                            return (
                                x0,
                                x1,
                                x2,
                                x3,
                                0,
                                x5,
                                x6,
                                x7,
                                x8,
                                x9,
                                x10,
                            )
                    raise AssertionError("filtered unequal q block fell through")
                raise AssertionError("filtered unequal pair block fell through")

        for a in range(self.e // 2 + 1):
            count = self._equal_a_count(a)
            if rank >= count:
                rank -= count
                continue
            rem = self.e - 2 * a
            target_parity = a & 1
            support_base = 0 if a == 0 else 2
            for u in range(rem + 1):
                for b_parity in (0, 1):
                    count = self._equal_u_block_count(a, u, b_parity)
                    if rank >= count:
                        rank -= count
                        continue
                    limit = rem - u
                    x10_parity = target_parity ^ b_parity
                    for q in range(b_parity, u + 1, 2):
                        a_sum = u - q
                        q_count = sum(
                            count * self._tail_count(
                                limit, x10_parity, support_base + pair_support
                            )
                            for pair_support, count in lex_pair_support_distribution(
                                a_sum, q
                            )
                        )
                        if rank >= q_count:
                            rank -= q_count
                            continue
                        for x5 in range(a_sum + 1):
                            allowed_x8: list[int] = []
                            if a_sum <= q and x5 <= q:
                                allowed_x8.append(x5)
                            allowed_x8.extend(range(x5 + 1, q + 1))
                            for x8 in allowed_x8:
                                x6 = a_sum - x5
                                x9 = q - x8
                                pair_support = sum(
                                    int(v > 0)
                                    for v in (x5, x6, x8, x9)
                                )
                                count = self._tail_count(
                                    limit,
                                    x10_parity,
                                    support_base + pair_support,
                                )
                                if rank >= count:
                                    rank -= count
                                    continue
                                for x10 in range(x10_parity, limit + 1, 2):
                                    count = self._free_at_most_count(
                                        3,
                                        limit - x10,
                                        support_base
                                        + pair_support
                                        + int(x10 > 0),
                                    )
                                    if rank >= count:
                                        rank -= count
                                        continue
                                    x2, x3, x7 = self._unrank_free_at_most(
                                        3,
                                        limit - x10,
                                        support_base
                                        + pair_support
                                        + int(x10 > 0),
                                        rank,
                                    )
                                    return (
                                        a,
                                        a,
                                        x2,
                                        x3,
                                        0,
                                        x5,
                                        x6,
                                        x7,
                                        x8,
                                        x9,
                                        x10,
                                    )
                        raise AssertionError("filtered equal pair block fell through")
            raise AssertionError("filtered equal a block fell through")
        raise AssertionError("filtered exceptional unrank fell through")

    def rank(self, values: Sequence[int]) -> int:
        x = tuple(int(v) for v in values)
        old_rank = self.old.rank(x)
        if not self.accepts(x):
            raise ValueError(f"old canonical rank {old_rank} is N220_REJECTED")
        exceptional = list(x)
        x4 = exceptional[4]
        exceptional[4] = 0
        filtered_exceptional_rank = self.rank_exceptional(tuple(exceptional))
        filtered_rank = filtered_exceptional_rank * self.normal_block + x4
        if self.unrank(filtered_rank) != x:
            raise AssertionError("filtered rank/unrank roundtrip regression")
        return filtered_rank

    def unrank(self, rank: int) -> tuple[int, ...]:
        rank = int(rank)
        if not 0 <= rank < self.terminal_count:
            raise ValueError("filtered terminal rank outside family")
        filtered_exceptional_rank, x4 = divmod(rank, self.normal_block)
        x = list(self.unrank_exceptional(filtered_exceptional_rank))
        x[4] = x4
        out = tuple(x)
        if not self.accepts(out):
            raise AssertionError("filtered unrank returned N220 rejection")
        self.old.rank(out)
        return out

    def filtered_rank_of_old(self, old_rank: int) -> int | None:
        x = self.old.unrank(int(old_rank))
        if not self.accepts(x):
            return None
        return self.rank(x)

    def old_rank_of_filtered(self, filtered_rank: int) -> int:
        return self.old.rank(self.unrank(int(filtered_rank)))

    def disposition_of_old(self, old_rank: int) -> dict:
        old_rank = int(old_rank)
        x = self.old.unrank(old_rank)
        if not self.accepts(x):
            return {"old_rank": old_rank, "disposition": "N220_REJECTED"}
        return {
            "old_rank": old_rank,
            "disposition": "N220_SURVIVOR",
            "filtered_rank": self.rank(x),
        }

    def certificate(self) -> dict:
        old_exceptional = self.old.exceptional_count
        accepted_exceptional = self.accepted_exceptional_count
        old_terminal = self.old.terminal_count
        accepted_terminal = self.terminal_count
        return {
            "schema": "STAGE32_32_01_178_N230_N220_FILTERED_TERMINAL_INDEXER_V1",
            "genus": self.genus,
            "degree": self.degree,
            "e": self.e,
            "required_support": self.required_support,
            "old_indexer_git_blob_sha1": EXPECTED_OLD_INDEXER_GIT_BLOB_SHA1,
            "old_canonical_order": CANONICAL_OLD_ORDER,
            "normal_block": self.normal_block,
            "old_exceptional_count": str(old_exceptional),
            "accepted_exceptional_count": str(accepted_exceptional),
            "rejected_exceptional_count": str(old_exceptional - accepted_exceptional),
            "old_terminal_count": str(old_terminal),
            "filtered_terminal_count": str(accepted_terminal),
            "n220_rejected_terminal_count": str(old_terminal - accepted_terminal),
            "old_rank_remains_completeness_authority": True,
            "secondary_rank_only": True,
            "x4_block_preserved_exactly": True,
            "materializes_full_terminal_family": False,
            "materializes_full_exceptional_family": False,
        }
