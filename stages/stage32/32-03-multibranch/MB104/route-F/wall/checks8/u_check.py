"""CHECK-05: theorem U of THEORY-07 on the F-02 records.
For every recorded Moebius map T (files ../../f02/low3x3.json, low4x4.json: records [ia, ib, s, t, omega, j, h, bd])
whose O-sets coincide completely (j + h = |O| = 2n + 4), T is rebuilt in mpmath from the frame points s -> t
(as in analyze_extremal.exact), and we test q o T = h o p with h a Moebius map that maps B onto B
(an octahedral rotation): h is fitted on three generic points and checked on three more (tolerance 1e-25).
usage: python -I -O u_check.py 3 | 4      (prints a summary; mpmath dps 50)
"""
import json, os, sys
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); sys.path.insert(0, F02)
import recheck_amb as RA
import analyze_extremal as AE
mp = AE.mp
BPTS = AE.BPTS
TESTS = [mp.mpc("0.3127", "0.7781"), mp.mpc("-1.137", "0.291"), mp.mpc("0.6", "-1.4"),
         mp.mpc("2.2", "0.15"), mp.mpc("-0.41", "-0.93"), mp.mpc("1.7", "1.1")]
_W = {}


def init(n): RA._rinit(n, n); _W.update(RA._R)


def work(rec):
    ia, ib, s, t = rec[:4]
    O1, Oq = _W["A_mp"][ia], _W["B_mp"][ib]
    X1 = [p for p, _ in O1]; Xq = [p for p, _ in Oq]
    T = RA.frame(*[Xq[k] for k in t[:3]]) * mp.inverse(RA.frame(*[X1[k] for k in s[:3]]))
    Tm = (T[0, 0], T[0, 1], T[1, 0], T[1, 1])
    P, Q = _W["A_maps"][ia]; Pq, Qq = _W["B_maps"][ib]
    P = [mp.mpc(x) for x in P]; Q = [mp.mpc(x) for x in Q]; Pq = [mp.mpc(x) for x in Pq]; Qq = [mp.mpc(x) for x in Qq]
    v1 = [AE.peval(P, Q, z) for z in TESTS]; v2 = [AE.peval(Pq, Qq, AE.mob(Tm, z)) for z in TESTS]
    h = AE.mob3(v1[:3], v2[:3])
    ok = all(AE.same_pt(AE.mob(h, a), b, mp.mpf(10) ** -25) for a, b in zip(v1[3:], v2[3:]))
    octa = all(any(AE.same_pt(AE.mob(h, b), c, mp.mpf(10) ** -25) for c in BPTS) for b in BPTS)
    return ok, octa


if __name__ == "__main__":
    n = int(sys.argv[1])
    recs = json.load(open(os.path.join(F02, f"low{n}x{n}.json")))
    full = [r for r in recs if r[5] + r[6] == 2 * n + 4]
    with Pool(11, initializer=init, initargs=(n,)) as pool:
        res = pool.map(work, full, chunksize=200)
    print(json.dumps(dict(degree=n, full_coincidence_T=len(full),
                          birationality_degree=dict(Counter(r[7] for r in full)),
                          q_T_equals_h_p=sum(1 for ok, _ in res if ok),
                          h_octahedral=sum(1 for ok, o in res if ok and o),
                          jh=sorted([list(k) + [v] for k, v in Counter((r[5], r[6]) for r in full).items()]))))
