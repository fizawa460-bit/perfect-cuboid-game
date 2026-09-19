#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import sympy
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
SIGNATURE = HERE / "verify_fibration_nef_signature_factorization.py"
EXISTENTIAL = HERE / "verify_fibration_nef_picard_existential_preflight.py"
SOURCE_LOCKS = {
    "signature_factorization": (SIGNATURE, "eaa1351f3da2d18cbc4ee9525e3447b665e753dd"),
    "picard_existential": (EXISTENTIAL, "d04213380ffa3c656a17c1423b68200599f0e5c8"),
}


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
class MinStats:
    visited_nodes: int = 0
    sum_prunes: int = 0
    incumbent_prunes: int = 0
    lattice_prefix_prunes: int = 0
    lattice_leaf_prunes: int = 0
    leaves: int = 0
    incumbent_updates: int = 0


def picard_min_penalty(prefix_mod, leaf, bnb, kernel, problem: dict, cert: dict, *, static_values: tuple[int, ...]):
    """Exact minimum residual Schur penalty over the Picard-admissible integer box.

    The current qexc-dependent genus budget is intentionally not used.  This
    minimizes the residual penalty once for the static signature
    (a,b,c,t,x4,e,d), allowing every qexc value with those static observables
    to be decided by a single exact threshold.
    """
    if problem.get("structurally_infeasible"):
        return None, None, MinStats()

    caps = tuple(int(v) for v in problem["caps"])
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    mu = problem["mu"]
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    suffix_caps = [0] * (prefix_mod.RESIDUAL_DIM + 1)
    for i in range(prefix_mod.RESIDUAL_DIM - 1, -1, -1):
        suffix_caps[i] = suffix_caps[i + 1] + caps[i]
    syndrome_suffix = prefix_mod.suffix_syndrome_sets(cert, caps)
    req(len(static_values) == prefix_mod.STATIC_WIDTH, "static Picard observable width regression")

    best = None
    best_witness = None
    stats = MinStats()

    def rec(pfx: tuple[int, ...], total: int) -> None:
        nonlocal best, best_witness
        stats.visited_nodes += 1
        depth = len(pfx)
        if total > sum_hi or total + suffix_caps[depth] < sum_lo:
            stats.sum_prunes += 1
            return

        lower = bnb.quadratic_lower(pfx, mu, lowers)
        if best is not None and lower > best:
            stats.incumbent_prunes += 1
            return

        lattice_ok = prefix_mod.prefix_picard_extendable(cert, static_values, pfx, syndrome_suffix)
        if depth == prefix_mod.RESIDUAL_DIM:
            direct = leaf.is_picard_extendable(cert, static_values + pfx)
            req(lattice_ok == direct, "prefix/leaf Picard oracle mismatch at minimum search leaf")
            stats.leaves += 1
            if not lattice_ok:
                stats.lattice_leaf_prunes += 1
                return
            if not (sum_lo <= total <= sum_hi):
                return
            delta = Matrix([Rational(pfx[i]) - mu[i, 0] for i in range(prefix_mod.RESIDUAL_DIM)])
            penalty = bnb.eval_quad(kernel.penalty, delta)
            if best is None or penalty < best:
                best = penalty
                best_witness = pfx
                stats.incumbent_updates += 1
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
            rec(pfx + (value,), total + value)

    rec((), 0)
    return best, best_witness, stats


def qexc_threshold(*, g: int, d: int, t: int, x4: int, min_penalty):
    if min_penalty is None:
        return None, None
    genus_budget = Rational(d * d, 16) + d + 2 - 2 * g
    static_rho = Rational(1, 12) * (Rational(d, 2) - 2 * x4 - t) ** 2
    exact_cut = sympy.factor(2 * (genus_budget - static_rho - min_penalty))
    return exact_cut, int(sympy.floor(exact_cut))


