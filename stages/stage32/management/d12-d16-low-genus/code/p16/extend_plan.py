"""32R-69h: for pencils whose hidden set H (p16/h_<i>.out) is non-empty, add decompositions penalising every curve
hidden so far (weights grow with the number of decompositions hiding it), up to 5 decompositions."""
import sys, json, re, os
import numpy as np
exec(open("p16/pencil_plan.py", encoding="utf-8").read().split("plan = json.load(open(\"p16/plan.json\")) if os.environ")[0])
plan = json.load(open("p16/plan.json")); newjobs = []
for i, p in plan.items():
    t = open(f"p16/h_{i}.out").read()
    mdim = re.search(r"dim (-?\d+)", t)
    if "no hidden curve" in t or (mdim and int(mdim.group(1)) <= 0): continue
    x = np.array(R[int(i)]["x"], dtype=np.int64); pe = Pn.dot(x.astype(object))
    danger = lambda D: sorted(k for k in D if k <= 92 and pe[k - 1] >= 2)
    cnt = {}
    for m, D, hid in p["decs"]:
        for k in hid: cnt[k] = cnt.get(k, 0) + 1
    v0 = len(p["decs"])
    while len(p["decs"]) < 5:
        best = None
        for m in (1, 2, 3):
            vv = m * K - x; w = np.ones(140)
            for k, c in cnt.items(): w[k - 1] = 100 ** c
            r = milp(c=w, constraints=[LinearConstraint(Cm.T.astype(float), vv.astype(float), vv.astype(float))],
                     integrality=np.ones(140), bounds=Bounds(0, np.array([4] * 92 + [3] * 48)))
            if not r.success: continue
            c = np.round(r.x).astype(np.int64)
            if not (c.dot(Cm) == vv).all(): continue
            D = {int(k) + 1: int(c[k]) for k in np.nonzero(c)[0]}
            if F.h0(m, comps(D)) != 2: continue
            sc = sum(100 ** cnt.get(k, 0) for k in danger(D))
            if best is None or sc < best[0]: best = (sc, m, D)
        if best is None: break
        _, m, D = best
        if any(set(D) == set({int(k) for k in d[1]}) for d in p["decs"]): break
        p["decs"].append([m, {str(k): v for k, v in D.items()}, danger(D)])
        for k in danger(D): cnt[k] = cnt.get(k, 0) + 1
        if not danger(D): break
    for tt in range(v0, len(p["decs"])):
        m, D, _ = p["decs"][tt]; D = {int(k): v for k, v in D.items()}
        s = script(D, m); s = s[:s.index("ideal B = std(S + Lsys);")]
        open(f"p16/c_{i}_{tt}.sing", "w", newline="\n").write(s + TAIL); newjobs.append(f"c_{i}_{tt}")
    if os.path.exists(f"p16/h_{i}.out"): os.remove(f"p16/h_{i}.out")
    print(i, "decs", len(p["decs"]), [d[2] for d in p["decs"]][v0:])
json.dump(plan, open("p16/plan.json", "w"))
open("p16/jobs_ext.txt", "w", newline="\n").write("\n".join(newjobs) + "\n"); print("new jobs", len(newjobs))
