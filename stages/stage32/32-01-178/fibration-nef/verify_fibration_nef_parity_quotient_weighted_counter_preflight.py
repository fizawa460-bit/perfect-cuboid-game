#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
WEIGHTED = HERE / "verify_fibration_nef_weighted_signature_counter_preflight.py"
WEIGHTED_BLOB = "be2817633e1ef60e0415927889e1d589bec99aa4"


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


def legacy_unequal_with_stats(limit: int, qcap: int):
    """Exact copy of the retained unequal-branch DP, instrumented only for state counts."""
    states: Counter[tuple[int, int, int, int, int, int]] = Counter()
    vmax = min(limit, math.isqrt(qcap))
    for x0 in range(vmax + 1):
        for x1 in range(x0 + 1, vmax + 1):
            if x0 + x1 > limit:
                break
            q = x0 * x0 + x1 * x1
            if q > qcap:
                break
            states[(x1, x0, x0 + x1, q, 0, x1 & 1)] += 1

    state_counts = [len(states)]
    specs = (
        (1, 0, 0, 0),
        (0, 1, 1, 0),
        (0, 1, 0, 1),
        (1, 0, 1, 1),
        (0, 1, 0, 1),
    )
    for db, dc, dt, toggles_parity in specs:
        nxt: Counter[tuple[int, int, int, int, int, int]] = Counter()
        for (b, c, t, q, parity, target), multiplicity in states.items():
            vmax2 = min(limit - b - c, math.isqrt(qcap - q))
            for value in range(vmax2 + 1):
                nxt[(
                    b + db * value,
                    c + dc * value,
                    t + dt * value,
                    q + value * value,
                    parity ^ ((value & 1) if toggles_parity else 0),
                    target,
                )] += multiplicity
        states = nxt
        state_counts.append(len(states))

    out: dict[tuple[int, int, int], Counter[int]] = defaultdict(Counter)
    for (b, c, t, q, parity, target), multiplicity in states.items():
        if parity == target:
            out[(b, c, t)][q] += multiplicity
    return dict(out), state_counts


def parity_quotient_unequal_with_stats(limit: int, qcap: int):
    """Exact quotient of the unequal-branch DP by its redundant parity coordinates.

    With
      c=x0+x6+x8+x10,
      t=x0+x1+x6+x9,
    we have
      c+t == x1+x8+x9+x10 (mod 2).
    Hence the retained parity condition is exactly c==t (mod 2).  The explicit
    running parity and target bits carry no information not already present in
    (c,t), so they can be dropped from every intermediate DP state and checked
    once at the output boundary.
    """
    states: Counter[tuple[int, int, int, int]] = Counter()
    vmax = min(limit, math.isqrt(qcap))
    for x0 in range(vmax + 1):
        for x1 in range(x0 + 1, vmax + 1):
            if x0 + x1 > limit:
                break
            q = x0 * x0 + x1 * x1
            if q > qcap:
                break
            states[(x1, x0, x0 + x1, q)] += 1

    state_counts = [len(states)]
    # x5, x6, x8, x9, x10 contributions to (b,c,t).
    specs = (
        (1, 0, 0),
        (0, 1, 1),
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0),
    )
    for db, dc, dt in specs:
        nxt: Counter[tuple[int, int, int, int]] = Counter()
        for (b, c, t, q), multiplicity in states.items():
            vmax2 = min(limit - b - c, math.isqrt(qcap - q))
            for value in range(vmax2 + 1):
                nxt[(
                    b + db * value,
                    c + dc * value,
                    t + dt * value,
                    q + value * value,
                )] += multiplicity
        states = nxt
        state_counts.append(len(states))

    out: dict[tuple[int, int, int], Counter[int]] = defaultdict(Counter)
    for (b, c, t, q), multiplicity in states.items():
        if ((c - t) & 1) == 0:
            out[(b, c, t)][q] += multiplicity
    return dict(out), state_counts


def parity_quotient_unequal_h_polynomials(limit: int, qcap: int):
    out, _stats = parity_quotient_unequal_with_stats(limit, qcap)
    return out


def parity_quotient_bc_h_polynomials(weighted, limit: int, qcap: int):
    out: dict[tuple[int, int, int], Counter[int]] = defaultdict(Counter)
    for branch in (
        parity_quotient_unequal_h_polynomials(limit, qcap),
        weighted.equal_h_polynomials(limit, qcap),
    ):
        for key, poly in branch.items():
            out[key].update(poly)
    return dict(out)


def build_factorized_counter(weighted, e: int, qcap: int):
    limit = weighted.effective_mass_cap(e, qcap)
    return (
        limit,
        weighted.triple_a_polynomials(limit, qcap),
        parity_quotient_bc_h_polynomials(weighted, limit, qcap),
    )


