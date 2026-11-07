"""32R-70: compare a symmetry-broken rep list with the old pe-lexmax reps (same orbits?)."""
import sys, json, numpy as np
new = np.loadtxt(sys.argv[1], dtype=np.int64, ndmin=2)
old_keys = list(json.load(open(sys.argv[3])).keys()) if len(sys.argv) > 3 else None
R = json.load(open(sys.argv[2]))["reps"]
oldx = [R[int(i)]["x"] for i in old_keys] if old_keys else [r["x"] for r in R]
S = json.load(open("symz_d16.json")); G = np.array(S["perms"], dtype=np.int64)
sys.path.insert(0, "../stoll/fasth0")
from script_v2 import _g
P140 = np.array([[int(v) for v in _g["L"].D["Pn"][k]] for k in range(140)], dtype=np.int64)
def canon(x):
    pe = P140.dot(np.array(x, dtype=np.int64)); im = pe[G]          # |G| x 140
    best = max(map(tuple, im)); return best
A = {canon(x) for x in new}; B = {canon(x) for x in oldx}
print("new", len(new), "distinct orbits", len(A), "old", len(oldx), "distinct", len(B), "equal sets:", A == B)
