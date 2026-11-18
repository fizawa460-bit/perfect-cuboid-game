#!/usr/bin/env python3
"""E19 s.21.4: mechanical check of the Gauss-Bonnet bookkeeping for the closed-star complex D of a vertex set H
(pinches resolved into sectors), on random simplicial triangulations of the sphere.

For H (any vertex set), H° = vertices of H all of whose neighbours are in H, D = closed triangles with a vertex in H°,
D^ = D with every vertex split into its sectors.  Checked, for every sample:
  (1) the vertices of D are in H, the interior vertices of D^ are exactly H°, every other vertex of D has a gap;
  (2) every sector at a vertex outside H° has j >= 2 triangles;
  (3) sum_{H°} (6 - deg) + sum_{sectors} (3 - j) = 6 chi(D^)   (chi computed directly as V - E + F of D^);
  (4) chi(D^) = 2 c - k with k boundary circles, every circle has >= 3 sector copies (simplicial case).
Only combinatorics is checked here; the valence-4/8 and seed constraints of s.21.4 are not.
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/gb21_check.py
"""
import random, sys
sys.dont_write_bytecode = True


def octahedron():
    F = [(0, 2, 4), (2, 1, 4), (1, 3, 4), (3, 0, 4), (2, 0, 5), (1, 2, 5), (3, 1, 5), (0, 3, 5)]
    return 6, [list(f) for f in F]


def edges_of(F):
    E = {}
    for i, f in enumerate(F):
        for a in range(3):
            e = frozenset((f[a], f[(a + 1) % 3])); E.setdefault(e, []).append(i)
    return E


def random_triangulation(rng, n_split, n_flip):
    nv, F = octahedron()
    for _ in range(n_split):                       # stellar subdivision of a random face
        i = rng.randrange(len(F)); a, b, c = F[i]; v = nv; nv += 1
        F[i] = [a, b, v]; F.append([b, c, v]); F.append([c, a, v])
    for _ in range(n_flip):                        # random flips that keep the complex simplicial
        E = edges_of(F); e = rng.choice(list(E)); i, j = E[e]
        a, b = tuple(e); fi, fj = F[i], F[j]
        c = [x for x in fi if x not in e][0]; d = [x for x in fj if x not in e][0]
        if frozenset((c, d)) in E: continue
        if min(sum(1 for f in F if x in f) for x in (a, b)) <= 3: continue
        k = fi.index(a)                            # keep orientation: fi = (a, b, c) cyclically or (b, a, c)
        if fi[(k + 1) % 3] == b: F[i] = [a, d, c]; F[j] = [d, b, c]
        else: F[i] = [b, d, c]; F[j] = [d, a, c]
    return nv, F


def links(nv, F):
    """cyclic link of each vertex as the list of its faces in order"""
    inc = {v: [] for v in range(nv)}
    for i, f in enumerate(F):
        for v in f: inc[v].append(i)
    cyc = {}
    for v, fs in inc.items():
        nxt = {}
        for i in fs:
            f = F[i]; k = f.index(v); nxt[f[(k + 1) % 3]] = (f[(k + 2) % 3], i)
        start = next(iter(nxt)); u = start; order = []
        while True:
            w, i = nxt[u]; order.append(i); u = w
            if u == start: break
        assert len(order) == len(fs)
        cyc[v] = order
    return cyc


def check(nv, F, H):
    nb = {v: set() for v in range(nv)}
    for f in F:
        for a in f:
            nb[a].update(x for x in f if x != a)
    Hin = {v for v in H if nb[v] <= H}
    Dfaces = {i for i, f in enumerate(F) if any(x in Hin for x in f)}
    if not Dfaces: return None
    cyc = links(nv, F)
    assert all(x in H for i in Dfaces for x in F[i])                                   # (1)
    sectors = {}                    # (v, sector id) for v outside H°; face -> sector at v
    sec_of = {}
    jlist = []
    for v in {x for i in Dfaces for x in F[i]} - Hin:
        order = cyc[v]; inD = [i in Dfaces for i in order]
        assert not all(inD)                                                             # (1) a gap exists
        k0 = inD.index(False); m = len(order); sid = -1; prev = False
        for t in range(m):
            i = order[(k0 + 1 + t) % m]
            if i in Dfaces:
                if not prev: sid += 1; jlist.append(0)
                sec_of[(v, i)] = sid; jlist[-1] += 1; prev = True
            else: prev = False
        sectors[v] = sid + 1
    assert all(j >= 2 for j in jlist)                                                   # (2)
    node = lambda v, i: ("in", v) if v in Hin else ("bd", v, sec_of[(v, i)])
    Vset, Eset = set(), {}
    for i in Dfaces:
        f = F[i]; ns = [node(x, i) for x in f]; Vset.update(ns)
        for a in range(3):
            e = frozenset((ns[a], ns[(a + 1) % 3])); Eset[e] = Eset.get(e, 0) + 1
    chi = len(Vset) - len(Eset) + len(Dfaces)
    lhs = sum(6 - len(nb[v]) for v in Hin) + sum(3 - j for j in jlist)
    assert lhs == 6 * chi, (lhs, chi)                                                   # (3)
    bd = [e for e, cnt in Eset.items() if cnt == 1]
    adj = {}
    for e in bd:
        a, b = tuple(e); adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    assert all(len(x) == 2 for x in adj.values()) and all(n[0] == "bd" for n in adj)
    seen, circles = set(), []
    for s in adj:
        if s in seen: continue
        ln, u, p = 0, s, None
        while True:
            seen.add(u); ln += 1; w = adj[u][0] if adj[u][0] != p else adj[u][1]; p, u = u, w
            if u == s: break
        circles.append(ln)
    par = {x: x for x in Vset}
    def fd(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for e in Eset:
        a, b = tuple(e); par[fd(a)] = fd(b)
    comps = len({fd(x) for x in Vset})
    assert chi == 2 * comps - len(circles) and min(circles) >= 3                         # (4)
    return max(sectors.values()) if sectors else 0


rng = random.Random(20261118)
n_ok = 0; max_m = 0
for trial in range(200):
    nv, F = random_triangulation(rng, rng.randrange(20, 200), rng.randrange(0, 800))
    for _ in range(5):
        p = rng.uniform(0.3, 0.95)
        H = {v for v in range(nv) if rng.random() < p}
        if len(H) == nv: continue                  # bad vertices exist in E19
        r = check(nv, F, H)
        if r is not None: n_ok += 1; max_m = max(max_m, r)
print("samples checked: %d   largest number of sectors at one vertex: %d" % (n_ok, max_m))
assert n_ok > 500 and max_m >= 2
print("PASS")
