"""32R-69h fixed-component filter for h0 >= 2 reps: if h0(D + Γ) = h0(D) for a known curve Γ (1..92, mult+1 <= 4)
or an exceptional curve E_k (node power+1 <= 3), every member of |x| contains Γ -> no irreducible member.
usage: python fixfilt.py H0JSON OUT NPROC"""
import sys, json, os
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
def init():
    global F; sys.path.insert(0, HERE); import fasth0v2 as _F; F = _F
def work(item):
    idx, (m, h, D) = item
    D = {int(k): int(c) for k, c in D.items()}
    def comps(DD): return [f"C{k}_{c}" if k <= 92 else f"N{k}_{c}" for k, c in sorted(DD.items()) if c > 0]
    assert F.h0(m, comps(D)) == h
    fixed = []
    for k in range(1, 141):
        c1 = D.get(k, 0) + 1
        if c1 > (4 if k <= 92 else 3): continue
        D2 = dict(D); D2[k] = c1
        if F.h0(m, comps(D2)) == h: fixed.append(k)
    return idx, fixed
if __name__ == "__main__":
    H = json.load(open(sys.argv[1]))
    items = [(i, v) for i, v in H.items() if v[1] is not None and v[1] >= 2]
    with Pool(int(sys.argv[3]), initializer=init) as pool:
        res = dict(pool.imap_unordered(work, items, chunksize=4))
    json.dump(res, open(sys.argv[2], "w"))
    fx = [i for i, c in res.items() if c]
    print("h0>=2 reps", len(items), "with a fixed known/exceptional curve", len(fx), "remaining", len(items) - len(fx))
    print("fixed only exceptional:", sum(1 for c in res.values() if c and all(k > 92 for k in c)))
