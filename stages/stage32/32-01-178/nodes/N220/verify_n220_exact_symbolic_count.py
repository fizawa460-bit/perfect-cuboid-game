#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

MAX_E = 729
EXPECTED_MANIFEST_CANONICAL = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PREFIX_CANONICAL = "65a5ab43e44ebb33341c250a8fa2c5ece09999203893f9a76ca46fb037df558f"
EXPECTED_ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_TOTAL_BEFORE_NODE_MASS = 688101306360803751427719294
EXPECTED_TOTAL_AFTER_NODE_MASS = 688101306357436883335845534
EXPECTED_N220_REJECTED = 342047598454520296245948565
EXPECTED_TOTAL_AFTER_N220 = 346053707902916587089896969
EXPECTED_EXACT_MASS_COUNTS_0_TO_5 = [1, 3, 16, 60, 195, 529]


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    body = dict(raw)
    body.pop("canonical_sha256_without_this_field", None)
    if claimed != expected or csha(body) != expected:
        raise ValueError(f"canonical hash regression: {path}")
    return raw


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = str(row_id).split("-d")
    return int(g[1:]), int(d)


def add_unbounded_variable(dp: list, *, parity_marked: bool) -> list:
    """Adjoin one nonnegative variable, tracking total mass/support/parity.

    dp[m][s][p] is an exact count.  A zero value adds no support; every
    positive value adds one support.  For parity_marked variables, parity is
    the value modulo 2.  Prefix sums make the unbounded update O(MAX_E*S).
    """
    max_support = len(dp[0]) - 1
    out = [[[0, 0] for _ in range(max_support + 2)] for __ in range(MAX_E + 1)]
    for s in range(max_support + 1):
        for p in (0, 1):
            for m in range(MAX_E + 1):
                value = dp[m][s][p]
                if value:
                    out[m][s][p] += value
            if not parity_marked:
                prefix = 0
                for m in range(1, MAX_E + 1):
                    prefix += dp[m - 1][s][p]
                    out[m][s + 1][p] += prefix
            else:
                even_index_prefix = 0
                odd_index_prefix = 0
                for m in range(1, MAX_E + 1):
                    old_index = m - 1
                    if old_index & 1:
                        odd_index_prefix += dp[old_index][s][p]
                    else:
                        even_index_prefix += dp[old_index][s][p]
                    if m & 1:
                        same = odd_index_prefix
                        opposite = even_index_prefix
                    else:
                        same = even_index_prefix
                        opposite = odd_index_prefix
                    out[m][s + 1][p] += same
                    out[m][s + 1][p ^ 1] += opposite
    return out


def build_free_distribution(*, unmarked: int, marked: int) -> list:
    dp = [[[0, 0]] for _ in range(MAX_E + 1)]
    dp[0][0][0] = 1
    for _ in range(unmarked):
        dp = add_unbounded_variable(dp, parity_marked=False)
    for _ in range(marked):
        dp = add_unbounded_variable(dp, parity_marked=True)
    return dp


def support_intervals(pair_sum: int) -> dict[int, list[tuple[int, int]]]:
    """First-coordinate intervals of a 2-vector with fixed sum by support."""
    if pair_sum == 0:
        return {0: [(0, 0)]}
    out = {1: [(0, 0), (pair_sum, pair_sum)]}
    if pair_sum >= 2:
        out[2] = [(1, pair_sum - 1)]
    return out


def interval_less(a_lo: int, a_hi: int, b_lo: int, b_hi: int) -> int:
    """Count (a,b) in two integer intervals with a<b exactly."""
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


def lex_pair_distribution(a_sum: int, b_sum: int) -> dict[tuple[int, int], int]:
    """Count A=(x5,x6), B=(x8,x9) with A<=lex B by support/parity(B)."""
    ai = support_intervals(a_sum)
    bi = support_intervals(b_sum)
    allow_equal_first = a_sum <= b_sum
    out: dict[tuple[int, int], int] = defaultdict(int)
    for sa, a_intervals in ai.items():
        for sb, b_intervals in bi.items():
            count = 0
            for a_lo, a_hi in a_intervals:
                for b_lo, b_hi in b_intervals:
                    count += interval_less(a_lo, a_hi, b_lo, b_hi)
                    if allow_equal_first:
                        count += interval_equal(a_lo, a_hi, b_lo, b_hi)
            if count:
                out[(sa + sb, b_sum & 1)] += count
    return out


