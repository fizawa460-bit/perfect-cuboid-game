#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
EXISTENTIAL = HERE / "verify_fibration_nef_picard_existential_preflight.py"
INDEXER = RES / "compressed_terminal_indexer.py"
FAMILY = RES / "compressed_terminal_family.py"
CHECKPOINT = RES / "full178-prefix-indexed-compression-main-checkpoint.json"

SOURCE_LOCKS = {
    "picard_existential_carrier": (EXISTENTIAL, "d04213380ffa3c656a17c1423b68200599f0e5c8"),
    "compressed_terminal_indexer": (INDEXER, "4fb0a8dd34909494bd62646373e42877ed7a3c9e"),
    "compressed_terminal_family": (FAMILY, "90ff82ed312dcc0cb32cf207935945f550e29170"),
    "prefix_indexed_checkpoint": (CHECKPOINT, "eb823cc2f99d74456d5701b4673f848f18ba3151"),
}

PRODUCTION_G = 1
PRODUCTION_D = 192
PRODUCTION_E = 663
EXPECTED_TERMINAL_COUNT = 410107396030458090802608


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def lock_sources_before_import() -> None:
    for name, (path, expected) in SOURCE_LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def deterministic_ranks(total: int, panel_size: int) -> list[int]:
    total = int(total)
    panel_size = int(panel_size)
    req(total > 0, "empty production stratum")
    req(panel_size >= 2, "panel size must be >= 2")
    if total <= panel_size:
        return list(range(total))
    ranks = {0, total - 1}
    denominator = panel_size - 1
    for i in range(1, panel_size - 1):
        ranks.add((i * (total - 1)) // denominator)
    return sorted(ranks)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Exact existence-only production panel for retained fibration/Picard residual feasibility"
    )
    parser.add_argument("--panel-size", type=int, default=9)
    args = parser.parse_args()

    lock_sources_before_import()
    sys.path.insert(0, str(RES))
    from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402

    existential = load_module(EXISTENTIAL, "stage32_178_direct_picard_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(
        existential.PREFIX, "stage32_178_direct_picard_existential_prefix"
    )
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_direct_picard_existential_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_direct_picard_existential_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(
        bnb.RECOVERABILITY, "stage32_178_direct_picard_existential_recoverability"
    )
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    checkpoint = json.loads(CHECKPOINT.read_text())
    max_stratum = checkpoint["symbolic_full178_prefix_census"]["max_single_stratum"]
    req(max_stratum["row_id"] == "g1-d192", "production max-stratum row drift")
    req(int(max_stratum["e"]) == PRODUCTION_E, "production max-stratum e drift")
    req(int(max_stratum["terminal_count"]) == EXPECTED_TERMINAL_COUNT,
        "production max-stratum terminal-count drift")

    indexer = CompressedTerminalIndexer(e=PRODUCTION_E, d=PRODUCTION_D)
    req(indexer.terminal_count == EXPECTED_TERMINAL_COUNT,
        "indexer/checkpoint terminal-count mismatch")
    ranks = deterministic_ranks(indexer.terminal_count, args.panel_size)

    rows = []
    baseline_exists_count = 0
    picard_exists_count = 0
    strict_terminal_rejections = 0
    aggregate_baseline_nodes = 0
    aggregate_picard_nodes = 0
    aggregate_prefix_prunes = 0

    for rank in ranks:
        x = indexer.unrank(rank)
        req(indexer.rank(x) == rank, f"rank/unrank regression at rank {rank}")
        problem = bnb.residual_problem(
            kernel, g=PRODUCTION_G, d=PRODUCTION_D, e=PRODUCTION_E, x=x
        )
        one_count, baseline_first, baseline_stats = bnb.bnb_count(
            kernel, problem, stop_after_one=True
        )
        baseline_exists = one_count > 0
        picard_exists, picard_first, picard_stats = existential.picard_exists(
            prefix, leaf, bnb, kernel, problem, cert,
            x=x, e=PRODUCTION_E, d=PRODUCTION_D,
        )
        req(not picard_exists or baseline_exists,
            f"Picard existential oracle enlarged feasible set at rank {rank}")

        baseline_exists_count += int(baseline_exists)
        picard_exists_count += int(picard_exists)
        strict_terminal_rejections += int(baseline_exists and not picard_exists)
        aggregate_baseline_nodes += baseline_stats.visited_nodes
        aggregate_picard_nodes += picard_stats.visited_nodes
        aggregate_prefix_prunes += picard_stats.lattice_prefix_prunes

        rows.append({
            "rank": str(rank),
            "x": list(x),
            "structurally_infeasible": bool(problem.get("structurally_infeasible")),
            "structural_reason": problem.get("reason"),
            "baseline_exists": baseline_exists,
            "picard_exists": picard_exists,
            "strict_picard_terminal_rejection": baseline_exists and not picard_exists,
            "baseline_first_witness": list(baseline_first) if baseline_first is not None else None,
            "picard_first_witness": list(picard_first) if picard_first is not None else None,
            "baseline_visited_nodes": baseline_stats.visited_nodes,
            "picard_visited_nodes": picard_stats.visited_nodes,
            "picard_prefix_prunes": picard_stats.lattice_prefix_prunes,
            "picard_leaf_prunes": picard_stats.lattice_leaf_prunes,
        })

    out = {
        "schema": "STAGE32_32_01_178_DIRECT_NUMERICAL_PICARD_EXISTENCE_PANEL_V1",
        "purpose": "measure exact terminal-level elimination and search-tree effect using existence-only residual consumers on a deterministic panel of the largest real production stratum",
        "production_stratum": {
            "g": PRODUCTION_G,
            "d": PRODUCTION_D,
            "e": PRODUCTION_E,
            "row_id": "g1-d192",
            "terminal_count": str(indexer.terminal_count),
        },
        "panel": {
            "selection": "ENDPOINTS_PLUS_EXACT_INTEGER_QUANTILES",
            "requested_panel_size": args.panel_size,
            "realized_panel_size": len(ranks),
            "ranks": [str(r) for r in ranks],
            "rows": rows,
        },
        "aggregate_panel_measurement": {
            "baseline_exists_terminals": baseline_exists_count,
            "picard_exists_terminals": picard_exists_count,
            "strict_picard_terminal_rejections": strict_terminal_rejections,
            "strict_picard_terminal_rejection_observed": strict_terminal_rejections > 0,
            "baseline_visited_nodes": aggregate_baseline_nodes,
            "picard_visited_nodes": aggregate_picard_nodes,
            "exact_picard_prefix_prunes": aggregate_prefix_prunes,
            "picard_node_ratio_num": aggregate_picard_nodes,
            "picard_node_ratio_den": aggregate_baseline_nodes,
        },
        "semantics": {
            "real_production_terminal_family": True,
            "production_terminal_rank_unrank_exact": True,
            "baseline_existence_exact": True,
            "picard_existence_exact": True,
            "count_all_not_used": True,
            "bounded_deterministic_panel_only": True,
            "full_stratum_census_claimed": False,
            "full178_census_claimed": False,
            "main_credit_changed": False,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
        },
        "next_exact_step": "aggregate exact terminal multiplicities by the compact signature (a,b,c,t,x4,qexc,e,d,g); then replace per-terminal residual search by a qexc threshold derived from the minimum residual penalty",
        "merge": False,
    }
    print("PICARD_EXISTENCE_PANEL_SUMMARY=" + json.dumps({
        "panel_size": len(ranks),
        "baseline_exists": baseline_exists_count,
        "picard_exists": picard_exists_count,
        "strict_terminal_rejections": strict_terminal_rejections,
        "baseline_nodes": aggregate_baseline_nodes,
        "picard_nodes": aggregate_picard_nodes,
        "prefix_prunes": aggregate_prefix_prunes,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
