"""32R-72 d=16 nets: basic data (C2, p_a, node incidences, danger curves) for the 23 open nets."""
import sys, json
import numpy as np
sys.path.insert(0, "fasth0")
from script_v2 import _g
L = _g["L"]; Pn = np.array(L.D["Pn"], dtype=object); Gn = np.array(L.D["Gn"], dtype=np.int64)
H = json.load(open("fasth0/d16v2f_h0.json")); R = json.load(open("../split/reps_d16.json"))["reps"]
for i in json.load(open("n16/nets.json")):
    x = np.array(R[int(i)]["x"], dtype=np.int64); pe = Pn.dot(x.astype(object)); C2 = int(x.dot(Gn).dot(x))
    m, h, D = H[i]
    print(i, "h0", h, "m", m, "C2", C2, "pa", 1 + (C2 + 16) // 2, "x.G>=2:", sorted(k + 1 for k in range(92) if pe[k] >= 2),
          "nodes>=1:", sum(1 for k in range(92, 140) if pe[k] >= 1), "max node", max(pe[92:]), "min x.G", min(pe))
