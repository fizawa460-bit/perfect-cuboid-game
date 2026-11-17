"""Clause (L) of claim D for the (4,4) omega = 14 class-4 configurations without a symmetry transfer: do p1 and
g o q (g one of the 24 Moebius symmetries of B, or g followed by complex conjugation) have a degree-2 left factor
with the same critical values?  Uses the left-factor lists cached by p1_check.py (critical-value pairs of r for
p = r o u).  usage: python -I l_check.py > l_check.out
"""
import json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); sys.path.insert(0, F02)
os.environ["EXT_N"] = "4"
import mpmath as mp
import extremal_struct as ES
H = {tuple(json.loads(k)): v for k, v in json.load(open(os.path.join(HERE, "p1_cache.json"))).items()}
rows = json.load(open(os.path.join(HERE, "p1_rows.json")))
r = [x for x in rows if x["cls"] == "4" and x["T"] == "-"]
G = ES.FO["group"]()
BIG = 1e300


def img(g, w, conj):
    z = mp.inf if abs(w) > 1e200 else mp.mpc(w)
    v = ES.FO["mob"](g, z)
    v = BIG if v == mp.inf or abs(v) > 1e200 else complex(v)
    return v.conjugate() if conj and v != BIG else v


def key(pair): return tuple(sorted((round(w.real, 6), round(w.imag, 6)) for w in pair))


def lfs(i): return [tuple(complex(a, b) for a, b in x) for x in H[("m", i)]["lf"]]


def shared(ia, ib):
    A = {key(x) for x in lfs(ia)}
    for g in G:
        for conj in (False, True):
            if A & {key([img(g, w, conj) for w in x]) for x in lfs(ib)}: return True
    return False


res = Counter()
memo = {}
for x in r:
    pr = (x["ia"], x["ib"])
    if pr not in memo: memo[pr] = shared(*pr)
    res[memo[pr]] += 1
print("class-4 (5,0) configurations without transfer:", len(r))
print("p1 and g o q share a degree-2 left factor (some g, with or without conjugation):", dict(res))
print("maps decomposable (p1, q):", dict(Counter((bool(H[("m", x["ia"])]["lf"]), bool(H[("m", x["ib"])]["lf"])) for x in r)))
# cross-tabulate with the invariant s of g_check.py (rational 9824 vs. the quadratic pair)
src = open(os.path.join(HERE, "g_check.py"), encoding="utf-8").read().split("groups = defaultdict(list)")[0]
ns = {"__file__": os.path.join(HERE, "g_check.py")}; exec(src, ns)
rat = {i: abs(mp.re(ns["S"][i]) - 9824) < 1e-20 for i in ns["ms"]}
print("(L) x (p1 rational s, q rational s):", dict(Counter((memo[(x["ia"], x["ib"])], rat[x["ia"]], rat[x["ib"]]) for x in r)))
