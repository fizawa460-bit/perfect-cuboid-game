#!/usr/bin/env python3
from __future__ import annotations
import bisect
import hashlib
import json
from collections import defaultdict
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREFLIGHT = HERE / "HPADJ23-EXACT-T-HOLE-PREFLIGHT.json"
INF = 10**30

EXPECTED = {
    "schema": "STAGE32EX5_HPADJ23_EXACT_T_SUPPORT_PREFLIGHT_V1",
    "canonical": "31b7c9d6c2446daf94cf08af43efd1200cec15839433b7366d3dd28c20ce26ea",
    "hpadj22_head": "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2",
    "v48_head": "b4642621dd736457c4d9df349f89d7081e71ccef",
    "v48_canonical": "d106029369dd5a029cd7a56e1c7d80fdd29f8471454fd2ed6c638af2b70288b1",
    "support_worker": "37e72735125c232e534d92c6e24c7afc0a0f4f24",
}

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def min_square_sum_positive(total: int, positive_parts: int) -> int:
    if positive_parts == 0:
        return 0 if total == 0 else INF
    if total < positive_parts:
        return INF
    q, r = divmod(total, positive_parts)
    return (positive_parts-r)*q*q + r*(q+1)*(q+1)

def support_q_lower(total_mass: int, t: int, support: int) -> int:
    m, t, s = int(total_mass), int(t), int(support)
    if not (0 <= t <= m and 0 <= s <= 7):
        return INF
    best = INF
    for k in range(max(0, s-3), min(4, s)+1):
        qt = min_square_sum_positive(t, k)
        qu = min_square_sum_positive(m-t, s-k)
        if qt < INF and qu < INF:
            best = min(best, qt+qu)
    return best

def pair_square_min(total: int) -> int:
    q, r = divmod(total, 2)
    return (2-r)*q*q + r*(q+1)*(q+1)

def parity_nearest_candidates(lo: int, hi: int, parity: int, center_num: int):
    parity &= 1
    first = lo + ((parity-lo) & 1)
    last = hi - ((hi-parity) & 1)
    if first > last:
        return ()
    vals = {first, last}
    k0 = (center_num - 5*parity) // 10
    for k in (k0-1, k0, k0+1, k0+2):
        p = parity + 2*k
        if first <= p <= last:
            vals.add(p)
    return tuple(sorted(vals))

def bc_t_q_lower(b: int, c: int, t: int) -> int:
    lo, hi = max(0, t-c), min(b, t)
    if lo > hi:
        return INF
    center_num = 2*b - c + 2*t
    candidates = set()
    for parity in (0, 1):
        candidates.update(parity_nearest_candidates(lo, hi, parity, center_num))
    req(bool(candidates), f"empty minimizer {(b,c,t)}")
    return min(
        pair_square_min(p) + (b-p)**2 + pair_square_min(t-p) + pair_square_min(c-t+p)
        for p in candidates
    )

def aggregate_q_lower(b: int, c: int, t: int, support: int) -> int:
    return max(support_q_lower(b+c, t, support), bc_t_q_lower(b, c, t))

def current_hull(b: int, c: int, support: int, qbc: int) -> set[int]:
    parity = c & 1
    rows = []
    for t in range(parity, b+c+1, 2):
        q = aggregate_q_lower(b, c, t, support)
        if q < INF:
            rows.append((q, t))
    rows.sort()
    cuts, lows, highs = [], [], []
    lo = hi = None
    i = 0
    while i < len(rows):
        q = rows[i][0]
        while i < len(rows) and rows[i][0] == q:
            t = rows[i][1]
            lo = t if lo is None else min(lo, t)
            hi = t if hi is None else max(hi, t)
            i += 1
        cuts.append(q); lows.append(lo); highs.append(hi)
    pos = bisect.bisect_right(cuts, qbc) - 1
    req(pos >= 0, f"qBC below safe lower envelope {(b,c,support,qbc)}")
    return set(range(int(lows[pos]), int(highs[pos])+1, 2))

