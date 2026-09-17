#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNEQUAL = HERE / "verify_fibration_nef_static_minq_unequal_preflight.py"
UNEQUAL_BLOB = "f0b6b587e3f25c9341ad9096fea187a303f89acd"


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


def pair_sum_min_q(total: int, lower_first: int) -> int | None:
    """Minimize u^2+w^2 over u+w=total and u>=lower_first."""
    total = int(total)
    lower_first = int(lower_first)
    if lower_first > total:
        return None
    candidates = {lower_first, total}
    half = total // 2
    for u in (half, half + 1):
        if lower_first <= u <= total:
            candidates.add(u)
    return min(u * u + (total - u) * (total - u) for u in candidates)


def equal_static_key_minq(b: int, c: int, t: int, qcap: int) -> int | None:
    """Exact minimum qH for one x0=x1 canonical static key.

    Put s=x0=x1, p=x5, r=x6, u=x8, v=x9, w=x10.  For fixed
    (b,c,t) and p,
      r=t-b-s+p,
      v=b-s-p,
      u+w=b+c-t-p.
    The s-dependent quadratic has continuous center t/4, independent of p.
    The pair-lex condition (p,r)<=(u,v) becomes u>=p, strengthened to u>=p+1
    exactly when r>v; that inequality is 2p>2b-t and is also independent of s.
    Therefore each p needs only constant many exact nearest-integer candidates.
    """
    b, c, t, qcap = int(b), int(c), int(t), int(qcap)
    if min(b, c, t) < 0 or t > b + c or ((c - t) & 1):
        return None

    k = b + c - t  # p + (u+w)
    p_lo = max(0, b - t)
    p_hi = min(b, k)
    if p_lo > p_hi:
        return None

    best = None
    for p in range(p_lo, p_hi + 1):
        # Write r=A-s and v=B-s.
        a = t - b + p
        bb = b - p
        if a < 0 or bb < 0:
            continue
        s_hi = min(a, bb)
        if s_hi < 0:
            continue

        # Exact integer minimum of 2s^2+(A-s)^2+(B-s)^2 on [0,s_hi].
        s_candidates = {0, s_hi}
        sfloor = t // 4
        for s in (sfloor, sfloor + 1):
            if 0 <= s <= s_hi:
                s_candidates.add(s)
        s_part = min(
            2 * s * s + (a - s) * (a - s) + (bb - s) * (bb - s)
            for s in s_candidates
        )

        pair_total = k - p
        # r<=v iff 2p<=2b-t.  Equality in the first lex coordinate is allowed
        # only in that case; otherwise u must be strictly larger than p.
        pair_lower = p if 2 * p <= 2 * b - t else p + 1
        pair_part = pair_sum_min_q(pair_total, pair_lower)
        if pair_part is None:
            continue

        q = p * p + s_part + pair_part
        if q <= qcap and (best is None or q < best):
            best = q
    return best


def equal_static_minq(limit: int, qcap: int) -> dict[tuple[int, int, int], int]:
    """Generate exact equal-branch static support/min-q without q histograms."""
    out: dict[tuple[int, int, int], int] = {}
    for b in range(limit + 1):
        for c in range(limit - b + 1):
            mass = b + c
            for t in range(mass + 1):
                if ((c - t) & 1):
                    continue
                q = equal_static_key_minq(b, c, t, qcap)
                if q is not None:
                    out[(b, c, t)] = q
    return out


def merge_static_minq(*maps: dict[tuple[int, int, int], int]):
    out: dict[tuple[int, int, int], int] = {}
    for source in maps:
        for key, q in source.items():
            if key not in out or q < out[key]:
                out[key] = q
    return out


