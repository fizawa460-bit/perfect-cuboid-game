"""Prediction P4 of ROUTE-F-THEORY-01: are the cross ratios of the coincident points of the (3,3) extremal
configurations (f02/extremal3x3.json) in Q(i)?  Each cross ratio of points 0,1,2,k is identified (real and imaginary
parts separately) with mpmath.findpoly at dps 50.  usage: python -I p4_check.py > p4_check.out
"""
import json, os, sys
from collections import Counter
F2D = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "f02"))
sys.path.insert(0, F2D)
import mpmath as mp
import recheck_amb as RA
mp.mp.dps = 50
RA._rinit(3, 3)
A = RA._R["A_mp"]
top = json.load(open(os.path.join(F2D, "extremal3x3.json")))
def pt(x):  # projective (x0,x1) -> affine
    return mp.inf if abs(x[1]) < mp.mpf(10)**-40 else x[0] / x[1]
def cr(a, b, c, d):
    num = (a[0]*c[1]-a[1]*c[0])*(b[0]*d[1]-b[1]*d[0]); den = (a[0]*d[1]-a[1]*d[0])*(b[0]*c[1]-b[1]*c[0])
    return num / den
def kind(v):
    out = []
    for part in (mp.re(v), mp.im(v)):
        if abs(part) < mp.mpf(10)**-40: out.append("0"); continue
        for deg in (1, 2, 4):
            p = mp.findpoly(part, deg, maxcoeff=10**6)
            if p: out.append(f"deg{deg}:{p}"); break
        else: out.append("?")
    return tuple(out)
res = Counter(); ex = {}
for e in top:
    om, j, h = e["exact"]
    if (j, h) != (5, 0) and (j, h) != (4, 2): continue
    X = [p for p, _ in A[e["ia"]]]
    pts = [X[c[0]] for c in e["co"]]
    vals = [cr(pts[0], pts[1], pts[2], pts[k]) for k in range(3, len(pts))]
    key = ((j, h), tuple(kind(v) for v in vals))
    res[key] += 1; ex.setdefault(key, [str(mp.nstr(v, 15)) for v in vals])
for k, v in sorted(res.items(), key=lambda x: -x[1]):
    print(v, k, ex[k])
