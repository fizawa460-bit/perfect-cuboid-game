"""O3: genus of the Pell cover C: y^2 = phi(p1) - phi(p2), phi(x) = x^2 + x^-2, for the low-mismatch slack-0 pairs of F-02.

For p_i = P_i/Q_i (homogeneous), phi(p1) - phi(p2) = N / (P1 Q1 P2 Q2)^2 with
  N = (P1^4 + Q1^4) P2^2 Q2^2 - (P2^4 + Q2^4) P1^2 Q1^2,   bihomogeneous of degree 4(a+b) in the source,
and div(N) = Phi^*(sum of the 4 Klein graphs). The denominator is a square, so the odd-order points of
phi(p1) - phi(p2) are the odd-multiplicity zeros of N, and g(C) = (#odd - 2)/2 (#odd = 0: C splits).
Recorded per configuration (p1, q, T), p2 = q o T:
  M_K = sum over matched v (Phi(v) in B x B, same label) of min(e_v(p1), e_v(p2))   (Lemma K: M_K <= 2(a+b));
  deficiency = 4(a+b) - 2 M_K = sum_J exc_v + sum_{v not in J} ord_v N;  #odd;  g(C);  check of the identity.
Precision: the maps are stored with 40 digits; work at dps 60. The source is moved by a fixed random Moebius map so
that no zero of N is at infinity. Zeros of N are clustered (chordal 1e-6); the run flags any configuration whose
clusters are not separated by at least 1e-3, or whose multiplicities disagree with the local degrees.
usage: python -I -O o3_genus.py 4 4 extremal4x4.json [workers]    (inputs from ../f02; output o3_<input>.jsonl)
"""
import json, os, sys, time
from collections import Counter
from multiprocessing import Pool
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "f02")); sys.path.insert(0, F02)
import recheck_amb as RA
mp.mp.dps = 60
SIG = mp.matrix([[mp.mpc("0.8712", "0.2213"), mp.mpc("-0.3307", "0.5121")], [mp.mpc("0.4419", "-0.6137"), mp.mpc("1.1931", "0.0723")]])
BV = {"a": [mp.mpc(0, 1), mp.mpc(0, -1)], "b": [mp.mpc(1), mp.mpc(-1)], "e": [mp.mpc(0), mp.inf]}


def pmul(A, B):
    C = [mp.mpc(0)] * (len(A) + len(B) - 1)
    for i, x in enumerate(A):
        if x == 0: continue
        for k, y in enumerate(B): C[i + k] += x * y
    return C


def padd(A, B, s=1):
    n = max(len(A), len(B)); A = A + [mp.mpc(0)] * (n - len(A)); B = B + [mp.mpc(0)] * (n - len(B))
    return [x + s * y for x, y in zip(A, B)]


def ppow(A, k):
    R = [mp.mpc(1)]
    for _ in range(k): R = pmul(R, A)
    return R


def subst(P, M):
    """P(z) = sum P_k z^k of formal degree n; z = (m00 w + m01)/(m10 w + m11); returns the numerator in w (degree n)"""
    n = len(P) - 1; L1 = [M[0, 1], M[0, 0]]; L2 = [M[1, 1], M[1, 0]]
    out = [mp.mpc(0)]
    for k, c in enumerate(P):
        out = padd(out, [c * t for t in pmul(ppow(L1, k), ppow(L2, n - k))])
    return out


def peval(A, w): return mp.polyval(list(reversed(A)), w)


def chord(z, w): return abs(z - w) / mp.sqrt((1 + abs(z) ** 2) * (1 + abs(w) ** 2))


def roots(A):
    nrm = max(abs(c) for c in A)
    deg = max(k for k in range(len(A)) if abs(A[k]) > nrm * mp.mpf(10) ** -45)
    return list(mp.polyroots(list(reversed(A[:deg + 1])), maxsteps=800, extraprec=800)), len(A) - 1 - deg


