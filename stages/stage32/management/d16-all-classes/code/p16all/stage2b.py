# R2 p16/stage2b.py with paths p16 -> p16all (audit item 4(c), 2026-11-09)
"""32R-69k stage 2b: fast-genus jobs on the special members found by the node analysis (n_ branch values; nt_
direct version for the 9 'tangent' pencils), the hidden-point search (hp_) and the member F1 (u = infinity) of every
pencil with node / hidden analysis.  All factors are in u = F0/F1 with the basis of c_<i>_0.
Member union of k conjugates: g >= (B + k - 1) / k, B = fast lower bound of p_a - sum(delta)."""
import json, re, os, glob
from collections import defaultdict
NL = chr(10)
plan = json.load(open("p16all/plan.json")); FAST = open("gfast/tail_fast.sing").read()
fac = defaultdict(set); src_of = defaultdict(set); opens = []
tangent = {re.match(r"nt_(\d+_\d+_\d)", os.path.basename(f)).group(1) for f in glob.glob("p16all/nt_*.sing")}
for f in glob.glob("p16all/n_*_*_*.out"):
    b = re.match(r"n_(\d+_\d+_\d)\.out", os.path.basename(f)).group(1); i = b.split("_")[0]
    t = open(f).read(); src = f"p16all/nt_{b}.out" if b in tangent else f
    t = open(src).read() if os.path.exists(src) else ""
    if "NODE-NONE" in t: continue
    if "NODE-OPEN" in t or "special t" not in t: opens.append((b, "node")); continue
    for x in re.findall(r"special factor: (.*)", t): fac[i].add(x.strip().replace("tt", "u")); src_of[i].add("node")
for f in glob.glob("p16all/hp_*.out"):
    i = re.match(r"hp_(\d+)\.out", os.path.basename(f)).group(1); t = open(f).read()
    if "HIDDEN-MOVING-BASEPOINT" in t: src_of[i].add("hidden(base points simple)"); continue
    if "HIDDEN-CHART" in t or "hidden fibre values" not in t: opens.append((i, "hidden")); continue
    for x in re.findall(r"special factor: (.*)", t): fac[i].add(x.strip()); src_of[i].add("hidden")
jobs = []
for i in sorted(set(fac) | set(src_of), key=int):
    s0 = open(f"p16all/c_{i}_0.sing").read()
    pre = s0[:s0.index('system("random", 2718);')] + s0[s0.index('system("random", 2718);'):].split(NL, 1)[0] + NL
    m, D, hid = plan[i]["decs"][0]
    cids = sorted(int(k) for k in D if int(k) <= 92)
    dc = ("intersect(" + ",".join(f"G{k}" for k in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
    items = sorted(fac[i]) + ["F1"]
    for j, q in enumerate(items):
        L = [pre + f"ideal Dc = std({dc});"]
        if q == "F1":
            L.append("int kq = 1; poly NN = F1;")
        else:
            L.append(f"ring RQ = 10009,(u),dp; poly qq = {q}; int kq = deg(qq); matrix CQ = coeffs(qq, u);")
            L.append("setring R; poly NN = 0; int jq; for (jq = 0; jq <= kq; jq++) { NN = NN + number(imap(RQ, CQ)[jq + 1, 1]) * F0^jq * F1^(kq - jq); }")
        L.append('ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;')
        L.append('"special member(s): k", kq, " residual dim", dim(Bp), " degree", mult(Bp), " expected", 16 * kq;')
        L.append('if (mult(Bp) < 16 * kq) { "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }')
        L.append('if (dim(Bp) != 2) { "MEMBER-NOT-CURVE"; quit; }')
        nm = f"sb_{i}_{j}"; open(f"p16all/{nm}.sing", "w", newline=NL).write(NL.join(L) + NL + FAST); jobs.append(nm)
open("p16all/sbjobs.txt", "w", newline=NL).write(NL.join(jobs) + NL)
json.dump({"factors": {i: sorted(v) for i, v in fac.items()}, "sources": {i: sorted(v) for i, v in src_of.items()}, "open": opens}, open("p16all/stage2b.json", "w"), indent=0)
print("pencils", len(set(fac) | set(src_of)), "jobs", len(jobs), "open", opens[:10])
