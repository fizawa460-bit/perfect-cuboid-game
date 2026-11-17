"""checks12 / bands12.py -- request 11, candidate 3: do cone-free bands occur in the data, and how wide are they?

For a slack-0 map p: tau_p has 8n triangles; T0 = triangles without cone vertex.  Dual graph: two triangles are adjacent
when they share an edge (found by continuing the n preimages of a face centre across the midpoint of each side).
Per map:
  comp   = number of components of the cone-bearing triangles (dual graph restricted to triangles with a cone vertex);
  compG  = number of components of the graph on the cone points with edges "adjacent" or "2h-linked" (iso11);
           Lemma G of ANSWER-10 says comp = compG   (checked here on data for the first time);
  T0     = number of T0 triangles, regions = components of the T0 triangles, largest region;
  depth  = max over T0 triangles of the dual distance to the nearest cone-bearing triangle (1 = touches one);
  cross  = if comp >= 2: the largest, over the components C other than the biggest one, of the least number of T0
           triangles on a dual path from C to the biggest component ("width of the band in triangles").
usage (from the repository root):
  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks12/bands12.py [stride for degree 4, default 4]
"""
import sys, os, io, contextlib, json
sys.dont_write_bytecode = True
from collections import Counter, defaultdict, deque
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
I11 = os.path.join(HERE, "..", "checks11")
src = open(os.path.join(I11, "iso11.py"), encoding="utf-8").read().split("\nstride = ")[0]
G = {"__name__": "iso11_defs", "__file__": os.path.join(I11, "iso11.py")}
exec(compile(src, "iso11_defs", "exec"), G)
C9, tau, compose, with_generic_source, ANTI = G["C9"], G["tau"], G["compose"], G["with_generic_source"], G["ANTI"]
FACES, SPH, faces_of = G["FACES"], G["SPH"], G["faces_of"]
ok = True
TS2 = np.linspace(0.0, 1.0, 241)


def dual_edges(P, Q, n):
    """pairs (triangle id, triangle id) sharing an edge; triangle id = face index * n + index of the root at the centre."""
    Pc = np.array([complex(c) for c in P]); Qc = np.array([complex(c) for c in Q])
    def roots_at(v):
        x, y, z = v / np.linalg.norm(v)
        if z < 0:
            w = (x + 1j * y) / (1 - z); F = Pc - w * Qc
        else:
            w = (x - 1j * y) / (1 + z); F = Qc - w * Pc
        return np.roots(F[::-1])
    cen = [(SPH[f[0]] + SPH[f[1]] + SPH[f[2]]) / 3.0 for f in FACES]
    out = []
    for fi, f in enumerate(FACES):
        for gi in range(fi + 1, 8):
            g = FACES[gi]; sh = set(f) & set(g)
            if len(sh) != 2: continue
            a_, b_ = sorted(sh); mid = (SPH[a_] + SPH[b_]) / 2.0
            ts = TS2
            path = [(1 - t) * cen[fi] + t * mid for t in ts] + [(1 - t) * mid + t * cen[gi] for t in ts[1:]]
            cur = roots_at(path[0]); start = cur.copy()
            idx = np.arange(n)
            for v in path[1:]:
                nr = roots_at(v)
                D = np.abs(cur[:, None] - nr[None, :]); perm = [-1] * n; used = set()
                for a, b in sorted(((a, b) for a in range(n) for b in range(n)), key=lambda ab: D[ab]):
                    if perm[a] == -1 and b not in used: perm[a] = b; used.add(b)
                cur = nr[perm]
            end0 = roots_at(cen[gi])
            for a in range(n):
                b = int(np.argmin(np.abs(end0 - cur[a])))
                out.append((fi * n + a, gi * n + b))
    return out


def comps(nodes, adj):
    seen, res = set(), []
    for s in nodes:
        if s in seen: continue
        st, cc = [s], []; seen.add(s)
        while st:
            x = st.pop(); cc.append(x)
            for y in adj[x]:
                if y in nodes and y not in seen: seen.add(y); st.append(y)
        res.append(cc)
    return res


