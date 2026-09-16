#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import sympy
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
ST33 = ROOT / "stages" / "stage33" / "33-07"
RECOVERABILITY = HERE / "verify_fibration_nef_recoverability.py"
AGGREGATE = HERE / "verify_five_residual_aggregate_hperp_preflight.py"
GRF04 = ROOT / "stages" / "stage32" / "32-01-178" / "topdown-02" / "TD02-GRF04-FULL178-AGGREGATE-CHECKPOINT.json"
EX6 = ROOT / "stages" / "stage32-ex6" / "diagnose_stage32_ex6_rank4_fibration_orbit.py"

ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)
EXTRA_LOCKS = {
    "five_residual_aggregate_preflight": (AGGREGATE, "ea8d78ca26cbe38561606e8e71f43a40ece2f485"),
    "td02_grf04_full178_checkpoint": (GRF04, "4e2ccf5f9f8d25f117e4e9792d3b54ec31a0799b"),
    "rank4_fibration_source_lock_carrier": (EX6, "fac8b2c3eb673e19f2952b63c3e201aade82edd5"),
}
STOLL_TESTA_SECTION5_LOG_BLOB = "9cfef75aa58335655d6ae3e78597f5924b6c2433"
EXPECTED_SUPPORTS = (
    (100,),
    (104, 105, 106, 107, 108),
    (109, 110, 111, 112, 113, 114, 115, 116),
    (117, 118, 119, 120, 121, 122, 123, 124),
    (125, 126, 127, 128, 129, 130, 131, 132),
)


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@dataclass(frozen=True)
class Kernel:
    blocks: tuple[tuple[int, ...], ...]
    observed_exceptionals: tuple[int, ...]
    residual_supports: tuple[tuple[int, ...], ...]
    x_degrees: tuple[int, ...]
    r_degrees: tuple[int, ...]
    old_norm_matrix: Matrix
    center: Matrix
    penalty: Matrix


@dataclass
class Stats:
    visited_nodes: int = 0
    sum_prunes: int = 0
    quadratic_prunes: int = 0
    leaves: int = 0


def lock_extra_sources() -> None:
    for name, (path, expected) in EXTRA_LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")
    req(STOLL_TESTA_SECTION5_LOG_BLOB in EX6.read_text(), "Stoll-Testa Section5 source-lock regression")


