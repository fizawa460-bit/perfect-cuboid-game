#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
N220 = HERE.parent / "N220"
sys.path.insert(0, str(N220))

import verify_n220_exact_symbolic_count as base
import verify_n220_exact_symbolic_count_fast as fast

ROOT = HERE.parents[4]
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
PREFIX = ROOT / "stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json"

EXPECTED_STRATA = 60491
EXPECTED_POST_NODE_MASS = 688101306357436883335845534
EXPECTED_POST_N220 = 346053707902916587089896969
EXPECTED_ROW_STREAM_SHA256 = "10380cb8ce2e03827cb563a8ad79b052b6254905317a4955d2be74f0a5a03a60"
EXPECTED_SURVIVOR_EXCEPTIONAL_BLOCKS_SUM = 1318904498253281860795425
EXPECTED_BUCKETS = {
    "le_1": 4,
    "le_10": 12,
    "le_100": 36,
    "le_1000": 230,
    "le_10000": 581,
    "le_100000": 1116,
    "le_1000000": 1680,
}
EXPECTED_MINIMA = [
    ("g0-d174", 48, 1),
    ("g0-d176", 48, 1),
    ("g1-d190", 48, 1),
    ("g1-d192", 48, 1),
]


def main() -> None:
    manifest = base.load_canonical(MANIFEST, base.EXPECTED_MANIFEST_CANONICAL)
    prefix = base.load_canonical(PREFIX, base.EXPECTED_PREFIX_CANONICAL)
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != base.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("indexed-terminal assignment-order regression")

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    exact = base.build_exceptional_exact_mass_support()
    support_lt = fast.build_support_lt(exact)
    cumulative_exceptional: list[int] = []
    running = 0
    for e in range(base.MAX_E + 1):
        running += sum(exact[e])
        cumulative_exceptional.append(running)

    records = []
    total_post_node_mass = 0
    total_post_n220 = 0
    survivor_exceptional_sum = 0

    for row_id in rows:
        genus, degree = base.parse_row_id(row_id)
        legacy_emin = 8 if genus == 0 else 4
        required = base.ceil_div(degree - 16 * genus + 16, 4)
        effective_emin = max(legacy_emin, required)
        emax = (19 * degree) // 5
        for e in range(effective_emin, emax + 1):
            old_exceptional = cumulative_exceptional[e]
            rejected_exceptional = fast.rejected_fast(exact, support_lt, e=e, required=required)
            survivor_exceptional = old_exceptional - rejected_exceptional
            if survivor_exceptional <= 0:
                raise ValueError("unexpected zero-survivor post-node-mass stratum")
            normal_block = 19 * degree - 5 * e + 1
            old_terminal = old_exceptional * normal_block
            survivor_terminal = survivor_exceptional * normal_block
            total_post_node_mass += old_terminal
            total_post_n220 += survivor_terminal
            survivor_exceptional_sum += survivor_exceptional
            records.append({
                "row_id": row_id,
                "g": genus,
                "d": degree,
                "e": e,
                "K": required,
                "normal_block": normal_block,
                "old_exceptional_blocks": old_exceptional,
                "survivor_exceptional_blocks": survivor_exceptional,
            })

    if len(records) != EXPECTED_STRATA:
        raise ValueError("post-node-mass stratum count regression")
    if total_post_node_mass != EXPECTED_POST_NODE_MASS or total_post_n220 != EXPECTED_POST_N220:
        raise ValueError("terminal-total regression")
    if survivor_exceptional_sum != EXPECTED_SURVIVOR_EXCEPTIONAL_BLOCKS_SUM:
        raise ValueError("survivor exceptional-block sum regression")

    canonical_records = sorted(records, key=lambda r: (r["g"], r["d"], r["e"]))
    stream = hashlib.sha256()
    for rec in canonical_records:
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    if stream.hexdigest() != EXPECTED_ROW_STREAM_SHA256:
        raise ValueError("per-stratum census stream regression")

    buckets = {}
    for threshold in (1, 10, 100, 1000, 10000, 100000, 1000000):
        buckets[f"le_{threshold}"] = sum(1 for r in records if r["survivor_exceptional_blocks"] <= threshold)
    if buckets != EXPECTED_BUCKETS:
        raise ValueError(f"bucket regression: {buckets}")

    minima = sorted(records, key=lambda r: (r["survivor_exceptional_blocks"], r["row_id"], r["e"]))[:4]
    got_minima = [(r["row_id"], r["e"], r["survivor_exceptional_blocks"]) for r in minima]
    if got_minima != EXPECTED_MINIMA:
        raise ValueError(f"minimum-block strata regression: {got_minima}")

    print(json.dumps({
        "verdict": "PASS_N250_POST_N220_EXACT_BLOCK_CENSUS",
        "post_node_mass_strata": len(records),
        "post_node_mass_terminal_total": total_post_node_mass,
        "post_n220_terminal_total": total_post_n220,
        "survivor_exceptional_blocks_sum": survivor_exceptional_sum,
        "per_stratum_stream_sha256": stream.hexdigest(),
        "small_block_strata": buckets,
        "minimum_survivor_block_strata": minima,
        "interpretation": "priority census only; no new pruning credit and no Picard leaf credit",
        "full178_complete": False,
        "heavy_compute": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
