#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path

from z3 import Int, SolverFor, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[5]
PARENT = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_normalmass_bounded_panel.py"
PARENT_BLOB = "29114c0cd8a2c604d24b2a9ad3418fc2b5200171"
RR = ROOT / "stages/stage32/final-chain/32-02-effectivity/hperp_norm_rr_adapter.py"
RR_BLOB = "069e9215305fe4fa34d9949c871914b5ee17f19d"
HANDOFF = ROOT / "stages/stage32/final-chain/32-02-effectivity/SCALAR-PRODUCER-RESEARCH-HANDOFF.md"
HANDOFF_BLOB = "61da6fb75643d8e58b642f5de5d90dc6fe9ff227"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
MANIFEST_BLOB = "0a46b34e278688240656b4977e9cb7f589e90e06"

ROW_ID = "g0-d018"
GENUS = 0
DEGREE = 18
EXCEPTIONAL_MASS = 8
NORMAL_MASS = 19 * DEGREE - 5 * EXCEPTIONAL_MASS
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64
X4_VALUES = NORMAL_MASS + 1
ADJUNCTION_LOWER = -DEGREE - 2 + 2 * GENUS
RR_C2_THRESHOLD = DEGREE - 14
BAD_SHELL_UPPER_SAFE = RR_C2_THRESHOLD - 1
EXPECTED_BASE4_KEYS = 343
EXPECTED_EXCEPTIONAL_STATES = 11318
EXPECTED_STATIC7_KEYS = EXPECTED_BASE4_KEYS * X4_VALUES
EXPECTED_TERMINAL_MASS = EXPECTED_EXCEPTIONAL_STATES * X4_VALUES
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


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {name}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def quadratic_form(gram: list[list[int]], xvars):
    terms = []
    for i in range(PICARD_RANK):
        gii = int(gram[i][i])
        if gii:
            terms.append(gii * xvars[i] * xvars[i])
        for j in range(i + 1, PICARD_RANK):
            gij = int(gram[i][j])
            req(gij == int(gram[j][i]), "Picard Gram lost symmetry")
            if gij:
                terms.append(2 * gij * xvars[i] * xvars[j])
    return sum(terms)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--lane178-root", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=15000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    req(args.solver_timeout_ms > 0, "solver timeout")

    # Lock every executable/semantic dependency before importing.
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "BTVA base4 parent drift")
    req(RR.is_file() and git_blob(RR) == RR_BLOB, "RR adapter drift")
    req(HANDOFF.is_file() and git_blob(HANDOFF) == HANDOFF_BLOB, "32-02 scalar handoff drift")
    req(MANIFEST.is_file() and git_blob(MANIFEST) == MANIFEST_BLOB, "FULL178 manifest drift")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    req(manifest["schema"] == "STAGE32_RESIDUAL32_01_FULL178_MANIFEST_V1", "manifest schema")
    req(manifest["residual_row_count"] == 178, "FULL178 row count")
    r = math.gcd(DEGREE, 16)
    m = 16 // r
    req(ROW_ID in manifest["m_class_rows"][str(m)], "g0-d018 absent from FULL178 manifest")
    req(EXCEPTIONAL_MASS >= manifest["row_parameter_derivation"]["exceptional_mass_min_g0"],
        "e below genus-0 FULL178 minimum")
    req(EXCEPTIONAL_MASS <= (19 * DEGREE) // 5, "e above FULL178 maximum")

    parent = load_module(PARENT, "stage32_eff_cfrr01_parent")
    req(parent.RELAXED.is_file() and parent.blob(parent.RELAXED) == parent.RELAXED_BLOB,
        "BTVA relaxed source drift")
    old = parent.load_module(parent.RELAXED, "stage32_eff_cfrr01_relaxed")
    req(old.BASE.is_file() and old.git_blob(old.BASE) == old.BASE_BLOB,
        "base Picard solver drift")
    lane_agg = args.lane178_root / old.LANE178_AGG_REL
    req(lane_agg.is_file() and old.git_blob(lane_agg) == old.LANE178_AGG_BLOB,
        "lane178 aggregate Picard source drift")
    v1 = old.load_module(old.BASE, "stage32_eff_cfrr01_base")

    # Exact source-key census for the d18/e8 row.  Exceptional base4 states
    # depend only on e; x4 is the independent normal coordinate.
    indexer = v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    req(indexer.normal_budget == NORMAL_MASS, "normal budget drift")
    req(int(indexer.exceptional_count) == EXPECTED_EXCEPTIONAL_STATES,
        "e8 exceptional-state count drift")
    req(int(indexer.terminal_count) == EXPECTED_TERMINAL_MASS,
        "d18/e8 terminal mass drift")
    counts: Counter[tuple[int, int, int, int]] = Counter()
    stride = X4_VALUES
    for erank in range(int(indexer.exceptional_count)):
        terminal = tuple(int(v) for v in indexer.unrank(erank * stride))
        req(terminal[4] == 0, "x4 stride replay")
        req(indexer.rank(terminal) == erank * stride, "rank/unrank replay")
        key = tuple(old.static_from_terminal(terminal)[:4])
        counts[key] += 1
    req(len(counts) == EXPECTED_BASE4_KEYS, "base4 key count drift")
    req(sum(counts.values()) == EXPECTED_EXCEPTIONAL_STATES, "exceptional census mass")
    req({k: int(counts[k]) for k in SAMPLE_BASE4} == EXPECTED_MULTIPLICITY,
        "sample base4 multiplicity drift")
    req(len(counts) * X4_VALUES == EXPECTED_STATIC7_KEYS, "static7 count drift")
    req(sum(int(v) * X4_VALUES for v in counts.values()) == EXPECTED_TERMINAL_MASS,
        "terminal mass conservation")

    bundle = v1.load_retained(args.retained, "stage32_eff_cfrr01_bundle")
    marking = v1.load_retained(args.marking, "stage32_eff_cfrr01_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    req(P.shape == (140, PICARD_RANK), "pairing matrix shape")
    req(bridge.certificate.get("mass_identity_exact_on_picard64") is True,
        "Picard64 mass identity source drift")
    gram = [[int(v) for v in row] for row in bundle["picard_gram_64x64"]]
    req(len(gram) == PICARD_RANK and all(len(row) == PICARD_RANK for row in gram),
        "Picard Gram shape")

    rr = load_module(RR, "stage32_eff_cfrr01_rr")
    boundary_num = m * m * (DEGREE * DEGREE - 16 * RR_C2_THRESHOLD)
    req(boundary_num % 16 == 0, "boundary norm nonintegral")
    boundary_N = boundary_num // 16
    rr_boundary = rr.classify_from_norm(DEGREE, boundary_N, source_affirmed=True)
    req(rr_boundary.effective_divisor_certified is True, "RR boundary not certified")
    req(rr_boundary.C2 == RR_C2_THRESHOLD, "RR boundary C2 drift")

    def add_linear_fiber(solver, xvars, base4):
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
        return pairings, assignment_exprs[4]

    panel = []
    for idx, base4 in enumerate(SAMPLE_BASE4):
        base_vars = [Int(f"base_{idx}_{j}") for j in range(PICARD_RANK)]
        base_solver = SolverFor("QF_LIA")
        base_solver.set(timeout=args.solver_timeout_ms)
        _, base_x4 = add_linear_fiber(base_solver, base_vars, base4)
        base_result = base_solver.check()

        row = {
            "base4": list(base4),
            "exceptional_multiplicity_per_x4": int(counts[base4]),
            "x4_values_covered": X4_VALUES,
            "source_terminal_mass": int(counts[base4]) * X4_VALUES,
            "base_linear_status": str(base_result).upper(),
            "bad_shell_status": None,
            "classification": None,
            "reason_unknown": None,
        }

        if base_result == unsat:
            row["classification"] = "LINEAR_FIBER_UNSAT__SOURCE_KEY_IMPOSSIBLE"
            panel.append(row)
            continue
        if base_result == unknown:
            row["classification"] = "UNKNOWN_BASE_LINEAR"
            row["reason_unknown"] = base_solver.reason_unknown()
            panel.append(row)
            continue
        req(base_result == sat, "unexpected base solver result")
        base_model = base_solver.model()
        x4_value = int(base_model.eval(base_x4, model_completion=True).as_long())
        req(0 <= x4_value <= NORMAL_MASS, "base x4 witness range")
        row["base_x4_witness"] = x4_value

        bad_vars = [Int(f"bad_{idx}_{j}") for j in range(PICARD_RANK)]
        bad_solver = SolverFor("QF_NIA")
        bad_solver.set(timeout=args.solver_timeout_ms)
        bad_pairings, bad_x4 = add_linear_fiber(bad_solver, bad_vars, base4)
        selfsq = quadratic_form(gram, bad_vars)
        bad_solver.add(selfsq >= ADJUNCTION_LOWER)
        # Search a deliberately slightly enlarged failure shell.  UNSAT here
        # implies every actual integral lift has C^2 >= d-14 without relying
        # on the surface parity identity.
        bad_solver.add(selfsq <= BAD_SHELL_UPPER_SAFE)
        bad_result = bad_solver.check()
        row["bad_shell_status"] = str(bad_result).upper()

        if bad_result == unsat:
            row["classification"] = "ALL_RELAXED_BASE4_LIFTS_RR_EFFECTIVE_CANDIDATE"
        elif bad_result == unknown:
            row["classification"] = "UNKNOWN_BAD_SHELL"
            row["reason_unknown"] = bad_solver.reason_unknown()
        else:
            req(bad_result == sat, "unexpected bad-shell solver result")
            model = bad_solver.model()
            coords = [int(model.eval(v, model_completion=True).as_long()) for v in bad_vars]
            c2 = int(model.eval(selfsq, model_completion=True).as_long())
            x4_bad = int(model.eval(bad_x4, model_completion=True).as_long())
            req(ADJUNCTION_LOWER <= c2 <= BAD_SHELL_UPPER_SAFE, "bad-shell witness C2")
            req(0 <= x4_bad <= NORMAL_MASS, "bad-shell x4 witness")
            vals = [int(model.eval(expr, model_completion=True).as_long()) for expr in bad_pairings]
            req(min(vals) >= 0, "bad-shell all140 nonnegativity")
            req(sum(vals[:NORMAL_COUNT]) == NORMAL_MASS, "bad-shell normal mass")
            req(sum(vals[NORMAL_COUNT:]) == EXCEPTIONAL_MASS, "bad-shell exceptional mass")
            row["classification"] = "RR_AMBIGUOUS_LOW_C2_WITNESS__NOT_NON_EFFECTIVITY"
            row["bad_shell_witness"] = {
                "C2": c2,
                "x4": x4_bad,
                "picard_coordinates": coords,
                "picard_coordinates_sha256": csha(coords),
                "all140_pairings_sha256": csha(vals),
            }
        panel.append(row)

    summary = {
        "sample_base4_keys": len(panel),
        "linear_fiber_unsat": sum(r["classification"] == "LINEAR_FIBER_UNSAT__SOURCE_KEY_IMPOSSIBLE" for r in panel),
        "rr_all_lifts_candidate": sum(r["classification"] == "ALL_RELAXED_BASE4_LIFTS_RR_EFFECTIVE_CANDIDATE" for r in panel),
        "rr_ambiguous_low_c2_witness": sum(r["classification"] == "RR_AMBIGUOUS_LOW_C2_WITNESS__NOT_NON_EFFECTIVITY" for r in panel),
        "unknown": sum(r["classification"].startswith("UNKNOWN") for r in panel),
        "source_terminal_mass_in_sample": sum(r["source_terminal_mass"] for r in panel),
        "source_terminal_mass_rr_candidate": sum(
            r["source_terminal_mass"] for r in panel
            if r["classification"] == "ALL_RELAXED_BASE4_LIFTS_RR_EFFECTIVE_CANDIDATE"
        ),
    }
    out = {
        "schema": "STAGE32_MAIN_32_02_EFF_CFRR01_D18E8_BASE4_PILOT_V1",
        "stage": 32,
        "item": "32-02_EFFECTIVITY_SURVIVOR_DISPOSAL",
        "route": "EFF_CFRR01_COMPRESSED_BASE4_PICARD64_RR_FAILURE_SHELL",
        "status": "BOUNDED_FIVE_BASE4_PILOT_COMPLETE_ZERO_CREDIT",
        "source_locks": {
            "btva_base4_parent_blob_sha1": PARENT_BLOB,
            "rr_adapter_blob_sha1": RR_BLOB,
            "scalar_handoff_blob_sha1": HANDOFF_BLOB,
            "full178_manifest_blob_sha1": MANIFEST_BLOB,
            "base_picard_solver_blob_sha1": old.BASE_BLOB,
            "lane178_aggregate_picard_blob_sha1": old.LANE178_AGG_BLOB,
        },
        "target": {
            "row_id": ROW_ID,
            "genus": GENUS,
            "degree": DEGREE,
            "exceptional_mass": EXCEPTIONAL_MASS,
            "normal_mass": NORMAL_MASS,
            "base4_order": ["a", "b", "c", "t"],
            "x4_existential": True,
            "base4_key_count": EXPECTED_BASE4_KEYS,
            "exceptional_state_count": EXPECTED_EXCEPTIONAL_STATES,
            "x4_values_per_base4": X4_VALUES,
            "static7_key_count": EXPECTED_STATIC7_KEYS,
            "terminal_mass": EXPECTED_TERMINAL_MASS,
        },
        "rr_gate": {
            "adjunction_C2_lower": ADJUNCTION_LOWER,
            "rr_effective_C2_threshold": RR_C2_THRESHOLD,
            "bad_shell_upper_safe": BAD_SHELL_UPPER_SAFE,
            "gcd_d_16": r,
            "m": m,
            "boundary_N": boundary_N,
            "boundary_16N": 16 * boundary_N,
            "adapter_gate_rhs": m * m * (DEGREE * DEGREE - 16 * DEGREE + 224),
            "source_affirmed_by_this_worker_only_after_retained_bundle_marking_and_lane178_replay": True,
        },
        "decision_problem": {
            "picard_integer_variables": PICARD_RANK,
            "base4_plus_e_d_fixed": True,
            "x4_and_residual_observables_existential": True,
            "all140_pairings_nonnegative": True,
            "normal_pairing_sum": NORMAL_MASS,
            "exceptional_pairing_sum": EXCEPTIONAL_MASS,
            "linear_feasibility_solver": "Z3_QF_LIA",
            "bad_rr_shell_solver": "Z3_QF_NIA",
            "bad_rr_shell": [ADJUNCTION_LOWER, BAD_SHELL_UPPER_SAFE],
            "safe_logic":
                "UNSAT of the enlarged low-C2 shell over the relaxed base4 Picard64 fiber implies every actual source terminal under that base4 key has C2>=d-14. SAT only proves an ambiguous numerical lift exists and is not a non-effectivity certificate.",
        },
        "panel": panel,
        "summary": summary,
        "firewalls": {
            "qf_nia_unsat_is_independently_certified": False,
            "main_pruning_credit": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
        "next_exact_step":
            "Run this five-key pilot. If any RR-all-lifts candidates appear, replace QF_NIA UNSAT reliance with an independent HNF/Gram-LLL/Fincke-Pohst base4-fiber checker before expanding to all 343 d18/e8 base4 keys.",
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("EFF_CFRR01_SUMMARY=" + json.dumps(summary, sort_keys=True))
    print("EFF_CFRR01_CANONICAL=" + out["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
