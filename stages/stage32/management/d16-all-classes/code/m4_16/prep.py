"""d=16 all-class judge (s16allmu -> j16all): the one class with no m <= 3 decomposition (out_348 line 1).
Same m = 4 test as m4_18/prep.py (32R-89): MILP 4K - x = sum c_k, then h0 of |4K - D| mod p (h0_p >= h0 in char 0).
usage (from stoll/): python m4_16/prep.py"""
import sys, numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0, "fasth0")
from script_v2 import script, _g
K, Cm = _g["K"], _g["Cm"]
x = np.array(list(map(int, open("//wsl.localhost/Ubuntu/root/s16allmu/out_348.txt").readline().split())), dtype=np.int64)
print("len x", len(x), "K.x-type check len K", len(K))
v = 4 * K - x
r = milp(c=np.ones(140), constraints=[LinearConstraint(Cm.T.astype(float), v.astype(float), v.astype(float))],
         integrality=np.ones(140), bounds=Bounds(0, np.array([6] * 92 + [5] * 48)))
print("milp", r.success)
c = np.round(r.x).astype(np.int64); assert (c.dot(Cm) == v).all()
D = {int(k) + 1: int(c[k]) for k in np.nonzero(c)[0]}
print("D", D)
s = script(D, 4); s = s[:s.index("ideal B = std(S + Lsys);")] + "quit;\n"
open("m4_16/h_348_1.sing", "w", newline="\n").write(s)
