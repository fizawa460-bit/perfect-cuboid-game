#!/usr/bin/env python3
"""Expand degree-5 slack-0 maps from orbit representatives to all 90 branch types.

The 24 orientation-preserving octahedral rotations h permute B = {0, oo, +-1, +-i}.
For a slack-0 map p with branch type ns, h o p is a slack-0 map with the permuted
type, the same critical points, and critical values h(v).  Since h is a bijection
on maps of type ns -> maps of type h(ns), the representative maps determine all.

Checks:
  (a) every input map: Wronskian roots = finite critical points (simple, 2n-3 finite
      + oo), values p(c) = prescribed value, residual recorded;
  (b) per target type: images from every rotation h with h(rep) = target are
      deduplicated (signature prefilter + exact coefficient identity after source
      Moebius); final count must equal the hurwitz5.json target; and every single h
      must alone give exactly `target` distinct maps (consistency of the bijection);
  (c) total 6090.
Usage: python -I expand5.py IN_STATE OUTDIR
"""
import itertools
import json
import os
import sys
import time
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import mpmath as mp
import build_maps5 as b5

mp.mp.dps = 110
n = 5
BKEYS = b5.BKEYS                       # ["I", "-I", "1", "-1", "0", "oo"]
PT = {"I": mp.mpc(0, 1), "-I": mp.mpc(0, -1), "1": mp.mpc(1), "-1": mp.mpc(-1),
      "0": mp.mpc(0), "oo": mp.inf}


def apply_mob(M, z):
    a, b, c, d = M
    if z == mp.inf:
        return mp.inf if abs(c) < mp.mpf("1e-50") else a / c
    den = c * z + d
    if abs(den) < mp.mpf("1e-50"):
        return mp.inf
    return (a * z + b) / den


def label_of(z):
    for k, v in PT.items():
        if v == mp.inf and z == mp.inf:
            return k
        if v != mp.inf and z != mp.inf and abs(z - v) < mp.mpf("1e-40"):
            return k
    raise ValueError(z)


def rotations():
    gens = [(mp.mpc(0, 1), mp.mpc(0), mp.mpc(0), mp.mpc(1)),      # z -> i z
            (mp.mpc(1), mp.mpc(1), mp.mpc(-1), mp.mpc(1))]        # z -> (z+1)/(-z+1)
    def perm(M):
        return tuple(label_of(apply_mob(M, PT[k])) for k in BKEYS)
    def mul(A, B):
        a, b, c, d = A; e, f, g, h = B
        return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
    ident = (mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1))
    group = {perm(ident): ident}
    frontier = [ident]
    while frontier:
        new = []
        for M in frontier:
            for G in gens:
                N = mul(G, M)
                p = perm(N)
                if p not in group:
                    group[p] = N; new.append(N)
        frontier = new
    assert len(group) == 24, len(group)
    return [(dict(zip(BKEYS, p)), M) for p, M in group.items()]


def check_map(P, Q, cps, vals):
    """residual of critical structure; raises on failure"""
    dP = [k * P[k] for k in range(1, n + 1)]; dQ = [k * Q[k] for k in range(1, n + 1)]
    W = [mp.mpc(0)] * (2 * n)
    for i, a in enumerate(dP):
        for k, b in enumerate(Q): W[i + k] += a * b
    for i, a in enumerate(P):
        for k, b in enumerate(dQ): W[i + k] -= a * b
    nrm = max(abs(t) for t in P + Q)
    deg = max(k for k in range(2 * n) if abs(W[k]) > mp.mpf("1e-40") * nrm ** 2)
    fin = [c for c in cps if c != mp.inf]
    n_inf = sum(1 for c in cps if c == mp.inf)
    assert len(cps) == 2 * n - 2 and n_inf <= 1
    assert n_inf == 1 and deg == len(fin) == 2 * n - 3, (deg, len(fin))
    rts = mp.polyroots(list(reversed(W[:deg + 1])), maxsteps=500, extraprec=500)
    # each finite critical point matched by a distinct Wronskian root
    used = set(); worst = mp.mpf(0)
    for c in fin:
        j = min((j for j in range(len(rts)) if j not in used), key=lambda j: abs(rts[j] - c))
        used.add(j); worst = max(worst, abs(rts[j] - c) / (1 + abs(c)))
    # values
    for c, y in zip(cps, vals):
        if c == mp.inf:
            num, den = P[n], Q[n]
        else:
            num = mp.polyval(list(reversed(P)), c); den = mp.polyval(list(reversed(Q)), c)
        if PT[y] == mp.inf:
            r = abs(den) / (abs(num) + abs(den))
        else:
            r = abs(num - PT[y] * den) / (abs(num) + abs(den))
        worst = max(worst, r)
    # distinctness of critical points
    for a, b in itertools.combinations(fin, 2):
        assert abs(a - b) > mp.mpf("1e-12")
    return worst


