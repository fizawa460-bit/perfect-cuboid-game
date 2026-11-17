"""F-03: coincidence counts c for elliptic-type (E) slack-0 pairs of degree 2^k, in mpmath.

Model (as in theory02/checks/t02_isogeny_chain.py, rewritten in mpmath):
  E': y^2 = x(x+1)(x+i), B' = {0, oo, -1, -i}; Phi = composition of k quotient 2-isogeny maps x -> x + a + b/x
  (a cyclic 2^k-isogeny E1 -> E', divided by +-1).  p = Phi (degree n = 2^k), with critical values in B'.
  O(p) = Phi^-1(1) u Phi^-1(i) u U  (U = the 4 two-torsion x-values of E1, one of them oo).
  q = k2 o Phi with k2(x) = -(x+i)/(x+1) (an involution of B' that is not a symmetry of B): the (H) pair.
  Coordinates on the source: z = mv(x) (a Moebius map that spreads U).
Pairs measured: (p_c, q_c') for chain choices c, c' (default: the (H) pair p_c vs k2 o p_c).

Search (exact, no floating-point prefilter):
  every ordered 4-tuple of O(p1) and of O(q) gets its cross ratio at dps 60; equal cross ratios (to 1e-40) give a
  candidate T (from the first 3 points); T is kept if it maps >= 4 points of O(p1) onto O(q) with chordal error
  < 1e-40, and every other pair is farther than 1e-15 (else the run reports a separation failure).
  Birationality of (p1, q o T): the fibre of p1 through two random points is computed exactly (preimages under the
  chain), and the number of fibre points with the same value of q o T is counted (1 = birational).
Precision: dps 60 by default; set the environment variable F03_DPS for more (the tag then ends in _dpsNN).
Resumable: per first index of the O(p1) 4-tuple, results are appended to f03_{tag}.jsonl; a restart skips the
  finished indices.
usage: python -I f03_isogeny_pairs.py steps [choice1] [choice2] [workers]
   e.g. python -I f03_isogeny_pairs.py 2           (degree 4, (H) pair, choice 00)
        python -I f03_isogeny_pairs.py 3 000 000   (degree 8)
"""
import itertools, json, os, sys, time
from collections import Counter
from multiprocessing import Pool
import mpmath as mp
mp.mp.dps = int(os.environ.get("F03_DPS", "60"))
HERE = os.path.dirname(os.path.abspath(__file__))
EPS = mp.mpf(10) ** -40
SEP = mp.mpf(10) ** -15
I = mp.mpc(0, 1)


def k2s(x):
    if x == mp.inf: return mp.mpc(-1)
    if abs(x + 1) < EPS: return mp.inf
    return (-x - I) / (x + 1)


def chain(steps, choice):
    roots = [mp.mpc(0), mp.mpc(-1), -I]; ker = mp.mpc(0)
    maps = []
    for st in range(steps):
        others = [r - ker for r in roots if abs(r - ker) > EPS]
        a = (others[0] + others[1]) / 2; b = ((others[0] - others[1]) / 4) ** 2
        maps.append((ker, a, b))
        disc = mp.sqrt(a * a - 4 * b); rp = (-a + disc) / 2; rm = (-a - disc) / 2
        roots = [mp.mpc(0), rp, rm]; ker = [rp, rm][int(choice[st]) if st < len(choice) else 0]
    return maps, roots


def pre(maps, vals):
    pts = list(vals)
    for ker, a, b in maps:
        new = []
        for X in pts:
            c = X - ker - a
            d = mp.sqrt(c * c - 4 * b); new += [(c + d) / 2, (c - d) / 2]
        pts = new
    return pts


def Phi(maps, x):
    for ker, a, b in reversed(maps):
        if x == mp.inf or abs(x) < EPS: return mp.inf if x == mp.inf else (mp.inf if abs(b) > EPS else ker + a)
        x = x + a + b / x + ker
    return x


