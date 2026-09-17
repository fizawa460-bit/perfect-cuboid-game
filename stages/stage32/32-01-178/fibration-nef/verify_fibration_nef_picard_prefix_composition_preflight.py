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
LEAF = HERE / "verify_fibration_nef_picard_leaf_composition_preflight.py"
LEAF_BLOB = "94fc641cbc47dc917ba9d0badcbfa06bd9f10e84"
OBSERVABLE_ORDER = ("a", "b", "c", "t", "x4", "e", "d", "r0", "r1", "r2", "r3", "r4")
STATIC_WIDTH = 7
RESIDUAL_DIM = 5


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


def lock_leaf_and_dependencies(leaf) -> None:
    # Lock the leaf-composition carrier before import, then lock every
    # load-bearing dependency it declares before executing any producer logic.
    req(LEAF.is_file(), "missing leaf-composition source")
    req(git_blob(LEAF) == LEAF_BLOB, "leaf-composition source drift")
    for name, (path, expected) in leaf.LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")


def suffix_syndrome_sets(cert: dict, caps: tuple[int, ...]) -> list[set[tuple[int, ...]]]:
    """Exact congruence syndromes attainable by suffix variables inside caps.

    Only residues matter.  For a coordinate 0 <= r_i <= cap_i, all residues
    0..q-1 occur once cap_i >= q-1; otherwise the attainable residues are
    exactly 0..cap_i.  The coupled syndrome tuple preserves all congruence
    rows simultaneously, so membership testing below is exact for the linear
    Picard congruences subject to the coordinate caps.
    """
    req(len(caps) == RESIDUAL_DIM, "residual cap dimension regression")
    q = int(cert["membership_modulus"])
    req(q >= 1, "invalid Picard membership modulus")
    rows = [tuple(int(c) % q for c in row) for row in cert["membership_coefficients_mod_q"]]
    req(all(len(row) == len(OBSERVABLE_ORDER) for row in rows), "congruence row width regression")
    m = len(rows)
    zero = tuple(0 for _ in range(m))
    suffix: list[set[tuple[int, ...]]] = [set() for _ in range(RESIDUAL_DIM + 1)]
    suffix[RESIDUAL_DIM] = {zero}
    if q == 1 or m == 0:
        for depth in range(RESIDUAL_DIM):
            suffix[depth] = {zero}
        return suffix

    for depth in range(RESIDUAL_DIM - 1, -1, -1):
        coeff = tuple(row[STATIC_WIDTH + depth] for row in rows)
        cap = int(caps[depth])
        req(cap >= 0, "negative residual cap")
        residues = range(q) if cap >= q - 1 else range(cap + 1)
        reachable: set[tuple[int, ...]] = set()
        for tail in suffix[depth + 1]:
            for residue in residues:
                reachable.add(tuple((tail[j] + residue * coeff[j]) % q for j in range(m)))
        suffix[depth] = reachable
    return suffix


def prefix_picard_extendable(
    cert: dict,
    static_values: tuple[int, ...],
    prefix: tuple[int, ...],
    suffix: list[set[tuple[int, ...]]],
) -> bool:
    req(len(static_values) == STATIC_WIDTH, "static observable width regression")
    req(len(prefix) <= RESIDUAL_DIM, "residual prefix too long")
    q = int(cert["membership_modulus"])
    if q == 1:
        return True
    rows = cert["membership_coefficients_mod_q"]
    if not rows:
        return True
    current = []
    for row in rows:
        value = sum(int(row[i]) * int(static_values[i]) for i in range(STATIC_WIDTH))
        value += sum(int(row[STATIC_WIDTH + j]) * int(prefix[j]) for j in range(len(prefix)))
        current.append(value % q)
    target = tuple((-value) % q for value in current)
    return target in suffix[len(prefix)]


@dataclass
class PrefixStats:
    visited_nodes: int = 0
    sum_prunes: int = 0
    quadratic_prunes: int = 0
    lattice_prefix_prunes: int = 0
    lattice_leaf_prunes: int = 0
    leaves: int = 0


