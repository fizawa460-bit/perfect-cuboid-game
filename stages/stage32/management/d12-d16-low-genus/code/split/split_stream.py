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

NRi = np.array([[int(v) for v in r] for r in Nr.tolist()], dtype=np.int64)
z0i = np.array([int(v) for v in z0], dtype=np.int64)
G4 = [[int((GL[i][j] * 4).p) for j in range(16)] for i in range(16)]
assert all((GL[i][j] * 4).q == 1 for i in range(16) for j in range(16))
c2min = -2 - d
mt0 = Pm.dot(xt0); MTi = XTi.dot(Pm.T)
rows_D = [[int(v) % 2 for v in s_] for s_ in satm]
Rr = []
for r in rows_D:
    r = r[:]
    for (piv, rr) in Rr:
        if r[piv]: r = [a ^ b for a, b in zip(r, rr)]
    if any(r):
        piv = r.index(1)
        Rr = [(pp, [a ^ b for a, b in zip(q, r)] if q[piv] else q) for pp, q in Rr]
        Rr.append((piv, r))
inp = [f"15 {Bmat.shape[0]} {float(R) * (1 + 1e-9) + 1e-9!r}", " ".join(repr(float(v)) for v in Dg)]
inp += [" ".join(repr(float(v)) for v in row) for row in Uu]
inp.append(" ".join(repr(float(v)) for v in cen))
inp.append(" ".join(map(str, z0i))); inp += [" ".join(map(str, r)) for r in NRi]
inp += [" ".join(map(str, r)) for r in G4]
inp.append(f"{int(4 * y2lo)} {int(math.floor(4 * y2hi))} {c2min}")
inp.append(" ".join(map(str, mt0))); inp += [" ".join(map(str, r)) for r in MTi]
inp.append(" ".join(map(str, bq0))); inp += [" ".join(map(str, r)) for r in BQi]
inp.append(f"{MU.shape[0]} {len(Rr)}"); inp += [" ".join(map(str, MU[q])) for q in range(MU.shape[0])]
inp.append(" ".join(str(pp) for pp, _ in Rr)); inp += [" ".join(map(str, r)) for _, r in Rr]
base = "\n".join(inp) + "\n"
NSH = int(args[2]) if len(args) > 2 else 2
for sh in range(NSH):
    open(f"s{d}_in_{sh}.txt", "w", newline="\n").write(base + f"{sh} {NSH}\n")
t0 = time.time()
procs = [subprocess.Popen(WSL + [f"/root/splitenum < {HERE_WSL}/s{d}_in_{sh}.txt > {HERE_WSL}/s{d}_out_{sh}.txt"], stderr=subprocess.PIPE, text=True) for sh in range(NSH)]
for p in procs:
    err = p.communicate()[1]
    print("shard:", err.strip(), flush=True)
print(f"stream stage {time.time() - t0:.1f}s", flush=True)
S = np.array([[int(v) for v in s_] for s_ in sat], dtype=np.int64)
SMinv = fmpq_mat([[fmpq(int(v)) for v in r] for r in S.dot(Pm.T).tolist()]).inv()
SMinv_np = np.array([[float(SMinv[i, j]) for j in range(48)] for i in range(48)])

# vectorised, chunked reconstruction (memory-light): x = xt0 + w.XTi + round((m - Pm xt) . SMinv) . S
Gn64 = np.array(L.D["Gn"], dtype=np.int64)
F1 = np.array([int(v) for v in L.D["F1row"]], dtype=np.int64)
exc = np.array([int(v) for v in L.D["exc"]], dtype=np.int64)
P140 = np.array([[int(v) for v in L.D["Pn"][k]] for k in range(140)], dtype=np.int64)
degv = np.array([int(v) for v in L.D["deg"]], dtype=np.int64)
def inv_mask(X):
    ok = (X.dot(degv) == d) & (X.dot(P140.T) >= 0).all(axis=1)
    n1 = X.dot(F1); e = X.dot(exc); c2 = np.einsum("ij,jk,ik->i", X, Gn64, X)
    n2 = d - n1; M = np.maximum(n1, n2); mm = np.minimum(n1, n2)
    g0 = (2 * M + 4 <= e) & (e <= 6 * mm) & (c2 >= -2 - d)
    g1 = (2 * M <= e) & (e <= np.minimum(6 * mm, 2 * M + 3)) & (c2 >= -d)
    return ok & (n1 >= 1) & (n2 >= 1) & (g0 | g1)
chunks, nsol = [], 0
for sh in range(NSH):
    buf = []
    def flush(buf):
        A = np.asarray(buf, dtype=np.int64)
        W, Mm = A[:, :15], A[:, 15:]
        XT = xt0[None, :] + W.dot(XTi)
        MTt = XT.dot(Pm.T)
        coef = (Mm - MTt).dot(SMinv_np); ci = np.rint(coef).astype(np.int64)
        assert np.abs(coef - ci).max() < 1e-6
        X = XT + ci.dot(S)
        X = X[inv_mask(X)]
        chunks.append(X.astype(np.int8) if np.abs(X).max(initial=0) < 127 else X)
    with open(f"s{d}_out_{sh}.txt") as fh:
        while True:
            lines = fh.readlines(64 << 20)
            if not lines: break
            A = np.array("".join(lines).replace("|", " ").split(), dtype=np.int64).reshape(len(lines), -1)
            nsol += len(lines)
            flush(A)
# 32R-64: dedupe in int8 via a 64-byte void view (memory-light); JSON only for small d
small = all(c.dtype == np.int8 for c in chunks)
if chunks:
    Xc = np.concatenate([c.astype(np.int8 if small else np.int64) for c in chunks]); chunks = None
    Xc = np.ascontiguousarray(Xc)
    V = np.dtype((np.void, Xc.dtype.itemsize * 64))
    _, ui = np.unique(Xc.view(V).ravel(), return_index=True)
    X = Xc[np.sort(ui)]; Xc = None
else:
    X = np.zeros((0, 64), dtype=np.int8)
print(f"d={d}: solutions {nsol}, distinct classes in inventory {len(X)}", flush=True)
np.save(f"split_d{d}.npy", X)
inv = None
if d <= 12 or len(args) > 1:
    inv = sorted(tuple(int(v) for v in r) for r in X.tolist())
    json.dump({"d": d, "classes": [list(x) for x in inv]}, open(f"split_d{d}.json", "w"))
if len(args) > 1 and args[1] != "none":
    known = {tuple(x) for x in json.load(open(args[1]))["classes"]}
    print("compare: known", len(known), " common", len(known & set(inv)), " new", len(set(inv) - known), " missing", len(known - set(inv)))
