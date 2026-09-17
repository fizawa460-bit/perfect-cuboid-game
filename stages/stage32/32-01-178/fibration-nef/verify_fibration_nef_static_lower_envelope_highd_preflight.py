#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from bisect import bisect_right
from pathlib import Path

import sympy
from sympy import Rational

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
WEIGHTED = HERE / "verify_fibration_nef_weighted_signature_counter_preflight.py"
QTHRESH = HERE / "verify_fibration_nef_picard_qexc_threshold_preflight.py"
CHECKPOINT = RES / "full178-prefix-indexed-compression-main-checkpoint.json"
CENSUS_BUILDER = RES / "build_compressed_full178_prefix_census.py"
LOCKS = {
    "weighted_signature_counter": (WEIGHTED, "be2817633e1ef60e0415927889e1d589bec99aa4"),
    "picard_qexc_threshold": (QTHRESH, "c583466ff865c0dcf33c19879cf4936e35983e83"),
    "prefix_indexed_checkpoint": (CHECKPOINT, "eb823cc2f99d74456d5701b4673f848f18ba3151"),
    "compressed_census_builder": (CENSUS_BUILDER, "5cef4d833d4d3cec407a3d57e9fb93788f0e6752"),
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


def cumulative_product(aq, hq, threshold: int | None) -> int:
    """Exact multiplicity in A(z)H(z) with total qexc <= threshold."""
    if threshold is None or threshold < 0 or not aq or not hq:
        return 0
    qs = sorted(hq)
    running = 0
    prefix = []
    for q in qs:
        running += hq[q]
        prefix.append(running)
    total = 0
    for qa, ma in aq.items():
        pos = bisect_right(qs, int(threshold) - qa) - 1
        if pos >= 0:
            total += ma * prefix[pos]
    return total


def one_coordinate_picard_lower_envelope(prefix, bnb, kernel, problem: dict, cert: dict, *, static_values):
    """Safe qexc-independent lower bound on the exact Picard residual penalty.

    Every feasible full residual vector has an r0 inside the sum-feasible
    interval below and its one-coordinate Schur lower bound is <= its full
    quadratic penalty.  Picard-prefix extendability only removes r0 values
    that cannot satisfy the retained exact linear congruences.  The suffix
    oracle ignores the final sum-window coupling, so it can admit false
    positives but cannot remove a genuinely feasible vector.
    """
    if problem.get("structurally_infeasible"):
        return None, 0, 0

    caps = tuple(int(v) for v in problem["caps"])
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    suffix_capacity = sum(caps[1:])
    lo = max(0, sum_lo - suffix_capacity)
    hi = min(caps[0], sum_hi)
    if lo > hi:
        return None, 0, 0

    syndrome_suffix = prefix.suffix_syndrome_sets(cert, caps)
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    best = None
    tested = 0
    picard_extendable = 0
    for r0 in range(lo, hi + 1):
        tested += 1
        if not prefix.prefix_picard_extendable(
            cert, tuple(static_values), (r0,), syndrome_suffix
        ):
            continue
        picard_extendable += 1
        lower = bnb.quadratic_lower((r0,), problem["mu"], lowers)
        if best is None or lower < best:
            best = lower
    return best, tested, picard_extendable


def envelope_qthreshold(*, g: int, d: int, t: int, x4: int, lower):
    if lower is None:
        return None, None
    genus_budget = Rational(d * d, 16) + d + 2 - 2 * g
    static_rho = Rational(1, 12) * (Rational(d, 2) - 2 * x4 - t) ** 2
    exact_cut = sympy.factor(2 * (genus_budget - static_rho - lower))
    return exact_cut, int(sympy.floor(exact_cut))


def evaluate_slice(
    *,
    weighted,
    qthr,
    sigmod,
    prefix,
    leaf,
    bnb,
    kernel,
    cert,
    g: int,
    d: int,
    e: int,
    x4: int,
    compare_without_envelope: bool,
    factorized_counter=None,
):
    qcap = (d * d) // 8 + 2 * d + 4 - 4 * g
    if factorized_counter is None:
        limit, apoly, hpoly = weighted.build_factorized_counter(e, qcap)
    else:
        limit, apoly, hpoly = factorized_counter

    total_mass = 0
    accepted = 0
    structural_rejected_mass = 0
    prefix_empty_rejected_mass = 0
    envelope_q_rejected_mass = 0

    static_keys = 0
    structural_keys = 0
    prefix_empty_keys = 0
    envelope_q_pruned_keys = 0
    exact_minimized_keys = 0
    exact_min_nodes = 0
    r0_candidates_tested = 0
    r0_picard_extendable = 0

    baseline_exact_minimized_keys = 0
    baseline_accepted = 0

    for a, aq in apoly.items():
        min_qa = min(aq)
        for (b, c, t), hq in hpoly.items():
            if a + b + c > e:
                continue
            mass = cumulative_product(aq, hq, qcap)
            if not mass:
                continue
            static_keys += 1
            total_mass += mass
            min_q = min_qa + min(hq)

            zero_problem = sigmod.signature_problem(
                bnb, kernel, g=g, d=d, e=e,
                sig=(a, b, c, t, x4, 0),
            )
            if zero_problem.get("structurally_infeasible"):
                structural_keys += 1
                structural_rejected_mass += mass
                continue

            static_values = (a, b, c, t, x4, e, d)
            lower, tested, extendable = one_coordinate_picard_lower_envelope(
                prefix, bnb, kernel, zero_problem, cert,
                static_values=static_values,
            )
            r0_candidates_tested += tested
            r0_picard_extendable += extendable

            if compare_without_envelope:
                baseline_minimum, _bw, _bstats = qthr.picard_min_penalty(
                    prefix, leaf, bnb, kernel, zero_problem, cert,
                    static_values=static_values,
                )
                _bcut, bthreshold = qthr.qexc_threshold(
                    g=g, d=d, t=t, x4=x4, min_penalty=baseline_minimum
                )
                baseline_exact_minimized_keys += 1
                baseline_accepted += cumulative_product(
                    aq, hq,
                    min(qcap, bthreshold) if bthreshold is not None else None,
                )

            if lower is None:
                prefix_empty_keys += 1
                prefix_empty_rejected_mass += mass
                continue

            _coarse_cut, coarse_threshold = envelope_qthreshold(
                g=g, d=d, t=t, x4=x4, lower=lower
            )
            if coarse_threshold is None or min_q > coarse_threshold:
                envelope_q_pruned_keys += 1
                envelope_q_rejected_mass += mass
                continue

            minimum, _witness, stats = qthr.picard_min_penalty(
                prefix, leaf, bnb, kernel, zero_problem, cert,
                static_values=static_values,
            )
            _exact_cut, threshold = qthr.qexc_threshold(
                g=g, d=d, t=t, x4=x4, min_penalty=minimum
            )
            exact_minimized_keys += 1
            exact_min_nodes += stats.visited_nodes
            accepted += cumulative_product(
                aq, hq,
                min(qcap, threshold) if threshold is not None else None,
            )

    rejected = total_mass - accepted
    if compare_without_envelope:
        req(accepted == baseline_accepted,
            f"lower-envelope changed exact accepted mass g={g} d={d} e={e} x4={x4}")

    return {
        "g": g,
        "d": d,
        "e": e,
        "x4": x4,
        "absolute_qcap": qcap,
        "effective_exceptional_mass_cap": limit,
        "qcapped_exceptional_mass": str(total_mass),
        "accepted_mass": str(accepted),
        "rejected_mass": str(rejected),
        "static_keys": static_keys,
        "structural_reject_keys": structural_keys,
        "picard_prefix_empty_keys": prefix_empty_keys,
        "lower_envelope_q_pruned_keys": envelope_q_pruned_keys,
        "exact_picard_minimized_keys": exact_minimized_keys,
        "baseline_exact_picard_minimized_keys": baseline_exact_minimized_keys if compare_without_envelope else None,
        "exact_picard_min_search_nodes": exact_min_nodes,
        "r0_candidates_tested": r0_candidates_tested,
        "r0_picard_extendable": r0_picard_extendable,
        "structural_rejected_mass": str(structural_rejected_mass),
        "picard_prefix_empty_rejected_mass": str(prefix_empty_rejected_mass),
        "lower_envelope_q_rejected_mass": str(envelope_q_rejected_mass),
        "accepted_matches_no_envelope_baseline": True if compare_without_envelope else None,
    }


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    weighted = load_module(WEIGHTED, "stage32_178_lowerenv_weighted")
    qthr = load_module(QTHRESH, "stage32_178_lowerenv_qthreshold")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_lowerenv_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_lowerenv_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_lowerenv_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_lowerenv_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_lowerenv_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_lowerenv_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    checkpoint = json.loads(CHECKPOINT.read_text())
    req(checkpoint["symbolic_full178_prefix_census"]["max_single_stratum"]["row_id"] == "g1-d192",
        "retained high-d production row drift")
    req(int(checkpoint["symbolic_full178_prefix_census"]["maximum_e"]) == 729,
        "retained production maximum-e drift")

    # Exact small regressions compare every accepted multiplicity with the
    # pre-envelope factorized threshold route.
    regressions = []
    for g, d, e, x4 in (
        (0, 8, 2, 0),
        (1, 8, 4, 0),
        (0, 10, 5, 1),
        (1, 12, 6, 2),
    ):
        regressions.append(evaluate_slice(
            weighted=weighted, qthr=qthr, sigmod=sigmod, prefix=prefix,
            leaf=leaf, bnb=bnb, kernel=kernel, cert=cert,
            g=g, d=d, e=e, x4=x4, compare_without_envelope=True,
        ))

    # Bounded real production telemetry on the retained g1-d192 row.  The
    # census rule for genus 1 is e=4..floor(19*d/5), hence e=32 is an actual
    # coarse production stratum.  Only five exact x4 slices are measured.
    highd_g, highd_d, highd_e = 1, 192, 32
    req(4 <= highd_e <= (19 * highd_d) // 5, "high-d e outside production census range")
    normal_budget = 19 * highd_d - 5 * highd_e
    highd_x4 = (0, 24, 48, 72, 96)
    req(all(0 <= x4 <= normal_budget for x4 in highd_x4), "high-d x4 outside production range")
    highd_qcap = (highd_d * highd_d) // 8 + 2 * highd_d + 4 - 4 * highd_g
    highd_counter = weighted.build_factorized_counter(highd_e, highd_qcap)
    highd_rows = [
        evaluate_slice(
            weighted=weighted, qthr=qthr, sigmod=sigmod, prefix=prefix,
            leaf=leaf, bnb=bnb, kernel=kernel, cert=cert,
            g=highd_g, d=highd_d, e=highd_e, x4=x4,
            compare_without_envelope=False,
            factorized_counter=highd_counter,
        )
        for x4 in highd_x4
    ]

    out = {
        "schema": "STAGE32_32_01_178_STATIC_LOWER_ENVELOPE_HIGHD_PREFLIGHT_V1",
        "purpose": "prune static factorized production keys before exact Picard residual minimization by an exact one-coordinate Schur lower envelope with Picard-prefix congruence filtering",
        "lower_envelope": {
            "residual_prefix_depth": 1,
            "integer_r0_interval_preserves_sum_window_feasibility": True,
            "picard_prefix_congruence_filter_exact": True,
            "suffix_sum_window_relaxed": True,
            "therefore_bound_is_safe_lower_bound": True,
            "qexc_independent_for_fixed_static_key": True,
            "whole_static_key_rejected_when": "min_qexc_support > floor(2*(genus_budget-static_rho-lower_envelope))",
            "terminal_by_terminal_picard_minimization_required": False,
        },
        "bounded_exact_regression": {
            "cases": len(regressions),
            "all_accepted_multiplicities_match_no_envelope_factorized_route": True,
            "rows": regressions,
        },
        "bounded_real_high_d_production_slice": {
            "row_id": "g1-d192",
            "e": highd_e,
            "x4_slices": list(highd_x4),
            "normal_x4_budget": normal_budget,
            "is_exact_coarse_production_stratum": True,
            "full_exceptional_family_counted_per_selected_x4_slice": True,
            "rows": highd_rows,
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
        },
        "next_exact_step": "if high-d telemetry shows material exact-minimization savings, extend from selected x4 slices to a resumable x4 interval counter; otherwise strengthen the envelope to depth two before any wider production execution",
        "production_heavy_run_armed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("STATIC_LOWER_ENVELOPE_HIGHD_SUMMARY=" + json.dumps({
        "regression_cases": len(regressions),
        "highd_slices": len(highd_rows),
        "highd_static_keys": sum(r["static_keys"] for r in highd_rows),
        "highd_exact_minimized_keys": sum(r["exact_picard_minimized_keys"] for r in highd_rows),
        "highd_envelope_pruned_keys": sum(r["lower_envelope_q_pruned_keys"] for r in highd_rows),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
