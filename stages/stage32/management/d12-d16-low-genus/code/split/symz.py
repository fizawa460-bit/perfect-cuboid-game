"""32R-70 symmetry on the y-part: matrices A_g (16x16) with z' = z A_g for every element g of the geometric group,
where x = z.pre + c.S (pre: 16x64, S = sat: 48x64) and g acts on x through the 140 intersection numbers.
usage: python symz.py d  -> symz_d{d}.json (integral check)"""
import sys, json
args = sys.argv[1:]; sys.argv = ["x"]
exec(open("../scripts/32R-59_split_enum.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0])
import numpy as np
from flint import fmpq_mat, fmpq, fmpz_mat
pre_ = [[int(v) for v in r] for r in pre]
S_ = [[int(v) for v in r] for r in sat]
P140 = [[int(v) for v in L.D["Pn"][k]] for k in range(140)]
print("pre", len(pre_), len(pre_[0]), "S", len(S_), len(S_[0]))
B = fmpq_mat(pre_ + S_)                     # 64 x 64, rows = basis
Binv = B.inv()
P = fmpq_mat(P140)                          # 140 x 64
# left inverse of P: (P^T P)^{-1} P^T
Pt = P.transpose(); PL = (Pt * P).inv() * Pt
gens = [tuple(p) for p in json.load(open("../stoll/geo_perms.json"))["perms"]]
G = {tuple(range(140))}; fr = list(G)
while fr:
    nf = []
    for a in fr:
        for g in gens:
            c = tuple(a[g[k]] for k in range(140))
            if c not in G: G.add(c); nf.append(c)
    fr = nf
G = sorted(G); print("group", len(G))
Pre = fmpq_mat(pre_)                         # 16 x 64
out = []; bad = 0
for g in G:
    Pg = fmpq_mat([P140[g[k]] for k in range(140)])   # rows permuted: pe'[k] = pe[g[k]]
    # x' with P x' = Pg x  ->  x' = PL Pg x ; as row vectors: x'^T = x^T (PL Pg)^T
    Mx = (PL * Pg).transpose()               # 64 x 64 acting on row vectors x
    assert P * (PL * Pg) == Pg, "not a lattice automorphism"
    A = Pre * Mx * Binv                     # 16 x 64 coefficients in basis [pre; S]
    Az = [[A[i, j] for j in range(16)] for i in range(16)]
    if any(A[i, j].q != 1 for i in range(16) for j in range(16)): bad += 1
    out.append([[int(v.p) if v.q == 1 else str(v) for v in r] for r in Az])
print("non-integral A_g:", bad)
json.dump({"d": int(args[0]), "A": out, "perms": [list(g) for g in G]}, open(f"symz_d{args[0]}.json", "w"))
