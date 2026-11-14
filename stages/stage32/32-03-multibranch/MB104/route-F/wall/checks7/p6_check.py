"""CHECK-04: predictions P-6a and P-6b of THEORY-06 on the (4,4) extremal slack-0 pairs of F-02.

For each configuration (p1, q, T), p2 = q o T, the branches of W = Phi(P^1) at the 12 matched points P in Z are
found from p1^-1(B) (refined zeros) with local degrees (e1, e2). For g = (g1, g2) in G = V4 x V4, g != e:
  - gW = W is tested at a generic point (then g is skipped, as in lemma T);
  - P-6b: L(g) = sum_P m_P m_{g^-1 P}, compared with 2ab = 32;
  - P-6a: a branch of W at P and a branch of gW at P (image of a branch of W at g^-1 P) are tangent when their
    tangent directions agree (direction: leading coefficients cY/cX of the branch in local charts, horizontal if
    e1 < e2, vertical if e1 > e2). Tangent pairs force local intersection > m m'. Each tangency is tagged "self" (a branch and its own image: g fixes
    P, and g = (s, s') acts with derivative (-1, -1), or (-1, 1) on a horizontal branch) or "other".
Directions are computed with mpmath derivatives (dps 60) of chart(g_i(p_i(t))); equal = relative difference < 1e-20.
usage: python -I -O p6_check.py extremal4x4.json [workers]   (input from ../../f02; output p6_<input>.jsonl + summary)
"""
import itertools, json, os, sys, time
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
O3 = os.path.normpath(os.path.join(HERE, "..", "..", "o3")); sys.path.insert(0, O3)
import o3_genus as O
mp = O.mp; RA = O.RA
V4 = {"t": lambda z: z, "-t": lambda z: mp.inf if z == mp.inf else -z,
      "1/t": lambda z: mp.mpc(0) if z == mp.inf else (mp.inf if z == 0 else 1 / z),
      "-1/t": lambda z: mp.mpc(0) if z == mp.inf else (mp.inf if z == 0 else -1 / z)}
BNAME = {"e": [mp.mpc(0), mp.inf], "b": [mp.mpc(1), mp.mpc(-1)], "a": [mp.mpc(0, 1), mp.mpc(0, -1)]}


def snap(v):
    for l, vals in BNAME.items():
        for k, b in enumerate(vals):
            if b == mp.inf:
                if v == mp.inf or abs(v) > mp.mpf(10) ** 12: return (l, k)
            elif v != mp.inf and abs(v - b) < mp.mpf(10) ** -12: return (l, k)
    return None


def bval(key): return BNAME[key[0]][key[1]]


def chart(beta, z):
    """local coordinate at beta"""
    if beta == mp.inf: return mp.mpc(0) if z == mp.inf else 1 / z
    return z - beta


def pval(P, Q, t):
    q = O.peval(Q, t); p = O.peval(P, t)
    return mp.inf if abs(q) < mp.mpf(10) ** -50 * (abs(p) + 1) else p / q


def lead(P, Q, gname, t0, beta_img, e):
    """leading coefficient of chart_{beta_img}(g(p(t))) at t0 (order e)"""
    f = lambda t: chart(beta_img, V4[gname](pval(P, Q, t)))
    return mp.diff(f, t0, e) / mp.factorial(e)


def direction(e1, c1, e2, c2):
    if e1 < e2: return mp.mpc(0)
    if e1 > e2: return mp.inf
    return c2 / c1


def same_dir(d, d2):
    if d == mp.inf or d2 == mp.inf: return d == d2
    return abs(d - d2) < mp.mpf(10) ** -20 * (1 + abs(d) + abs(d2))


_W = {}


def init(): RA._rinit(4, 4); _W.update(RA._R)


