#!/usr/bin/env python3
"""32R-65 split enumeration with in-C reduction to geometric orbit representatives (no big files).
usage: python split_reps.py d nshards
(header of the 32R-60 split enumeration driver follows) (research prototype, floating Fincke-Pohst with margins; exact recheck of all x).
usage: python split_run.py d [compare-file]
  y-stage : C program yenum (rank-15 Fincke-Pohst over Λ with K.y = d, y^2 >= -d/2, plus b_q >= 0 filter)
  m-stage : C program msearch (parity coset + packing constraints + Σ m^2 bound)
  output  : classes in the inventory of degree d (same slice rules as the certified runs), written to split_d{d}.json
y^2 >= -d/2 is justified: x^2 >= 2g-2-d and e >= 2 max(n1,n2) + 4 - 4g >= d + 4 - 4g (inventory), Σ m^2 >= Σ m = e,
so y^2 = x^2 + Σ m^2 / 2 >= -2 - d + (d + 4)/2 (g = 0) and >= -d + d/2 (g = 1); both = -d/2."""
import sys, json, time, math, subprocess, re, os
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
NSH = int(args[1]) if len(args) > 1 else 12
S = np.array([[int(v) for v in s_] for s_ in sat], dtype=np.int64)
SMq = fmpq_mat([[fmpq(int(v)) for v in r] for r in S.dot(Pm.T).tolist()]).inv()
Dden = 1
for i in range(48):
    for j in range(48):
        Dden = Dden * int(SMq[i, j].q) // math.gcd(Dden, int(SMq[i, j].q))
SMD = [[int((SMq[i, j] * Dden).p) for j in range(48)] for i in range(48)]
Gn64 = np.array(L.D["Gn"], dtype=np.int64)
F1 = np.array([int(v) for v in L.D["F1row"]], dtype=np.int64)
exc = np.array([int(v) for v in L.D["exc"]], dtype=np.int64)
P140 = np.array([[int(v) for v in L.D["Pn"][k]] for k in range(140)], dtype=np.int64)
degv = np.array([int(v) for v in L.D["deg"]], dtype=np.int64)
gens = [tuple(p) for p in json.load(open("../stoll/geo_perms.json"))["perms"]]
G = {tuple(range(140))}; frontier = list(G)
while frontier:
    nf = []
    for a in frontier:
        for g in gens:
            c = tuple(a[g[k]] for k in range(140))
            if c not in G: G.add(c); nf.append(c)
    frontier = nf
G = sorted(G)
print("geometric group order", len(G), flush=True)
ext = ["1", str(d), " ".join(map(str, xt0))] + [" ".join(map(str, r)) for r in XTi]
ext += [" ".join(map(str, r)) for r in Pm.astype(np.int64)] + [str(Dden)] + [" ".join(map(str, r)) for r in SMD]
ext += [" ".join(map(str, r)) for r in S] + [" ".join(map(str, r)) for r in P140]
ext += [" ".join(map(str, degv)), " ".join(map(str, F1)), " ".join(map(str, exc))] + [" ".join(map(str, r)) for r in Gn64]
ext += [str(len(G))] + [" ".join(map(str, p)) for p in G]
for sh in range(NSH):
    NLc = chr(10)
    open(f"r{d}_in_{sh}.txt", "w", newline=NLc).write(base + f"{sh} {NSH}" + NLc + NLc.join(ext) + NLc)
if os.environ.get("SPLIT_PREP_ONLY"): print("inputs written", NSH); sys.exit(0)
t0 = time.time()
UBP = "SPLIT_UB=1 " if os.environ.get("SPLIT_UB") else ""
TAG = "_ub" if UBP else ""
# 32R-68e: write shard outputs on the WSL native filesystem (writes to /mnt/c lost chunks under WSL timeouts at
# d = 18), then copy, and check every shard's line count against the reps count it reports.
LOC = "/root/splitout"
subprocess.run(WSL + [f"mkdir -p {LOC}"], check=True)
procs = [subprocess.Popen(WSL + [UBP + os.environ.get("SPLIT_BIN", "/root/splitenum") + f" < {HERE_WSL}/r{d}_in_{sh}.txt > {LOC}/r{d}{TAG}_out_{sh}.txt"], stderr=subprocess.PIPE, text=True) for sh in range(NSH)]
tot_inv, nrep_sh = 0, []
for p in procs:
    err = p.communicate()[1]
    print("shard:", err.strip(), flush=True)
    mm_ = re.search(r"inventory (\d+) reps (\d+)", err); tot_inv += int(mm_.group(1)); nrep_sh.append(int(mm_.group(2)))
    assert p.returncode == 0, "shard failed"
print(f"stream stage {time.time() - t0:.1f}s", flush=True)
for sh in range(NSH):
    r = subprocess.run(WSL + [f"wc -l < {LOC}/r{d}{TAG}_out_{sh}.txt"], capture_output=True, text=True, check=True)
    assert int(r.stdout.strip()) == nrep_sh[sh], f"shard {sh}: native file has {r.stdout.strip()} lines, reported {nrep_sh[sh]}"
    subprocess.run(WSL + [f"cp {LOC}/r{d}{TAG}_out_{sh}.txt {HERE_WSL}/"], check=True)
    with open(f"r{d}{TAG}_out_{sh}.txt") as fh:
        nl = sum(1 for _ in fh)
    assert nl == nrep_sh[sh], f"shard {sh}: copied file has {nl} lines, reported {nrep_sh[sh]}"
print("shard outputs verified (native and copied line counts = reported reps)", flush=True)
X = np.concatenate([np.loadtxt(f"r{d}{TAG}_out_{sh}.txt", dtype=np.int64, ndmin=2).reshape(-1, 64) for sh in range(NSH)])
Garr = np.array(G, dtype=np.int64)
reps, tot = [], 0
for x in X:
    pe = P140.dot(x)
    orb = len({tuple(pe[g]) for g in Garr})
    tot += orb
    reps.append({"x": [int(v) for v in x], "orbit": orb, "C2": int(x.dot(Gn64).dot(x))})
print(f"d={d}: inventory classes {tot_inv}, geometric reps {len(reps)}, sum of orbit sizes {tot}", flush=True)
assert tot == tot_inv, "orbit sizes do not add up: class set not closed under the group?"
json.dump({"d": d, "classes": tot_inv, "reps": reps}, open(f"reps_d{d}{TAG}.json", "w"))
from collections import Counter
print("geometric reps by C^2:", sorted(Counter(r["C2"] for r in reps).items()))
