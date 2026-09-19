#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
PREFIX = HERE / "verify_fibration_nef_picard_prefix_composition_preflight.py"
PREFIX_BLOB = "7f0cfae30b2e081f9579d68bd4e80c1e57f94f6a"


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
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@dataclass
class ExistStats:
    visited_nodes: int = 0
    sum_prunes: int = 0
    quadratic_prunes: int = 0
    lattice_prefix_prunes: int = 0
    lattice_leaf_prunes: int = 0
    leaves: int = 0


def picard_exists(prefix_mod, leaf, bnb, kernel, problem: dict, cert: dict, *, x: tuple[int, ...], e: int, d: int):
    """Exact existential version of the retained Picard-prefix B&B.

    Traversal order and every pruning predicate are identical to the count-all
    consumer.  The only semantic change is safe early termination at the first
    accepted complete residual vector.
    """
    if problem.get("structurally_infeasible"):
        return False, None, ExistStats()
    caps = tuple(int(v) for v in problem["caps"])
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    mu, budget = problem["mu"], problem["penalty_budget"]
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    suffix_caps = [0] * (prefix_mod.RESIDUAL_DIM + 1)
    for i in range(prefix_mod.RESIDUAL_DIM - 1, -1, -1):
        suffix_caps[i] = suffix_caps[i + 1] + caps[i]
    static_values = leaf.td02_aggregate_from_x(x) + (e, d)
    req(len(static_values) == prefix_mod.STATIC_WIDTH, "static TD02/Picard observable regression")
    syndrome_suffix = prefix_mod.suffix_syndrome_sets(cert, caps)
    stats = ExistStats()
    first = None

    def rec(pfx: tuple[int, ...], total: int) -> bool:
        nonlocal first
        stats.visited_nodes += 1
        depth = len(pfx)
        if total > sum_hi or total + suffix_caps[depth] < sum_lo:
            stats.sum_prunes += 1
            return False
        if bnb.quadratic_lower(pfx, mu, lowers) > budget:
            stats.quadratic_prunes += 1
            return False
        lattice_ok = prefix_mod.prefix_picard_extendable(cert, static_values, pfx, syndrome_suffix)
        if depth == prefix_mod.RESIDUAL_DIM:
            direct = leaf.is_picard_extendable(cert, leaf.observable_vector(x=x, e=e, d=d, r=pfx))
            req(lattice_ok == direct, "prefix/leaf Picard oracle mismatch")
            stats.leaves += 1
            if not lattice_ok:
                stats.lattice_leaf_prunes += 1
                return False
            if not (sum_lo <= total <= sum_hi):
                return False
            delta = Matrix([Rational(pfx[i]) - mu[i, 0] for i in range(prefix_mod.RESIDUAL_DIM)])
            if bnb.eval_quad(kernel.penalty, delta) > budget:
                return False
            first = pfx
            return True
        if not lattice_ok:
            stats.lattice_prefix_prunes += 1
            return False
        rem_after = suffix_caps[depth + 1]
        lo = max(0, sum_lo - total - rem_after)
        hi = min(caps[depth], sum_hi - total)
        if lo > hi:
            stats.sum_prunes += 1
            return False
        values = list(range(lo, hi + 1))
        values.sort(key=lambda v: (abs(Rational(v) - mu[depth, 0]), v))
        for value in values:
            if rec(pfx + (value,), total + value):
                return True
        return False

    exists = rec((), 0)
    return exists, first, stats


def main() -> None:
    req(PREFIX.is_file(), "missing Picard-prefix carrier")
    req(git_blob(PREFIX) == PREFIX_BLOB, "Picard-prefix carrier drift")
    prefix = load_module(PREFIX, "stage32_178_picard_prefix_existential_carrier")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_picard_leaf_existential_carrier")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_picard_existential_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_picard_existential_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    cases = 0
    strict_early_exit = 0
    for d in (8, 10, 12):
        for e in range(0, d + 1, 2):
            for x4 in range(0, min(3, d // 2) + 1):
                x = (0, 0, 0, 0, x4, 0, 0, 0, 0, 0, 0)
                problem = bnb.residual_problem(kernel, g=0, d=d, e=e, x=x)
                count, first_count, count_stats = prefix.bnb_count_with_picard_prefix(
                    leaf, bnb, kernel, problem, cert, x=x, e=e, d=d
                )
                exists, first_exists, exist_stats = picard_exists(
                    prefix, leaf, bnb, kernel, problem, cert, x=x, e=e, d=d
                )
                req(exists == (count > 0), f"existence/count mismatch d={d} e={e} x4={x4}")
                req(first_exists == first_count, f"first-witness mismatch d={d} e={e} x4={x4}")
                req(exist_stats.visited_nodes <= count_stats.visited_nodes,
                    f"existential search enlarged tree d={d} e={e} x4={x4}")
                if exists and exist_stats.visited_nodes < count_stats.visited_nodes:
                    strict_early_exit += 1
                cases += 1

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_PICARD_EXISTENTIAL_PREFLIGHT_V1",
        "purpose": "replace count-all by an exact first-witness existential consumer for Stage32 elimination decisions",
        "bounded_exact_regression_cases": cases,
        "existence_matches_count_positive": True,
        "first_witness_matches_count_all": True,
        "visited_nodes_never_increased": True,
        "strict_early_exit_cases": strict_early_exit,
        "production_semantics": {
            "elimination_requires_only_existence": True,
            "accepted_leaf_predicate_changed": False,
            "prefix_pruning_predicate_changed": False,
            "quadratic_pruning_predicate_changed": False,
            "search_order_changed": False,
            "count_all_required": False,
        },
        "next_exact_step": "attach this existential consumer to deterministic real-production terminal panels, then aggregate terminal masses by the compact signature proved by the companion factorization verifier",
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("PICARD_EXISTENTIAL_SUMMARY=" + json.dumps({
        "cases": cases,
        "strict_early_exit_cases": strict_early_exit,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