def bnb_count_with_picard_prefix(leaf, bnb, kernel, problem: dict, cert: dict, *, x: tuple[int, ...], e: int, d: int):
    if problem.get("structurally_infeasible"):
        return 0, None, PrefixStats()
    caps = tuple(int(v) for v in problem["caps"])
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    mu, budget = problem["mu"], problem["penalty_budget"]
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    suffix_caps = [0] * (RESIDUAL_DIM + 1)
    for i in range(RESIDUAL_DIM - 1, -1, -1):
        suffix_caps[i] = suffix_caps[i + 1] + caps[i]
    static_values = leaf.td02_aggregate_from_x(x) + (e, d)
    req(len(static_values) == STATIC_WIDTH, "static TD02/Picard observable regression")
    syndrome_suffix = suffix_syndrome_sets(cert, caps)

    stats = PrefixStats()
    first = None
    count = 0

    def rec(prefix: tuple[int, ...], total: int) -> None:
        nonlocal first, count
        stats.visited_nodes += 1
        depth = len(prefix)
        if total > sum_hi or total + suffix_caps[depth] < sum_lo:
            stats.sum_prunes += 1
            return
        if bnb.quadratic_lower(prefix, mu, lowers) > budget:
            stats.quadratic_prunes += 1
            return

        lattice_ok = prefix_picard_extendable(cert, static_values, prefix, syndrome_suffix)
        if depth == RESIDUAL_DIM:
            # At a full leaf, suffix contribution is zero, hence the prefix
            # oracle must be identical to the existing exact leaf oracle.
            direct = leaf.is_picard_extendable(
                cert, leaf.observable_vector(x=x, e=e, d=d, r=prefix)
            )
            req(lattice_ok == direct, "prefix/leaf Picard oracle mismatch")
            stats.leaves += 1
            if not lattice_ok:
                stats.lattice_leaf_prunes += 1
                return
            if not (sum_lo <= total <= sum_hi):
                return
            delta = Matrix([Rational(prefix[i]) - mu[i, 0] for i in range(RESIDUAL_DIM)])
            if bnb.eval_quad(kernel.penalty, delta) > budget:
                return
            count += 1
            if first is None:
                first = prefix
            return

        if not lattice_ok:
            stats.lattice_prefix_prunes += 1
            return

        rem_after = suffix_caps[depth + 1]
        lo = max(0, sum_lo - total - rem_after)
        hi = min(caps[depth], sum_hi - total)
        if lo > hi:
            stats.sum_prunes += 1
            return
        values = list(range(lo, hi + 1))
        values.sort(key=lambda v: (abs(Rational(v) - mu[depth, 0]), v))
        for value in values:
            rec(prefix + (value,), total + value)

    rec((), 0)
    return count, first, stats


