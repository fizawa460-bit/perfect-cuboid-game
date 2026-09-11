#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import verify_n220_exact_symbolic_count as base


def build_support_lt(exact: list[list[int]]) -> list[list[int]]:
    """support_lt[m][t] = count at exact mass m with support < t."""
    out = [[0] * 13 for _ in range(base.MAX_E + 1)]
    for mass in range(base.MAX_E + 1):
        running = 0
        for t in range(13):
            if 0 < t <= 11:
                running += exact[mass][t - 1]
            out[mass][t] = running
    return out


def rejected_fast(exact: list[list[int]], support_lt: list[list[int]], *, e: int, required: int) -> int:
    total = 0
    for mass in range(e + 1):
        threshold = required - min(38, e - mass)
        if threshold <= 0:
            continue
        if threshold >= 12:
            total += sum(exact[mass])
        else:
            total += support_lt[mass][threshold]
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    args = ap.parse_args()

    manifest = base.load_canonical(args.manifest, base.EXPECTED_MANIFEST_CANONICAL)
    prefix = base.load_canonical(args.prefix_checkpoint, base.EXPECTED_PREFIX_CANONICAL)
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != base.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("indexed-terminal assignment-order regression")

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    exact = base.build_exceptional_exact_mass_support()
    support_lt = build_support_lt(exact)
    cumulative_exceptional = []
    running = 0
    for e in range(base.MAX_E + 1):
        running += sum(exact[e])
        cumulative_exceptional.append(running)

    total_before_node_mass = 0
    total_after_node_mass = 0
    n220_rejected = 0
    for row_id in rows:
        genus, degree = base.parse_row_id(row_id)
        legacy_emin = 8 if genus == 0 else 4
        emax = (19 * degree) // 5
        required = base.ceil_div(degree - 16 * genus + 16, 4)
        effective_emin = max(legacy_emin, required)
        for e in range(legacy_emin, emax + 1):
            normal_count = 19 * degree - 5 * e + 1
            stratum_total = normal_count * cumulative_exceptional[e]
            total_before_node_mass += stratum_total
            if e < effective_emin:
                continue
            total_after_node_mass += stratum_total
            n220_rejected += normal_count * rejected_fast(
                exact, support_lt, e=e, required=required
            )

    total_after_n220 = total_after_node_mass - n220_rejected
    observed = {
        "total_before_node_mass": total_before_node_mass,
        "total_after_node_mass": total_after_node_mass,
        "n220_rejected": n220_rejected,
        "total_after_n220": total_after_n220,
    }
    expected = {
        "total_before_node_mass": base.EXPECTED_TOTAL_BEFORE_NODE_MASS,
        "total_after_node_mass": base.EXPECTED_TOTAL_AFTER_NODE_MASS,
        "n220_rejected": base.EXPECTED_N220_REJECTED,
        "total_after_n220": base.EXPECTED_TOTAL_AFTER_N220,
    }
    if observed != expected:
        raise ValueError(f"N220 fast symbolic-count regression: {observed} != {expected}")

    print(json.dumps({
        "verdict": "PASS_N220_EXACT_SYMBOLIC_FULL178_COUNT_FAST_REPLAY",
        "rejection_fraction_numerator": n220_rejected,
        "rejection_fraction_denominator": total_after_node_mass,
        "rejection_percent_approx": 100.0 * n220_rejected / total_after_node_mass,
        **observed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
