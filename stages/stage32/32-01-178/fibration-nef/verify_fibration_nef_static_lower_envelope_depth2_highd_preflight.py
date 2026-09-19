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
DEPTH1 = HERE / "verify_fibration_nef_static_lower_envelope_highd_preflight.py"
DEPTH1_BLOB = "48bb34719422163cf5e78a8a0cb6fbe5938a2d63"


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


def residue_min_candidates(lo: int, hi: int, residue: int, modulus: int, center):
    """Exact minimizer candidates for a convex quadratic on one residue class."""
    lo, hi, residue, modulus = int(lo), int(hi), int(residue), int(modulus)
    req(modulus >= 1, "invalid Picard modulus")
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return ()
    last = hi - ((hi - residue) % modulus)
    kcenter = (sympy.Rational(center) - residue) / modulus
    kfloor = int(sympy.floor(kcenter))
    vals = {first, last}
    for k in (kfloor - 1, kfloor, kfloor + 1, kfloor + 2):
        value = residue + modulus * k
        if first <= value <= last:
            vals.add(value)
    return tuple(sorted(vals))


def two_coordinate_picard_lower_envelope_fast(
    prefix, bnb, kernel, problem: dict, cert: dict, *, static_values
):
    """Exact minimum depth-2 Schur lower bound on the relaxed feasible prefix.

    For each integer r0, the admissible r1 set is an interval intersected with
    residue classes modulo the Picard membership modulus.  On each residue
    class the depth-2 Schur form is a one-variable convex quadratic, so its
    exact integer minimum is attained at one of the nearest lattice points to
    the continuous center (with interval endpoints included defensively).
    """
    if problem.get("structurally_infeasible"):
        return None, 0, 0, 0

    caps = tuple(int(v) for v in problem["caps"])
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    suffix_capacity = sum(caps[2:])
    syndrome_suffix = prefix.suffix_syndrome_sets(cert, caps)
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    lower2 = lowers[2]
    modulus = int(cert["membership_modulus"])
    req(modulus >= 1, "invalid Picard membership modulus")

    r0_lo = max(0, sum_lo - caps[1] - suffix_capacity)
    r0_hi = min(caps[0], sum_hi)
    if r0_lo > r0_hi:
        return None, 0, 0, 0

    best = None
    r0_tested = 0
    residue_classes_tested = 0
    candidate_points_tested = 0

    mu0, mu1 = problem["mu"][0, 0], problem["mu"][1, 0]
    q11 = lower2[1, 1]
    req(q11 > 0, "depth-2 Schur diagonal lost positivity")
    q01 = lower2[0, 1]

    for r0 in range(r0_lo, r0_hi + 1):
        r0_tested += 1
        lo1 = max(0, sum_lo - r0 - suffix_capacity)
        hi1 = min(caps[1], sum_hi - r0)
        if lo1 > hi1:
            continue

        # For fixed r0, minimize q00*d0^2 + 2*q01*d0*d1 + q11*d1^2.
        # Continuous minimizer in r1 is mu1 - (q01/q11)*(r0-mu0).
        center = sympy.factor(mu1 - q01 * (Rational(r0) - mu0) / q11)

        residues = range(modulus) if modulus > 1 else (0,)
        for residue in residues:
            candidates = residue_min_candidates(lo1, hi1, residue, modulus, center)
            if not candidates:
                continue
            residue_classes_tested += 1
            # Extendability depends only on the residue class modulo q.
            probe = candidates[0]
            if not prefix.prefix_picard_extendable(
                cert, tuple(static_values), (r0, probe), syndrome_suffix
            ):
                continue
            for r1 in candidates:
                candidate_points_tested += 1
                value = bnb.quadratic_lower(
                    (r0, r1), problem["mu"], lowers
                )
                if best is None or value < best:
                    best = value

    return best, r0_tested, residue_classes_tested, candidate_points_tested


def two_coordinate_picard_lower_envelope_bruteforce(
    prefix, bnb, kernel, problem: dict, cert: dict, *, static_values
):
    """Small-case oracle for the fast depth-2 minimizer."""
    if problem.get("structurally_infeasible"):
        return None
    caps = tuple(int(v) for v in problem["caps"])
    sum_lo, sum_hi = int(problem["sum_lo"]), int(problem["sum_hi"])
    suffix_capacity = sum(caps[2:])
    syndrome_suffix = prefix.suffix_syndrome_sets(cert, caps)
    lowers = bnb.prefix_lower_matrices(kernel.penalty)
    best = None
    for r0 in range(caps[0] + 1):
        for r1 in range(caps[1] + 1):
            total = r0 + r1
            if total > sum_hi or total + suffix_capacity < sum_lo:
                continue
            if not prefix.prefix_picard_extendable(
                cert, tuple(static_values), (r0, r1), syndrome_suffix
            ):
                continue
            value = bnb.quadratic_lower((r0, r1), problem["mu"], lowers)
            if best is None or value < best:
                best = value
    return best


