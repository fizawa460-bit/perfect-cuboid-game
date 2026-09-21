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
RELAXED = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_static7_bounded_panel.py"
RELAXED_BLOB = "e44bec7ad9c0b7a4d8d7d87a455f181a681035c6"
CENSUS_RECEIPT = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-STATIC7-KEY-CENSUS-RECEIPT.json"
CENSUS_RECEIPT_CANON = "b975417fe28296a53f7877e9a02ce230a8852dfbc26fe29c428aeddff209719c"

DEGREE = 8
EXCEPTIONAL_MASS = 8
NORMAL_MASS = 112
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64
X4_VALUES = 113
SAMPLE_BASE4 = (
    (0, 1, 1, 1),
    (0, 4, 4, 8),
    (0, 6, 2, 6),
    (1, 2, 2, 2),
    (1, 3, 3, 3),
)
EXPECTED_MULTIPLICITY = {
    (0, 1, 1, 1): 4,
    (0, 4, 4, 8): 15,
    (0, 6, 2, 6): 50,
    (1, 2, 2, 2): 39,
    (1, 3, 3, 3): 93,
}


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
    ap.add_argument("--solver-timeout-ms", type=int, default=10000)
    ap.add_argument("--max-flat-cuts", type=int, default=32)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    req(args.solver_timeout_ms > 0, "solver timeout")
    req(args.max_flat_cuts > 0, "flat-cut bound")

    req(blob(RELAXED) == RELAXED_BLOB, "relaxed producer drift")
    census = load_canonical(CENSUS_RECEIPT, CENSUS_RECEIPT_CANON)
    req(census["result"]["base4_key_count"] == 343, "census base4 count drift")
    req(census["result"]["static7_key_count"] == 38759, "census static7 count drift")

    old = load_module(RELAXED, "stage32_main_btva_base4_relaxed")
    req(old.DEGREE == DEGREE and old.EXCEPTIONAL_MASS == EXCEPTIONAL_MASS,
        "target drift")
    req(old.BASE.is_file() and old.git_blob(old.BASE) == old.BASE_BLOB,
        "base Picard solver drift")
    req(old.NODE_BRIDGE.is_file() and old.git_blob(old.NODE_BRIDGE) == old.NODE_BRIDGE_BLOB,
        "node bridge drift")
    lane_agg = args.lane178_root / old.LANE178_AGG_REL
    req(lane_agg.is_file() and old.git_blob(lane_agg) == old.LANE178_AGG_BLOB,
        "lane178 source drift")

    v1 = old.load_module(old.BASE, "stage32_main_btva_base4_base")
    indexer = v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    req(indexer.normal_budget == NORMAL_MASS, "normal mass/indexer budget drift")
    req(indexer.normal_budget + 1 == X4_VALUES, "x4 count drift")

    # Exact sample multiplicities from exceptional states only.
    counts: Counter[tuple[int, int, int, int]] = Counter()
    stride = X4_VALUES
    for erank in range(int(indexer.exceptional_count)):
        x = tuple(int(v) for v in indexer.unrank(erank * stride))
        req(x[4] == 0, "x4 stride replay")
        key = tuple(old.static_from_terminal(x)[:4])
        if key in EXPECTED_MULTIPLICITY:
            counts[key] += 1
    req(dict(counts) == EXPECTED_MULTIPLICITY, "sample multiplicity replay drift")

    bundle = v1.load_retained(args.retained, "stage32_main_btva_base4_bundle")
    marking = v1.load_retained(args.marking, "stage32_main_btva_base4_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    req(P.shape == (140, PICARD_RANK), "pairing matrix shape")
    req(bridge.certificate.get("mass_identity_exact_on_picard64") is True,
        "mass identity source drift")

    node_bridge = json.loads(old.NODE_BRIDGE.read_text(encoding="utf-8"))
    nodes = old.node_matrix(node_bridge)
    req(nodes.shape == (48, 7) and int(nodes.rank()) == 7, "node ambient rank")

    panel = []
    for base4 in SAMPLE_BASE4:
        xvars = [Int(f"x_{len(panel)}_{j}") for j in range(PICARD_RANK)]
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

        # x4 is intentionally existential, but stays in the exact normal-pairing range.
        x4_expr = assignment_exprs[4]
        cuts = []
        seen = set()
        result_status = "UNKNOWN"
        compatible = None
        iterations = 0
        reason_unknown = None

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
                    "exceptional_pairings": ev,
                    "support_indices_0based": list(support),
                    "support_size": len(support),
                    "support_rank": rank,
                }
                break
            flat = old.closure(nodes, support)
            req(flat not in seen, "repeated flat")
            seen.add(flat)
            outside = [k for k in range(EXCEPTIONAL_COUNT) if k not in flat]
            req(outside, "improper flat")
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

        m = int(EXPECTED_MULTIPLICITY[base4])
        panel.append({
            "base4": list(base4),
            "exceptional_multiplicity_per_x4": m,
            "x4_values_covered_if_unsat": X4_VALUES,
            "terminal_mass_covered_if_unsat": m * X4_VALUES,
            "result": result_status,
            "solver_iterations": iterations,
            "lazy_flat_cuts": cuts,
            "compatible_support": compatible,
            "reason_unknown": reason_unknown,
        })

    unsat_rows = [x for x in panel if x["result"] == "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"]
    payload = {
        "schema": "STAGE32_MAIN_BTVA_BASE4_NORMALMASS_BOUNDED_PANEL_V1",
        "stage": 32,
        "route": "BTVA_COMPRESSED_PICARD_LIFT_RECEIVER_INTERSECTION",
        "status": "BOUNDED_BASE4_PANEL_COMPLETE_ZERO_CREDIT",
        "census_receipt_canonical_sha256": CENSUS_RECEIPT_CANON,
        "target": {
            "row_id": "g0-d008",
            "degree": DEGREE,
            "exceptional_mass": EXCEPTIONAL_MASS,
            "normal_mass": NORMAL_MASS,
            "base4_total_population": 343,
            "x4_values_per_base4": X4_VALUES,
            "static7_total_population": 38759,
            "terminal_total_population": 1278934,
        },
        "decision_problem": {
            "fixed_observables": ["a", "b", "c", "t", "e", "d"],
            "x4_existential": True,
            "residual_r0_to_r4_existential": True,
            "all140_pairings_nonnegative": True,
            "normal_pairing_sum": NORMAL_MASS,
            "exceptional_pairing_sum": EXCEPTIONAL_MASS,
            "btva_nonconic_p6_span_required": True,
        },
        "panel": panel,
        "summary": {
            "sample_base4_keys": len(panel),
            "unsat_base4_fibers": len(unsat_rows),
            "compatible_sat_base4_fibers": sum(1 for x in panel if x["result"] == "SAT_BTVA_COMPATIBLE_BASE4_LIFT"),
            "unknown_base4_fibers": sum(1 for x in panel if x["result"] == "UNKNOWN"),
            "static7_keys_covered_by_unsat_fibers": len(unsat_rows) * X4_VALUES,
            "terminal_mass_covered_by_unsat_fibers": sum(x["terminal_mass_covered_if_unsat"] for x in unsat_rows),
        },
        "firewalls": {
            "sample_only": True,
            "main_pruning_credit": False,
            "receiver_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
        "next_exact_step":
            "If base4 UNSAT is common, shard the 343 exact base4 keys and solve with x4 existential before any per-x4 fallback.",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_BASE4_NORMALMASS_SUMMARY=" + json.dumps(payload["summary"], sort_keys=True))
    print("BTVA_BASE4_NORMALMASS_CANONICAL=" + payload["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
