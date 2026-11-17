#!/usr/bin/env python3
"""checks15 / fpcount2.py -- same count as fpcount.py, but only one fibre-over-0 form P0 per PGL_2(F_p)-orbit.

count = sum over orbits O of P0-forms of |O| * #{(Q0, c) valid with the representative}, because the source action of
PGL_2(F_p) maps valid triples to valid triples bijectively.  Orbits by BFS with the generators X -> X + Y, X -> g X
(g a primitive root) and X <-> Y.  Work drops by about p^3.  N_p = count / |PGL_2(F_p)| as before.
Results are written to fpcount2.jsonl; fpcount.jsonl (full count) is used as a regression check for small p.
Usage: python -I fpcount2.py n p [datum ...]
"""
import os, sys, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fpcount as F1


def prim_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in {q for q in range(2, p) if (p - 1) % q == 0 and all(q % r for r in range(2, q))}):
            return g


def normalise(f, p):
    k = max(i for i, x in enumerate(f) if x)
    il = pow(f[k], p - 2, p)
    return tuple((x * il) % p for x in f)


def act_T(f, p):
    """F(X, Y) -> F(X + Y, Y); f[k] = coefficient of X^k Y^(n-k)"""
    n = len(f) - 1; r = [0] * (n + 1)
    from math import comb
    for k, a in enumerate(f):
        if a:
            for j in range(k + 1): r[j] = (r[j] + a * comb(k, j)) % p
    return tuple(r)


def orbits(forms, p):
    g = prim_root(p)
    idx = {normalise(f, p): i for i, f in enumerate(forms)}
    seen = [False] * len(forms); reps = []
    for i0 in range(len(forms)):
        if seen[i0]: continue
        seen[i0] = True; stack = [i0]; size = 0
        while stack:
            i = stack.pop(); size += 1
            f = tuple(forms[i])
            for h in (act_T(f, p), tuple((a * pow(g, k, p)) % p for k, a in enumerate(f)), tuple(reversed(f))):
                j = idx[normalise(h, p)]
                if not seen[j]: seen[j] = True; stack.append(j)
        reps.append((i0, size))
    return reps


def run(n, p, datum, cp, kern):
    ns = F1.best_rotation(datum)
    i = F1.sqrt_m1(p)
    yv = [i, p - i, 1, p - 1]; want = ns[:4]
    t0 = time.time()
    Pall = F1.fibre_polys(n, ns[4], p)
    reps = orbits(Pall, p)
    G = p * (p * p - 1)
    assert sum(s for _, s in reps) == len(Pall)
    P = np.array([Pall[j] for j, _ in reps], dtype=np.int32)
    W = [s for _, s in reps]
    Q = np.array(F1.fibre_polys(n, ns[5], p), dtype=np.int32)
    inv = np.array([0] + [pow(x, p - 2, p) for x in range(1, p)], dtype=np.int32)
    dQ = cp.asarray(Q); dinv = cp.asarray(inv); dy = cp.asarray(np.array(yv, dtype=np.int32)); dw = cp.asarray(np.array(want, dtype=np.int32))
    total = 0
    for r, wgt in zip(P, W):                      # one launch per representative; weights applied on the host
        out = cp.zeros(1, dtype=cp.uint64)
        kern((1024,), (256,), (cp.asarray(r[None, :]), dQ, np.int64(1), np.int64(len(Q)), np.int32(n), np.int32(p), dinv, dy, dw, out))
        total += int(out[0]) * wgt
    cp.cuda.Stream.null.synchronize()
    return {"n": n, "p": p, "datum": datum, "rotated": "".join(map(str, ns)), "orbits": len(reps), "nP": len(Pall), "nQ": len(Q),
            "count": total, "N_p": total / G, "integral": total % G == 0, "seconds": round(time.time() - t0, 1)}


def main():
    import cupy as cp
    n, p = int(sys.argv[1]), int(sys.argv[2])
    assert p % 4 == 1 and p > n
    data = sys.argv[3:]
    if not data:
        H = json.load(open(os.path.join(F1.F02, f"hurwitz{n}.json" if n != 6 else "hurwitz6.json")))
        seen = set()
        for d in sorted(k for k in H if not k.startswith("_")):
            if H[d][0] == 0: continue
            r = "".join(map(str, F1.best_rotation(d)))
            if r in seen: continue
            seen.add(r); data.append(d)
    outf = os.path.join(HERE, "fpcount2.jsonl")
    done = set()
    if os.path.exists(outf):
        for l in open(outf):
            if l.strip(): r = json.loads(l); done.add((r["n"], r["p"], r["rotated"]))
    kern = cp.RawKernel(F1.KERNEL, "count")
    for d in data:
        rot = "".join(map(str, F1.best_rotation(d)))
        if (n, p, rot) in done: continue
        r = run(n, p, d, cp, kern)
        print(json.dumps(r), flush=True)
        with open(outf, "a") as f: f.write(json.dumps(r) + "\n")
        done.add((n, p, rot))


if __name__ == "__main__":
    main()
