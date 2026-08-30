#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import pathlib
import statistics
from decimal import Decimal, getcontext

LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
NORMAL_LABEL_MAX = 92
NODE_LIMIT_GEN37 = 64_000_000
NODE_LIMIT_GEN38 = 256_000_000
FULL178_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_RESIDUAL_VOLUME_DIAGNOSTIC_V1"

getcontext().prec = 80


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-")
    return int(g[1:]), int(d[1:])


def budget_remaining(prefix: list[int], *, e: int, d: int) -> tuple[int, int]:
    ex = 0
    normal = 0
    for label, value in zip(LABELS, prefix):
        if label > NORMAL_LABEL_MAX:
            ex += int(value)
        else:
            normal += int(value)
    er = e - ex
    nr = 19 * d - 5 * e - normal
    assert er >= 0 and nr >= 0
    return er, nr


def future_raw_nodes(depth: int, exceptional_remaining: int, normal_remaining: int) -> int:
    """Exact node count of the budget-only DFS subtree below a prefix.

    This deliberately ignores membership and automorphism pruning. Therefore it is
    an exact finite envelope for the real Stage32 DFS, whose actual node visits can
    only be smaller.
    """
    if depth >= len(LABELS):
        return 0
    if depth <= 4:
        # Before (or at) the unique normal label at depth 4 there are p exceptional
        # variables before that normal coordinate, followed by six exceptional ones.
        p = 4 - depth
        q = 6
        pre = sum(math.comb(exceptional_remaining + k, k) for k in range(1, p + 1))
        post = (normal_remaining + 1) * sum(
            math.comb(exceptional_remaining + r, r) for r in range(p, p + q + 1)
        )
        return pre + post
    # The normal coordinate has already been chosen. Every remaining label is exceptional.
    q = len(LABELS) - depth
    return sum(math.comb(exceptional_remaining + k, k) for k in range(1, q + 1))


def full_stratum_raw_nodes(e: int, d: int) -> int:
    normal_budget = 19 * d - 5 * e
    assert e >= 0 and normal_budget >= 0
    return future_raw_nodes(0, e, normal_budget)


def range_raw_nodes(prefix: list[int], lo: int, hi: int, *, e: int, d: int) -> int:
    depth = len(prefix)
    if lo > hi:
        return 0
    er, nr = budget_remaining(prefix, e=e, d=d)
    out = 0
    label = LABELS[depth]
    for value in range(int(lo), int(hi) + 1):
        if label > NORMAL_LABEL_MAX:
            if value > er:
                break
            er2, nr2 = er - value, nr
        else:
            if value > nr:
                break
            er2, nr2 = er, nr - value
        out += 1 + future_raw_nodes(depth + 1, er2, nr2)
    return out


def cursor_current_raw_remaining(unit: dict) -> int:
    genus, d = parse_row_id(unit["row_id"])
    _ = genus
    e = int(unit["e_current"])
    source = unit["source_unit"]
    continuation = unit.get("continuation")
    if continuation is None:
        if source["kind"] == "STRATUM_PARTITION":
            prefix = [int(v) for v in source.get("prefix", [])]
            lo = int(source["next_min"])
            hi = int(source["next_max"])
        else:
            prefix = []
            lo = 0
            hi = e
        return range_raw_nodes(prefix, lo, hi, e=e, d=d)

    values = [int(v) for v in continuation["values"]]
    stack = continuation["stack"]
    total = 0
    for frame in stack:
        depth = int(frame["depth"])
        prefix = values[:depth]
        total += range_raw_nodes(
            prefix,
            int(frame["next_value"]),
            int(frame["hi"]),
            e=e,
            d=d,
        )
    return total


def cursor_raw_envelope(unit: dict) -> int:
    _, d = parse_row_id(unit["row_id"])
    e = int(unit["e_current"])
    current = cursor_current_raw_remaining(unit)
    source = unit["source_unit"]
    if source["kind"] != "ROW_TAIL":
        return current
    emax = (19 * d) // 5
    later = sum(full_stratum_raw_nodes(x, d) for x in range(e + 1, emax + 1))
    return current + later


def lineage(unit: dict) -> str:
    assert unit["kind"] == "RESUMABLE_CURSOR"
    return unit["source_unit"]["work_unit_id"]


def load_frontier(path: pathlib.Path, expected_sha: str) -> dict:
    m = json.loads(path.read_text())
    claimed = m.pop("canonical_sha256_without_this_field")
    assert csha(m) == claimed == expected_sha
    m["canonical_sha256_without_this_field"] = claimed
    return m


def find_single_json(path: pathlib.Path) -> pathlib.Path:
    files = sorted(path.rglob("*.json"))
    if len(files) != 1:
        raise RuntimeError(f"expected one JSON under {path}, got {files}")
    return files[0]