def build_exact(H: int):
    exact = defaultdict(set)
    valid = 0
    for vals in product(range(H+1), repeat=7):
        x0,x1,x5,x6,x8,x9,x10 = vals
        if x0 > x1:
            continue
        if x0 == x1 and (x5,x6) > (x8,x9):
            continue
        b = x1+x5+x9
        c = x0+x6+x8+x10
        if b > H or c > H:
            continue
        if (x1+x8+x9+x10) & 1:
            continue
        support = sum(v > 0 for v in vals)
        required_parity = (x0+x8+x10) & 1
        qbc = sum(v*v for v in vals)
        t = x0+x1+x6+x9
        req((t & 1) == (c & 1), f"t parity drift {vals}")
        exact[(b,c,support,required_parity,qbc)].add(t)
        valid += 1
    return exact, valid

def strictness(exact):
    strict = removed = 0
    for (b,c,s,r,qbc), ts in exact.items():
        hull = current_hull(b,c,s,qbc)
        req(ts <= hull, f"unsafe refinement {(b,c,s,r,qbc)}")
        if ts != hull:
            strict += 1
            removed += len(hull-ts)
    merged = defaultdict(set)
    for (b,c,s,r,qbc), ts in exact.items():
        merged[(b,c,s,qbc)].update(ts)
    strict_merged = removed_merged = 0
    for (b,c,s,qbc), ts in merged.items():
        hull = current_hull(b,c,s,qbc)
        req(ts <= hull, f"unsafe marginal refinement {(b,c,s,qbc)}")
        if ts != hull:
            strict_merged += 1
            removed_merged += len(hull-ts)
    return len(exact), strict, removed, len(merged), strict_merged, removed_merged, merged

def main() -> None:
    obj = json.loads(PREFLIGHT.read_text())
    req(obj["schema"] == EXPECTED["schema"], "schema drift")
    req(canonical(obj) == EXPECTED["canonical"] == obj["canonical_sha256_without_this_field"], "canonical drift")
    sl = obj["source_locks"]
    req(sl["hpadj22_source_head"] == EXPECTED["hpadj22_head"], "HPADJ22 head drift")
    req(sl["v48_main_audited_head"] == EXPECTED["v48_head"], "V48 head drift")
    req(sl["v48_authority_canonical_sha256"] == EXPECTED["v48_canonical"], "V48 canonical drift")
    req(sl["support_qbc_worker_blob_sha1"] == EXPECTED["support_worker"], "support worker drift")

    exact, valid = build_exact(4)
    bins, strict, removed, mbins, mstrict, mremoved, merged = strictness(exact)
    got = (valid, bins, strict, removed, mbins, mstrict, mremoved)
    want = (686, 151, 91, 146, 101, 52, 74)
    req(got == want, f"bounded metrics drift got={got} want={want}")

    witness = merged[(0,4,1,16)]
    req(witness == {0}, f"witness exact set drift {witness}")
    req(current_hull(0,4,1,16) == {0,2,4}, "witness hull drift")

    p = obj["bounded_pilot"]
    req(p["valid_canonical_tuples"] == valid, "retained valid tuple count drift")
    req(p["exact_bins_with_required_parity"] == bins, "retained bin count drift")
    req(p["strict_vs_parity_hull_bins_with_required_parity"] == strict, "retained strict count drift")
    req(p["filled_hull_t_points_removed_with_required_parity"] == removed, "retained removed count drift")
    req(p["exact_bins_after_required_parity_marginalization"] == mbins, "retained marginal bin drift")
    req(p["strict_vs_parity_hull_bins_after_required_parity_marginalization"] == mstrict, "retained marginal strict drift")
    req(p["filled_hull_t_points_removed_after_required_parity_marginalization"] == mremoved, "retained marginal removed drift")

    print("PASS: HPADJ23 exact-t structural preflight")
    print(f"H=4 valid={valid} bins={bins} strict={strict} removed_hull_t={removed}")
    print(f"parity_marginal bins={mbins} strict={mstrict} removed_hull_t={mremoved}")
    print("witness=(b=0,c=4,support=1,qBC=16): exact_t=[0], hull=[0,2,4]")

if __name__ == "__main__":
    main()
