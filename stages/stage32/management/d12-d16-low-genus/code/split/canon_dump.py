"""32R-70: dump P140, perms and old d18 x-list for the C canonicalizer."""
import json, sys, numpy as np
ARGV = list(sys.argv)
sys.path.insert(0, "../stoll/fasth0")
from script_v2 import _g
P140 = np.array([[int(v) for v in _g["L"].D["Pn"][k]] for k in range(140)], dtype=np.int64)
G = np.array(json.load(open("symz_d16.json"))["perms"], dtype=np.int64)
with open("/c/Users/fizaw/claudework/stage32_research/split/canon_tab.txt" if False else "canon_tab.txt", "w") as f:
    f.write(f"{P140.shape[0]} {P140.shape[1]} {G.shape[0]}\n")
    for r in P140: f.write(" ".join(map(str, r)) + "\n")
    for r in G: f.write(" ".join(map(str, r)) + "\n")
R = json.load(open(ARGV[1]))["reps"]
with open(ARGV[2], "w") as f:
    for r in R: f.write(" ".join(map(str, r["x"])) + "\n")
print("old", len(R))
