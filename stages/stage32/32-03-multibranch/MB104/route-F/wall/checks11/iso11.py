"""checks11 / iso11.py -- request 10: isolated cone points of tau_p, face counts and 2h-links.

For a slack-0 map p (degree n) the octahedral triangulation tau_p has 8n triangles; T_k := number of triangles with
exactly k cone vertices.  Checked here on data:
  (F1) T_1 + 2 T_2 + 3 T_3 = 8n + 16, hence  T_2 + 2 T_3 = T_0 + 16.
  (F2) I1 := cone points with no cone neighbour ("isolated"),  I2 := isolated cone points with no cone point at
       distance 2h (two neighbours of a common vertex, over antipodal points of B).   4 |I2| <= 3 T_0  and
       |I2| <= 2 Nc - 12,  Nc := number of non-isolated cone points.
  (F3) the graph on the cone points with edges "adjacent" or "2h-linked": its largest component.
  (F4) labels: over which points of B do the isolated cone points lie (square-Lattes pattern: an antipodal pair).
Triangles are found by continuing the n preimages of each face centre to the three vertices of the face
(numpy roots, greedy matching, ends matched to the B-preimages computed with mpmath in census9.Map; the vertex
incidences are integers and are checked by the identities (F1) and "cone vertex in 4 triangles, smooth vertex in 8").
usage (from the repository root):
  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks11/iso11.py [stride for degree 4, default 1]
"""
import sys, os, io, contextlib, json
sys.dont_write_bytecode = True
from collections import Counter, defaultdict
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
T10 = os.path.join(HERE, "..", "checks10")
src = open(os.path.join(T10, "tau10.py"), encoding="utf-8").read().split("# ---------------- Part 1")[0]
src = src.replace("HERE = os.path.dirname(os.path.abspath(__file__))", "HERE = " + repr(T10))
G = {"__name__": "tau10_defs"}
exec(compile(src, "tau10_defs", "exec"), G)
C9, tau, compose, with_generic_source, ANTI = G["C9"], G["tau"], G["compose"], G["with_generic_source"], G["ANTI"]
BV = C9.BV
ok = True


def sph(k):
    b = BV[k]
    if b is None: return np.array([0.0, 0.0, 1.0])
    b = complex(b)
    if b == 0: return np.array([0.0, 0.0, -1.0])
    return np.array([b.real, b.imag, 0.0])
SPH = [sph(k) for k in range(6)]
FACES = [(i, j, k) for i in range(6) for j in range(i + 1, 6) for k in range(j + 1, 6)
         if ANTI[i] != j and ANTI[i] != k and ANTI[j] != k]
assert len(FACES) == 8
TS = np.concatenate([np.linspace(0.0, 0.998, 500), [1 - 1e-3, 1 - 1e-4, 1 - 1e-5, 1 - 1e-7, 1 - 1e-9]])


def faces_of(P, Q, verts, n):
    Pc = np.array([complex(c) for c in P]); Qc = np.array([complex(c) for c in Q])
    def roots_at(v):
        x, y, z = v / np.linalg.norm(v)
        if z < 0:
            w = (x + 1j * y) / (1 - z); F = Pc - w * Qc
        else:
            w = (x - 1j * y) / (1 + z); F = Qc - w * Pc          # w = 1/value
        return np.roots(F[::-1])
    def nearest_vertex(zz, k):
        return min((abs(zz - complex(v[0])), idx) for idx, v in enumerate(verts) if v[1] == k)[1]
    tris = []
    for f in FACES:
        c = (SPH[f[0]] + SPH[f[1]] + SPH[f[2]]) / 3.0
        r0 = roots_at(c); assert len(r0) == n
        ends = []
        for k in f:
            cur = r0.copy()
            for t in TS[1:]:
                nr = roots_at((1 - t) * c + t * SPH[k])
                D = np.abs(cur[:, None] - nr[None, :]); perm = [-1] * n; used = set()
                for a, b in sorted(((a, b) for a in range(n) for b in range(n)), key=lambda ab: D[ab]):
                    if perm[a] == -1 and b not in used: perm[a] = b; used.add(b)
                cur = nr[perm]
            ends.append([nearest_vertex(zz, k) for zz in cur])
        tris += [(ends[0][a], ends[1][a], ends[2][a]) for a in range(n)]
    return tris


def analyse(P, Q, n):
    PP, QQ = with_generic_source(P, Q, n)
    m, verts, arcs, good = tau(PP, QQ)
    tris = faces_of(PP, QQ, verts, n)
    cone = {i for i, v in enumerate(verts) if v[2] == 1}
    inc = Counter(v for t in tris for v in t)
    good &= len(tris) == 8 * n and all(inc[i] == (4 if i in cone else 8) for i in range(len(verts)))
    T = Counter(sum(1 for v in t if v in cone) for t in tris)
    good &= T[1] + 2 * T[2] + 3 * T[3] == 8 * n + 16 and T[2] + 2 * T[3] == T[0] + 16
    nb = defaultdict(set)
    for u, v in arcs: nb[u].add(v); nb[v].add(u)
    lab = {i: verts[i][1] for i in range(len(verts))}
    link = defaultdict(set)                                   # 2h-links between cone points
    for v in range(len(verts)):
        cs = [c for c in nb[v] if c in cone]
        for c in cs:
            for c2 in cs:
                if c2 != c and lab[c2] == ANTI[lab[c]]: link[c].add(c2)
    I1 = {c for c in cone if not (nb[c] & cone)}
    I2 = {c for c in I1 if not link[c]}
    Nc = len(cone) - len(I1)
    f2 = 4 * len(I2) <= 3 * T[0] and len(I2) <= max(0, 2 * Nc - 12)
    seen, best = set(), 0
    for c in cone:
        if c in seen: continue
        st, size = [c], 0; seen.add(c)
        while st:
            x = st.pop(); size += 1
            for y in (nb[x] & cone) | link[x]:
                if y not in seen: seen.add(y); st.append(y)
        best = max(best, size)
    isolab = Counter(str(BV[lab[c]]) for c in I1)
    # coarser graph: cone points with a common neighbour (distance <= 2 l_min = 3.057), or adjacent
    link2 = defaultdict(set)
    for v in range(len(verts)):
        cs = [c for c in nb[v] if c in cone]
        for c in cs: link2[c].update(x for x in cs if x != c)
    I3 = {c for c in I1 if not link2[c]}
    seen2, best2 = set(), 0
    for c in cone:
        if c in seen2: continue
        st, size = [c], 0; seen2.add(c)
        while st:
            x = st.pop(); size += 1
            for y in (nb[x] & cone) | link2[x]:
                if y not in seen2: seen2.add(y); st.append(y)
        best2 = max(best2, size)
    return dict(n=n, cone=len(cone), T=[T[0], T[1], T[2], T[3]], I1=len(I1), I2=len(I2), Nc=Nc, good=bool(good),
                F2=bool(f2), big=best, isolab=dict(isolab), I3=len(I3), big2=best2)