def build_kernel(vf) -> Kernel:
    blocks, _ = vf.recover_unordered_fibration_blocks()
    observed = tuple(sorted(x for x in vf.ASSIGNMENT_LABELS if x >= 93))
    residual_supports = tuple(tuple(sorted(set(block) - set(observed))) for block in blocks)
    req(residual_supports[:5] == EXPECTED_SUPPORTS, "five residual support regression")
    req(len(residual_supports) == 6 and all(residual_supports), "six residual supports must be nonempty")

    sys.path.insert(0, str(RES))
    from hperp_integral_adapter import _parse_hperp  # noqa: E402

    marking = vf.load_retained(ST33 / "stage32_picard_marking_retained.py", "bnb_marking")
    q, degree, linear, _caps, _meta = _parse_hperp(marking["hperp_text"])
    x_rows = linear.extract([lab - 1 for lab in ASSIGNMENT], list(range(63)))
    r_rows = []
    for support in residual_supports[:5]:
        row = Matrix([[0] * 63])
        for lab in support:
            row += linear.row(lab - 1)
        r_rows.append(row)
    a = Matrix.vstack(x_rows, *r_rows)
    req(int(x_rows.rank()) == 11 and int(a.rank()) == 16, "Hperp rank regression")

    s = sympy.simplify(a * q.inv() * a.T)
    sxx, sxr = s[:11, :11], s[:11, 11:]
    srx, srr = s[11:, :11], s[11:, 11:]
    old_norm = sympy.simplify(sxx.inv())
    center = sympy.simplify(srx * old_norm)
    schur = sympy.simplify(srr - srx * old_norm * sxr)
    penalty = sympy.simplify(schur.inv())
    req(penalty == penalty.T, "penalty symmetry regression")
    req(all(sympy.factor(penalty[:k, :k].det()) > 0 for k in range(1, 6)), "penalty positive-definite regression")

    x_degrees = tuple(int(degree[lab - 1, 0]) for lab in ASSIGNMENT)
    r_degrees = tuple(sum(int(degree[lab - 1, 0]) for lab in support) for support in residual_supports[:5])
    req(x_degrees == (0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0), "existing degree regression")

    # Symbolic identity, not a numerical sample:
    # min_Hperp(x) = q/2 + (d/2 - 2*x4 - t)^2/12.
    xs = sympy.symbols("x0:11")
    dsym = sympy.symbols("d")
    zx = Matrix([xs[i] - dsym * Rational(x_degrees[i], 16) for i in range(11)])
    matrix_rho = sympy.expand((zx.T * old_norm * zx)[0])
    qexc = sum(xs[i] ** 2 for i in range(11) if i != 4)
    t = xs[0] + xs[1] + xs[6] + xs[9]
    closed_rho = Rational(1, 2) * qexc + Rational(1, 12) * (dsym * Rational(1, 2) - 2 * xs[4] - t) ** 2
    req(sympy.simplify(matrix_rho - closed_rho) == 0, "GRF04/Hperp symbolic identity regression")

    grf = json.loads(GRF04.read_text())
    req(grf["mathematical_adapter"]["rho"] == "q/2 + (d/2 - 2*x4 - t)^2/12", "GRF04 rho authority regression")
    req(grf["mathematical_adapter"]["t"] == "x0+x1+x6+x9", "GRF04 t authority regression")
    return Kernel(tuple(tuple(x) for x in blocks), observed, residual_supports, x_degrees, r_degrees, old_norm, center, penalty)


def eval_quad(m: Matrix, v: Matrix) -> sympy.Expr:
    return sympy.factor((v.T * m * v)[0])


def prefix_lower_matrices(q: Matrix) -> list[Matrix]:
    out = [Matrix.zeros(0, 0)]
    for depth in range(1, q.rows + 1):
        aa = q[:depth, :depth]
        if depth == q.rows:
            out.append(aa)
        else:
            af, ff = q[:depth, depth:], q[depth:, depth:]
            out.append(sympy.simplify(aa - af * ff.inv() * af.T))
    return out


def quadratic_lower(prefix: tuple[int, ...], mu: Matrix, lowers: list[Matrix]) -> sympy.Expr:
    if not prefix:
        return Rational(0)
    delta = Matrix([Rational(prefix[i]) - mu[i, 0] for i in range(len(prefix))])
    return eval_quad(lowers[len(prefix)], delta)