def main() -> None:
    req(WEIGHTED.is_file(), "missing retained weighted counter")
    req(git_blob(WEIGHTED) == WEIGHTED_BLOB, "retained weighted counter source drift")
    weighted = load_module(WEIGHTED, "stage32_178_parity_quotient_weighted")
    weighted.lock_sources_before_import()

    # Exhaust the parity classes themselves: the identity
    # c+t-(x1+x8+x9+x10)=2*x0+2*x6 implies exact equivalence of the two tests.
    for x0 in (0, 1):
        for x1 in (0, 1):
            for x6 in (0, 1):
                for x8 in (0, 1):
                    for x9 in (0, 1):
                        for x10 in (0, 1):
                            c = x0 + x6 + x8 + x10
                            t = x0 + x1 + x6 + x9
                            retained_even = ((x1 + x8 + x9 + x10) & 1) == 0
                            quotient_even = ((c - t) & 1) == 0
                            req(retained_even == quotient_even,
                                "parity quotient identity regression")

    regressions = []
    for e in range(0, 15):
        for qcap in sorted({e * e, (e * e) // 2}):
            legacy = weighted.unequal_h_polynomials(e, qcap)
            quotient, qstates = parity_quotient_unequal_with_stats(e, qcap)
            req(legacy == quotient,
                f"parity quotient changed unequal histogram e={e} qcap={qcap}")
            req(all(((c - t) & 1) == 0 for (b, c, t) in quotient),
                f"quotient emitted parity-invalid H key e={e} qcap={qcap}")
            regressions.append({
                "e": e,
                "qcap": qcap,
                "quotient_state_peak": max(qstates, default=0),
                "unequal_h_keys": len(quotient),
                "unequal_h_terms": sum(len(poly) for poly in quotient.values()),
            })

    # Real high-d counter regime used by the current lower-envelope telemetry.
    # At e=32 every exceptional vector has qexc<=e^2=1024, so the retained
    # g1-d192 absolute qcap 4992 is inactive for this exceptional subfamily.
    highd_e = 32
    highd_qcap = 4992
    legacy_highd, legacy_states = legacy_unequal_with_stats(highd_e, highd_qcap)
    quotient_highd, quotient_states = parity_quotient_unequal_with_stats(
        highd_e, highd_qcap
    )
    req(legacy_highd == quotient_highd,
        "high-d e32 parity quotient changed exact unequal histogram")
    req(legacy_highd == weighted.unequal_h_polynomials(highd_e, highd_qcap),
        "instrumented legacy DP drifted from retained weighted producer")

    old_peak = max(legacy_states)
    new_peak = max(quotient_states)
    req(new_peak <= old_peak, "parity quotient unexpectedly increased DP state peak")

    # Full A/H producer equality at the same real production parameters.
    old_counter = weighted.build_factorized_counter(highd_e, highd_qcap)
    new_counter = build_factorized_counter(weighted, highd_e, highd_qcap)
    req(old_counter == new_counter,
        "parity quotient changed full factorized counter at g1-d192/e32 qcap")

    out = {
        "schema": "STAGE32_32_01_178_PARITY_QUOTIENT_WEIGHTED_COUNTER_PREFLIGHT_V1",
        "purpose": "remove redundant parity/target coordinates from the unequal H weighted-counter DP using the exact identity x1+x8+x9+x10 even iff c and t have equal parity",
        "exact_identity": {
            "c": "x0+x6+x8+x10",
            "t": "x0+x1+x6+x9",
            "c_plus_t_mod2": "x1+x8+x9+x10 (mod 2)",
            "retained_parity_condition": "c == t (mod 2)",
            "running_parity_coordinate_required": False,
            "parity_target_coordinate_required": False,
        },
        "bounded_exact_regression": {
            "e_range": [0, 14],
            "qcap_modes": ["floor(e^2/2)", "e^2"],
            "all_quotient_histograms_match_retained_unequal_dp": True,
            "rows": regressions,
        },
        "real_highd_counter_telemetry": {
            "row_id": "g1-d192",
            "e": highd_e,
            "absolute_qcap": highd_qcap,
            "qcap_inactive_for_e32_exceptional_family": True,
            "legacy_unequal_state_peak": old_peak,
            "parity_quotient_unequal_state_peak": new_peak,
            "state_peak_reduction": old_peak - new_peak,
            "state_peak_retained_fraction": f"{new_peak}/{old_peak}",
            "full_factorized_counter_exact_match": True,
        },
        "next_exact_step": "substitute this drop-in factorized counter into the depth-2 high-d lower-envelope telemetry, then move the static-envelope filter ahead of q-polynomial materialization for larger e",
        "production_heavy_run_armed": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("PARITY_QUOTIENT_COUNTER_SUMMARY=" + json.dumps({
        "regression_cases": len(regressions),
        "highd_e": highd_e,
        "legacy_state_peak": old_peak,
        "quotient_state_peak": new_peak,
        "state_peak_reduction": old_peak - new_peak,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