def main() -> None:
    # Importing the carrier itself executes no producer logic.  Its exact blob
    # is locked first; producer dependencies are then locked before use.
    req(LEAF.is_file(), "missing leaf-composition source")
    req(git_blob(LEAF) == LEAF_BLOB, "leaf-composition source drift")
    leaf = load_module(LEAF, "stage32_178_picard_leaf_prefix_carrier")
    lock_leaf_and_dependencies(leaf)

    cert = leaf.load_picard_certificate()
    req(tuple(cert["observable_order"]) == OBSERVABLE_ORDER, "Picard observable order regression")
    bnb = leaf.load_module(leaf.BNB, "stage32_178_fibration_bnb_picard_prefix")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_fibration_recoverability_picard_prefix")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    panels = []
    strict_examples = []
    total_leaf_nodes = 0
    total_prefix_nodes = 0
    total_prefix_prunes = 0

    # Same lightweight synthetic domain used by the retained leaf-composition
    # preflight.  This is deliberately not a FULL178 production census.
    for d in (8, 10, 12):
        for e in range(0, d + 1, 2):
            for x4 in range(0, min(3, d // 2) + 1):
                x = (0, 0, 0, 0, x4, 0, 0, 0, 0, 0, 0)
                problem = bnb.residual_problem(kernel, g=0, d=d, e=e, x=x)
                leaf_count, leaf_first, leaf_stats = leaf.bnb_count_with_picard(
                    bnb, kernel, problem, cert, x=x, e=e, d=d
                )
                prefix_count, prefix_first, prefix_stats = bnb_count_with_picard_prefix(
                    leaf, bnb, kernel, problem, cert, x=x, e=e, d=d
                )
                req(prefix_count == leaf_count,
                    f"prefix pruning changed accepted leaf count d={d} e={e} x4={x4}")
                req(prefix_first == leaf_first,
                    f"prefix pruning changed first accepted witness d={d} e={e} x4={x4}")
                req(prefix_stats.visited_nodes <= leaf_stats.visited_nodes,
                    f"prefix pruning enlarged search tree d={d} e={e} x4={x4}")

                item = {
                    "g": 0,
                    "d": d,
                    "e": e,
                    "x4": x4,
                    "accepted_residual_vectors": prefix_count,
                    "leaf_only_visited_nodes": leaf_stats.visited_nodes,
                    "prefix_pruned_visited_nodes": prefix_stats.visited_nodes,
                    "visited_node_reduction": leaf_stats.visited_nodes - prefix_stats.visited_nodes,
                    "exact_lattice_prefix_prunes": prefix_stats.lattice_prefix_prunes,
                    "exact_lattice_leaf_prunes": prefix_stats.lattice_leaf_prunes,
                }
                panels.append(item)
                total_leaf_nodes += leaf_stats.visited_nodes
                total_prefix_nodes += prefix_stats.visited_nodes
                total_prefix_prunes += prefix_stats.lattice_prefix_prunes
                if item["visited_node_reduction"] > 0 and len(strict_examples) < 8:
                    strict_examples.append(item)

    req(total_prefix_nodes <= total_leaf_nodes, "aggregate prefix pruning enlarged search tree")
    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_PICARD_PREFIX_COMPOSITION_PREFLIGHT_V1",
        "purpose": "move the retained exact Picard64 linear-lattice leaf oracle to a safe residual-prefix existential congruence test without changing accepted complete leaves; lightweight bounded preflight only",
        "observable_order": list(OBSERVABLE_ORDER),
        "picard_membership_modulus": int(cert["membership_modulus"]),
        "picard_active_congruence_rows": int(cert["active_congruence_rows"]),
        "prefix_rule": {
            "suffix_domain": "each unassigned residual coordinate ranges over its exact integer cap interval; only its exact residues modulo q are retained",
            "coupled_congruence_syndromes_preserved": True,
            "sum_and_quadratic_constraints_weakened_or_changed": False,
            "full_leaf_oracle_equivalence_asserted_at_every_visited_leaf": True,
            "accepted_complete_leaf_population_changed": False,
        },
        "bounded_synthetic_regression": {
            "panel_count": len(panels),
            "leaf_only_visited_nodes": total_leaf_nodes,
            "prefix_pruned_visited_nodes": total_prefix_nodes,
            "visited_node_reduction": total_leaf_nodes - total_prefix_nodes,
            "exact_lattice_prefix_prunes": total_prefix_prunes,
            "strict_node_reduction_found": bool(strict_examples),
            "strict_examples": strict_examples,
            "all_prefix_counts_and_first_witnesses_match_leaf_only_consumer": True,
        },
        "next_exact_step": "if strict_node_reduction_found, attach the same prefix oracle to an authorized FULL178 branch-and-bound consumer; production numerical pruning still requires the repository heavy-workflow authorization gate",
        "production_domain_bridge_ready": True,
        "production_execution_armed": False,
        "bounded_violation_census_run": False,
        "full178_census_run": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "td02_additive_credit_claimed": False,
        "merge": False,
    }
    print("PICARD_PREFIX_COMPOSITION_SUMMARY=" + json.dumps({
        "modulus": out["picard_membership_modulus"],
        "congruence_rows": out["picard_active_congruence_rows"],
        "panel_count": len(panels),
        "leaf_nodes": total_leaf_nodes,
        "prefix_nodes": total_prefix_nodes,
        "node_reduction": total_leaf_nodes - total_prefix_nodes,
        "prefix_prunes": total_prefix_prunes,
        "strict": bool(strict_examples),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
