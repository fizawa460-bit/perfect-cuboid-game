"""32R-71 d=18 sample stage 2 with fibre matching: read c_<i>_<t>.out (same OPEN checks as p16/stage2.py) and the
Moebius maps m_<i>.out; fibre classes over all decompositions; a class needs a member job iff
sum_t L_t >= p_a - 1.  One member job per needed class (stage2x body, expected degree DEG).
32R-85 copy for d=18 production: a fibre that the Moebius map sends to w = infinity (the F1 = 0 fibre of dec 0)
is kept as class "inf" and always gets a member job (conservative; dec 0 does not list that fibre).
usage (from stoll/): DIR=p18 python p18/stage2m.py  -> p18s/sx_<i>_<k>.sing, p18s/sxjobs.txt, p18s/stage2m.json"""
import json, re, os, sys
sys.path.insert(0, "p16/mob2")
from collections import defaultdict
DIR = os.environ.get("DIR", "p18s"); DEG = 16; NL = "\n"; p = 10009
_m = open("p16/mob2/match.py").read()
exec(_m[_m.index("def parse_poly"):_m.index("def cfacs")])          # parse_poly, pmul, monic, mobmap
FAST = open("gfast/tail_fast_v2.sing").read()
plan = json.load(open(DIR + "/plan.json"))
def cf(i, t):
    L = open(f"{DIR}/c_{i}_{t}.out").read().splitlines(); pr = []; un = set()
    for k, l in enumerate(L):
        m = re.match(r"fibre factor degree (\d+)  critical length (\d+)  per fibre (\d+)", l)
        if not m: continue
        dg, per = int(m.group(1)), int(m.group(3))
        if per >= 2:
            f = parse_poly(re.match(r"\s*factor: (.*)", L[k + 1]).group(1).strip()); pr.append((dg, per, monic(f)))
        else: un.add(dg)
    for l in L:
        m = re.match(r"fibre factor degree (\d+)  critical length at most", l)
        if m: un.add(int(m.group(1)))
    return pr, un
def openchk(o):
    if "time" not in o: return "unfinished"
    if "CRITCURVE-NOT-IN-FIBRE" in o: return "OPEN:critical curve not in a fibre"
    if not re.search(r"critical points with F1 = 0: dim (-1|0)\b", o): return "OPEN:F1=0"
    if not re.search(r"critical points on the chart hyperplane: dim (-1|0)\b", o): return "OPEN:chart"
    if not re.search(r"dim ZU (0|-1)\b", o): return "OPEN:ZU not finite"
    tot = re.search(r"critical points \(with multiplicity\): (\d+)", o); vd = re.search(r"vdim (-?\d+)", o)
    if tot and vd and int(tot.group(1)) != int(vd.group(1)): return "OPEN:chart misses points"
    vz = int(re.search(r"dim ZU \S+  vdim (\d+)", o).group(1))
    if "FIBRE-LOOP-DONE" not in o and sum(int(x) for x in re.findall(r"critical length (\d+)", o)) != vz: return "INCOMPLETE fibre loop"
    return None
res = {}; jobs = []; MAP = {}
for i, P in plan.items():
    nD = len(P["decs"]); pa = P["pa"]
    outs = [open(f"{DIR}/c_{i}_{t}.out").read() if os.path.exists(f"{DIR}/c_{i}_{t}.out") else "" for t in range(nD)]
    st = [openchk(o) for o in outs]
    if any(st): res[i] = {"status": st}; continue
    mo = open(f"{DIR}/m_{i}.out").read() if os.path.exists(f"{DIR}/m_{i}.out") else ""
    if nD > 1 and "time ms" not in mo: res[i] = {"status": "mob pending"}; continue
    M = {0: (1, 0, 0, 1)}
    for t in range(1, nD):
        if int(re.search(rf"MOBCOUNT {t} (\d+)", mo).group(1)) != 1: break
        c_, d_, ma, mb = map(int, re.search(rf"MOB {t} (\S+) (\S+) (\S+) (\S+)", mo).groups())
        M[t] = ((-ma) % p, (-mb) % p, c_ % p, d_ % p)
    if len(M) < nD: res[i] = {"status": "OPEN:no unique Moebius"}; continue
    inv = lambda m: (m[3], (-m[1]) % p, (-m[2]) % p, m[0])
    Fc = {t: cf(i, t) for t in range(nD)}
    cls = defaultdict(dict); rep = {}
    for t in range(nD):
        for dg, L, f in Fc[t][0]:
            g = mobmap(list(f), *inv(M[t]))
            if g is None: assert dg == 1, (i, t, f); g = "inf"
            else: g = tuple(g)
            cls[g][t] = L; rep.setdefault(g, (t, f))
    need = []
    for g, D in cls.items():
        if g == "inf": dg = 1; S_ = max(pa - 1, sum(D.values()))
        else: dg = len(g) - 1; S_ = sum(D.get(t, 1 if dg in Fc[t][1] else 0) for t in range(nD))
        if S_ >= pa - 1: need.append((dg, S_, rep[g]))
    res[i] = {"status": "ok", "pa": pa, "classes": len(cls), "need": [(a, b) for a, b, _ in need]}
    srcc = open(f"{DIR}/c_{i}_0.sing").read()
    for k, (dg, S_, (t, f)) in enumerate(need):
        src = open(f"{DIR}/c_{i}_{t}.sing").read(); kk = src.index('system("random", ')
        pre = src[:kk] + src[kk:].split(NL, 1)[0] + NL
        Dd = P["decs"][t][1]; cids = sorted(int(x) for x in Dd if int(x) <= 92)
        dc = ("intersect(" + ",".join(f"G{x}" for x in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
        body = pre + f"ideal Dc = std({dc});" + NL
        fac = "+".join(f"({c})*ww^{e}" for e, c in enumerate(f) if c)
        if dg == 1:
            body += f"poly NN = F0 - ({(-f[0]) % p}) * F1;" + NL
        else:
            body += "poly NN = F0 - ww * F1;" + NL
        body += 'ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;' + NL
        body += f'"heavy member: factor degree {dg}, summed length {S_}; residual dim", dim(Bp), " degree", mult(Bp), " expected {DEG}";' + NL
        body += f'if (mult(Bp) < {DEG}) {{ "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }}' + NL
        body += 'if (dim(Bp) != 2) { "MEMBER-NOT-CURVE"; quit; }' + NL + FAST
        if dg >= 2:
            body = re.sub(r"ring (\w+) = 10009,(\([^)]*\)),dp;", lambda mm: f"ring {mm.group(1)} = (10009,ww),{mm.group(2)},dp; minpoly = {fac};", body)
        nm = f"sx_{i}_{k}"; MAP[nm] = (i, t, P["decs"][t][0], P["decs"][t][1]); jobs.append((dg, nm))
json.dump(MAP, open(DIR + "/sxmap.json", "w"))
