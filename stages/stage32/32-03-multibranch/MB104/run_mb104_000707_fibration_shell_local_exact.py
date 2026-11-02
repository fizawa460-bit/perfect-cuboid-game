#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Int, Or, SolverFor, get_version_string, sat, unknown, unsat

import run_mb104_000707_fibration_isotropic_shells as retained

SCHEMA = "STAGE32_MB104_000707_FIBRATION_SHELL_LOCAL_EXACT_SHARD_V1"
SHARD_COUNT = 8
RETAINED_RUNNER_BLOB = "cae7d170990128bbf1a80ed840b4c0b4a2b84cd4"
HERE = Path(__file__).resolve().parent
RUNKEY = HERE / "runkeys" / "000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"


def certificate_source_locks() -> dict:
    k = json.loads(RUNKEY.read_text(encoding="utf-8"))
    sl = k["source_locks"]
    _, _, _, _, meta = retained.load_retained_numeric()
    return {
        "execution_surface_generation": int(k["generation"]),
        "retained_runner_git_blob": sl["runner_git_blob"],
        "local_exact_engine_git_blob": sl["local_exact_engine_git_blob"],
        "local_exact_shard_verifier_git_blob": sl["local_exact_shard_verifier_git_blob"],
        "local_exact_aggregate_git_blob": sl["local_exact_aggregate_git_blob"],
        "workflow_git_blob": sl["workflow_git_blob"],
        "stoll_cuboids_blob": sl["stoll_cuboids_blob"],
        "stage33_stoll_helper_blob": sl["stage33_stoll_helper_blob"],
        "stage33_picard_marking_blob": sl["stage33_picard_marking_blob"],
        "stage33_picard_base_rows_blob": sl["stage33_picard_base_rows_blob"],
        "hperp_integral_adapter_blob": sl["hperp_integral_adapter_blob"],
        "pairing_prefix_engine_blob": sl["pairing_prefix_engine_blob"],
        "retained_hperp_text_sha256": meta["hperp_text_sha256"],
        "retained_picard_base_canonical": meta["picard_base_canonical"],
    }


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def gcd_all(values: list[int]) -> int:
    g = 0
    for value in values:
        g = math.gcd(g, abs(int(value)))
    return g


def exact_ldl_positive(q: list[list[int]]) -> list[Fraction]:
    n = len(q)
    if n == 0 or any(len(row) != n for row in q):
        raise ValueError("H-perp Gram shape")
    if any(q[i][j] != q[j][i] for i in range(n) for j in range(n)):
        raise ValueError("H-perp Gram symmetry")
    L = [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]
    d: list[Fraction] = []
    for i in range(n):
        L[i][i] = Fraction(1, 1)
        di = Fraction(q[i][i], 1) - sum(L[i][k] * L[i][k] * d[k] for k in range(i))
        if di <= 0:
            raise ValueError(f"H-perp Gram is not positive definite at pivot {i}")
        d.append(di)
        for j in range(i + 1, n):
            num = Fraction(q[j][i], 1) - sum(L[j][k] * L[i][k] * d[k] for k in range(i))
            L[j][i] = num / di
    return d


