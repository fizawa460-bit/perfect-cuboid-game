#!/usr/bin/env python3
"""32R-60 split enumeration driver (research prototype, floating Fincke-Pohst with margins; exact recheck of all x).
usage: python split_run.py d [compare-file]
  y-stage : C program yenum (rank-15 Fincke-Pohst over Λ with K.y = d, y^2 >= -d/2, plus b_q >= 0 filter)
  m-stage : C program msearch (parity coset + packing constraints + Σ m^2 bound)
  output  : classes in the inventory of degree d (same slice rules as the certified runs), written to split_d{d}.json
y^2 >= -d/2 is justified: x^2 >= 2g-2-d and e >= 2 max(n1,n2) + 4 - 4g >= d + 4 - 4g (inventory), Σ m^2 >= Σ m = e,
so y^2 = x^2 + Σ m^2 / 2 >= -2 - d + (d + 4)/2 (g = 0) and >= -d + d/2 (g = 1); both = -d/2."""
import sys, json, time, math, subprocess
import numpy as np
args = sys.argv[1:]
sys.argv = ["x"]
exec(open("../scripts/32R-59_split_enum.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0])
WSL = ["wsl.exe", "-d", "Ubuntu", "-u", "root", "--", "bash", "-c"]
HERE_WSL = "/mnt/c/Users/fizaw/claudework/stage32_research/split"
d = int(args[0])
y2lo, y2hi = fmpq(-d, 2), fmpq(d * d, 16)
Gm = fmpq_mat([[GL[i][j] for j in range(16)] for i in range(16)])
Kint = [int(v * 2) for v in Kb]
Hr, T = fmpz_mat([[Kint[i]] for i in range(16)]).hnf(transform=True)
T = np.array([[int(T[i, j]) for j in range(16)] for i in range(16)], dtype=object)
s = int(np.array(T[0], dtype=object).dot(np.array(Kint, dtype=object)))
assert (2 * d) % s == 0
z0 = T[0] * ((2 * d) // s)
N = T[1:]
Nq = fmpq_mat([[fmpq(int(v)) for v in r] for r in N.tolist()])
A2 = Nq * Gm * Nq.transpose()
den = 1
for i in range(15):
    for j in range(15):
        den = den * int(A2[i, j].q) // math.gcd(den, int(A2[i, j].q))
Gi = fmpz_mat([[int((-A2[i, j] * den).p) for j in range(15)] for i in range(15)])
_, Tl = Gi.lll(transform=True, rep="gram", gram="exact")
Tl = np.array([[int(Tl[i, j]) for j in range(15)] for i in range(15)], dtype=object)
Nr = Tl.dot(N)
Nrq = fmpq_mat([[fmpq(int(v)) for v in r] for r in Nr.tolist()])
z0q = fmpq_mat([[fmpq(int(v)) for v in z0]])
A2r = Nrq * Gm * Nrq.transpose()
br = Nrq * Gm * z0q.transpose()
c0 = (z0q * Gm * z0q.transpose())[0, 0]
wsr = -(A2r.inv() * br)
ymax = c0 + (br.transpose() * wsr)[0, 0]
R = ymax - y2lo
Mf = np.array([[-float(A2r[i, j]) for j in range(15)] for i in range(15)])
Lc = np.linalg.cholesky(Mf).T
Dg = [Lc[i, i] ** 2 for i in range(15)]
Uu = [[Lc[i, j] / Lc[i, i] for j in range(15)] for i in range(15)]
cen = [float(wsr[i, 0]) for i in range(15)]
pre64 = np.array(pre, dtype=np.int64)
Bmat = 2 * Pq + MU.dot(Pm)                       # bq = Bmat . xt  (92 x 64)
xt0 = np.array([int(v) for v in z0], dtype=np.int64).dot(pre64)
XTi = np.array([[int(v) for v in r] for r in Nr.tolist()], dtype=np.int64).dot(pre64)    # 15 x 64
bq0 = Bmat.dot(xt0); BQi = XTi.dot(Bmat.T)
inp = [f"15 {Bmat.shape[0]} {float(R) * (1 + 1e-9) + 1e-9!r}", " ".join(repr(float(v)) for v in Dg)]
inp += [" ".join(repr(float(v)) for v in row) for row in Uu]
inp.append(" ".join(repr(float(v)) for v in cen))
inp.append(" ".join(map(str, bq0)))
inp += [" ".join(map(str, r)) for r in BQi]
open(f"y{d}_in.txt", "w", newline="\n").write("\n".join(inp) + "\n")
t0 = time.time()
p = subprocess.run(WSL + [f"/root/yenum < {HERE_WSL}/y{d}_in.txt > {HERE_WSL}/y{d}_out.txt"], capture_output=True, text=True)
print("y-stage:", p.stderr.strip(), f"{time.time() - t0:.1f}s", flush=True)
W = np.loadtxt(f"y{d}_out.txt", dtype=np.int64, ndmin=2) if open(f"y{d}_out.txt").read().strip() else np.zeros((0, 15), dtype=np.int64)
# exact y^2 for the survivors
Zs = np.array([int(v) for v in z0], dtype=np.int64)[None, :] + W.dot(np.array([[int(v) for v in r] for r in Nr.tolist()], dtype=np.int64))
G4 = np.array([[int((GL[i][j] * 4).p) for j in range(16)] for i in range(16)], dtype=object)   # 4*Gram integer?
assert all((GL[i][j] * 4).q == 1 for i in range(16) for j in range(16))
keep, Y2x4 = [], []
for k in range(len(Zs)):
    z = [int(v) for v in Zs[k]]
    y4 = sum(G4[i][j] * z[i] * z[j] for i in range(16) for j in range(16))   # 4 y^2
    if 4 * y2lo <= y4 <= 4 * y2hi:
        keep.append(k); Y2x4.append(int(y4))
Zs = Zs[keep]
print("y in exact range:", len(Zs), flush=True)
XT = Zs.dot(pre64); MTs = XT.dot(Pm.T); BQs = XT.dot(Bmat.T)
assert (BQs >= 0).all()
# m-stage input
rows_D = [[int(v) % 2 for v in s] for s in satm]
Rr = []
for r in rows_D:
    r = r[:]
    for (piv, rr) in Rr:
        if r[piv]: r = [a ^ b for a, b in zip(r, rr)]
    if any(r):
        piv = r.index(1)
        Rr = [(pp, [a ^ b for a, b in zip(q, r)] if q[piv] else q) for pp, q in Rr]
        Rr.append((piv, r))
c2min = -2 - d
lines = [f"{MU.shape[0]} {len(Rr)}"] + [" ".join(map(str, MU[q])) for q in range(MU.shape[0])]
lines.append(" ".join(str(pp) for pp, _ in Rr)); lines += [" ".join(map(str, r)) for _, r in Rr]
for i in range(len(Zs)):
    s2max = (2 * Y2x4[i] - 4 * c2min) // 4 if False else int(math.floor((Y2x4[i] / 4 - c2min) * 2 + 1e-9))
    lines.append(f"{i} {s2max}"); lines.append(" ".join(map(str, MTs[i]))); lines.append(" ".join(map(str, BQs[i])))
open(f"m{d}_in.txt", "w", newline="\n").write("\n".join(lines) + "\n")
t0 = time.time()
p = subprocess.run(WSL + [f"/root/msearch < {HERE_WSL}/m{d}_in.txt > {HERE_WSL}/m{d}_out.txt"], capture_output=True, text=True)
print("m-stage:", p.stderr.strip(), f"{time.time() - t0:.1f}s", flush=True)
S = np.array([[int(v) for v in s] for s in sat], dtype=np.int64)
SMinv = fmpq_mat([[fmpq(int(v)) for v in r] for r in S.dot(Pm.T).tolist()]).inv()
SMinv_np = np.array([[float(SMinv[i, j]) for j in range(48)] for i in range(48)])
found = set()
for line in open(f"m{d}_out.txt"):
    a = list(map(int, line.split()))
    i, m = a[0], np.array(a[1:], dtype=np.int64)
    coef = (m - MTs[i]).dot(SMinv_np); ci = np.rint(coef).astype(np.int64)
    assert np.abs(coef - ci).max() < 1e-6
    found.add(tuple(int(v) for v in XT[i] + ci.dot(S)))
Gn64 = np.array(L.D["Gn"], dtype=np.int64)
F1 = np.array([int(v) for v in L.D["F1row"]], dtype=np.int64)
exc = np.array([int(v) for v in L.D["exc"]], dtype=np.int64)
P140 = np.array([[int(v) for v in L.D["Pn"][k]] for k in range(140)], dtype=np.int64)
degv = np.array([int(v) for v in L.D["deg"]], dtype=np.int64)
def in_inventory(x):
    x = np.array(x, dtype=np.int64)
    if int(degv.dot(x)) != d or (P140.dot(x) < 0).any(): return False
    n1, e, c2 = int(F1.dot(x)), int(exc.dot(x)), int(x.dot(Gn64).dot(x))
    n2 = d - n1; M = max(n1, n2); mm = min(n1, n2)
    if n1 < 1 or n2 < 1: return False
    if 2 * M + 4 <= e <= 6 * mm: return c2 >= -2 - d
    if 2 * M <= e <= min(6 * mm, 2 * M + 3): return c2 >= -d
    return False
inv = sorted(x for x in found if in_inventory(x))
print(f"d={d}: distinct x {len(found)}, in inventory {len(inv)}")
json.dump({"d": d, "classes": [list(x) for x in inv]}, open(f"split_d{d}.json", "w"))
if len(args) > 1:
    known = {tuple(x) for x in json.load(open(args[1]))["classes"]}
    print("compare: known", len(known), " common", len(known & set(inv)), " new", len(set(inv) - known), " missing", len(known - set(inv)))