def residual_problem(kernel: Kernel, *, g: int, d: int, e: int, x: tuple[int, ...]) -> dict:
    req(g in (0, 1), "g must be 0 or 1")
    req(d >= 0 and e >= 0 and len(x) == 11 and all(v >= 0 for v in x), "invalid terminal coordinates")
    pos = {lab: i for i, lab in enumerate(ASSIGNMENT)}
    observed = set(kernel.observed_exceptionals)
    m10 = sum(x[pos[lab]] for lab in observed)
    remaining = e - m10
    if remaining < 0:
        return {"structurally_infeasible": True, "reason": "e_minus_M10_negative"}

    known = tuple(sum(x[pos[lab]] for lab in block if lab in observed) for block in kernel.blocks)
    req(sum(known) == m10, "observed block-mass partition regression")
    caps = []
    for i in range(5):
        if d - known[i] < 0:
            return {"structurally_infeasible": True, "reason": f"nef_block_{i}_already_negative"}
        caps.append(min(remaining, d - known[i]))
    if d - known[5] < 0:
        return {"structurally_infeasible": True, "reason": "nef_block_5_already_negative"}
    sum_lo = max(0, remaining - (d - known[5]))
    sum_hi = remaining
    if sum(caps) < sum_lo:
        return {"structurally_infeasible": True, "reason": "nef_simplex_empty"}

    zx = Matrix([Rational(x[i]) - Rational(d * kernel.x_degrees[i], 16) for i in range(11)])
    old_rho = eval_quad(kernel.old_norm_matrix, zx)
    qexc = sum(x[i] * x[i] for i in range(11) if i != 4)
    t = x[0] + x[1] + x[6] + x[9]
    closed_rho = Rational(qexc, 2) + Rational(1, 12) * (Rational(d, 2) - 2 * x[4] - t) ** 2
    req(sympy.simplify(old_rho - closed_rho) == 0, "terminal GRF04/Hperp identity regression")
    genus_budget = Rational(d * d, 16) + d + 2 - 2 * g
    penalty_budget = sympy.factor(genus_budget - old_rho)
    if penalty_budget < 0:
        return {"structurally_infeasible": True, "reason": "already_rejected_by_GRF04"}
    center_shift = kernel.center * zx
    mu = Matrix([Rational(d * kernel.r_degrees[i], 16) + center_shift[i, 0] for i in range(5)])
    return {
        "structurally_infeasible": False,
        "m10": m10,
        "remaining": remaining,
        "known_block_masses": known,
        "caps": tuple(caps),
        "sum_lo": sum_lo,
        "sum_hi": sum_hi,
        "old_rho": old_rho,
        "genus_budget": genus_budget,
        "penalty_budget": penalty_budget,
        "mu": mu,
    }


def bnb_count(kernel: Kernel, problem: dict, *, stop_after_one: bool = False) -> tuple[int, tuple[int, ...] | None, Stats]:
    if problem.get("structurally_infeasible"):
        return 0, None, Stats()
    caps = problem["caps"]
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    mu, budget = problem["mu"], problem["penalty_budget"]
    lowers = prefix_lower_matrices(kernel.penalty)
    suffix_caps = [0] * 6
    for i in range(4, -1, -1):
        suffix_caps[i] = suffix_caps[i + 1] + caps[i]
    stats, first, count = Stats(), None, 0

    def rec(prefix: tuple[int, ...], total: int) -> bool:
        nonlocal first, count
        stats.visited_nodes += 1
        depth = len(prefix)
        if total > sum_hi or total + suffix_caps[depth] < sum_lo:
            stats.sum_prunes += 1
            return False
        if quadratic_lower(prefix, mu, lowers) > budget:
            stats.quadratic_prunes += 1
            return False
        if depth == 5:
            stats.leaves += 1
            if not (sum_lo <= total <= sum_hi):
                return False
            delta = Matrix([Rational(prefix[i]) - mu[i, 0] for i in range(5)])
            if eval_quad(kernel.penalty, delta) > budget:
                return False
            count += 1
            if first is None:
                first = prefix
            return stop_after_one

        rem_after = suffix_caps[depth + 1]
        lo = max(0, sum_lo - total - rem_after)
        hi = min(caps[depth], sum_hi - total)
        if lo > hi:
            stats.sum_prunes += 1
            return False
        values = list(range(lo, hi + 1))
        values.sort(key=lambda v: (abs(Rational(v) - mu[depth, 0]), v))
        for v in values:
            if rec(prefix + (v,), total + v):
                return True
        return False

    rec((), 0)
    return count, first, stats


def brute_count(kernel: Kernel, problem: dict) -> int:
    if problem.get("structurally_infeasible"):
        return 0
    count = 0
    for r in itertools.product(*(range(c + 1) for c in problem["caps"])):
        if not (problem["sum_lo"] <= sum(r) <= problem["sum_hi"]):
            continue
        delta = Matrix([Rational(r[i]) - problem["mu"][i, 0] for i in range(5)])
        if eval_quad(kernel.penalty, delta) <= problem["penalty_budget"]:
            count += 1
    return count