def exact_coordinate_bounds(q: list[list[int]], norm: int) -> tuple[list[tuple[int, int]], str]:
    exact_ldl_positive(q)
    qi = Matrix(q).inv()
    bounds: list[tuple[int, int]] = []
    dual_diag_payload: list[list[int]] = []
    for j in range(len(q)):
        a = frac(qi[j, j])
        if a <= 0:
            raise ValueError("nonpositive dual diagonal")
        p, den = a.numerator, a.denominator
        b = math.isqrt((norm * p) // den)
        if b * b * den > norm * p or (b + 1) * (b + 1) * den <= norm * p:
            raise ValueError("dual coordinate-bound arithmetic")
        bounds.append((-b, b))
        dual_diag_payload.append([p, den])
    return bounds, csha(dual_diag_payload)


def support_rows_0based() -> list[int]:
    return [91 + int(j) for j in retained.SUPPORT_STOLL]


def shell_data(shell_index: int) -> dict:
    if not 0 <= shell_index < len(retained.SHELLS):
        raise ValueError("shell index")
    return dict(retained.SHELLS[shell_index])


def split_contract(shell_index: int, shard_count: int = SHARD_COUNT) -> dict:
    if shard_count < 1:
        raise ValueError("shard count")
    q, degree, linear, gram, meta = retained.load_retained_numeric()
    sh = shell_data(shell_index)
    bounds, dual_sha = exact_coordinate_bounds(q, int(sh["hperp_norm"]))
    domains = [hi - lo + 1 for lo, hi in bounds]
    candidates = [j for j, n in enumerate(domains) if n > 1]
    if not candidates:
        split_j = 0
    else:
        split_j = min(
            candidates,
            key=lambda j: (
                domains[j],
                -sum(abs(int(linear[r][j])) for r in range(140)),
                j,
            ),
        )
    lo, hi = bounds[split_j]
    n = hi - lo + 1
    intervals = []
    for r in range(shard_count):
        a = lo + (n * r) // shard_count
        b = lo + (n * (r + 1)) // shard_count - 1
        intervals.append([a, b])
    nonempty = [(a, b) for a, b in intervals if a <= b]
    if nonempty:
        if nonempty[0][0] != lo or nonempty[-1][1] != hi:
            raise ValueError("partition endpoint coverage")
        for left, right in zip(nonempty, nonempty[1:]):
            if left[1] + 1 != right[0]:
                raise ValueError("partition gap/overlap")
    return {
        "shell_index": shell_index,
        "shard_count": shard_count,
        "split_coordinate_0based": split_j,
        "split_coordinate_bound": [lo, hi],
        "coordinate_bounds": [[a, b] for a, b in bounds],
        "intervals": intervals,
        "coverage_is_exact_disjoint": True,
        "bound_method": "EXACT_DUAL_NORM_DIAGONAL_FROM_POSITIVE_DEFINITE_HPERP_GRAM",
        "dual_diagonal_sha256": dual_sha,
        "retained_hperp_text_sha256": meta["hperp_text_sha256"],
        "retained_picard_base_canonical": meta["picard_base_canonical"],
    }


def integrality_specs(gram: list[list[int]]) -> list[tuple[int, list[int]]]:
    inv = Matrix(gram).inv()
    specs: list[tuple[int, list[int]]] = []
    for k in range(64):
        coeff = [frac(inv[i, k]) for i in range(64)]
        D = 1
        for a in coeff:
            D = math.lcm(D, a.denominator)
        nums = [int(a * D) for a in coeff]
        g = D
        for v in nums:
            g = math.gcd(g, abs(v))
        if g > 1:
            D //= g
            nums = [v // g for v in nums]
        specs.append((D, nums))
    return specs


def problem_payload(shell_index: int, shard_count: int = SHARD_COUNT) -> dict:
    q, degree, linear, gram, meta = retained.load_retained_numeric()
    sh = shell_data(shell_index)
    aa, bb = int(sh["scale_a"]), int(sh["scale_b"])
    support_rows = support_rows_0based()
    prow = [-4 * sum(int(linear[r][j]) for r in support_rows) for j in range(63)]
    pc = aa * int(sh["p_intersection"]) - bb * 112
    contract = split_contract(shell_index, shard_count)
    return {
        "q": q,
        "degree": [int(v) for v in degree],
        "linear": [[int(v) for v in row] for row in linear],
        "gram": [[int(v) for v in row] for row in gram],
        "shell": sh,
        "prow": prow,
        "pc": pc,
        "support_rows": support_rows,
        "contract": contract,
        "integrality_specs": integrality_specs(gram),
        "meta": meta,
    }


def build_solver(shell_index: int, shard_residue: int, *, shard_count: int = SHARD_COUNT, timeout_ms: int = 300000):
    if not 0 <= shard_residue < shard_count:
        raise ValueError("shard residue")
    p = problem_payload(shell_index, shard_count)
    sh = p["shell"]
    aa, bb = int(sh["scale_a"]), int(sh["scale_b"])
    x = [Int(f"x_{j}") for j in range(63)]
    y = [Int(f"y_{r}") for r in range(140)]
    f = [Int(f"f_{j}") for j in range(64)]
    solver = SolverFor("QF_NIA")
    solver.set(timeout=timeout_ms)
    solver.set(random_seed=0)

    for j, (lo, hi) in enumerate(p["contract"]["coordinate_bounds"]):
        solver.add(x[j] >= int(lo), x[j] <= int(hi))

    q = p["q"]
    norm_expr = sum(int(q[i][i]) * x[i] * x[i] for i in range(63))
    norm_expr += 2 * sum(int(q[i][j]) * x[i] * x[j] for i in range(63) for j in range(i + 1, 63))
    solver.add(norm_expr == int(sh["hperp_norm"]))
    solver.add(sum(int(p["prow"][j]) * x[j] for j in range(63)) == int(p["pc"]))

    for r in range(140):
        rhs = sum(int(p["linear"][r][j]) * x[j] for j in range(63)) + bb * int(p["degree"][r])
        solver.add(aa * y[r] == rhs)
        solver.add(y[r] >= 0)

    solver.add(sum(y[r] for r in p["support_rows"]) == int(sh["support_mass"]))

    labels = [int(v) - 1 for v in retained.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    for k, (D, nums) in enumerate(p["integrality_specs"]):
        expr = sum(int(nums[i]) * y[labels[i]] for i in range(64))
        solver.add(D * f[k] == expr)

    split_j = int(p["contract"]["split_coordinate_0based"])
    a, b = p["contract"]["intervals"][shard_residue]
    if a <= b:
        solver.add(x[split_j] >= int(a), x[split_j] <= int(b))
    else:
        solver.add(False)
    return solver, x, y, f, p


def replay_solution(shell_index: int, xvals: list[int]) -> dict:
    p = problem_payload(shell_index)
    if len(xvals) != 63:
        raise ValueError("H-perp coordinate length")
    for value, (lo, hi) in zip(xvals, p["contract"]["coordinate_bounds"]):
        if not int(lo) <= int(value) <= int(hi):
            raise ValueError("coordinate bound replay")
    q = p["q"]
    norm = sum(int(xvals[i]) * int(q[i][j]) * int(xvals[j]) for i in range(63) for j in range(63))
    if norm != int(p["shell"]["hperp_norm"]):
        raise ValueError("norm replay")
    pairing = sum(int(p["prow"][j]) * int(xvals[j]) for j in range(63))
    if pairing != int(p["pc"]):
        raise ValueError("P-pairing replay")

    aa, bb = int(p["shell"]["scale_a"]), int(p["shell"]["scale_b"])
    allpairs = []
    for r in range(140):
        num = sum(int(p["linear"][r][j]) * int(xvals[j]) for j in range(63)) + bb * int(p["degree"][r])
        if num % aa:
            raise ValueError("Picard divisibility replay")
        value = num // aa
        if value < 0:
            raise ValueError("known140 nonnegative replay")
        allpairs.append(value)
    if sum(allpairs[r] for r in p["support_rows"]) != int(p["shell"]["support_mass"]):
        raise ValueError("support mass replay")

    labels = [int(v) - 1 for v in retained.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    bp = Matrix([[allpairs[i] for i in labels]])
    frow = bp * Matrix(p["gram"]).inv()
    if any(frac(v).denominator != 1 for v in frow):
        raise ValueError("Picard64 integrality replay")
    fseq = [int(v) for v in frow]
    g = Matrix(p["gram"])
    fsq = int((Matrix([fseq]) * g * Matrix(fseq))[0])
    if fsq != 0:
        raise ValueError("isotropic Picard class replay")
    primitive = gcd_all(fseq) == 1
    return {
        "x_hperp_coordinates": [int(v) for v in xvals],
        "picard_basis_coordinates": fseq,
        "minimum_known140_pairing": min(allpairs),
        "zero_known140_indices_1based": [i + 1 for i, v in enumerate(allpairs) if v == 0],
        "primitive": primitive,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shell-index", type=int, required=True, choices=range(4))
    ap.add_argument("--shard-count", type=int, default=SHARD_COUNT)
    ap.add_argument("--shard-residue", type=int, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=300000)
    ap.add_argument("--wall-seconds", type=int, default=2400)
    ap.add_argument("--model-cap", type=int, default=10000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    solver, x, y, f, p = build_solver(
        args.shell_index,
        args.shard_residue,
        shard_count=args.shard_count,
        timeout_ms=args.solver_timeout_ms,
    )

    models = 0
    primitive = []
    status = "PARTIAL_NOT_STARTED"
    reason = None
    final_solver_result = None
    checks = 0
    while True:
        if time.monotonic() - started >= args.wall_seconds:
            status = "PARTIAL_WALL_NO_CREDIT"
            reason = "local wall reached before exhaustive UNSAT"
            break
        if models >= args.model_cap:
            status = "PARTIAL_MODEL_CAP_NO_CREDIT"
            reason = "model cap reached before exhaustive UNSAT"
            break
        checks += 1
        res = solver.check()
        if res == unsat:
            status = "COMPLETE_EXACT_SHARD_ZERO_CREDIT"
            final_solver_result = "unsat"
            break
        if res == unknown:
            status = "PARTIAL_UNKNOWN_NO_CREDIT"
            final_solver_result = "unknown"
            reason = solver.reason_unknown()
            break
        if res != sat:
            raise RuntimeError(f"unexpected Z3 result: {res}")
        model = solver.model()
        xv = [int(model.eval(v, model_completion=True).as_long()) for v in x]
        rec = replay_solution(args.shell_index, xv)
        fv = [int(model.eval(v, model_completion=True).as_long()) for v in f]
        if fv != rec["picard_basis_coordinates"]:
            raise ValueError("solver/replay Picard coordinate mismatch")
        models += 1
        if rec["primitive"]:
            primitive.append(rec)
        solver.add(Or(*[x[j] != xv[j] for j in range(63)]))

    primitive.sort(key=lambda rec: tuple(rec["picard_basis_coordinates"]))
    contract = p["contract"]
    interval = contract["intervals"][args.shard_residue]
    split_j = int(contract["split_coordinate_0based"])
    for rec in primitive:
        v = int(rec["x_hperp_coordinates"][split_j])
        if not (interval[0] <= v <= interval[1]):
            raise ValueError("candidate escaped shard interval")

    out = {
        "schema": SCHEMA,
        "status": status,
        "shell_index": args.shell_index,
        "source_locks": certificate_source_locks(),
        "solver": {
            "engine": "Z3_QF_NIA",
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "wall_seconds": args.wall_seconds,
            "model_cap": args.model_cap,
            "solver_checks": checks,
            "final_solver_result": final_solver_result,
            "reason": reason,
            "floating_point_used": False,
        },
        "partition": {
            **contract,
            "shard_residue": args.shard_residue,
            "shard_interval": interval,
        },
        "mathematical_scope": {
            "support_mask": retained.SUPPORT["mask"],
            "degree": int(p["shell"]["degree"]),
            "p_intersection": int(p["shell"]["p_intersection"]),
            "support_mass": int(p["shell"]["support_mass"]),
            "hperp_norm": int(p["shell"]["hperp_norm"]),
            "hperp_p_pairing": int(p["pc"]),
            "direct_constraints": [
                "exact positive-definite H-perp norm equality",
                "exact fixed P pairing",
                "all140 nonnegative integral pairings under x=aF-bH",
                "exact support mass",
                "exact retained Picard64 integrality",
            ],
        },
        "result": {
            "complete": status == "COMPLETE_EXACT_SHARD_ZERO_CREDIT",
            "integral_known140_nonnegative_solution_count": models,
            "primitive_known140_nonnegative_candidate_count": len(primitive),
            "primitive_known140_nonnegative_candidates": primitive,
        },
        "credit_firewall": {
            "numerical_fibration_shell_credit": False,
            "effectivity_credit": False,
            "semiampleness_credit": False,
            "global_fibration_optimum_credit": False,
            "MB104_complete": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": status,
        "shell_index": args.shell_index,
        "shard_residue": args.shard_residue,
        "models": models,
        "primitive_candidates": len(primitive),
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    raise SystemExit(0 if status == "COMPLETE_EXACT_SHARD_ZERO_CREDIT" else 2)


if __name__ == "__main__":
    main()