def cumulative_product(aq, hq, threshold: int | None) -> int:
    if threshold is None or threshold < 0 or not aq or not hq:
        return 0
    qs = sorted(hq)
    running = 0
    prefix_mass = []
    for q in qs:
        running += hq[q]
        prefix_mass.append(running)
    total = 0
    for qa, ma in aq.items():
        pos = bisect_right(qs, int(threshold) - qa) - 1
        if pos >= 0:
            total += ma * prefix_mass[pos]
    return total


def qthreshold(depth1, *, g: int, d: int, t: int, x4: int, lower):
    return depth1.envelope_qthreshold(g=g, d=d, t=t, x4=x4, lower=lower)


def evaluate_small_exact(
    *,
    depth1,
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
):
    qcap = (d * d) // 8 + 2 * d + 4 - 4 * g
    limit, apoly, hpoly = weighted.build_factorized_counter(e, qcap)
    total_mass = 0
    accepted_depth2 = 0
    accepted_exact = 0
    depth1_pruned = 0
    depth2_pruned = 0
    depth2_additional = 0
    surviving_exact_minimizations = 0
    checked_fast_vs_brute = 0

    for a, aq in apoly.items():
        min_qa = min(aq)
        for (b, c, t), hq in hpoly.items():
            if a + b + c > e:
                continue
            mass = cumulative_product(aq, hq, qcap)
            if not mass:
                continue
            total_mass += mass
            min_q = min_qa + min(hq)
            problem = sigmod.signature_problem(
                bnb, kernel, g=g, d=d, e=e,
                sig=(a, b, c, t, x4, 0),
            )
            if problem.get("structurally_infeasible"):
                continue

            static_values = (a, b, c, t, x4, e, d)
            lower1, _tested1, _ext1 = depth1.one_coordinate_picard_lower_envelope(
                prefix, bnb, kernel, problem, cert, static_values=static_values
            )
            lower2, _r0, _res, _pts = two_coordinate_picard_lower_envelope_fast(
                prefix, bnb, kernel, problem, cert, static_values=static_values
            )
            brute2 = two_coordinate_picard_lower_envelope_bruteforce(
                prefix, bnb, kernel, problem, cert, static_values=static_values
            )
            req(lower2 == brute2, f"fast/brute depth2 mismatch g={g} d={d} e={e} x4={x4} key={(a,b,c,t)}")
            checked_fast_vs_brute += 1

            if lower1 is None:
                req(lower2 is None, "depth2 found prefix after depth1 declared empty")
            elif lower2 is not None:
                req(sympy.simplify(lower2 - lower1) >= 0,
                    "depth2 lower bound weakened depth1")

            _c1, threshold1 = qthreshold(
                depth1, g=g, d=d, t=t, x4=x4, lower=lower1
            )
            _c2, threshold2 = qthreshold(
                depth1, g=g, d=d, t=t, x4=x4, lower=lower2
            )
            prune1 = threshold1 is None or min_q > threshold1
            prune2 = threshold2 is None or min_q > threshold2
            req((not prune1) or prune2, "depth2 failed to dominate depth1 pruning")
            depth1_pruned += int(prune1)
            depth2_pruned += int(prune2)
            depth2_additional += int(prune2 and not prune1)

            minimum, _witness, _stats = qthr.picard_min_penalty(
                prefix, leaf, bnb, kernel, problem, cert,
                static_values=static_values,
            )
            _ce, exact_threshold = qthr.qexc_threshold(
                g=g, d=d, t=t, x4=x4, min_penalty=minimum
            )
            exact_mass = cumulative_product(
                aq, hq,
                min(qcap, exact_threshold) if exact_threshold is not None else None,
            )
            accepted_exact += exact_mass
            if not prune2:
                surviving_exact_minimizations += 1
                accepted_depth2 += exact_mass

    req(accepted_depth2 == accepted_exact,
        f"depth2 envelope changed exact accepted mass g={g} d={d} e={e} x4={x4}")
    return {
        "g": g,
        "d": d,
        "e": e,
        "x4": x4,
        "absolute_qcap": qcap,
        "effective_exceptional_mass_cap": limit,
        "qcapped_exceptional_mass": str(total_mass),
        "accepted_mass": str(accepted_exact),
        "depth1_pruned_static_keys": depth1_pruned,
        "depth2_pruned_static_keys": depth2_pruned,
        "depth2_additional_pruned_static_keys": depth2_additional,
        "exact_minimizations_after_depth2": surviving_exact_minimizations,
        "fast_vs_bruteforce_depth2_keys_checked": checked_fast_vs_brute,
        "accepted_matches_exact_picard_minimum": True,
    }


