"""checks9 / census9.py -- mixed-type census of near-full coincidences of odd sets, degrees 1-4.

For slack-0 maps p (degree a) and q (degree b) and a Moebius map T, put q' := q o T and compare
O(p) with O(q') (points over B = {i, -i, 1, -1, 0, oo} with local degree 1; labels a = {+-i}, b = {+-1}, e = {0, oo}).
  j  = label-matched common points, h = label-differing common points,
  m1 = |O(p)| - j - h, m2 = |O(q')| - j - h, |Omega| = m1 + m2 + h.
Problem window: mixed type (m1, m2) != (0, 0) with |Omega| <= 4, i.e. (1,1) h<=2, (2,2) h=0, (1,3) h=0.

Search (complete for the problem window): T is fixed by 3 label-matched coincidences. If m1 + m2 + h <= 4 and m2 >= 1,
then m1 + h <= 3, so among the first 6 points of O(p) at least 3 are label-matched common points. Every 3-subset of the
first 6 points of O(p) is sent to every ordered label-matched triple of O(q); T with >= |O(p)| - 3 numerical
coincidences (double precision, chordal 1e-7) are re-checked with mpmath (dps 50, input data 40 digits, tolerance
1e-25; the gap to the nearest non-coincidence is reported). Records outside the window (e.g. type (0,0) with h >= 4,
or m1 = 3) are reported but are NOT claimed complete.

Per record: type, |Omega|, the monodromy order delta = |span of mu_v| and genus g = 1 - delta + delta|Omega|/4;
the degree of (p, q') onto its image (1 = birational); for type (0,0) whether q' = h o p with h an octahedral
rotation (Theorem U); for every record the Bezout count N_h = sum over common B-preimages c with q'(c) = h(p(c)) of
min(e_p(c), e_q'(c)), maximized over the 24 rotations h (if q' != h o p then N_h <= a + b); and the overlaps
crit(p) n crit(q'), crit(p) n O(q'), O(p) n crit(q') (critical points over B).

Maps: degree 1 and 2 are generated here (degree 1: a generic Moebius map; degree 2: M(z^2) for the 15 pairs of
critical values); degree 3, 4 are read from route-F/f02/maps3.json, maps4.json (F-02, 60 and 680 maps).
usage (from the repository root, numpy + mpmath):
  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks9/census9.py [--f02 DIR] [--bideg 3,4 ...]
Default bidegrees: 1,1 1,2 2,2 2,3 3,3 3,4; --bideg 4,4 for degree 4 (longer).
Cross-check of the earlier near.py numbers (degree 2, every coincidence pattern):
  ... census9.py --bideg 2,2 --first 8 --anylabel --keep 2
"""
import sys, os, json, itertools, argparse, time
sys.dont_write_bytecode = True
from collections import Counter, defaultdict
import numpy as np
import mpmath as mp

mp.mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
BV = [1j, -1j, 1, -1, 0, None]                 # None = oo
LAB = ["a", "a", "b", "b", "e", "e"]
TOL_NUM, TOL_MP = 1e-7, mp.mpf(10) ** -25


def chord(z, w):
    if z is None and w is None: return mp.mpf(0)
    if z is None: return 1 / mp.sqrt(1 + abs(w) ** 2)
    if w is None: return 1 / mp.sqrt(1 + abs(z) ** 2)
    return abs(z - w) / mp.sqrt((1 + abs(z) ** 2) * (1 + abs(w) ** 2))


def peval(c, z): return mp.polyval(list(reversed(c)), z)


def mval(P, Q, z):                             # value of P/Q at a finite z, None = oo
    q = peval(Q, z); p = peval(P, z)
    return None if abs(q) < mp.mpf(10) ** -40 * (1 + abs(p)) else p / q


