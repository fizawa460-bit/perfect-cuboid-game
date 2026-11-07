"""32R-71: can cheap numbers predict the d=16 detailed-survey outcomes?  (exploration)"""
import sys, os, json
from collections import Counter
sys.argv = ["x"]
ST = "C:/Users/fizaw/claudework/stage32_research/stoll"; os.chdir(ST); g = {}
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
import numpy as np
Gn = np.array(g["Gn"], dtype=np.int64); K = g["K"]; Cm = g["Cm"]
print("check K.C = deg>0:", (Cm.dot(Gn).dot(K) > 0).sum(), "self-int of nodes", set(np.einsum("ij,jk,ik->i", Cm[92:], Gn, Cm[92:])))
print("C^2 of curves", Counter(np.einsum("ij,jk,ik->i", Cm[:92], Gn, Cm[:92]).tolist()))
R = json.load(open("../split/reps_d16.json"))["reps"]
H = json.load(open("fasth0/d16v2f_h0.json")); CT = json.load(open("fasth0/d16v2f_cont.json"))
X = np.array([R[int(i)]["x"] for i in H], dtype=np.int64)
I = X.dot(Gn).dot(Cm.T)        # x . Gamma
neg = (I < 0).any(1)
keys = list(H)
h1 = [k for k, i in zip(keys, range(len(keys))) if H[k][1] == 1]
pos = {k: n for n, k in enumerate(keys)}
red = {k for k, v in CT.items() if v}
a = Counter((k in red, bool(neg[pos[k]])) for k in h1)
print("h0=1: (form-containment reducible, numeric x.G<0)", a)
print("all reps with some x.G<0 by h0:", Counter(H[k][1] for k in keys if neg[pos[k]]))