def run_family(name, items):
    global ok
    agg = Counter(); worst = dict(i1=0.0, i2=0.0, comp=1.0); rows = []
    for P, Q, n in items:
        r = analyse(P, Q, n); rows.append(r)
        agg["maps"] += 1; agg["cone"] += r["cone"]; agg["I1"] += r["I1"]; agg["I2"] += r["I2"]
        for k in range(4): agg["T%d" % k] += r["T"][k]
        agg["good"] += r["good"]; agg["F2"] += r["F2"]; agg["conn"] += (r["big"] == r["cone"])
        agg["I3"] += r["I3"]; agg["conn2"] += (r["big2"] == r["cone"]); worst["comp2"] = min(worst.get("comp2", 1.0), r["big2"] / r["cone"])
        worst["i1"] = max(worst["i1"], r["I1"] / r["cone"]); worst["i2"] = max(worst["i2"], r["I2"] / r["cone"])
        worst["comp"] = min(worst["comp"], r["big"] / r["cone"])
    print("  %-22s maps %4d  cone %6d  isolated %5d (%.1f%%, max %.0f%%)  2h-isolated %4d (%.1f%%, max %.0f%%)  T0..T3 %s"
          % (name, agg["maps"], agg["cone"], agg["I1"], 100 * agg["I1"] / agg["cone"], 100 * worst["i1"],
             agg["I2"], 100 * agg["I2"] / agg["cone"], 100 * worst["i2"], [agg["T%d" % k] for k in range(4)]))
    print("  %-22s   counts ok %d/%d   (F2) ok %d/%d   adjacency+2h graph connected %d/%d (smallest share of the largest component %.0f%%)"
          % ("", agg["good"], agg["maps"], agg["F2"], agg["maps"], agg["conn"], agg["maps"], 100 * worst["comp"]))
    print("  %-22s   within 2 l_min (common neighbour): cone points with none %d; graph connected %d/%d (smallest share %.0f%%)"
          % ("", agg["I3"], agg["conn2"], agg["maps"], 100 * worst["comp2"]))
    sys.stdout.flush()
    ok &= agg["good"] == agg["maps"] and agg["F2"] == agg["maps"]
    return dict(name=name, worst=worst, rows=rows if len(rows) <= 20 else None, **{k: int(v) for k, v in agg.items()})


stride = int(sys.argv[1]) if len(sys.argv) > 1 else 1
with contextlib.redirect_stdout(io.StringIO()):
    MAPS = {d: C9.load_maps(d, os.path.join(HERE, "..", "..", "f02")) for d in (1, 2, 3, 4)}
out = []
for d in (1, 2, 3):
    out.append(run_family("degree %d (all maps)" % d, [(m.P, m.Q, m.n) for m in MAPS[d]]))
out.append(run_family("degree 4 (stride %d)" % stride, [(m.P, m.Q, m.n) for m in MAPS[4][::stride]]))
LP, LQ = [mp.mpc(-1), 0, mp.mpc(1)], [mp.mpc(0), mp.mpc(0, 2)]
Ln = []; P, Q = [mp.mpc(0), mp.mpc(1)], [mp.mpc(1), mp.mpc(0)]
for k in range(1, 6):
    P, Q = compose(LP, LQ, P, Q, 2) if k > 1 else (LP, LQ)
    Ln.append((list(P) + [mp.mpc(0)] * (2 ** k + 1 - len(P)), list(Q) + [mp.mpc(0)] * (2 ** k + 1 - len(Q)), 2 ** k))
res = run_family("L_n, n = 1..5", Ln); out.append(res)
for r in res["rows"]:
    print("     L_n degree %2d: cone %2d  T0..T3 %s  isolated %2d  2h-isolated %d  largest component %d  isolated lie over %s"
          % (r["n"], r["cone"], r["T"], r["I1"], r["I2"], r["big"], r["isolab"]))
comp_items = []
for m0 in MAPS[4][::40]:
    c1, c2 = m0.O[0][0], m0.O[5][0]
    A, Bp = [mp.mpc(c1), 0, -mp.mpc(c2)], [mp.mpc(1), 0, mp.mpc(-1)]
    P, Q = compose(m0.P, m0.Q, A, Bp, 4)
    comp_items.append((P, Q, 8))
out.append(run_family("p0 o kappa (degree 8)", comp_items))
json.dump(out, open(os.path.join(HERE, "iso11.json"), "w"), indent=1)
print("PASS" if ok else "FAIL")