class Map:
    """p = P/Q, coefficient lists low -> high (mpc). pre[k] = list of (point, multiplicity) over BV[k]."""
    def __init__(s, P, Q, name):
        s.P, s.Q, s.name = P, Q, name
        s.n = max(len(P), len(Q)) - 1
        s.pre = []
        for k, bv in enumerate(BV):
            F = list(Q) if bv is None else [P[i] - bv * Q[i] for i in range(len(P))]
            while len(F) > 1 and abs(F[-1]) < mp.mpf(10) ** -35: F.pop()
            minf = s.n - (len(F) - 1)
            assert minf in (0, 2), (name, "odd point at oo; normalise the source")
            r = mp.polyroots(list(reversed(F)), maxsteps=400, extraprec=200) if len(F) > 1 else []
            pts, used = ([(None, 2)] if minf == 2 else []), [False] * len(r)
            for i in range(len(r)):
                if used[i]: continue
                grp = [i] + [j for j in range(i + 1, len(r)) if not used[j] and abs(r[i] - r[j]) < 1e-12]
                for j in grp: used[j] = True
                z = sum(r[j] for j in grp) / len(grp)
                if len(grp) == 2:                # refine a double root by Newton on F'
                    dF = [i * F[i] for i in range(1, len(F))]
                    for _ in range(60): z = z - peval(dF, z) / peval([i * dF[i] for i in range(1, len(dF))], z)
                pts.append((z, len(grp)))
            assert all(m <= 2 for _, m in pts), (name, "local degree > 2: not slack 0")
            s.pre.append(pts)
        s.O = [(z, k) for k in range(6) for z, m in s.pre[k] if m == 1]
        s.crit = [(z, k) for k in range(6) for z, m in s.pre[k] if m == 2]
        assert len(s.O) == 2 * s.n + 4 and len(s.crit) == 2 * s.n - 2, (name, len(s.O), len(s.crit))
        s.Onp = np.array([complex(z) for z, _ in s.O]); s.Lnp = np.array([LAB[k] for _, k in s.O])

    def __call__(s, z): return mval(s.P, s.Q, z)


def load_maps(deg, f02):
    if deg == 1:                                # generic Moebius map, B-preimages finite
        a, b, c, d = mp.mpc(0.7, 0.2), mp.mpc(0.3, -0.1), mp.mpc(0.2, -0.5), mp.mpc(1.1, 0.4)
        return [Map([b, a], [d, c], "deg1")]
    if deg == 2:                                # M(z^2), M(0) = b1, M(oo) = b2, M(1) = generic c3
        out = []; c3 = mp.mpc(0.31, 0.77)
        for i1, i2 in itertools.combinations(range(6), 2):
            b1, b2 = BV[i1], BV[i2]
            # M(w) = (A w + Bc) / (C w + D) with M(0) = b1, M(oo) = b2, M(1) = c3
            if b2 is None: A, Bc, C, D = c3 - b1, b1, 0, 1
            elif b1 is None: A, Bc, C, D = b2, (c3 - b2), 1, 0
            else: A, Bc, C, D = b2 * (c3 - b1), b1 * (b2 - c3), (c3 - b1), (b2 - c3)
            P = [mp.mpc(Bc), 0, mp.mpc(A)]; Q = [mp.mpc(D), 0, mp.mpc(C)]
            out.append(Map(P, Q, "deg2_%d%d" % (i1, i2)))
        return out
    d = json.load(open(os.path.join(f02, "maps%d.json" % deg)))
    cv = lambda s: mp.mpc(*[mp.mpf(x) for x in _split(s)])
    return [Map([cv(c) for c in m["P"]], [cv(c) for c in m["Q"]], "deg%d_%04d" % (deg, i)) for i, m in enumerate(d)]


def _split(s):
    """'(x + yj)' or '(x - yj)' or 'x' -> (x, y) strings, keeping all digits."""
    s = s.strip().strip("()").replace(" ", "")
    if not s.endswith("j"): return (s, "0")
    s = s[:-1]
    for i in range(len(s) - 1, 0, -1):
        if s[i] in "+-" and s[i - 1] not in "eE": return (s[:i], s[i:])
    return ("0", s)


def mob_from_triples(z, w):
    """2x2 matrix (mp) of the Moebius map with z_k -> w_k (finite points)."""
    z1, z2, z3 = z; w1, w2, w3 = w
    Mz = mp.matrix([[z2 - z3, -z1 * (z2 - z3)], [z2 - z1, -z3 * (z2 - z1)]])
    Mw = mp.matrix([[w2 - w3, -w1 * (w2 - w3)], [w2 - w1, -w3 * (w2 - w1)]])
    return mp.inverse(Mw) * Mz


def mob(M, z):
    if z is None: return None if abs(M[1, 0]) < mp.mpf(10) ** -40 else M[0, 0] / M[1, 0]
    den = M[1, 0] * z + M[1, 1]
    return None if abs(den) < mp.mpf(10) ** -40 else (M[0, 0] * z + M[0, 1]) / den


# octahedral rotations as permutations of BV
def _rot_perms():
    def act(f):
        return tuple(min(range(6), key=lambda k: float(chord(f(BV[i]), BV[k]))) for i in range(6))
    def r1(z): return None if z is None else 1j * z
    def r2(z):
        if z is None: return mp.mpf(-1)
        return None if abs(1 - z) < 1e-30 else (1 + z) / (1 - z)
    gens = [act(r1), act(r2)]; G = {tuple(range(6))}; fr = list(G)
    while fr:
        nf = []
        for g in fr:
            for s in gens:
                c = tuple(s[g[i]] for i in range(6))
                if c not in G: G.add(c); nf.append(c)
        fr = nf
    return sorted(G)
ROT = _rot_perms(); assert len(ROT) == 24


