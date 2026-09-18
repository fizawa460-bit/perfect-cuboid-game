#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import sympy
from sympy import I, Matrix
from z3 import Int, SolverFor, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_to_picard64_completion.py"
BASE_BLOB = "6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633"
NODE_BRIDGE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-01b-runtime-node-coordinate-bridge.json"
NODE_BRIDGE_BLOB = "2a14a683e8ec38ec993eb711841c466f2be6eb06"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
MANIFEST_BLOB = "0a46b34e278688240656b4977e9cb7f589e90e06"
LANE178_AGG_REL = "stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_aggregate_picard_lattice_preflight.py"
LANE178_AGG_BLOB = "5fa9f1d67d6411cb550230b62398aff7bd6488ff"
LANE178_HEAD = "e60f03cf5105bc6e26cb4615acabd6fe0c07625c"

ROW_ID = "g0-d008"
GENUS = 0
DEGREE = 8
EXCEPTIONAL_MASS = 8
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64
ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)
L = (
    (0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0),
    (1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1),
    (1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
)
STATIC_ORDER = ("a", "b", "c", "t", "x4", "e", "d")


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
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


def parse_node_value(s: str):
    return sympy.sympify(str(s), locals={"i": I})


def node_matrix(bridge: dict) -> Matrix:
    rows = bridge["rows"]
    req(len(rows) == 48, "node bridge row count")
    req([int(r["runtime_index_0based"]) for r in rows] == list(range(48)),
        "node runtime indices")
    req([int(r["retained_exceptional_index_0based"]) for r in rows] == list(range(48)),
        "node exceptional indices")
    return Matrix([
        [parse_node_value(v) for v in row["canonical_stoll_coordinates"]]
        for row in rows
    ])


def support_rank(nodes: Matrix, support: tuple[int, ...]) -> int:
    if not support:
        return 0
    return int(nodes[list(support), :].rank())


def closure(nodes: Matrix, support: tuple[int, ...]) -> tuple[int, ...]:
    req(support, "empty support cannot define positive-mass closure")
    base = nodes[list(support), :]
    rank = int(base.rank())
    out = []
    for i in range(nodes.rows):
        if int(Matrix.vstack(base, nodes.row(i)).rank()) == rank:
            out.append(i)
    return tuple(out)


def panel_ranks(total: int) -> tuple[int, ...]:
    req(total > 0, "empty terminal family")
    return tuple(sorted({0, total // 4, total // 2, (3 * total) // 4, total - 1}))


def static_from_terminal(terminal: tuple[int, ...]) -> tuple[int, ...]:
    req(len(terminal) == len(ASSIGNMENT), "terminal width")
    vals = []
    for row in L:
        vals.append(sum(int(row[j]) * int(terminal[j]) for j in range(len(terminal))))
    return tuple(vals) + (EXCEPTIONAL_MASS, DEGREE)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--lane178-root", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=10000)
    ap.add_argument("--max-flat-cuts", type=int, default=64)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    req(args.solver_timeout_ms > 0, "solver timeout")
    req(args.max_flat_cuts > 0, "max flat cuts")

    # Lock every load-bearing local source before importing executable code.
    req(BASE.is_file() and git_blob(BASE) == BASE_BLOB, "base Picard solver drift")
    req(NODE_BRIDGE.is_file() and git_blob(NODE_BRIDGE) == NODE_BRIDGE_BLOB,
        "node bridge drift")
    req(MANIFEST.is_file() and git_blob(MANIFEST) == MANIFEST_BLOB, "manifest drift")
    lane_agg = args.lane178_root / LANE178_AGG_REL
    req(lane_agg.is_file() and git_blob(lane_agg) == LANE178_AGG_BLOB,
        "lane178 aggregate Picard source drift")

    agg_text = lane_agg.read_text(encoding="utf-8")
    req('AGGREGATE_ORDER = ("a", "b", "c", "t", "x4")' in agg_text,
        "lane178 aggregate order drift")
    req("ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)" in agg_text,
        "lane178 assignment drift")
    for literal in (
        "[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]",
        "[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]",
        "[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1]",
        "[1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]",
        "[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]",
    ):
        req(literal in agg_text, "lane178 aggregate matrix drift")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = set()
    for ids in manifest["m_class_rows"].values():
        rows.update(str(x) for x in ids)
    req(len(rows) == 178 and ROW_ID in rows, "g0-d008 absent from FULL178 manifest")

    v1 = load_module(BASE, "stage32_main_btva_static7_base")
    req(tuple(v1.EXPECTED_ASSIGNMENT_ORDER) == ASSIGNMENT, "base assignment order drift")
    indexer = v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    total = int(indexer.terminal_count)
    ranks = panel_ranks(total)

    bundle = v1.load_retained(args.retained, "stage32_main_btva_static7_bundle")
    marking = v1.load_retained(args.marking, "stage32_main_btva_static7_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    req(P.shape == (140, PICARD_RANK), "all140 pairing matrix shape")
    req(bridge.certificate.get("mass_identity_exact_on_picard64") is True,
        "Picard64 mass identity source drift")

    node_bridge = json.loads(NODE_BRIDGE.read_text(encoding="utf-8"))
    nodes = node_matrix(node_bridge)
    req(nodes.shape == (48, 7) and int(nodes.rank()) == 7, "48-node ambient span drift")

    terminal_rows = []
    unique_static: dict[tuple[int, ...], list[int]] = {}
    for rank in ranks:
        terminal = tuple(int(x) for x in indexer.unrank(rank))
        req(indexer.rank(terminal) == rank, "rank/unrank replay")
        static = static_from_terminal(terminal)
        unique_static.setdefault(static, []).append(rank)
        terminal_rows.append({
            "terminal_rank": rank,
            "terminal_pairings": list(terminal),
            "static7": list(static),
        })

    panel = []
    for static, source_ranks in sorted(unique_static.items()):
        xvars = [Int(f"x_{len(panel)}_{j}") for j in range(PICARD_RANK)]
        solver = SolverFor("QF_LIA")
        solver.set(timeout=args.solver_timeout_ms)

        pairings = [v1.linear_expr(P.row(i), xvars) for i in range(140)]
        exceptional = pairings[NORMAL_COUNT:NORMAL_COUNT + EXCEPTIONAL_COUNT]
        for expr in exceptional:
            solver.add(expr >= 0, expr <= EXCEPTIONAL_MASS)
        solver.add(sum(exceptional) == EXCEPTIONAL_MASS)
        solver.add(v1.linear_expr(bridge.degree_functional, xvars) == DEGREE)
        solver.add(v1.linear_expr(bridge.exceptional_mass_functional, xvars) == EXCEPTIONAL_MASS)

        assignment_exprs = [pairings[label - 1] for label in ASSIGNMENT]
        aggregate_exprs = [
            sum(int(L[i][j]) * assignment_exprs[j] for j in range(len(ASSIGNMENT)))
            for i in range(5)
        ]
        for expr, value in zip(aggregate_exprs, static[:5]):
            solver.add(expr == int(value))

        cuts = []
        seen_closures: set[tuple[int, ...]] = set()
        result_status = "UNKNOWN"
        compatible_support = None
        iterations = 0
        reason_unknown = None

        while iterations <= args.max_flat_cuts:
            iterations += 1
            result = solver.check()
            if result == unsat:
                result_status = "UNSAT_NONCONIC_BTVA_RELAXED_FIBER"
                break
            if result == unknown:
                result_status = "UNKNOWN"
                reason_unknown = solver.reason_unknown()
                break
            req(result == sat, "unexpected solver status")
            model = solver.model()
            ev = [int(model.eval(expr, model_completion=True).as_long()) for expr in exceptional]
            req(min(ev) >= 0 and sum(ev) == EXCEPTIONAL_MASS,
                "exceptional mass model replay")
            support = tuple(i for i, value in enumerate(ev) if value > 0)
            rank = support_rank(nodes, support)
            if rank == 7:
                result_status = "SAT_BTVA_COMPATIBLE_RELAXED_LIFT"
                compatible_support = {
                    "exceptional_pairings": ev,
                    "support_indices_0based": list(support),
                    "support_size": len(support),
                    "support_rank": rank,
                }
                break

            req(rank < 7, "support rank exceeded ambient rank")
            flat = closure(nodes, support)
            req(flat not in seen_closures, "lazy-flat separator repeated a forbidden closure")
            seen_closures.add(flat)
            outside = [k for k in range(EXCEPTIONAL_COUNT) if k not in flat]
            req(outside, "proper support closure has no outside node")
            solver.add(sum(exceptional[k] for k in outside) >= 1)
            cuts.append({
                "support_rank": rank,
                "support_size": len(support),
                "closure_size": len(flat),
                "closure_indices_0based": list(flat),
                "outside_count": len(outside),
            })
        else:
            result_status = "UNKNOWN"
            reason_unknown = "max_flat_cuts_exhausted"

        panel.append({
            "static7": list(static),
            "source_terminal_ranks": source_ranks,
            "result": result_status,
            "solver_iterations": iterations,
            "lazy_flat_cuts": cuts,
            "compatible_support": compatible_support,
            "reason_unknown": reason_unknown,
            "nonconic_btva_only": True,
            "known_32_plane_conics_not_excluded": True,
            "normal_all140_nonnegativity_imposed": False,
            "relaxation_semantics": "UNSAT is safe for the nonconic BTVA receiver; SAT/UNKNOWN carries no pruning credit",
        })

    out = {
        "schema": "STAGE32_MAIN_BTVA_STATIC7_BOUNDED_PANEL_V1",
        "stage": 32,
        "route": "BTVA_COMPRESSED_PICARD_LIFT_RECEIVER_INTERSECTION",
        "status": "BOUNDED_REAL_PRODUCTION_PANEL_COMPLETE_ZERO_CREDIT",
        "source_locks": {
            "base_picard_solver_blob_sha1": BASE_BLOB,
            "node_bridge_blob_sha1": NODE_BRIDGE_BLOB,
            "manifest_blob_sha1": MANIFEST_BLOB,
            "lane178_head": LANE178_HEAD,
            "lane178_aggregate_picard_blob_sha1": LANE178_AGG_BLOB,
        },
        "target": {
            "row_id": ROW_ID,
            "genus": GENUS,
            "degree": DEGREE,
            "exceptional_mass": EXCEPTIONAL_MASS,
            "static_order": list(STATIC_ORDER),
            "terminal_family_count": total,
            "sample_terminal_ranks": list(ranks),
            "sample_terminal_rows": terminal_rows,
            "unique_static_key_count": len(unique_static),
        },
        "decision_problem": {
            "picard_variables": PICARD_RANK,
            "static_observables_fixed": 7,
            "residual_observables_left_existential": 5,
            "exceptional_pairings_nonnegative": True,
            "exceptional_pairing_sum_fixed_to_e": True,
            "normal_all140_nonnegativity_imposed": False,
            "btva_condition": "nonconic genus-0 support must span P6; known 32 plane conics preserved separately",
            "lazy_flat_cut": "for a realized proper node-span closure F, add sum_{k notin F} y_k >= 1",
        },
        "panel": panel,
        "summary": {
            "keys": len(panel),
            "btva_compatible_sat": sum(1 for x in panel if x["result"] == "SAT_BTVA_COMPATIBLE_RELAXED_LIFT"),
            "btva_nonconic_unsat": sum(1 for x in panel if x["result"] == "UNSAT_NONCONIC_BTVA_RELAXED_FIBER"),
            "unknown": sum(1 for x in panel if x["result"] == "UNKNOWN"),
            "total_lazy_flat_cuts": sum(len(x["lazy_flat_cuts"]) for x in panel),
        },
        "firewalls": {
            "bounded_panel_only": True,
            "nonconic_only": True,
            "known_32_plane_conics_closed": False,
            "main_pruning_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
        "next_exact_step": "If bounded keys show UNSAT, add an exact conic-exception adapter and a multiplicity/source-key mass adapter before any numerical pruning proposal. If all keys are SAT, test a higher-degree genus-0 row before scaling.",
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_STATIC7_BOUNDED_PANEL_SUMMARY=" + json.dumps(out["summary"], sort_keys=True))
    print("BTVA_STATIC7_BOUNDED_PANEL_CANONICAL=" + out["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
