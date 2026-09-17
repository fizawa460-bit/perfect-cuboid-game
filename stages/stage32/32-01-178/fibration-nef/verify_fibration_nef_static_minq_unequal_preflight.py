#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARITY = HERE / "verify_fibration_nef_parity_quotient_weighted_counter_preflight.py"
PARITY_BLOB = "051dd67a3317194f743314340722eb15efd44a40"


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


def a_min_q_closed(a: int) -> int:
    """Minimum x2^2+x3^2+x7^2 over nonnegative triples summing to a."""
    k, r = divmod(int(a), 3)
    return (3 - r) * k * k + r * (k + 1) * (k + 1)


def unequal_static_minq(limit: int, qcap: int):
    """Exact min-plus DP for the x0<x1 H branch.

    The static depth-2 envelope needs only support and the minimum possible qH
    for each (b,c,t).  Because every later coordinate contributes a
    nonnegative square and the transition depends only on (b,c,t), retaining
    only the smallest q at each static key is exact for support/min-q.  The
    parity quotient is applied at the final boundary as c==t (mod 2).
    """
    inf = 10**100
    states: dict[tuple[int, int, int], int] = {}
    vmax = min(limit, math.isqrt(qcap))
    for x0 in range(vmax + 1):
        for x1 in range(x0 + 1, vmax + 1):
            if x0 + x1 > limit:
                break
            q = x0 * x0 + x1 * x1
            if q > qcap:
                break
            key = (x1, x0, x0 + x1)
            if q < states.get(key, inf):
                states[key] = q

    state_counts = [len(states)]
    specs = (
        (1, 0, 0),  # x5
        (0, 1, 1),  # x6
        (0, 1, 0),  # x8
        (1, 0, 1),  # x9
        (0, 1, 0),  # x10
    )
    for db, dc, dt in specs:
        nxt: dict[tuple[int, int, int], int] = {}
        for (b, c, t), q in states.items():
            vmax2 = min(limit - b - c, math.isqrt(qcap - q))
            for value in range(vmax2 + 1):
                key = (b + db * value, c + dc * value, t + dt * value)
                q2 = q + value * value
                if q2 < nxt.get(key, inf):
                    nxt[key] = q2
        states = nxt
        state_counts.append(len(states))

    out = {
        key: q for key, q in states.items()
        if ((key[1] - key[2]) & 1) == 0
    }
    return out, state_counts


def main() -> None:
    req(PARITY.is_file(), "missing parity-quotient producer")
    req(git_blob(PARITY) == PARITY_BLOB, "parity-quotient producer drift")
    parity = load_module(PARITY, "stage32_178_static_minq_parity")

    req(parity.WEIGHTED.is_file(), "missing retained weighted producer")
    req(parity.git_blob(parity.WEIGHTED) == parity.WEIGHTED_BLOB,
        "retained weighted producer drift")
    weighted = parity.load_module(parity.WEIGHTED, "stage32_178_static_minq_weighted")
    weighted.lock_sources_before_import()

    regressions = []
    for e in range(0, 15):
        for qcap in sorted({e * e, (e * e) // 2}):
            quotient, qstates = parity.parity_quotient_unequal_with_stats(e, qcap)
            static, sstates = unequal_static_minq(e, qcap)
            expected = {key: min(poly) for key, poly in quotient.items()}
            req(static == expected,
                f"static min-plus unequal map mismatch e={e} qcap={qcap}")

            apoly = weighted.triple_a_polynomials(e, qcap)
            for a, poly in apoly.items():
                req(min(poly) == a_min_q_closed(a),
                    f"closed A min-q mismatch e={e} qcap={qcap} a={a}")

            regressions.append({
                "e": e,
                "qcap": qcap,
                "quotient_full_q_state_peak": max(qstates, default=0),
                "static_minq_state_peak": max(sstates, default=0),
                "unequal_static_keys": len(static),
            })

    # Same real production regime as the current depth-2 high-d telemetry.
    highd_e = 32
    highd_qcap = 4992
    quotient_highd, quotient_states = parity.parity_quotient_unequal_with_stats(
        highd_e, highd_qcap
    )
    static_highd, static_states = unequal_static_minq(highd_e, highd_qcap)
    expected_highd = {key: min(poly) for key, poly in quotient_highd.items()}
    req(static_highd == expected_highd,
        "g1-d192/e32 static min-plus map changed unequal support/min-q")

    qpeak = max(quotient_states)
    speak = max(static_states)
    req(speak <= qpeak, "static min-plus unexpectedly increased state peak")

    out = {
        "schema": "STAGE32_32_01_178_STATIC_MINQ_UNEQUAL_PREFLIGHT_V1",
        "purpose": "move the depth-2 static-envelope decision ahead of full qexc-polynomial materialization on the x0<x1 branch by computing exact static support and minimum qH with min-plus DP",
        "exactness": {
            "branch": "x0<x1",
            "state": ["b", "c", "t"],
            "q_dimension_materialized": False,
            "kept_value": "minimum qH for each static key",
            "transition_costs_nonnegative_squares": True,
            "support_exact_under_qcap": True,
            "parity_filter": "c == t (mod 2)",
            "A_min_q_closed_formula": "if a=3k+r, min qA=(3-r)k^2+r(k+1)^2",
        },
        "bounded_exact_regression": {
            "e_range": [0, 14],
            "qcap_modes": ["floor(e^2/2)", "e^2"],
            "all_static_minq_maps_match_full_parity_quotient_histograms": True,
            "rows": regressions,
        },
        "real_highd_telemetry": {
            "row_id": "g1-d192",
            "e": highd_e,
            "absolute_qcap": highd_qcap,
            "unequal_static_keys": len(static_highd),
            "full_q_quotient_state_peak": qpeak,
            "static_minq_state_peak": speak,
            "state_peak_reduction": qpeak - speak,
            "state_peak_retained_fraction": f"{speak}/{qpeak}",
            "support_and_min_q_exact_match": True,
        },
        "remaining_boundary": "derive the analogous static support/min-q producer for the x0=x1 pair-lex branch; then depth-2 can prune the complete H static family before any qexc histogram is built",
        "production_heavy_run_armed": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("STATIC_MINQ_UNEQUAL_SUMMARY=" + json.dumps({
        "regression_cases": len(regressions),
        "highd_static_keys": len(static_highd),
        "highd_full_q_state_peak": qpeak,
        "highd_static_minq_state_peak": speak,
        "highd_state_peak_reduction": qpeak - speak,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
