"""checks10 / tau10.py -- the pulled-back octahedral triangulation tau_p, and how "clusters" look in the data.

tau_p: vertices p^{-1}(B), edges = lifts of the 12 edges of the octahedron (b, b' not antipodal). Two cone points
(odd points) of X_p are at distance l_min iff they are joined by an edge of tau_p (radius10.py, Part A). Edges are
found by continuing the n roots of p(z) = gamma(t) along each octahedron edge gamma (numpy, 600 steps, ends matched
to the B-preimages computed with mpmath; a generic Moebius change of the source keeps everything finite).

Part 1 (step 1 of the plan: are the cone points on clusters at all?): for every slack-0 map of degree 1-4
  (census9 maps), for L_n (degree 2^n, n <= 5, E14 sec. 6) and for composites p0 o kappa (degree 8), count the cone
  points with NO cone neighbour in tau_p ("isolated": they can lie on no edge of any cluster, whatever the radius),
  the cone-cone edges, and the components of the cone graph. Checks the Euler counts (8n faces, 12n edges, and
  sum over faces of cone vertices = 8n + 16).
Part 2 (step 2: do neighbouring pieces carry one rotation?): for every mixed record of census9 at degrees
  (1,1), (1,2), (2,2): pseudo-edges = pairs of anchors adjacent in tau_p AND in tau_q' (necessary for an edge of a
  cluster); each determines the unique rotation sigma with (p(c1), p(c2)) -> (q'(c1), q'(c2)); report the components,
  whether sigma is constant on each, the number of rotation classes, and the largest set of anchors with
  q'(c) = sigma(p(c)) for one sigma (Corollary R: <= a + b).
  At these degrees no anchor is R-deep for any R used in checks10 (the whole orbifold has diameter < R), so these are
  NOT E13 clusters; they show what the combinatorics alone allows.
usage (from the repository root):  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks10/tau10.py
"""
import sys, os, itertools, importlib.util, io, contextlib, json
sys.dont_write_bytecode = True
from collections import Counter, defaultdict
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("census9", os.path.join(HERE, "..", "checks9", "census9.py"))
C9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C9)
mp.mp.dps = 40
BV, LAB, chord, mob = C9.BV, C9.LAB, C9.chord, C9.mob
ANTI = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
EDGES = [(i, j) for i in range(6) for j in range(i + 1, 6) if ANTI[i] != j]
assert len(EDGES) == 12
ok = True


def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def pmul(a, b):
    r = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def ppow(a, k):
    r = [mp.mpc(1)]
    for _ in range(k): r = pmul(r, a)
    return r
def compose_mob(P, Q, M, n):
    """(P/Q) o M, M = [[a, b], [c, d]] acting z -> (az + b)/(cz + d); formal degree n."""
    A = [mp.mpc(M[0][1]), mp.mpc(M[0][0])]; Bp = [mp.mpc(M[1][1]), mp.mpc(M[1][0])]
    num = [mp.mpc(0)]; den = [mp.mpc(0)]
    for k in range(n + 1):
        t = pmul(ppow(A, k), ppow(Bp, n - k))
        if k < len(P): num = padd(num, [P[k] * x for x in t])
        if k < len(Q): den = padd(den, [Q[k] * x for x in t])
    return num, den
def compose(P, Q, A, Bp, n):
    num = [mp.mpc(0)]; den = [mp.mpc(0)]
    for k in range(n + 1):
        t = pmul(ppow(A, k), ppow(Bp, n - k))
        if k < len(P): num = padd(num, [P[k] * x for x in t])
        if k < len(Q): den = padd(den, [Q[k] * x for x in t])
    return num, den
GEN = [[mp.mpc(0.83, 0.21), mp.mpc(0.37, -0.52)], [mp.mpc(-0.29, 0.44), mp.mpc(1.07, 0.13)]]


def gamma(i, j, t):
    """point at parameter t on the octahedron edge from BV[i] to BV[j]; returns (value, reciprocal?)"""
    bi, bj = BV[i], BV[j]
    if bi == 0: return bj * t, False
    if bj == 0: return bi * (1 - t), False
    if bj is None: return (1 - t) / bi, True              # 1/w from 1/bi to 0
    if bi is None: return t / bj, True
    th = np.angle(complex(bj) / complex(bi))
    return complex(bi) * np.exp(1j * th * t), False


