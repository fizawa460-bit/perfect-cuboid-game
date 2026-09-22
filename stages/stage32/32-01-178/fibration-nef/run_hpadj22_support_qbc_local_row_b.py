#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
import os
import time
import tempfile
import subprocess
import ctypes
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
FAST_PARENT = HERE / "verify_hpadj22_zero_center_qbc_tinterval_g1d192_band4_fast.py"
FAST_PARENT_BLOB = "bb7541979bb29078cda1207d1882e4d4d8c2138d"
INF = 10**30


def peak_rss_bytes():
    if os.name != 'nt':
        import resource
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if sys.platform == 'darwin' else 1024)
    class Counters(ctypes.Structure):
        _fields_ = [('cb', ctypes.c_ulong), ('faults', ctypes.c_ulong)] + [(n, ctypes.c_size_t) for n in ('peak_working', 'working', 'peak_paged', 'paged', 'peak_nonpaged', 'nonpaged', 'pagefile', 'peak_pagefile')]
    m = Counters()
    m.cb = ctypes.sizeof(m)
    req(bool(ctypes.windll.psapi.GetProcessMemoryInfo(ctypes.c_void_p(-1), ctypes.byref(m), m.cb)), 'RSS measurement failed')
    return m.peak_working


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def min_square_sum_positive(total: int, positive_parts: int) -> int:
    """Exact min of sum yi^2 for k positive integers summing to N."""
    total = int(total)
    positive_parts = int(positive_parts)
    if positive_parts == 0:
        return 0 if total == 0 else INF
    if total < positive_parts:
        return INF
    q, r = divmod(total, positive_parts)
    return (positive_parts - r) * q * q + r * (q + 1) * (q + 1)


def support_q_lower(total_mass: int, t: int, support: int) -> int:
    """Exact qBC minimum under only (m,t,total H support)."""
    m = int(total_mass)
    t = int(t)
    s = int(support)
    if not (0 <= t <= m and 0 <= s <= 7):
        return INF
    best = INF
    for k in range(max(0, s - 3), min(4, s) + 1):
        qt = min_square_sum_positive(t, k)
        qu = min_square_sum_positive(m - t, s - k)
        if qt < INF and qu < INF:
            best = min(best, qt + qu)
    return best


def pair_square_min(total: int) -> int:
    """Exact min u^2+v^2 over nonnegative u+v=total."""
    total = int(total)
    q, r = divmod(total, 2)
    return (2 - r) * q * q + r * (q + 1) * (q + 1)


def parity_nearest_candidates(lo: int, hi: int, parity: int, center_num: int):
    """Exact candidates nearest center_num/5 on one parity lattice."""
    parity &= 1
    first = lo + ((parity - lo) & 1)
    last = hi - ((hi - parity) & 1)
    if first > last:
        return ()
    vals = {first, last}
    # p = parity + 2k, continuous center p0=center_num/5.
    # Hence k0=(center_num-5*parity)/10.
    k0 = (center_num - 5 * parity) // 10
    for k in (k0 - 1, k0, k0 + 1, k0 + 2):
        p = parity + 2 * k
        if first <= p <= last:
            vals.add(p)
    return tuple(sorted(vals))


def bc_t_q_lower(b: int, c: int, t: int) -> int:
    """Exact qBC minimum under only fixed (b,c,t), canonical order relaxed.

    Put p=x1+x9. Then
      x5=b-p,
      x0+x6=t-p,
      x8+x10=c-t+p.
    For fixed p the three two-coordinate groups have exact balanced square
    minima.  The resulting objective is a convex quadratic plus a parity-class
    constant, so the exact integer minimum is attained at the nearest point to
    the continuous center on each parity lattice (with interval endpoints).
    """
    b, c, t = int(b), int(c), int(t)
    lo = max(0, t - c)
    hi = min(b, t)
    if lo > hi:
        return INF
    center_num = 2 * b - c + 2 * t  # continuous center = center_num/5
    candidates = set()
    for parity in (0, 1):
        candidates.update(parity_nearest_candidates(lo, hi, parity, center_num))
    req(bool(candidates), f"empty bc/t minimizer domain {(b,c,t)}")
    return min(
        pair_square_min(p)
        + (b - p) * (b - p)
        + pair_square_min(t - p)
        + pair_square_min(c - t + p)
        for p in candidates
    )