def q(vals: list[int], p: float) -> int | None:
    if not vals:
        return None
    xs = sorted(vals)
    idx = min(len(xs) - 1, max(0, math.ceil(p * len(xs)) - 1))
    return xs[idx]


def int_summary(vals: list[int]) -> dict:
    if not vals:
        return {"count": 0}
    xs = sorted(vals)
    return {
        "count": len(xs),
        "min": str(xs[0]),
        "p25": str(q(xs, 0.25)),
        "median": str(q(xs, 0.50)),
        "p75": str(q(xs, 0.75)),
        "max": str(xs[-1]),
    }


def log10_int(v: int) -> float | None:
    if v <= 0:
        return None
    return math.log10(v)


def ratio_float(a: int, b: int) -> float | None:
    if b == 0:
        return None
    return float(Decimal(a) / Decimal(b))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--full178-manifest", type=pathlib.Path, required=True)
    ap.add_argument("--gen36-dir", type=pathlib.Path, required=True)
    ap.add_argument("--gen37-dir", type=pathlib.Path, required=True)
    ap.add_argument("--gen38-dir", type=pathlib.Path, required=True)
    ap.add_argument("--gen36-sha", required=True)
    ap.add_argument("--gen37-sha", required=True)
    ap.add_argument("--gen38-sha", required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    fm = json.loads(args.full178_manifest.read_text())
    fm_claimed = fm.pop("canonical_sha256_without_this_field")
    assert csha(fm) == fm_claimed == FULL178_MANIFEST_SHA256
    all_rows: list[str] = []
    for ids in fm["m_class_rows"].values():
        all_rows.extend(ids)
    assert len(all_rows) == 178 and len(set(all_rows)) == 178

    exact_strata = 0
    full_campaign_raw_upper = 0
    max_degree = 0
    max_emax = 0
    for row_id in all_rows:
        genus, d = parse_row_id(row_id)
        emin = 8 if genus == 0 else 4
        emax = (19 * d) // 5
        max_degree = max(max_degree, d)
        max_emax = max(max_emax, emax)
        exact_strata += emax - emin + 1
        full_campaign_raw_upper += sum(full_stratum_raw_nodes(e, d) for e in range(emin, emax + 1))
    assert exact_strata == int(fm["coarse_strata_count"]) == 64111

    m36 = load_frontier(find_single_json(args.gen36_dir), args.gen36_sha)
    m37 = load_frontier(find_single_json(args.gen37_dir), args.gen37_sha)
    m38 = load_frontier(find_single_json(args.gen38_dir), args.gen38_sha)
    f36 = m36["frontier_exact_work_units"]
    f37 = m37["frontier_exact_work_units"]
    f38 = m38["frontier_exact_work_units"]
    assert len(f36) == 92 and len(f37) == 73 and len(f38) == 52

    b36 = {lineage(u): u for u in f36}
    b37 = {lineage(u): u for u in f37}
    b38 = {lineage(u): u for u in f38}
    assert len(b36) == 92 and len(b37) == 73 and len(b38) == 52
    assert set(b38) <= set(b37) <= set(b36)

    r36 = {k: cursor_raw_envelope(v) for k, v in b36.items()}
    r37 = {k: cursor_raw_envelope(v) for k, v in b37.items()}
    r38 = {k: cursor_raw_envelope(v) for k, v in b38.items()}

    line_records = []
    estimate_nodes: list[int] = []
    latest_compressions: list[float] = []
    prior_compressions: list[float] = []
    compression_change: list[float] = []
    source_counts = collections.Counter()
    row_groups: dict[str, list[dict]] = collections.defaultdict(list)

    for lid, u38 in sorted(b38.items()):
        u37 = b37[lid]
        u36 = b36[lid]
        assert u37["row_id"] == u38["row_id"] == u36["row_id"]
        assert int(u38["e_current"]) == int(u37["e_current"]), "Gen38 diagnostic already established same-e for all survivors"
        drop256 = r37[lid] - r38[lid]
        drop64 = r36[lid] - r37[lid]
        assert drop256 >= NODE_LIMIT_GEN38, (lid, drop256)
        assert drop64 >= NODE_LIMIT_GEN37, (lid, drop64)
        c256 = Decimal(drop256) / Decimal(NODE_LIMIT_GEN38)
        c64 = Decimal(drop64) / Decimal(NODE_LIMIT_GEN37)
        est = (r38[lid] * NODE_LIMIT_GEN38 + drop256 - 1) // drop256
        estimate_nodes.append(est)
        latest_compressions.append(float(c256))
        prior_compressions.append(float(c64))
        compression_change.append(float(c256 / c64))

        genus, d = parse_row_id(u38["row_id"])
        e = int(u38["e_current"])
        emin = 8 if genus == 0 else 4
        emax = (19 * d) // 5
        source_kind = u38["source_unit"]["kind"]
        source_counts[source_kind] += 1
        later_e_count = emax - e if source_kind == "ROW_TAIL" else 0
        raw_current_full = full_stratum_raw_nodes(e, d)
        raw_next_full = full_stratum_raw_nodes(e + 1, d) if e < emax else 0
        rec = {
            "lineage_id": lid,
            "row_id": u38["row_id"],
            "source_kind": source_kind,
            "degree": d,
            "emin": emin,
            "e_current": e,
            "emax": emax,
            "later_e_count_owned_by_this_source": later_e_count,
            "nodes_accumulated_current_partition": int(u38["nodes_accumulated"]),
            "raw_remaining_envelope_gen36": str(r36[lid]),
            "raw_remaining_envelope_gen37": str(r37[lid]),
            "raw_remaining_envelope_gen38": str(r38[lid]),
            "raw_envelope_drop_over_gen37_64m": str(drop64),
            "raw_envelope_drop_over_gen38_256m": str(drop256),
            "raw_envelope_nodes_removed_per_actual_node_gen37": float(c64),
            "raw_envelope_nodes_removed_per_actual_node_gen38": float(c256),
            "compression_ratio_gen38_over_gen37": float(c256 / c64),
            "local_linear_estimated_actual_nodes_remaining": str(est),
            "local_linear_estimated_256m_chunks_remaining": ratio_float(est, NODE_LIMIT_GEN38),
            "full_raw_current_stratum_nodes": str(raw_current_full),
            "full_raw_next_stratum_nodes": str(raw_next_full) if raw_next_full else None,
            "full_raw_next_over_current": ratio_float(raw_next_full, raw_current_full) if raw_next_full else None,
        }
        line_records.append(rec)
        row_groups[u38["row_id"]].append(rec)

    total_raw_remaining = sum(r38.values())
    total_estimated_remaining = sum(estimate_nodes)
    total_est_chunks = (total_estimated_remaining + NODE_LIMIT_GEN38 - 1) // NODE_LIMIT_GEN38
    ideal_17_runner_waves = (total_est_chunks + 16) // 17

    row_records = []
    for row_id, recs in sorted(row_groups.items()):
        genus, d = parse_row_id(row_id)
        emin = 8 if genus == 0 else 4
        emax = (19 * d) // 5
        curve = [(e, full_stratum_raw_nodes(e, d)) for e in range(emin, emax + 1)]
        peak_e, peak_nodes = max(curve, key=lambda x: x[1])
        row_tail_recs = [r for r in recs if r["source_kind"] == "ROW_TAIL"]
        current_es = [int(r["e_current"]) for r in recs]
        next_ratios = [r["full_raw_next_over_current"] for r in recs if r["full_raw_next_over_current"] is not None]
        row_records.append({
            "row_id": row_id,
            "degree": d,
            "frontier_units": len(recs),
            "row_tail_units": len(row_tail_recs),
            "stratum_partition_units": len(recs) - len(row_tail_recs),
            "current_e_min": min(current_es),
            "current_e_median": statistics.median(current_es),
            "current_e_max": max(current_es),
            "emax": emax,
            "raw_curve_peak_e": peak_e,
            "raw_curve_peak_nodes": str(peak_nodes),
            "raw_curve_peak_log10": log10_int(peak_nodes),
            "all_current_e_before_or_at_raw_peak": all(e <= peak_e for e in current_es),
            "row_tail_later_e_counts": [int(r["later_e_count_owned_by_this_source"]) for r in row_tail_recs],
            "median_raw_next_over_current": statistics.median(next_ratios) if next_ratios else None,
            "raw_remaining_envelope_total": str(sum(int(r["raw_remaining_envelope_gen38"]) for r in recs)),
            "local_linear_estimated_actual_nodes_remaining_total": str(sum(int(r["local_linear_estimated_actual_nodes_remaining"]) for r in recs)),
        })

    raw_tail_before_peak = sum(
        1
        for r in line_records
        if r["source_kind"] == "ROW_TAIL"
        and int(r["e_current"]) <= next(x["raw_curve_peak_e"] for x in row_records if x["row_id"] == r["row_id"])
    )
    row_tail_total = source_counts["ROW_TAIL"]

    summary = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "purpose": "MEASURE_FINITE_SEARCH_ENVELOPE_AND_RESIDUAL_SCALE_BEFORE_MORE_HEAVY_COMPUTE",
        "finite_search_certificate": {
            "outer_e_bound": "emin <= e <= floor(19*degree/5)",
            "label_count": len(LABELS),
            "exceptional_label_count": sum(1 for x in LABELS if x > NORMAL_LABEL_MAX),
            "normal_label_count": sum(1 for x in LABELS if x <= NORMAL_LABEL_MAX),
            "full178_row_count": len(all_rows),
            "full178_exact_coarse_e_strata": exact_strata,
            "maximum_degree": max_degree,
            "maximum_emax": max_emax,
            "raw_budget_only_full_campaign_node_upper_bound": str(full_campaign_raw_upper),
            "raw_budget_only_full_campaign_node_upper_bound_log10": log10_int(full_campaign_raw_upper),
            "interpretation": "The Stage32 prefix search is finite. Removing membership/canonical pruning gives an exact combinatorial supertree; the real DFS can visit no more nodes than this finite supertree.",
        },
        "source_locks": {
            "gen36_manifest_sha256": args.gen36_sha,
            "gen37_manifest_sha256": args.gen37_sha,
            "gen38_manifest_sha256": args.gen38_sha,
            "gen36_frontier_count": len(f36),
            "gen37_frontier_count": len(f37),
            "gen38_frontier_count": len(f38),
        },
        "current_exact_frontier": {
            "count": len(f38),
            "unique_rows": len(row_groups),
            "source_kind_counts": dict(sorted(source_counts.items())),
            "row_tail_sources_before_or_at_budget_only_raw_peak": raw_tail_before_peak,
            "row_tail_source_count": row_tail_total,
            "total_later_e_strata_owned_by_row_tail_sources": sum(int(r["later_e_count_owned_by_this_source"]) for r in line_records),
            "exact_finite_raw_remaining_node_upper_bound": str(total_raw_remaining),
            "exact_finite_raw_remaining_node_upper_bound_log10": log10_int(total_raw_remaining),
            "raw_remaining_fraction_of_full_campaign_upper_envelope": ratio_float(total_raw_remaining, full_campaign_raw_upper),
        },
        "observed_envelope_consumption": {
            "definition": "raw-envelope drop divided by actual DFS nodes spent; values >1 measure subtrees skipped by exact pruning",
            "gen37_64m_compression": {
                "min": min(prior_compressions),
                "median": statistics.median(prior_compressions),
                "max": max(prior_compressions),
            },
            "gen38_256m_compression": {
                "min": min(latest_compressions),
                "median": statistics.median(latest_compressions),
                "max": max(latest_compressions),
            },
            "gen38_over_gen37_compression_ratio": {
                "min": min(compression_change),
                "median": statistics.median(compression_change),
                "max": max(compression_change),
                "below_1_count": sum(1 for x in compression_change if x < 1.0),
                "above_or_equal_1_count": sum(1 for x in compression_change if x >= 1.0),
            },
        },
        "local_linear_residual_model": {
            "model": "For each surviving lineage, assume its latest Gen38 raw-envelope-removal per actual node remains constant over its remaining exact domain. This is an extrapolation, not a proof or rigorous runtime bound.",
            "per_lineage_estimated_actual_nodes": int_summary(estimate_nodes),
            "total_estimated_actual_nodes_remaining": str(total_estimated_remaining),
            "total_estimated_256m_equivalent_chunks": str(total_est_chunks),
            "idealized_17_runner_256m_waves": str(ideal_17_runner_waves),
            "warning": "Later e strata can have different pruning density; use the raw growth curve and compression trend to judge whether this model is optimistic or pessimistic.",
        },
        "rows": row_records,
        "lineages": line_records,
        "firewalls": {
            "diagnostic_only": True,
            "unknown_is_unsat": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    summary["canonical_sha256_without_this_field"] = csha(summary)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    print(json.dumps({
        "verdict": "PASS_EXACT_FINITE_RESIDUAL_VOLUME_DIAGNOSTIC",
        "full178_exact_strata": exact_strata,
        "maximum_emax": max_emax,
        "frontier": len(f38),
        "source_kind_counts": dict(sorted(source_counts.items())),
        "later_e_strata": summary["current_exact_frontier"]["total_later_e_strata_owned_by_row_tail_sources"],
        "raw_remaining_upper_log10": summary["current_exact_frontier"]["exact_finite_raw_remaining_node_upper_bound_log10"],
        "compression64_median": summary["observed_envelope_consumption"]["gen37_64m_compression"]["median"],
        "compression256_median": summary["observed_envelope_consumption"]["gen38_256m_compression"]["median"],
        "compression_change_below_1": summary["observed_envelope_consumption"]["gen38_over_gen37_compression_ratio"]["below_1_count"],
        "estimated_256m_chunks": str(total_est_chunks),
        "idealized_17_runner_waves": str(ideal_17_runner_waves),
        "sha256": summary["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