def main() -> None:
    req(UNEQUAL.is_file(), "missing unequal static min-q producer")
    req(git_blob(UNEQUAL) == UNEQUAL_BLOB, "unequal static min-q producer drift")
    unequal = load_module(UNEQUAL, "stage32_178_static_minq_complete_unequal")

    req(unequal.PARITY.is_file(), "missing parity quotient producer")
    req(unequal.git_blob(unequal.PARITY) == unequal.PARITY_BLOB,
        "parity quotient producer drift")
    parity = unequal.load_module(unequal.PARITY, "stage32_178_static_minq_complete_parity")
    req(parity.WEIGHTED.is_file(), "missing retained weighted producer")
    req(parity.git_blob(parity.WEIGHTED) == parity.WEIGHTED_BLOB,
        "retained weighted producer drift")
    weighted = parity.load_module(parity.WEIGHTED, "stage32_178_static_minq_complete_weighted")
    weighted.lock_sources_before_import()

    regressions = []
    for e in range(0, 15):
        for qcap in sorted({e * e, (e * e) // 2}):
            equal_full = weighted.equal_h_polynomials(e, qcap)
            equal_min = equal_static_minq(e, qcap)
            equal_expected = {key: min(poly) for key, poly in equal_full.items()}
            req(equal_min == equal_expected,
                f"equal static min-q mismatch e={e} qcap={qcap}")

            unequal_min, _ustates = unequal.unequal_static_minq(e, qcap)
            complete = merge_static_minq(unequal_min, equal_min)
            full_h = parity.parity_quotient_bc_h_polynomials(weighted, e, qcap)
            complete_expected = {key: min(poly) for key, poly in full_h.items()}
            req(complete == complete_expected,
                f"complete H static min-q mismatch e={e} qcap={qcap}")

            regressions.append({
                "e": e,
                "qcap": qcap,
                "equal_static_keys": len(equal_min),
                "complete_h_static_keys": len(complete),
                "full_h_q_terms": sum(len(poly) for poly in full_h.values()),
            })

    highd_e = 32
    highd_qcap = 4992
    unequal_highd, unequal_states = unequal.unequal_static_minq(highd_e, highd_qcap)
    equal_highd = equal_static_minq(highd_e, highd_qcap)
    complete_highd = merge_static_minq(unequal_highd, equal_highd)
    full_h_highd = parity.parity_quotient_bc_h_polynomials(
        weighted, highd_e, highd_qcap
    )
    expected_highd = {key: min(poly) for key, poly in full_h_highd.items()}
    req(complete_highd == expected_highd,
        "g1-d192/e32 complete static min-q changed H support/min-q")

    out = {
        "schema": "STAGE32_32_01_178_STATIC_MINQ_COMPLETE_PREFLIGHT_V1",
        "purpose": "produce exact complete H static support/min-q for both canonical branches before qexc-polynomial materialization, enabling depth-2 envelope pruning ahead of full weighted counting",
        "equal_branch_reduction": {
            "parameterization": "p=x5; for fixed (b,c,t,p), minimize s=x0=x1 near t/4 and u=x8 near half of u+w subject to exact pair-lex lower bound",
            "parity_condition": "c == t (mod 2)",
            "s_continuous_center": "t/4",
            "pair_lex_switch": "2p <= 2b-t permits u=p; otherwise u>=p+1",
            "q_histogram_materialized": False,
            "support_and_min_q_exact": True,
        },
        "bounded_exact_regression": {
            "e_range": [0, 14],
            "qcap_modes": ["floor(e^2/2)", "e^2"],
            "equal_branch_matches_full_weighted_histogram_minima": True,
            "complete_H_matches_full_weighted_histogram_minima": True,
            "rows": regressions,
        },
        "real_highd_telemetry": {
            "row_id": "g1-d192",
            "e": highd_e,
            "absolute_qcap": highd_qcap,
            "unequal_static_keys": len(unequal_highd),
            "equal_static_keys": len(equal_highd),
            "complete_h_static_keys": len(complete_highd),
            "full_h_q_terms": sum(len(poly) for poly in full_h_highd.values()),
            "unequal_minplus_state_peak": max(unequal_states),
            "complete_support_and_min_q_exact_match": True,
        },
        "next_exact_step": "feed complete static min-q into depth-2 before any q histogram; only surviving static keys should request weighted q distributions. For e approaching the Cauchy cap, optimize the remaining equal-branch p scan by its piecewise-convex structure.",
        "production_heavy_run_armed": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("STATIC_MINQ_COMPLETE_SUMMARY=" + json.dumps({
        "regression_cases": len(regressions),
        "highd_unequal_static_keys": len(unequal_highd),
        "highd_equal_static_keys": len(equal_highd),
        "highd_complete_h_static_keys": len(complete_highd),
        "highd_full_h_q_terms": sum(len(poly) for poly in full_h_highd.values()),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