def mu_span(vecs):
    span = {0}
    for v in vecs:
        span |= {x ^ v for x in span}
    return len(span)


def analyse(p, q, M):
    """full mp analysis of the pair (p, q o T), T = M."""
    TO = [(mob(M, z), k) for z, k in p.O]
    used = set(); j = h = 0; gap = mp.mpf(1); worst = mp.mpf(0); mus = []; matched_p = set()
    for i, (w, k) in enumerate(TO):
        dist = [(chord(w, u), jj) for jj, (u, kk) in enumerate(q.O)]
        dmin, jj = min(dist)
        if dmin < TOL_MP:
            worst = max(worst, dmin); used.add(jj); matched_p.add(i)
            k2 = q.O[jj][1]
            if LAB[k] == LAB[k2]: j += 1
            else:
                h += 1; mus.append((1 << "abe".index(LAB[k])) ^ (1 << "abe".index(LAB[k2])))
        else:
            gap = min(gap, dmin); mus.append(1 << "abe".index(LAB[k]))
    for jj, (u, k2) in enumerate(q.O):
        if jj not in used: mus.append(1 << "abe".index(LAB[k2]))
    m1, m2 = len(p.O) - j - h, len(q.O) - j - h
    omega = m1 + m2 + h
    delta = mu_span(mus)
    genus = 1 - delta + mp.mpf(delta * omega) / 4
    # common B-preimages with multiplicities, for Bezout counts and critical overlaps
    Tpre = [(mob(M, z), k, m) for k in range(6) for z, m in p.pre[k]]
    qpre = [(u, k, m) for k in range(6) for u, m in q.pre[k]]
    pairs = []
    for w, k, m in Tpre:
        for u, k2, m2_ in qpre:
            if chord(w, u) < TOL_MP: pairs.append((k, m, k2, m2_))
    NH = max(sum(min(m, m2_) for k, m, k2, m2_ in pairs if r[k] == k2) for r in ROT)
    cc = sum(1 for k, m, k2, m2_ in pairs if m == 2 and m2_ == 2)
    co = sum(1 for k, m, k2, m2_ in pairs if m == 2 and m2_ == 1)
    oc = sum(1 for k, m, k2, m2_ in pairs if m == 1 and m2_ == 2)
    # degree of (p, q o T) onto the image
    t0 = mp.mpc(0.123, 0.456); v0 = p(t0); w0 = q(mob(M, t0))
    F = [p.P[i] - v0 * p.Q[i] for i in range(len(p.P))]
    while len(F) > 1 and abs(F[-1]) < mp.mpf(10) ** -35: F.pop()
    fib = mp.polyroots(list(reversed(F)), maxsteps=400, extraprec=200)
    bdeg = sum(1 for t in fib if chord(q(mob(M, t)), w0) < mp.mpf(10) ** -20)
    # Theorem U check for type (0,0): q o T = h o p with h preserving B
    thmU = None
    if m1 == 0 and m2 == 0 and p.n == q.n:
        ts = [mp.mpc(0.21, 0.13), mp.mpc(-0.4, 0.6), mp.mpc(0.9, -0.35)]
        Hm = mob_from_triples([p(t) for t in ts], [q(mob(M, t)) for t in ts])
        ok = all(chord(q(mob(M, t)), mob(Hm, p(t))) < mp.mpf(10) ** -20 for t in
                 [mp.mpc(0.55, 0.05), mp.mpc(-0.15, -0.8), mp.mpc(1.3, 0.7)])
        okB = all(min(chord(mob(Hm, b), b2) for b2 in BV) < mp.mpf(10) ** -20 for b in BV)
        thmU = bool(ok and okB)
    return dict(m1=m1, m2=m2, h=h, j=j, omega=omega, delta=delta, genus=int(genus), bdeg=bdeg, NH=NH,
                cc=cc, co=co, oc=oc, thmU=thmU, worst=float(worst), gap=float(gap), M=M, p=p, q=q)