def bc_t_q_lower_bruteforce(b: int, c: int, t: int) -> int:
    lo = max(0, int(t) - int(c))
    hi = min(int(b), int(t))
    if lo > hi:
        return INF
    return min(
        pair_square_min(p)
        + (int(b) - p) * (int(b) - p)
        + pair_square_min(int(t) - p)
        + pair_square_min(int(c) - int(t) + p)
        for p in range(lo, hi + 1)
    )


def aggregate_q_lower(b: int, c: int, t: int, support: int) -> int:
    return max(
        support_q_lower(int(b) + int(c), int(t), int(support)),
        bc_t_q_lower(int(b), int(c), int(t)),
    )


@lru_cache(maxsize=None)
def support_envelope(b: int, c: int, support: int, parity: int):
    """Cumulative parity interval for qBC >= support_q_lower.

    The hull between cumulative min/max t is a deliberate relaxation; holes
    are filled rather than rejected.  That makes the resulting z-distance a
    safe lower bound while keeping lookup O(log m).
    """
    b, c = int(b), int(c)
    m = b + c
    s = int(support)
    parity = int(parity) & 1
    rows = []
    for t in range(parity, m + 1, 2):
        q = aggregate_q_lower(b, c, t, s)
        if q < INF:
            rows.append((q, t))
    rows.sort()

    cuts = []
    lows = []
    highs = []
    lo = hi = None
    i = 0
    while i < len(rows):
        q = rows[i][0]
        while i < len(rows) and rows[i][0] == q:
            t = rows[i][1]
            lo = t if lo is None else min(lo, t)
            hi = t if hi is None else max(hi, t)
            i += 1
        cuts.append(q)
        lows.append(lo)
        highs.append(hi)
    return tuple(cuts), tuple(lows), tuple(highs)


def support_t_interval(*, b: int, c: int, support: int, qbc: int) -> tuple[int, int]:
    m = int(b) + int(c)
    parity = int(c) & 1
    cuts, lows, highs = support_envelope(int(b), int(c), int(support), parity)
    pos = bisect.bisect_right(cuts, int(qbc)) - 1
    req(pos >= 0, f"nonempty current qBC bin violates support lower bound {(b,c,support,qbc)}")
    lo, hi = int(lows[pos]), int(highs[pos])
    req(
        lo <= hi and (lo & 1) == parity and (hi & 1) == parity,
        f"support interval parity drift {(b,c,support,qbc,lo,hi)}",
    )
    return lo, hi


def qcut_support(qparent, *, g: int, d: int, b: int, c: int, support: int,
                 qbc: int, x4: int, a_parity: int) -> int:
    lo, hi = support_t_interval(b=b, c=c, support=support, qbc=qbc)
    z = qparent.nearest_distance(d=d, x4=x4, lo=lo, hi=hi, parity=c & 1)
    p0 = (b + c) & 1
    p1 = int(a_parity) & 1
    rhs120 = (15 * d * d) // 2 + 120 * d + 240 - 240 * g
    return (rhs120 - 10 * z * z - 60 * p0 - 12 * p1) // 60


def abstract_regression() -> int:
    checked = 0
    for xs in product(range(3), repeat=7):
        t = xs[0] + xs[1] + xs[2] + xs[3]
        u = xs[4] + xs[5] + xs[6]
        m = t + u
        support = sum(int(v > 0) for v in xs)
        q = sum(v * v for v in xs)
        req(
            q >= support_q_lower(m, t, support),
            f"support q lower bound exceeded exact q {xs}",
        )
        x0, x1, x5, x6, x8, x9, x10 = xs
        b = x1 + x5 + x9
        c = x0 + x6 + x8 + x10
        tt = x0 + x1 + x6 + x9
        req(
            q >= bc_t_q_lower(b, c, tt),
            f"bc/t q lower bound exceeded exact q {xs}",
        )
        checked += 1

    # Independent bounded regression of the parity-lattice convex minimizer
    # against a literal scan over every admissible p.
    for b in range(13):
        for c in range(13):
            for t in range(b + c + 1):
                req(
                    bc_t_q_lower(b, c, t) == bc_t_q_lower_bruteforce(b, c, t),
                    f"bc/t convex minimizer mismatch {(b,c,t)}",
                )
                checked += 1
    return checked


