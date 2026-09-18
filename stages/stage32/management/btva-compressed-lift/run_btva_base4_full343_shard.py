#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from z3 import Int, SolverFor, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[4]
PARENT = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_normalmass_bounded_panel.py"
PARENT_BLOB = "29114c0cd8a2c604d24b2a9ad3418fc2b5200171"
CENSUS_RECEIPT = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-STATIC7-KEY-CENSUS-RECEIPT.json"
CENSUS_RECEIPT_CANON = "b975417fe28296a53f7877e9a02ce230a8852dfbc26fe29c428aeddff209719c"

ROW_ID = "g0-d008"
DEGREE = 8
EXCEPTIONAL_MASS = 8
NORMAL_MASS = 112
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64
X4_VALUES = 113
EXPECTED_BASE4_KEYS = 343
EXPECTED_TERMINAL_MASS = 1278934


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    stored = obj.get("canonical_sha256_without_this_field")
    req(stored == expected, "census receipt stored canonical drift")
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    req(csha(body) == expected, "census receipt canonical drift")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--lane178-root", type=Path, required=True)
    ap.add_argument("--shard-index", type=int, required=True)
    ap.add_argument("--shard-count", type=int, default=8)
    ap.add_argument("--solver-timeout-ms", type=int, default=1500)
    ap.add_argument("--max-flat-cuts", type=int, default=16)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    req(args.shard_count == 8, "approved shard-count drift")
    req(0 <= args.shard_index < args.shard_count, "shard index")
    req(0 < args.solver_timeout_ms <= 5000, "solver timeout outside approved bounded range")
    req(0 < args.max_flat_cuts <= 32, "flat-cut bound outside approved range")

    req(blob(PARENT) == PARENT_BLOB, "base4 bounded parent drift")
    census = load_canonical(CENSUS_RECEIPT, CENSUS_RECEIPT_CANON)
    req(census["result"]["base4_key_count"] == EXPECTED_BASE4_KEYS, "base4 census count drift")
    req(census["result"]["reconstructed_terminal_mass"] == EXPECTED_TERMINAL_MASS,
        "terminal mass census drift")

    parent = load_module(PARENT, "stage32_main_btva_full343_parent")
    old = parent.load_module(parent.RELAXED, "stage32_main_btva_full343_relaxed")
    req(parent.DEGREE == DEGREE and parent.EXCEPTIONAL_MASS == EXCEPTIONAL_MASS,
        "parent target drift")
    req(parent.NORMAL_MASS == NORMAL_MASS, "parent normal mass drift")

    req(old.BASE.is_file() and old.git_blob(old.BASE) == old.BASE_BLOB,
        "base Picard solver drift")
    req(old.NODE_BRIDGE.is_file() and old.git_blob(old.NODE_BRIDGE) == old.NODE_BRIDGE_BLOB,
        "node bridge drift")
    lane_agg = args.lane178_root / old.LANE178_AGG_REL
    req(lane_agg.is_file() and old.git_blob(lane_agg) == old.LANE178_AGG_BLOB,
        "lane178 aggregate Picard source drift")

    v1 = old.load_module(old.BASE, "stage32_main_btva_full343_base")
    indexer = v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    req(indexer.normal_budget == NORMAL_MASS, "normal budget drift")
    req(int(indexer.terminal_count) == EXPECTED_TERMINAL_MASS, "terminal count drift")

    counts: Counter[tuple[int, int, int, int]] = Counter()
    representative_rank: dict[tuple[int, int, int, int], int] = {}
    stride = X4_VALUES
    for erank in range(int(indexer.exceptional_count)):
        x = tuple(int(v) for v in indexer.unrank(erank * stride))
        req(x[4] == 0, "x4 stride replay")
        key = tuple(old.static_from_terminal(x)[:4])
        counts[key] += 1
        representative_rank.setdefault(key, erank)

    keys = sorted(counts)
    req(len(keys) == EXPECTED_BASE4_KEYS, "base4 key population drift")
    req(sum(int(counts[k]) * X4_VALUES for k in keys) == EXPECTED_TERMINAL_MASS,
        "base4 terminal mass conservation")

    selected = [(i, key) for i, key in enumerate(keys) if i % args.shard_count == args.shard_index]
    expected_indices = list(range(args.shard_index, EXPECTED_BASE4_KEYS, args.shard_count))
    req([i for i, _ in selected] == expected_indices, "shard partition drift")

    bundle = v1.load_retained(args.retained, f"stage32_main_btva_full343_bundle_{args.shard_index}")
    marking = v1.load_retained(args.marking, f"stage32_main_btva_full343_marking_{args.shard_index}")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    req(P.shape == (140, PICARD_RANK), "pairing matrix shape")
    req(bridge.certificate.get("mass_identity_exact_on_picard64") is True,
        "Picard64 mass identity drift")

    node_bridge = json.loads(old.NODE_BRIDGE.read_text(encoding="utf-8"))
    nodes = old.node_matrix(node_bridge)
    req(nodes.shape == (48, 7) and int(nodes.rank()) == 7, "48-node ambient span drift")

    rows = []
    for global_index, base4 in selected:
        xvars = [Int(f"x_{args.shard_index}_{global_index}_{j}") for j in range(PICARD_RANK)]
        solver = SolverFor("QF_LIA")
        solver.set(timeout=args.solver_timeout_ms)

        pairings = [v1.linear_expr(P.row(i), xvars) for i in range(140)]
        normal = pairings[:NORMAL_COUNT]
        exceptional = pairings[NORMAL_COUNT:NORMAL_COUNT + EXCEPTIONAL_COUNT]
        for expr in normal:
            solver.add(expr >= 0, expr <= NORMAL_MASS)
        for expr in exceptional:
            solver.add(expr >= 0, expr <= EXCEPTIONAL_MASS)
        solver.add(v1.linear_expr(bridge.degree_functional, xvars) == DEGREE)
        solver.add(v1.linear_expr(bridge.exceptional_mass_functional, xvars) == EXCEPTIONAL_MASS)
        solver.add(sum(normal) == NORMAL_MASS)
        solver.add(sum(exceptional) == EXCEPTIONAL_MASS)

        assignment_exprs = [pairings[label - 1] for label in old.ASSIGNMENT]
        aggregate4 = [
            sum(int(old.L[i][j]) * assignment_exprs[j] for j in range(len(old.ASSIGNMENT)))
            for i in range(4)
        ]
        for expr, value in zip(aggregate4, base4):
            solver.add(expr == int(value))

        x4_expr = assignment_exprs[4]
        cuts = []
        seen = set()
        result_status = "UNKNOWN"
        compatible = None
        reason_unknown = None
        iterations = 0

        while iterations <= args.max_flat_cuts:
            iterations += 1
            result = solver.check()
            if result == unsat:
                result_status = "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"
                break
            if result == unknown:
                result_status = "UNKNOWN"
                reason_unknown = solver.reason_unknown()
                break
            req(result == sat, "unexpected solver status")
            model = solver.model()
            ev = [int(model.eval(expr, model_completion=True).as_long()) for expr in exceptional]
            x4 = int(model.eval(x4_expr, model_completion=True).as_long())
            req(0 <= x4 <= NORMAL_MASS, "x4 model range")
            support = tuple(i for i, value in enumerate(ev) if value > 0)
            rank = old.support_rank(nodes, support)
            if rank == 7:
                result_status = "SAT_BTVA_COMPATIBLE_BASE4_LIFT"
                compatible = {
                    "x4_witness": x4,
                    "exceptional_pairings_sha256": v1.csha(ev),
                    "support_indices_0based": list(support),
                    "support_size": len(support),
                    "support_rank": rank,
                }
                break

            flat = old.closure(nodes, support)
            req(flat not in seen, "repeated lazy flat")
            seen.add(flat)
            outside = [k for k in range(EXCEPTIONAL_COUNT) if k not in flat]
            req(outside, "improper lazy flat")
            solver.add(sum(exceptional[k] for k in outside) >= 1)
            cuts.append({
                "support_rank": rank,
                "support_size": len(support),
                "closure_size": len(flat),
                "outside_count": len(outside),
            })
        else:
            result_status = "UNKNOWN"
            reason_unknown = "max_flat_cuts_exhausted"

        multiplicity = int(counts[base4])
        rows.append({
            "global_base4_index": global_index,
            "base4": list(base4),
            "exceptional_multiplicity_per_x4": multiplicity,
            "representative_exceptional_rank": int(representative_rank[base4]),
            "result": result_status,
            "solver_iterations": iterations,
            "lazy_flat_cut_count": len(cuts),
            "reason_unknown": reason_unknown,
            "compatible_support": compatible,
            "static7_keys_covered_if_unsat": X4_VALUES,
            "terminal_mass_covered_if_unsat": multiplicity * X4_VALUES,
        })

    unsat = [r for r in rows if r["result"] == "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"]
    satrows = [r for r in rows if r["result"] == "SAT_BTVA_COMPATIBLE_BASE4_LIFT"]
    unknowns = [r for r in rows if r["result"] == "UNKNOWN"]

    payload = {
        "schema": "STAGE32_MAIN_BTVA_BASE4_FULL343_SHARD_V1",
        "stage": 32,
        "route": "BTVA_COMPRESSED_PICARD_LIFT_RECEIVER_INTERSECTION",
        "status": "EXACT_SHARD_COMPLETE_ZERO_CREDIT",
        "source_locks": {
            "parent_blob_sha1": PARENT_BLOB,
            "census_receipt_canonical_sha256": CENSUS_RECEIPT_CANON,
            "base_picard_solver_blob_sha1": old.BASE_BLOB,
            "node_bridge_blob_sha1": old.NODE_BRIDGE_BLOB,
            "lane178_head": old.LANE178_HEAD,
            "lane178_aggregate_picard_blob_sha1": old.LANE178_AGG_BLOB,
        },
        "execution": {
            "shard_index": args.shard_index,
            "shard_count": args.shard_count,
            "partition_rule": "sorted_base4_global_index_mod_shard_count",
            "expected_global_indices": expected_indices,
            "solver": "Z3_QF_LIA",
            "solver_timeout_ms": args.solver_timeout_ms,
            "max_flat_cuts": args.max_flat_cuts,
        },
        "target": {
            "row_id": ROW_ID,
            "degree": DEGREE,
            "exceptional_mass": EXCEPTIONAL_MASS,
            "normal_mass": NORMAL_MASS,
            "base4_total_population": EXPECTED_BASE4_KEYS,
            "x4_values_per_base4": X4_VALUES,
            "terminal_total_population": EXPECTED_TERMINAL_MASS,
        },
        "rows": rows,
        "summary": {
            "key_count": len(rows),
            "unsat_base4_fibers": len(unsat),
            "compatible_sat_base4_fibers": len(satrows),
            "unknown_base4_fibers": len(unknowns),
            "static7_keys_covered_by_unsat_fibers": len(unsat) * X4_VALUES,
            "terminal_mass_covered_by_unsat_fibers":
                sum(int(r["terminal_mass_covered_if_unsat"]) for r in unsat),
        },
        "firewalls": {
            "main_pruning_credit": False,
            "receiver_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_FULL343_SHARD_SUMMARY=" + json.dumps(payload["summary"], sort_keys=True))
    print("BTVA_FULL343_SHARD_CANONICAL=" + payload["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
