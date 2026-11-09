"""d = 16 all reps (s16allmu -> j16all), classes NOT among the unibranch-compatible reps (/root/s16sym), h0 = 1.
Same method as d18/prep_h1.py (32R-82) WITHOUT the odd-contact filter (32R-83 is valid for unibranch curves only):
mu filter already applied (mupre), all x.E >= 0, containment prefilter, fast-genus scripts.
Input /root/j16all_new_h0pos.txt: chunk TAB x TAB judge line.  usage (from stoll/): python d16all/prep_h1.py NPROC"""
import sys, json
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, "fasth0")
def init():
    global F; import fasth0v2 as _F; F = _F
def cont(item):
    k, m, comps = item
    return k, F.contained_curves(m, comps)
if __name__ == "__main__":
    NP = int(sys.argv[1])
    L = [l.split("\t") for l in open("//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt").read().split("\n")[:-1]]
    X = np.array([list(map(int, t[1].split())) for t in L], dtype=np.int64); J = [t[2] for t in L]
    rows = [list(map(int, l.split())) for l in open("mu1820/emat.txt")]
    deg = np.array(rows[0]); W = np.array(rows[1:]).T
    assert (X @ deg == 16).all()
    P = X @ W; mu = P.sum(1); mn = P.min(1)
    print("new classes h0>0:", len(L), " h0=1:", sum(j.split()[1] == "1" for j in J), " min x.E < 0:", int((mn < 0).sum()),
          " mu < 18:", int((mu < 18).sum()))
    sel = [k for k, l in enumerate(J) if l.split()[1] == "1" and mn[k] >= 0 and mu[k] >= 18]
    print("h0=1 with x.E >= 0, mu >= 18:", len(sel))
    items = []
    for k in sel:
        t = J[k].split(); D = {int(a): int(b) for a, b in (q.split(":") for q in t[2].split(","))}
        items.append((k, int(t[0]), [f"C{i}_{c}" if i <= 92 else f"N{i}_{c}" for i, c in sorted(D.items())]))
    with Pool(NP, initializer=init) as pool:
        res = dict(pool.imap_unordered(cont, items, chunksize=16))
    json.dump({str(k): v for k, v in res.items()}, open("d16all/h1_cont.json", "w"))
    from script_v2 import script
    FAST = open("gfast/tail_fast_v2.sing").read(); END = " }\nquit;\n"
    jobs = []
    for k, m, comps in items:
        if res[k]: continue
        t = J[k].split(); D = {int(a): int(b) for a, b in (q.split(":") for q in t[2].split(","))}
        s = script(D, m); assert s.endswith(END)
        open(f"d16all/h1/t_{k}.sing", "w", newline="\n").write(s[:-len(END)] + FAST + "\n" + END); jobs.append(f"t_{k}")
    open("d16all/h1/jobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
    print("contained (reducible):", len(items) - len(jobs), " genus jobs:", len(jobs))