def main() -> None:
    for name, (path, expected) in SOURCE_LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    sigmod = load_module(SIGNATURE, "stage32_178_qexc_signature")
    existential = load_module(EXISTENTIAL, "stage32_178_qexc_existential")

    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_qexc_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_qexc_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_qexc_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_qexc_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    cases = []
    tested_qexc = 0
    strict_threshold_rejections = 0
    total_min_nodes = 0
    total_exist_nodes = 0

    # Lightweight exact regression.  qexc is varied independently while the
    # static signature is fixed; this is precisely the parameter factorization
    # proved by the companion signature verifier, not a claim that every tested
    # qexc occurs as a production terminal square-sum.
    for g in (0, 1):
        for d in (8, 10, 12):
            for e in range(0, d + 1, 2):
                for x4 in range(0, min(2, d // 2) + 1):
                    static_sig = (0, 0, 0, 0, x4)
                    static_values = static_sig + (e, d)
                    zero_problem = sigmod.signature_problem(
                        bnb, kernel, g=g, d=d, e=e,
                        sig=(0, 0, 0, 0, x4, 0),
                    )
                    if zero_problem.get("structurally_infeasible"):
                        # If qexc=0 already exceeds GRF04, every qexc>=0 is rejected.
                        req(zero_problem.get("reason") == "already_rejected_by_GRF04",
                            f"unexpected zero-qexc structural failure g={g} d={d} e={e} x4={x4}")
                        cases.append({
                            "g": g, "d": d, "e": e, "x4": x4,
                            "zero_qexc_already_rejected_by_grf04": True,
                            "threshold_floor": -1,
                            "min_penalty": None,
                            "min_witness": None,
                            "min_search_nodes": 0,
                        })
                        strict_threshold_rejections += 1
                        continue

                    minimum, witness, mstats = picard_min_penalty(
                        prefix, leaf, bnb, kernel, zero_problem, cert,
                        static_values=static_values,
                    )
                    total_min_nodes += mstats.visited_nodes
                    exact_cut, threshold = qexc_threshold(
                        g=g, d=d, t=0, x4=x4, min_penalty=minimum
                    )

                    probes = {0, 1, 2, 3}
                    if threshold is not None:
                        probes.update({max(0, threshold - 1), max(0, threshold), max(0, threshold + 1), max(0, threshold + 2)})
                    for qexc in sorted(probes):
                        problem = sigmod.signature_problem(
                            bnb, kernel, g=g, d=d, e=e,
                            sig=(0, 0, 0, 0, x4, qexc),
                        )
                        expected = minimum is not None and threshold is not None and qexc <= threshold
                        if problem.get("structurally_infeasible"):
                            observed = False
                            enodes = 0
                        else:
                            observed, _first, estats = existential.picard_exists(
                                prefix, leaf, bnb, kernel, problem, cert,
                                x=(0, 0, 0, 0, x4, 0, 0, 0, 0, 0, 0),
                                e=e, d=d,
                            )
                            enodes = estats.visited_nodes
                        req(observed == expected,
                            f"qexc threshold mismatch g={g} d={d} e={e} x4={x4} qexc={qexc} threshold={threshold}")
                        tested_qexc += 1
                        total_exist_nodes += enodes
                        strict_threshold_rejections += int(not observed)

                    cases.append({
                        "g": g,
                        "d": d,
                        "e": e,
                        "x4": x4,
                        "zero_qexc_already_rejected_by_grf04": False,
                        "min_penalty": str(minimum) if minimum is not None else None,
                        "min_witness": list(witness) if witness is not None else None,
                        "qexc_exact_cut": str(exact_cut) if exact_cut is not None else None,
                        "threshold_floor": threshold,
                        "min_search_nodes": mstats.visited_nodes,
                        "min_search_incumbent_prunes": mstats.incumbent_prunes,
                        "min_search_lattice_prefix_prunes": mstats.lattice_prefix_prunes,
                    })

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_PICARD_QEXC_THRESHOLD_PREFLIGHT_V1",
        "purpose": "eliminate repeated qexc-dependent residual searches by minimizing the exact Picard-admissible residual Schur penalty once per static compact signature",
        "exact_identity": {
            "static_signature": ["a", "b", "c", "t", "x4", "e", "d", "g"],
            "varying_coordinate": "qexc",
            "acceptance_iff": "qexc/2 + (d/2-2*x4-t)^2/12 + min_picard_residual_penalty <= d^2/16 + d + 2 - 2*g",
            "integer_threshold": "qexc <= floor(2*(genus_budget-static_rho-min_picard_residual_penalty))",
            "minimum_is_independent_of_qexc": True,
            "picard_congruence_is_preserved_exactly": True,
            "nef_caps_and_sum_window_are_preserved_exactly": True,
        },
        "bounded_exact_regression": {
            "static_cases": len(cases),
            "qexc_probe_cases": tested_qexc,
            "all_threshold_decisions_match_existing_exact_existential_consumer": True,
            "strict_rejection_observations": strict_threshold_rejections,
            "aggregate_min_search_nodes": total_min_nodes,
            "aggregate_existing_existential_nodes": total_exist_nodes,
        },
        "cases": cases,
        "next_exact_step": "construct an exact weighted production counter by static signature plus qexc distribution; evaluate the Picard residual minimum once per static signature and charge all qexc masses by this threshold",
        "production_census_run": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("PICARD_QEXC_THRESHOLD_SUMMARY=" + json.dumps({
        "static_cases": len(cases),
        "qexc_probes": tested_qexc,
        "strict_rejections": strict_threshold_rejections,
        "min_nodes": total_min_nodes,
        "exist_nodes": total_exist_nodes,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
