#!/usr/bin/env python3
"""checks15 / moduli6.py -- P2 of ANSWER-14: which degree-6 slack-0 maps have field of moduli inside Q(i)?

Input: the representative maps from f02/build_maps6.py (OUTDIR/state/<datum>.jsonl, 60 digits).
For each map:
  1. Newton refinement in mpmath at DPS digits (same system as refine5.py, normalisation x_kmax = 1).
  2. Invariants J_e = sum over all normalising triples (a, b, c) (a, b, c over the first three active labels)
     of t^e, e = 1, 2, 3, where t = sum_y sum_{k=1,2} r_{y,k} * (power sum of degree k of the cross ratios
     w(x) = (x-a)(c-b)/((x-b)(c-a)) over the critical points x with label y, x not in {a,b,c}).
     The J_e are rational expressions with Q coefficients, invariant under source Moebius maps and under
     permutations within labels.  Gal(Qbar/Q(i)) fixes B pointwise, so J_e(sigma p) = sigma(J_e(p)).
     Hence if (J_1, J_2, J_3) is injective on the maps of the datum (checked numerically: trap F),
     field of moduli of p  subset of Q(i)  <=>  all J_e(p) in Q(i).
  3. Re J_e, Im J_e are tested for being rational by PSLQ on [x, 1] (maxcoeff 10^MAXC); a relation is
     accepted only if its height leaves >= 60 digits of margin (log10|a| + log10|b| < DPS - 60).
     "not in Q(i)" means: no relation of that height, a numerical statement, not a proof.
Structure flags per map: n3 = labels with three critical points (two such labels => p = f o g with deg f = 2,
since P - uQ and P - vQ are then squares), and the number of active labels (critical values).
Output: OUT/moduli6/<datum>.jsonl (resumable), OUT/moduli6.summary.json
Usage: python -I moduli6.py MAPSDIR OUTDIR [--workers 11] [--dps 220]
"""
import os, sys
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import argparse, itertools, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02"))
sys.path.insert(0, F02)
import mpmath as mp
import build_maps as bm
import build_maps5 as b5

n = int(os.environ.get("MAPS_N", "6"))   # 5 only as a regression test
CHUNK = 60
BKEYS = bm.BKEYS
WEIGHTS = {("I", 1): 1, ("I", 2): 2, ("-I", 1): 3, ("-I", 2): 5, ("1", 1): 7, ("1", 2): 11,
           ("-1", 1): 13, ("-1", 2): 17, ("0", 1): 19, ("0", 2): 23, ("oo", 1): 29, ("oo", 2): 31}


def refine(rec, dps):
    P, Q, cps, vals = rec
    with mp.workdps(dps):
        x = [mp.mpc(t) for t in list(P) + list(Q)]; lam = [mp.mpc(t) for t in cps[3:]]
        kmax = max(range(len(x)), key=lambda k: abs(x[k])); s = x[kmax]; x = [t / s for t in x]
        zz = x + lam; m = len(zz)
        def FJ(zz):
            xx = zz[:2 * n + 2]; cl = [mp.mpf(0), "oo", mp.mpf(1)] + list(zz[2 * n + 2:])
            F = []; J = mp.matrix(m, m); r = 0
            for i, (c, y) in enumerate(zip(cl, vals)):
                yv = (mp.mpc(bm.BH[y][0]), mp.mpc(bm.BH[y][1]))
                for d in (0, 1):
                    row = bm.cond_rows(n, c, yv, d)
                    F.append(mp.fsum(a * b for a, b in zip(row, xx)))
                    for k in range(2 * n + 2): J[r, k] = row[k]
                    if i >= 3: J[r, 2 * n + 2 + i - 3] = mp.fsum(a * b for a, b in zip(bm.drow(n, c, yv, d), xx))
                    r += 1
            F.append(xx[kmax] - 1); J[r, kmax] = 1
            return F, J
        for _ in range(12):
            F, J = FJ(zz)
            dz = mp.lu_solve(J, mp.matrix([-f for f in F]))
            zz = [a + dz[k] for k, a in enumerate(zz)]
            if mp.norm(dz) < mp.mpf(10) ** (-(dps - 15)): break
        F, _ = FJ(zz)
        res = mp.norm(mp.matrix(F))
    return zz, res


def crv(x, a, b, c):
    """(x-a)(c-b)/((x-b)(c-a)); factors containing oo are dropped (they cancel in pairs)"""
    def f(p, q): return None if (p is None or q is None) else p - q
    num = [f(x, a), f(c, b)]; den = [f(x, b), f(c, a)]
    N = mp.mpf(1); D = mp.mpf(1)
    for t in num:
        if t is not None: N *= t
    for t in den:
        if t is not None: D *= t
    return N / D


def invariants(zz, vals, ns, dps):
    with mp.workdps(dps):
        cps = [mp.mpf(0), None, mp.mpf(1)] + list(zz[2 * n + 2:])
        act = [y for y, k in zip(BKEYS, ns) if k][:3]
        pools = [[i for i, v in enumerate(vals) if v == y] for y in act]
        J = [mp.mpf(0)] * 3
        for tri in itertools.product(*pools):
            a, b, c = [cps[i] for i in tri]
            t = mp.mpf(0)
            for y in BKEYS:
                ws = [crv(cps[i], a, b, c) for i, v in enumerate(vals) if v == y and i not in tri]
                if not ws: continue
                t += WEIGHTS[(y, 1)] * mp.fsum(ws) + WEIGHTS[(y, 2)] * mp.fsum(w * w for w in ws)
            for e in range(3): J[e] += t ** (e + 1)
        return J


