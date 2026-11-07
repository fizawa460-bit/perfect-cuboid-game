"""32R-69c: parallel v2 recheck of the d = 18 fast-judge results (same decompositions)."""
import sys, os, json
from multiprocessing import Pool
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def init():
    global F
    sys.path.insert(0, HERE); import fasth0v2 as _F; F = _F
def work(item):
    i, (m, h0v, D) = item
    if m is None: return i, h0v, None
    comps = [f"C{k}_{c}" for k, c in D.items() if int(k) <= 92] + [f"N{k}_{c}" for k, c in D.items() if int(k) > 92]
    if any((c, m) not in F.ANN for c in comps): return i, h0v, "skip"
    return i, h0v, int(F.h0(m, comps))
if __name__ == "__main__":
    H = json.load(open(os.path.join(HERE, "d18_h0.json")))
    out = {}; res = Counter()
    with Pool(10, initializer=init) as pool:
        for i, old, new in pool.imap_unordered(work, list(H.items()), chunksize=256):
            out[i] = new; res[(old, new)] += 1
    json.dump(out, open(os.path.join(HERE, "d18_h0_v2.json"), "w"))
    print(dict(res))
    print("old 0 -> new >= 1:", sum(v for (o, n), v in res.items() if o == 0 and isinstance(n, int) and n >= 1))
