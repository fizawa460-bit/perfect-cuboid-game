#!/usr/bin/env python3
"""Compare two slack-0 map lists of degree n up to source Moebius (bijection test).

A: a state.jsonl (with critical data) from build_maps5.py;  B: a flat maps{n}.json [{datum,P,Q}].
Critical points/values of B are recomputed from the Wronskian.  Within A, duplicates are also
counted (fixed signature sort, see the PATCH note in build_maps5.signature_set).
Usage: python -I compare_maps.py N A_state.jsonl B_maps.json
"""
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import mpmath as mp
import build_maps as bm
import build_maps5 as b5

mp.mp.dps = 60
PT = {"I": mp.mpc(0, 1), "-I": mp.mpc(0, -1), "1": mp.mpc(1), "-1": mp.mpc(-1), "0": mp.mpc(0)}


def crit_data(n, P, Q):
    dP = [k * P[k] for k in range(1, n + 1)]; dQ = [k * Q[k] for k in range(1, n + 1)]
    W = [mp.mpc(0)] * (2 * n)
    for i, a in enumerate(dP):
        for k, b in enumerate(Q): W[i + k] += a * b
    for i, a in enumerate(P):
        for k, b in enumerate(dQ): W[i + k] -= a * b
    nrm = max(abs(t) for t in P + Q)
    deg = max(k for k in range(2 * n - 1) if abs(W[k]) > mp.mpf("1e-35") * nrm ** 2)
    rts = list(mp.polyroots(list(reversed(W[:deg + 1])), maxsteps=500, extraprec=300)) if deg > 0 else []
    cps = []
    if deg < 2 * n - 2:
        assert deg == 2 * n - 3, "critical point at oo not simple"
        cps.append(mp.inf)
    cps += rts
    vals = []
    for c in cps:
        if c == mp.inf: num, den = P[n], Q[n]
        else: num = mp.polyval(list(reversed(P)), c); den = mp.polyval(list(reversed(Q)), c)
        s = abs(num) + abs(den)
        if abs(den) < mp.mpf("1e-25") * s: vals.append("oo"); continue
        w = num / den
        lab = min(PT, key=lambda k: abs(w - PT[k]))
        assert abs(w - PT[lab]) < mp.mpf("1e-25"), mp.nstr(w, 10)
        vals.append(lab)
    # put three points over distinct values first (equivalence test frames on cB[:3])
    order = []; seen = set()
    for i, v in enumerate(vals):
        if v not in seen and len(order) < 3: order.append(i); seen.add(v)
    order += [i for i in range(len(cps)) if i not in order]
    return [cps[i] for i in order], [vals[i] for i in order]


def dedupe_match(n, ns, pool, item):
    sig = b5.signature_set(n, item, ns)
    for k, (rec, sigs) in enumerate(pool):
        if any(b5.signatures_close(a, b) for a in sig[:1] for b in sigs):
            if b5.equivalent_by_source_mobius(n, rec, item):
                return k, sig
    return None, sig


def main():
    n = int(sys.argv[1])
    A = b5.read_state(sys.argv[2])
    with open(sys.argv[3], encoding="utf-8") as f:
        Bflat = json.load(f)
    B = defaultdict(list)
    for r in Bflat:
        P = [bm.parse_c(x) for x in r["P"]]; Q = [bm.parse_c(x) for x in r["Q"]]
        cps, vals = crit_data(n, P, Q)
        B[r["datum"]].append((P, Q, cps, vals))
    types = sorted(set(A) | set(B))
    bad = 0; dupA = 0; totA = 0; totB = 0
    for d in types:
        ns = [int(c) for c in d]
        poolA = []
        for rec in A.get(d, []):
            k, sig = dedupe_match(n, ns, poolA, rec)
            if k is None: poolA.append((rec, sig))
            else: dupA += 1
        matched = set(); unmatched = 0
        for rec in B.get(d, []):
            k, _ = dedupe_match(n, ns, poolA, rec)
            if k is None or k in matched: unmatched += 1
            else: matched.add(k)
        totA += len(poolA); totB += len(B.get(d, []))
        if unmatched or len(matched) != len(poolA):
            bad += 1
            print(f"[{d}] A distinct {len(poolA)}, B {len(B.get(d, []))}, matched {len(matched)}, B unmatched {unmatched}")
    print(f"types {len(types)}; A distinct {totA} (dups removed {dupA}); B {totB}; types with differences {bad}")


if __name__ == "__main__":
    main()