class Model:
    def __init__(self, steps, choice):
        self.maps, top = chain(steps, choice)
        self.n = 2 ** steps
        U = list(top)
        self.u0, self.u1 = U[0], U[1]
        self.U = U + [mp.inf]
        self.A = pre(self.maps, [mp.mpc(1)]); self.Bp = pre(self.maps, [I])

    def mv(self, x):
        if x == mp.inf: return mp.mpc(0)
        den = 2 * x - self.u0 - self.u1
        return mp.inf if abs(den) < EPS else (self.u1 - self.u0) / den

    def mvinv(self, z):
        if z == mp.inf: return (self.u0 + self.u1) / 2
        if abs(z) < EPS: return mp.inf
        return ((self.u1 - self.u0) / z + self.u0 + self.u1) / 2

    def p(self, z): return Phi(self.maps, self.mvinv(z))


def lab(v):
    if v == mp.inf or abs(v) > 1 / EPS or abs(v) < EPS: return "e"
    if abs(v - 1) < 1e-30 or abs(v + 1) < 1e-30: return "b"
    if abs(v - I) < 1e-30 or abs(v + I) < 1e-30: return "a"
    return "?"


def oset(M, post):
    """O-points (source coordinate z) and labels of post o p (post = identity or k2, an involution):
    the unramified points over post^-1(1), post^-1(i), and U"""
    pts = []
    for x in pre(M.maps, [post(mp.mpc(1)), post(I)]) + M.U:
        v = Phi(M.maps, x); w = post(v)
        pts.append((M.mv(x), lab(w)))
    assert all(l != "?" for _, l in pts), "label"
    return pts


def chord(z, w):
    if z == mp.inf and w == mp.inf: return mp.mpf(0)
    if z == mp.inf: return 1 / mp.sqrt(1 + abs(w) ** 2)
    if w == mp.inf: return 1 / mp.sqrt(1 + abs(z) ** 2)
    return abs(z - w) / mp.sqrt((1 + abs(z) ** 2) * (1 + abs(w) ** 2))


def cr(a, b, c, d):
    def df(u, v):
        if u == mp.inf: return mp.mpc(1)
        if v == mp.inf: return mp.mpc(-1)
        return u - v
    num = df(a, c) * df(b, d); den = df(a, d) * df(b, c)
    return mp.inf if abs(den) < EPS * abs(num) else num / den


def ckey(v):
    if v == mp.inf: return ("inf",)
    if abs(v) > 1: w = 1 / v; f = 1
    else: w = v; f = 0
    return (f, int(mp.nint(mp.re(w) * 10 ** 35)), int(mp.nint(mp.im(w) * 10 ** 35)))


def mob3(src, dst):
    def to01inf(z1, z2, z3):
        if z1 == mp.inf: return (0, z2 - z3, 1, -z3)
        if z2 == mp.inf: return (1, -z1, 1, -z3)
        if z3 == mp.inf: return (1, -z1, 0, z2 - z1)
        return (z2 - z3, -z1 * (z2 - z3), z2 - z1, -z3 * (z2 - z1))
    A = to01inf(*src); B = to01inf(*dst)
    a, b, c, d = B; a1, b1, c1, d1 = (d, -b, -c, a); a2, b2, c2, d2 = A
    return (a1 * a2 + b1 * c2, a1 * b2 + b1 * d2, c1 * a2 + d1 * c2, c1 * b2 + d1 * d2)


def mob(T, z):
    a, b, c, d = T
    if z == mp.inf: return mp.inf if abs(c) < EPS * (abs(a) + abs(c)) else a / c
    den = c * z + d
    return mp.inf if abs(den) < EPS * (abs(a * z + b) + abs(den)) else (a * z + b) / den


W = {}


def winit(steps, c1, c2):
    M1 = Model(steps, c1); M2 = Model(steps, c2)
    W.update(M1=M1, M2=M2, O1=oset(M1, lambda v: v), O2=oset(M2, k2s))
    X2 = [p for p, _ in W["O2"]]
    H = {}
    for t in itertools.permutations(range(len(X2)), 4):
        H.setdefault(ckey(cr(*[X2[k] for k in t])), []).append(t)
    W["H"] = H


