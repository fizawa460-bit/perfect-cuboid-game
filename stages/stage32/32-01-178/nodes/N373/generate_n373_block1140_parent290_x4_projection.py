#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

from sympy import Matrix
from z3 import sat, unsat, unknown

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STATE = HERE / "STATE.json"
N372_DIR = HERE.parent / "N372"
N372_AUDIT = N372_DIR / "AUDIT-PASS.json"
N372_RESULT = N372_DIR / "RESULT.json"
N372_GENERATOR = N372_DIR / "generate_n372_block1140_parent290_direct_picard64_probe.py"

STATE_BLOB = "3a0ca8355131c5a791c50c299e368cd8c4ffaba9"
STATE_CANON = "79946afd0d1948ff3165b9ece960ed21c3c18a9943acffc571ba0090ae74afd8"
N372_AUDIT_BLOB = "6ff80567e922890d0fb4517789537d398b34f761"
N372_AUDIT_CANON = "4bead765cb9badfe6fb8ce4b1ae0c74807f541e35879fe1ad44b00f240680454"
N372_RESULT_BLOB = "c0267d903fd0b397fcd4766b03964bde788650e7"
N372_RESULT_CANON = "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48"
N372_GENERATOR_BLOB = "4ac20f586028345ef5f1a691718305e1bbcbf700"
BLOCK, OFFSET, WIDTH = 1140, 797, 113
PARENT_ORDINAL = 290


