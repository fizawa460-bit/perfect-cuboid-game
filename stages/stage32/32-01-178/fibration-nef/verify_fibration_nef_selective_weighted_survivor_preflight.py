#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from bisect import bisect_right
from collections import Counter
from pathlib import Path

import sympy

HERE = Path(__file__).resolve().parent
STATIC_FIRST = HERE / "verify_fibration_nef_depth2_static_first_highd_preflight.py"
STATIC_FIRST_BLOB = "51ecf6a2a676afc7449abe95b4ee910122c4dfda"


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


def a_poly_for_key(a: int, qcap: int) -> Counter[int]:
    """Exact A[a](z) without generating unrelated a-values."""
    out: Counter[int] = Counter()
    a = int(a)
    for x2 in range(a + 1):
        for x3 in range(a - x2 + 1):
            x7 = a - x2 - x3
            q = x2 * x2 + x3 * x3 + x7 * x7
            if q <= qcap:
                out[q] += 1
    return out


def pair_split_spectrum(total: int) -> Counter[int]:
    """Exact q-spectrum of u^2+w^2 over u+w=total, u,w>=0."""
    out: Counter[int] = Counter()
    for u in range(int(total) + 1):
        w = int(total) - u
        out[u * u + w * w] += 1
    return out


def unequal_h_poly_for_key(b: int, c: int, t: int, qcap: int) -> Counter[int]:
    """Exact x0<x1 H polynomial for one static key.

    Put v=x9.  Then
      x5=b-x1-v,
      x6=t-x0-x1-v,
      x8+x10=c-t+x1+v.
    Thus only x0,x1,v and the final two-variable split remain.  The retained
    parity condition is exactly c==t (mod 2).
    """
    b, c, t, qcap = map(int, (b, c, t, qcap))
    out: Counter[int] = Counter()
    if min(b, c, t) < 0 or b + c < t or ((c - t) & 1):
        return out

    split_cache: dict[int, Counter[int]] = {}
    for x0 in range(c + 1):
        for x1 in range(x0 + 1, b + 1):
            vmax = min(b - x1, t - x0 - x1)
            if vmax < 0:
                continue
            for v in range(vmax + 1):
                x5 = b - x1 - v
                x6 = t - x0 - x1 - v
                pair_total = c - t + x1 + v
                if x5 < 0 or x6 < 0 or pair_total < 0:
                    continue
                base = x0 * x0 + x1 * x1 + x5 * x5 + x6 * x6 + v * v
                if base > qcap:
                    continue
                split = split_cache.setdefault(pair_total, pair_split_spectrum(pair_total))
                for qpair, multiplicity in split.items():
                    q = base + qpair
                    if q <= qcap:
                        out[q] += multiplicity
    return out


def equal_h_poly_for_key(b: int, c: int, t: int, qcap: int) -> Counter[int]:
    """Exact x0=x1 pair-lex H polynomial for one static key."""
    b, c, t, qcap = map(int, (b, c, t, qcap))
    out: Counter[int] = Counter()
    if min(b, c, t) < 0 or t > b + c or ((c - t) & 1):
        return out

    k = b + c - t
    p_lo = max(0, b - t)
    p_hi = min(b, k)
    for p in range(p_lo, p_hi + 1):
        a = t - b + p
        bb = b - p
        if a < 0 or bb < 0:
            continue
        s_hi = min(a, bb)
        pair_total = k - p
        pair_lower = p if 2 * p <= 2 * b - t else p + 1
        if pair_lower > pair_total:
            continue
        for s in range(s_hi + 1):
            x6 = a - s
            x9 = bb - s
            base = 2 * s * s + p * p + x6 * x6 + x9 * x9
            if base > qcap:
                continue
            for x8 in range(pair_lower, pair_total + 1):
                x10 = pair_total - x8
                q = base + x8 * x8 + x10 * x10
                if q <= qcap:
                    out[q] += 1
    return out


def h_poly_for_key(b: int, c: int, t: int, qcap: int) -> Counter[int]:
    out = unequal_h_poly_for_key(b, c, t, qcap)
    out.update(equal_h_poly_for_key(b, c, t, qcap))
    return out


def cumulative_product(aq: Counter[int], hq: Counter[int], threshold: int | None) -> int:
    if threshold is None or threshold < 0 or not aq or not hq:
        return 0
    qs = sorted(hq)
    prefix = []
    running = 0
    for q in qs:
        running += hq[q]
        prefix.append(running)
    total = 0
    for qa, ma in aq.items():
        pos = bisect_right(qs, int(threshold) - qa) - 1
        if pos >= 0:
            total += ma * prefix[pos]
    return total


