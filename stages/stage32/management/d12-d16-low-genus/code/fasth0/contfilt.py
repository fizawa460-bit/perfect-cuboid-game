"""32R-69f fast containment prefilter for h0 = 1 reps: the unique member F of |mK - D| (v2 spaces, char p);
if F lies in V(Γ, c_Γ + 1) for a known curve Γ (1..92), the curve of class x contains Γ -> reducible.
usage: python contfilt.py H0JSON OUT NPROC   (H0JSON from judge_fast.py)"""
import sys, json, os
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
def init():
    global F; sys.path.insert(0, HERE); import fasth0v2 as _F; F = _F
def work(item):
    idx, (m, h, D) = item
    comps = [f"C{k}_{c}" if int(k) <= 92 else f"N{k}_{c}" for k, c in sorted(D.items(), key=lambda t: int(t[0]))]
    return idx, F.contained_curves(m, comps)
if __name__ == "__main__":
    H = json.load(open(sys.argv[1]))
    items = [(i, v) for i, v in H.items() if v[1] == 1]
    with Pool(int(sys.argv[3]), initializer=init) as pool:
        res = dict(pool.imap_unordered(work, items, chunksize=8))
    json.dump(res, open(sys.argv[2], "w"))
    red = [i for i, c in res.items() if c]
    print("h0=1 reps", len(items), "reducible (known curve in member)", len(red), "remaining", len(items) - len(red))