def build_exceptional_exact_mass_support() -> list[list[int]]:
    """Exact current indexed-prefix count by exceptional mass and support.

    The ten exceptional variables are x0,x1,x2,x3,x5,x6,x7,x8,x9,x10.
    Split x0<x1 from x0=x1 exactly as the retained symbolic counter does.
    """
    # x0<x1.  Remaining eight variables have five parity-free variables and
    # parity x8+x9+x10.
    free8 = build_free_distribution(unmarked=5, marked=3)
    pair01 = [[[0, 0] for _ in range(3)] for __ in range(MAX_E + 1)]
    for x0 in range(MAX_E + 1):
        for x1 in range(x0 + 1, MAX_E - x0 + 1):
            mass = x0 + x1
            support = int(x0 > 0) + 1
            pair01[mass][support][x1 & 1] += 1

    unequal = [[0] * 11 for _ in range(MAX_E + 1)]
    for u in range(MAX_E + 1):
        for m in range(MAX_E - u + 1):
            total_mass = u + m
            for sp in (1, 2):
                for parity in (0, 1):
                    left = pair01[u][sp][parity]
                    if not left:
                        continue
                    for sf in range(9):
                        right = free8[m][sf][parity]
                        if right:
                            unequal[total_mass][sp + sf] += left * right

    # x0=x1=a.  Build exact distribution of A=(x5,x6)<=lex B=(x8,x9)
    # by total mass/support/parity(sum B).
    pair_pairs = [[[0, 0] for _ in range(5)] for __ in range(MAX_E + 1)]
    for a_sum in range(MAX_E + 1):
        for b_sum in range(MAX_E - a_sum + 1):
            mass = a_sum + b_sum
            for (support, parity), count in lex_pair_distribution(a_sum, b_sum).items():
                pair_pairs[mass][support][parity] += count

    # x2,x3,x7 are free; x10 carries parity.
    free4 = build_free_distribution(unmarked=3, marked=1)
    equal_remainder = [[[0, 0] for _ in range(9)] for __ in range(MAX_E + 1)]
    for u in range(MAX_E + 1):
        for m in range(MAX_E - u + 1):
            total_mass = u + m
            for sw in range(5):
                w0, w1 = pair_pairs[u][sw]
                if not (w0 or w1):
                    continue
                for st in range(5):
                    t0, t1 = free4[m][st]
                    if t0:
                        if w0:
                            equal_remainder[total_mass][sw + st][0] += w0 * t0
                        if w1:
                            equal_remainder[total_mass][sw + st][1] += w1 * t0
                    if t1:
                        if w0:
                            equal_remainder[total_mass][sw + st][1] += w0 * t1
                        if w1:
                            equal_remainder[total_mass][sw + st][0] += w1 * t1

    equal = [[0] * 11 for _ in range(MAX_E + 1)]
    for a in range(MAX_E // 2 + 1):
        base_mass = 2 * a
        base_support = 0 if a == 0 else 2
        required_parity = a & 1
        for m in range(MAX_E - base_mass + 1):
            for sr in range(9):
                count = equal_remainder[m][sr][required_parity]
                if count:
                    equal[base_mass + m][base_support + sr] += count

    exact = [
        [unequal[m][s] + equal[m][s] for s in range(11)]
        for m in range(MAX_E + 1)
    ]
    if [sum(exact[m]) for m in range(6)] != EXPECTED_EXACT_MASS_COUNTS_0_TO_5:
        raise ValueError("small exact-mass distribution regression")
    return exact


def n220_rejected_exceptional_prefixes(exact: list[list[int]], *, e: int, required: int) -> int:
    total = 0
    for mass in range(e + 1):
        remaining = e - mass
        extra_capacity = min(38, remaining)
        for support, count in enumerate(exact[mass]):
            if support + extra_capacity < required:
                total += count
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    args = ap.parse_args()

    manifest = load_canonical(args.manifest, EXPECTED_MANIFEST_CANONICAL)
    prefix = load_canonical(args.prefix_checkpoint, EXPECTED_PREFIX_CANONICAL)
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("indexed-terminal assignment-order regression")

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    exact = build_exceptional_exact_mass_support()
    cumulative_exceptional = []
    running = 0
    for e in range(MAX_E + 1):
        running += sum(exact[e])
        cumulative_exceptional.append(running)

    total_before_node_mass = 0
    total_after_node_mass = 0
    n220_rejected = 0
    for row_id in rows:
        genus, degree = parse_row_id(row_id)
        legacy_emin = 8 if genus == 0 else 4
        emax = (19 * degree) // 5
        required = ceil_div(degree - 16 * genus + 16, 4)
        effective_emin = max(legacy_emin, required)
        for e in range(legacy_emin, emax + 1):
            normal_count = 19 * degree - 5 * e + 1
            stratum_total = normal_count * cumulative_exceptional[e]
            total_before_node_mass += stratum_total
            if e < effective_emin:
                continue
            total_after_node_mass += stratum_total
            rejected_exceptional = n220_rejected_exceptional_prefixes(
                exact, e=e, required=required
            )
            n220_rejected += normal_count * rejected_exceptional

    total_after_n220 = total_after_node_mass - n220_rejected
    observed = {
        "total_before_node_mass": total_before_node_mass,
        "total_after_node_mass": total_after_node_mass,
        "n220_rejected": n220_rejected,
        "total_after_n220": total_after_n220,
    }
    expected = {
        "total_before_node_mass": EXPECTED_TOTAL_BEFORE_NODE_MASS,
        "total_after_node_mass": EXPECTED_TOTAL_AFTER_NODE_MASS,
        "n220_rejected": EXPECTED_N220_REJECTED,
        "total_after_n220": EXPECTED_TOTAL_AFTER_N220,
    }
    if observed != expected:
        raise ValueError(f"N220 symbolic-count regression: {observed} != {expected}")

    print(json.dumps({
        "verdict": "PASS_N220_EXACT_SYMBOLIC_FULL178_COUNT",
        "cut": "S10 + min(38, e-M10) >= ceil((d-16g+16)/4)",
        "rejection_fraction_numerator": n220_rejected,
        "rejection_fraction_denominator": total_after_node_mass,
        "rejection_percent_approx": 100.0 * n220_rejected / total_after_node_mass,
        **observed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
