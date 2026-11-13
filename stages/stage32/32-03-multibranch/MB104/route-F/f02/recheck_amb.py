"""Recheck, in high precision, every borderline Moebius map T recorded by f02_spectrum.py (file amb{a}x{b}.json).

A record is (ia, ib, s, t, omega, j, h): T sends the points s[0], s[1], s[2] of O_{p1} to t[0], t[1], t[2] of O_q.
Here T is rebuilt in mpmath (dps 50) from O-sets computed in mpmath, which use the same root order as F1.map_data.
A pair of points counts as coincident when its cross value is below 1e-30. Non-coincident pairs must stay above
1e-12, or the run fails. The exact omega, j and h are compared with the floating-point values.
If a T changes and its exact omega is <= cut, the birationality degree is computed again.

usage: python -I -O recheck_amb.py 4 4
"""
import json, os, sys
import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import f02_spectrum as F2
F1 = F2.F1

mp.mp.dps = 50


def mp_map_data(P, Q):
    """same as F1.map_data, but the points are kept in mpmath (same order)"""
    n = len(P) - 1; pts = []
    for key, (yx, yz) in F1.BH.items():
        F = [mp.mpc(yz) * P[k] - mp.mpc(yx) * Q[k] for k in range(n + 1)]
        scale = max(abs(c) for c in F)
        deg = max(k for k in range(n + 1) if abs(F[k]) > scale * mp.mpf(10) ** -35)
        rts = [(mp.mpc(1), mp.mpc(0))] * (n - deg)
        if deg > 0:
            rts += [(r, mp.mpc(1)) for r in mp.polyroots(list(reversed(F[:deg + 1])), maxsteps=300, extraprec=300)]
        rts = [(x / mp.sqrt(abs(x) ** 2 + abs(z) ** 2), z / mp.sqrt(abs(x) ** 2 + abs(z) ** 2)) for x, z in rts]
        for r in rts:
            mult = sum(1 for s in rts if abs(r[0] * s[1] - r[1] * s[0]) < 1e-12)
            if mult == 1: pts.append((r, F1.LAB[key]))
    return pts


def frame(p0, p1, p2):
    M = mp.matrix([[p0[0], p1[0]], [p0[1], p1[1]]])
    co = mp.lu_solve(M, mp.matrix([p2[0], p2[1]]))
    return M * mp.diag([co[0], co[1]])


_R = {}


def _rinit(a, b):
    A_maps, B_maps = F2.maps_of_degree(a), F2.maps_of_degree(b)
    _R.update(a=a, A_maps=A_maps, B_maps=B_maps, cut=F2.CUT[(a, b)],
              A_mp=[mp_map_data(*m) for m in A_maps], B_mp=[mp_map_data(*m) for m in B_maps])


def _recheck(recs):
    a, cut = _R["a"], _R["cut"]
    out = []; minfar = mp.mpf(1); maxnear = mp.mpf(0); lowest = None
    eps = mp.mpf(10) ** -30
    for ia, ib, s, t, om, j, h in recs:
        O1, Oq = _R["A_mp"][ia], _R["B_mp"][ib]
        X1 = [p for p, _ in O1]; Xq = [p for p, _ in Oq]
        T = frame(*[Xq[k] for k in t[:3]]) * mp.inverse(frame(*[X1[k] for k in s[:3]]))
        Ti = mp.inverse(T)
        V = []
        for y, ly in Oq:
            v = Ti * mp.matrix([y[0], y[1]]); nv = mp.sqrt(abs(v[0]) ** 2 + abs(v[1]) ** 2)
            V.append((v[0] / nv, v[1] / nv, ly))
        jj = hh = 0
        for x, lx in O1:
            for v0, v1, ly in V:
                c = abs(x[0] * v1 - x[1] * v0)
                if c < eps:
                    maxnear = max(maxnear, c)
                    if lx == ly: jj += 1
                    else: hh += 1
                elif c < minfar: minfar = c
        om2 = len(O1) + len(Oq) - 2 * jj - hh
        if lowest is None or om2 < lowest: lowest = om2
        if (om2, jj, hh) != (om, j, h):
            bd = None
            if om2 <= cut:
                Tn = np.array([[complex(T[0, 0]), complex(T[0, 1])], [complex(T[1, 0]), complex(T[1, 1])]])
                bd = F2.bir_degree(a, *_R["A_maps"][ia], *_R["B_maps"][ib], Tn / np.linalg.norm(Tn))
            out.append(dict(ia=ia, ib=ib, s=s, t=t, float=[om, j, h], exact=[om2, jj, hh], bir_degree=bd))
    return out, float(minfar), float(maxnear), lowest


def main(a, b, workers=None):
    from multiprocessing import Pool
    amb = json.load(open(os.path.join(HERE, f"amb{a}x{b}.json")))
    cut = F2.CUT[(a, b)]
    # the high-precision O-sets must list the same points, in the same order, as the floating-point ones
    _rinit(a, b)
    for mpl, maps in ((_R["A_mp"], _R["A_maps"]), (_R["B_mp"], _R["B_maps"])):
        for O, m in zip(mpl, maps):
            fl = F1.map_data(*m)
            if len(fl) != len(O) or not all(abs(complex(p[0]) * q[1] - complex(p[1]) * q[0]) < 1e-12 and l == k
                                            for (p, l), (q, k) in zip(O, fl)):
                raise SystemExit("point order differs between mpmath and floating-point O-sets")
    workers = workers or max(1, (os.cpu_count() or 2) - 1)
    size = 2000
    parts = [amb[i:i + size] for i in range(0, len(amb), size)]
    changed = []; minfar = 1.0; maxnear = 0.0; lowest = None
    with Pool(workers, initializer=_rinit, initargs=(a, b)) as pool:
        for k, (out, mf, mn, lo) in enumerate(pool.imap_unordered(_recheck, parts)):
            changed += out; minfar = min(minfar, mf); maxnear = max(maxnear, mn)
            if lo is not None and (lowest is None or lo < lowest): lowest = lo
            if k % 20 == 0: print(f"  part {k + 1}/{len(parts)}", file=sys.stderr, flush=True)
    from collections import Counter
    trans = Counter((tuple(c["float"]), tuple(c["exact"]), c["bir_degree"]) for c in changed)
    res = dict(bidegree=[a, b], borderline=len(amb), changed=len(changed),
               transitions=[[list(f), list(e), bd, n] for (f, e, bd), n in sorted(trans.items())],
               changed_to_omega_le_cut=[c for c in changed if c["exact"][0] <= cut][:50],
               changed_from_omega_le_cut=sum(1 for c in changed if c["float"][0] <= cut),
               lowest_exact_omega_among_borderline=lowest,
               max_coincident_cross=maxnear, min_noncoincident_cross=minfar)
    json.dump(changed, open(os.path.join(HERE, f"amb{a}x{b}_changed.json"), "w"))
    print(json.dumps(res, default=str))
    ok = minfar > 1e-12
    print("PASS" if ok else "FAIL: a non-coincident pair below 1e-12 in high precision")
    if not ok: raise SystemExit(1)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
