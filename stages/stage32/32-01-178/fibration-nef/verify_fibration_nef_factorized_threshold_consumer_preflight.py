#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from bisect import bisect_right
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
WEIGHTED = HERE / "verify_fibration_nef_weighted_signature_counter_preflight.py"
QTHRESH = HERE / "verify_fibration_nef_picard_qexc_threshold_preflight.py"
LOCKS = {
    "weighted_signature_counter": (WEIGHTED, "be2817633e1ef60e0415927889e1d589bec99aa4"),
    "picard_qexc_threshold": (QTHRESH, "c583466ff865c0dcf33c19879cf4936e35983e83"),
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


def convolve_qhist(aq: Counter[int], hq: Counter[int], qcap: int) -> Counter[int]:
    out: Counter[int] = Counter()
    for qa, ma in aq.items():
        for qh, mh in hq.items():
            q = qa + qh
            if q <= qcap:
                out[q] += ma * mh
    return out


def cumulative(poly: Counter[int], threshold: int | None) -> int:
    if threshold is None or threshold < 0:
        return 0
    qs = sorted(poly)
    pos = bisect_right(qs, int(threshold))
    return sum(poly[q] for q in qs[:pos])


def grf04_absolute_qcap(g: int, d: int) -> int:
    # qexc/2 <= d^2/16+d+2-2g after dropping the nonnegative static-rho
    # and residual-penalty terms.  This is only an absolute safe cap.
    return (d * d) // 8 + 2 * d + 4 - 4 * g


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    weighted = load_module(WEIGHTED, "stage32_178_factorized_weighted")
    qthr = load_module(QTHRESH, "stage32_178_factorized_qthreshold")

    # Re-run each producer's own dependency locks before load-bearing use.
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_factorized_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_factorized_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_factorized_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_factorized_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_factorized_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_factorized_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    sys.path.insert(0, str(RES))
    from compressed_terminal_family import exceptional_terminal_count  # noqa: E402
    from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402

    # Full exceptional-family regression for selected small exact strata and
    # exact x4 slices.  No terminal sampling is used inside a selected slice.
    cases = [
        (0, 8, 0, 0),
        (0, 8, 1, 0),
        (0, 8, 2, 0),
        (1, 8, 2, 0),
        (0, 10, 3, 1),
        (1, 10, 4, 2),
    ]
    rows = []
    total_static_searches = 0
    total_min_nodes = 0

    for g, d, e, x4 in cases:
        qcap = grf04_absolute_qcap(g, d)
        limit, apoly, hpoly = weighted.build_factorized_counter(e, qcap)
        indexer = CompressedTerminalIndexer(e=e, d=d)
        req(0 <= x4 <= indexer.normal_budget, "selected x4 outside production range")

        threshold_cache: dict[tuple[int, int, int, int], int | None] = {}
        factorized_total = 0
        factorized_accepted = 0
        factorized_rejected = 0

        for a, aq in apoly.items():
            for (b, c, t), hq in hpoly.items():
                if a + b + c > e:
                    continue
                qhist = convolve_qhist(aq, hq, qcap)
                mass = sum(qhist.values())
                if not mass:
                    continue
                key = (a, b, c, t)
                zero_problem = sigmod.signature_problem(
                    bnb, kernel, g=g, d=d, e=e,
                    sig=(a, b, c, t, x4, 0),
                )
                if zero_problem.get("structurally_infeasible"):
                    threshold = None
                    req(zero_problem.get("reason") in {
                        "e_minus_M10_negative",
                        "nef_block_0_already_negative",
                        "nef_block_1_already_negative",
                        "nef_block_2_already_negative",
                        "nef_block_3_already_negative",
                        "nef_block_4_already_negative",
                        "nef_block_5_already_negative",
                        "nef_simplex_empty",
                        "already_rejected_by_GRF04",
                    }, f"unexpected structural failure {zero_problem.get('reason')}")
                else:
                    minimum, _witness, stats = qthr.picard_min_penalty(
                        prefix, leaf, bnb, kernel, zero_problem, cert,
                        static_values=(a, b, c, t, x4, e, d),
                    )
                    _exact_cut, threshold = qthr.qexc_threshold(
                        g=g, d=d, t=t, x4=x4, min_penalty=minimum
                    )
                    total_min_nodes += stats.visited_nodes
                threshold_cache[key] = threshold
                total_static_searches += 1
                accepted = cumulative(qhist, threshold)
                factorized_total += mass
                factorized_accepted += accepted
                factorized_rejected += mass - accepted

        req(factorized_total == exceptional_terminal_count(e),
            f"factorized exceptional mass mismatch g={g} d={d} e={e} x4={x4}")

        direct_total = 0
        direct_accepted = 0
        stride = indexer.normal_budget + 1
        for exceptional_rank in range(indexer.exceptional_count):
            rank = exceptional_rank * stride + x4
            x = indexer.unrank(rank)
            req(indexer.rank(x) == rank, "canonical indexer roundtrip regression")
            a, b, c, t, observed_x4, qexc = sigmod.aggregate(x)
            req(observed_x4 == x4, "x4 slice drift")
            threshold = threshold_cache[(a, b, c, t)]
            direct_total += 1
            direct_accepted += int(threshold is not None and qexc <= threshold)

        req(direct_total == factorized_total,
            f"direct/factorized total mismatch g={g} d={d} e={e} x4={x4}")
        req(direct_accepted == factorized_accepted,
            f"direct/factorized accepted mismatch g={g} d={d} e={e} x4={x4}")

        rows.append({
            "g": g,
            "d": d,
            "e": e,
            "x4": x4,
            "absolute_qcap": qcap,
            "effective_mass_cap": limit,
            "static_signature_count": len(threshold_cache),
            "exceptional_terminal_multiplicity": str(factorized_total),
            "accepted_by_exact_picard_qexc_threshold": str(factorized_accepted),
            "rejected_by_exact_picard_qexc_threshold": str(factorized_rejected),
            "canonical_indexer_exact_match": True,
        })

    out = {
        "schema": "STAGE32_32_01_178_FACTORIZED_THRESHOLD_CONSUMER_PREFLIGHT_V1",
        "purpose": "connect the exact A[a](z)H[b,c,t](z) production counter directly to the exact Picard qexc-threshold consumer and charge whole qexc multiplicities without terminal materialization",
        "exact_composition": {
            "static_key": ["a", "b", "c", "t", "x4", "e", "d", "g"],
            "picard_minimization_runs_per_static_key": 1,
            "accepted_multiplicity": "sum_{qexc<=threshold(static)} [z^qexc] A[a](z)H[b,c,t](z)",
            "terminal_by_terminal_picard_search_required": False,
            "five_dimensional_signature_table_required": False,
            "qexc_truncation_safe": True,
        },
        "bounded_exact_regression": {
            "selected_exact_x4_slices": len(rows),
            "all_exceptional_terminals_in_each_slice_checked": True,
            "canonical_indexer_match": True,
            "static_picard_minimum_searches": total_static_searches,
            "aggregate_picard_min_search_nodes": total_min_nodes,
            "rows": rows,
        },
        "next_exact_step": "add static lower-envelope pruning for qexc before Picard minimization, then run a bounded real high-d production slice with the factorized consumer and measure static-key compression",
        "production_full178_run": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("FACTORIZED_THRESHOLD_CONSUMER_SUMMARY=" + json.dumps({
        "cases": len(rows),
        "static_searches": total_static_searches,
        "min_nodes": total_min_nodes,
        "strict_cases": sum(int(int(r["rejected_by_exact_picard_qexc_threshold"]) > 0) for r in rows),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
