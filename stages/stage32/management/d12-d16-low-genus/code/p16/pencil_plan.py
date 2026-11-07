"""32R-69h pencil plan (h0 = 2, no fixed component, all m_j <= 1): greedy decompositions of mK - x so that no
'hidden' curve (D-curve Γ with x.Γ >= 2) is hidden in every decomposition; Singular critical-point scripts
(v2 ideals + c14 fibre tail) per decomposition.  usage (from stoll/): python p16/pencil_plan.py"""
import sys, json, os
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0, "fasth0")
import fasth0v2 as F
from script_v2 import script, _g
K, Cm, L = _g["K"], _g["Cm"], _g["L"]
Pn = np.array(L.D["Pn"], dtype=object)
H = json.load(open("fasth0/d16v2f_h0.json")); X = json.load(open("fasth0/d16_fix.json"))
R = json.load(open("../split/reps_d16.json"))["reps"]
TAIL = open("p16/crit_tail.sing").read()
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
plan = json.load(open("p16/plan.json")) if os.environ.get("NODES") else {}; jobs = []
for i, fx in X.items():
    if fx or H[i][1] != 2: continue
    x = np.array(R[int(i)]["x"], dtype=np.int64); pe = Pn.dot(x.astype(object))
    if (max(pe[92:]) >= 2) != bool(os.environ.get("NODES")) or i in plan: continue
    m0, h, D0 = H[i]; D0 = {int(k): v for k, v in D0.items()}
    danger = lambda D: sorted(k for k in D if k <= 92 and pe[k - 1] >= 2)
    decs = [(m0, D0)]; bad = set(danger(D0)); tries = 0
    while bad and tries < 6:
        tries += 1; best = None
        for m in (1, 2, 3):
            D = decomp(x, m, bad)
            if D is None or F.h0(m, comps(D)) != 2: continue
            nb = bad & set(danger(D))
            if best is None or len(nb) < len(best[2]): best = (m, D, nb)
        if best is None or best[2] == bad: break
        decs.append(best[:2]); bad = best[2]
    plan[i] = {"pa": 1 + (int(R[int(i)]["C2"]) + 16) // 2, "decs": [[m, {str(k): v for k, v in D.items()}, danger(D)] for m, D in decs], "always_hidden": sorted(bad)}
    for t, (m, D) in enumerate(decs):
        s = script(D, m); s = s[:s.index("ideal B = std(S + Lsys);")]
        open(f"p16/c_{i}_{t}.sing", "w", newline="\n").write(s + TAIL); jobs.append(f"c_{i}_{t}")
json.dump(plan, open("p16/plan.json", "w"))
open("p16/jobs_n.txt" if os.environ.get("NODES") else "p16/jobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
from collections import Counter
print("pencils", len(plan), "jobs", len(jobs), "decs per pencil", Counter(len(p["decs"]) for p in plan.values()))
print("pencils with a curve hidden in every decomposition:", [(i, p["always_hidden"]) for i, p in plan.items() if p["always_hidden"]][:20])
