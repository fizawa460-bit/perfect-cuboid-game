#!/usr/bin/env python3
"""Degree-6 slack-0 maps p = f o g with deg f = 2, deg g = 3 (the data with two labels n = 3), added to the state.

f: the degree-2 map with critical values y1 != y2 in B: P = y1x + y2x x^2, Q = y1z + y2z x^2 (critical points 0, oo).
O(f) = the 8 simple points over the other four points of B.  By lemma T0 (DRAFT-TOWER-17) p is slack 0 iff g has
simple critical points with values in O(f); a cubic has 4 critical points with distinct values, so the critical
values form a 4-subset S of O(f).  For each S the 4 cubics with branch set S are found numerically:
  move S[0] to oo by a Moebius map M of the middle line; normal form gt(x) = (x^3 + b x^2 + c x + d) / x
  (pole of order 2 at oo and simple pole at 0; translation and scaling fixed up to x -> -x);
  critical points: roots of 2x^3 + b x^2 - d; solve e_k(critical values) = e_k(M(S[1:])) (k = 1, 2, 3) by Newton
  from random starts; g = M^-1 o gt.
Datum: n(y1) = n(y2) = 3, n(y) = #(S over y).  A rotation of B moves it to the representative, then Datum.offer
(K filter, mp refinement, verification, exact Moebius test) decides.  Usage: python -I compose23.py MAPS6DIR [--only ...]
"""
import os, sys, json, itertools, argparse, time
os.environ["MAPS_N"] = "6"
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import build_maps6 as B6
import build_maps as bm
from compose6 import ROT, target_apply, hom_eval, to_chart

BK = B6.BKEYS


def cubic_solutions(T, rng, starts=400):
    """all (b, c, d) with critical values of (x^3+bx^2+cx+d)/x equal to the multiset T (3 complex numbers)"""
    eT = np.array([sum(T), T[0] * T[1] + T[0] * T[2] + T[1] * T[2], T[0] * T[1] * T[2]])
    sc = max(1.0, max(abs(t) for t in T))
    def F(v):
        b, c, d = v
        cr = np.roots([2, b, 0, -d])
        if len(cr) != 3 or np.min(np.abs(cr)) < 1e-12: return None
        vals = (cr ** 3 + b * cr ** 2 + c * cr + d) / cr
        e = np.array([vals.sum(), vals[0] * vals[1] + vals[0] * vals[2] + vals[1] * vals[2], vals.prod()])
        return (e - eT) / np.array([sc, sc ** 2, sc ** 3])
    sols = []
    for _ in range(starts):
        v = (rng.normal(size=3) + 1j * rng.normal(size=3)) * np.array([sc ** (1 / 3), sc ** (2 / 3), sc])
        for _it in range(60):
            f0 = F(v)
            if f0 is None: break
            if np.linalg.norm(f0) < 1e-13: break
            Jm = np.zeros((3, 3), complex); h = 1e-7 * (1 + np.abs(v))
            ok = True
            for k in range(3):
                vp = v.copy(); vp[k] += h[k]; fp = F(vp)
                if fp is None: ok = False; break
                Jm[:, k] = (fp - f0) / h[k]
            if not ok: break
            try: st = np.linalg.solve(Jm, -f0)
            except np.linalg.LinAlgError: break
            if not np.isfinite(st).all(): break
            if np.linalg.norm(st) > 10 * (1 + np.linalg.norm(v)): st *= 10 * (1 + np.linalg.norm(v)) / np.linalg.norm(st)
            v = v + st
        f0 = F(v)
        if f0 is None or np.linalg.norm(f0) > 1e-11: continue
        if not any(np.max(np.abs(v - s) / (1 + np.abs(s))) < 1e-6 for s in sols): sols.append(v)
    return sols


def quad_f(y1, y2):
    (a1, z1), (a2, z2) = bm.BH[y1], bm.BH[y2]
    return np.array([a1, 0, a2], complex), np.array([z1, 0, z2], complex)


def simple_pts(P, Q, y):
    a, z = bm.BH[y]
    F = complex(z) * P - complex(a) * Q
    return list(np.roots(np.trim_zeros(F, "b")[::-1]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("maps6"); ap.add_argument("--only", default="")
    a = ap.parse_args()
    H = json.load(open(os.path.join(HERE, "hurwitz6.json")))
    reps = {d: t for d, t, _ in B6.rep_data(H)}
    if a.only: reps = {d: t for d, t in reps.items() if d in set(a.only.split(","))}
    rng = np.random.default_rng(20261117)
    D, stats = {}, {}
    for y1, y2 in itertools.permutations(BK, 2):
        P, Q = quad_f(y1, y2)
        others = [y for y in BK if y not in (y1, y2)]
        O = [(w, y) for y in others for w in simple_pts(P, Q, y)]
        if len(O) != 8: continue
        for S in itertools.combinations(O, 4):
            ns = [0] * 6; ns[BK.index(y1)] = 3; ns[BK.index(y2)] = 3
            for _, y in S: ns[BK.index(y)] += 1
            for h, perm in ROT:
                img = [0] * 6
                for i in range(6): img[perm[i]] = ns[i]
                key = "".join(map(str, img))
                if key in reps: break
            else:
                continue
            if key not in D:
                D[key] = B6.Datum(key, reps[key], a.maps6); D[key].prog.setdefault("found_by_compose", 0)
                stats[key] = [len(D[key].recs), 0, 0]
            Dk = D[key]
            if len(Dk.recs) >= Dk.target: continue
            w = [s for s, _ in S]
            # M: z -> 1/(z - w0), then centre the other three
            t = [1 / (x - w[0]) for x in w[1:]]; cen = sum(t) / 3; t = [x - cen for x in t]
            for b, c, d in cubic_solutions(t, rng):
                # gt = (x^3 + b x^2 + c x + d)/x ; g = M^-1(gt) = w0 + 1/(gt + cen)
                G1 = np.array([d, c, b, 1], complex); G2 = np.array([0, 1, 0, 0], complex)     # gt = G1/G2
                N = G1 + cen * G2                                                              # gt + cen
                g1 = w[0] * N + G2; g2 = N                                                     # g = (w0 N + G2)/N
                Pp, Qp = hom_eval(P, g1, g2), hom_eval(Q, g1, g2)
                Pp, Qp = target_apply(h, Pp, Qp)
                stats[key][1] += 1
                r = to_chart(Pp, Qp, rng)
                if r is None: continue
                z, e, nv = r
                if Dk.offer(z, e, "compose", nv): stats[key][2] += 1
    for k, Dk in D.items():
        Dk.save(time.time(), "compose23")
        print(k, "before", stats[k][0], "tried", stats[k][1], "added", stats[k][2], "now", len(Dk.recs), "/", Dk.target, flush=True)


if __name__ == "__main__":
    main()