def evaluate_highd_envelope_only(
    *,
    depth1,
    weighted,
    sigmod,
    prefix,
    bnb,
    kernel,
    cert,
    g: int,
    d: int,
    e: int,
    x4: int,
    factorized_counter,
):
    qcap = (d * d) // 8 + 2 * d + 4 - 4 * g
    limit, apoly, hpoly = factorized_counter
    total_mass = 0
    static_keys = 0
    structural_keys = 0
    depth1_pruned = 0
    depth2_pruned = 0
    depth2_additional = 0
    depth1_pruned_mass = 0
    depth2_pruned_mass = 0
    r0_tested = 0
    residue_classes_tested = 0
    candidate_points_tested = 0

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
            problem = sigmod.signature_problem(
                bnb, kernel, g=g, d=d, e=e,
                sig=(a, b, c, t, x4, 0),
            )
            if problem.get("structurally_infeasible"):
                structural_keys += 1
                depth1_pruned += 1
                depth2_pruned += 1
                depth1_pruned_mass += mass
                depth2_pruned_mass += mass
                continue

            static_values = (a, b, c, t, x4, e, d)
            lower1, _tested1, _ext1 = depth1.one_coordinate_picard_lower_envelope(
                prefix, bnb, kernel, problem, cert, static_values=static_values
            )
            lower2, n0, nres, npts = two_coordinate_picard_lower_envelope_fast(
                prefix, bnb, kernel, problem, cert, static_values=static_values
            )
            r0_tested += n0
            residue_classes_tested += nres
            candidate_points_tested += npts
            if lower1 is None:
                req(lower2 is None, "depth2 found prefix after depth1 empty")
            elif lower2 is not None:
                req(sympy.simplify(lower2 - lower1) >= 0,
                    "depth2 high-d lower bound weakened depth1")

            _c1, threshold1 = qthreshold(
                depth1, g=g, d=d, t=t, x4=x4, lower=lower1
            )
            _c2, threshold2 = qthreshold(
                depth1, g=g, d=d, t=t, x4=x4, lower=lower2
            )
            prune1 = threshold1 is None or min_q > threshold1
            prune2 = threshold2 is None or min_q > threshold2
            req((not prune1) or prune2, "depth2 high-d pruning failed to dominate depth1")
            if prune1:
                depth1_pruned += 1
                depth1_pruned_mass += mass
            if prune2:
                depth2_pruned += 1
                depth2_pruned_mass += mass
            if prune2 and not prune1:
                depth2_additional += 1

    return {
        "g": g,
        "d": d,
        "e": e,
        "x4": x4,
        "absolute_qcap": qcap,
        "effective_exceptional_mass_cap": limit,
        "qcapped_exceptional_mass": str(total_mass),
        "static_keys": static_keys,
        "structural_keys": structural_keys,
        "structural_or_envelope_depth1_pruned_keys": depth1_pruned,
        "structural_or_envelope_depth2_pruned_keys": depth2_pruned,
        "depth2_additional_pruned_keys": depth2_additional,
        "keys_requiring_exact_picard_minimum_after_depth2": static_keys - depth2_pruned,
        "depth1_pruned_mass": str(depth1_pruned_mass),
        "depth2_pruned_mass": str(depth2_pruned_mass),
        "r0_values_tested": r0_tested,
        "picard_residue_classes_tested": residue_classes_tested,
        "quadratic_candidate_points_tested": candidate_points_tested,
        "exact_picard_minimum_executed": False,
    }