def req(v: bool, msg: str) -> None:
    if not v:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def checked(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
    req(canonical(obj) == expected_canon, f"canonical drift: {path}")
    return obj


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    state = checked(STATE, STATE_BLOB, STATE_CANON)
    audit = checked(N372_AUDIT, N372_AUDIT_BLOB, N372_AUDIT_CANON)
    n372_result = checked(N372_RESULT, N372_RESULT_BLOB, N372_RESULT_CANON)
    req(blob(N372_GENERATOR) == N372_GENERATOR_BLOB, "N372 generator blob drift")
    req(audit["status"] == "HOSTILE_REAUDIT_PASS_CURRENT_V15_WITNESS_CANDIDATE_ONLY", "N372 audit PASS drift")
    req(audit["review_id"] == 5187357950 and audit["audited_exact_head"] == "9fb78a0e0c7b52baca84058dea69b8b083e33774", "N372 audit identity drift")
    req(n372_result["status"] == "SAT_CURRENT_V15_WITNESS_CANDIDATE", "N372 result drift")

    n372 = load_module(N372_GENERATOR, "n373_n372")
    _n372_state, cut196, comp, n362 = n372.preflight(args.cut196_root.resolve(), args.n357_composition_root.resolve())
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    idx = core.e8.indexer()
    survivors = core.e8.current_main_survivor_block_indices()
    req(survivors[OFFSET] == BLOCK, "block1140 survivor offset drift")
    base = tuple(int(v) for v in idx.unrank(BLOCK * WIDTH))
    req(comp.prefix_survives(base) and comp.n357_accepts(base), "current-V15 membership replay failed")
    parents = list(core.e8.iter_parent_population(BLOCK, g))
    req(len(parents) == 300, "block1140 parent population drift")
    parent = parents[PARENT_ORDINAL]

    timeout_ms = int(state["method"]["per_check_timeout_ms"])
    solver, cvars, yexpr, _fixed, allowed = n362.exact_solver_for_parent(core, P, blocks, g, BLOCK, parent, timeout_ms)
    req(allowed == list(range(8)), "parent290 x4 residue projection drift")
    solver.set(timeout=timeout_ms)

    bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, "n373_bundle")
    G = Matrix(bundle["picard_gram_64x64"])
    selected_labels = [int(v) for v in g.selected_labels]
    Psel = P.extract([label - 1 for label in selected_labels], list(range(64)))

    witnesses: list[dict] = []
    seen: set[int] = set()
    terminal_status = None
    reason_unknown = None
    checks = 0
    max_models = int(state["method"]["maximum_sat_models"])

    while len(seen) < max_models:
        r = solver.check()
        checks += 1
        if r == unsat:
            terminal_status = "COMPLETE_EXACT_X4_PROJECTION"
            break
        if r == unknown:
            terminal_status = "PARTIAL_X4_PROJECTION_UNKNOWN_TIMEOUT"
            reason_unknown = solver.reason_unknown()
            break
        req(r == sat, f"unexpected solver result: {r}")
        m = solver.model()
        x4 = int(m.eval(yexpr[48], model_completion=True).as_long())
        req(0 <= x4 <= 112 and x4 not in seen, f"x4 projection duplicate/out of range: {x4}")
        coords = [int(m.eval(v, model_completion=True).as_long()) for v in cvars]
        pairings = [int(m.eval(v, model_completion=True).as_long()) for v in yexpr]
        terminal = [pairings[label - 1] for label in n362.ASSIGNMENT_ORDER]
        rank = int(idx.rank(tuple(terminal)))
        req(rank == BLOCK * WIDTH + x4, "terminal rank/x4 projection drift")
        req(list(idx.unrank(rank)) == terminal, "terminal roundtrip drift")
        cv = Matrix(coords)
        selected64 = [pairings[label - 1] for label in selected_labels]
        req([int(v) for v in Psel * cv] == selected64, "selected64 replay drift")
        req([int(v) for v in P * cv] == pairings, "all140 replay drift")
        self_square = int((cv.T * G * cv)[0])
        scale = 16 // math.gcd(8, 16)
        numerator = scale * scale * 64 - 16 * scale * scale * self_square
        req(numerator % 16 == 0, "Hperp scalar integrality drift")
        witnesses.append({
            "x4": x4,
            "terminal_rank": rank,
            "terminal_identity": f"g1-d008|e=8|rank={rank}",
            "compressed_terminal_pairings": terminal,
            "picard64_coordinates": coords,
            "picard64_coordinates_sha256": csha(coords),
            "selected64_pairings_sha256": csha(selected64),
            "all140_pairings_sha256": csha(pairings),
            "self_square": self_square,
            "negative_hperp_square_N": numerator // 16,
        })
        seen.add(x4)
        solver.add(yexpr[48] != x4)

    if len(seen) == 113:
        terminal_status = "COMPLETE_EXACT_X4_PROJECTION"
    req(terminal_status is not None, "projection status missing")
    witnesses.sort(key=lambda w: w["x4"])
    feasible = [int(w["x4"]) for w in witnesses]
    infeasible = [x for x in range(113) if x not in seen] if terminal_status == "COMPLETE_EXACT_X4_PROJECTION" else None
    body = {
        "schema": "STAGE32_32_01_178_N373_BLOCK1140_PARENT290_X4_TERMINAL_PROJECTION_RESULT_V1",
        "status": terminal_status,
        "target": {"row_id":"g1-d008","block_index":BLOCK,"survivor_offset":OFFSET,"parent_ordinal":PARENT_ORDINAL,"x4_domain":[0,112]},
        "method": {"formulation":"INCREMENTAL_DIRECT_PICARD64_COORDINATES_BLOCK_X4_MODEL_VALUE","per_check_timeout_ms":timeout_ms,"solver_checks":checks,"reason_unknown":reason_unknown},
        "projection": {
            "complete": terminal_status == "COMPLETE_EXACT_X4_PROJECTION",
            "feasible_x4": feasible,
            "feasible_terminal_count": len(feasible),
            "infeasible_x4": infeasible,
            "infeasible_terminal_count": len(infeasible) if infeasible is not None else None,
            "one_witness_per_feasible_x4": witnesses,
        },
        "scope": {"counts_all_picard_classes_per_terminal":False,"local_parent_projection_only":True},
        "credit": {"main_pruning_credit":False,"full178_complete":False,"n350_registered":False,"effectivity_final":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": terminal_status,
        "feasible_terminal_count": len(feasible),
        "feasible_x4": feasible,
        "infeasible_terminal_count": len(infeasible) if infeasible is not None else None,
        "solver_checks": checks,
        "reason_unknown": reason_unknown,
        "canonical": body["canonical_sha256_without_this_field"],
        "main_pruning_credit": False,
        "full178_complete": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
