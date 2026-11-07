"""32R-69h: per pencil, H = ∩_D (∪ hidden curves of D) minus the nodes must be empty (char p; incidences can only
grow mod p).  Writes n16/h_<i>.sing and n16/hjobs.txt."""
import json, sys
sys.path.insert(0, "fasth0")
from script_v2 import _g
CURVES = _g["CURVES"]
plan = json.load(open("n16/plan.json")); jobs = []
hdr = 'LIB "elim.lib";\nring R = 10009,(a1,a2,a3,b1,b2,b3,c),dp; number z = 792;\nideal S = a1^2+a2^2-b3^2, a2^2+a3^2-b1^2, a1^2+a3^2-b2^2, a1^2+a2^2+a3^2-c^2;\n'
hdr += 'ideal NODES = std(S + minor(jacob(S), 4));\n'   # 32R-69j: the 48 nodes (S + (a1*...*c) was a degree-112 curve)
for i, p in plan.items():
    s = hdr; parts = []
    for t, (m, D, hid) in enumerate(p["decs"]):
        if not hid: parts = None; break
        s += f"ideal U{t} = intersect(" + ",".join(f"std(S + ideal({','.join(CURVES[k-1])}))" for k in hid) + ");\n" if len(hid) > 1 else f"ideal U{t} = std(S + ideal({','.join(CURVES[hid[0]-1])}));\n"
        parts.append(f"U{t}")
    if parts is None:
        s += '"HIDDEN-EMPTY (a decomposition with no hidden curve)";\nquit;\n'
    else:
        s += "ideal HH = std(" + " + ".join(parts) + ");\n"
        s += 'def LL = sat(HH, NODES); ideal H2; if (typeof(LL) == "list") { H2 = std(LL[1]); } else { H2 = std(LL); }\n'
        s += '"hidden set off nodes: dim", dim(H2), " degree", mult(H2);\nif (dim(H2) <= 0) { "HIDDEN-EMPTY"; } else { "HIDDEN-NONEMPTY"; }\nquit;\n'
    open(f"n16/h_{i}.sing", "w", newline="\n").write(s); jobs.append(f"h_{i}")
open("n16/hjobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n"); print(len(jobs))