def survivor_rows(
    *, sf, depth2, depth1, sigmod, prefix, bnb, kernel, cert,
    static_keys, g: int, d: int, e: int, x4_values,
):
    rows = []
    all_survivors = set()
    for x4 in x4_values:
        survivors = []
        thresholds = {}
        for a, b, c, t, min_q in static_keys:
            problem = sigmod.signature_problem(
                bnb, kernel, g=g, d=d, e=e,
                sig=(a, b, c, t, x4, 0),
            )
            if problem.get("structurally_infeasible"):
                continue
            static_values = (a, b, c, t, x4, e, d)
            lower2, _n0, _nres, _npts = depth2.two_coordinate_picard_lower_envelope_fast(
                prefix, bnb, kernel, problem, cert, static_values=static_values
            )
            _cut2, threshold2 = depth2.qthreshold(
                depth1, g=g, d=d, t=t, x4=x4, lower=lower2
            )
            if threshold2 is None or min_q > threshold2:
                continue
            key = (a, b, c, t)
            survivors.append(key)
            thresholds[key] = int(threshold2)
            all_survivors.add(key)
        rows.append((x4, tuple(survivors), thresholds))
    return rows, all_survivors


def main() -> None:
    req(STATIC_FIRST.is_file(), "missing static-first carrier")
    req(git_blob(STATIC_FIRST) == STATIC_FIRST_BLOB, "static-first carrier drift")
    sf = load_module(STATIC_FIRST, "stage32_178_selective_static_first")

    for name, (path, expected) in sf.LOCKS.items():
        req(path.is_file(), f"missing static-first source lock {name}")
        req(sf.git_blob(path) == expected, f"static-first source drift {name}")
    depth2 = sf.load_module(sf.DEPTH2, "stage32_178_selective_depth2")
    complete = sf.load_module(sf.COMPLETE, "stage32_178_selective_complete")

    req(depth2.DEPTH1.is_file(), "missing depth1 carrier")
    req(depth2.git_blob(depth2.DEPTH1) == depth2.DEPTH1_BLOB,
        "depth1 carrier drift")
    depth1 = depth2.load_module(depth2.DEPTH1, "stage32_178_selective_depth1")
    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file(), f"missing depth1 source lock {name}")
        req(depth1.git_blob(path) == expected, f"depth1 source drift {name}")

    weighted = depth1.load_module(depth1.WEIGHTED, "stage32_178_selective_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "stage32_178_selective_qthreshold")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_selective_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_selective_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_selective_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_selective_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_selective_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_selective_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    req(complete.UNEQUAL.is_file(), "missing unequal static min-q producer")
    req(complete.git_blob(complete.UNEQUAL) == complete.UNEQUAL_BLOB,
        "unequal static min-q producer drift")
    unequal = complete.load_module(complete.UNEQUAL, "stage32_178_selective_unequal")
    req(unequal.PARITY.is_file(), "missing parity quotient producer")
    req(unequal.git_blob(unequal.PARITY) == unequal.PARITY_BLOB,
        "parity quotient producer drift")
    parity = unequal.load_module(unequal.PARITY, "stage32_178_selective_parity")

    # Small exact regression: targeted polynomials reproduce every old key.
    regressions = []
    for e in range(0, 11):
        for qcap in sorted({e * e, (e * e) // 2}):
            full_a = weighted.triple_a_polynomials(e, qcap)
            for a, poly in full_a.items():
                req(a_poly_for_key(a, qcap) == poly,
                    f"targeted A polynomial mismatch e={e} qcap={qcap} a={a}")
            full_h = parity.parity_quotient_bc_h_polynomials(weighted, e, qcap)
            for key, poly in full_h.items():
                req(h_poly_for_key(*key, qcap) == poly,
                    f"targeted H polynomial mismatch e={e} qcap={qcap} key={key}")
            regressions.append({
                "e": e,
                "qcap": qcap,
                "A_keys": len(full_a),
                "H_keys": len(full_h),
                "H_q_terms": sum(len(poly) for poly in full_h.values()),
            })

    # Real production slice: first derive static depth-2 survivors without any
    # q histogram, then generate only A/H polynomials projected from survivors.
    g, d, e = 1, 192, 32
    qcap = (d * d) // 8 + 2 * d + 4 - 4 * g
    req(qcap == 4992, "g1-d192 qcap drift")
    limit = weighted.effective_mass_cap(e, qcap)
    unequal_h, _ustates = unequal.unequal_static_minq(limit, qcap)
    equal_h = complete.equal_static_minq(limit, qcap)
    hmin = complete.merge_static_minq(unequal_h, equal_h)

    static_keys = []
    for a in range(limit + 1):
        qa = unequal.a_min_q_closed(a)
        if qa > qcap:
            continue
        for (b, c, t), qh in hmin.items():
            if a + b + c > e:
                continue
            min_q = qa + qh
            if min_q <= qcap:
                static_keys.append((a, b, c, t, min_q))

    x4_values = (0, 24, 48, 72, 96)
    rows, survivor_union = survivor_rows(
        sf=sf, depth2=depth2, depth1=depth1, sigmod=sigmod,
        prefix=prefix, bnb=bnb, kernel=kernel, cert=cert,
        static_keys=static_keys, g=g, d=d, e=e, x4_values=x4_values,
    )
    needed_a = sorted({key[0] for key in survivor_union})
    needed_h = sorted({key[1:] for key in survivor_union})

    selective_a = {a: a_poly_for_key(a, qcap) for a in needed_a}
    selective_h = {key: h_poly_for_key(*key, qcap) for key in needed_h}
    req(all(selective_a[a] for a in selective_a), "empty targeted A polynomial")
    req(all(selective_h[key] for key in selective_h), "empty targeted H polynomial")

    # Full polynomials are an oracle only; the selective route itself does not
    # require them to decide which keys are generated.
    full_a = weighted.triple_a_polynomials(limit, qcap)
    full_h = parity.parity_quotient_bc_h_polynomials(weighted, limit, qcap)
    for a, poly in selective_a.items():
        req(full_a.get(a) == poly, f"high-d selective A mismatch a={a}")
    for key, poly in selective_h.items():
        req(full_h.get(key) == poly, f"high-d selective H mismatch key={key}")

    telemetry = []
    for x4, survivors, thresholds in rows:
        selective_mass = 0
        oracle_mass = 0
        for key in survivors:
            a, b, c, t = key
            threshold = min(qcap, thresholds[key])
            selective_mass += cumulative_product(
                selective_a[a], selective_h[(b, c, t)], threshold
            )
            oracle_mass += cumulative_product(
                full_a[a], full_h[(b, c, t)], threshold
            )
        req(selective_mass == oracle_mass,
            f"selective/oracle depth2-surviving mass mismatch x4={x4}")
        telemetry.append({
            "x4": x4,
            "surviving_static_keys": len(survivors),
            "depth2_envelope_surviving_weighted_mass": str(selective_mass),
        })

    full_h_terms = sum(len(poly) for poly in full_h.values())
    selective_h_terms = sum(len(poly) for poly in selective_h.values())
    out = {
        "schema": "STAGE32_32_01_178_SELECTIVE_WEIGHTED_SURVIVOR_PREFLIGHT_V1",
        "purpose": "materialize qexc polynomials only for depth-2 surviving static keys after the static-first envelope, instead of building the complete H weighted family before pruning",
        "exact_selective_generators": {
            "A": "one requested a at a time from x2+x3+x7=a",
            "H_unequal": "one requested (b,c,t) at a time using x5=b-x1-x9, x6=t-x0-x1-x9, x8+x10=c-t+x1+x9",
            "H_equal": "one requested (b,c,t) at a time using the retained p=x5 pair-lex reduction",
            "parity": "c == t (mod 2)",
            "non_survivor_H_polynomials_materialized": False,
        },
        "bounded_exact_regression": {
            "e_range": [0, 10],
            "qcap_modes": ["floor(e^2/2)", "e^2"],
            "all_targeted_A_polynomials_match_full_counter": True,
            "all_targeted_H_polynomials_match_full_counter": True,
            "rows": regressions,
        },
        "real_highd_selective_telemetry": {
            "row_id": "g1-d192",
            "e": e,
            "absolute_qcap": qcap,
            "x4_slices": list(x4_values),
            "static_keys_before_depth2": len(static_keys),
            "union_surviving_static_keys": len(survivor_union),
            "requested_A_keys": len(needed_a),
            "requested_H_keys": len(needed_h),
            "full_H_keys_oracle": len(full_h),
            "selective_H_q_terms": selective_h_terms,
            "full_H_q_terms_oracle": full_h_terms,
            "selective_H_term_fraction": f"{selective_h_terms}/{full_h_terms}",
            "selected_polynomials_exact_match_oracle": True,
            "depth2_surviving_weighted_mass_exact_match_oracle": True,
            "rows": telemetry,
            "full_histogram_oracle_used_only_for_regression": True,
        },
        "next_exact_step": "replace the full-histogram oracle with retained selective certificates and run exact Picard minima only on the depth-2 survivors; then package x4 intervals as resumable bounded work units",
        "production_heavy_run_armed": False,
        "full_row_census_claimed": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("SELECTIVE_WEIGHTED_SURVIVOR_SUMMARY=" + json.dumps({
        "static_keys_before_depth2": len(static_keys),
        "union_surviving_static_keys": len(survivor_union),
        "requested_H_keys": len(needed_h),
        "selective_H_q_terms": selective_h_terms,
        "full_H_q_terms_oracle": full_h_terms,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