def main() -> None:
    started = time.perf_counter()
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--b", type=int, required=True)
    ap.add_argument("--row-index", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--before", required=True)
    ap.add_argument("--head", required=True)
    args = ap.parse_args()
    key_path = HERE / "SUPPORT-QBC-LOCAL-WAVE-RUNKEY.json"
    rel = key_path.relative_to(args.repo_root).as_posix()
    def git(*words):
        return subprocess.check_output(["git", "-C", str(args.repo_root), *words], text=True).strip()
    req(args.head == git("rev-parse", "HEAD"), "execution head drift")
    git("merge-base", "--is-ancestor", args.before, args.head)
    req(rel in git("diff", "--name-only", args.before, args.head).splitlines(), "no fresh runkey arm")
    key = json.loads(git("show", args.head + ":" + rel))
    old_key = json.loads(git("show", args.before + ":" + rel))
    req(key == json.loads(key_path.read_text()), "working runkey drift")
    req(key["armed"] and key["generation"] > old_key["generation"], "cold or stale generation")
    req(key["worker_blob_sha1"] == blob(Path(__file__)), "worker lock drift")
    req(key["local_only"] is True and 1 <= key["planned_local_concurrency"] <= 4, "execution scope drift")
    req(all(key[k] is False for k in ("main_credit_changed", "theorem_credit_changed", "endpoint_credit_changed")), "credit firewall drift")
    req(args.b in key["authorized_b"] and args.row_index in key["authorized_rows"] and not 48 <= args.b <= 59, "unauthorized or remote-overlap unit")
    req([args.row_index, args.b] not in key["excluded_completed_units"], "completed unit must be carried")
    req(not args.output.exists(), "existing receipt: validate and carry, never overwrite")
    print(json.dumps({"event": "AUTHORIZED", "row_index": args.row_index, "b": args.b, "head": args.head}), flush=True)
    req(subprocess.check_output(["git", "-C", str(args.source_root), "rev-parse", "HEAD"], text=True).strip() == "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2", "source checkout head drift")

    req(
        FAST_PARENT.is_file() and blob(FAST_PARENT) == FAST_PARENT_BLOB,
        "fast qBC parent drift",
    )
    fp = load(FAST_PARENT, "stage32_178_support_qbc_fast_parent")
    req(
        fp.PARENT.is_file() and fp.blob(fp.PARENT) == fp.PARENT_BLOB,
        "qBC mathematical parent drift",
    )
    q = fp.load(fp.PARENT, "stage32_178_support_qbc_math_parent")

    direct_path = args.repo_root / q.DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == q.DIRECT_BLOB, "direct-count source drift")
    req(q.FAST.is_file() and blob(q.FAST) == q.FAST_BLOB, "zero-center parity source drift")
    direct = load(direct_path, "stage32_178_support_qbc_direct")
    fast = load(q.FAST, "stage32_178_support_qbc_picard")
    cert = fast.load_certificate()
    req(int(cert["membership_modulus"]) == 2, "Picard modulus drift")

    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx
    req(0 <= args.row_index < len(rows), "row index outside source manifest")
    row_id, g0, d0 = rows[args.row_index]
    g, d = int(g0), int(d0)
    req(d % 2 == 0 and g in (0, 1) and 0 <= args.b <= d//2, "target row outside proved domain")
    req(row_id == f"g{g}-d{d:03d}", "row identity drift")
    h = d // 2
    K = counter.ceil_div(d - 16 * g + 16, 4)
    tq = (d * d + 16 * d + (32 if g == 0 else 0)) // 8

    regression_cases = abstract_regression()

    band = next(i for i, (lo, hi) in enumerate(old.PLANNED) if lo <= args.b <= hi)
    full_b0, full_b1 = old.PLANNED[band]
    b0 = b1 = args.b
    full_band = (b0, b1) == (full_b0, full_b1)
    joint = bc.build_joint_bc_shard(old.HMAX, b0, b1)
    print(json.dumps({"event": "JOINT_READY", "b": b0, "wall_seconds": time.perf_counter()-started}), flush=True)

    ca = [counter.component_a(d, a) for a in range(h + 1)]
    row_aprof = {}
    row_qas = set()
    for a in range(h + 1):
        if ca[a] < 0:
            continue
        for sa in range(4):
            tiers = profiles[a][sa]
            if tiers:
                tt = tuple((int(qv), int(mult)) for qv, mult in tiers)
                row_aprof[(a, sa)] = tt
                row_qas.update(qv for qv, _ in tt)
    row_qas = tuple(sorted(qv for qv in row_qas if qv <= tq))

    current = parent_refined = refined = 0
    strict_bc = 0
    strict_vs_parent_bc = 0
    bc_records = []
    all_bc_records = []
    qbc_bins_seen = x4_qbc_pairs = 0
    support_interval_queries = strict_support_intervals = 0
    current_limit_states = parent_limit_states = refined_limit_states = 0
    lookup_count = current_regression_queries = 0

    for b in range(b0, min(b1, h) + 1):
        for c in range(h + 1):
            jbc = joint[b][c]
            active = []
            for sbc in range(8):
                for r in (0, 1):
                    hist0 = jbc[sbc][r]
                    if not hist0:
                        continue
                    hist = {
                        int(qv): int(mult)
                        for qv, mult in hist0.items()
                        if int(mult) and int(qv) <= tq
                    }
                    if hist:
                        active.append((sbc, r, hist))
            if not active:
                all_bc_records.append({"b": b, "c": c, "current": "0", "parent_refined": "0", "refined": "0", "zero_reason": "no_active_histogram"})
                continue

            c3 = counter.component3(d, b, c)
            if c3 < 0:
                all_bc_records.append({"b": b, "c": c, "current": "0", "parent_refined": "0", "refined": "0", "zero_reason": "negative_component3"})
                continue
            caps = bnd.x4_caps(h16, h, g, b, c)
            xr = h16.a0_interval(h, g, b, c)
            if xr is None:
                all_bc_records.append({"b": b, "c": c, "current": "0", "parent_refined": "0", "refined": "0", "zero_reason": "empty_x4_interval"})
                continue

            x4_by_r = {0: [], 1: []}
            for x4 in range(int(xr[0]), int(xr[1]) + 1):
                room = -int(h16.f0(h, g, b, c, x4))
                req(room >= 0, f"negative current x4 room {(b,c,x4)}")
                x4_by_r[x4 & 1].append((x4, room // 138))

            prepared = []
            for sbc, r, hist in active:
                qbc_bins_seen += len(hist)
                hist_prefix = fp.prefix_index(hist)
                cur_limits = Counter()
                parent_limits = {0: Counter(), 1: Counter()}
                ref_limits = {0: Counter(), 1: Counter()}

                for qbc, mult in hist.items():
                    old_lo, old_hi = q.t_interval(b=b, c=c, qbc=qbc)
                    new_lo, new_hi = support_t_interval(
                        b=b, c=c, support=sbc, qbc=qbc
                    )
                    req(
                        old_lo <= new_lo <= new_hi <= old_hi,
                        f"support interval failed to refine parent {(b,c,sbc,r,qbc,old_lo,old_hi,new_lo,new_hi)}",
                    )
                    support_interval_queries += 1
                    strict_support_intervals += int((new_lo, new_hi) != (old_lo, old_hi))

                    for x4, cap in x4_by_r[r]:
                        x4_qbc_pairs += 1
                        cur_limit = min(cap, tq - qbc)
                        if cur_limit >= 0:
                            cur_limits[cur_limit] += mult

                        for ap in (0, 1):
                            parent_cut = q.qcut(
                                g=g, d=d, b=b, c=c, qbc=qbc,
                                x4=x4, a_parity=ap,
                            )
                            cut = qcut_support(
                                q, g=g, d=d, b=b, c=c, support=sbc,
                                qbc=qbc, x4=x4, a_parity=ap,
                            )
                            req(
                                cut <= parent_cut <= tq,
                                f"support qcut failed to dominate parent {(b,c,sbc,r,qbc,x4,ap,cut,parent_cut)}",
                            )
                            parent_limit = min(cap, parent_cut - qbc)
                            limit = min(cap, cut - qbc)
                            if parent_limit >= 0:
                                parent_limits[ap][parent_limit] += mult
                            if limit >= 0:
                                ref_limits[ap][limit] += mult

                cur_index = fp.suffix_index(cur_limits)
                parent_index = {
                    0: fp.suffix_index(parent_limits[0]),
                    1: fp.suffix_index(parent_limits[1]),
                }
                ref_index = {
                    0: fp.suffix_index(ref_limits[0]),
                    1: fp.suffix_index(ref_limits[1]),
                }
                current_limit_states += len(cur_limits)
                parent_limit_states += len(parent_limits[0]) + len(parent_limits[1])
                refined_limit_states += len(ref_limits[0]) + len(ref_limits[1])

                for qa in row_qas:
                    expected = (
                        int(bnd.survivor_count(caps, r, qa))
                        * fp.prefix_leq(hist_prefix, tq - qa)
                    )
                    observed = fp.suffix_ge(cur_index, qa)
                    req(
                        observed == expected,
                        f"current limit aggregation drift {(b,c,sbc,r,qa,observed,expected)}",
                    )
                    current_regression_queries += 1

                prepared.append((sbc, r, cur_index, parent_index, ref_index))

            bc_cur = bc_parent = bc_ref = 0
            for a in range(h + 1):
                if ca[a] < 0:
                    continue
                srem = min(16, d) + ca[a] + c3
                ec = {}
                for support in range(11):
                    es = bnd.eligible_e(counter, d, g, h, a, b, c, support, srem, K)
                    if es:
                        req(
                            all((int(e) & 1) == 0 for e in es),
                            f"odd eligible e {(a,b,c,support)}",
                        )
                        ec[support] = len(es)
                if not ec:
                    continue

                ap = a & 1
                for sbc, r, cur_index, parent_index, ref_index in prepared:
                    for sa in range(4):
                        tiers = row_aprof.get((a, sa))
                        ne = ec.get(sbc + sa)
                        if tiers is None or ne is None:
                            continue
                        for qa, va in tiers:
                            cur = fp.suffix_ge(cur_index, qa)
                            if not cur:
                                continue
                            par = fp.suffix_ge(parent_index[ap], qa)
                            ref = fp.suffix_ge(ref_index[ap], qa)
                            req(
                                ref <= par <= cur,
                                f"support refinement order drift {(a,b,c,sbc,r,sa,qa,ref,par,cur)}",
                            )
                            w = int(va) * int(ne)
                            bc_cur += cur * w
                            bc_parent += par * w
                            bc_ref += ref * w
                            lookup_count += 1

            current += bc_cur
            parent_refined += bc_parent
            refined += bc_ref
            all_bc_records.append({"b": b, "c": c, "current": str(bc_cur), "parent_refined": str(bc_parent), "refined": str(bc_ref)})
            print(json.dumps({"event": "BC_COMPLETE", "b": b, "c": c, "current": str(bc_cur), "refined": str(bc_ref), "wall_seconds": time.perf_counter()-started}), flush=True)
            if bc_ref < bc_cur:
                strict_bc += 1
                strict_vs_parent_bc += int(bc_ref < bc_parent)
                bc_records.append({
                    "b": b,
                    "c": c,
                    "current": str(bc_cur),
                    "parent_qbc_refined": str(bc_parent),
                    "support_qbc_refined": str(bc_ref),
                    "reduction": str(bc_cur - bc_ref),
                    "additional_reduction_vs_parent_qbc": str(bc_parent - bc_ref),
                })

    req(refined <= parent_refined <= current, "aggregate refinement order drift")
    parent_reduction = current - parent_refined
    reduction = current - refined
    additional = parent_refined - refined
    req(reduction >= parent_reduction >= 0 and additional >= 0, "reduction accounting drift")
    candidate = q.CURRENT_GLOBAL - reduction

    out = {
        "schema": "STAGE32_178_LOCAL_SUPPORT_QBC_ROW_B_V1",
        "status": "EXACT_CURRENT_HPADJ22_ROW_BAND_SUPPORT_QBC_REFINEMENT__ZERO_MAIN_CREDIT",
        "target": {
            "row_index": args.row_index,
            "row_id": row_id,
            "g": g,
            "d": d,
            "band_position": band,
            "b_interval": [b0, b1],
            "containing_band_interval": [full_b0, full_b1],
            "full_band_execution": full_band,
        },
        "source_locks": {
            "local_worker_blob_sha1": blob(Path(__file__)),
            "execution_head": args.head,
            "authorization_before": args.before,
            "fast_qbc_parent_blob_sha1": FAST_PARENT_BLOB,
            "mathematical_qbc_parent_blob_sha1": fp.PARENT_BLOB,
            "direct_count_blob_sha1": q.DIRECT_BLOB,
            "zero_center_picard_blob_sha1": q.FAST_BLOB,
            "hpadj22_source_head": "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2",
            "hpadj22_row_source_locks": old.row_source_locks(bc, bnd, h21, p14),
        },
        "result": {
            "current_row_band_survivors": str(current),
            "parent_qbc_refined_survivors": str(parent_refined),
            "support_qbc_refined_survivors": str(refined),
            "parent_qbc_exact_reduction": str(parent_reduction),
            "support_qbc_exact_reduction": str(reduction),
            "additional_reduction_vs_parent_qbc": str(additional),
            "current_global_upper_bound": str(q.CURRENT_GLOBAL),
            "candidate_global_upper_bound_if_promoted": str(candidate),
            "global_reduction_fraction": reduction / q.CURRENT_GLOBAL,
            "one_percent_threshold": str((q.CURRENT_GLOBAL + 99) // 100),
            "one_percent_reached_by_this_single_row_band": 100 * reduction >= q.CURRENT_GLOBAL,
            "strict_bc_cells": strict_bc,
            "strict_vs_parent_bc_cells": strict_vs_parent_bc,
        },
        "support_qbc_bound": {
            "identity_t": "t=x0+x1+x6+x9",
            "identity_complement": "b+c-t=x5+x8+x10",
            "exact_H_support": "sbc=#positive(x0,x1,x5,x6,x8,x9,x10)",
            "support_split": "k positives in the four-coordinate t-group and sbc-k positives in the three-coordinate complement",
            "balanced_positive_square_minimum": "for N over k positive integers, N=kq+r gives min sum squares=(k-r)q^2+r(q+1)^2",
            "support_q_lower": "min_k minsq_positive(t,k)+minsq_positive(b+c-t,sbc-k)",
            "bc_t_q_lower": "min_p pairmin(p)+(b-p)^2+pairmin(t-p)+pairmin(c-t+p), p=x1+x9",
            "combined_q_lower": "max(support_q_lower,bc_t_q_lower)",
            "bc_t_minimizer": "exact nearest-point search on each parity lattice around p=(2b-c+2t)/5",
            "canonical_order_relaxed": True,
            "retained_H_parity": "t==c (mod2)",
            "support_interval_is_parity_hull_of_all_t_with_support_q_lower<=qBC": True,
            "interval_holes_deliberately_filled": True,
            "pointwise_dominates_parent_cauchy_qbc_interval": True,
            "abstract_exact_regression_cases": regression_cases,
        },
        "optimization": {
            "fast_parent_aggregation_reused": True,
            "current_limit_hist_replayed_against_separated_current_rule_for_every_realized_qA": True,
            "qbc_bins_seen": qbc_bins_seen,
            "x4_qbc_pairs": x4_qbc_pairs,
            "support_interval_queries": support_interval_queries,
            "strict_support_interval_states": strict_support_intervals,
        "b_interval": [b0, b1],
        "full_band": full_band,
            "current_limit_states": current_limit_states,
            "parent_limit_states": parent_limit_states,
            "support_refined_limit_states": refined_limit_states,
            "current_regression_queries": current_regression_queries,
            "weighted_lookup_count": lookup_count,
        },
        "semantics": {
            "same_population_as_current_hpadj22": True,
            "same_current_joint_qA_qBC_histograms": True,
            "same_current_x4_capacity_rule": True,
            "only_parent_t_relaxation_strengthened_using_exact_support_and_qBC": True,
            "parent_qbc_refinement_replayed_in_same_execution": True,
            "direct_replacement_not_additive_subtraction": True,
            "statistical_independence": False,
            "all_non_target_current_hpadj22_survivors_unchanged": True,
            "main_consumption_performed": False,
            "shard_result_requires_disjoint_full-band_recomposition_before_any_full-band_claim": not full_band,
        },
        "strict_cells": bc_records,
        "visited_cells": all_bc_records,
        "firewalls": {
            "main_credit_changed": False,
            "full178_complete": False,
            "hostile_audit_required_before_promotion": True,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
            "merge": False,
        },
    }

    out["timing"] = {"wall_seconds": time.perf_counter()-started, "cpu_seconds": time.process_time(), "peak_rss_bytes": peak_rss_bytes()}
    out["canonical_sha256_without_this_field"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=args.output.parent, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
        json.dump(out, stream, sort_keys=True, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, args.output)

    print("HPADJ22_SUPPORT_QBC_LOCAL_ROW_B=" + json.dumps({
        "row_index": args.row_index,
        "b": args.b,
        "current": str(current),
        "parent_refined": str(parent_refined),
        "support_refined": str(refined),
        "parent_reduction": str(parent_reduction),
        "reduction": str(reduction),
        "additional_vs_parent": str(additional),
        "global_fraction": reduction / q.CURRENT_GLOBAL,
        "one_percent": 100 * reduction >= q.CURRENT_GLOBAL,
        "candidate_global": str(candidate),
        "strict_bc": strict_bc,
        "strict_vs_parent_bc": strict_vs_parent_bc,
        "strict_support_interval_states": strict_support_intervals,
    }, sort_keys=True))
    print(json.dumps({"event": "ATOMIC_RECEIPT_COMPLETE", "canonical": out["canonical_sha256_without_this_field"], "output": str(args.output)}), flush=True)


if __name__ == "__main__":
    main()
