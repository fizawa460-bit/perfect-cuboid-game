#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import sympy

HERE = Path(__file__).resolve().parent
DEPTH2 = HERE / "verify_fibration_nef_static_lower_envelope_depth2_highd_preflight.py"
COMPLETE = HERE / "verify_fibration_nef_static_minq_complete_preflight.py"
LOCKS = {
    "depth2_envelope": (DEPTH2, "c60e7dbde8b60a1d0edefd407c4a745373a02b01"),
    "complete_static_minq": (COMPLETE, "f8a85f38114275eb58e011850e5457fbdda24948"),
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


def evaluate_static_first(
    *, depth2, depth1, complete, sigmod, prefix, bnb, kernel, cert,
    static_keys, g: int, d: int, e: int, x4: int,
):
    structural = 0
    depth1_pruned = 0
    depth2_pruned = 0
    additional = 0
    r0_tested = 0
    residue_classes = 0
    candidate_points = 0

    for a, b, c, t, min_q in static_keys:
        problem = sigmod.signature_problem(
            bnb, kernel, g=g, d=d, e=e,
            sig=(a, b, c, t, x4, 0),
        )
        if problem.get("structurally_infeasible"):
            structural += 1
            depth1_pruned += 1
            depth2_pruned += 1
            continue

        static_values = (a, b, c, t, x4, e, d)
        lower1, _n1, _ext1 = depth1.one_coordinate_picard_lower_envelope(
            prefix, bnb, kernel, problem, cert, static_values=static_values
        )
        lower2, n0, nres, npts = depth2.two_coordinate_picard_lower_envelope_fast(
            prefix, bnb, kernel, problem, cert, static_values=static_values
        )
        r0_tested += n0
        residue_classes += nres
        candidate_points += npts

        if lower1 is None:
            req(lower2 is None, "depth2 found prefix after depth1 empty")
        elif lower2 is not None:
            req(sympy.simplify(lower2 - lower1) >= 0,
                "static-first depth2 lower bound weakened depth1")

        _cut1, threshold1 = depth2.qthreshold(
            depth1, g=g, d=d, t=t, x4=x4, lower=lower1
        )
        _cut2, threshold2 = depth2.qthreshold(
            depth1, g=g, d=d, t=t, x4=x4, lower=lower2
        )
        prune1 = threshold1 is None or min_q > threshold1
        prune2 = threshold2 is None or min_q > threshold2
        req((not prune1) or prune2,
            "static-first depth2 pruning failed to dominate depth1")
        depth1_pruned += int(prune1)
        depth2_pruned += int(prune2)
        additional += int(prune2 and not prune1)

    total = len(static_keys)
    return {
        "x4": x4,
        "static_keys": total,
        "structural_keys": structural,
        "depth1_pruned_keys": depth1_pruned,
        "depth2_pruned_keys": depth2_pruned,
        "depth2_additional_pruned_keys": additional,
        "surviving_static_keys_after_depth2": total - depth2_pruned,
        "r0_values_tested": r0_tested,
        "picard_residue_classes_tested": residue_classes,
        "quadratic_candidate_points_tested": candidate_points,
    }


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    depth2 = load_module(DEPTH2, "stage32_178_static_first_depth2")
    complete = load_module(COMPLETE, "stage32_178_static_first_complete")

    req(depth2.DEPTH1.is_file(), "missing depth1 carrier")
    req(depth2.git_blob(depth2.DEPTH1) == depth2.DEPTH1_BLOB,
        "depth1 carrier drift")
    depth1 = depth2.load_module(depth2.DEPTH1, "stage32_178_static_first_depth1")
    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file(), f"missing depth1 source lock {name}")
        req(depth1.git_blob(path) == expected, f"depth1 source drift {name}")

    weighted = depth1.load_module(depth1.WEIGHTED, "stage32_178_static_first_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "stage32_178_static_first_qthreshold")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_static_first_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_static_first_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_static_first_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_static_first_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_static_first_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_static_first_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    req(complete.UNEQUAL.is_file(), "missing unequal static min-q producer")
    req(complete.git_blob(complete.UNEQUAL) == complete.UNEQUAL_BLOB,
        "unequal static min-q producer drift")
    unequal = complete.load_module(complete.UNEQUAL, "stage32_178_static_first_unequal")
    req(unequal.PARITY.is_file(), "missing parity quotient producer")
    req(unequal.git_blob(unequal.PARITY) == unequal.PARITY_BLOB,
        "parity quotient producer drift")
    parity = unequal.load_module(unequal.PARITY, "stage32_178_static_first_parity")

    highd_g, highd_d, highd_e = 1, 192, 32
    qcap = (highd_d * highd_d) // 8 + 2 * highd_d + 4 - 4 * highd_g
    req(qcap == 4992, "g1-d192 qcap drift")
    limit = weighted.effective_mass_cap(highd_e, qcap)
    req(limit == highd_e, "unexpected effective mass cap at e32")

    unequal_h, _ustates = unequal.unequal_static_minq(limit, qcap)
    equal_h = complete.equal_static_minq(limit, qcap)
    hmin = complete.merge_static_minq(unequal_h, equal_h)

    # Primary static-first population: no H q-polynomial is needed here.
    static_keys = []
    for a in range(limit + 1):
        qa = unequal.a_min_q_closed(a)
        if qa > qcap:
            continue
        for (b, c, t), qh in hmin.items():
            if a + b + c > highd_e:
                continue
            min_q = qa + qh
            if min_q <= qcap:
                static_keys.append((a, b, c, t, min_q))

    normal_budget = 19 * highd_d - 5 * highd_e
    highd_x4 = (0, 24, 48, 72, 96)
    req(all(0 <= x4 <= normal_budget for x4 in highd_x4),
        "high-d x4 outside production range")
    static_rows = [
        evaluate_static_first(
            depth2=depth2, depth1=depth1, complete=complete,
            sigmod=sigmod, prefix=prefix, bnb=bnb, kernel=kernel, cert=cert,
            static_keys=static_keys,
            g=highd_g, d=highd_d, e=highd_e, x4=x4,
        )
        for x4 in highd_x4
    ]

    # Regression oracle only: materialize the existing exact factorized q
    # polynomials and require identical key-level depth1/depth2 decisions.
    full_counter = parity.build_factorized_counter(weighted, highd_e, qcap)
    oracle_rows = [
        depth2.evaluate_highd_envelope_only(
            depth1=depth1,
            weighted=weighted,
            sigmod=sigmod,
            prefix=prefix,
            bnb=bnb,
            kernel=kernel,
            cert=cert,
            g=highd_g,
            d=highd_d,
            e=highd_e,
            x4=x4,
            factorized_counter=full_counter,
        )
        for x4 in highd_x4
    ]

    for static_row, oracle in zip(static_rows, oracle_rows):
        req(static_row["static_keys"] == oracle["static_keys"],
            "static-first key population mismatch")
        req(static_row["structural_keys"] == oracle["structural_keys"],
            "static-first structural count mismatch")
        req(static_row["depth1_pruned_keys"] == oracle["structural_or_envelope_depth1_pruned_keys"],
            "static-first depth1 prune mismatch")
        req(static_row["depth2_pruned_keys"] == oracle["structural_or_envelope_depth2_pruned_keys"],
            "static-first depth2 prune mismatch")
        req(static_row["depth2_additional_pruned_keys"] == oracle["depth2_additional_pruned_keys"],
            "static-first depth2 additional-prune mismatch")
        req(static_row["surviving_static_keys_after_depth2"] == oracle["keys_requiring_exact_picard_minimum_after_depth2"],
            "static-first survivor count mismatch")

    out = {
        "schema": "STAGE32_32_01_178_DEPTH2_STATIC_FIRST_HIGHD_PREFLIGHT_V1",
        "purpose": "execute depth-2 static pruning from exact support/min-q before qexc histogram materialization, with the old full weighted counter retained only as a bounded regression oracle",
        "static_first": {
            "row_id": "g1-d192",
            "e": highd_e,
            "absolute_qcap": qcap,
            "h_q_histogram_required_before_depth2": False,
            "A_q_histogram_required_before_depth2": False,
            "complete_static_key_count": len(static_keys),
            "min_qexc": "closed min-qA(a) + exact complete min-qH(b,c,t)",
        },
        "bounded_real_high_d_telemetry": {
            "x4_slices": list(highd_x4),
            "rows": static_rows,
            "full_histogram_oracle_key_counts_match": True,
            "full_histogram_oracle_used_only_for_regression": True,
            "exact_picard_minimum_executed": False,
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
        },
        "next_exact_step": "construct weighted qexc distributions only for the static keys surviving depth-2, rather than for the whole H family; then extend this static-first architecture beyond e=32 toward the Cauchy mass cap",
        "production_heavy_run_armed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("DEPTH2_STATIC_FIRST_SUMMARY=" + json.dumps({
        "static_keys": len(static_keys),
        "highd_slices": len(static_rows),
        "depth2_pruned_keys": sum(r["depth2_pruned_keys"] for r in static_rows),
        "surviving_static_keys": sum(r["surviving_static_keys_after_depth2"] for r in static_rows),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