def search(P, Qs, a, b, first=6, anylabel=False, keep=3):
    recs = {}
    k1 = len(P[0].O) if P else 0
    for p in P:
        trip = list(itertools.combinations(range(min(first, len(p.O))), 3))
        for q in Qs:
            byl = defaultdict(list)
            for jj, l in enumerate(q.Lnp): byl[l].append(jj)
            Z, W, src = [], [], []
            for t in trip:
                ls = [p.Lnp[i] for i in t]
                pools = [range(len(q.O))] * 3 if anylabel else [byl[l] for l in ls]
                for tgt in itertools.product(*pools):
                    if len(set(tgt)) < 3: continue
                    Z.append([p.Onp[i] for i in t]); W.append([q.Onp[jj] for jj in tgt]); src.append((t, tgt))
            if not Z: continue
            Z = np.array(Z); W = np.array(W)
            z1, z2, z3 = Z[:, 0:1], Z[:, 1:2], Z[:, 2:3]; w1, w2, w3 = W[:, 0:1], W[:, 1:2], W[:, 2:3]
            x = p.Onp[None, :]
            cn = (x - z1) * (z2 - z3); cd = (x - z3) * (z2 - z1)
            with np.errstate(all="ignore"):
                w = (cn * w3 * (w2 - w1) - cd * w1 * (w2 - w3)) / (cn * (w2 - w1) - cd * (w2 - w3))
                u = q.Onp[None, None, :]
                dd = np.abs(w[:, :, None] - u) / np.sqrt((1 + np.abs(w[:, :, None]) ** 2) * (1 + np.abs(u) ** 2))
            dd = np.nan_to_num(dd, nan=1.0)
            cnt = (dd.min(axis=2) < TOL_NUM).sum(axis=1)
            for idx in np.nonzero(cnt >= k1 - keep)[0]:
                t, tgt = src[idx]
                M = mob_from_triples([p.O[i][0] for i in t], [q.O[jj][0] for jj in tgt])
                nm = M / max(abs(M[r, c]) for r in range(2) for c in range(2))
                ph = nm[0, 0] / abs(nm[0, 0]) if abs(nm[0, 0]) > 1e-3 else nm[0, 1] / abs(nm[0, 1])
                nm = nm / ph
                key = (p.name, q.name) + tuple((round(float(nm[r, c].real), 6) + 0.0, round(float(nm[r, c].imag), 6) + 0.0)
                                               for r in range(2) for c in range(2))
                if key not in recs: recs[key] = analyse(p, q, M)
    return list(recs.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--f02", default=os.path.join(HERE, "..", "..", "f02"))
    ap.add_argument("--bideg", nargs="*", default=["1,1", "1,2", "2,2", "2,3", "3,3", "3,4"])
    ap.add_argument("--first", type=int, default=6, help="use 3-subsets of the first FIRST odd points of p")
    ap.add_argument("--anylabel", action="store_true", help="targets of any label (cross-check of r7/near.py)")
    ap.add_argument("--keep", type=int, default=3, help="keep T with >= |O(p)| - KEEP coincidences")
    args = ap.parse_args()
    cache = {}
    def maps(d):
        if d not in cache: cache[d] = load_maps(d, args.f02)
        return cache[d]
    out = []; allok = True
    for bd in args.bideg:
        a, b = map(int, bd.split(",")); t0 = time.time()
        P, Qs = maps(a), maps(b)
        recs = search(P, Qs, a, b, args.first, args.anylabel, args.keep)
        cnt = Counter((r["m1"], r["m2"], r["h"], r["omega"], r["delta"], r["genus"], r["bdeg"]) for r in recs)
        window = [r for r in recs if (r["m1"], r["m2"]) != (0, 0) and r["omega"] <= 4]
        mixed = [r for r in recs if (r["m1"], r["m2"]) != (0, 0)]
        u = [r["thmU"] for r in recs if r["thmU"] is not None]
        bez = all(r["NH"] <= a + b for r in mixed)
        # composite lemma: if (p, q') has degree d onto its image, d divides m1 and m2
        comp = all(r["m1"] % r["bdeg"] == 0 and r["m2"] % r["bdeg"] == 0 for r in recs)
        allok &= bez and all(u) and comp
        mixed_omega = sorted({r["omega"] for r in mixed})
        out.append(dict(
            bidegree=[a, b], maps=[len(P), len(Qs)], search=dict(first=args.first, anylabel=args.anylabel, keep=args.keep),
            distinct_T=len(recs),
            key="(m1, m2, h, |Omega|, delta, genus, degree onto image)",
            counts=sorted([list(k) + [v] for k, v in cnt.items()]),
            problem_window_mixed=len(window),
            mixed_records_min_omega=(mixed_omega[0] if mixed_omega else None),
            typeU_records=len(u), typeU_all_octahedral=all(u),
            bezout_NH_le_a_plus_b_on_mixed=bez, composite_degree_divides_m1_m2=comp,
            max_NH_mixed=max([r["NH"] for r in mixed], default=None),
            crit_overlaps_mixed=dict(crit_crit=sum(r["cc"] for r in mixed), crit_O=sum(r["co"] for r in mixed),
                                     O_crit=sum(r["oc"] for r in mixed)),
            worst_coincidence=max([r["worst"] for r in recs], default=0.0),
            smallest_gap=min([r["gap"] for r in recs], default=1.0),
            seconds=round(time.time() - t0, 1)))
        print(json.dumps(out[-1]), flush=True)
    print("PASS" if allok else "FAIL")


if __name__ == "__main__":
    main()