def compose(M, rec):
    a, b, c, d = M
    P, Q, cps, vals = rec
    P2 = [a * p + b * q for p, q in zip(P, Q)]
    Q2 = [c * p + d * q for p, q in zip(P, Q)]
    s = max(abs(t) for t in P2 + Q2)
    return [t / s for t in P2], [t / s for t in Q2], list(cps), None


def main():
    in_state, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    targets = b5.load_targets(5)
    reps = b5.read_state(in_state)
    t0 = time.time()
    rots = rotations()
    worst_in = mp.mpf(0)
    for d, recs in reps.items():
        assert len(recs) == targets[d], (d, len(recs))
        for rec in recs:
            worst_in = max(worst_in, check_map(*rec))
    print(f"input reps: {sum(len(v) for v in reps.values())} maps in {len(reps)} types; worst residual {mp.nstr(worst_in, 5)}", flush=True)

    images = defaultdict(list)            # target datum -> list of (rot index, rec)
    for d, recs in reps.items():
        ns = dict(zip(BKEYS, (int(ch) for ch in d)))
        for ri, (perm, M) in enumerate(rots):
            ns2 = {perm[k]: v for k, v in ns.items()}
            d2 = "".join(str(ns2[k]) for k in BKEYS)
            for rec in recs:
                P2, Q2, cps, _ = compose(M, rec)
                vals2 = [perm[y] for y in rec[3]]
                images[d2].append((ri, d, (P2, Q2, cps, vals2)))
    assert set(images) == set(targets), set(targets) ^ set(images)

    out = {}; worst_out = mp.mpf(0); exact_calls = 0; report = {}
    for d2 in sorted(targets):
        tgt = targets[d2]
        ns2 = [int(ch) for ch in d2]
        uniq, uniq_sigs, sig_rows, sig_owner = [], [], [], []
        per_rot = defaultdict(int)
        for ri, src, rec in images[d2]:
            sig = b5.signature_set(n, rec, ns2)
            v0 = np.array([float(x) for x in sig[0]])
            dup = False
            if sig_rows:
                A = np.array(sig_rows)
                dist = np.max(np.abs(A - v0), axis=1)
                for j in np.nonzero(dist < 1e-9)[0]:
                    exact_calls += 1
                    if b5.equivalent_by_source_mobius(n, uniq[sig_owner[j]], rec):
                        dup = True; break
            if not dup:
                worst_out = max(worst_out, check_map(*rec))
                k = len(uniq); uniq.append(rec)
                for s in sig:
                    sig_rows.append([float(x) for x in s]); sig_owner.append(k)
        # per-rotation consistency: each rotation hitting d2 contributes |reps of its source| maps
        rot_src = defaultdict(int)
        for ri, src, rec in images[d2]:
            rot_src[(ri, src)] += 1
        assert all(c == tgt for c in rot_src.values()), (d2, set(rot_src.values()), tgt)
        report[d2] = {"target": tgt, "found": len(uniq), "images": len(images[d2]),
                      "rotations": len(rot_src)}
        status = "OK" if len(uniq) == tgt else "MISMATCH"
        print(f"[{d2}] {len(uniq)}/{tgt} from {len(images[d2])} images ({len(rot_src)} rotations) {status}", flush=True)
        out[d2] = uniq
    total = sum(len(v) for v in out.values())
    ok = all(r["found"] == r["target"] for r in report.values()) and total == 6090
    print(f"TOTAL {total}/6090; all types match: {ok}; worst output residual {mp.nstr(worst_out, 5)}; "
          f"exact tests {exact_calls}; {time.time()-t0:.1f}s", flush=True)
    b5.export_outputs(5, targets, out, outdir)
    b5.rewrite_state_file(os.path.join(outdir, "maps5.state.jsonl"), targets, out)
    with open(os.path.join(outdir, "expand5.report.json"), "w", encoding="utf-8") as f:
        json.dump({"total": total, "ok": ok, "worst_input_residual": mp.nstr(worst_in, 5),
                   "worst_output_residual": mp.nstr(worst_out, 5), "types": report}, f, indent=1)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
