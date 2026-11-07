"""32R-69h stage 2: read p16/c_<i>_<t>.out; per pencil with nD decompositions and p_a, threshold
h = (p_a - 2) // nD + 1 (so nD (h - 1) <= p_a - 2 < p_a - 1 for every fibre below threshold in all
decompositions).  Fibres with per-fibre length >= h in some decomposition get a fast-genus job on the union of the
conjugate members (norm form N of the fibre factor; g >= (B + k - 1) / k for k conjugates).
usage (from stoll/): python p16/stage2.py  -> p16/s2_<i>_<t>_<j>.sing, p16/s2jobs.txt, p16/stage2.json"""
import json, re, os
plan = json.load(open("p16/plan.json"))
FAST = open("gfast/tail_fast.sing").read()
res, jobs = {}, []
for i, p in plan.items():
    nD = len(p["decs"]); pa = p["pa"]; h = (pa - 2) // nD + 1
    st = {"pa": pa, "nD": nD, "h": h, "decs": []}
    for t, (m, D, hid) in enumerate(p["decs"]):
        fn = f"p16/c_{i}_{t}.out"; o = open(fn).read() if os.path.exists(fn) else ""
        if "time" not in o: st["decs"].append("unfinished"); continue
        bad = None
        if "CRITCURVE-NOT-IN-FIBRE" in o: bad = "critical curve not in a fibre"
        elif not re.search(r"critical points with F1 = 0: dim (-1|0)\b", o): bad = "critical point with F1 = 0"
        elif not re.search(r"critical points on the chart hyperplane: dim (-1|0)\b", o): bad = "critical point on chart hyperplane"
        elif not re.search(r"dim ZU (0|-1)\b", o): bad = "ZU not finite"
        tot = re.search(r"critical points \(with multiplicity\): (\d+)", o); vd = re.search(r"vdim (-?\d+)", o)
        if bad is None and tot and vd and int(tot.group(1)) != int(vd.group(1)): bad = f"chart misses points {tot.group(1)} vs {vd.group(1)}"
        if bad: st["decs"].append("OPEN:" + bad); continue
        heavy = []
        lines = o.splitlines()
        for k, l in enumerate(lines):
            mm = re.match(r"fibre factor degree (\d+)  critical length (\d+)  per fibre (\d+)", l)
            if mm and int(mm.group(3)) >= h:
                fac = re.match(r"\s*factor: (.*)", lines[k + 1]).group(1).strip()
                heavy.append((int(mm.group(1)), int(mm.group(3)), fac))
        st["decs"].append({"maxlen": max([int(x) for x in re.findall(r"per fibre (\d+)", o)] or [0]), "heavy": heavy})
        src = open(f"p16/c_{i}_{t}.sing").read()
        pre = src[:src.index('system("random", 2718);')]
        pre += src[src.index('system("random", 2718);'):].split("\n", 1)[0] + "\n"
        cids = sorted(int(k) for k in D if int(k) <= 92)
        dc = ("intersect(" + ",".join(f"G{k}" for k in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
        for j, (deg, L, fac) in enumerate(heavy):
            body = pre + f"ideal Dc = std({dc});\n"
            body += f"ring RQ = 10009,(u),dp; poly qq = {fac}; int kq = deg(qq); matrix CQ = coeffs(qq, u);\nsetring R;\n"
            body += "poly NN = 0; int jq; for (jq = 0; jq <= kq; jq++) { NN = NN + number(imap(RQ, CQ)[jq + 1, 1]) * F0^jq * F1^(kq - jq); }\n"
            body += "ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == \"list\") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;\n"
            body += f'"union of {deg} conjugate member(s): residual dim", dim(Bp), " degree", mult(Bp), " expected", {16 * deg};\n'
            body += f'if (mult(Bp) < {16 * deg}) {{ "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }}\n'
            body += f'if (dim(Bp) != 2) {{ "MEMBER-NOT-CURVE"; quit; }}\n'
            nm = f"s2_{i}_{t}_{j}"; open(f"p16/{nm}.sing", "w", newline="\n").write(body + FAST); jobs.append(nm)
    res[i] = st
json.dump(res, open("p16/stage2.json", "w"), indent=0)
open("p16/s2jobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
from collections import Counter
print("stage-2 jobs", len(jobs)); print(Counter(d if isinstance(d, str) else "ok" for s in res.values() for d in s["decs"]))