def main() -> None:
    req(DEPTH1.is_file(), "missing depth1 lower-envelope carrier")
    req(git_blob(DEPTH1) == DEPTH1_BLOB, "depth1 lower-envelope carrier drift")
    depth1 = load_module(DEPTH1, "stage32_178_depth2_depth1")

    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file(), f"missing depth1 source lock {name}")
        req(depth1.git_blob(path) == expected, f"depth1 source drift {name}")

    weighted = depth1.load_module(depth1.WEIGHTED, "stage32_178_depth2_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "stage32_178_depth2_qthreshold")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_depth2_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_depth2_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_depth2_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_depth2_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_depth2_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_depth2_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    checkpoint = json.loads(depth1.CHECKPOINT.read_text())
    max_stratum = checkpoint["symbolic_full178_prefix_census"]["max_single_stratum"]
    req(max_stratum["row_id"] == "g1-d192", "retained high-d row drift")
    req(int(max_stratum["e"]) == 663, "retained maximum single stratum e drift")

    regressions = []
    for g, d, e, x4 in (
        (0, 8, 2, 0),
        (1, 8, 4, 0),
        (0, 10, 5, 1),
        (1, 12, 6, 2),
    ):
        regressions.append(evaluate_small_exact(
            depth1=depth1, weighted=weighted, qthr=qthr, sigmod=sigmod,
            prefix=prefix, leaf=leaf, bnb=bnb, kernel=kernel, cert=cert,
            g=g, d=d, e=e, x4=x4,
        ))

    highd_g, highd_d, highd_e = 1, 192, 32
    qcap = (highd_d * highd_d) // 8 + 2 * highd_d + 4 - 4 * highd_g
    factorized_counter = weighted.build_factorized_counter(highd_e, qcap)
    normal_budget = 19 * highd_d - 5 * highd_e
    highd_x4 = (0, 24, 48, 72, 96)
    req(all(0 <= x4 <= normal_budget for x4 in highd_x4),
        "high-d x4 outside production range")
    highd_rows = [
        evaluate_highd_envelope_only(
            depth1=depth1, weighted=weighted, sigmod=sigmod, prefix=prefix,
            bnb=bnb, kernel=kernel, cert=cert,
            g=highd_g, d=highd_d, e=highd_e, x4=x4,
            factorized_counter=factorized_counter,
        )
        for x4 in highd_x4
    ]

    out = {
        "schema": "STAGE32_32_01_178_STATIC_LOWER_ENVELOPE_DEPTH2_HIGHD_PREFLIGHT_V1",
        "purpose": "strengthen the exact static qexc lower-envelope from residual-prefix depth one to depth two without executing high-d Picard minimization",
        "depth2_envelope": {
            "prefix": ["r0", "r1"],
            "sum_window_suffix_capacity_preserved": True,
            "picard_prefix_extendability_preserved": True,
            "depth2_schur_lower_bound_exact": True,
            "r1_search": "EXACT_RESIDUE_CLASS_CONVEX_MINIMIZATION",
            "r1_full_interval_scan_required": False,
            "safe_lower_bound": True,
            "dominates_depth1_on_checked_keys": True,
        },
        "bounded_exact_regression": {
            "cases": len(regressions),
            "fast_depth2_matches_bruteforce_depth2": True,
            "accepted_mass_matches_exact_picard_minimum": True,
            "rows": regressions,
        },
        "bounded_real_high_d_envelope_telemetry": {
            "row_id": "g1-d192",
            "e": highd_e,
            "x4_slices": list(highd_x4),
            "full_exceptional_factorized_family_per_slice": True,
            "exact_picard_minimum_deliberately_not_executed": True,
            "rows": highd_rows,
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
        },
        "next_exact_step": "use depth2 envelope telemetry to choose between a resumable x4 interval counter and a depth3 prefix envelope; do not arm wider production until the exact-head telemetry is replayed",
        "production_heavy_run_armed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("STATIC_LOWER_ENVELOPE_DEPTH2_SUMMARY=" + json.dumps({
        "regression_cases": len(regressions),
        "highd_slices": len(highd_rows),
        "highd_static_keys": sum(r["static_keys"] for r in highd_rows),
        "depth1_pruned_keys": sum(r["structural_or_envelope_depth1_pruned_keys"] for r in highd_rows),
        "depth2_pruned_keys": sum(r["structural_or_envelope_depth2_pruned_keys"] for r in highd_rows),
        "depth2_additional_pruned_keys": sum(r["depth2_additional_pruned_keys"] for r in highd_rows),
        "remaining_exact_minimization_keys": sum(r["keys_requiring_exact_picard_minimum_after_depth2"] for r in highd_rows),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