def tau(P, Q):
    """P, Q (mp, formal degree n) with all B-preimages finite. Returns Map and the list of arcs (u, v)."""
    m = C9.Map(P, Q, "tau")
    n = m.n
    verts = [(z, k, mult) for k in range(6) for z, mult in m.pre[k]]
    assert all(z is not None for z, _, _ in verts)
    Pc = np.array([complex(c) for c in P]); Qc = np.array([complex(c) for c in Q])
    arcs = []
    ts = np.concatenate([[1e-9, 1e-7, 1e-5, 1e-4, 1e-3], np.linspace(0.002, 0.998, 600), [1 - 1e-3, 1 - 1e-4, 1 - 1e-5, 1 - 1e-7, 1 - 1e-9]])
    def roots_at(i, j, t):
        w, rec = gamma(i, j, t)
        F = (Qc - w * Pc) if rec else (Pc - w * Qc)
        return np.roots(F[::-1])
    def nearest_vertex(z, k):
        cand = [(abs(z - complex(v[0])), idx) for idx, v in enumerate(verts) if v[1] == k]
        return min(cand)[1]
    for i, j in EDGES:
        r = roots_at(i, j, ts[0]); assert len(r) == n
        start = [nearest_vertex(z, i) for z in r]
        cur = r
        for t in ts[1:]:
            nr = roots_at(i, j, t)
            # match by nearest (greedy on the distance matrix)
            D = np.abs(cur[:, None] - nr[None, :]); perm = [-1] * n; used = set()
            for a, b in sorted(((a, b) for a in range(n) for b in range(n)), key=lambda ab: D[ab]):
                if perm[a] == -1 and b not in used: perm[a] = b; used.add(b)
            cur = nr[perm]
        end = [nearest_vertex(z, j) for z in cur]
        arcs += list(zip(start, end))
    # consistency: every vertex of local degree e meets e arcs of each of its 4 edges
    deg = Counter();
    for u, v in arcs: deg[u] += 1; deg[v] += 1
    good = all(deg[idx] == 4 * mult for idx, (z, k, mult) in enumerate(verts))
    return m, verts, arcs, good


def cone_stats(verts, arcs):
    cone = {i for i, v in enumerate(verts) if v[2] == 1}
    nb = defaultdict(set)
    for u, v in arcs:
        if u in cone and v in cone: nb[u].add(v); nb[v].add(u)
    iso = sum(1 for c in cone if not nb[c])
    cc = sum(1 for u, v in arcs if u in cone and v in cone)
    comp, seen = [], set()
    for c in cone:
        if c in seen: continue
        st, cs = [c], 0
        seen.add(c)
        while st:
            x = st.pop(); cs += 1
            for y in nb[x]:
                if y not in seen: seen.add(y); st.append(y)
        comp.append(cs)
    return len(cone), iso, cc, sorted(comp, reverse=True)


def with_generic_source(P, Q, n):
    return compose_mob(P, Q, GEN, n)


# ---------------- Part 1 ----------------
print("Part 1: cone points of X_p and their tau_p-neighbours")
with contextlib.redirect_stdout(io.StringIO()):
    MAPS = {d: C9.load_maps(d, os.path.join(HERE, "..", "..", "f02")) for d in (1, 2, 3, 4)}
summary = {}
def run_family(name, items):
    global ok
    agg = Counter(); worst_iso = 0; frac = []; allgood = True; comps = Counter()
    for P, Q, n in items:
        PP, QQ = with_generic_source(P, Q, n)
        m, verts, arcs, good = tau(PP, QQ)
        allgood &= good and len(arcs) == 12 * n
        nc, iso, cc, comp = cone_stats(verts, arcs)
        agg["maps"] += 1; agg["cone"] += nc; agg["iso"] += iso; agg["cc"] += cc
        frac.append(iso / nc); comps[comp[0]] += 1
    print("  %-28s maps %4d  cone points %6d  isolated %5d (%.1f%%; max per map %.0f%%)  cone-cone edges %5d  arc counts ok %s"
          % (name, agg["maps"], agg["cone"], agg["iso"], 100 * agg["iso"] / agg["cone"], 100 * max(frac), agg["cc"], allgood))
    summary[name] = dict(maps=agg["maps"], cone=agg["cone"], isolated=agg["iso"], cc_edges=agg["cc"],
                         max_isolated_fraction=max(frac), largest_component_hist=dict(comps), arcs_ok=allgood)
    ok &= allgood
for d in (1, 2, 3, 4):
    run_family("degree %d (all census9 maps)" % d, [(m.P, m.Q, m.n) for m in MAPS[d]])
LP, LQ = [mp.mpc(-1), 0, mp.mpc(1)], [mp.mpc(0), mp.mpc(0, 2)]
Ln = []; P, Q = [mp.mpc(0), mp.mpc(1)], [mp.mpc(1), mp.mpc(0)]
for k in range(1, 6):
    P, Q = compose(LP, LQ, P, Q, 2) if k > 1 else (LP, LQ)
    Ln.append((list(P) + [mp.mpc(0)] * (2 ** k + 1 - len(P)), list(Q) + [mp.mpc(0)] * (2 ** k + 1 - len(Q)), 2 ** k))
