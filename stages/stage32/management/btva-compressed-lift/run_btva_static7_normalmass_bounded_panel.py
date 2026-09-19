#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from z3 import Int, SolverFor, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[4]
RELAXED = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_static7_bounded_panel.py"
RELAXED_BLOB = "e44bec7ad9c0b7a4d8d7d87a455f181a681035c6"
OLD_PANEL_CANONICAL = "476aca330bea8c6e70de64dbdd8c6db7395787c8510d76a53fcbfa2e38d8a25c"

ROW_ID = "g0-d008"
GENUS = 0
DEGREE = 8
EXCEPTIONAL_MASS = 8
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64
NORMAL_MASS = 19 * DEGREE - 5 * EXCEPTIONAL_MASS
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
    req(NORMAL_MASS == 112, "g0-d008 e8 normal-mass regression")

    # Lock the previously audited/merged relaxed producer before importing it.
    req(RELAXED.is_file() and git_blob(RELAXED) == RELAXED_BLOB,
        "relaxed static7 producer drift")
    old = load_module(RELAXED, "stage32_main_btva_static7_relaxed")

    # Reuse the same exact source locks and static-key sampler as the relaxed
    # bounded panel, but strengthen only by exact all140 nonnegativity and the
    # Picard64 mass identity normal_total + 5*exceptional_total = 19*degree.
    req(old.ROW_ID == ROW_ID and old.GENUS == GENUS and old.DEGREE == DEGREE,
        "relaxed target drift")
    req(old.EXCEPTIONAL_MASS == EXCEPTIONAL_MASS, "relaxed e drift")
    req(tuple(old.STATIC_ORDER) == STATIC_ORDER, "relaxed static order drift")

    req(old.BASE.is_file() and old.git_blob(old.BASE) == old.BASE_BLOB,
        "base Picard solver drift")
    req(old.NODE_BRIDGE.is_file() and old.git_blob(old.NODE_BRIDGE) == old.NODE_BRIDGE_BLOB,
        "node bridge drift")
    req(old.MANIFEST.is_file() and old.git_blob(old.MANIFEST) == old.MANIFEST_BLOB,
        "manifest drift")
    lane_agg = args.lane178_root / old.LANE178_AGG_REL
    req(lane_agg.is_file() and old.git_blob(lane_agg) == old.LANE178_AGG_BLOB,
        "lane178 aggregate Picard source drift")

    manifest = json.loads(old.MANIFEST.read_text(encoding="utf-8"))
    rows = set()
    for ids in manifest["m_class_rows"].values():
        rows.update(str(x) for x in ids)
    req(len(rows) == 178 and ROW_ID in rows, "g0-d008 absent from FULL178 manifest")

    v1 = old.load_module(old.BASE, "stage32_main_btva_static7_normalmass_base")
    req(tuple(v1.EXPECTED_ASSIGNMENT_ORDER) == old.ASSIGNMENT,
        "base assignment order drift")
    indexer = v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    total = int(indexer.terminal_count)
    ranks = old.panel_ranks(total)

    bundle = v1.load_retained(args.retained, "stage32_main_btva_static7_normalmass_bundle")
    marking = v1.load_retained(args.marking, "stage32_main_btva_static7_normalmass_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    req(P.shape == (140, PICARD_RANK), "all140 pairing matrix shape")
    bridge_cert = bridge.certificate
    req(bridge_cert.get("mass_identity_exact_on_picard64") is True,
        "Picard64 mass identity source drift")
    req(bridge_cert.get("mass_identity") ==
        "normal_total + 5*exceptional_total = 19*degree",
        "Picard64 mass identity formula drift")

    node_bridge = json.loads(old.NODE_BRIDGE.read_text(encoding="utf-8"))
    nodes = old.node_matrix(node_bridge)
    req(nodes.shape == (48, 7) and int(nodes.rank()) == 7,
        "48-node ambient span drift")

    terminal_rows = []
    unique_static: dict[tuple[int, ...], list[int]] = {}
    for rank in ranks:
        terminal = tuple(int(x) for x in indexer.unrank(rank))
        req(indexer.rank(terminal) == rank, "rank/unrank replay")
        static = old.static_from_terminal(terminal)
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
        aggregate_exprs = [
            sum(int(old.L[i][j]) * assignment_exprs[j] for j in range(len(old.ASSIGNMENT)))
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
                result_status = "UNSAT_NONCONIC_BTVA_EFFECTIVE_PAIRING_FIBER"
                break
            if result == unknown:
                result_status = "UNKNOWN"
                reason_unknown = solver.reason_unknown()
                break
            req(result == sat, "unexpected solver status")

            model = solver.model()
            nv = [int(model.eval(expr, model_completion=True).as_long()) for expr in normal]
            ev = [int(model.eval(expr, model_completion=True).as_long()) for expr in exceptional]
            req(min(nv) >= 0 and sum(nv) == NORMAL_MASS,
                "normal mass model replay")
            req(min(ev) >= 0 and sum(ev) == EXCEPTIONAL_MASS,
                "exceptional mass model replay")

            support = tuple(i for i, value in enumerate(ev) if value > 0)
            rank = old.support_rank(nodes, support)
            if rank == 7:
                result_status = "SAT_BTVA_COMPATIBLE_EFFECTIVE_PAIRING_LIFT"
                compatible_support = {
                    "normal_pairings_sha256": v1.csha(nv),
                    "exceptional_pairings": ev,
                    "support_indices_0based": list(support),
                    "support_size": len(support),
                    "support_rank": rank,
                }
                break

            req(rank < 7, "support rank exceeded ambient rank")
            flat = old.closure(nodes, support)
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
            "normal_all140_nonnegativity_imposed": True,
            "normal_mass": NORMAL_MASS,
            "normal_mass_identity":
                "normal_total + 5*exceptional_total = 19*degree",
            "semantics":
                "UNSAT is safe for the nonconic BTVA receiver under exact effective-pairing necessary conditions; SAT/UNKNOWN carries no pruning credit",
        })

    out = {
        "schema": "STAGE32_MAIN_BTVA_STATIC7_NORMALMASS_BOUNDED_PANEL_V1",
        "stage": 32,
        "route": "BTVA_COMPRESSED_PICARD_LIFT_RECEIVER_INTERSECTION",
        "status": "BOUNDED_NORMALMASS_PANEL_COMPLETE_ZERO_CREDIT",
        "predecessor": {
            "relaxed_producer_blob_sha1": RELAXED_BLOB,
            "relaxed_bounded_panel_canonical_sha256": OLD_PANEL_CANONICAL,
            "relation":
                "strict solver strengthening by exact all140 nonnegativity and exact normal mass only",
        },
        "source_locks": {
            "base_picard_solver_blob_sha1": old.BASE_BLOB,
            "node_bridge_blob_sha1": old.NODE_BRIDGE_BLOB,
            "manifest_blob_sha1": old.MANIFEST_BLOB,
            "lane178_head": old.LANE178_HEAD,
            "lane178_aggregate_picard_blob_sha1": old.LANE178_AGG_BLOB,
        },
        "target": {
            "row_id": ROW_ID,
            "genus": GENUS,
            "degree": DEGREE,
            "exceptional_mass": EXCEPTIONAL_MASS,
            "normal_mass": NORMAL_MASS,
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
            "all140_pairings_nonnegative": True,
            "normal_pairing_sum": NORMAL_MASS,
            "exceptional_pairing_sum": EXCEPTIONAL_MASS,
            "normal_pairing_upper_bound": NORMAL_MASS,
            "exceptional_pairing_upper_bound": EXCEPTIONAL_MASS,
            "mass_identity_exact_on_picard64": True,
            "btva_condition":
                "nonconic genus-0 support must span P6; known 32 plane conics preserved separately",
            "lazy_flat_cut":
                "for a realized proper node-span closure F, add sum_{k notin F} y_k >= 1",
        },
        "panel": panel,
        "summary": {
            "keys": len(panel),
            "btva_compatible_sat": sum(
                1 for x in panel
                if x["result"] == "SAT_BTVA_COMPATIBLE_EFFECTIVE_PAIRING_LIFT"
            ),
            "btva_nonconic_unsat": sum(
                1 for x in panel
                if x["result"] == "UNSAT_NONCONIC_BTVA_EFFECTIVE_PAIRING_FIBER"
            ),
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
        "next_exact_step":
            "Compare with the relaxed 5-key panel. If timeout keys become UNSAT, build a source-key multiplicity adapter and an exact conic-exception disposition before any numerical MAIN pruning proposal.",
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_STATIC7_NORMALMASS_SUMMARY=" + json.dumps(out["summary"], sort_keys=True))
    print("BTVA_STATIC7_NORMALMASS_CANONICAL=" + out["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
