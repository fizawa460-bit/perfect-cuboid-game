"""d = 16 ALL reps, new classes (not among the unibranch-compatible reps of R2), h0 = 2; input /root/j16all_new_h0pos.txt.
No odd-contact filter is used (32R-83 is valid for unibranch curves only).  Derived from p18/prep_all.py (32R-85):
fixed-component check (fixfilt rule; then checked in char 0 by p16all/mkfix0.py), decompositions as p16/pencil_plan.py
(several decompositions to shrink the hidden curves), critical scripts p16all/c_<i>_<t>.sing with the tail
p16/crit_tail_v6.sing.  usage (from stoll/): python p16all/prep_all.py"""
import sys, json, random
ARGV = sys.argv[1:]
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0, "fasth0")
import fasth0v2 as F
from script_v2 import script, _g
K, Cm, L = _g["K"], _g["Cm"], _g["L"]
Pn = np.array(L.D["Pn"], dtype=object); Gn = np.array(L.D["Gn"], dtype=np.int64)
TAIL = open("p16/crit_tail_v6.sing").read()
LN = [l.split(chr(9)) for l in open("//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt").read().split(chr(10))[:-1]]
J = [t[2] for t in LN]
pick = [k for k, l in enumerate(J) if l.split()[1] == "2"]
fixlist = []
Xs = {k: np.array(list(map(int, LN[k][1].split())), dtype=np.int64) for k in pick}
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
plan = {}; jobs = []; nfix = 0
for i in pick:
    t = J[i].split(); m0 = int(t[0]); D0 = {int(a): int(b) for a, b in (q.split(":") for q in t[2].split(","))}
    assert F.h0(m0, comps(D0)) == 2
    fixed = False
    for k in range(1, 141):
        c1 = D0.get(k, 0) + 1
        if c1 > (4 if k <= 92 else 3): continue
        D2 = dict(D0); D2[k] = c1
        if F.h0(m0, comps(D2)) == 2: fixed = True; break
    if fixed: nfix += 1; fixlist.append([i, k]); continue
    x = Xs[i]; pe = Pn.dot(x.astype(object))
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
    C2 = int(x.dot(Gn).dot(x))
    plan[str(i)] = {"pa": 1 + (C2 + 16) // 2, "C2": C2, "nodes2": bool(max(pe[92:]) >= 2),
                    "decs": [[m, {str(k): v for k, v in D.items()}, danger(D)] for m, D in decs], "always_hidden": sorted(bad)}
    for t_, (m, D) in enumerate(decs):
        s = script(D, m); s = s[:s.index("ideal B = std(S + Lsys);")]
        open(f"p16all/c_{i}_{t_}.sing", "w", newline="\n").write(s + TAIL); jobs.append(f"c_{i}_{t_}")
json.dump(plan, open("p16all/plan.json", "w")); json.dump(fixlist, open("p16all/fixed.json", "w"))
open("p16all/jobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
from collections import Counter
print("pencils in", len(pick), "fixed", nfix, "pencils", len(plan), "jobs", len(jobs), Counter(len(p["decs"]) for p in plan.values()),
      "nodes2", sum(p["nodes2"] for p in plan.values()), "pa", Counter(p["pa"] for p in plan.values()))
