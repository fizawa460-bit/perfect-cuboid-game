"""32R-69 fast judging for degree d: decomposition of mK - x (m = 1..3, multiplicities <= 3, HiGHS MILP with
mip_rel_gap = 1) + exact char-p h0 via fasth0. usage: python judge_fast.py REPSFILE OUTPREFIX NPROC
Writes OUTPREFIX_h0.json: {idx: [m, h0, {curve label: mult}]}; reps with no bounded decomposition get m = None."""
import sys, json, time, os
import numpy as np
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); ST = os.path.dirname(HERE)
def init():
    global K, Cm, F, milp, LinearConstraint, Bounds
    os.chdir(ST); sys.argv = ["x"]; g = {}
    exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
    K, Cm = g["K"], g["Cm"]
    from scipy.optimize import milp as _m, LinearConstraint as _L, Bounds as _B
    milp, LinearConstraint, Bounds = _m, _L, _B
    sys.path.insert(0, HERE); import fasth0v2 as _F; F = _F
def work(item):
    idx, x = item; x = np.array(x, dtype=np.int64)
    for mm in (1, 2, 3):
        v = mm * K - x
        r = milp(c=np.ones(140), constraints=[LinearConstraint(Cm.T.astype(float), v.astype(float), v.astype(float))],
                 integrality=np.ones(140), bounds=Bounds(0, 3), options={"mip_rel_gap": 1.0})
        if r.success:
            c = np.round(r.x).astype(np.int64)
            if (c.dot(Cm) == v).all():
                comps = [f"C{k+1}_{c[k]}" for k in range(92) if c[k] > 0] + [f"N{k+1}_{c[k]}" for k in range(92, 140) if c[k] > 0]
                return idx, [mm, int(F.h0(mm, comps)), {int(k) + 1: int(c[k]) for k in np.nonzero(c)[0]}]
    return idx, [None, None, None]
if __name__ == "__main__":
    reps, out, npr = sys.argv[1], sys.argv[2], int(sys.argv[3])
    R = json.load(open(reps))["reps"]
    t0 = time.time(); res = {}
    with Pool(npr, initializer=init) as pool:
        for k, (idx, v) in enumerate(pool.imap_unordered(work, [(i, r["x"]) for i, r in enumerate(R)], chunksize=64)):
            res[idx] = v
            if k % 20000 == 0: print(k, f"{time.time()-t0:.0f}s", flush=True)
    json.dump({str(k): v for k, v in sorted(res.items())}, open(out + "_h0.json", "w"))
    from collections import Counter
    print("h0 distribution:", sorted(Counter(v[1] for v in res.values()), key=str), Counter(v[1] for v in res.values()), f"{time.time()-t0:.0f}s")