def main() -> None:
    lock_extra_sources()
    vf = load_module(RECOVERABILITY, "bnb_fibration_recoverability")
    vf.lock_sources()
    req(tuple(vf.ASSIGNMENT_LABELS) == ASSIGNMENT, "assignment order regression")
    semantics = vf.audited_total_exceptional_semantics()
    req(semantics["E_total_pairing_value_in_each_stratum"] == "e", "N220 E_total semantics regression")
    kernel = build_kernel(vf)

    regressions = []
    for e in (0, 2, 4, 6, 8):
        problem = residual_problem(kernel, g=0, d=8, e=e, x=(0,) * 11)
        bcount, witness, stats = bnb_count(kernel, problem)
        rcount = brute_count(kernel, problem)
        req(bcount == rcount, f"B&B/brute count mismatch e={e}: {bcount} != {rcount}")
        one_count, one_witness, _ = bnb_count(kernel, problem, stop_after_one=True)
        req((one_count > 0) == (bcount > 0), f"stop-after-one mismatch e={e}")
        req((witness is None) == (bcount == 0) and (one_witness is None) == (bcount == 0), f"witness mismatch e={e}")
        regressions.append({
            "g": 0, "d": 8, "e": e,
            "bnb_feasible_aggregate_vectors": bcount,
            "brute_feasible_aggregate_vectors": rcount,
            "bnb_visited_nodes": stats.visited_nodes,
            "bnb_sum_prunes": stats.sum_prunes,
            "bnb_quadratic_prunes": stats.quadratic_prunes,
        })

    print(json.dumps({
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_BRANCH_AND_BOUND_PREFLIGHT_V1",
        "purpose": "exact five-residual aggregate feasibility engine combining N220 mass, six rank-3 fibration-nef inequalities, and retained GRF04/Hperp completion budget; no production census",
        "source_authority": {
            "N220_total_exceptional_pairing": "sum_{E93..E140}<D,E>=e",
            "rank3_fibration_normalization": "2F_Q = H - sum_{P in B_Q} E_P",
            "rank3_fibration_nef_test": "<D,2F_Q>=d-B_Q >= 0",
            "stoll_testa_section5_log_blob": STOLL_TESTA_SECTION5_LOG_BLOB,
            "grf04_rho": "q/2 + (d/2 - 2*x4 - t)^2/12",
            "grf04_genus_budget": "rho <= d^2/16 + d + 2 - 2g",
        },
        "exact_residual_projection": {
            "R": "e-M10",
            "r0_through_r4": "nonnegative integer residual masses of canonical fibration blocks 0..4",
            "r5": "R-sum(r0..r4)",
            "nef": "known_block_mass_i + r_i <= d for all six blocks",
            "individual_residual_node_assignments_expanded": False,
        },
        "quadratic_bridge": {
            "old_GRF04_equals_existing_11_coordinate_Hperp_minimum": True,
            "new_minimum": "rho + (r-mu)^T*T^{-1}*(r-mu)",
            "continuous_free_suffix_schur_lower_bound_used_for_pruning": True,
            "exact_rational_arithmetic": True,
            "picard_integral_lattice_constraints_dropped_in_this_relaxation": True,
            "dropping_lattice_constraints_is_safe_for_rejection": True,
        },
        "solver": {
            "dimension": 5,
            "method": "depth-first exact branch-and-bound over aggregate simplex; exact Schur lower bound at every prefix",
            "stop_after_first_extension_supported": True,
            "full_fivefold_cartesian_production_enumeration_required": False,
        },
        "regression": {"panels": regressions, "all_bnb_counts_match_independent_bruteforce": True},
        "production_domain_bridge_ready": True,
        "production_execution_armed": False,
        "bounded_violation_census_run": False,
        "full178_census_run": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "td02_additive_credit_claimed": False,
        "merge_authorized": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