def birational(T):
    M1, M2 = W["M1"], W["M2"]
    out = []
    for z0 in (mp.mpc("0.3127", "0.7781"), mp.mpc("-1.137", "0.291")):
        v = M1.p(z0)
        fib = [M1.mv(x) for x in pre(M1.maps, [v])]
        q0 = k2s(M2.p(mob(T, z0)))
        out.append(sum(1 for w in fib if chord(k2s(M2.p(mob(T, w))), q0) < mp.mpf(10) ** -30))
    return max(out)


def job(i):
    O1, O2, H = W["O1"], W["O2"], W["H"]
    X1 = [p for p, _ in O1]; X2 = [p for p, _ in O2]
    found = {}; seen = set(); minfar = mp.mpf(1)
    for rest in itertools.permutations([k for k in range(len(X1)) if k != i], 3):
        t1 = (i,) + rest
        for t2 in H.get(ckey(cr(*[X1[k] for k in t1])), ()):
            if tuple(sorted(zip(t1, t2))) in seen: continue
            T = mob3([X1[k] for k in t1[:3]], [X2[k] for k in t2[:3]])
            co = []
            for a, x in enumerate(X1):
                y = mob(T, x)
                for b, w in enumerate(X2):
                    d = chord(y, w)
                    if d < EPS: co.append((a, b))
                    elif d < minfar: minfar = d
            if len(co) < 4: continue
            key = tuple(sorted(co))
            for s in itertools.combinations(key, 4): seen.add(s)
            if key in found: continue
            j = sum(1 for a, b in co if O1[a][1] == O2[b][1])
            found[key] = dict(c=len(co), j=j, h=len(co) - j, bir=birational(T))
    return i, [dict(co=list(k), **v) for k, v in found.items()], float(minfar)


if __name__ == "__main__":
    steps = int(sys.argv[1]); c1 = sys.argv[2] if len(sys.argv) > 2 else "0" * steps
    c2 = sys.argv[3] if len(sys.argv) > 3 else c1; workers = int(sys.argv[4]) if len(sys.argv) > 4 else 11
    tag = f"n{2 ** steps}_{c1}_{c2}" + ("" if mp.mp.dps == 60 else f"_dps{mp.mp.dps}")
    path = os.path.join(HERE, f"f03_{tag}.jsonl")
    done = {}
    if os.path.exists(path):
        for line in open(path):
            r = json.loads(line); done[r["i"]] = r
    winit(steps, c1, c2)
    n1 = len(W["O1"])
    print(f"degree {2 ** steps}, |O1| = {n1}, |O2| = {len(W['O2'])}, labels O1 {Counter(l for _, l in W['O1'])},"
          f" O2 {Counter(l for _, l in W['O2'])}; resumed {len(done)}/{n1}", flush=True)
    todo = [i for i in range(n1) if i not in done]
    t0 = time.time()
    if todo:
        with Pool(min(workers, len(todo)), initializer=winit, initargs=(steps, c1, c2)) as pool:
            for i, recs, mf in pool.imap_unordered(job, todo):
                r = dict(i=i, recs=recs, minfar=mf); done[i] = r
                with open(path, "a") as f: f.write(json.dumps(r) + chr(10))
                print(f"  index {i} done ({len(done)}/{n1}, {time.time() - t0:.0f}s)", flush=True)
    allT = {}
    for r in done.values():
        for rec in r["recs"]: allT[tuple(map(tuple, rec["co"]))] = rec
    minfar = min(r["minfar"] for r in done.values())
    hist = Counter((v["c"], v["j"], v["h"], v["bir"]) for v in allT.values())
    birc = [v for v in allT.values() if v["bir"] == 1]
    out = dict(tag=tag, degree=2 ** steps, T_with_c_ge_4=len(allT), min_noncoincident_chordal=minfar,
               separation_ok=minfar > float(SEP),
               max_c_birational=max((v["c"] for v in birc), default=None),
               max_M_birational=max((2 * v["j"] + v["h"] for v in birc), default=None),
               hist_c_j_h_bir=sorted([list(k) + [n] for k, n in hist.items()]))
    json.dump(out, open(os.path.join(HERE, f"f03_{tag}_summary.json"), "w"), indent=1)
    print(json.dumps(out))