def clusters(rts, tol=1e-6):
    cl = []
    for r in rts:
        for c in cl:
            if chord(c[0], r) < tol: c.append(r); break
        else: cl.append([r])
    return [(sum(c) / len(c), len(c)) for c in cl]


def pder(A, k):
    for _ in range(k): A = [i * A[i] for i in range(1, len(A))]
    return A


def refine(N, w, m):
    """Newton on the (m-1)-th derivative of N, which has a simple zero at an m-fold zero of N"""
    D = pder(N, m - 1); D1 = pder(D, 1)
    for _ in range(40):
        d1 = peval(D1, w)
        if d1 == 0: break
        st = peval(D, w) / d1; w -= st
        if abs(st) < mp.mpf(10) ** -55: break
    return w


LABTOL = mp.mpf(10) ** -12      # a multiple zero of N is only known to ~1e-19 (map coefficients have 40 digits)
NEAR = [mp.mpf(0)]               # largest accepted distance to B (chordal), reported per configuration


def label(v):
    for l, vals in BV.items():
        for b in vals:
            d = (1 / mp.sqrt(1 + abs(v) ** 2) if b == mp.inf else chord(v, b)) if v != mp.inf else (0 if b == mp.inf else 1)
            if d < LABTOL:
                NEAR[0] = max(NEAR[0], d); return l
    return None


def local_deg(P, Q, w):
    """order of zero at w of P - beta Q (beta = value at w, in B), from root multiplicities"""
    v = peval(P, w) / peval(Q, w) if abs(peval(Q, w)) > mp.mpf(10) ** -25 * abs(peval(P, w)) else mp.inf
    l = label(v)
    if l is None: return None, None
    if v == mp.inf or abs(v) > mp.mpf(10) ** 6: F = Q; v = mp.inf
    else:
        b = min(BV[l], key=lambda x: mp.inf if x == mp.inf else abs(x - v)); F = padd(P, [b * c for c in Q], -1)
        if abs(b) < 1e-30: F = P
    rts, inf_ = roots(F)
    return l, sum(1 for r in rts if chord(r, w) < 1e-6)


_W = {}


def init(a, b):
    RA._rinit(a, b); _W.update(RA._R)


