#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import time
from collections import Counter

import z3

EXPECTED_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
DEGREE = 16
GENUS = 0
M = 1
N = 1
NORM_BOUND = 34
NORMAL_CAP = 8
EXCEPTIONAL_CAP = 4


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def dot(row: list[int], vars_: list[z3.ArithRef]) -> z3.ArithRef:
    terms = [int(a) * vars_[i] for i, a in enumerate(row) if int(a)]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def quad(gram: list[list[int]], vars_: list[z3.ArithRef]) -> z3.ArithRef:
    terms: list[z3.ArithRef] = []
    for i in range(len(vars_)):
        g = int(gram[i][i])
        if g:
            terms.append(g * vars_[i] * vars_[i])
        for j in range(i + 1, len(vars_)):
            g = int(gram[i][j])
            if g:
                terms.append(2 * g * vars_[i] * vars_[j])
    return z3.Sum(terms) if terms else z3.IntVal(0)


def exact_recheck(core: dict, values: list[int]) -> dict[str, int]:
    gram = core["basis_gram"]
    h = [int(v) for v in core["hyperplane"]]
    known = core["raw_cross_pairings_with_basis"]

    def idot(a: list[int], b: list[int]) -> int:
        return sum(int(x) * int(y) for x, y in zip(a, b))

    hrow = [sum(h[i] * int(gram[i][j]) for i in range(64)) for j in range(64)]
    degree = idot(hrow, values)
    assert degree == DEGREE
    y = [values[i] - h[i] for i in range(64)]
    hy = idot(hrow, y)
    assert hy == 0
    y2 = sum(y[i] * int(gram[i][j]) * y[j] for i in range(64) for j in range(64))
    norm = -y2
    assert 0 <= norm <= NORM_BOUND
    pairings = [idot([int(v) for v in row], values) for row in known]
    assert all(0 <= pairings[i] <= NORMAL_CAP for i in range(92))
    assert all(0 <= pairings[i] <= EXCEPTIONAL_CAP for i in range(92, 140))
    e = sum(pairings[92:])
    a = sum(pairings[:46])
    c2 = sum(values[i] * int(gram[i][j]) * values[j] for i in range(64) for j in range(64))
    assert c2 == DEGREE - norm
    assert c2 >= -DEGREE - 2 + 2 * GENUS
    return {"norm": norm, "self_intersection": c2, "exceptional_mass": e, "curve_group_mass": a}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--max-models", type=int, default=20000)
    ap.add_argument("--max-seconds", type=float, default=600.0)
    ap.add_argument("--check-timeout-ms", type=int, default=60000)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    claimed = core.get("canonical_sha256_without_this_field")
    unsigned = dict(core)
    unsigned.pop("canonical_sha256_without_this_field", None)
    assert claimed == EXPECTED_CORE_SHA == csha(unsigned)
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    assert int(core["rank"]) == 64 and int(core["h2"]) == 16
    assert len(core["raw_cross_pairings_with_basis"]) == 140

    gram = [[int(v) for v in row] for row in core["basis_gram"]]
    h = [int(v) for v in core["hyperplane"]]
    hrow = [sum(h[i] * gram[i][j] for i in range(64)) for j in range(64)]
    assert sum(hrow[i] * h[i] for i in range(64)) == 16

    # Direct norm-first/global formulation.  No exceptional-assignment or
    # signature-cell materialization is constructed in this scout.
    x = [z3.Int(f"c{i}") for i in range(64)]
    y = [x[i] - h[i] for i in range(64)]
    solver = z3.SolverFor("QF_NIA")
    solver.set(random_seed=0, threads=1, timeout=int(args.check_timeout_ms))
    solver.add(dot(hrow, x) == DEGREE)
    solver.add(dot(hrow, y) == 0)

    for i, row in enumerate(core["raw_cross_pairings_with_basis"]):
        p = dot([int(v) for v in row], x)
        cap = NORMAL_CAP if i < 92 else EXCEPTIONAL_CAP
        solver.add(p >= 0, p <= cap)

    ynorm = -quad(gram, y)
    solver.add(ynorm >= 0, ynorm <= NORM_BOUND)

    started = time.perf_counter()
    models = 0
    norm_hist: Counter[int] = Counter()
    parent_hist: Counter[tuple[int, int]] = Counter()
    self_hist: Counter[int] = Counter()
    sample: list[dict] = []
    digest = hashlib.sha256()
    terminal = "RUNNING"
    last_check_seconds = 0.0

    while True:
        if models >= args.max_models:
            terminal = "MODEL_CAP"
            break
        if time.perf_counter() - started >= args.max_seconds:
            terminal = "WALL_TIME_CAP"
            break
        check_started = time.perf_counter()
        result = solver.check()
        last_check_seconds = time.perf_counter() - check_started
        if result == z3.unsat:
            terminal = "EXHAUSTED_UNSAT"
            break
        if result == z3.unknown:
            terminal = "UNKNOWN"
            break
        model = solver.model()
        values = [model.eval(v, model_completion=True).as_long() for v in x]
        stats = exact_recheck(core, values)
        models += 1
        norm_hist[int(stats["norm"])] += 1
        self_hist[int(stats["self_intersection"])] += 1
        parent_hist[(int(stats["exceptional_mass"]), int(stats["curve_group_mass"]))] += 1
        raw = json.dumps(values, separators=(",", ":")).encode()
        digest.update(hashlib.sha256(raw).digest())
        if len(sample) < 20:
            sample.append({"basis_coordinates": values, **stats})
        solver.add(z3.Or([x[i] != values[i] for i in range(64)]))

    elapsed = time.perf_counter() - started
    report = {
        "schema": "STAGE32_SCOUT_D16_NORM_FIRST_GLOBAL_QFNIA_V1",
        "scope": "SCOUT_ONLY_NO_CREDIT",
        "source_core_canonical_sha256": EXPECTED_CORE_SHA,
        "source_blob_sha1": EXPECTED_SOURCE_BLOB,
        "parameters": {
            "degree": DEGREE,
            "genus": GENUS,
            "m": M,
            "n": N,
            "hperp_norm_bound": NORM_BOUND,
            "normal_intersection_cap": NORMAL_CAP,
            "exceptional_intersection_cap": EXCEPTIONAL_CAP,
        },
        "architecture": {
            "direction": "GLOBAL_PICARD_COORDINATES_EQUIVALENT_TO_NORM_FIRST_HPERP_BALL",
            "exceptional_assignment_materialization": False,
            "signature_cell_materialization": False,
            "materialized_branch_count_constructed": 0,
            "solver": "Z3_QF_NIA",
            "single_global_solver_context": True,
        },
        "pilot_limits": {
            "max_models": args.max_models,
            "max_seconds": args.max_seconds,
            "check_timeout_ms": args.check_timeout_ms,
        },
        "terminal_status": terminal,
        "exact_models_rechecked": models,
        "elapsed_seconds": round(elapsed, 6),
        "last_solver_check_seconds": round(last_check_seconds, 6),
        "model_stream_digest": digest.hexdigest(),
        "norm_histogram": {str(k): v for k, v in sorted(norm_hist.items())},
        "self_intersection_histogram": {str(k): v for k, v in sorted(self_hist.items())},
        "parent_histogram_top20": [
            {"exceptional_mass": e, "curve_group_mass": a, "models": n}
            for (e, a), n in parent_hist.most_common(20)
        ],
        "sample_models": sample,
        "interpretation": {
            "exhaustive_numerical_row_if_terminal_unsat": terminal == "EXHAUSTED_UNSAT",
            "otherwise_exact_prefix_only": terminal != "EXHAUSTED_UNSAT",
            "purpose": "TEST_WHETHER_D16_CAN_BYPASS_D8_STYLE_10E17_BRANCH_MATERIALIZATION",
        },
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = csha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "terminal": terminal,
        "models": models,
        "seconds": round(elapsed, 3),
        "norm_histogram": dict(sorted(norm_hist.items())),
        "parent_count_seen": len(parent_hist),
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
