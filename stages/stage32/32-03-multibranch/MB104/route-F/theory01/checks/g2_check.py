"""Second invariant for the 6,144 (4,4) omega = 14 class-4 configurations with no transfer, no shared left factor
(even after g) and equal s (see g_check.py, l_check.py).  s2(p) = sum over the 15 four-point subsets of the critical
points of (j/256)^2, again an invariant of beta_p.  Lists the distinct (s, s2) values of the maps involved, the
configuration counts by (s2 of p1, s2 of q), and tries to identify s2 and the pair sums/products (degree <= 4).
usage: python -I g2_check.py > g2_check.out
"""
import itertools, json, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "g_check.py"), encoding="utf-8").read().split("groups = defaultdict(list)")[0]
ns = {"__file__": os.path.join(HERE, "g_check.py")}; exec(src, ns)
mp = ns["mp"]; AE = ns["AE"]; D = ns["D"]; S = ns["S"]
lsrc = open(os.path.join(HERE, "l_check.py"), encoding="utf-8").read().split("res = Counter()")[0]
ls = {"__file__": os.path.join(HERE, "l_check.py")}; exec(lsrc, ls)
r = [x for x in ns["r"] if not ls["shared"](x["ia"], x["ib"])]
ms = sorted({x["ia"] for x in r} | {x["ib"] for x in r})


def s2_of(i):
    P = [ns["pc"](x) for x in D[i]["P"]]; Q = [ns["pc"](x) for x in D[i]["Q"]]
    c = AE.crit(P, Q)
    return sum((ns["jinv"](ns["cr"](*q)) / 256) ** 2 for q in itertools.combinations(c, 4))


S2 = {i: mp.re(s2_of(i)) for i in ms}
g = defaultdict(list)
for i in ms: g[(mp.nstr(mp.re(S[i]), 12), mp.nstr(S2[i], 12))].append(i)
print("configurations:", len(r), " maps:", len(ms))
print("distinct (s, s2):", {k: len(v) for k, v in g.items()})
gid = {i: k[1] for k, v in g.items() for i in v}
pc = Counter((gid[x["ia"]], gid[x["ib"]]) for x in r)
print("configurations by (s2 of p1, s2 of q):", dict(pc))
for k in g:
    print("s2 =", mp.nstr(S2[g[k][0]], 30), " poly (deg<=4):", mp.findpoly(S2[g[k][0]], 4, maxcoeff=10 ** 8))
for (a, b) in pc:
    if a == b: continue
    x = S2[next(i for i in ms if gid[i] == a)]; y = S2[next(i for i in ms if gid[i] == b)]
    print("pair", a, b, " sum poly:", mp.findpoly(x + y, 2, maxcoeff=10 ** 12), " product poly:", mp.findpoly(x * y, 2, maxcoeff=10 ** 14))
