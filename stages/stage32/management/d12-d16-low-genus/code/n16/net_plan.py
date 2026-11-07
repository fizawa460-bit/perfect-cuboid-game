"""32R-72 d=16 net plan: decompositions of mK - x (h0 = 3 or 4, as p16/pencil_plan.py) so that no curve with x.G >= 2
is hidden in every decomposition; Singular scripts n16/e_<i>_<t>.sing = script_v2 prefix + n16/net_tail_c.sing.
THR = ceil((p_a - 1) / nD): a member of genus <= 1 needs delta >= p_a - 1, so some decomposition sees >= THR.
usage (from stoll/): python n16/net_plan.py"""
import sys, json
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0, "fasth0")
import fasth0v2 as F
from script_v2 import script, _g
K, Cm, L = _g["K"], _g["Cm"], _g["L"]
Pn = np.array(L.D["Pn"], dtype=object); Gn = np.array(L.D["Gn"], dtype=np.int64)
H = json.load(open("fasth0/d16v2f_h0.json")); R = json.load(open("../split/reps_d16.json"))["reps"]
TAIL = open("n16/net_tail_c.sing").read()
def comps(D): return [f"C{k}_{c}" if k <= 92 else f"N{k}_{c}" for k, c in sorted(D.items()) if c > 0]
def decomp(x, m, penal):
    v = m * K - x
    w = np.ones(140); w[[k - 1 for k in penal]] = 1000
    r = milp(c=w, constraints=[LinearConstraint(Cm.T.astype(float), v.astype(float), v.astype(float))],
             integrality=np.ones(140), bounds=Bounds(0, np.array([4] * 92 + [3] * 48)))
    if not r.success: return None
    c = np.round(r.x).astype(np.int64)
    if not (c.dot(Cm) == v).all(): return None
    return {int(k) + 1: int(c[k]) for k in np.nonzero(c)[0]}
plan = {}; jobs = []
for i in json.load(open("n16/nets.json")):
    x = np.array(R[int(i)]["x"], dtype=np.int64); pe = Pn.dot(x.astype(object)); C2 = int(x.dot(Gn).dot(x))
    m0, h, D0 = H[i]; D0 = {int(k): v for k, v in D0.items()}
    danger = lambda D: sorted(k for k in D if k <= 92 and pe[k - 1] >= 2)
    decs = [(m0, D0)]; bad = set(danger(D0)); tries = 0
    while bad and tries < 6:
        tries += 1; best = None
        for m in (1, 2, 3):
            D = decomp(x, m, bad)
            if D is None or F.h0(m, comps(D)) != h: continue
            nb = bad & set(danger(D))
            if best is None or len(nb) < len(best[2]): best = (m, D, nb)
        if best is None or best[2] == bad: break
        decs.append(best[:2]); bad = best[2]
    pa = 1 + (C2 + 16) // 2; thr = -(-(pa - 1) // len(decs))
    plan[i] = {"h0": h, "pa": pa, "C2": C2, "thr": thr, "decs": [[m, {str(k): v for k, v in D.items()}, danger(D)] for m, D in decs],
               "always_hidden": sorted(bad)}
    pars = "u,v" if h == 3 else "u,v,w"
    for t, (m, D) in enumerate(decs):
        s = script(D, m); s = s[:s.index("ideal B = std(S + Lsys);")]
        hdr = f'int HH = {h}; string PARS = "{pars}"; int THR = {thr}; string OUTF = "n16/e_{i}_{t}.txt";\n'
        open(f"n16/e_{i}_{t}.sing", "w", newline="\n").write(s + hdr + TAIL); jobs.append(f"e_{i}_{t}")
json.dump(plan, open("n16/plan.json", "w"))
open("n16/jobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
from collections import Counter
print("nets", len(plan), "jobs", len(jobs), "decs", Counter(len(p["decs"]) for p in plan.values()),
      "thr", Counter(p["thr"] for p in plan.values()))
print("always hidden:", [(i, p["always_hidden"]) for i, p in plan.items() if p["always_hidden"]])