run_family("L_n, n = 1..5 (degree 2^n)", Ln)
# composites p0 o kappa, kappa a double cover branched at two odd points of p0 (degree 8 from degree 4)
comp_items = []
for m0 in MAPS[4][::40]:
    c1, c2 = m0.O[0][0], m0.O[5][0]
    A, Bp = [mp.mpc(c1), 0, -mp.mpc(c2)], [mp.mpc(1), 0, mp.mpc(-1)]
    P, Q = compose(m0.P, m0.Q, A, Bp, 4)
    comp_items.append((P, Q, 8))
run_family("p0 o kappa (degree 8)", comp_items)


# ---------------- Part 2 ----------------
print("Part 2: pseudo-clusters of the mixed census9 records (anchors adjacent in tau_p and in tau_q')")
def rot_of_edge(k1, k2, l1, l2):
    """the unique rotation (as a permutation of BV) with k1 -> l1, k2 -> l2 (adjacent pairs)"""
    rs = [r for r in C9.ROT if r[k1] == l1 and r[k2] == l2]
    assert len(rs) == 1
    return rs[0]
part2 = []
for a, b in ((1, 1), (1, 2), (2, 2)):
    with contextlib.redirect_stdout(io.StringIO()):
        recs = C9.search(MAPS[a], MAPS[b], a, b)
    mixed = [r for r in recs if (r["m1"], r["m2"]) != (0, 0)]
    stats = Counter(); cls_hist = Counter(); best_hist = Counter(); const_all = True; nrec = 0
    for r in mixed[:: max(1, len(mixed) // 60)]:
        p, q, M = r["p"], r["q"], r["M"]
        Mi = mp.inverse(M)
        P1, Q1 = compose(p.P, p.Q, [Mi[0, 1], Mi[0, 0]], [Mi[1, 1], Mi[1, 0]], p.n)
        P1 += [mp.mpc(0)] * (p.n + 1 - len(P1)); Q1 += [mp.mpc(0)] * (p.n + 1 - len(Q1))
        PP, QQ = with_generic_source(P1, Q1, p.n); PQ, QQq = with_generic_source(list(q.P), list(q.Q), q.n)
        mA, vA, aA, gA = tau(PP, QQ); mB, vB, aB, gB = tau(PQ, QQq)
        ok &= gA and gB
        # anchors: odd points of both, matched by position
        anc = []
        for ia, (z, k, e) in enumerate(vA):
            if e != 1: continue
            for ib, (u, k2, e2) in enumerate(vB):
                if e2 == 1 and chord(z, u) < mp.mpf(10) ** -20: anc.append((ia, ib, k, k2))
        idxA = {x[0]: t for t, x in enumerate(anc)}; idxB = {x[1]: t for t, x in enumerate(anc)}
        eA = {frozenset((idxA[u], idxA[v])) for u, v in aA if u in idxA and v in idxA}
        eB = {frozenset((idxB[u], idxB[v])) for u, v in aB if u in idxB and v in idxB}
        pe = [tuple(sorted(e)) for e in eA & eB]
        nb = defaultdict(list)
        for s, t in pe:
            r_ = rot_of_edge(anc[s][2], anc[t][2], anc[s][3], anc[t][3])
            nb[s].append((t, r_)); nb[t].append((s, r_))
        seen = set(); classes = set(); const = True; ncomp = 0
        for s in range(len(anc)):
            if s in seen or not nb[s]: continue
            ncomp += 1; st = [s]; seen.add(s); rots = set()
            while st:
                x = st.pop()
                for y, r_ in nb[x]:
                    rots.add(r_)
                    if y not in seen: seen.add(y); st.append(y)
            const &= len(rots) == 1; classes |= rots
        best = max(sum(1 for (_, _, k, k2) in anc if rr[k] == k2) for rr in C9.ROT)
        nrec += 1; stats["anchors"] += len(anc); stats["pseudo_edges"] += len(pe); stats["components"] += ncomp
        cls_hist[len(classes)] += 1; best_hist[best] += 1; const_all &= const
    line = dict(bidegree=[a, b], records_examined=nrec, mixed_records=len(mixed), anchors=stats["anchors"],
                pseudo_edges=stats["pseudo_edges"], components=stats["components"],
                sigma_constant_on_every_component=const_all, rotation_classes_histogram=dict(cls_hist),
                largest_single_sigma_anchor_set_histogram=dict(best_hist), a_plus_b=a + b)
    print("  " + json.dumps(line)); part2.append(line)
    ok &= all(k <= a + b for k in best_hist)
json.dump(dict(part1=summary, part2=part2), open(os.path.join(HERE, "tau10.json"), "w"), indent=1)
print("PASS" if ok else "FAIL")