def analyse(P, Q, n):
    PP, QQ = with_generic_source(P, Q, n)
    m, verts, arcs, good = tau(PP, QQ)
    tris = faces_of(PP, QQ, verts, n)
    de = dual_edges(PP, QQ, n)
    adj = defaultdict(set)
    for a, b in de: adj[a].add(b); adj[b].add(a)
    good = bool(good) and len(tris) == 8 * n and all(len(adj[t]) == 3 for t in range(8 * n))
    # a shared edge means two common vertices
    good &= all(len(set(tris[a]) & set(tris[b])) >= 2 for a, b in de)
    cone = {i for i, v in enumerate(verts) if v[2] == 1}
    k = [sum(1 for v in t if v in cone) for t in tris]
    T0 = {t for t in range(8 * n) if k[t] == 0}; CB = set(range(8 * n)) - T0
    cb = comps(CB, adj); regs = comps(T0, adj)
    # graph on cone points (iso11): adjacency or 2h-link
    nb = defaultdict(set)
    for u, v in arcs: nb[u].add(v); nb[v].add(u)
    lab = {i: verts[i][1] for i in range(len(verts))}
    gadj = defaultdict(set)
    for c in cone: gadj[c] |= (nb[c] & cone)
    for v in range(len(verts)):
        cs = [c for c in nb[v] if c in cone]
        for c in cs:
            for c2 in cs:
                if c2 != c and lab[c2] == ANTI[lab[c]]: gadj[c].add(c2)
    cg = comps(cone, gadj)
    # depth of T0 triangles
    dist = {t: 0 for t in CB}; dq = deque(CB)
    while dq:
        x = dq.popleft()
        for y in adj[x]:
            if y not in dist: dist[y] = dist[x] + 1; dq.append(y)
    depth = max([dist[t] for t in T0], default=0)
    cross = 0
    if len(cb) >= 2:
        big = max(cb, key=len); cost = {t: 0 for t in big}; dq = deque(big)   # 0-1 BFS: entering a T0 triangle costs 1
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                c = cost[x] + (1 if y in T0 else 0)
                if y not in cost or c < cost[y]:
                    cost[y] = c
                    (dq.append if y in T0 else dq.appendleft)(y)
        cross = max(min(cost[t] for t in cc) for cc in cb if cc is not big)
    return dict(n=n, good=good, comp=len(cb), compG=len(cg), T0=len(T0), regions=len(regs),
                largest=max([len(r) for r in regs], default=0), depth=depth, cross=cross)


def run_family(name, items):
    global ok
    rows = [analyse(P, Q, n) for P, Q, n in items]
    g = sum(r["good"] for r in rows); lg = sum(r["comp"] == r["compG"] for r in rows)
    print("  %-22s maps %4d  checks ok %d  Lemma G (comp = compG) %d/%d  maps with >= 2 components %d  with T0 > 0: %d"
          % (name, len(rows), g, lg, len(rows), sum(r["comp"] >= 2 for r in rows), sum(r["T0"] > 0 for r in rows)))
    print("  %-22s   components: %s   T0 share max %.0f%%   largest T0 region (triangles): %s"
          % ("", dict(sorted(Counter(r["comp"] for r in rows).items())), 100 * max(r["T0"] / (8.0 * r["n"]) for r in rows),
             dict(sorted(Counter(r["largest"] for r in rows).items()))))
    print("  %-22s   depth of T0 triangles: %s   band width (T0 triangles to cross): %s"
          % ("", dict(sorted(Counter(r["depth"] for r in rows).items())), dict(sorted(Counter(r["cross"] for r in rows if r["comp"] >= 2).items()))))
    sys.stdout.flush()
    ok &= g == len(rows) and lg == len(rows)
    return dict(name=name, rows=rows)


stride = int(sys.argv[1]) if len(sys.argv) > 1 else 4
with contextlib.redirect_stdout(io.StringIO()):
    MAPS = {d: C9.load_maps(d, os.path.join(HERE, "..", "..", "f02")) for d in (2, 3, 4)}
out = []
for d in (2, 3):
    out.append(run_family("degree %d (all maps)" % d, [(m.P, m.Q, m.n) for m in MAPS[d]]))
out.append(run_family("degree 4 (stride %d)" % stride, [(m.P, m.Q, m.n) for m in MAPS[4][::stride]]))
LP, LQ = [mp.mpc(-1), 0, mp.mpc(1)], [mp.mpc(0), mp.mpc(0, 2)]
Ln = []; P, Q = [mp.mpc(0), mp.mpc(1)], [mp.mpc(1), mp.mpc(0)]
for k in range(1, 5):                       # degree 32 is left out: tracking 32 roots in double precision fails the edge check
    P, Q = compose(LP, LQ, P, Q, 2) if k > 1 else (LP, LQ)
    Ln.append((list(P) + [mp.mpc(0)] * (2 ** k + 1 - len(P)), list(Q) + [mp.mpc(0)] * (2 ** k + 1 - len(Q)), 2 ** k))
out.append(run_family("L_n, degree 2..16", Ln))
comp_items = []
for m0 in MAPS[4][::40]:
    c1, c2 = m0.O[0][0], m0.O[5][0]
    A, Bp = [mp.mpc(c1), 0, -mp.mpc(c2)], [mp.mpc(1), 0, mp.mpc(-1)]
    P, Q = compose(m0.P, m0.Q, A, Bp, 4)
    comp_items.append((P, Q, 8))
out.append(run_family("p0 o kappa (degree 8)", comp_items))
# second composition: (p0 o kappa) o kappa', degree 16, branched over two odd points of p0 o kappa
comp2 = []
for (P, Q, n) in comp_items[:6]:
    with contextlib.redirect_stdout(io.StringIO()):
        m1 = C9.Map(*with_generic_source(P, Q, n), "c")
    c1, c2 = m1.O[0][0], m1.O[7][0]
    A, Bp = [mp.mpc(c1), 0, -mp.mpc(c2)], [mp.mpc(1), 0, mp.mpc(-1)]
    P2, Q2 = compose(m1.P, m1.Q, A, Bp, 8)
    comp2.append((P2, Q2, 16))
out.append(run_family("p0 o kappa o kappa' (16)", comp2))
json.dump(out, open(os.path.join(HERE, "bands12.json"), "w"), indent=1)
print("PASS" if ok else "FAIL")