def work(rec):
    ia, ib, co = rec["ia"], rec["ib"], rec["co"]
    O1, Oq = _W["A_mp"][ia], _W["B_mp"][ib]
    X1 = [p for p, _ in O1]; Xq = [p for p, _ in Oq]
    T = RA.frame(*[Xq[c[1]] for c in co[:3]]) * mp.inverse(RA.frame(*[X1[c[0]] for c in co[:3]]))
    P1, Q1 = [mp.mpc(x) for x in _W["A_maps"][ia][0]], [mp.mpc(x) for x in _W["A_maps"][ia][1]]
    Pq, Qq = [mp.mpc(x) for x in _W["B_maps"][ib][0]], [mp.mpc(x) for x in _W["B_maps"][ib][1]]
    P1s, Q1s = O.subst(P1, O.SIG), O.subst(Q1, O.SIG); MT = T * O.SIG; P2s, Q2s = O.subst(Pq, MT), O.subst(Qq, MT)
    br = []                                    # branches: (t, key1, key2, e1, e2)
    for l, vals in BNAME.items():
        for bv in vals:
            F1 = Q1s if bv == mp.inf else O.padd(P1s, [bv * c for c in Q1s], -1)
            r1, inf1 = O.roots(F1); assert inf1 == 0
            for w, e1 in O.clusters(r1, 1e-8):
                w = O.refine(F1, w, e1)
                k1 = snap(pval(P1s, Q1s, w)); k2 = snap(pval(P2s, Q2s, w))
                if k1 and k2 and k1[0] == k2[0]:
                    l2, e2 = O.local_deg(P2s, Q2s, w)
                    br.append((w, k1, k2, e1, e2))
    m = Counter()
    for w, k1, k2, e1, e2 in br: m[(k1, k2)] += min(e1, e2)
    pts = [(k1, k2) for l in BNAME for k1 in [(l, 0), (l, 1)] for k2 in [(l, 0), (l, 1)]]
    gnames = list(V4)
    def act(gn, key): return snap(V4[gn](bval(key)))
    t0 = mp.mpc("0.4142", "0.3317")
    Lmax = 0; tang = Counter(); skipped = 0
    for g1, g2 in itertools.product(gnames, gnames):
        if g1 == "t" and g2 == "t": continue
        # gW = W ?  (image of a generic point lies on W)
        x0, y0 = V4[g1](pval(P1s, Q1s, t0)), V4[g2](pval(P2s, Q2s, t0))
        F = O.padd(P1s, [x0 * c for c in Q1s], -1)
        rr, _ = O.roots(F)
        if any(O.chord(pval(P2s, Q2s, r), y0) < 1e-20 for r in rr): skipped += 1; continue
        L = sum(m[P] * m[(act(g1, P[0]), act(g2, P[1]))] for P in pts)     # g involution: g^-1 P = g P
        Lmax = max(Lmax, L)
        for w, k1, k2, e1, e2 in br:            # branch of W at P = (k1, k2)
            d = direction(e1, lead(P1s, Q1s, "t", w, bval(k1), e1), e2, lead(P2s, Q2s, "t", w, bval(k2), e2))
            for w2, j1, j2, f1, f2 in br:       # branch of W at g P, mapped by g to P
                if (act(g1, j1), act(g2, j2)) != (k1, k2): continue
                d2 = direction(f1, lead(P1s, Q1s, g1, w2, bval(k1), f1), f2, lead(P2s, Q2s, g2, w2, bval(k2), f2))
                if same_dir(d, d2):
                    self_img = O.chord(w, w2) < 1e-20           # the branch and its own image (g fixes P)
                    tang[f"{'self' if self_img else 'other'} ({e1},{e2})x({f1},{f2}) g={g1},{g2}"] += 1
    return dict(ia=ia, ib=ib, jh=rec["exact"][1:], M=sum(m.values()), branches=len(br), Lmax=Lmax,
                tangent=dict(tang), g_skipped=skipped)


if __name__ == "__main__":
    inp = sys.argv[1]; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    recs = json.load(open(os.path.join(O.F02, inp)))
    out = os.path.join(HERE, "p6_" + inp.replace(".json", ".jsonl"))
    done = set()
    if os.path.exists(out):
        for line in open(out): done.add(json.loads(line)["k"])
    todo = [k for k in range(len(recs)) if k not in done]
    print(f"{inp}: {len(recs)} records, {len(todo)} to do", flush=True); t0 = time.time()
    with Pool(workers, initializer=init) as pool, open(out, "a") as f:
        for n, (k, r) in enumerate(zip(todo, pool.imap(work, [recs[k] for k in todo], chunksize=20))):
            r["k"] = k; f.write(json.dumps(r) + chr(10)); f.flush()
            if n % 1000 == 0: print(f"  {n}/{len(todo)} {time.time() - t0:.0f}s", flush=True)
    rows = [json.loads(l) for l in open(out)]
    summ = dict(input=inp, records=len(rows), Lmax_max=max(r["Lmax"] for r in rows), two_ab=32,
                Lmax_hist=sorted(Counter(r["Lmax"] for r in rows).items()),
                tangent_total=sum(sum(r["tangent"].values()) for r in rows),
                tangent_other=sum(v for r in rows for k, v in r["tangent"].items() if k.startswith("other")),
                tangent_types=dict(sum((Counter(r["tangent"]) for r in rows), Counter())),
                records_with_tangency=sum(1 for r in rows if r["tangent"]),
                g_skipped_hist=sorted(Counter(r["g_skipped"] for r in rows).items()),
                M_hist=sorted(Counter(r["M"] for r in rows).items()))
    json.dump(summ, open(out.replace(".jsonl", "_summary.json"), "w"), indent=1)
    print(json.dumps(summ))
