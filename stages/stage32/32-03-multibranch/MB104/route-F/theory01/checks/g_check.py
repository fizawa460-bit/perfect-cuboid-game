"""Prediction P1 of ROUTE-F-THEORY-01 (part G): the (4,4) omega = 14 class-4 configurations without a symmetry
transfer (rows of p1_rows.json).  For each map involved, s(p) = sum over the 15 four-point subsets of the
critical points of j(cross ratio).  s is invariant under p -> g o p o S (g a symmetry of B), so it is an invariant
of the class beta_p; s(p^tau) = tau(s(p)) for a field automorphism tau.  The script lists the distinct values of s,
and identifies the real and imaginary parts with mpmath.findpoly (dps 45; the stored coefficients have about 40 digits, so only degree <= 2 is tried).
usage: python -I g_check.py > g_check.out
"""
import itertools, json, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); sys.path.insert(0, F02)
os.environ["EXT_N"] = "4"
import mpmath as mp
mp.mp.dps = 45
import extremal_struct as ES
import analyze_extremal as AE
mp.mp.dps = 45
rows = json.load(open(os.path.join(HERE, "p1_rows.json")))
r = [x for x in rows if x["cls"] == "4" and x["T"] == "-"]
ms = sorted({x["ia"] for x in r} | {x["ib"] for x in r})
D = json.load(open(os.path.join(F02, "maps4.json")))


def jinv(l): return 256 * (l * l - l + 1) ** 3 / (l * l * (l - 1) ** 2)


def cr(a, b, c, d):
    if a == mp.inf: return (b - d) / (b - c)
    if b == mp.inf: return (a - c) / (a - d)
    if c == mp.inf: return (b - d) / (a - d)
    if d == mp.inf: return (a - c) / (b - c)
    return (a - c) * (b - d) / ((a - d) * (b - c))


def pc(x):              # "(a + bj)" -> mpc (the stored coefficients have about 40 digits)
    x = x.strip("()").replace(" ", "")
    k = max(x.rfind("+"), x.rfind("-"))
    while k > 0 and x[k - 1] in "eE": k = max(x.rfind("+", 0, k), x.rfind("-", 0, k))
    return mp.mpc(mp.mpf(x[:k]), mp.mpf(x[k:-1]))


def s_of(i):
    P = [pc(x) for x in D[i]["P"]]; Q = [pc(x) for x in D[i]["Q"]]
    c = AE.crit(P, Q)
    return sum(jinv(cr(*q)) for q in itertools.combinations(c, 4))


S = {i: s_of(i) for i in ms}
groups = defaultdict(list)
for i in ms: groups[mp.nstr(mp.re(S[i]), 15)].append(i)          # imaginary parts are below 1e-30
print("maps:", len(ms), " distinct s values:", {k: len(v) for k, v in groups.items()})
for k in groups:
    v = mp.re(S[groups[k][0]])
    print("s =", mp.nstr(v, 30), " minimal polynomial (degree <= 2):", mp.findpoly(v, 2, maxcoeff=10 ** 12))
gid = {i: k for k, g in groups.items() for i in g}
print("configurations by (s of p1, s of q):", dict(Counter((gid[x["ia"]], gid[x["ib"]]) for x in r)))
print("same datum within a pair:", dict(Counter(D[x["ia"]]["datum"] == D[x["ib"]]["datum"] for x in r)))
