#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
BNB = HERE / "verify_fibration_nef_branch_and_bound_preflight.py"
PICARD = HERE / "verify_fibration_nef_aggregate_picard_lattice_preflight.py"
LOCKS = {
    "branch_and_bound_preflight": (BNB, "6d4c79db4246b8b54cdc45bc6423f00d622740e6"),
    "aggregate_picard_lattice_preflight": (PICARD, "5fa9f1d67d6411cb550230b62398aff7bd6488ff"),
}
OBSERVABLE_ORDER = ("a", "b", "c", "t", "x4", "e", "d", "r0", "r1", "r2", "r3", "r4")


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


def load_picard_certificate() -> dict:
    proc = subprocess.run(
        [sys.executable, str(PICARD)],
        cwd=HERE,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(proc.stdout)
    req(payload["rule_is_exact_for_linear_picard_lattice_extendability"] is True,
        "Picard lattice producer lost exact linear-extendability semantics")
    cert = payload["full_observable_image_lattice"]
    req(tuple(cert["observable_order"]) == OBSERVABLE_ORDER,
        "Picard observable order regression")
    req(int(cert["rank"]) == len(OBSERVABLE_ORDER), "Picard observable rank regression")
    return cert


def td02_aggregate_from_x(x: tuple[int, ...]) -> tuple[int, int, int, int, int]:
    req(len(x) == 11, "TD02 assignment must have eleven coordinates")
    a = x[2] + x[3] + x[7]
    b = x[1] + x[5] + x[9]
    c = x[0] + x[6] + x[8] + x[10]
    t = x[0] + x[1] + x[6] + x[9]
    x4 = x[4]
    return a, b, c, t, x4


def observable_vector(*, x: tuple[int, ...], e: int, d: int, r: tuple[int, ...]) -> tuple[int, ...]:
    req(len(r) == 5, "residual leaf must have five coordinates")
    return td02_aggregate_from_x(x) + (e, d) + tuple(r)


def is_picard_extendable(cert: dict, values: tuple[int, ...]) -> bool:
    req(len(values) == len(OBSERVABLE_ORDER), "Picard observable vector length regression")
    modulus = int(cert["membership_modulus"])
    req(modulus >= 1, "invalid Picard membership modulus")
    if modulus == 1:
        return True
    for coeff in cert["membership_coefficients_mod_q"]:
        req(len(coeff) == len(values), "Picard membership coefficient length regression")
        if sum(int(c) * int(v) for c, v in zip(coeff, values)) % modulus:
            return False
    return True


@dataclass
class PicardStats:
    visited_nodes: int = 0
    sum_prunes: int = 0
    quadratic_prunes: int = 0
    lattice_leaf_prunes: int = 0
    leaves: int = 0


def bnb_count_with_picard(bnb, kernel, problem: dict, cert: dict, *, x: tuple[int, ...], e: int, d: int) -> tuple[int, tuple[int, ...] | None, PicardStats]:
    if problem.get("structurally_infeasible"):
        return 0, None, PicardStats()
    caps = problem["caps"]
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    mu, budget = problem["mu"], problem["penalty_budget"]
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    suffix_caps = [0] * 6
    for i in range(4, -1, -1):
        suffix_caps[i] = suffix_caps[i + 1] + caps[i]
    stats = PicardStats()
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
        if depth == 5:
            stats.leaves += 1
            if not (sum_lo <= total <= sum_hi):
                return
            delta = Matrix([Rational(prefix[i]) - mu[i, 0] for i in range(5)])
            if bnb.eval_quad(kernel.penalty, delta) > budget:
                return
            values = observable_vector(x=x, e=e, d=d, r=prefix)
            if not is_picard_extendable(cert, values):
                stats.lattice_leaf_prunes += 1
                return
            count += 1
            if first is None:
                first = prefix
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


def brute_count_with_picard(bnb, kernel, problem: dict, cert: dict, *, x: tuple[int, ...], e: int, d: int) -> int:
    if problem.get("structurally_infeasible"):
        return 0
    count = 0
    for r in itertools.product(*(range(c + 1) for c in problem["caps"])):
        if not (problem["sum_lo"] <= sum(r) <= problem["sum_hi"]):
            continue
        delta = Matrix([Rational(r[i]) - problem["mu"][i, 0] for i in range(5)])
        if bnb.eval_quad(kernel.penalty, delta) > problem["penalty_budget"]:
            continue
        if is_picard_extendable(cert, observable_vector(x=x, e=e, d=d, r=tuple(r))):
            count += 1
    return count


def main() -> None:
    # Fail closed before importing either load-bearing producer.
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    cert = load_picard_certificate()
    bnb = load_module(BNB, "stage32_178_fibration_bnb_picard_leaf")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_fibration_recoverability_picard_leaf")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)
    bridge = bnb.td02_aggregate_bridge(kernel)
    req(tuple(bridge["aggregate_order"]) == OBSERVABLE_ORDER[:5], "TD02 aggregate bridge order regression")
    req(bridge["exact_factorization_C_equals_F_L"] is True, "TD02 aggregate bridge lost exactness")

    panels = []
    strict_examples = []
    # Lightweight bounded research panel only.  These are synthetic terminal-coordinate
    # fixtures, not a FULL178 census and not a MAIN-credit population.
    for d in (8, 10, 12):
        for e in range(0, d + 1, 2):
            for x4 in range(0, min(3, d // 2) + 1):
                x = (0, 0, 0, 0, x4, 0, 0, 0, 0, 0, 0)
                problem = bnb.residual_problem(kernel, g=0, d=d, e=e, x=x)
                baseline, _, _ = bnb.bnb_count(kernel, problem)
                composed, witness, stats = bnb_count_with_picard(
                    bnb, kernel, problem, cert, x=x, e=e, d=d
                )
                brute = brute_count_with_picard(
                    bnb, kernel, problem, cert, x=x, e=e, d=d
                )
                req(composed == brute, f"Picard B&B/bruteforce mismatch d={d} e={e} x4={x4}")
                req(composed <= baseline, f"Picard composition enlarged feasible set d={d} e={e} x4={x4}")
                item = {
                    "g": 0,
                    "d": d,
                    "e": e,
                    "x4": x4,
                    "baseline_feasible_residual_vectors": baseline,
                    "picard_composed_feasible_residual_vectors": composed,
                    "picard_leaf_rejections": baseline - composed,
                    "picard_bnb_lattice_leaf_prunes": stats.lattice_leaf_prunes,
                    "first_composed_witness": list(witness) if witness is not None else None,
                }
                panels.append(item)
                if baseline > composed and len(strict_examples) < 8:
                    strict_examples.append(item)

    total_baseline = sum(x["baseline_feasible_residual_vectors"] for x in panels)
    total_composed = sum(x["picard_composed_feasible_residual_vectors"] for x in panels)
    req(total_composed <= total_baseline, "aggregate preflight composition enlarged feasible population")

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_PICARD_LEAF_COMPOSITION_PREFLIGHT_V1",
        "purpose": "compose the exact Picard64 image-lattice membership oracle with complete five-residual B&B leaves using the existing TD02 aggregate state; lightweight bounded preflight only",
        "observable_order": list(OBSERVABLE_ORDER),
        "picard_image_lattice_index": int(cert["image_lattice_index_in_Zm"]),
        "picard_membership_modulus": int(cert["membership_modulus"]),
        "picard_active_congruence_rows": int(cert["active_congruence_rows"]),
        "composition": {
            "static_td02_observables": ["a", "b", "c", "t", "x4", "e", "d"],
            "dynamic_leaf_observables": ["r0", "r1", "r2", "r3", "r4"],
            "all_twelve_picard_observables_reconstructed_exactly": True,
            "picard_oracle_applied_only_at_complete_residual_leaves": True,
            "partial_prefix_picard_rejection_used": False,
            "baseline_prefix_relaxation_unchanged": True,
            "composition_can_only_remove_baseline_feasible_leaves": True,
        },
        "bounded_synthetic_regression": {
            "panel_count": len(panels),
            "baseline_feasible_residual_vectors_sum": total_baseline,
            "picard_composed_feasible_residual_vectors_sum": total_composed,
            "strict_picard_leaf_rejections_sum": total_baseline - total_composed,
            "strict_rejection_found": bool(strict_examples),
            "strict_examples": strict_examples,
            "all_composed_bnb_counts_match_independent_bruteforce": True,
        },
        "next_exact_step": "attach this leaf oracle to the authorized FULL178 TD02 scaleout consumer and measure the resulting certified upper bound; do not infer production pruning from the synthetic panel",
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
    print("PICARD_LEAF_COMPOSITION_SUMMARY=" + json.dumps({
        "modulus": out["picard_membership_modulus"],
        "congruence_rows": out["picard_active_congruence_rows"],
        "panel_count": len(panels),
        "baseline": total_baseline,
        "composed": total_composed,
        "rejected": total_baseline - total_composed,
        "strict": bool(strict_examples),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
