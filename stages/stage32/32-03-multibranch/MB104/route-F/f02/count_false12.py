"""How many of the birational omega<=cut T of f02_spectrum (4,4) were false (borderline, exact omega larger)?
Recomputes, for each changed record with float omega <= cut, the floating-point T exactly as the run did and its
birationality degree as the run did. usage: python -I -O count_false12.py 4 4"""
import json, os, sys
from collections import Counter
from multiprocessing import Pool
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f02_spectrum as F2
F1 = F2.F1
_D = {}
def init(a, b):
    A, B = F2.maps_of_degree(a), F2.maps_of_degree(b)
    _D.update(a=a, A=A, B=B, Ad=[F1.map_data(*m) for m in A], Bd=[F1.map_data(*m) for m in B])
def one(c):
    a = _D["a"]; X1 = np.array([p for p, _ in _D["Ad"][c["ia"]]]); Xq = np.array([p for p, _ in _D["Bd"][c["ib"]]])
    s, t = c["s"], c["t"]
    T = F2.frame(Xq[t[0]], Xq[t[1]], Xq[t[2]]) @ np.linalg.inv(F2.frame(X1[s[0]], X1[s[1]], X1[s[2]]))
    T = T / np.linalg.norm(T)
    return tuple(c["float"]), F2.bir_degree(a, *_D["A"][c["ia"]], *_D["B"][c["ib"]], T)
if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2]); cut = F2.CUT[(a, b)]
    ch = [c for c in json.load(open(os.path.join(HERE, f"amb{a}x{b}_changed.json"))) if c["float"][0] <= cut]
    with Pool(11, initializer=init, initargs=(a, b)) as p: r = p.map(one, ch, chunksize=50)
    cnt = Counter((f, bd == 1) for f, bd in r)
    print(json.dumps({"changed_with_float_omega_le_cut": len(ch),
                      "by_float_omega_and_birational": [[list(k[0]), k[1], v] for k, v in sorted(cnt.items())]}))
