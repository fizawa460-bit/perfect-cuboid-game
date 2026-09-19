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
PREFIX = HERE / "verify_fibration_nef_picard_prefix_composition_preflight.py"
INDEXER = RES / "compressed_terminal_indexer.py"
FAMILY = RES / "compressed_terminal_family.py"
CHECKPOINT = RES / "full178-prefix-indexed-compression-main-checkpoint.json"

SOURCE_LOCKS = {
    "picard_prefix_carrier": (PREFIX, "7f0cfae30b2e081f9579d68bd4e80c1e57f94f6a"),
    "compressed_terminal_indexer": (INDEXER, "4fb0a8dd34909494bd62646373e42877ed7a3c9e"),
    "compressed_terminal_family": (FAMILY, "90ff82ed312dcc0cb32cf207935945f550e29170"),
    "prefix_indexed_checkpoint": (CHECKPOINT, "eb823cc2f99d74456d5701b4673f848f18ba3151"),
}

# Largest exact coarse-e stratum retained by the production checkpoint.
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
    """Deterministic spread across one exact indexed stratum.

    This is a bounded production panel, not a FULL178 census.  Endpoints are
    always included.  Interior ranks are exact integer quantiles, deduplicated.
    """
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
        description="Bounded exact production-stratum Picard-prefix composition panel"
    )
    parser.add_argument(
        "--panel-size",
        type=int,
        default=9,
        help="deterministic rank panel size (default: 9)",
    )
    args = parser.parse_args()

    # Fail closed before importing either the production indexer or the
    # Picard/fibration carrier.  The latter performs its own dependency locks
    # before executing load-bearing producer logic.
    lock_sources_before_import()

    sys.path.insert(0, str(RES))
    from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402

    prefix = load_module(PREFIX, "stage32_178_direct_picard_prefix_carrier")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_direct_picard_leaf_carrier")
    prefix.lock_leaf_and_dependencies(leaf)

    cert = leaf.load_picard_certificate()
    req(tuple(cert["observable_order"]) == prefix.OBSERVABLE_ORDER,
        "Picard observable order regression")
    bnb = leaf.load_module(leaf.BNB, "stage32_178_direct_picard_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_direct_picard_recoverability")
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
    aggregate_baseline = 0
    aggregate_picard = 0
    aggregate_visited_without_prefix = 0
    aggregate_visited_with_prefix = 0
    aggregate_prefix_prunes = 0

    for rank in ranks:
        x = indexer.unrank(rank)
        req(indexer.rank(x) == rank, f"rank/unrank regression at rank {rank}")
        problem = bnb.residual_problem(
            kernel, g=PRODUCTION_G, d=PRODUCTION_D, e=PRODUCTION_E, x=x
        )
        baseline_count, baseline_first, baseline_stats = bnb.bnb_count(kernel, problem)
        picard_count, picard_first, picard_stats = prefix.bnb_count_with_picard_prefix(
            leaf,
            bnb,
            kernel,
            problem,
            cert,
            x=x,
            e=PRODUCTION_E,
            d=PRODUCTION_D,
        )
        req(picard_count <= baseline_count,
            f"Picard composition enlarged feasible set at rank {rank}")

        aggregate_baseline += baseline_count
        aggregate_picard += picard_count
        aggregate_visited_without_prefix += baseline_stats.visited_nodes
        aggregate_visited_with_prefix += picard_stats.visited_nodes
        aggregate_prefix_prunes += picard_stats.lattice_prefix_prunes

        rows.append({
            "rank": str(rank),
            "x": list(x),
            "structurally_infeasible": bool(problem.get("structurally_infeasible")),
            "structural_reason": problem.get("reason"),
            "baseline_feasible_residual_vectors": baseline_count,
            "picard_feasible_residual_vectors": picard_count,
            "picard_rejected_residual_vectors": baseline_count - picard_count,
            "baseline_first_witness": list(baseline_first) if baseline_first is not None else None,
            "picard_first_witness": list(picard_first) if picard_first is not None else None,
            "baseline_visited_nodes": baseline_stats.visited_nodes,
            "picard_prefix_visited_nodes": picard_stats.visited_nodes,
            "picard_prefix_prunes": picard_stats.lattice_prefix_prunes,
            "picard_leaf_prunes": picard_stats.lattice_leaf_prunes,
        })

    out = {
        "schema": "STAGE32_32_01_178_DIRECT_NUMERICAL_PICARD_LEAF_COMPRESSION_PANEL_V1",
        "purpose": "connect the exact prefix-indexed production terminal family to the retained exact Picard-prefix residual oracle on a deterministic bounded panel of the largest real production stratum",
        "production_stratum": {
            "g": PRODUCTION_G,
            "d": PRODUCTION_D,
            "e": PRODUCTION_E,
            "row_id": "g1-d192",
            "terminal_count": str(indexer.terminal_count),
            "canonical_index_order": indexer.certificate()["canonical_index_order"],
        },
        "panel": {
            "selection": "ENDPOINTS_PLUS_EXACT_INTEGER_QUANTILES",
            "requested_panel_size": args.panel_size,
            "realized_panel_size": len(ranks),
            "ranks": [str(r) for r in ranks],
            "rows": rows,
        },
        "aggregate_panel_measurement": {
            "baseline_feasible_residual_vectors": aggregate_baseline,
            "picard_feasible_residual_vectors": aggregate_picard,
            "picard_rejected_residual_vectors": aggregate_baseline - aggregate_picard,
            "strict_picard_rejection_observed": aggregate_picard < aggregate_baseline,
            "baseline_visited_nodes": aggregate_visited_without_prefix,
            "picard_prefix_visited_nodes": aggregate_visited_with_prefix,
            "exact_picard_prefix_prunes": aggregate_prefix_prunes,
        },
        "semantics": {
            "real_production_terminal_family": True,
            "production_terminal_rank_unrank_exact": True,
            "picard_prefix_oracle_exact_for_each_measured_terminal": True,
            "bounded_deterministic_panel_only": True,
            "full_stratum_census_claimed": False,
            "full178_census_claimed": False,
            "main_credit_changed": False,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
        },
        "next_exact_step": "if strict rejection or prefix-node reduction is material on this real stratum panel, aggregate by compressed exceptional-family prefixes so exact family masses can be charged without materializing the 24-digit stratum",
        "merge": False,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
