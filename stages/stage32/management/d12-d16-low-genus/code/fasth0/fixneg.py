import json, sys, collections
import numpy as np
REPO = "C:/Users/fizaw/claudework/perfect-cuboid-game"
sys.path.insert(0, REPO + "/stages/stage32/management/d10-low-genus/enumeration")
import slice_lib as L
L.load(REPO)
Gn = np.array([[int(v) for v in r] for r in L.D["Gn"].tolist()], dtype=np.int64)
Cn = np.array([[int(v) for v in L.D["Cn"][i]] for i in range(140)], dtype=np.int64)
reps = json.load(open("d16_reps_full.json"))["reps"]
F = json.load(open("fasth0/d16_fix.json"))
C = collections.Counter(); rest = {}
for k, fx in F.items():
    if not fx: continue
    x = np.array(reps[int(k)]["x"], dtype=np.int64)
    v = {K: int(x @ Gn @ Cn[K-1]) for K in fx}
    if any(t < 0 for t in v.values()): C["some x.K<0"] += 1
    else: C["all x.K>=0"] += 1; rest[k] = v
print(dict(C)); print(list(rest.items())[:15])
json.dump(rest, open("fasth0/d16_fix_rest.json", "w"))
