"""32R-72 D-check members: for every finite bad member q of d_<i>_<t>.out (all curves, both field triples, deduplicated
by ideal), one member job as in mkcand.py: G_q = s0 F1 + u F2 + v F3 (same basis/seed as e_<i>_<t>), residual after
saturating out the D-curves, fast genus tail v2.  Degree-k points over F_p(ww), minpoly of degree k.
usage (from stoll/): python n16/mkdmem.py  -> n16/dm/dm_<i>_<t>_<k>.sing, n16/dm/jobs.txt"""
import json, re, os
NL = chr(10); P = 10009
plan = json.load(open("n16/plan.json"))
FAST = open("gfast/tail_fast_v2.sing").read()
TAIL = open("n16/net_tail_c.sing").read().split(NL)
BASIS = NL.join(l for l in TAIL if l.startswith(("ideal SS", "ideal NFL", "system(\"random\"", "int ii;", "list FL;", "ideal FI;")))
def polyterms(s):
    s = s.replace(" ", ""); out = {}
    for sg, body in re.findall(r"([+-]?)([^+-]+)", s):
        c = 1; e = [0, 0, 0]
        for f in body.split("*"):
            m = re.fullmatch(r"(s0|u|v)(?:\^(\d+))?", f)
            if m: e[["s0", "u", "v"].index(m.group(1))] += int(m.group(2) or 1)
            else: c *= int(f)
        if sg == "-": c = -c
        out[tuple(e)] = (out.get(tuple(e), 0) + c) % P
    return out
def kernel(rows):
    a, b = rows
    k = [(a[1] * b[2] - a[2] * b[1]) % P, (a[2] * b[0] - a[0] * b[2]) % P, (a[0] * b[1] - a[1] * b[0]) % P]
    assert any(k); return k
os.makedirs("n16/dm", exist_ok=True)
jobs = []; bad = []; percls = {}
for jt in open("n16/dlist2.txt").read().split():
    i, t = jt.split("_")
    txt = open(f"n16/d_{jt}.out").read()
    pts = {}
    for m in re.finditer(r"bad \d+\s+deg (\d+) : _\[1\]=([^\n]*)\n_\[2\]=([^\n]*)", txt):
        pts.setdefault((m.group(2).strip(), m.group(3).strip()), int(m.group(1)))
    src = open(f"n16/e_{jt}.sing").read(); k = src.index("int HH = ")
    pre = src[:k] + src[k:src.index(NL, k)] + NL
    ti = int(t); ti = 2 if (ti >= 2 and ti == plan[i].get("third")) else ti
    D = plan[i]["decs"][ti][1]
    cids = sorted(int(x) for x in D if int(x) <= 92)
    dc = ("intersect(" + ",".join(f"G{x}" for x in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
    for n, ((g1, g2), dg) in enumerate(sorted(pts.items())):
        p1, p2 = polyterms(g1), polyterms(g2); mp = None
        if dg == 1:
            if any(sum(e) != 1 for p in (p1, p2) for e in p): bad.append((jt, g1, g2, "nonlinear")); continue
            rows = [[p.get((1, 0, 0), 0), p.get((0, 1, 0), 0), p.get((0, 0, 1), 0)] for p in (p1, p2)]
            coef = [str(x) for x in kernel(rows)]
        else:
            if any(e[0] for e in p1) or any(sum(e) != dg for e in p1) or p1.get((0, dg, 0), 0) == 0:
                bad.append((jt, g1, g2, "shape1")); continue
            s0t = [e for e in p2 if e[0]]
            if len(s0t) != 1 or s0t[0][0] != 1 or s0t[0][1] != 0 or p2[s0t[0]] != 1:
                bad.append((jt, g1, g2, "shape2")); continue
            # p2 = s0 * v^k + R(u, v)  ->  chart v = 1: s0 = -R(ww, 1)
            R = "+".join(f"({c})*ww^{e[1]}" for e, c in p2.items() if not e[0]) or "0"
            mp = "+".join(f"({c})*ww^{e[1]}" for e, c in p1.items())
            coef = [f"(-({R}))", "ww", "1"]
        body = pre + BASIS + NL + f"ideal Dc = std({dc});" + NL
        body += f"poly NN = {coef[0]} * FL[1] + {coef[1]} * FL[2] + {coef[2]} * FL[3];" + NL
        body += 'ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;' + NL
        body += f'"D-check member {jt} #{n} degree {dg}; residual dim", dim(Bp), " degree", mult(Bp), " expected 16";' + NL
        body += 'if (mult(Bp) < 16) { "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }' + NL
        body += 'if (dim(Bp) != 2) { "MEMBER-NOT-CURVE"; quit; }' + NL + FAST
        if mp:
            body = re.sub(r"ring (\w+) = 10009,(\([^)]*\)),dp;", lambda mm: f"ring {mm.group(1)} = (10009,ww),{mm.group(2)},dp; minpoly = {mp};", body)
        nm = f"dm_{jt}_{n}"; open(f"n16/dm/{nm}.sing", "w", newline=NL).write(body); jobs.append((dg, nm))
        percls[jt] = percls.get(jt, 0) + 1
jobs.sort()
open("n16/dm/jobs.txt", "w", newline=NL).write(NL.join(n for _, n in jobs) + NL)
from collections import Counter
print("jobs", len(jobs), sorted(Counter(d for d, _ in jobs).items()))
print("unparsed", len(bad), bad[:5])
