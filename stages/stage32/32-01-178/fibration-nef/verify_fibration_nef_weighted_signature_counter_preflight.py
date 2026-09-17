#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from bisect import bisect_right
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
FAMILY = RES / "compressed_terminal_family.py"
INDEXER = RES / "compressed_terminal_indexer.py"
SIGNATURE = HERE / "verify_fibration_nef_signature_factorization.py"
SOURCE_LOCKS = {
    "compressed_terminal_family": (FAMILY, "90ff82ed312dcc0cb32cf207935945f550e29170"),
    "compressed_terminal_indexer": (INDEXER, "4fb0a8dd34909494bd62646373e42877ed7a3c9e"),
    "signature_factorization": (SIGNATURE, "eaa1351f3da2d18cbc4ee9525e3447b665e753dd"),
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


def lock_sources_before_import() -> None:
    for name, (path, expected) in SOURCE_LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")


def effective_mass_cap(e: int, qcap: int) -> int:
    """Exact exceptional-mass cap for qexc<=qcap.

    There are ten exceptional coordinates.  Cauchy gives
    (sum xi)^2 <= 10*sum xi^2 = 10*qexc, so no qexc<=qcap terminal can have
    exceptional mass above floor(sqrt(10*qcap)).
    """
    return min(int(e), math.isqrt(10 * int(qcap)))


def triple_a_polynomials(limit: int, qcap: int) -> dict[int, Counter[int]]:
    """A[a](z): x2+x3+x7=a, weighted by z^(x2^2+x3^2+x7^2)."""
    out: dict[int, Counter[int]] = defaultdict(Counter)
    vmax = min(limit, math.isqrt(qcap))
    for x2 in range(vmax + 1):
        q2 = x2 * x2
        for x3 in range(min(limit - x2, math.isqrt(qcap - q2)) + 1):
            q23 = q2 + x3 * x3
            for x7 in range(min(limit - x2 - x3, math.isqrt(qcap - q23)) + 1):
                q = q23 + x7 * x7
                out[x2 + x3 + x7][q] += 1
    return dict(out)


def unequal_h_polynomials(limit: int, qcap: int) -> dict[tuple[int, int, int], Counter[int]]:
    """H[b,c,t](z) for the x0<x1 canonical branch.

    State compression is exact because b+c is precisely the mass of these
    seven variables and the only remaining global condition is the retained
    parity x1+x8+x9+x10 == 0 (mod 2).
    """
    states: Counter[tuple[int, int, int, int, int, int]] = Counter()
    vmax = min(limit, math.isqrt(qcap))
    for x0 in range(vmax + 1):
        for x1 in range(x0 + 1, vmax + 1):
            if x0 + x1 > limit:
                break
            q = x0 * x0 + x1 * x1
            if q > qcap:
                break
            # b,c,t,q, parity(x8+x9+x10 so far), required parity
            states[(x1, x0, x0 + x1, q, 0, x1 & 1)] += 1

    # x5, x6, x8, x9, x10 contributions to (b,c,t,tail-parity).
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

    out: dict[tuple[int, int, int], Counter[int]] = defaultdict(Counter)
    for (b, c, t, q, parity, target), multiplicity in states.items():
        if parity == target:
            out[(b, c, t)][q] += multiplicity
    return dict(out)


def equal_h_polynomials(limit: int, qcap: int) -> dict[tuple[int, int, int], Counter[int]]:
    """H[b,c,t](z) for x0=x1 with the exact pair-lex canonical filter."""
    out: dict[tuple[int, int, int], Counter[int]] = defaultdict(Counter)
    for s in range(limit // 2 + 1):
        q0 = 2 * s * s
        if q0 > qcap:
            break
        rem = limit - 2 * s
        for x5 in range(min(rem, math.isqrt(qcap - q0)) + 1):
            q5 = q0 + x5 * x5
            rem5 = rem - x5
            for x6 in range(min(rem5, math.isqrt(qcap - q5)) + 1):
                q6 = q5 + x6 * x6
                rem6 = rem5 - x6
                for x8 in range(min(rem6, math.isqrt(qcap - q6)) + 1):
                    q8 = q6 + x8 * x8
                    rem8 = rem6 - x8
                    for x9 in range(min(rem8, math.isqrt(qcap - q8)) + 1):
                        if (x5, x6) > (x8, x9):
                            continue
                        q9 = q8 + x9 * x9
                        rem9 = rem8 - x9
                        x10_parity = (s ^ ((x8 + x9) & 1)) & 1
                        vmax10 = min(rem9, math.isqrt(qcap - q9))
                        for x10 in range(x10_parity, vmax10 + 1, 2):
                            q = q9 + x10 * x10
                            b = s + x5 + x9
                            c = s + x6 + x8 + x10
                            t = 2 * s + x6 + x9
                            out[(b, c, t)][q] += 1
    return dict(out)


def bc_h_polynomials(limit: int, qcap: int) -> dict[tuple[int, int, int], Counter[int]]:
    out: dict[tuple[int, int, int], Counter[int]] = defaultdict(Counter)
    for branch in (unequal_h_polynomials(limit, qcap), equal_h_polynomials(limit, qcap)):
        for key, poly in branch.items():
            out[key].update(poly)
    return dict(out)


def build_factorized_counter(e: int, qcap: int):
    limit = effective_mass_cap(e, qcap)
    return limit, triple_a_polynomials(limit, qcap), bc_h_polynomials(limit, qcap)


def materialize_signature_hist(
    e: int,
    qcap: int,
    apoly: dict[int, Counter[int]],
    hpoly: dict[tuple[int, int, int], Counter[int]],
) -> Counter[tuple[int, int, int, int, int]]:
    out: Counter[tuple[int, int, int, int, int]] = Counter()
    for a, aq in apoly.items():
        for (b, c, t), hq in hpoly.items():
            if a + b + c > e:
                continue
            for qa, ma in aq.items():
                for qh, mh in hq.items():
                    q = qa + qh
                    if q <= qcap:
                        out[(a, b, c, t, q)] += ma * mh
    return out


def direct_index_hist(indexer_cls, aggregate, *, e: int, qcap: int) -> Counter[tuple[int, int, int, int, int]]:
    # Any d with nonnegative normal budget is valid because the exceptional
    # family is d-independent.  x4 is fixed to zero by choosing the first rank
    # of every exceptional block.
    d = max(e, 2)
    indexer = indexer_cls(e=e, d=d)
    stride = indexer.normal_budget + 1
    out: Counter[tuple[int, int, int, int, int]] = Counter()
    for exceptional_rank in range(indexer.exceptional_count):
        x = indexer.unrank(exceptional_rank * stride)
        req(x[4] == 0, "exceptional-rank projection did not fix x4=0")
        a, b, c, t, _x4, qexc = aggregate(x)
        if qexc <= qcap:
            out[(a, b, c, t, qexc)] += 1
    return out


def factorized_qcapped_total(
    e: int,
    qcap: int,
    apoly: dict[int, Counter[int]],
    hpoly: dict[tuple[int, int, int], Counter[int]],
) -> int:
    # Do not materialize the five-dimensional signature table.  Prefix-sum each
    # H polynomial and answer the q-convolution cumulatively.
    indexed_h = {}
    for key, poly in hpoly.items():
        qs = sorted(poly)
        running = 0
        prefix = []
        for q in qs:
            running += poly[q]
            prefix.append(running)
        indexed_h[key] = (qs, prefix)

    total = 0
    for a, aq in apoly.items():
        for (b, c, t), (qs, prefix) in indexed_h.items():
            if a + b + c > e:
                continue
            for qa, ma in aq.items():
                pos = bisect_right(qs, qcap - qa) - 1
                if pos >= 0:
                    total += ma * prefix[pos]
    return total


def main() -> None:
    lock_sources_before_import()
    sys.path.insert(0, str(RES))
    from compressed_terminal_family import exceptional_terminal_count  # noqa: E402
    from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402

    sigmod = load_module(SIGNATURE, "stage32_178_weighted_counter_signature")

    regressions = []
    for e in range(0, 11):
        for qcap in sorted({e * e, (e * e) // 2}):
            limit, apoly, hpoly = build_factorized_counter(e, qcap)
            factored = materialize_signature_hist(e, qcap, apoly, hpoly)
            direct = direct_index_hist(
                CompressedTerminalIndexer, sigmod.aggregate, e=e, qcap=qcap
            )
            req(factored == direct, f"factorized/indexed histogram mismatch e={e} qcap={qcap}")
            total = sum(factored.values())
            cumulative = factorized_qcapped_total(e, qcap, apoly, hpoly)
            req(cumulative == total, f"factorized cumulative mismatch e={e} qcap={qcap}")
            if qcap == e * e:
                req(total == exceptional_terminal_count(e),
                    f"full-q exceptional count mismatch e={e}")
            regressions.append({
                "e": e,
                "qcap": qcap,
                "effective_mass_cap": limit,
                "a_polynomial_terms": sum(len(v) for v in apoly.values()),
                "h_polynomial_keys": len(hpoly),
                "h_polynomial_terms": sum(len(v) for v in hpoly.values()),
                "materialized_signature_terms": len(factored),
                "qcap_terminal_multiplicity": str(total),
            })

    # Medium bounded telemetry: large enough to expose state growth while still
    # deliberately remaining a preflight rather than a production census.
    telemetry_e = 24
    telemetry_qcap = 576
    tlimit, tapoly, thpoly = build_factorized_counter(telemetry_e, telemetry_qcap)
    telemetry_total = factorized_qcapped_total(
        telemetry_e, telemetry_qcap, tapoly, thpoly
    )

    # Current GRF04-only absolute qexc ceiling at d=192 is <=4996 (g=0).
    # Record the Cauchy consequence without attempting a FULL178 census here.
    production_qcap_ceiling = 4996
    production_mass_cap_ceiling = effective_mass_cap(729, production_qcap_ceiling)

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_WEIGHTED_SIGNATURE_COUNTER_PREFLIGHT_V1",
        "purpose": "factor the exact production exceptional-terminal weighted counter into qexc polynomials A[a](z) and H[b,c,t](z), avoiding immediate materialization of the full (a,b,c,t,qexc) table",
        "exact_factorization": {
            "A_variables": ["x2", "x3", "x7"],
            "A_observable": "a=x2+x3+x7",
            "H_variables": ["x0", "x1", "x5", "x6", "x8", "x9", "x10"],
            "H_observables": ["b", "c", "t"],
            "exceptional_mass_identity": "a+b+c=sum(x_i for i!=4)",
            "qexc_identity": "qA+qH",
            "signature_multiplicity": "[z^qexc] A[a](z)*H[b,c,t](z) when a+b+c<=e",
            "qcap_truncation_exact": True,
            "cauchy_mass_cap": "sum_exceptional <= floor(sqrt(10*qcap))",
            "x4_independent_of_exceptional_family": True,
        },
        "bounded_exact_regression": {
            "cases": len(regressions),
            "e_range": [0, 10],
            "qcap_modes": ["floor(e^2/2)", "e^2"],
            "all_factorized_histograms_match_canonical_indexer": True,
            "full_q_cases_match_exceptional_terminal_count": True,
            "rows": regressions,
        },
        "medium_bounded_telemetry": {
            "e": telemetry_e,
            "qcap": telemetry_qcap,
            "effective_mass_cap": tlimit,
            "a_polynomial_keys": len(tapoly),
            "a_polynomial_terms": sum(len(v) for v in tapoly.values()),
            "h_polynomial_keys": len(thpoly),
            "h_polynomial_terms": sum(len(v) for v in thpoly.values()),
            "qcap_terminal_multiplicity": str(telemetry_total),
            "five_dimensional_signature_table_materialized": False,
        },
        "production_ceiling_observation": {
            "d": 192,
            "grf04_only_qexc_ceiling_g0": production_qcap_ceiling,
            "certified_e_max": 729,
            "cauchy_effective_exceptional_mass_cap": production_mass_cap_ceiling,
            "full178_counter_run": False,
        },
        "next_exact_step": "connect the qexc-threshold Picard consumer directly to the factorized A/H polynomials and evaluate cumulative qexc mass on demand, without constructing the full five-dimensional weighted signature table",
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("WEIGHTED_SIGNATURE_COUNTER_SUMMARY=" + json.dumps({
        "regression_cases": len(regressions),
        "telemetry_e": telemetry_e,
        "telemetry_qcap": telemetry_qcap,
        "telemetry_A_terms": sum(len(v) for v in tapoly.values()),
        "telemetry_H_terms": sum(len(v) for v in thpoly.values()),
        "production_mass_cap_ceiling": production_mass_cap_ceiling,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
