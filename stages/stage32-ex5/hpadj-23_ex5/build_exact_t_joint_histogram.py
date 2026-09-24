#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / "hpadj-22_ex5" / "bounded_exact_deletion_correlation.py"
RESULT = HERE / "HPADJ23-EXACT-T-BUILDER-BOUNDED-RESULT.json"
PARENT_BLOB = "98d84c925af74c35b99001b08d8428f997ab63ea"
RESULT_CANON = "0ab20358bdcb62c487cd0213b0156f2f7a95875e147e4733e0f65c7d3df72db3"
INF = 10**30

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def load_parent():
    req(PARENT.is_file() and blob(PARENT) == PARENT_BLOB, "HPADJ22 joint source drift")
    spec = importlib.util.spec_from_file_location("hpadj22_joint_locked_for_hpadj23", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ22 joint source")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def build_joint_bc_t(H: int):
    B = [[[defaultdict(lambda: defaultdict(int)) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(lambda: defaultdict(int)) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][x5*x5 + x9*x9][x9] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8+x10) & 1][x6*x6 + x8*x8 + x10*x10][x6] += 1

    out = defaultdict(lambda: defaultdict(int))
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        x0par = x0 & 1
        for x1 in range(x0 + 1, H + 1):
            x1par = x1 & 1
            q01 = x0*x0 + x1*x1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    for sb in range(3):
                        for x9par in (0, 1):
                            left = B[g2][sb][x9par]
                            if not left:
                                continue
                            required_cpar = x9par ^ x1par
                            r = x0par ^ x1par ^ x9par
                            for sc in range(4):
                                right = C[g3][sc][required_cpar]
                                if not right:
                                    continue
                                support = sb + sc + extra
                                for ql, x9_counts in left.items():
                                    for qr, x6_counts in right.items():
                                        dst = out[(b,c,support,r,q01+ql+qr)]
                                        for x9, vl in x9_counts.items():
                                            for x6, vr in x6_counts.items():
                                                dst[x0+x1+x6+x9] += vl * vr

    for u in range(H + 1):
        terminal_parity = u & 1
        cap = H - u
        for x5 in range(cap + 1):
            for x8 in range(x5 + 1, cap + 1):
                for x9 in range(cap - x5 + 1):
                    b = u + x5 + x9
                    for x6 in range(cap - x8 + 1):
                        for x10 in range(cap - x8 - x6 + 1):
                            c = u + x8 + x6 + x10
                            if ((x8+x9+x10) & 1) != terminal_parity:
                                continue
                            vals = (u,u,x5,x6,x8,x9,x10)
                            support = sum(v > 0 for v in vals)
                            qbc = sum(v*v for v in vals)
                            r = (u+x8+x10) & 1
                            out[(b,c,support,r,qbc)][2*u+x6+x9] += 1
        for x5 in range(cap + 1):
            x8 = x5
            for x6 in range(cap - x8 + 1):
                for x9 in range(x6, cap - x5 + 1):
                    b = u + x5 + x9
                    for x10 in range(cap - x8 - x6 + 1):
                        c = u + x8 + x6 + x10
                        if ((x8+x9+x10) & 1) != terminal_parity:
                            continue
                        vals = (u,u,x5,x6,x8,x9,x10)
                        support = sum(v > 0 for v in vals)
                        qbc = sum(v*v for v in vals)
                        r = (u+x8+x10) & 1
                        out[(b,c,support,r,qbc)][2*u+x6+x9] += 1
    return out

def brute_joint_bc_t(H: int):
    out = defaultdict(lambda: defaultdict(int))
    for vals in product(range(H + 1), repeat=7):
        x0,x1,x5,x6,x8,x9,x10 = vals
        if x0 > x1:
            continue
        if x0 == x1 and (x5,x6) > (x8,x9):
            continue
        b = x1+x5+x9
        c = x0+x6+x8+x10
        if b > H or c > H or ((x1+x8+x9+x10) & 1):
            continue
        support = sum(v > 0 for v in vals)
        r = (x0+x8+x10) & 1
        qbc = sum(v*v for v in vals)
        t = x0+x1+x6+x9
        out[(b,c,support,r,qbc)][t] += 1
    return out

def normalized(hist):
    return {k: dict(sorted(v.items())) for k,v in hist.items() if v}

def marginal_check(parent, exact_t, H: int) -> None:
    old = parent.build_joint_bc(H)
    marginal = {k: sum(v.values()) for k,v in exact_t.items()}
    total = 0
    for b in range(H + 1):
        for c in range(H + 1):
            for s in range(8):
                for r in (0, 1):
                    want = dict(old[b][c][s][r])
                    got = {q: marginal.get((b,c,s,r,q), 0) for q in want}
                    got = {q:v for q,v in got.items() if v}
                    req(got == want, f"HPADJ22 marginal mismatch {(H,b,c,s,r)}")
                    total += sum(want.values())
    req(sum(marginal.values()) == total, f"HPADJ22 total marginal mismatch H={H}")

def min_square_sum_positive(total: int, positive_parts: int) -> int:
    if positive_parts == 0:
        return 0 if total == 0 else INF
    if total < positive_parts:
        return INF
    q,r = divmod(total, positive_parts)
    return (positive_parts-r)*q*q + r*(q+1)*(q+1)

def support_q_lower(total_mass: int, t: int, support: int) -> int:
    best = INF
    for k in range(max(0, support-3), min(4, support)+1):
        qt = min_square_sum_positive(t, k)
        qu = min_square_sum_positive(total_mass-t, support-k)
        if qt < INF and qu < INF:
            best = min(best, qt+qu)
    return best

def pair_square_min(total: int) -> int:
    q,r = divmod(total, 2)
    return (2-r)*q*q + r*(q+1)*(q+1)

def parity_nearest_candidates(lo: int, hi: int, parity: int, center_num: int):
    parity &= 1
    first = lo + ((parity-lo) & 1)
    last = hi - ((hi-parity) & 1)
    if first > last:
        return ()
    vals = {first,last}
    k0 = (center_num - 5*parity) // 10
    for k in (k0-1,k0,k0+1,k0+2):
        p = parity + 2*k
        if first <= p <= last:
            vals.add(p)
    return tuple(sorted(vals))

def bc_t_q_lower(b: int, c: int, t: int) -> int:
    lo,hi = max(0,t-c), min(b,t)
    if lo > hi:
        return INF
    candidates = set()
    center_num = 2*b-c+2*t
    for parity in (0,1):
        candidates.update(parity_nearest_candidates(lo,hi,parity,center_num))
    return min(pair_square_min(p)+(b-p)**2+pair_square_min(t-p)+pair_square_min(c-t+p) for p in candidates)

def aggregate_q_lower(b: int, c: int, t: int, support: int) -> int:
    return max(support_q_lower(b+c,t,support), bc_t_q_lower(b,c,t))

def current_hull(b: int, c: int, support: int, qbc: int) -> set[int]:
    parity = c & 1
    rows = sorted((aggregate_q_lower(b,c,t,support),t) for t in range(parity,b+c+1,2))
    cuts=[]; lows=[]; highs=[]; lo=hi=None; i=0
    while i < len(rows):
        q=rows[i][0]
        while i < len(rows) and rows[i][0] == q:
            t=rows[i][1]
            lo=t if lo is None else min(lo,t)
            hi=t if hi is None else max(hi,t)
            i += 1
        cuts.append(q); lows.append(lo); highs.append(hi)
    pos=bisect.bisect_right(cuts,qbc)-1
    req(pos >= 0, f"empty hull {(b,c,support,qbc)}")
    return set(range(lows[pos],highs[pos]+1,2))

def strictness(exact_t):
    strict=removed=entries=multiplicity=0
    merged=defaultdict(set)
    for (b,c,s,r,qbc),counts in exact_t.items():
        ts=set(counts); entries += len(ts); multiplicity += sum(counts.values())
        hull=current_hull(b,c,s,qbc)
        req(ts <= hull, f"unsafe exact-t set {(b,c,s,r,qbc)}")
        if ts != hull:
            strict += 1; removed += len(hull-ts)
        merged[(b,c,s,qbc)].update(ts)
    mstrict=mremoved=0
    for (b,c,s,qbc),ts in merged.items():
        hull=current_hull(b,c,s,qbc)
        req(ts <= hull, f"unsafe exact-t marginal {(b,c,s,qbc)}")
        if ts != hull:
            mstrict += 1; mremoved += len(hull-ts)
    return {
        "valid_canonical_tuple_multiplicity":multiplicity,
        "exact_bins_with_required_parity":len(exact_t),
        "exact_t_support_entries_with_required_parity":entries,
        "strict_vs_current_parity_hull_bins_with_required_parity":strict,
        "filled_hull_t_points_removed_with_required_parity":removed,
        "exact_bins_after_required_parity_marginalization":len(merged),
        "strict_vs_current_parity_hull_bins_after_required_parity_marginalization":mstrict,
        "filled_hull_t_points_removed_after_required_parity_marginalization":mremoved,
    }

def main() -> None:
    parent=load_parent()
    result=json.loads(RESULT.read_text())
    req(canonical(result) == RESULT_CANON == result["canonical_sha256_without_this_field"], "retained result canonical drift")
    h4=build_joint_bc_t(4)
    req(normalized(h4) == normalized(brute_joint_bc_t(4)), "H4 exact-t builder differs from brute force")
    marginal_check(parent,h4,4)
    h16=build_joint_bc_t(16)
    marginal_check(parent,h16,16)
    metrics=strictness(h16)
    want=result["bounded_H16"]
    for key,value in metrics.items():
        req(want[key] == value, f"H16 retained metric drift {key}: {value} != {want[key]}")
    req(want["all_exact_t_sets_subset_of_current_support_qbc_hull"] is True, "safe-subset flag drift")
    print("PASS: HPADJ23 exact-t builder bounded H=16")
    for key in sorted(metrics):
        print(f"{key}={metrics[key]}")

if __name__ == "__main__":
    main()