def work(rec):
    NEAR[0] = mp.mpf(0)
    a, b = _W["a"], len(_W["B_maps"][0][0]) - 1
    ia, ib, co = rec["ia"], rec["ib"], rec["co"]
    O1, Oq = _W["A_mp"][ia], _W["B_mp"][ib]
    X1 = [p for p, _ in O1]; Xq = [p for p, _ in Oq]
    T = RA.frame(*[Xq[c[1]] for c in co[:3]]) * mp.inverse(RA.frame(*[X1[c[0]] for c in co[:3]]))
    Ti = mp.inverse(T); nco = 0
    for x, _ in O1:
        for y, _ in Oq:
            v = Ti * mp.matrix([y[0], y[1]])
            nco += abs(x[0] * v[1] - x[1] * v[0]) < mp.mpf(10) ** -30 * mp.sqrt(abs(v[0]) ** 2 + abs(v[1]) ** 2)
    P1, Q1 = [mp.mpc(x) for x in _W["A_maps"][ia][0]], [mp.mpc(x) for x in _W["A_maps"][ia][1]]
    Pq, Qq = [mp.mpc(x) for x in _W["B_maps"][ib][0]], [mp.mpc(x) for x in _W["B_maps"][ib][1]]
    P1s, Q1s = subst(P1, SIG), subst(Q1, SIG)
    MT = T * SIG; P2s, Q2s = subst(Pq, MT), subst(Qq, MT)
    deg = 4 * (a + b)
    # N = (x^2 - y^2)(x^2 y^2 - 1) pulled back = product of the 4 Klein-graph factors (degree a+b each):
    #   y = x: P2 Q1 - P1 Q2,  y = -x: P2 Q1 + P1 Q2,  y = 1/x: P1 P2 - Q1 Q2,  y = -1/x: P1 P2 + Q1 Q2.
    # Each factor is well conditioned (degree a+b); a zero of N lies on exactly one graph unless it is matched.
    facs = [padd(pmul(P2s, Q1s), pmul(P1s, Q2s), -1), padd(pmul(P2s, Q1s), pmul(P1s, Q2s)),
            padd(pmul(P1s, P2s), pmul(Q1s, Q2s), -1), padd(pmul(P1s, P2s), pmul(Q1s, Q2s))]
    pts = []                                   # [point, total multiplicity, set of factors]
    at_inf = 0; sep = mp.mpf(1)
    for fi, Fc in enumerate(facs):
        rts, ai = roots(Fc); at_inf += ai
        cl = [(refine(Fc, w, m), m) for w, m in clusters(rts, 1e-10)]
        for i, (x, _) in enumerate(cl):
            for y, _ in cl[i + 1:]: sep = min(sep, chord(x, y))
        for w, m in cl:
            for q in pts:
                if chord(q[0], w) < 1e-10: q[1] += m; q[2].add(fi); break
            else: pts.append([w, m, {fi}])
    Jords = []; other = []; bad = 0
    for w, m, fs in pts:
        l1, e1 = local_deg(P1s, Q1s, w); l2, e2 = local_deg(P2s, Q2s, w)
        if l1 is not None and l1 == l2:
            Jords.append([e1, e2, m])
            if len(fs) != 2 or m < 2 * min(e1, e2) or (e1 != e2 and m != 2 * min(e1, e2)): bad += 1
        else:
            other.append(m)
            if len(fs) != 1: bad += 1
    Jords.sort()
    MK = sum(min(e1, e2) for e1, e2, _ in Jords)
    odd = sum(1 for *_, m in Jords if m % 2) + sum(1 for m in other if m % 2) + (at_inf % 2)
    return dict(ia=ia, ib=ib, jh=rec["exact"][1:], MK=MK, deficiency=deg - 2 * MK, odd=odd,
                g=(odd - 2) // 2 if odd else None, J=Jords, other=sorted(other), at_inf=at_inf,
                identity_ok=(sum(m for *_, m in Jords) + sum(other) + at_inf == deg), sep=float(sep), bad=bad, T_ok=(nco == len(co)), near_B=float(NEAR[0]))


if __name__ == "__main__":
    a, b, inp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 11
    recs = json.load(open(os.path.join(F02, inp)))
    out = os.path.join(HERE, "o3_" + inp.replace(".json", ".jsonl"))
    done = set()
    if os.path.exists(out):
        for line in open(out): r = json.loads(line); done.add(r["k"])
    todo = [k for k in range(len(recs)) if k not in done]
    print(f"{inp}: {len(recs)} records, {len(todo)} to do", flush=True)
    t0 = time.time()
    with Pool(workers, initializer=init, initargs=(a, b)) as pool, open(out, "a") as f:
        for n, (k, r) in enumerate(zip(todo, pool.imap(work, [recs[k] for k in todo], chunksize=20))):
            r["k"] = k; f.write(json.dumps(r) + chr(10)); f.flush()
            if n % 500 == 0: print(f"  {n}/{len(todo)} {time.time() - t0:.0f}s", flush=True)
    rows = [json.loads(l) for l in open(out)]
    summ = dict(input=inp, records=len(rows),
                identity_ok=all(r["identity_ok"] for r in rows), T_ok=all(r["T_ok"] for r in rows), bad=sum(r["bad"] for r in rows),
                min_sep=min(r["sep"] for r in rows), max_near_B=max(r["near_B"] for r in rows),
                M_ge_j=all(r["MK"] >= r["jh"][0] for r in rows),
                equality_delta_eq_odd=sum(1 for r in rows if
                             r["deficiency"] == r["odd"]),
                hist_jh_MK_def_g=sorted([list(k) + [v] for k, v in Counter(
                    (tuple(r["jh"]), r["MK"], r["deficiency"], r["g"]) for r in rows).items()], key=str))
    json.dump(summ, open(out.replace(".jsonl", "_summary.json"), "w"), indent=1)
    print(json.dumps(summ))