def rational(x, dps, maxc):
    with mp.workdps(dps):
        if abs(x) < mp.mpf(10) ** (-(dps - 40)): return "0"
        r = mp.pslq([x, mp.mpf(1)], maxcoeff=10 ** maxc, maxsteps=10 ** 6, tol=mp.mpf(10) ** (-(dps - 30)))
        if r is None or r[0] == 0: return None
        a, b = r
        h = mp.log10(abs(a) + 1) + mp.log10(abs(b) + 1)
        if h > dps - 60: return None
        return f"{-b}/{a}"


def work(args):
    datum, lo, mapsdir, outdir, dps = args
    ns = [int(c) for c in datum]
    src = os.path.join(mapsdir, "state", f"{datum}.jsonl")
    dst = os.path.join(outdir, "moduli6", f"{datum}.{lo:05d}.part")
    done = set()
    if os.path.exists(dst):
        for l in open(dst):
            if l.strip(): done.add(json.loads(l)["idx"])
    rows = [json.loads(l) for l in open(src) if l.strip()]
    maxc = (dps - 60) // 2
    t0 = time.time()
    with open(dst, "a") as f:
        for idx, r in enumerate(rows):
            if idx in done or not (lo <= idx < lo + CHUNK): continue
            rec = b5.parse_state_map(r)
            zz, res = refine(rec, dps)
            J = invariants(zz, rec[3], ns, dps)
            rq = [[rational(j.real, dps, maxc), rational(j.imag, dps, maxc)] for j in J]
            inQi = all(a is not None and b is not None for a, b in rq)
            out = {"idx": idx, "datum": datum, "residual": mp.nstr(res, 5),
                   "J": [[mp.nstr(j.real, 50), mp.nstr(j.imag, 50)] for j in J],
                   "rational": rq, "in_Qi": inQi}
            f.write(json.dumps(out) + "\n"); f.flush()
    return datum, lo, time.time() - t0


def summarize(mapsdir, outdir, dps):
    summ = {}
    parts = {}
    for fn in sorted(os.listdir(os.path.join(outdir, "moduli6"))):
        if fn.endswith(".part"): parts.setdefault(fn.split(".")[0], []).append(fn)
    for datum, fns in sorted(parts.items()):
        ns = [int(c) for c in datum]
        rows = sorted((json.loads(l) for fn in fns for l in open(os.path.join(outdir, "moduli6", fn)) if l.strip()),
                      key=lambda r: r["idx"])
        with mp.workdps(dps):
            Js = [(mp.mpf(r["J"][0][0]), mp.mpf(r["J"][0][1]), mp.mpf(r["J"][1][0]), mp.mpf(r["J"][1][1])) for r in rows]
            close = 0; eps = mp.mpf(10) ** -30
            Js.sort(key=lambda t: t[0])
            for i, a in enumerate(Js):
                for b in Js[i + 1:]:
                    if abs(b[0] - a[0]) / (1 + abs(a[0])) >= eps: break
                    if max(abs(x - y) / (1 + abs(x)) for x, y in zip(a, b)) < eps: close += 1
        summ[datum] = {"maps": len(rows), "in_Qi": [r["idx"] for r in rows if r["in_Qi"]],
                       "n3_labels": sum(1 for k in ns if k == 3), "critical_values": sum(1 for k in ns if k),
                       "J_collisions": close, "worst_residual": max((r["residual"] for r in rows), key=lambda s: mp.mpf(s)) if rows else None}
    json.dump(summ, open(os.path.join(outdir, "moduli6.summary.json"), "w"), indent=1)
    tot = sum(len(v["in_Qi"]) for v in summ.values())
    print("data", len(summ), "maps", sum(v["maps"] for v in summ.values()), "in Q(i)", tot,
          "J collisions", sum(v["J_collisions"] for v in summ.values()))
    for d, v in summ.items():
        if v["in_Qi"]: print(" ", d, "n3", v["n3_labels"], "values", v["critical_values"], "in_Qi", len(v["in_Qi"]), "/", v["maps"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mapsdir"); ap.add_argument("outdir")
    ap.add_argument("--workers", type=int, default=11); ap.add_argument("--dps", type=int, default=220)
    ap.add_argument("--only", default=""); ap.add_argument("--summary-only", action="store_true")
    a = ap.parse_args()
    os.makedirs(os.path.join(a.outdir, "moduli6"), exist_ok=True)
    if not a.summary_only:
        data = sorted(fn[:-6] for fn in os.listdir(os.path.join(a.mapsdir, "state")) if fn.endswith(".jsonl"))
        if a.only: data = [d for d in data if d in set(a.only.split(","))]
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=a.workers) as ex:
            jobs = []
            for d in data:
                cnt = sum(1 for l in open(os.path.join(a.mapsdir, "state", d + ".jsonl")) if l.strip())
                jobs += [(d, lo, a.mapsdir, a.outdir, a.dps) for lo in range(0, cnt, CHUNK)]
            for d, lo, s in ex.map(work, jobs):
                print(d, lo, f"{s:.0f}s", flush=True)
    summarize(a.mapsdir, a.outdir, a.dps)


if __name__ == "__main__":
    main()
